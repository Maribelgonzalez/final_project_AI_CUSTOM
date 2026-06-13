# Sprint 1 — Planning

**Fecha:** 2026-06-12
**Duración:** 1 semana
**Objetivo:** Implementar el módulo CAG funcional con pruebas pasando

## Items seleccionados del backlog

| ID  | Historia | Estimación |
|-----|----------|------------|
| US1 | Contexto persistente entre preguntas | 3 puntos |
| US2 | Persistencia en almacenamiento local | 2 puntos |
| US3 | Pruebas unitarias del módulo CAG | 2 puntos |
| US4 | Escenarios BDD | 1 punto |

**Total:** 8 puntos

## Tareas técnicas

- [ ] Implementar `context_store.py` con métodos `save`, `list_for_user`, `get`
- [ ] Implementar `cag.py` con función `apply_context`
- [ ] Integrar CAG en `assistant.py`
- [ ] Verificar que 6/6 pruebas pasan
- [ ] Primer commit y push al repositorio