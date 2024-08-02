# Usando block para criar blocos de posts e home
- O que fizemos na última aula foi com intuito de, caso você queira colocar algo diferente em qualquer um dos arquivos de html, seria difícil de alterar se todos eles fossem apenas uma coisa só, separando cada arquivo html de forma que cada um tenha sua função, facilita na hora de fazer qualquer alteração.

Nesta aula, utilizamos o arquivo *base.html* para recceber as informções de diversos outros arquivos HTML, ficand dessa maneira:
~~~html
<!-- base.html -->
{% include "global/partials/head.html" %}
{% include "global/partials/menu.html" %}

<!-- aqui nesse bloco ele vai colocar o título da página de acordo com a URL -->
<h1>{% block texto %}{% endblock texto %}</h1>

<main class="content">
    <!-- aqui ele expõe os posts da página -->
    {% block posts %}{% endblock posts %}
    <!-- aqui ele vai colocar tod e qualquer conteúdo que estiver vindo de index.html de home -->
    {% block home %}{% endblock home %}
</main>

</body>
</html>
~~~
- esse arquivo recebe tanto as informações parciais de head.html e menu.html nos primeiros *includes*, em seguida um bloco de texto qu varia de acordo com a URL que está navegando, depois os blocos de posts e home nos quais vão se comportar de maneira diferente coforme a navegação através das URLs.