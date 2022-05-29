import random
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase') == 'on':
        characters.extend(list('ABCDEFGHJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special') == 'on':
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers') == 'on':
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))
    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)
    return render(request, 'generator/password.html', {'password': the_password})


def about(request):
    return render(request, 'generator/about.html')
