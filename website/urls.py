from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administrator', views.admin_index, name='administrator'),
    path('index', views.admin_page, name='index'),

    path('judgers', views.judgers, name='judgers'),
    path('add_judger', views.add_judger, name='add_judger'),
    path('edit_judger', views.edit_judger, name='edit_judger'),
    path('delete_judger', views.delete_judger, name='delete_judger'),
    path('judging_page', views.judging_page, name='judging_page'),



    path('judges', views.judges, name='judges'),

    path('candidates', views.candidates, name='candidates'),
    path('results', views.results, name='results'),
    path('sessions', views.sessions, name='sessions'),
    path('new_session/<str:session_id>', views.new_session, name='new session'),
    path('finish', views.finish, name='finish voting'),


]
