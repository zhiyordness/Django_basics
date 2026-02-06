from pydoc import resolve

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from common.models import Like
from photos.models import Photo


# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    all_photos = Photo.objects.prefetch_related('tagged_pets', 'like_set')

    context = {
        'all_photos': all_photos,
    }
    return render(request, 'common/home-page.html', context)


def like_functionality(request: HttpRequest, photo_pk: int) -> HttpResponse:

    like_object = Like.objects.filter(to_photo_id=photo_pk).first()

    if like_object:
        like_object.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_pk,
        )

    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(f"{referer}#{photo_pk}")

    return redirect(resolve_url('photos:details', photo_pk) + f"#{photo_pk}")

def share_functionality(request: HttpRequest, photo_pk: int) -> HttpResponse:
    absolute_url = request.build_absolute_uri(resolve_url('photos:details', photo_pk))
    copy(absolute_url)

    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(f"{referer}#{photo_pk}")

    return redirect(absolute_url + f"#{photo_pk}")
