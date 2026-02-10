# Workflow

## Política de TDD

**Flexível** — testes recomendados apenas para lógica complexa. Não é obrigatório escrever testes antes da implementação, mas código com lógica de negócio significativa deve ter cobertura de testes.

## Estratégia de Commits

**Conventional Commits** em português:

- `feat:` — nova funcionalidade
- `fix:` — correção de bug
- `docs:` — documentação
- `refactor:` — refatoração
- `test:` — testes
- `chore:` — tarefas de manutenção
- `ci:` — mudanças em CI/CD

Exemplo: `feat: adicionar endpoint de autenticação JWT`

## Code Review

**Opcional / auto-revisão** — revisão de código não é obrigatória. Auto-revisão é aceita para este projeto de aprendizado.

## Checkpoints de Verificação

**Apenas na conclusão da track** — verificação manual necessária somente quando a feature/track estiver completa. Não exigido entre tarefas ou fases.

## Ciclo de Vida de uma Tarefa

1. **Pendente** — tarefa criada no plano
2. **Em progresso** — desenvolvimento ativo
3. **Concluída** — implementação finalizada
4. **Verificada** — (apenas na conclusão da track) revisão final confirmada

## Fluxo de Desenvolvimento

1. Criar track com `/conductor:new-track`
2. Implementar tarefas com `/conductor:implement`
3. Commitar com mensagens Conventional Commits
4. Verificar ao finalizar a track
