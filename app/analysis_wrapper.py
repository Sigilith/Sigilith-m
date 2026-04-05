import uuid
from datetime import datetime
from app import config


def wrap_analysis(raw_output: dict) -> dict:
    """
    Wrap analysis output with metadata: UUID, timestamp, risk/regime classification.

    Args:
        raw_output: Dict containing entropy, transition_density, risk_score, sequence

    Returns:
        Dict with id, timestamp, sequence, risk, regime_class, and all metrics
    """
    analysis_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    risk_score = raw_output.get("risk_score", 0)
    entropy = raw_output.get("entropy", 0)

    # Use app.config for unified classification
    risk = config.classify_risk(risk_score)
    regime = config.classify_regime(entropy)

    return {
        "id": analysis_id,
        "timestamp": timestamp,
        "sequence": raw_output.get("sequence", ""),
        "risk": risk,
        "regime_class": regime,
        "entropy": entropy,
        "transition_density": raw_output.get("transition_density", 0),
        "risk_score": risk_score,
        "vector": raw_output.get("vector", []),
        "summary": raw_output.get("summary", ""),
    }
