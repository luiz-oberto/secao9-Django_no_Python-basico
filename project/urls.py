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
from home import views
from blog import views as blog_Views

#   cliente           servidor
# HTTP Resquest <-> HTTP Reponse (é stateless)
# MVT (Model view template) -> a view vai decidir o que vai fazer com os dados  


urlpatterns = [
    # path('nome_do_caminho/', view->)
    path('', views.home),
    path('blog/', blog_Views.blog),
    path('admin/', admin.site.urls),
]
