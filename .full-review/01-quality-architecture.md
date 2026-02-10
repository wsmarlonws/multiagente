# Phase 1: Code Quality & Architecture Review

## Code Quality Findings

**Resumo:** 19 achados (3 Critical, 5 High, 7 Medium, 4 Low)

### Critical

1. **Credenciais Hardcoded no Código-Fonte** — `app/core/config.py:6-7`
   - Senha do banco (`multiagente123`) como valor padrão no código.
   - **Correção:** Remover defaults de campos sensíveis, usar `SecretStr` do Pydantic.

2. **`.env.example` com Credenciais Reais** — `.env.example`
   - Conteúdo idêntico ao `.env` real, expondo credenciais no controle de versão.
   - **Correção:** Usar placeholders (`POSTGRES_PASSWORD=ALTERAR_AQUI`).

3. **`onupdate=func.now()` Não Funciona com Async** — `app/models/tarefa.py:17-19`
   - `onupdate` é mecanismo do ORM Python, não trigger de banco. Em async com `asyncpg`, pode não disparar confiavelmente.
   - **Correção:** Atualizar explicitamente na aplicação ou criar trigger no banco.

### High

4. **Lógica de Busca+404 Duplicada** — `app/routers/tarefas.py:56-61, 71-76, 92-97`
5. **Ausência de Camada de Serviço/Repositório** — `app/routers/tarefas.py`
6. **Ausência de Autenticação e Autorização** — `app/routers/tarefas.py`
7. **Sem Gerenciamento de Lifecycle do Engine** — `app/core/database.py:8-14`
8. **Divergência SQLite vs PostgreSQL nos Testes** — `tests/conftest.py:9`

### Medium

9-15. Commit automático em GETs, falta de índice em criado_em, falta pool_pre_ping, PUT com semântica de PATCH, ausência de logging, ausência de CORS, lógica de sessão duplicada nos testes.

### Low

16-19. Tipo de retorno dict genérico, falta de docstrings, cobertura de testes incompleta, health check superficial.

---

## Architecture Findings

**Resumo:** 16 achados (2 Critical, 5 High, 6 Medium, 3 Low)

### Critical

1. **Ausência Total de Autenticação/Autorização**
2. **Credenciais Padrão Fracas no Código-Fonte**

### High

3-7. Ausência de camada de serviço, PUT para atualização parcial, ausência de índices, DateTime sem timezone, commit automático em todas as requests.

### Medium

8-13. Ausência de repositório, instanciação global de engine, ausência de contrato de erro, health check superficial, onupdate não refletido, migração acoplada ao start.

### Low

14-16. Singleton de config, ausência de filtros, ausência de .dockerignore.

---

## Critical Issues for Phase 2 Context

### Para Security Review:
- Credenciais hardcoded e `.env.example` com valores reais
- Ausência total de autenticação/autorização
- Ausência de CORS configurado
- `setattr()` usado na atualização pode expor campos internos
- Sem rate limiting
- Sem middleware de erro global

### Para Performance Review:
- Ausência de índices em `criado_em`
- `DateTime` sem timezone
- `pool_pre_ping` ausente
- Commit em operações de leitura
- Engine sem lifecycle management

### Pontos Positivos:
- Versionamento de API (`/api/v1/`)
- Tipagem completa com type hints
- SQLAlchemy 2.0 moderno
- Pydantic v2 com ConfigDict
- Dockerfile com usuário não-root
- Docker Compose com healthcheck
- Pool de conexões configurado
- Ruff configurado
- Nomenclatura consistente em português
