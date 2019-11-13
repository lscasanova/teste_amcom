# teste_amcom

## Instalar as dependencias do python
pip install -r requirements.txt

## Criar o banco de dados
createdb -h localhost -p 5432 -U postgres amcom

## Efetuar as migrações do banco
python amcom/manage.py migrate