from django.shortcuts import render

def  startingPage(request):
    return render(request,'blog/index.html')

def post(request):
    pass

def postDetail(request,slug):
     pass