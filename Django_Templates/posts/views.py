from django.forms.models import modelform_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from posts.forms import SearchForm, PostBaseForm, PostEditForm, PostCreateForm, PostDeleteForm, CommentFormSet
from posts.models import Post


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:

    return HttpResponse('Hello World! ')


def dashboard(request: HttpRequest) -> HttpResponse:

    form = SearchForm(request.GET or None)
    posts = Post.objects.all()

    if request.method == "GET":
        if form.is_valid():
            query = form.cleaned_data['query']
            posts = Post.objects.filter(title__icontains=query)

    context = {
        'posts': posts,
        'form': form,
    }


    return render(request, 'dashboard.html', context)


# def add_post(request: HttpRequest) -> HttpResponse:
#     form = PostForm(request.POST or None)
#
#     if request.method == "POST":
#         if form.is_valid():
#             post = Post(
#                 title=form.cleaned_data['title'],
#                 description = form.cleaned_data['content'],
#                 author= form.cleaned_data['author'],
#                 language=form.cleaned_data['language'],
#             )
#             post.save()
#
#             return redirect('dashboard')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'add_post.html', context)


def add_post(request: HttpRequest) -> HttpResponse:
    form = PostCreateForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save() # ONLY IM MODEL.FORM

            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'add_post.html', context)


def edit_post(request: HttpRequest, pk:int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    # form = PostEditForm(
    #     data=request.POST or None,
    #     instance=post, # MODEL FORMS ONLY
    # )

    if request.user.is_staff:
        PostForm = modelform_factory(
            Post,
            fields=(
                'title',
                'description',
                'author',
                'language',
            )
        )
    else:
        PostForm = modelform_factory(Post, fields=('description',))

    form = PostForm(
        data=request.POST or None,
        instance=post,  # MODEL FORMS ONLY
    )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form':form,
        'post':post,
    }

    return render(request, 'edit_post.html', context)



def details_post(request: HttpRequest, pk:int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    formset = CommentFormSet(request.POST or None)

    if request.method == 'POST':
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return  redirect('details-post', pk=post.pk)

    context = {
        'post': post,
        'formset': formset,
    }

    return render(request, 'post_details.html', context)


