# app/config.py

# Configuration constants
RISK_THRESHOLD = 0.7  # Example threshold for risk classification
REGIME_LEVELS = {
    'Bull Market': (0.7, 1.0),
    'Bear Market': (0.0, 0.3),
    'Sideways Market': (0.3, 0.7),
}

def classify_risk(score):
    """
    Classifies the risk level based on the provided score.

    Parameters:
    score (float): The risk score to be classified.

    Returns:
    str: A classification of the risk level.
    """
    if score >= RISK_THRESHOLD:
        return "High Risk"
    else:
        return "Low Risk"

def classify_regime(score):
    """
    Classifies the market regime based on the provided score.

    Parameters:
    score (float): The market score to be classified.

    Returns:
    str: A classification of the market regime.
    """
    for regime, (lower, upper) in REGIME_LEVELS.items():
        if lower <= score < upper:
            return regime
    return "Unknown"
