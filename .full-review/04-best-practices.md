# Phase 4: Best Practices & Standards

## Framework & Language Findings

**Resumo:** 18 achados (2 Critical, 5 High, 7 Medium, 4 Low)

### Critical

1. **Ausência de `lifespan`** — Engine nunca recebe dispose()
2. **`onupdate=func.now()` quebrado com async**

### High

3. PUT com semântica de PATCH
4. DateTime sem Timezone
5. Commit Automático em Leituras
6. aiosqlite Ausente nas Dependências Dev
7. Dockerfile CMD impede graceful shutdown

### Medium

8-14. Annotated como padrão, ausência de índices, computed_field, Session.get(), Annotated para validação, HEALTHCHECK ausente, setuptools vs hatchling.

### Low

15-18. PEP 695, import datetime, tipo retorno dict, .dockerignore.

---

## CI/CD & DevOps Findings

**Resumo:** 22 achados (6 Critical, 8 High, 6 Medium, 2 Low)

### Critical

1. Ausência Total de Pipeline CI/CD
2. Ausência de Estratégia de Deploy
3. Migrations Acopladas ao Start
4. Credenciais Hardcoded
5. PostgreSQL Exposto Externamente
6. Sem Capacidade de Rollback

### High

7-14. Sem quality gates, sem scanning, single worker, sem IaC, health check superficial, sem logging, sem métricas, sem rollback.

### Medium

15-20. Docker Compose única infra, sem healthcheck app, sem docs operacional, sem separação ambientes, sem .dockerignore, sem TLS.

### Low

21-22. Imagem sem pinning, sem lock file.
