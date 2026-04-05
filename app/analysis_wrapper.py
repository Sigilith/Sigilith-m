import uuid
from datetime import datetime, timezone
from app import config


def normalize_risk(risk_value):
    """Normalize the risk value between 0 and 1."""
    if isinstance(risk_value, str):
        return 0.5  # Default for unknown risk
    return min(1.0, max(0.0, risk_value / 100.0))


def normalize_regime(regime_value):
    """Normalize the regime value between 0 and 1."""
    if isinstance(regime_value, str):
        return 0.5  # Default for unknown regime
    return min(1.0, max(0.0, (regime_value - 1) / 2.0))


def wrap_analysis(raw_output):
    """
    Wrap analysis with UUID, timestamp, and classification using app.config.

    Args:
        raw_output (dict): Raw analysis output containing:
            - entropy: float
            - transition_density: float
            - risk_score: float
            - risk: str or None
            - regime_class: str or None
            - sequence: str (optional)

    Returns:
        dict: Wrapped analysis with id, timestamp, classifications, and metadata
    """
    analysis_id = str(uuid.uuid4())
    timestamp = datetime.now(timezone.utc).isoformat()

    risk_score = raw_output.get("risk_score", 0)
    regime_score = raw_output.get("entropy", 0)

    risk = config.classify_risk(risk_score)
    regime = config.classify_regime(regime_score)

    return {
        "id": analysis_id,
        "timestamp": timestamp,
        "sequence": raw_output.get("sequence", ""),
        "risk": risk,
        "regime_class": regime,
        "entropy": raw_output.get("entropy", 0),
        "transition_density": raw_output.get("transition_density", 0),
        "risk_score": risk_score,
    }
