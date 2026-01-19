import random
from django.core.management.base import BaseCommand
from books.models import Book
from reviews.models import Review
from datetime import date

class Command(BaseCommand):
    help = 'Seeds the database with books and reviews'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')

        # Clear existing data
        Review.objects.all().delete()
        Book.objects.all().delete()

        books_data = [
            {
                'title': 'The Lord of the Rings',
                'description': 'A high-fantasy novel by J. R. R. Tolkien.',
                'genre': 'Fantasy',
                'price': 25.99,
                'image_url': 'https://images.booksense.com/images/559/211/9780544211559.jpg',
                'publishing_date': date(1954, 7, 29),
                'isbn': '978054421155',
                'publisher': 'Allen & Unwin'
            },
            {
                'title': 'The Hitchhiker\'s Guide to the Galaxy',
                'description': 'A comedy science fiction series created by Douglas Adams.',
                'genre': 'Science Fiction',
                'price': 15.50,
                'image_url': 'https://m.media-amazon.com/images/I/51+q2M26o-L._SL500_.jpg',
                'publishing_date': date(1979, 10, 12),
                'isbn': '978034539180',
                'publisher': 'Megadodo Publications'
            },
            {
                'title': 'Pride and Prejudice',
                'description': 'A romantic novel of manners written by Jane Austen.',
                'genre': 'Romance',
                'price': 12.00,
                'image_url': 'https://almabooks.com/wp-content/uploads/2016/10/9781847493699.jpg',
                'publishing_date': date(1813, 1, 28),
                'isbn': '978184749369',
                'publisher': 'T. Egerton, Whitehall'
            },
            {
                'title': 'To Kill a Mockingbird',
                'description': 'A novel by Harper Lee published in 1960.',
                'genre': 'Fiction',
                'price': 18.75,
                'image_url': 'https://m.media-amazon.com/images/I/41j-s9fHJcL.jpg',
                'publishing_date': date(1960, 7, 11),
                'isbn': '978044631078',
                'publisher': 'J. B. Lippincott & Co.'
            },
            {
                'title': '1984',
                'description': 'A dystopian social science fiction novel by George Orwell.',
                'genre': 'Dystopian',
                'price': 14.99,
                'image_url': 'https://m.media-amazon.com/images/I/514fVhmk32L.jpg',
                'publishing_date': date(1949, 6, 8),
                'isbn': '978045152493',
                'publisher': 'Secker & Warburg'
            }
        ]

        reviews_data = [
            'A timeless classic that everyone should read.',
            'I couldn\'t put it down! Highly recommended.',
            'A bit slow at the beginning, but the ending is worth it.',
            'An emotional rollercoaster. Beautifully written.',
            'Changed my perspective on life. A must-read.',
            'I have read this book multiple times and it never gets old.',
            'The characters are so well-developed and relatable.',
            'A masterpiece of storytelling.',
            'I recommend this book to all my friends.',
            'This book will stay with you long after you finish it.'
        ]
        
        authors = ['John Doe', 'Jane Smith', 'Peter Jones', 'Mary Williams', 'David Brown']

        for book_data in books_data:
            book = Book.objects.create(**book_data)
            for _ in range(5):
                Review.objects.create(
                    book=book,
                    author=random.choice(authors),
                    body=random.choice(reviews_data),
                    rating=round(random.uniform(3.0, 5.0), 2)
                )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
