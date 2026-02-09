import random
from django.core.management.base import BaseCommand
from faker import Faker
from books.models import Book, Tag
from reviews.models import Review

class Command(BaseCommand):
    help = 'Seeds the database with books, tags, and reviews'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')

        # Clear existing data
        Review.objects.all().delete()
        Book.objects.all().delete()
        Tag.objects.all().delete()

        faker = Faker()

        # Create tags
        tags = []
        for _ in range(10):
            tag, _ = Tag.objects.get_or_create(name=faker.word())
            tags.append(tag)

        # Create books
        for _ in range(20):
            book = Book.objects.create(
                title=faker.catch_phrase(),
                description=faker.text(),
                genre=random.choice([choice[0] for choice in Book.GenreChoices.choices]),
                price=faker.pydecimal(left_digits=2, right_digits=2, positive=True),
                image_url=faker.image_url(),
                publishing_date=faker.date_this_century(),
                isbn=faker.isbn13().replace('-', ''),
                publisher=faker.company(),
                pages=faker.random_int(min=50, max=1000)
            )
            
            # Add tags to books
            book.tags.set(random.sample(tags, k=random.randint(1, 5)))

            # Create reviews for each book
            for _ in range(random.randint(1, 5)):
                Review.objects.create(
                    book=book,
                    author=faker.name(),
                    body=faker.paragraph(),
                    rating=faker.pydecimal(left_digits=1, right_digits=2, positive=True, min_value=1, max_value=5),
                    is_spoiler=faker.boolean(chance_of_getting_true=25)
                )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))