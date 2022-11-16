from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.method == 'GET':
        return render(request, "templates/home.html")
    elif request.method == 'POST':
        return HttpResponse("Thanks for post request!")