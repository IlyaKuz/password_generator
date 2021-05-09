import random

from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characrters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characrters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characrters.extend('!@#$%^&*()_+')
    if request.GET.get('number'):
        characrters.extend('0123456789')

    length = int(request.GET.get('length', 10))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characrters)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')
