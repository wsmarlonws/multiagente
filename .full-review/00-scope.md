# Review Scope

## Target

API REST de Tarefas (Todo-List) — Track todo-api_20260209
CRUD completo com FastAPI, SQLAlchemy async, PostgreSQL, Docker.

## Files

### Código da aplicação
- app/main.py
- app/core/config.py
- app/core/database.py
- app/models/tarefa.py
- app/schemas/tarefa.py
- app/routers/tarefas.py

### Testes
- tests/conftest.py
- tests/test_tarefas.py

### Infraestrutura
- Dockerfile
- docker-compose.yml
- pyproject.toml
- alembic.ini
- alembic/env.py
- alembic/versions/001_criar_tabela_tarefas.py
- .env.example

## Flags

- Security Focus: não
- Performance Critical: não
- Strict Mode: não
- Framework: FastAPI (Python 3.12+)

## Review Phases

1. Code Quality & Architecture
2. Security & Performance
3. Testing & Documentation
4. Best Practices & Standards
5. Consolidated Report
