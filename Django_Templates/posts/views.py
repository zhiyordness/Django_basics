from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:

    return HttpResponse('Hello World! ')


def dashboard(request: HttpRequest) -> HttpResponse:

    context = {
        'posts': [
        {
            'title': 'THIS IS A TEST POST',
            'content': 'Some description here',
            'author': 'Zhivomir',
            'created_at': datetime.now(),
        },
        {
            'title': 'THIS IS A second TEST POST',
            'content': '**Some**<i> more </i> description here <script>alert("You have been hacked!")</script>',
            'author': 'Molly',
            'created_at': datetime.now(),
        },
        {
            'title': 'THIS IS A third TEST POST',
            'content': '',
            'author': '',
            'created_at': datetime.now(),
        },
        ]
    }

    return render(request, 'dashboard.html', context)

