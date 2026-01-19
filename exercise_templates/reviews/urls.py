from django.urls import path

from reviews import views

app_name = 'reviews'
urlpatterns = [
    path('reviews/', views.recent_reviews, name='recent_reviews'),
    path('reviews/<int:pk>/', views.review_details, name='review_details'),
]