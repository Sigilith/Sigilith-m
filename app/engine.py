from app.normalization import normalize_sequence
from app.segmentation import segment_sequence
from app.transforms import apply_transforms
from app.signature import compute_signature
from app.scoring import compute_risk_score

def generate_summary(signature, risk):
    if risk["risk"] == "HIGH":
        return "High structural coherence under transformation; pattern consistent with malware-like behaviour."
    elif risk["risk"] == "LOW":
        return "Low structural stability; pattern resembles benign or random activity."
    else:
        return "Moderate structural consistency; further analysis recommended."

def analyze_sequence(sequence: list[str]) -> dict:
    # Step 0: normalization
    sequence = normalize_sequence(sequence)

    # Step 1: segmentation
    segments = segment_sequence(sequence)

    # Step 2: transform testing
    stability, drift = apply_transforms(segments)

    # Step 3: structural signature
    signature = compute_signature(segments, stability, drift)

    # Step 4: risk scoring
    risk = compute_risk_score(signature)

    return {
        "signature": signature,
        "risk": risk,
        "summary": generate_summary(signature, risk)
    }