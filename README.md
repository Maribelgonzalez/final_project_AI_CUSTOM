# final_project_AI_CUSTOM

Proyecto final — Integración de módulo CAG (Context-Augmented Generation) sobre un sistema RAG base.

## Descripción

Este proyecto extiende un sistema monolítico con frontend, backend y recuperación de conocimiento tipo RAG, agregando un módulo CAG que guarda, recupera y utiliza contexto persistente del usuario para mejorar respuestas posteriores.

## Arquitectura

[Usuario] → [Frontend JS]

↓

[Backend Python]

↓         ↓

[RAG - knowledge.py]  [CAG - cag.py + context_store.py]

↓         ↓

[knowledge_base.json]  [context_store.json]
### Componentes principales

| Archivo | Rol |
|---------|-----|
| `backend/server.py` | Servidor HTTP, expone endpoints REST |
| `backend/assistant.py` | Orquesta RAG + CAG para generar respuestas |
| `backend/knowledge.py` | Recuperación de snippets por palabras clave (RAG) |
| `backend/cag.py` | Enriquece respuesta con contexto previo del usuario |
| `backend/context_store.py` | Persiste y recupera contexto por usuario en JSON |
| `data/knowledge_base.json` | Base de conocimiento del curso |
| `data/context_store.json` | Almacén persistente de contexto por usuario |

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/health` | Verifica que el servidor está activo |
| POST | `/api/ask` | Responde una pregunta usando RAG + CAG |
| POST | `/api/context` | Guarda contexto para un usuario |
| GET | `/api/context?user_id=X` | Recupera contexto de un usuario |

## Instalación y ejecución

```bash
# Instalar dependencias
pip install pytest

# Ejecutar pruebas
python -m pytest tests/ -v

# Iniciar servidor
python -m backend.server
```

## Pruebas

El proyecto cuenta con 14 pruebas distribuidas en:

- `tests/base/` — pruebas base del sistema RAG original (3 pruebas)
- `tests/validation/` — pruebas de contrato del módulo CAG (3 pruebas)
- `tests/test_cag_own.py` — pruebas propias TDD (8 pruebas)

```bash
python -m pytest tests/ -v
# 14 passed
```

## Metodología

El proyecto fue desarrollado con metodología Scrum en 2 sprints. La documentación completa se encuentra en `docs/scrum/`.

- Sprint 1: Implementación del módulo CAG y pruebas
- Sprint 2: Documentación, README y entrega final

## Uso de IA

El registro cronológico de uso de IA se encuentra en `PROMPTS.md`.

## Evidencias

Las capturas del proceso están en `docs/evidencias/`.

## Autor

Maribel Gonzalez — ggonzalezg11@miumg.edu.gt