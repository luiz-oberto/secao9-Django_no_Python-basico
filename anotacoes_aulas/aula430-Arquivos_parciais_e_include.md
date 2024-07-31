# Arquivos parciais e include para separar trechos dos templates
### Include
O Include pode ser usado para colocar dentro de um arquivo *HTML* ou *django HTML* os códigos de outro arquivo HTML
- Sintaxe include:
~~~django html
{% include "global/partials/head.html" %}
~~~
- Esse exemplo diz para ir no caminho Global/partials e puxar as linhas do arquivo head.html

### Partials
O partials funciona de maneira parecida ao Include, porém o partials é voltado para utilizar apenas pequenos trachos de código.
- sintaxe partials
~~~django html
{% include "global/partials/paragrafo.html" %}
~~~