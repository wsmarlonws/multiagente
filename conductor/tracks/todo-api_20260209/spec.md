# Specification: API REST de Tarefas (Todo-List)

**Track ID:** todo-api_20260209
**Type:** Feature
**Created:** 2026-02-09

## Summary

API REST de tarefas (todo-list) com CRUD completo. Implementada com FastAPI, PostgreSQL e Docker.

## Acceptance Criteria

- [ ] POST /api/v1/tarefas cria uma nova tarefa e retorna 201
- [ ] GET /api/v1/tarefas lista tarefas com paginação
- [ ] GET /api/v1/tarefas/{id} retorna uma tarefa específica ou 404
- [ ] PUT /api/v1/tarefas/{id} atualiza uma tarefa existente ou 404
- [ ] DELETE /api/v1/tarefas/{id} remove uma tarefa e retorna 204
- [ ] Docker Compose sobe a aplicação + PostgreSQL

## Out of Scope

- Autenticação JWT (track futura)
- Frontend
- Deploy em produção
- CI/CD pipeline
