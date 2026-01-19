from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from reviews.models import Review


# Create your views here.
def recent_reviews(request: HttpRequest) -> HttpResponse:
    reviews = Review.objects.order_by('-created_at')[:5]

    context = {
        'reviews': reviews
    }

    return render(request, 'reviews/recent_reviews.html', context)

