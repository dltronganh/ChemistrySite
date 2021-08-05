from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Lecture,LectureCategory,LectureSeries
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.http import HttpResponse

def single_slug(request, single_slug):
    categories = [c.category_slug for c in LectureCategory.objects.all()]
    if single_slug in categories:
      return HttpResponse("{single_slug} is a category")

    lectures = [t.lecture_slug for t in Lecture.objects.all()]
    if single_slug in lectures:
      return HttpResponse("{single_slug} is a Lecture")

    return HttpResponse("'{single_slug}' does not correspond to anything we know of!")
def homepage(request):
    return render(request = request,
                  template_name='main/categories.html',
                  context = {"lectures":Lecture.objects.all})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "New account created: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, "{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})
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
                messages.info(request, "You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

