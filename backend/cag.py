"""CAG — Context-Augmented Generation module."""


def apply_context(user_id, question, base_answer, context_items):
    """
    Enriquece la respuesta base con el contexto previo del usuario.
    
    Args:
        user_id: identificador del usuario
        question: pregunta actual
        base_answer: respuesta generada por el RAG
        context_items: dict con contexto guardado del usuario
    
    Returns:
        str: respuesta enriquecida con contexto
    """
    if not context_items:
        return base_answer

    context_summary = "; ".join(
        f"{key}: {value}"
        for key, value in context_items.items()
    )

    return (
        f"{base_answer} "
        f"[Contexto previo del usuario considerado: {context_summary}]"
    )