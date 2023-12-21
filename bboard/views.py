from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template, render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView

from .forms import BbForm
from .models import Bb, Rubric
from django.template import loader

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)
    context = {'bbs': bbs, 'rubrics': rubrics}
    # template = get_template('index.html')
    # return HttpResponse(template.render(context=context, request=request))
    return HttpResponse(
        render_to_string('index.html', context, request)
    )


# def index(request):
#     response = HttpResponse('Здесь будет',
#                             content_type='text/plain; charset= utf-8')
#     response.write(' главная')
#     response.writelines((' страница', ' сайта'))
#     response['keywords'] = 'Python, Django'
#     return response
# def index(request):
#     bbs = Bb.objects.order_by('-published')
#     rubrics = Rubric.objects.filter(bb__isnull= False).distinct()
#     rubrics = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)
#     context = {'bbs': bbs, 'rubrics': rubrics}
#     return render(request, 'index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    #rubrics = Rubric.objects.all()
    rubrics = Rubric.objects.filter(bb__isnull= False).distinct()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics,
               "current_rubric": current_rubric}
    return render(request, 'by_rubric.html', context)

# def add(request):
#     bbf = BbForm()
#     context = {'form': bbf}
#     return render(request, 'create.html', context)
#
# def add_save(request):
#     bbf = BbForm(request.POST)
#
#     if bbf.is_valid():
#         bbf.save()
#         return HttpResponseRedirect(
#             reverse('bboard:by_rubric'),
#             kwargs={'rubric_id':bbf.cleaned_data['rubric'].pk}
#         )
#     else:
#         context = {'form':bbf}
#         return render(request, 'create.html', context)

def add_and_save(request):
    print(request.headers['Accept-Encoding'])
    print(request.headers['accept-Encoding'])
    print(request.headers['accept_Encoding'])
    print(request.headers['Cookie'])
    print(request.resolver_match)
    print(request.body)

    #if request.header.get("x-request-with") == 'XMLHttpRequest':
    if request.method == 'POST':
        bbf = BbForm(request.POST)
        if bbf.is_valid():
            bbf.save()
            return HttpResponseRedirect(
                reverse('bboard:by_rubric',
                kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk})
            )
        else:
            context = {'form': bbf}
            return render(request, 'create.html', context)
    else:
        bbf = BbForm()
        context = {'form': bbf}
        return render(request, 'create.html', context)

class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric'] = Rubric.objects.all()
        return context