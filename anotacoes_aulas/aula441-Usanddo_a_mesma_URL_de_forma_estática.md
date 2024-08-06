# Usando a mesma URL de forma estática e dinâmica
Basicamente, configurar uma URL específicca ou estática consiste em você dizer nas urls.py como a navegação será feita, por exemplo, até esse posnto da aula eu sei que a URL http://127.0.0.1:8000/blog/posts/ não existe porque não está especificada no nosso arquivo urls.py. Porém, se eu configurar ele da seguinte forma:

~~~python
urlpatterns = [
    # aqui acrescentei post no caminho principal do blog
    path('post/', views.blog, name='home'),
    path('post/<int:id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
~~~
Neste exemplo veremos que quando eu navegar para o *blog* a URL já virá com /post/ incluso no caminho da URL, mudando somente quando clico no título de algum post. Posso deixar as mesmas paths da seguinte maneira:

~~~python
urlpatterns = [
    path('', views.blog, name='home'),
    path('<int:id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
~~~
Agora, o /post/ não entrará masi no caminho de blog/ e a contagem dos IDs será inserido após o blog, ficando desse jeito:

- http://127.0.0.1:8000/blog/4/

- LEMBRE-SE: "Quanto mais coisa eu tenho na minha URL, mais específica ela é."