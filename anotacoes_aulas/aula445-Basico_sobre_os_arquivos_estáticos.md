# Básico sobre os arquivso estáticos, DEBUG e ALLOWED_HOST (local e em produção) 
- O django não é um servidor!
- o *runserver* é para desenvolvermos
- quandoo for subir seu site você vai ter que desabilitar o modo DEBUG
- Você também vai ter que configurar o host qu vão acessar sua aplicaçãoem settings.py ALLOWED_HOST.

Quando você configura o DEBUG para *False* e ajusta o ALLOWED_HOST para receber um host (como por exemplo 127.0.0.1) os arquivos eestáticos deixam de funcionar. Para ajustar isso precisamos colocar namespace aonde tiver arquivos estáticos.

Então vamos configurar nosso settings.py para saber onde vai ficar armazenado nossos arquivos estáticos da seguinte maneira:

~~~python
STATIC_ROOT = BASE_DIR / 'static_files'
~~~

Com isso, podemos dar o seguinte comando no terminal

~~~
python manage.py collectstatic
~~~

Ao fazer isso, vamos pegar todos os arquivos estáticos e copiar para uma única pasta no qual o servidor irá nos servir.

- O django não serve os arquivos estáticos em produção, quem vai fazer isso vai ser o seu servidor!

Agora podemos servir nossos arquivos estáticos usando o WhiteNoise, que é ma biblioteca que nos ajuda agindo como um seervidor que vai serveir os arquivos estáticos. Link para a documentação do WhiteNoise:
https://whitenoise.readthedocs.io/en/latest/

- Para instalar:
~~~
pip install whitenoise
~~~

- Em seguida vamos colocar o middleware do WhiteNoise abaixo de SecurityMiddleware do django, conforme diz a documentação:

~~~python
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
~~~

Agora, assim que subirmos nossa aplicação, os arquivos estáticos voltará a funcionar normalmente mesmo etando com DEBUG desativado.

Avisando que, nunca vamos editar os arquivos localizados na static_files, para atualizarmos esses arquivos basta darmos o mesmo comando no terminal de collectstatic, que automaticamente ele vai fazer as mudanças que foram feitas nos arquivos estáticos.

~~~
python manage.py collectstatic
~~~

Com isso aprendemos que quando desativamos o DEBUG nossa aplicação entende que ele vai subir pra produção e que vai precisar desativar várias coisas que só fuciona no modo DEBUG pela segurança da sua aplicação.