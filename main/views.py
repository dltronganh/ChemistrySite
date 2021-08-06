from django.contrib.auth import forms
from .forms import NewUserForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, PostCategory, PostSeries

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login

from django.shortcuts import render, redirect

from django.contrib import messages

def single_slug(request, single_slug):
    categories = [c.category_slug for c in PostCategory.objects.all()]

    if single_slug in categories:
        matching_series = PostSeries.objects.filter(post_category__category_slug=single_slug)
        series_urls = {}

        for m in matching_series.all():
            part_one = Post.objects.filter(post_series__post_series=m.post_series).earliest("post_published")
            series_urls[m] = part_one.post_slug
            
        return render(request=request,
                      template_name='main/category.html',
                      context={"post_series": matching_series, "part_ones": series_urls})


    post = [t.post_slug for t in Post.objects.all()]
    if single_slug in post:
        this_post = Post.objects.get(post_slug=single_slug)
        post_from_series = Post.objects.filter(post_series__post_series=this_post.post_series).order_by("post_published")
        this_post_idx = list(post_from_series).index(this_post)

        return render(
            request=request,
            template_name='main/post.html',
            context={
                "post":this_post,
                "sidebar": post_from_series,
                "this_post_idx": this_post_idx
            }
        )

    return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")

def homepage(request):
    return render(  
        request= request,
        template_name='main/categories.html',
        context= {'categories': PostCategory.objects.all}
    )

def register(request):
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created. Welcome {username}")
            login(request, user)
            return redirect("main:homepage")
        
        else: #form not valid
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
                # print(form.error_messages[msg])

    form = NewUserForm        
    return render(  
        request=request,
        template_name= "main/register.html",
        context={"form":form}
    )

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome {username}!")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(
        request=request,
        template_name= "main/login.html",
        context={"form":form}
    )

