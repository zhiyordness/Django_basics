from django.urls import path

from review.views import recent_reviews, detail_view

app_name = 'review'
urlpatterns = [
    path('', recent_reviews, name='list'),
    path('<int:pk>/', detail_view, name='detail'),
]