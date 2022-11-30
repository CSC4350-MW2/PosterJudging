from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from .models import session, judge, submission
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.db.models import F

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
        judge_id = request.POST['panther_id']
        request.session['session_id'] = request.POST['session_id'] 
        if session.objects.filter(id=id).exists():
            if judge.objects.filter(panther_id=judge_id).exists():
                response = redirect('judging_page')
                response.set_cookie('panther_id', judge_id)
                response.set_cookie('session_id', id)
                return response
            else:
                messages.error(request, "Panther ID isn't authorized for this session")
        else:
            messages.error(request, "This session does not exist")
        return render(request, 'website/home.html')

def judging_page(request):
    if not (judge.objects.filter(panther_id=request.COOKIES['panther_id']).exists() and session.objects.filter(id=request.COOKIES['session_id']).exists()):
        return redirect('/')
    else:
        if request.method == 'GET':
            judger = judge.objects.get(panther_id=request.COOKIES['panther_id'])
            submissions = judger.submissions.all()
            context = {'submissions': submissions}
            return render(request, 'website/judging_page.html', context)
        elif request.method == 'POST':
            for x in range(1,7):
                if request.POST.get('id_'+str(x), '') != '':  
                    sub = submission.objects.get(id=x)
                    sub.score = F('score') + int(request.POST['score_'+str(x)])
            return redirect('/finish')
@login_required(login_url="/login")
def admin_index(request):
    if request.method == 'GET':
        return render(request, 'website/administrator.html')


@login_required(login_url="/login")
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

def judge_logout(request):
    logout(request)
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


@login_required(login_url="/login")
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


@login_required(login_url="/login")
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


@login_required(login_url="/login")
def judges(request):
    if request.method == 'GET':
        return render(request, 'website/judges.html')


@login_required(login_url="/login")
def positions(request):
    if request.method == 'GET':
        return render(request, 'website/positions.html')


@login_required(login_url="/login")
def candidates(request):
    if request.method == 'GET':
        return render(request, 'website/candidates.html')


@login_required(login_url="/login")
def results(request):
    if request.method == 'GET':
        submissions = submission.objects.all()
        top_sub = submissions[0]
        for sub in submissions:
            if sub.score > top_sub.score:
                top_sub = sub
                
        context = {"id":top_sub.id, "title":top_sub.title, "score":top_sub.score}
        return render(request, 'website/results.html', context)

@login_required(login_url="/login")
def sessions(request):
    if request.method == 'GET':
        return render(request, 'website/sessions.html')
    elif request.method == 'POST':
        judge_list = judge.objects.all()
        submission_list = submission.objects.all()
        submission_to_judges = len(submission_list)/len(judge_list)
        for x in range(len(submission_list)):
            judge_list[int(x/submission_to_judges)].submissions.add(submission_list[x])
        post = session()
        post.id = get_random_string(8)
        session_id = post.id
        post.save()
        return redirect('new_session/' + session_id)

@login_required(login_url="/login")
def new_session(request, session_id):
    if request.method == 'GET':
        context = {'session_id': session_id}
        return render(request, 'website/new_session.html', context)

def finish(request):
    if request.method == 'GET':
        return render(request, 'website/finish.html')