from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')
def haha(request):
    return render(request, 'main/haha.html')
