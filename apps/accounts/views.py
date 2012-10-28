from django.shortcuts import render_to_response
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


@login_required(login_url='/ingresar/')
def user_detail(request):
    ctx = {}
    return render_to_response('accounts/user_detail.html', ctx, RequestContext(request))


def login_user(request):
    if request.method == 'POST':
        form_login = AuthenticationForm(request.POST)
        if form_login.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            access = authenticate(username=username, password=password)
            if access is not None:
                login(request, access)
                return HttpResponseRedirect('/')
            else:
                return render_to_response('accounts/user_login.html', {'form': form_login}, RequestContext(request))
    else:
        form_login = AuthenticationForm()
    return render_to_response('accounts/user_login.html', {'form': form_login}, RequestContext(request))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def register_user(request):
    ctx = {}
    return render_to_response('accounts/user_register.html', ctx, RequestContext(request))
