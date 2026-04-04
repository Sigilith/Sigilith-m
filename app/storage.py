import json
import os
from datetime import datetime
from pathlib import Path
import uuid
from typing import Optional


DATA_DIR = "data"
OUTPUTS_DIR = os.path.join(DATA_DIR, "outputs")
INDEX_FILE = os.path.join(DATA_DIR, "index.json")

def ensure_directories():
    """Create necessary directories if they don't exist."""
    Path(OUTPUTS_DIR).mkdir(parents=True, exist_ok=True)

def save_analysis(result: dict, context: Optional[dict] = None) -> str:
    """
    Save an analysis result as a JSON file in data/outputs/.
    
    Args:
        result: The analysis result dict (from analyze_sequence)
        context: Optional additional context (tags, source, etc.)
    
    Returns:
        The file path where the analysis was saved
    """
    ensure_directories()
    
    # Generate filename: <timestamp>_<shortid>.json
    timestamp = datetime.utcnow().isoformat() + "Z"
    short_id = str(uuid.uuid4())[:8]
    filename = f"{timestamp.replace(':', '-').replace('.', '-')}_{short_id}.json"
    file_path = os.path.join(OUTPUTS_DIR, filename)
    
    # Prepare the full data to save
    data_to_save = {
        "timestamp": timestamp,
        "sequence_id": short_id,
        **result,
        "context": context or {}
    }
    
    # Write to file
    with open(file_path, "w") as f:
        json.dump(data_to_save, f, indent=2)
    
    # Update index
    update_index({
        "file_path": file_path,
        "timestamp": timestamp,
        "risk": result.get("risk", {}).get("risk", "UNKNOWN"),
        "regime_class": result.get("signature", {}).get("regime_class", "UNKNOWN"),
        "context": context or {}
    })
    
    return file_path

def update_index(entry: dict):
    """
    Append metadata to data/index.json.
    
    Args:
        entry: Dict with keys:
            - file_path
            - timestamp
            - risk
            - regime_class
            - context (optional)
    """
    ensure_directories()
    
    # Load existing index or create new
    index = load_index()
    
    # Append new entry
    index.append(entry)
    
    # Write back to file
    with open(INDEX_FILE, "w") as f:
        json.dump(index, f, indent=2)

def load_index() -> list[dict]:
    """
    Load and return the index of all stored analyses.
    
    Returns:
        List of index entries
    """
    ensure_directories()
    
    if not os.path.exists(INDEX_FILE):
        return []
    
    try:
        with open(INDEX_FILE, "r") as f:
            index = json.load(f)
        return index if isinstance(index, list) else []
    except (json.JSONDecodeError, IOError):
        return []

def initialize_index():
    """Initialize data/index.json as an empty list if it doesn't exist."""
    ensure_directories()
    
    if not os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "w") as f:
            json.dump([], f)