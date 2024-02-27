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



