from django.urls import path, include

from posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-post/', views.add_post, name='add-post'),
    path('<int:pk>/', include([
        path('details/', views.details_post, name='details-post'),
        path('add-post/', views.edit_post, name='add-post'),
        path('delete-post/', views.edit_post, name='delete-post'),

    ])),
]