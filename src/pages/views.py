from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kargs):
    # print(args, kargs)
    # print(req.user)
    # return HttpResponse('<h1>This is home page</h1>')
    return render(request, 'home.html', {})

def about_view(request, *args, **kargs):
    # print(args, kargs)
    # print(req.user)
    # return HttpResponse('<h1>This is home page</h1>')
    return render(request, 'about.html', {})

def contact_view(*args, **kargs):
    return HttpResponse('<h1>This is CONTACT page</h1>')
