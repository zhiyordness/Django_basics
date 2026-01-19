from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from books.models import Book
from reviews.models import Review


# Create your views here.
def landing_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'base.html')


def list_all_books(request: HttpRequest) -> HttpResponse:

    list_of_books = Book.objects.all()

    context = {
        'books': list_of_books
    }


    return render(request, 'books/list_all_books.html', context)

def book_details(request: HttpRequest, pk: int) -> HttpResponse:

    book = Book.objects.get(pk=pk)
    reviews = Review.objects.filter(book__pk=pk).order_by('-created_at')

    context = {
        'book': book,
        'reviews': reviews
    }

    return render(request, 'books/book_details.html', context)