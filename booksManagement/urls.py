from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
]

