from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("NoiDung", views.NoiDung, name="TenNoiDung"),
    path("DuLieu", views.DuLieu, name="Ten Du Lieu"),
    path("HinhAnh", views.HinhAnh, name="Ten Hinh Anh"),
]