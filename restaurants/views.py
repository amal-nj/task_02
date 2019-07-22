from django.shortcuts import render

# Create your views here.
def helloWorld(request):
    context={
        "msg": "Hello World!"
    }
    return render(request,'task2.html',context)