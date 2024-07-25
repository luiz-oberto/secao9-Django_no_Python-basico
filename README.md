# secao9-Django_no_Python-basico
Aulas de django no python do curso de Python 3 do básico ao avançado

- Criando um projeto, faça isso em uma pasta úniica que vai ter apenas o projeto django

        django-admin startproject (nome_do_projeto) .

obs: esse comando vai criar um projeto django com o arquivo manage.py no diretório raiz


- Rodando o projeto

        python manage.py runserver



## Manage.py
Esse arquivo é criado com a incialização do projeto e serve para iniciar o servidor django.

## settings.py 
Arquivo aonde você vai configurar todo o projeto django, é basicamente o **coração** do seu programa. Vamos entender masi explorando superficialmente o que ele contém.

- INSTALLED _APPS => Nele podemos configurar os apps que vamos usar, por padrão ele vem assim:

~~~python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
~~~

- MIDDLEWARE => É um tipo de padrao de projeto, utilizado quando precisamos fazer alguma ação no meio de outra ação, por padrão:

~~~python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
~~~

- ROOT_ULRCONF => Lugar que você vai char todas as URLs do seu projeto:

~~~python
ROOT_URLCONF = 'project.urls'
~~~

- TEMAPLATES => para exibir os templates:

~~~python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
~~~

- DATABASE => Aonde você vai configurar a base de dados

~~~python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
~~~

- AUTH_PASSWORD_VALIDATORS => Validadores de senhas

~~~python
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
~~~

- WSGI => A interface de comunicação entre o django e o servidor que pode ser web ou assinchronous

- LANGUAGE_CODE
- TIME_ZONE
- USE_I18
- USE_TZ
- STATIC_URL
- DEFAULT_AUTO_FIELD