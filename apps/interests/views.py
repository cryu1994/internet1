from django.shortcuts import render, redirect
from .models import User, Interest
def index(request):
    return render(request, "index/index.html")

def create(request):
    user = User.objects.create(name=request.POST['name'])
    request.session['user_id'] = user.id
    Interest.objects.create(content=request.POST['content'], user=User.objects.get(id=request.session['user_id']))
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index/users.html', context)

def show(request):
    print Interest.objects.get(user=User.objects.get(id=request.session['user_id']))
    context = {
        "content": Interest.objects.get(user=User.objects.get(id=request.session['user_id']))
    }
    return render(request, "index/show.html", context)
# Create your views here.
