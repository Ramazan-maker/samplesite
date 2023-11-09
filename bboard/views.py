from django.shortcuts import render
from django.http import HttpResponse
from bboard.models import Bb
# Create your views here.
def index(request):
    items_list = 'Список обьявлений\r\n\r\n\n'
    for bb in Bb.objects.order_by('-published'):
        items_list += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(items_list, content_type='text/plain; charset=utf-8')




