from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administrator', views.admin_index, name='administrator'),
    path('index', views.admin_page, name='index'),
    path('<str:session_id>/judge-login', views.judge_login, name='judge-login'),

    path('judgers', views.judgers, name='judgers'),
    path('add_judger', views.add_judger, name='add_judger'),
    #path('edit_judger', views.edit_judger, name='edit_judger'),
    path('delete_judger', views.delete_judger, name='delete_judger'),




    path('judges', views.judges, name='judges'),
    path('positions', views.positions, name='positions'),
    path('candidates', views.candidates, name='candidates'),
    path('results', views.results, name='results'),


]
