from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from .models import session, judge
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_protect


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


# This is for admintrator part
# add new judger to table
global_judger = judge.objects.all()

# main page for judger


def judgers(request):
    global global_judger
    if request.method == 'GET':
        return render(request, 'website/judgers.html', {"data": global_judger})


# addd new judger
global_judger = judge.objects.all()


def add_judger(request):
    global global_judger
    if request.method == 'GET':
        return render(request, 'website/add_judger.html', {"data": global_judger})
    if request.method == 'POST':

        item_judger = judge()
        item_judger.first_name = request.POST['first_name']
        item_judger.last_name = request.POST.get('last_name', '')
        item_judger.panther_id = request.POST['panther_id']
        item_judger.subject = request.POST['subject_choices']
        item_judger.level = request.POST['level_choices']
        list_panther_id = [x.panther_id for x in global_judger]
        if item_judger.panther_id in list_panther_id:
            messages.error(request, "Panther ID already exists")
            return render(request, 'website/judgers.html', {"data": global_judger})
        else:  # add new item
            item_judger.save()
            messages.success(request, "New voter created")
            global_judger = judge.objects.all()

        return render(request, 'website/judgers.html', {"data": global_judger})


# delete judger


@csrf_protect
def delete_judger(request):
    global global_judger

    if request.method == 'GET':
        return render(request, 'website/edit_judger.html', {"data": global_judger})
    if request.method == 'POST':
        id = request.POST['panther_id']
        judge.objects.filter(panther_id=id).delete()
        global_judger = judge.objects.all()

        return render(request, 'website/judgers.html', {"data": global_judger})

# edit judger information


@csrf_protect
def edit_judger(request):
    global global_judger
    if request.method == 'GET':
        return render(request, 'website/edit_judger.html', {"data": global_judger})
    if request.method == 'POST':
        id = request.POST['panther_id']
        judge.objects.filter(panther_id=id).update(first_name=request.POST['first_name'],
                                                   last_name=request.POST['last_name'],
                                                   subject=request.POST['subject_choices'],
                                                   level=request.POST['level_choices'])
        global_judger = judge.objects.all()
        return render(request, 'website/judgers.html', {"data": global_judger})


def judges(request):
    if request.method == 'GET':
        return render(request, 'website/judges.html')


def positions(request):
    if request.method == 'GET':
        return render(request, 'website/positions.html')


def candidates(request):
    if request.method == 'GET':
        return render(request, 'website/candidates.html')


def results(request):
    if request.method == 'GET':
        return render(request, 'website/results.html')
