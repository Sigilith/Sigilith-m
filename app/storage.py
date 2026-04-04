# Simple in-memory store for testing
STORE = {}


def save_analysis(analysis: dict) -> str:
    """
    Saves the analysis object in memory.
    Returns the analysis ID.
    """
    analysis_id = analysis["id"]
    STORE[analysis_id] = analysis
    return analysis_id


def load_analysis(analysis_id: str):
    """
    Retrieves an analysis by ID.
    Returns None if not found.
    """
    return STORE.get(analysis_id)
