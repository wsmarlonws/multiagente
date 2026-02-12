# Projeto Multiagente - Contexto para Claude Code

## Projeto
API REST de Tarefas (Todo-List) construída com FastAPI, SQLAlchemy async e PostgreSQL.

## Stack
- Python 3.12+, FastAPI, SQLAlchemy[asyncio], asyncpg, Alembic
- Docker + Docker Compose para infraestrutura
- pytest + pytest-asyncio para testes

## Estrutura
```
app/              # Aplicacao FastAPI
  core/           # Config e database
  models/         # Modelos SQLAlchemy
  schemas/        # Schemas Pydantic
  routers/        # Endpoints da API
alembic/          # Migracoes de banco
tests/            # Testes automatizados
conductor/        # Gestao do projeto
```

## Comandos
- **Testes**: `python -m pytest tests/ -v`
- **Lint**: `ruff check app/ tests/`
- **Format**: `ruff format app/ tests/`
- **Servidor local**: `uvicorn app.main:app --reload`
- **Docker**: `docker compose up --build`

## Convencoes
- Commits: Conventional Commits em portugues (feat:, fix:, docs:, refactor:, test:, chore:)
- Codigo e nomes de variaveis em portugues quando aplicavel

## Configuracao Multi-Agente

Este projeto esta configurado para trabalho com multiplos agentes em paralelo.

### Agent Teams (equipes de agentes)
Habilitado via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` no `.claude/settings.json`.
Permite criar equipes de agentes que trabalham em paralelo com comunicacao entre si.

### Subagentes customizados
Disponiveis em `.claude/agents/`:
- **pesquisador** - Investigacao e analise de codigo
- **desenvolvedor** - Implementacao de features e correcoes
- **revisor** - Code review e validacao de qualidade
