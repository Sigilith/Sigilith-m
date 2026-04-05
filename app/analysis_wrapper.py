import uuid

from app import config


def wrap_analysis(raw_output: dict) -> dict:
    risk_score = raw_output.get("risk_score", 0.0)
    transition_density = raw_output.get("transition_density", 0.0)

    return {
        "id": str(uuid.uuid4()),
        "entropy": raw_output.get("entropy", 0.0),
        "transition_density": transition_density,
        "risk_score": risk_score,
        "risk": config.classify_risk(risk_score),
        "regime_class": config.classify_regime(transition_density),
    }
