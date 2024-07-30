from django.shortcuts import render
# o Render é feito para renderizar alguns templates


def home(request):
    print('home')
    return render(
        request,
        'home/index.html')