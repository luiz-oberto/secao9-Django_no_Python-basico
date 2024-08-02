#  Trabalhando com URLs dinâmcas em urls.py e nos templates HTML do Django
Nesta aula vamos aprender a mudar as urls de forma dinâmica sem ter o trabalho de alterar vários arquivos.

Para começar, vamos criar um arquivo html chamada de menu com a seguinte estrutura:
~~~django html
<nav>
    <ul>
        <li>
            <a href="{% url "home:home" %}">Home</a>
        </li>
        <li>
            <a href="{% url "blog:home" %}">Blog</a>
        </li>
        <li>
            <a href="{% url "blog:exemplo" %}">Exemplo</a>
        </li>
    </ul>
</nav>
~~~
nesse aruivo, criamos uma lista de links para navegar nas páginas home, blog e exemplo. Não é  recomendado utilizar links *hardcoded* em casos como esse, para isso nós utilizamos a sintaxe do django, mais especificamente a {% url "" %} que aponta qual página vamos utilizar.

Agora vamos mudar nosso código para que o menu.html saiba qual página deve renderizar. No urls.py podemos acrescenntar a variável *app_name* junto ao parâmetro de path chamado *name*. Ficando desse jeito:
~~~python
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
]
~~~

Da mesma maneira podemos fazer para o blog:
~~~python
from blog import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='home'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
~~~
Dessa forma, sempre que tivermos a necessidade de mudar a URL do nosso site, podemos simplesmente alterar no path o nome do caminho.

- Crtl + shift + r -> Recarrega a página da web sem cache. Pode ser usado para qquando você quer recarregar os arquivos staticos (css)
