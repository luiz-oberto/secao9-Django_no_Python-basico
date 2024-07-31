# Arquivos estáticos (staticfiles)
## STATIC_URL, STATIC_DIRS e load static
Arquivos estáticos são arquivos como imagens, arquivos do tipo .css, entre outros. Por padrão, essas pastas são inclusas em uma pasta chamada static. Na nossa aula vimos que podemos criar essa pasta dentro dos apps como também podemos criar no diretório raiz.

Ao fazer isso também devemos nos atentar a confuigurações feitas no setting.py. Nesse arquivo já por padrão o 
~~~python
STATIC_URL = static/
~~~
 no qual ele procura toda e qualquer pasta static e utiliza no caminho e podemos configurar também uma variável:
 ~~~python 
 STATICFILES_DIRS = [
    BASE_DIR / 'base' / 'static'
]
~~~
que vai buscar na raiz do projeto o caminho base/static.

Para utilizarmos os nossos arquivos .css, por exemplo, podemos ir até head.html e na dentro da tag head podemos acrescentar as seguintes linhas:

~~~django html
<link rel="stylesheet" href="{% static 'home/css/blue.css' %}">
<link rel="stylesheet" href="{% static 'global/css/red.css' %}">
~~~
- A primeira linha cita o caminho para se alcançar o arquivo blue.css através do app home
- a segunda linha cita o caminho para alcançar o arquivo red.css através da pasta global presente na raiz do projeto.