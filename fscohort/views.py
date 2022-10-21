from django.shortcuts import render


from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Hello. Welcome Back Resul!</>')


def fscohort(request):
    return HttpResponse('<h1>Now, you are in fscohort.</>')


def subfolder(request):
    return HttpResponse('<h1>Now, you are in subfolder.</>')
