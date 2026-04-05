HIGH_RISK_THRESHOLD = 0.7
MEDIUM_RISK_THRESHOLD = 0.4

CHAOTIC_THRESHOLD = 0.7
TRANSITIONAL_THRESHOLD = 0.4


def classify_risk(risk_score: float) -> str:
    if risk_score >= HIGH_RISK_THRESHOLD:
        return "HIGH"
    elif risk_score >= MEDIUM_RISK_THRESHOLD:
        return "MEDIUM"
    else:
        return "LOW"


def classify_regime(transition_density: float) -> str:
    if transition_density >= CHAOTIC_THRESHOLD:
        return "chaotic"
    elif transition_density >= TRANSITIONAL_THRESHOLD:
        return "transitional"
    else:
        return "stable"