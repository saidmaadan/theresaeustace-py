from django.shortcuts import render, redirect
from blog.models import Post
from book.models import Book
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-date')[:6]
    books = Book.objects.all().filter(is_available=True).order_by('-created_date')[:20]
    books_ = Book.objects.all().filter(is_new_released=True).order_by('-created_date')[:1]
    context = {
        'posts': posts,
        'books': books,
        'books_': books_,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    posts = Post.objects.all().order_by('-date')[:6]
    context = {
        'posts': posts,
    }
    return render(request, 'pages/about.html', context)


def disclaimer(request):
    context = {}
    return render(request, 'pages/disclaimer.html', context)

def privacy(request):
    context = {}
    return render(request, 'pages/privacy.html', context)

def terms(request):
    posts = Post.objects.all().order_by('-date')[:6]
    context = {
        'posts': posts,
    }
    return render(request, 'pages/terms.html', context)

def contact(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message
        to_email = 'mm@theresaeustace.com'
        
        send_email = EmailMessage(subject, message_body, email, to=[to_email])
        send_email.send()
        
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')
    
    return render(request, 'pages/contact.html')

def thankyou(request):
    context = {}
    return render(request, 'pages/thankyou.html', context)

def already_subscribed(request):
    context = {}
    return render(request, 'pages/already-subscribed.html', context)

