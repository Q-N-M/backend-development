from django.shortcuts import render

def index(request):
    return render(request, 'desktop2.html')