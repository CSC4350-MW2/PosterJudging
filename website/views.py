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
        return render(request, 'website/administrator.html')


def admin_page(request):
    if request.method == 'GET':
        return render(request, 'website/index.html')


def judge_login(request, session_id):
    if request.method == 'GET':
        Session = session.objects.get(id=session_id)
        return render(request, 'website/judge_login.html')
    elif request.method == 'POST':
        post = judge()
        post.first_name = request.POST['first_name']
        post.last_name = request.POST.get('last_name', '')
        post.panther_id = request.POST['panther_id']
        post.subject = request.POST['subject_choices']
        post.level = request.POST['level_choices']
        post.save()
        return HttpResponse("Logged In :)")


# This is for admintrator part
# add new judger to table
global_judger = judge.objects.all()


def judgers(request):
    global global_judger
    if request.method == 'GET':
        return render(request, 'website/judgers.html', {"data": global_judger})
    if request.method == 'POST':

        item_judger = judge()
        item_judger.first_name = request.POST['first_name']
        item_judger.last_name = request.POST.get('last_name', '')
        item_judger.panther_id = request.POST['panther_id']
        item_judger.subject = request.POST['subject_choices']
        item_judger.level = request.POST['level_choices']
        print(item_judger)
        list_panther_id = [x.panther_id for x in global_judger]
        if item_judger.panther_id in list_panther_id:
            print("already exist")
            return render(request, 'website/judgers.html', {"data": global_judger})
        else:  # add new item
            item_judger.save()
            global_judger = judge.objects.all()

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
        print(item_judger)
        list_panther_id = [x.panther_id for x in global_judger]
        if item_judger.panther_id in list_panther_id:
            print("already exist")
            return render(request, 'website/judgers.html', {"data": global_judger})
        else:  # add new item
            item_judger.save()
            global_judger = judge.objects.all()

        return render(request, 'website/judgers.html', {"data": global_judger})


# delete judger


@csrf_protect
def delete_judger(request):
    global global_judger

    if request.method == 'GET':
        return render(request, 'website/judgers.html', {"data": global_judger})
    if request.method == 'POST':

        id = request.POST['panther_id']
        print(id)
        judge.objects.filter(panther_id=id).delete()
        global_judger = judge.objects.all()

        return render(request, 'website/judgers.html', {"data": global_judger})

# edit judger information


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
