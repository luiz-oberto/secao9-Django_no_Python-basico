# Usando if, elif e else dentro do template HTML do Django
Nest aula vamos aprender sobre condicionais no django. Elas funcionam quase da mesma forma que o IF no python, a diferença é que precisamos indicar aonde elas começam e aonde terminam. 
- A sintaxe fica da seguinte forma.
~~~django html
<!-- Aqui verifica se 'text' existe, se existir ele retorna o bloco texto -->
{% if text %}
    <h1>{% block texto %}{% endblock texto %}</h1>
{% endif %}

<!-- Estrutura do if, elif e else com endif indicando o final da condicional -->
{% if 1 %}

{% elif 1 %}

{% else %}

{% endif %}
~~~