from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import session, judge


def index(request):
    if request.method == 'GET':
        return render(request, 'website/home.html')
    elif request.method == 'POST':
        # post = session()
        # post.id = request.POST['id']
        # post.save()

        context = {
            "session_id":request.POST['session_id'] 
        }

        id = request.POST['session_id']
        judge = request.POST['panther_id']
        request.session['session_id'] = request.POST['session_id'] 
        if session.objects.filter(id=id).exists():
            if session.objects.filter(judges=judge):
                return redirect(id+'/judge-login')
            else:
                messages.error(request, "Panther ID isn't authorized for this session")
        else:
            messages.error(request, "This session does not exist")
        return render(request, 'website/home.html')



def admin_index(request):
    if request.method == 'GET':
        return render(request, 'website/administrator.html')


def admin_page(request):
    if request.method == 'GET':
        return render(request, 'website/index.html')


def judge_login(request, session_id):
    if request.method == 'GET':
        return render(request, 'website/judge_login.html')
    elif request.method == 'POST':
        post = judge()
        post.first_name = request.POST['first_name']
        post.last_name = request.POST.get('last_name', '')
        post.panther_id = request.POST['panther_id']
        post.subject = request.POST['subject_choices']
        post.level = request.POST['level_choices']
        post.save()
        Session = session.objects.get(id=session_id)
        Session.judges.add(post)
        return HttpResponse("Logged In :)")
