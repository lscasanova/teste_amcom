# teste_amcom
[![Maintainability](https://api.codeclimate.com/v1/badges/478ce03c9f21fa113a05/maintainability)](https://codeclimate.com/github/lscasanova/teste_amcom/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/478ce03c9f21fa113a05/test_coverage)](https://codeclimate.com/github/lscasanova/teste_amcom/test_coverage)
[![Build Status](https://travis-ci.org/lscasanova/teste_amcom.svg?branch=master)](https://travis-ci.org/lscasanova/teste_amcom)

### Instalar as dependencias do python
pip install -r requirements.txt

### Criar o banco de dados
createdb -h localhost -p 5432 -U postgres amcom

### Efetuar as migrações do banco
python amcom/manage.py migrate

### Importar dados para testes
python amcom/manage.py loaddata data/data.json 