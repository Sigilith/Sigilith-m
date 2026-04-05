def compute_risk_score(signature):
    """Compute risk score from signature."""
    drift = signature.get("drift", 0)
    risk_score = 0.5 + (drift * 0.3)
    risk = "HIGH" if risk_score > 0.7 else ("MEDIUM" if risk_score > 0.4 else "LOW")
    return {
        "risk": risk,
        "score": risk_score
    }
