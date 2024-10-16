from django.shortcuts import render


def inicio(request):
    return render(request, 'inicio/index.html')

def about_me(request):
    return render(request, 'inicio/about_me.html')