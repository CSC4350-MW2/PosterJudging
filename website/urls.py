from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administrator', views.admin_index, name='administrator'),
    path('<str:session_id>/judge-login', views.judge_login, name='judge-login'),
]