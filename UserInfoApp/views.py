from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def info(request):
    user_agent = get_user_agent(request)
    ip = get_client_ip(request)
    return render(request, 'base.html', {'user_agent': user_agent, 'user_ip': ip})


def get_user_agent(request):
    user_agent = request.META['HTTP_USER_AGENT']
    return user_agent


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    return render(request, 'base.html')
