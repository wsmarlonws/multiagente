# Tech Stack

## Linguagem Principal

- **Python 3.12+**

## Frontend

Nenhum — projeto apenas API (backend).

## Backend

- **FastAPI** — framework async moderno para APIs REST
- **Uvicorn** — servidor ASGI
- **Pydantic** — validação de dados e serialização

## Autenticação

- **JWT (JSON Web Tokens)** — autenticação stateless
- **python-jose** ou **PyJWT** — biblioteca para manipulação de tokens
- **passlib[bcrypt]** — hashing de senhas

## Banco de Dados

- **PostgreSQL** — banco relacional principal
- **SQLAlchemy** — ORM
- **Alembic** — migrações de banco de dados

## Infraestrutura

- **Docker** — containerização
- **Docker Compose** — orquestração local de serviços

## Ferramentas de Desenvolvimento

- **pytest** — framework de testes
- **Ruff** — linter e formatter (substitui flake8, black, isort)
- **mypy** — verificação de tipos estática
- **pre-commit** — hooks de pré-commit

## Dependências-Chave

| Pacote | Propósito |
| --- | --- |
| fastapi | Framework web |
| uvicorn | Servidor ASGI |
| sqlalchemy | ORM |
| alembic | Migrações |
| pydantic | Validação |
| python-jose | JWT |
| passlib | Hashing de senhas |
| pytest | Testes |
| httpx | Cliente HTTP para testes |
| ruff | Linting e formatação |
