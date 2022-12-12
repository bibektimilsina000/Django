from django.shortcuts import render

def  startingPage(request):
    print('Starting page')

def post(request):
    print('Post Page')

def postDetail(request,slug):
     print("Post Detail")