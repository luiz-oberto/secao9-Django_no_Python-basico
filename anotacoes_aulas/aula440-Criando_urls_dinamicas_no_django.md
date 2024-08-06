# Criando urls dinâmicas no Django USL Dispatcher, view e template

Criar URLs dinâmicas nos permite trabalhar com interações que podem ser feita nos nossos sites como clicar em posts de blog que é o que vamos fazer aqui

Para começar, vamos até urls.py de blog e vamos acrescentar uma path que vai nos dizer qual a URL do post com o respectivo *id*, ficando desta forma:

~~~python
urlpatterns = [
    path('', views.blog, name='home'),
    # novo path
    path('post/<int:id>', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
~~~
- importante ressaltar que devemos especificar que o id que será passado na URL **DEVE** ser um inteiro.

- DICA: segue o link para para entender melhor sobre os tipos de caracteres que podemos usar nas URLs https://docs.djangoproject.com/en/5.0/topics/http/urls/

feito isso, vamos criar a nossa view de *post*, ela que vai dizer o que será feita ao navegar para a nossa URL:

~~~python
def post(request, id):
    print('post', id)

    context = {
        'posts': posts,
        # 'text': 'Olá Blog',
    }
    
    return render(
        request, 
        'blog/index.html',
        context
    )
~~~

Por fim, vamos tornar o título dos posts do blog em um link que nos redirecionará para o post/<'int:id>, deixando da seguinte forma:

~~~django html
<article class="post">
    <header>
        <h2 class="post__title">
        <!-- tag *a* acrescentada aqui para tornar os títulos em links -->
            <a href="{% url "blog:post" post.id %}">
                {{ post.title }}
            </a>
        </h2>
    </header>
    <div class="post__body">
        {{ post.body }}
    </div>
</article>
~~~

Pronto, agora qualquer título de post dentro do blog irá nos redirecionar para /post/(id do post).