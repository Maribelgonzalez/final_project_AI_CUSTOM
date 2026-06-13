import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONTEXT_FILE = PROJECT_ROOT / "data" / "context_store.json"


class ContextStore:

    def __init__(self, path=CONTEXT_FILE):
        self.path = path
        self._ensure_file()

    def _ensure_file(self):
        if not self.path.exists():
            self.path.write_text("{}", encoding="utf-8")

    def _load(self):
        return json.loads(self.path.read_text(encoding="utf-8"))

    def _save(self, data):
        self.path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    def save(self, user_id, key, value):
        data = self._load()
        if user_id not in data:
            data[user_id] = {}
        data[user_id][key] = value
        self._save(data)
        return {user_id: {key: value}}

    def list_for_user(self, user_id):
     data = self._load()
     raw = data.get(user_id, {})
     return [{"key": k, "value": v} for k, v in raw.items()]

    def get(self, user_id, key, default=None):
        return self.list_for_user(user_id).get(key, default)