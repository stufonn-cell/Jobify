from django.shortcuts import render


# Create your views here.

def lpView(request):
    return render(request,'landing.html')
