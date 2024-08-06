# Exibindo o erro 404 (página não encontrada) com django.http.Http404 (Not Found)
Nesta aula vamos aprender a retornar o erro 404, uma página que não existe.

Para isso basta importarmos o Http404 de Django.http:

~~~python
from django.http import HttpRequest, Http404
~~~

em seguida nós mudamos a Exception dentro da view post por Http404:

~~~python
def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        # Mudando aqui
        raise Http404('Post não existe.')

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

agora se você tentar acessa um post que não existe ele retornará o erro 404.