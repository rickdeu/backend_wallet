# Django Wallet API

Uma API para gerenciar carteiras digitais e transações financeiras, utilizando Django, PostgreSQL e Docker.


## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas no seu sistema:

    Docker
    Docker Compose

Configuração do Projeto

Siga as etapas abaixo para configurar e executar o projeto.
1. Clone o Repositório

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Configure as Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto e copie o conteúdo abaixo:

# PostgreSQL environment variables

POSTGRES_USER=django

POSTGRES_PASSWORD=django

POSTGRES_DB=django_db

POSTGRES_HOST=db

POSTGRES_PORT=5432

# Django environment variables
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=True
DATABASE_URL=postgres://django:django@db:5432/django_db

Substitua your_secret_key por uma chave secreta segura para o Django.
3. Build e Execute os Contêineres

Para construir e iniciar o projeto, execute:

docker-compose build
docker-compose up

    O serviço da API estará disponível em: http://localhost:8000/

Uso do Projeto
Criar um Superusuário (Admin)

Para acessar o painel administrativo do Django, crie um superusuário:

docker-compose exec web sh
python manage.py createsuperuser

Siga as instruções para definir o nome de usuário, e-mail e senha.
Endpoints Disponíveis

Aqui estão os endpoints principais da API:

    Autenticação:
        POST /api/token/: Gera um token de acesso.
        POST /api/token/refresh/: Atualiza o token de acesso.

    Usuários:
        POST /api/users/: Cria um novo usuário.

    Carteira:
        GET /api/wallet/: Consulta o saldo da carteira.
        POST /api/wallet/add_balance/: Adiciona saldo à carteira.

    Transações:
        POST /api/transactions/transfer/: Cria uma transferência entre carteiras.
        GET /api/transactions/: Lista transações realizadas por um usuário (com filtros opcionais).

Comandos Úteis
Aplicar Migrações

Se precisar rodar as migrações manualmente:

docker-compose exec web sh
python manage.py makemigrations
python manage.py migrate

Acessar o Shell do Django

docker-compose exec web sh
python manage.py shell

Encerrando os Contêineres

Para parar os contêineres:

docker-compose down

Estrutura do Projeto

    Dockerfile: Configuração do contêiner Docker para o Django.
    docker-compose.yml: Configuração do Docker Compose para o Django e PostgreSQL.
    .env: Arquivo de variáveis de ambiente.
    requirements.txt: Dependências do projeto.

Contribuição

Sinta-se à vontade para contribuir com este projeto. Envie um pull request ou abra uma issue para reportar problemas ou sugerir melhorias.
Licença

Este projeto está licenciado sob a MIT License.


# https://github.com/WL-Consultings/challenges/tree/main/backend