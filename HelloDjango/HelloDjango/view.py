from django.shortcuts import render

def hello(request):
    context         = {}
    context['hello'] = "Hello Django!"
    return render(request,"hello.html",context)
