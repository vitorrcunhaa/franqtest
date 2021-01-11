# franqtest

## Rodando a aplicação localmente (Instruções em inglês):

## Running the app on your local computer (dev envinronment)

`git clone https://github.com/vitorrcunhaa/franqtest.git` or unpack compressed file(if you got this project via compressed file)

Go to `franqtest` dir

To run the Django app on your local computer, set up a Python development environment, including Python, pip, and virtualenv.

Create an isolated Python environment, and install dependencies:

LINUX/MACOS
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
WINDOWS
```
virtualenv env
env\scripts\activate
pip install -r requirements.txt
```
Run the Django migrations to set up your models:
```
python manage.py makemigrations
python manage.py migrate
```
Start a local web server:

`python manage.py runserver`

In your browser, go to http://localhost:8000:


## Using the Django admin console

Create a superuser. You need to define a username and password.
`python manage.py createsuperuser`

Start a local web server:
`python manage.py runserver`

In your browser, go to http://localhost:8000/admin.


---------------------------------------------------------------------

# Já estamos no ar!

A aplicação em questão já teve sua primeira versão lançada e está disponível em:
https://franqtest.herokuapp.com/

Para checar a API de listagem de veículos(login necessário), e os respectivos usuários que os possuem(ou não) acesse:
https://franqtest.herokuapp.com/vehicle/api/vehicle_list

Para usuários administradores deve retornar a lista completa, ṕara consumidores, apenas os veículos que possuem.


Usuários para testes já foram criados e alguns campos populados para facilitar o entendimento.

### Usuário administrador
usuário: franqtest

senha: franq123456

### Usuário consumidor
usuário: testeee

senha: teste123456

Sinta-se a vontade para brincar dentro da aplicação ou para registrar novos usuários e fazer login.

Esta aplicação possui dois tipos de usuários: Consumidor ou Administrador.

A aplicação em questão simula um sistema de cadastro de veículos, onde existe um usuário administrador que pode fazer quase qualquer tipo de operação no sistema, e o usuário do tipo consumidor que tem apenas algumas permissões.

O administrador tem permissões de adicionar, editar ou deletar veículos. Dentro disto está inclusive colocar um veículo na garagem de algum consumidor, aumentar o saldo do consumidor, etc.

O administrador também possui permissão de edição de dados básicos do usuário.

O usuário consumidor quando é criado, começa por padrão com 100000 de saldo.

O consumidor pode apenas comprar veículas de uma lista de veículos previamente adicionados por um administrador.

O consumidor só podera comprar veículos se tiver saldo suficiente para tal.

O consumidor terá disponível em sua garagem os veículos que comprou ou que foram adicionados a ele pelo administrador.

### Mudança de escopo - explicação

Algumas especificações do teste não fizeram sentido pra mim, por este motivo adicionei novos métodos, novas páginas, autenticação, deploy e alguns pontos mais complexos para que como um todo a aplicação fizesse sentido e conseguisse simular algo mais próximo do mundo real.
