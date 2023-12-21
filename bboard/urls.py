"""
URL configuration for samplesite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import (index, by_rubric, BbCreateView,
                                      #add, add_save,
                                      add_and_save
                                      )
urlpatterns = [
    # path('add/', BbCreateView.as_view(), name = 'add'),
    # path('add/save/', add_save(), name='add_save'),
    # path('add/', add, name='add'),
    path('add/', add_and_save, name='add'),

    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name = 'index'),

    # path('add/comment/', BbCreateView.as_view(), name='add'),
    #     path('add/', BbCreateView.as_view(), name='add'),
    #     path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    # path('<int:rubric_id>/', by_rubric, vals, name='by_rubric'),
    # path('<slug:slug>/', by_rubric, name='by_rubric'),
    # path('', index, name='index'),
    # re_path(r'^add/$', BbCreateView.as_view(), name='add'),
    # re_path(r'^(?P<rubric_id>[0-9]*)/$', by_rubric, name='by_rubric'),
    # re_path(r'^$', index, name='index'),
]
