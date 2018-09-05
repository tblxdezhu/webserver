from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from books.forms import UserForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
    if request.method == 'GET':
        uf = UserForm()
        return render(request, 'page-login.html', {'forms': uf})
    else:
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = request.POST.get("username", '')
            password = request.POST.get("password", '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'page-login.html', {'forms': uf, 'password_is_wrong': True})
        else:
            return render(request, 'page-login.html', {'forms': uf, 'username_is_wrong': True})


@login_required
def index(request):
    return render(request, 'index.html')
