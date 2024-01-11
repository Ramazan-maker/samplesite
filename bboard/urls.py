from django.urls import path

from .views import (#index,
                    BbIndexView, BbByRubricView, BbMonthView,
                    # by_rubric,
                    BbCreateView, #add_and_save
                    BbDetailView, #BbAddView
                    BbEditView, BbDeleteView,BbRedirectView
                        )


app_name = 'bboard'

urlpatterns = [
    # path('add/', add_and_save, name='add'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BbEditView.as_view(), name='update'),
    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),

    path('add/', BbCreateView.as_view(), name='add'),
    # path('add/', BbAddView.as_view(), name='add'),
    # path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    # path('', index, name='index'),
    path('', BbIndexView.as_view(), name='index'),
    path('year/<int:year>/', BbRedirectView.as_view(), name ='redirect'),
    path('<int:year>/<int:month>/', BbMonthView.as_view(), name='month'),
]
