

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from department.models import Department


# Create your views here.


def index(request: HttpRequest, pk: int) -> HttpResponse:
    # return HttpResponse(f"The type is {type(id)}", content_type='text/plain')
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'index.html', {"department":department})

    # if Department.objects.get(pk=pk):
    #     ...
    # else:
    #     raise Http 404

def redirect_view(request: HttpRequest) -> HttpResponse:
    # return index(request) -> This is terrible because there is no redirect. It only returns the html from index(). The url is not redirected
    # return redirect('http://127.0.0.1:8000/') -> Bad because we hardcode the url
    # return redirect('/') -> Better but not perfect
    return redirect('home', pk = 2)
def slug_view(request: HttpRequest, slug: str) -> HttpResponse:
    return HttpResponse(f"The type is {type(slug)} and the slug is {slug}", content_type='text/plain')


def path_view(request: HttpRequest, path: str) -> HttpResponse:
    return HttpResponse(f"The type is {type(path)} and the slug is {path}", content_type='text/plain')


def uuid_view(request: HttpRequest, uuid: str) -> HttpResponse:
    return HttpResponse(f"The type is {type(uuid)} and the uuid is {uuid}", content_type='text/plain')


def show_archive(request: HttpRequest, archive_year:int):
    return HttpResponse(f"The requested year is {archive_year}")