from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def blogs(request):
    return render(request, 'blog/bloger.html')
