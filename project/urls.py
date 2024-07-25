"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# HTTP Resquest <-> HTTP Reponse
# MVT (Model view template) -> a view vai decidir o que vai fazer com os dados

def my_view(request):
    print('posso fazer outras coisas')
    return HttpResponse('Uma mensage para alguém especial')

def meu_blog(request):
    print()
    return HttpResponse('Esta é minha página do meu blog.')

urlpatterns = [
    # path('nome_do_caminho/', view->)
    path('admin/', admin.site.urls),
    path('blog/', my_view),
    path('meu_blog/', meu_blog)
]
