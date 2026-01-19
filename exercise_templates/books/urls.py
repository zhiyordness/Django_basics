from django.urls import path

from books import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('books-list/', views.list_all_books, name='list_books'),
    path('book-details/<int:pk>', views.book_details, name='book_details')

]