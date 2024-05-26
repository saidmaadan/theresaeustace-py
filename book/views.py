from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, BookGallery, ReviewRating
from collection.models import Collection
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.contrib import messages
from .forms import ReviewForm
from django.urls import reverse

def book(request, total=0, quantity=0, collection_slug=None):
    collections = None
    books = None
    
    # identified_book= get_object_or_404(Book, collection_slug=collection_slug)
      
    if collection_slug != None:
        collections = get_object_or_404(Collection, slug=collection_slug)
        books = Book.objects.filter(collection=collections, is_available=True).order_by("-created_date")
        featured_book = Book.objects.all().filter(collection=collections, is_feature=True).order_by('-created_date')
        paginator = Paginator(books, 12)
        page = request.GET.get('page')
        paged_books = paginator.get_page(page)
        book_count = books.count()
    else:
        books = Book.objects.all().filter(is_available=True).order_by('-created_date')
        featured_book = Book.objects.all().filter(is_feature=True).order_by('-created_date')
        paginator = Paginator(books, 12)
        page = request.GET.get('page')
        paged_books = paginator.get_page(page)
        book_count = books.count()
    
    
    book_gallery = None
    for book in books:
        book_gallery = BookGallery.objects.filter(book_id=book.id)

    context = {
        'books': paged_books,
        'featured_book': featured_book,
        'book_count': book_count,
        'book_gallery': book_gallery,
        
        
    }
    return render(request, 'book/book.html', context)

def book_detail(request, collection_slug, book_slug):
    try:
        single_book = Book.objects.get(collection__slug=collection_slug, slug=book_slug)
        
    except Exception as e:
        raise e
    
    books = Book.objects.all().filter(is_available=True).order_by('-created_date')[:4]
    book_gallery_ = None
    for book in books:
        book_gallery_ = BookGallery.objects.filter(book_id=book.id)
        
    #Get the book gallery
    book_gallery = BookGallery.objects.filter(book_id=single_book.id)
    
    context = {
        'single_book': single_book,
        "single_book_tags": single_book.tags.all(),
        'book_gallery': book_gallery,
        "book_gallery_": book_gallery_,

    }
    return render(request, 'book/book_detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            books = Book.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(title__icontains=keyword))
            book_count = books.count()
    context = {
        'books': books,
        'book_count': book_count,
    }
    return render(request, 'book/book_detail.html', context)

def submit_review(request, book_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        # try:
        #     reviews = ReviewRating.objects.get(user__id=request.user.id, book__id=book_id)
        #     form = ReviewForm(request.POST, instance=reviews)
        #     form.save()
        #     messages.success(request, 'Thank you! Your review has been updated.')
        #     return redirect(url)
        # except ReviewRating.DoesNotExist:
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = ReviewRating()
            data.user_name = form.cleaned_data['user_name']
            data.user_email = form.cleaned_data['user_email']
            data.subject = form.cleaned_data['subject']
            data.rating = form.cleaned_data['rating']
            data.review = form.cleaned_data['review']
            data.ip = request.META.get('REMOTE_ADDR')
            data.book_id = book_id
            
            data.save()
            messages.success(request, 'Thank you! Your review has been submitted.')
            return redirect(url)

