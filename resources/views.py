from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View
from django.db.models import Q
from .models import Tip


class StartingPageView(ListView):
    template_name = "home.html"
    model = Tip
    ordering = ["-date"]
    context_object_name = "tip"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllTipsView(ListView):
    def get(self, request):
      tips = Tip.objects.all().filter(available=True).order_by("-date")
      featured_tip = Tip.objects.all().filter(feature=True).order_by('-date')[:1]
      tip_ = Tip.objects.all().filter(feature=True).order_by('-date')[:1]
      paginator = Paginator(tips, 6)
      page = request.GET.get('page')
      paged_tips = paginator.get_page(page)
      # tags = Tag.objects.filter(product_id=product.id, status=True)
      context = {
        "tips": paged_tips,
        "featured_tip": featured_tip,
         "tip_": tip_,
        
      }
      return render(request, "resources/tips-page.html", context) 


class SingleTipView(View):
    
    def get(self, request, slug):
        tips = Tip.objects.all().order_by("-date")[:3]
        tip = Tip.objects.get(slug=slug)
        featured_tip = Tip.objects.all().filter(feature=True).order_by('-date')[:3]
        context = {
            "tips": tips,
            "tip": tip,
            "featured_tip": featured_tip,
        }
        return render(request, "resources/tip-detail.html", context)

   
def search_resources(request):
  tips = None
  if 'keyword' in request.GET:
      keyword = request.GET['keyword']
      if keyword:
          tips = Tip.objects.order_by('-date').filter(Q(content__icontains=keyword) | Q(title__icontains=keyword))
          tip_count = tips.count()
  context = {
      'tips': tips,
      # 'post_count': post_count,
  }
  return render(request, 'resources/index.html', context)

