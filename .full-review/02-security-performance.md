# Phase 2: Security & Performance Review

## Security Findings

**Resumo:** 17 achados (3 Critical, 6 High, 5 Medium, 3 Low)

### Critical

1. **SEC-001: Credenciais Hardcoded** — `app/core/config.py:6-7` — CVSS 9.8
2. **SEC-002: `.env.example` com Credenciais Reais** — CVSS 9.8
3. **SEC-003: Ausência Total de Autenticação** — CVSS 9.8

### High

4. SEC-004: Sem CORS (CVSS 7.5)
5. SEC-005: Sem Rate Limiting (CVSS 7.5)
6. SEC-006: Mass Assignment via setattr() (CVSS 7.2)
7. SEC-007: DEBUG=true no .env (CVSS 7.5)
8. SEC-008: Sem Exception Handler Global (CVSS 5.3)
9. SEC-009: PostgreSQL Exposto (CVSS 8.1)

### Medium

10-14. Sem headers segurança, docs públicos, sem logging, descricao sem limite, sem TLS.

### Low

15-17. Dependências sem pinning, sem testes segurança, migrations e app mesmo container.

---

## Performance Findings

**Resumo:** 18 achados (2 Critical, 5 High, 8 Medium, 3 Low)

### Critical

1. **Índice Ausente em `criado_em`** — ORDER BY sem índice = full table scan
2. **Duas Queries na Listagem** — dados + COUNT(*) separado

### High

3-7. DateTime sem timezone, pool_pre_ping ausente, commit em leituras, uvicorn single worker, pool subdimensionado.

### Medium

8-15. Offset sem limite, triple round-trip no create, sem cache HTTP, sem optimistic locking, sem rate limiting, health check sem banco, config sem multi-ambiente, migrations no startup.

### Low

16-18. DELETE com SELECT+DELETE, scalars().all() materializa lista, database_url sem cache.
