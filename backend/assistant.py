from backend.knowledge import retrieve_snippets
from backend.cag import apply_context
from backend.context_store import ContextStore

_store = ContextStore()


def answer_question(user_id, question):
    snippets = retrieve_snippets(question)

    if not snippets:
        return {
            "user_id": user_id,
            "answer": "No encontre informacion suficiente en la base de conocimiento del curso.",
            "sources": [],
            "context_used": [],
        }

    source_text = " ".join(item["content"] for item in snippets)
    base_answer = f"Segun la base de conocimiento del curso: {source_text}"

   # Recuperar contexto previo del usuario
    context_raw = _store.list_for_user(user_id)
    context_items = {item["key"]: item["value"] for item in context_raw}

    # Enriquecer respuesta con CAG
    final_answer = apply_context(user_id, question, base_answer, context_items)

  
    return {
        "user_id": user_id,
        "answer": final_answer,
        "sources": [item["id"] for item in snippets],
        "context_used": list(context_items.keys()),
    }