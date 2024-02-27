import random

from django import template
from django.utils.safestring import mark_safe, SafeText
from django.utils.html import escape
register = template.Library()

# @register.filter(name='cur', is_safe=True)
@register.filter(name='cur')
def currency(value, name='тг.'):
    # if not isinstance(value, SafeText):
    #     value = escape(value)
    return mark_safe(f'<strong>{value: .2f}</strong> {name}')

# register.filter('currency', currency)
#
# @register.filter(expects_localtime=True)
# def datetimefilter(value):
#     pass

# Т Е Г
@register.simple_tag()
def lst(sep, *args):
    # return f'{sep.join(args)} (итого {len(args)})'
    return mark_safe(f'{sep.join(args)} (<strong>итого {len(args)}<strong>)')

# @register.simple_tag(takes_context=True)
# def lst(context, sep, *args):
#     pass

@register.inclusion_tag('tags/ulist.html')
def ulist(*args):
    return {'items': args}
#practice
@register.filter()
def half_cut(value):
    half_lenght = len(value) // 2
    return value[:half_lenght]
@register.filter()
def split_string(value, separator):
    return value.split(separator)

#homework
@register.filter()
def uppercase(value, prefix, suffix):
    return f'{prefix}{value.upper()}{suffix}'

@register.simple_tag()
def random_price(min_price, max_price):

    return random.randint(min_price, max_price)

def random_text(value):
    options = ["Lorem ipsum dolor sit amet", "consectetur adipiscing elit", "sed do eiusmod tempor incididunt", "ut labore et dolore magna aliqua"]
    return random.choice(options)

register.filter('random_text', random_text)