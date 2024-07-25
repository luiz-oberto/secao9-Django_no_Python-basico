from django.http import HttpResponse

# from django.shortcuts import render

# Create your views here.
def blog(request):
    print('my_view')
    return HttpResponse('Blog do app')