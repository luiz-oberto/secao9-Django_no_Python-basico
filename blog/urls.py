from blog import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='home'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
