import os
import json
import uuid
from pathlib import Path


class StorageBackend:
    """File-based storage backend for Sigilith-M analysis results."""

    def __init__(self, base_dir: str = "data_storage"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)

        self.index_file = self.base_dir / "index.json"
        self.indices = self._load_index()

    def _load_index(self) -> dict:
        """Load the index file if it exists, otherwise return an empty dict."""
        if self.index_file.exists():
            with open(self.index_file, "r") as f:
                return json.load(f)
        return {}

    def _update_index(self):
        """Write the updated index back to disk."""
        with open(self.index_file, "w") as f:
            json.dump(self.indices, f)

    def _safe_id(self, analysis_id: str) -> str:
        """Validate that analysis_id is a proper UUID to prevent path injection."""
        try:
            uuid.UUID(analysis_id)
            return analysis_id
        except (ValueError, AttributeError):
            raise ValueError(f"Invalid analysis ID format: {analysis_id}")

    def save_analysis(self, analysis: dict) -> str:
        """Save a single analysis result to disk."""
        analysis_id = analysis.get("id")

        if not analysis_id:
            raise ValueError("Analysis must contain an 'id' field.")

        analysis_id = self._safe_id(analysis_id)
        analysis_path = self.base_dir / f"{analysis_id}.json"

        with open(analysis_path, "w") as f:
            json.dump(analysis, f)

        self.indices[analysis_id] = str(analysis_path)
        self._update_index()

        return analysis_id

    def load_analysis(self, analysis_id: str) -> dict | None:
        """Load a single analysis result by ID."""
        analysis_id = self._safe_id(analysis_id)
        analysis_path = self.indices.get(analysis_id)

        if analysis_path and os.path.exists(analysis_path):
            with open(analysis_path, "r") as f:
                return json.load(f)

        return None

    def load_all_analyses(self) -> list:
        """Load all stored analyses."""
        analyses = []
        for analysis_id in self.indices:
            analysis = self.load_analysis(analysis_id)
            if analysis:
                analyses.append(analysis)
        return analyses