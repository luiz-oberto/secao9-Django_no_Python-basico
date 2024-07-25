# Criando apps com manage.py startapp do Django
Nesta aula vamos criar um app dentro do nosso projeto. Um app em django serve para criarmos as funcionalidade que vamos criar em nosso projeto/site. Para entendermos melhor o uso de apps vamos criar dois apps com funções diferentes: home e blog. Para criarmos um app podemos utilizar o seguinte comando no terminal:

        python manage.py startapp (nome_do_app)

Assim, o django vai criar uma pasta com vários arquivos .py, vamos entender um pouco cada um deles:

### admin.py
- Aqui você vai registrar os seus modelos

### apps.py
- A configuração do meu app que vamos precisar adicionar no INSTALLED_APPS no settings.py

### models.py 
- aonde você registra os seus modelos

### tests.py
- aonde você criar seus testes para o django (não vamos aprender nesse curso, mas existe outro curso voltado para desenvolvimento com django)

### views.py 
- O que criamos nas aulas anteriores, aonde vamos colocar nossas funções para views

## Entendo o uso de apps
Quando você cria um app, você cria funcionalidades voltada para esse app, vamos dizer que esse app tenha o nome de 'home'. Agora suponhamos que precisamos criar no mesmo projeto um blog que vai ter funcionalidade totalmente diferentes do app 'home', para isso é necessario criar um novo app como o nome de 'blog'. Ou seja, quando precisamos lidar com funcionlidades diferentes dentro do mesmo projeto, faz-se necessário criar mais de um app, caso não haja essa necessidade, apenas um app já será o suficiente.