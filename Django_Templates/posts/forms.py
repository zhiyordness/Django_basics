from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory

from posts.mixins import ReadOnlyMixin
from posts.models import Post, Comment
from posts.validators import BadLanguageValidator


class SearchForm(forms.Form):
    query = forms.CharField(
        label="",
        required=False,
        max_length=100,
        validators=[
            BadLanguageValidator("Message Here")
        ]
    )


# class PostForm(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#         error_messages={
#             'max_length': 'message',
#         }
#
#     )
#     content = forms.CharField(
#     )
#
#     author = forms.CharField(
#         max_length=50
#     )
#
#     language = forms.ChoiceField(
#         choices = LanguageChoice.choices,
#     )

class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Your text here'
        #         }
        #     )
        # }

        error_messages = {
            'title': {
                'required': 'The post title is a required field!!!',
                'max_length': 'This is longer than it should be!!!',
                # 'unique': 'This is not unique! ',
                # 'invalid_choice': 'message',
                # 'invalid_list': 'message',
            },
        }

    def clean_author(self):
        author = self.cleaned_data.get('author')

        if not author.isalpha():
            raise ValidationError("The author must contain only letters!")

        return author


    def clean(self):
        cleaned_data = super().clean()
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')

        if title in description:
            raise ValidationError("Title can not be contained in the description!")

        return cleaned_data

    def save(self, commit = True):
        post = super().save(commit=False)

        post.author = post.author.capitalize()

        if commit:
            post.save()

        return post




class PostCreateForm(PostBaseForm):
    ...


class PostEditForm(PostBaseForm):
    ...


class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    ...


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        labels = {
            'author': '',
            'content': '',
        }
        error_messages = {
            'author': {
                'required': 'Please enter your username',
            },
            'content': {
                'required': 'Comment cannot be empty...',
            }
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            # 'style': 'display: none;',
        })
        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add comment',
            'rows': 3,
        })

CommentFormSet = formset_factory(CommentForm, extra=3)