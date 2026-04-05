def compute_risk_score(signature):
    """Compute risk score from signature."""
    return {
        "risk": "MEDIUM" if signature.get("drift", 0) > 0.5 else "LOW",
        "score": 0.5
    }
