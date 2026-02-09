

from django.urls import path

from destination.views import destination_list, destination_detail

app_name = 'destination'
urlpatterns = [
    path('', destination_list, name='list'),
    path('<slug:slug>/', destination_detail, name='detail'),
]