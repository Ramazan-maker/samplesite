from django.urls import path

from .views import (index, BbByRubricView,
                    # by_rubric,
                    BbCreateView, #add_and_save
                    BbDetailView
                        )


app_name = 'bboard'

urlpatterns = [
    # path('add/', add_and_save, name='add'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('add/', BbCreateView.as_view(), name='add'),
    # path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),

    path('', index, name='index'),
]
