

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from reviews.models import Review


# Create your views here.
def recent_reviews(request: HttpRequest) -> HttpResponse:
    reviews = Review.objects.order_by('-created_at')[:5]

    context = {
        'reviews': reviews,
        'page_title': 'Recent reviews',
    }

    return render(request, 'reviews/recent_reviews.html', context)


def review_details(request: HttpRequest, pk: int) -> HttpResponse:

    review = get_object_or_404(
        Review.objects.select_related('book'),
        pk=pk
    )

    context = {
        'review': review,
        'page_title': f"{review.author}'s review on {review.book.title}"
    }

    return render(request, 'reviews/review_details.html', context)

