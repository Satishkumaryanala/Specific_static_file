from django.shortcuts import render

# Create your views here.


def sepcific_static(request):
    return render(request,'sepcific_static.html')