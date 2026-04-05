import json
import os
import uuid

DATA_DIR = "data"
INDEX_FILE = os.path.join(DATA_DIR, "index.json")


class StorageBackend:
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        if not os.path.exists(INDEX_FILE):
            with open(INDEX_FILE, "w") as f:
                json.dump([], f)

    def _load_index(self) -> list:
        with open(INDEX_FILE, "r") as f:
            return json.load(f)

    def _save_index(self, index: list) -> None:
        with open(INDEX_FILE, "w") as f:
            json.dump(index, f)

    @staticmethod
    def _safe_id(analysis_id: str) -> str:
        """Validate that analysis_id is a canonical UUID to prevent path traversal."""
        return str(uuid.UUID(analysis_id))

    def save_analysis(self, analysis: dict) -> str:
        raw_id = analysis.get("id", str(uuid.uuid4()))
        analysis_id = self._safe_id(raw_id)
        analysis["id"] = analysis_id
        path = os.path.join(DATA_DIR, f"{analysis_id}.json")
        with open(path, "w") as f:
            json.dump(analysis, f)
        index = self._load_index()
        if analysis_id not in index:
            index.append(analysis_id)
            self._save_index(index)
        return analysis_id

    def load_analysis(self, analysis_id: str) -> dict | None:
        safe_id = self._safe_id(analysis_id)
        path = os.path.join(DATA_DIR, f"{safe_id}.json")
        if not os.path.exists(path):
            return None
        with open(path, "r") as f:
            return json.load(f)

    def load_all_analyses(self) -> list:
        index = self._load_index()
        analyses = []
        for analysis_id in index:
            analysis = self.load_analysis(analysis_id)
            if analysis:
                analyses.append(analysis)
        return analyses