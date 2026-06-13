# Escenarios BDD — Módulo CAG

## Funcionalidad: Guardar contexto del usuario

**Escenario 1: Guardar preferencia de estilo**
Dado que el usuario "ana" no tiene contexto guardado

Cuando envía POST /api/context con key="preferred_style" value="explicaciones con analogias"

Entonces el servidor responde 201

Y el cuerpo contiene "saved"
**Escenario 2: Recuperar contexto guardado**
Dado que el usuario "ana" tiene guardado key="project"

Cuando envía GET /api/context?user_id=ana

Entonces el servidor responde 200

Y el contexto contiene el objeto {key: "project", value: "usa arquitectura monolitica moderna"}
## Funcionalidad: Usar contexto en respuestas

**Escenario 3: Respuesta enriquecida con contexto**
Dado que el usuario "luis" tiene guardado key="audience" value="explicar como principiante"

Cuando envía POST /api/ask con question="Que es CAG?"

Entonces el servidor responde 200

Y la respuesta contiene "principiante"

Y context_used contiene "audience"
## Funcionalidad: Respuesta sin contexto

**Escenario 4: Usuario sin contexto previo**
Dado que el usuario "nuevo-user" no tiene contexto guardado

Cuando envía POST /api/ask con cualquier pregunta válida

Entonces context_used es una lista vacía []

Y la respuesta proviene únicamente del RAG