from django import template
from datetime import datetime


register = template.Library()


@register.simple_tag
def current_time(format_str="%d-%m-%Y %H:%M:%S"):
    return datetime.now().strftime(format_str)