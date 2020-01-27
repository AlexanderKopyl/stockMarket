from django.shortcuts import render


def home(request):
    return render(request, 'quotes/home.html', {})


def about(request):
    return render(request, 'quotes/about.html', {})