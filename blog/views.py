from blog.data import posts
from django.shortcuts import render

# Create your views here.
def blog(request):
    print('blog')

    context = {
        'posts': posts,
        'text': 'Olá Blog',
    }
    
    return render(
        request, 
        'blog/index.html',
        context
    )

def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Olá Exemplo',
        'title': 'Essa é uma páginca de exemplo - ',
    }

    return render(
        request,
        'blog/exemplo.html',
        context
    )