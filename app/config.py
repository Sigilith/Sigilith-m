# app/config.py

# Configuration constants
RISK_THRESHOLD = 0.7  # Threshold above which risk is HIGH
RISK_MEDIUM_THRESHOLD = 0.4  # Threshold above which risk is MEDIUM
REGIME_LEVELS = {
    'stable': (0.0, 0.3),
    'transitional': (0.3, 0.7),
    'chaotic': (0.7, 1.0),
}

def classify_risk(score):
    """
    Classifies the risk level based on the provided score.

    Parameters:
    score (float): The risk score to be classified.

    Returns:
    str: 'HIGH', 'MEDIUM', or 'LOW'
    """
    if score >= RISK_THRESHOLD:
        return "HIGH"
    elif score >= RISK_MEDIUM_THRESHOLD:
        return "MEDIUM"
    else:
        return "LOW"

def classify_regime(score):
    """
    Classifies the regime based on the provided entropy score.

    Parameters:
    score (float): The entropy score to be classified.

    Returns:
    str: 'stable', 'transitional', or 'chaotic'
    """
    for regime, (lower, upper) in REGIME_LEVELS.items():
        if lower <= score <= upper:
            return regime
    return "chaotic"
