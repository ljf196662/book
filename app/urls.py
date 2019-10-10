from django.urls import path, re_path
from app import views

urlpatterns = [
    path('books/all/', views.book_all, name="book_all")
]
