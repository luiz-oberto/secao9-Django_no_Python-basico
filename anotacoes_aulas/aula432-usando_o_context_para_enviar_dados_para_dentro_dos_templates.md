# Usando context para enviar dados para dentro dos templates do Django
Na função *render* que encontramos nas views, podemos ver diversos parâmetros que podemos utilizar, nesta aula vamos aprender a utilizar o parâmnetro *context*.

~~~~python
def render(
    request: HttpRequest,
    template_name: str | Sequence[str],
    context: Mapping[str, Any] | None = ..., #<-- esse carinha aqui
    content_type: str | None = ...,
    status: int | None = ...,
    using: str | None = ...,
) -> HttpResponse: ...
~~~~

O context é utilizado em conjunto com o Django HTML para passsar textos para serem exibidos em seu site. Vamos pegar uma das views de blog, nesse caso a view *exemplo*:

~~~~python
def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Olá Exemplo',
        'title': 'Essa é uma páginca de exemplo - ',
    }

    return render(
        request,
        'blog/exemplo.html',
        context
    )
~~~~
- Note que passamos uma variável que recebe um dicionário e dentro dela tem as chaves 'text' e 'title'. após isso passamos dentro da função render o nosso dicionário. Feito isso vamos alterar nosso arquivo exemplo.html as seguintes linhas deixando desse jeito:

~~~~django html
{% extends "global/base.html" %}

{% block texto %} {{ text }} {% endblock texto %}
~~~~
- Entre as chaves de texto podemos passar **chaves duplas** com a chave que queremos passar para o nosso site ao renderizarar a página exemplo.html.

Da mesma forma podemos fazer com o título da página, dessa vez vamos utilizar o arquivo head.html dentro de base/global/partials:

~~~~django html
{% load static %}<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}Site do Luiz</title>
    <link rel="stylesheet" href="{% static 'home/css/blue.css' %}">
    <link rel="stylesheet" href="{% static 'global/css/red.css' %}">
</head>
<body>
~~~~
- Note que agora eu coloquei entre *chaves duplas* a chave title presente na função render da view *exemplo*, alterando assim o título kque fica na aba do meu site.