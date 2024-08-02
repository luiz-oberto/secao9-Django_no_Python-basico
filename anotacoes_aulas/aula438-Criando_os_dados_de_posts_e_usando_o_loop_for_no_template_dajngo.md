# Criando os dados de posts (data.py) e usando o loop for no template django
Nesta aula vamos adicionar dados "fictícios" da API JSON Placeholder.

- Primeiro, vamos criar um arquivo chamado *data.py* no qual vamos copiar e colar os dados do link https://jsonplaceholder.typicode.com/posts . Feito isso, vamos configurar nosso context dentro de *views.py* do Blog para receber todos esses dados copiados, deixando dessa forma: 
~~~python
# Começamos imporatando a variável posts de data
from blog.data import posts
from django.shortcuts import render

def blog(request):
    print('blog')

    context = {
        'text': 'Olá Blog',
        # aqui enviamos ao blog todas as informações de data
        'posts': posts,
    }
    
    return render(
        request, 
        'blog/index.html',
        context
    )

~~~

- Agora vamos ajeitar nosso *postblock.html* para receber as informações de títulos e e textos de data, deixando dessa forma:
~~~django html
<article class="post">
    <header>
        <!-- aqui vamos receber o título de cada post -->
        <h2 class="post__title">{{ post.title }}</h2>
    </header>
    <div class="post__body">
        <!-- aqui vamos receber o texto de cada post -->
        {{ post.body }}
    </div>
</article>
~~~

- Para finalizar, vamos até nosso *index.html* e iterar cada post de data
~~~django html
{% extends "global/base.html" %}

{% block texto %} {{ text }} {% endblock texto %} 

{% block posts %}
    <!-- iterando post de posts -->
    {% for post in posts %}
        <!-- exibindo cada post -->
        {% include "global/partials/postblock.html" %}
    {% endfor %}
{% endblock posts %}
~~~

Agora se recarregarmos nosso site vamos obter todos os post na nossa página de blog.