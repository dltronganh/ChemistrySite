from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'base_hello/home.html')

def NoiDung(request):
     return render(request, 'base_hello/noidung.html')

def DuLieu(request):
     return render(request, 'base_hello/dulieu.html')

def HinhAnh(request):
     return render(request, 'base_hello/hinhanh.html')