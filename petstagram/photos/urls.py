from django.urls import path, include

from photos import views

app_name = 'photos'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='list'),
    path('add/', views.photo_add, name='add'),
    path('<int:pk>/', include([
        path('', views.photo_details, name='details'),
        path('edit/', views.photo_edit, name='edit'),
        path('delete/', views.photo_delete, name='delete'),
    ])),

]