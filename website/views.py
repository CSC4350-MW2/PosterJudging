from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import session

def index(request):
    if request.method == 'GET':
        return render(request, "website/home.html")
    elif request.method == 'POST':
        post = session()
        post.id = request.POST['id']
        post.save()

        context = {
            "session_id": post.id
        }

        request.session['session_id'] = post.id
        return redirect(post.id+'/judge-login')

def admin_index(request):
    if request.method == 'GET':
        return render(request, "website/administrator.html")

def judge_login(request, session_id):
    Session = session.objects.get(id=session_id)
    return render(request, "website/judge_login.html")