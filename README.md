# multiagente

API REST de tarefas (todo-list) com FastAPI, PostgreSQL e Docker.

## Requisitos

- Docker e Docker Compose

## Como rodar

```bash
# Subir app + PostgreSQL
docker compose up --build

# A API estará disponível em http://localhost:8000
# Documentação interativa em http://localhost:8000/docs
```

## Endpoints

| Método | Path | Descrição | Status |
| --- | --- | --- | --- |
| GET | /health | Health check | 200 |
| POST | /api/v1/tarefas | Criar tarefa | 201 |
| GET | /api/v1/tarefas | Listar tarefas (paginado) | 200 |
| GET | /api/v1/tarefas/{id} | Buscar tarefa | 200/404 |
| PUT | /api/v1/tarefas/{id} | Atualizar tarefa | 200/404 |
| DELETE | /api/v1/tarefas/{id} | Deletar tarefa | 204/404 |

## Exemplos

```bash
# Criar tarefa
curl -X POST http://localhost:8000/api/v1/tarefas \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Estudar FastAPI", "descricao": "Completar tutorial"}'

# Listar tarefas
curl http://localhost:8000/api/v1/tarefas

# Listar com paginação
curl "http://localhost:8000/api/v1/tarefas?limite=5&offset=0"

# Buscar tarefa
curl http://localhost:8000/api/v1/tarefas/1

# Atualizar tarefa
curl -X PUT http://localhost:8000/api/v1/tarefas/1 \
  -H "Content-Type: application/json" \
  -d '{"concluida": true}'

# Deletar tarefa
curl -X DELETE http://localhost:8000/api/v1/tarefas/1
```

## Desenvolvimento local (sem Docker)

```bash
# Instalar dependências
pip install -e ".[dev]"

# Configurar variáveis de ambiente
cp .env.example .env
# Ajustar POSTGRES_HOST=localhost no .env

# Rodar migrações
alembic upgrade head

# Iniciar servidor
uvicorn app.main:app --reload

# Rodar testes
pytest -v

# Lint
ruff check app/ tests/
```

## Tech Stack

- Python 3.12+
- FastAPI + Uvicorn
- SQLAlchemy (async) + Alembic
- PostgreSQL
- Docker + Docker Compose
- pytest + httpx (testes)
- Ruff (linting)
