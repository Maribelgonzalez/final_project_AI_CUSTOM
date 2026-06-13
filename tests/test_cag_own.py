import unittest
from backend.context_store import ContextStore
from backend.cag import apply_context
import tempfile
from pathlib import Path


class TestContextStore(unittest.TestCase):

    def setUp(self):
        # Usa archivo temporal para no afectar datos reales
        self.tmp = tempfile.NamedTemporaryFile(suffix=".json", delete=False)
        self.tmp.close()
        Path(self.tmp.name).write_text("{}", encoding="utf-8")
        self.store = ContextStore(path=Path(self.tmp.name))

    def test_save_and_retrieve(self):
        self.store.save("user1", "tema", "redes neuronales")
        items = self.store.list_for_user("user1")
        self.assertIn({"key": "tema", "value": "redes neuronales"}, items)

    def test_user_isolation(self):
        self.store.save("user1", "tema", "RAG")
        self.store.save("user2", "tema", "CAG")
        items1 = self.store.list_for_user("user1")
        items2 = self.store.list_for_user("user2")
        self.assertIn({"key": "tema", "value": "RAG"}, items1)
        self.assertIn({"key": "tema", "value": "CAG"}, items2)

    def test_empty_user_returns_empty_list(self):
        items = self.store.list_for_user("usuario_nuevo")
        self.assertEqual(items, [])

    def test_get_existing_key(self):
        self.store.save("user1", "nivel", "principiante")
        value = self.store.get("user1", "nivel")
        self.assertEqual(value, "principiante")

    def test_get_missing_key_returns_default(self):
        value = self.store.get("user1", "clave_inexistente", default="N/A")
        self.assertEqual(value, "N/A")


class TestApplyContext(unittest.TestCase):

    def test_no_context_returns_base_answer(self):
        result = apply_context("u1", "pregunta", "respuesta base", {})
        self.assertEqual(result, "respuesta base")

    def test_with_context_enriches_answer(self):
        context = {"nivel": "principiante"}
        result = apply_context("u1", "pregunta", "respuesta base", context)
        self.assertIn("principiante", result)
        self.assertIn("respuesta base", result)

    def test_multiple_context_items(self):
        context = {"nivel": "avanzado", "tema": "CAG"}
        result = apply_context("u1", "pregunta", "respuesta", context)
        self.assertIn("avanzado", result)
        self.assertIn("CAG", result)


if __name__ == "__main__":
    unittest.main()