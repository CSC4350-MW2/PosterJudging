from django.shortcuts import render
from django.http import HttpResponse
from .models import session

def index(request):
    if request.method == 'GET':
        return render(request, "website/home.html")
    elif request.method == 'POST':
        post = session()
        post.id = request.POST['id']
        return HttpResponse(post.id)

def admin_index(request):
    if request.method == 'GET':
        return render(request, "website/administrator.html")