# Criando o parial postblock.html e usadno include
- Utilize esse link caso queira zerar o seu css:

https://github.com/luizomf/cursopython2023/blob/71036bfd44d052823631f749f14e3f8ca99c01df/aula207_ola_django/base/static/global/css/style.css

- dica: Ctrl + P atalho que serve para pesquisar seus arquivos e facilitar sua navegação entre eles
- Ctrl + Shift + p -> para comandos ou troca de linguagens

Vamos começar indo até o site json placeholder, que é uma API "fake" utilizada para testes e protótipos, vamos utilizar ela nas próximas aulas.

Agora vamos até o nosso partials e criar o arquivo postblock.html, cuja a função será de exibir os blocos de postagem do blog. Vamos deixá-lo assim:
~~~html
<article class="post">
    <header>
        <h2 class="post__title">
            Lorem ipsum dolor sit amet.
        </h2>
    </header>
    <div class="post__body">
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis reprehenderit sit alias quibusdam delectus praesentium ipsa. Velit, sapiente nesciunt distinctio eum autem optio rem quibusdam ad mollitia, fuga hic quae facilis perspiciatis animi nulla! Dolorem quibusdam voluptatibus doloremque? Quam explicabo, asperiores vitae ab possimus necessitatibus exercitationem ipsa vel? Quam, quia?
    </div>
</article>
~~~

Feito isso podemos ir até nosso arquivo base.html alterar para deixá-lo assim:
~~~html
{% include "global/partials/head.html" %}
{% include "global/partials/menu.html" %}

<h1>{% block texto %}{% endblock texto %}</h1>

<main class="post">
    {% include "global/partials/postblock.html" %}
</main>

</body>
</html>
~~~
- Nesse rquivo foi carescentado a tag main juntamente com o include que diz aonde pegar os blocos de postagens.