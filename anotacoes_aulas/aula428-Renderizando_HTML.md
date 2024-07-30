# Aula 428 - Renderizando HTML, render, templates, INSTALLED_APPS e TemplateDoesNotExist
- **obs do professor**: Se você chegou até aqui sem saber HTML e CSS, PAUSE ESTA AULA e vá assistir a seção de HTML e CSS, é isso...

Nesta aula, vamos aprender a renderizar os templates HTML na nossa aplicação, para isso precisamos seguir os seguintes passos:
- Vamos ajustar o arquivo views.py para renderizar o arquivo home.html deixando da seguinte forma:

~~~python
from django.shortcuts import render

def home(request):
    print('home')
    return render(
        request,
        'home.html')
~~~

- Precisamos agora criar a pasta *template* dentro do nosso app 'home' para criarmos o home.html, que vai ser o template a ser renderizado.
- agora vá em apps.py dentro da pasta 'home' para verificar o nome que foi configurado lá, vamos deixar a variável 
~~~python
name='home'
~~~

- Por fim vamos em settings, na variável INSTALLED_APPS e vamos acrescentar ao fim da lista o app 'home', deixando dessa forma:
~~~python
NSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home', # <-- NOSSO APP
]
~~~
Tendo feito isso conseguimos renderizar nossa página ao executar nosso servidor. PORÉM, se repetirmos esse mesmo procedimento para o app blog, mantendo o nome da html de 'home.html' vamos ter um problema com a renderização de templates, porque ao invés de chamarmos a 'home.html' do *blog*, vamos acabar caindo na 'home.html' do app *home*. Para evitar isso, precisamos criar uma pasta dentro de templates com o nome do app e passar o caminho da pasta nas *views.py*. No caso do *blog*, fica desse jeito:
~~~python
from django.shortcuts import render

def blog(request):
    print('my_view')
    return render(
        request, 
        'blog/index.html'
    )

def exemplo(request):
    print('exemplo')
    return render(
        request,
        'blog/exemplo.html'
    )
~~~
- Dessa forma, mesmo que colocarmos os nomes dos templates iguais em apps diferentes, não teremos problemas com a renderização se estiverem com o devido caminhyo especificado nas *views.py*.
