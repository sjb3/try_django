from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kargs):
    # print(args, kargs)
    # print(req.user)
    # return HttpResponse('<h1>This is home page</h1>')
    return render(request, 'home.html', {})

def about_view(request, *args, **kargs):
    my_context = {
        'title'  : 'About me!',
        'This_is_true': True,
        'my_num' : 1234,
        'my_fav' : [123, 'cat', '1B$', 'FOOD!'],
        'my_html': '<h1>Hello World</h1>',
    }
    return render(request, 'about.html', my_context)

def contact_view(*args, **kargs):
    return HttpResponse('<h1>This is CONTACT page</h1>')
