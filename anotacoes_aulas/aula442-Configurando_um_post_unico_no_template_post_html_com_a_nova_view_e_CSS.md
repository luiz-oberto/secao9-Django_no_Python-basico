# Configurando um post único no template post.html com a nova view e CSS
Nesta aula vamos ver como configurar para visualizar um único post ao clicar no mesmo.

Primeiro configuramos nossa view criando um *post*, dessa maneira:

~~~python
def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Exception('Post não existe.')

    context = {
        # 'text': 'Olá Blog',
        'post': found_post,
        'title': found_post['title'] + ' - ',
    }
    
    return render(
        request, 
        'blog/post.html',
        context
    )
~~~
- Essa view vai receber um request (HttpRequest) e o id do post clicado (post_id) que deverá ser um inteiro
- em seguida será criado uma variável que receberá os dados do post que vai ser do tipo *dict*
- Então ele vai iterar os posts e quando achar o post clicado, found_post receberá os dados do post solicitado
- em seguida ele renderizará o post.html com as informções passadas no *context*

Ajustando nosso post.html
~~~django html
<!-- post.html -->
{% extends "global/base.html" %}

{% block texto %} {{ text }} {% endblock texto %} 

{% comment %} aqui estamos puxado o bloco de posts do index.html do app blog. {% endcomment %}
{% block posts %}
<article class="post single-post">
    <header>
        <h1 class="post__title">
            <a href="{% url "blog:post" post.id %}">
                {{ post.title }}
            </a>
        </h1>
    </header>
    <div class="post__body">
        {{ post.body }}
    </div>
</article>
{% endblock posts %}
~~~

Ajustando nossa estilização:
~~~css
@media (min-width: 600px) {
  .content:not(:has(.single-post)) {
    grid-template-columns: repeat(auto-fill, minmax(32rem, 1fr));
  }
}
~~~