import json
import os
from datetime import datetime

from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import StreamingHttpResponse, FileResponse, JsonResponse
from django.template.loader import render_to_string
from django.urls import resolve
from django.views.decorators.gzip import gzip_page
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe

from bboard.models import Rubric, Bb
from samplesite.settings import BASE_DIR
from testapp.forms import ImgForm
from testapp.models import Img
from django.core.mail import EmailMessage, get_connection, EmailMultiAlternatives, send_mail, send_mass_mail, \
    mail_admins

FILES_ROOT = os.path.join(BASE_DIR, 'files')


# def index(request):
#     resp_content = ('Здесь будет', ' главная', ' страница', ' сайта')
#     resp = StreamingHttpResponse(resp_content, content_type='text/plain; charset=utf-8')
#     return resp

# def index(request):
#     # file_name = r'static/bg.jpg'
#     file_name = r'static/lesson_15.zip'
#     return FileResponse(open(file_name, 'rb'),
#                         as_attachment=True,
#                         filename='file.zip')

# def index(request):
#     data = {'title': 'Мотоцикл', 'content': 'Старый', 'price': 10000.0}
#     return JsonResponse(data, encoder=DjangoJSONEncoder)

# def index(request):
#     context = {'title': 'Тестовая страница'}
#     return render(request, 'test.html', context)

# def index(request):
#     r = get_object_or_404(Rubric, name="Транспорт")
#     return redirect('bboard:by_rubric', rubric_id=r.id)

# @require_http_methods(['GET', 'POST'])
# @require_GET()
# @require_POST()
# @require_safe()  # GET, HEAD
# @gzip_page()
# def index(request):
#     rubric = get_object_or_404(Rubric, name="Транспорт")
#     bbs = get_list_or_404(Bb, rubric=rubric)
#
#     res = resolve('/2/')
#
#     context = {'title': 'Тестовая страница', 'bbs': bbs, 'res': res}
#
#     return render(request, 'test.html', context)


def index(request):
    imgs = []

    for entry in os.scandir(FILES_ROOT):
        imgs.append(os.path.basename(entry))

    context = {'title': 'Тестовая страница', 'imgs': imgs}

    return render(request, 'testapp/index.html', context)


def get(request, filename):
    fn = os.path.join(FILES_ROOT, filename)
    return FileResponse(open(fn, 'rb'),
                        content_type='application/octet-stream')


def add(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['img']
            # fn = '%s%s' % (datetime.now().timestamp(),
            #                os.path.splitext(uploaded_file.name)[1])
            fn = f'{datetime.now().timestamp()}{os.path.splitext(uploaded_file.name)[1]}'
            fn = os.path.join(FILES_ROOT, fn)

            with open(fn, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            return redirect('test:add')
    else:
        form = ImgForm()
    context = {'form': form}
    return render(request, 'testapp/add.html', context)


def delete(request, pk):
    img = Img.objects.get(pk=pk)
    img.img.delete()
    img.delete()
    return redirect('test:add')


# def hide_comment(request):
#     if request.user.has_perm('testapp.hide_comments'):
#         pass


def test_email(request):
    # em = EmailMessage(subject = 'Test Email', body='Test', to=['user@supersite.kz'])
    # em = EmailMessage(subject = 'Ваш новый пароль', body='Ваш новый пароль находится во вложении', attachments=[('password.txt', '12345678', 'text/plain')], to=['user@supersite.kz'])

    # em = EmailMessage(subject = 'Запрошенный вами файл',
    #                   body='Получите файл',
    #
    #                   to=['user@supersite.kz'])
    # em.attach_file(os.path.join(BASE_DIR, 'tmp', 'file.txt'))
    # context = {'user': 'Vasya Pypkin'}
    # s = render_to_string('email/letter.txt', context)
    # em = EmailMessage(subject='Оповешение', body=s, to=['vpupkin@supersite.kz'], headers={'Content-Type': 'text/plain; charset=UTF-8'})
    # em.send()

    # con = get_connection()
    # con.open()
    # em1 = EmailMessage(subject='Test1',body='Test1',to=['user1@supersite.kz'], connection=con)
    # em1.send()
    # em2 = EmailMessage(subject='Test2',body='Test2',to=['user2@supersite.kz'], connection=con)
    # em2.send()
    # em3 = EmailMessage(subject='Test3',body='Test3',to=['user3@supersite.kz'], connection=con)
    # em3.send()
    # em4 = EmailMessage(subject='Test4',body='Test4',to=['user4@supersite.kz'], connection=con)
    # em4.send()
    # em5 = EmailMessage(subject='Test5',body='Test5',to=['user5@supersite.kz'], connection=con)
    # em5.send()
    # con.close()

    # con = get_connection()
    # con.open()
    # em1 = EmailMessage(subject='Test1', body='Test1', to=['user1@supersite.kz'])
    # em2 = EmailMessage(subject='Test2', body='Test2', to=['user2@supersite.kz'])
    # em3 = EmailMessage(subject='Test3', body='Test3', to=['user3@supersite.kz'])
    # em4 = EmailMessage(subject='Test4', body='Test4', to=['user4@supersite.kz'])
    # em5 = EmailMessage(subject='Test5', body='Test5', to=['user5@supersite.kz'])
    # con.send_messages([em1, em2, em3, em4, em5])
    # con.close()

    # em = EmailMultiAlternatives(subject='Test', body='Test', to=['sartayevramazan@gmail.com'])
    # em.attach_alternative('<h1>Test</h1>', 'text/html')
    # em.send()

    # send_mail('Test', 'Test111', 'webmaster@supersite.kz', ['user@othersite.kz'], html_message='<h1>Test</h1>')

    # msg1 = ('Подписка', 'Подтвердите подписку','webmaster@supersite.kz', ['user@othersite.kz', 'user@othersite.kz'])
    # msg2 = ('Подписка', 'Подтвердите подписку','webmaster@supersite.kz', ['user2@othersite.kz', 'user2@othersite.kz'])
    # send_mass_mail((msg1, msg2))

    # user = User.objects.get(username='admin')
    # user.email_user('Подьем!', 'Admin', 'Не спи', fail_silently=True)

    mail_admins('Подьем!', 'Admin', 'Не спи' , html_message='<strong>Привет</strong>')
    return redirect('test:index')