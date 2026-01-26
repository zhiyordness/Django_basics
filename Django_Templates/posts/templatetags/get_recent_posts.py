from itertools import count

from django import template
from django.template import TemplateSyntaxError

from posts.models import Post

register = template.Library()


class RecentPostsNode(template.Node):
    def __init__(self, posts_count: int, context_varname: str ) -> None:
        self.posts_count = int(posts_count)
        self.context_varname = context_varname

    def render(self, context) -> str:

        recent_post = Post.objects.order_by('-created_at')[:self.posts_count]
        context[self.context_varname] = recent_post

        return ''


@register.tag
def get_recent_posts(parser, token):
    try:
        tag_name, count, varname = token.split_contents()
        # '{% get_recent_posts 5 recent_posts %}' -> [get_recent_posts, 5, recent_posts]

    except ValueError:
        raise TemplateSyntaxError(
            'The get_recent_posts tag expects only three arguments'
        )

    return RecentPostsNode(count, varname)