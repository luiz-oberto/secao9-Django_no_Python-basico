# Configurando tempçates globais com DIRS + extends para herança de templates
Aqui vamos aprende a utilizar o DIRS que se encontra em *setting.py* dentro da lista de dicionários chamado *TEMPLATES*. No DIRS podemos especificar o caminho dos arquivos de templates que queremos usar.


Para isso vamos fazer da seguinte forma:
- vamos criar uma pasta na raiz do projeto chamada base
- nessa pasta vamos criar outra pasta chamada global
- por fim nessa última pasta criada nós criamos o arquivo *base.html*

Após fazer isso vamos até settings e configurar o DIRS da seguinte maneira:
~~~python
        'DIRS': [
            BASE_DIR / 'base'
        ],
~~~
- essa linha diz aonde vamos procurar os templates 'primariamente'


Antes de continuarmos, precisamos saber de uma extensão chamada Django para o VSCode no qual vai nos auxiliar a escrever código HTML mas que é chamado de django_HTML. Nele podemos usar blocks que podem ser extensíveis para outros arquivos HTML.
Vamos ver um exemplo partindo do arquivo *base.html*:
~~~html
<!-- base/global/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{% block texto %} BASE {% endblock texto %}</h1>
</body>
</html>
~~~
Agora vamos olhar o arquivo index.html do app *home*:

~~~django html
<!-- home/index.html -->
{% extends "global/base.html" %}

{% block texto %} MUDAR O TEXTO {% endblock texto %}
~~~
- Nesse exemplo o arquivo o arquivo index.html estende do arquivo base, dessa forma tudo que está no arquivo base é replicado para o index.html. Como pode ver podemos até mesmo alterar o texto escrito no *{% block texto %}*.
- Em resumo, podemos evitar de criar templates dentro dos apps criados e utilizarmos apenas um único diretório para armazenar tudo o que precisamos de templates.