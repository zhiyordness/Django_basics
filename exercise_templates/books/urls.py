

from django.urls import path, include

from books import views


app_name='books'
books_urls = [
        path('list/',views.list_all_books, name='list_books' ),
        path('/<slug:slug>/', views.book_details, name='book_details')
    ]
urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('books/', include(books_urls)),
]