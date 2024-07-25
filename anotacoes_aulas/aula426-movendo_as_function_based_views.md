- **Obs de vida:** Quanddo se está refatorando um código, nunca tire a PARTE QUE FUNCIONA até que você consiga substituuir por outro código que funcione


Aqui vamos tirar do arquivo urls.py as funções que  fizemos em urls e colocarmos em seus devidos lugares. Nesse caso vamos tirar de de urls as funções home e blog e  colocar nas suas respectivas views adicionando também algumas alterações, deixando elas assim:

~~~python
# views.py do app blog
from django.http import HttpResponse

# from django.shortcuts import render

# Create your views here.
def blog(request):
    print('my_view')
    return HttpResponse('Blog do app')
~~~