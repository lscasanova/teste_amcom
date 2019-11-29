# Teste AMcom
[![Maintainability](https://api.codeclimate.com/v1/badges/478ce03c9f21fa113a05/maintainability)](https://codeclimate.com/github/lscasanova/teste_amcom/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/478ce03c9f21fa113a05/test_coverage)](https://codeclimate.com/github/lscasanova/teste_amcom/test_coverage)
[![Build Status](https://travis-ci.org/lscasanova/teste_amcom.svg?branch=master)](https://travis-ci.org/lscasanova/teste_amcom)

## Instalação

⚠ Utilizar o python 3.8
### Instalar as dependencias do python
    pip install -r requirements.txt

### Criar o banco de dados
    createdb -h localhost -p 5432 -U postgres amcom

### Efetuar as migrações do banco
    python manage.py migrate

### Importar dados para testes
    python manage.py loaddata data/data.json

### Criar o super usuário
    python manage.py createsuperuser


### Para executar os testes
    python manage.py test

### Para executar a aplicação
    python manage.py runserver
