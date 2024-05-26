from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from category.models import Category
from django.views.generic import ListView
from django.views import View
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

from .models import Post
from .forms import CommentForm

# Create your views here.

class AllPostsView(ListView):
    # template_name = "blog/posts.html"
    # model = Post
    # ordering = ["-date"]
    # context_object_name = "all_posts"

    def get(self, request, category_slug=None):
        categories = None
        posts = None
    
        if category_slug != None:
            categories = get_object_or_404(Category, slug=category_slug)
            posts = Post.objects.filter(category=categories, is_available=True).order_by('-date')
            side_posts = Post.objects.filter(category=categories, is_available=True).order_by('-date')[:4]
            featured_post = Post.objects.all().filter(is_home_feature=True).order_by('-date')[:1]
            post_ = Post.objects.all().filter(is_home_feature=True).order_by('-date')[:4]
            paginator = Paginator(posts, 6)
            page = request.GET.get('page')
            paged_posts = paginator.get_page(page)
            post_count = posts.count()
           
        else:
            posts = Post.objects.all().filter(is_available=True).order_by('-date')
            side_posts = Post.objects.filter(category=categories, is_available=True).order_by('-date')[:4]
            featured_post = Post.objects.all().filter(is_feature=True).order_by('-date')[:1]
            post_ = Post.objects.all().filter(is_home_feature=True).order_by('-date')[:4]
            paginator = Paginator(posts, 6)
            page = request.GET.get('page')
            paged_posts = paginator.get_page(page)
            post_count = posts.count()
            
            

        
        context = {
            'posts': paged_posts,
            'featured_post': featured_post,
            'post_count': post_count,
            'post_': post_,
            'side_posts': side_posts,
            
            
        }
        return render(request, 'blog/posts.html', context)



class SinglePostView(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
          is_saved_for_later = post_id in stored_posts
        else:
          is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, category_slug, post_slug):
        posts = Post.objects.all().filter(is_available=True).order_by('-date')[:4]
        post = Post.objects.get(category__slug=category_slug, slug=post_slug)

        context = {
            "posts": posts,
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id),
            
        }
        return render(request, "blog/post.html", context)

    def post(self, request, category_slug, post_slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(category__slug=category_slug, slug=post_slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail", args=[post_slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post.html", context)

    

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
          posts = Post.objects.filter(id__in=stored_posts)
          context["posts"] = posts
          context["has_posts"] = True

        return render(request, "blog/bookmarked-posts.html", context)


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
          stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
          stored_posts.append(post_id)
        else:
          stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        
        return HttpResponseRedirect("/read-later")


# class SearchView(View):
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            posts = Post.objects.order_by('-date').filter(Q(content__icontains=keyword) | Q(title__icontains=keyword))
            post_count = posts.count()
    context = {
        'posts': posts,
        'post_count': post_count,
    }
    return render(request, 'blog/posts.html', context)


