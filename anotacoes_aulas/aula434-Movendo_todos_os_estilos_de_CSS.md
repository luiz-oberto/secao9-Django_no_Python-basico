# Movendo todos os estilos CCSS para global/css/stle.css
- Nesta aula vamos apenas "zerar" nosso css. Para fazer isso vamos criar um arquivo em base/static/global/css/stye.css e vamos deixar dessa maneira:

~~~css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
~~~

agora fazemos algumas mudanças no nosso arquivo head.html:

~~~django html
{% load static %}<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}Site do Luiz</title>
    <link rel="stylesheet" href="{% static "global/css/style.css" %}">
</head>
<body>
~~~
Com isso finalizamos a aula.