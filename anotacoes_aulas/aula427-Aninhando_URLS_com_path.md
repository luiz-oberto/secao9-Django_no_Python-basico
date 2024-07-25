# Aninhando URLS com path, include e urls.py dos apps do Django
Digamos que criamos um blog com as sequintes URLs

- http://127.0.0.1:8000/
- http://127.0.0.1:8000
- http://127.0.0.1:8000/blog
- http://127.0.0.1:8000/blog/
- http://127.0.0.1:8000/blog/articles/
- http://127.0.0.1:8000/blog/articles/comments
- http://127.0.0.1:8000/blog/articles/categories

Para facilitar o uso dessas URLs, podemos aninhar todas elas da seguinte forma:

1. Criamos dentro da pasta dos apps um arquivo chamado urls.py em cada

2. Colocaremos o seguinte código:
~~~python
# Código do arquivo urls.py home
# o mesmo serve para blog
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
]
~~~

3. Voltando para o arquivo urls.py do nosso projeto nós podemos modificar acrescentando o método *include* que vai fazer a função de aninhar nossas URLs, ficando o códgo dessa maneira:

~~~python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]

~~~
### Desde ponto em diante já conseguimos acessar novamente nossas views, porém, agora quero acrescentar um novo caminho ao *blog*.
Para fazermos isso, podemos fazer da seguinte maneira:

1. Vamos até o arquivo urls.py do app blog e acrescentamos a path 'exemplo/' ao urlpatterns: 

~~~python
    path('exemplo/', views.exemplo),
~~~

2. Feito isso vamos criar nossa view de 'exemplo' que a url vai chamar ao ser feita a requisição, ficando desse jeito:

~~~python
def exemplo(request):
    print('exemplo')
    return HttpResponse('Exemplo do Blog do app 1')
~~~

3. A partir de agora , se quisermos acessar a view 'exemplo' é necessário que a URL seja escrita da seguinte maneira:
- http://127.0.0.1:8000/blog/exemplo/


Desse jeito temos uma URL aninhada para blog.