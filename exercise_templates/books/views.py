
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from books.models import Book
from reviews.models import Review


# Create your views here.
def landing_page(request: HttpRequest) -> HttpResponse:
    latest_books = Book.objects.order_by('-publishing_date')[:3]
    total_books = Book.objects.count()
    latest_book = Book.objects.order_by('-publishing_date').first()

    context = {
        'books': latest_books,
        'total_books': total_books,
        'latest_book': latest_book,
    }

    return render(request, 'books/landing_page.html', context)


def list_all_books(request: HttpRequest) -> HttpResponse:

    books = Book.objects.all()

    context = {
        'books': books,
        'page_title': 'Book Hub',
    }

    return render(request, 'books/list_all_books.html', context)

def book_details(request: HttpRequest, slug: str) -> HttpResponse:

    book = Book.objects.get(slug=slug)
    reviews = Review.objects.filter(book__pk=book.pk).order_by('-created_at')

    context = {
        'book': book,
        'reviews': reviews

    }

    return render(request, 'books/book_details.html', context)

