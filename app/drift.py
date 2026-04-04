import numpy as np
from typing import List

def compute_drift_trajectory(signatures: List[dict]) -> dict:
    """
    Compute temporal drift trajectory across a list of signatures.
    
    Args:
        signatures: List of dicts, each containing:
            - "vector": list[float]
            - "signature": dict (with regime_class, etc.)
            - "timestamp": str (ISO 8601) or None
            - "sequence_id": str (optional)
    
    Returns:
        dict with trajectory steps and summary metrics
    """
    if not signatures:
        return {
            "trajectory": [],
            "summary": {
                "total_steps": 0,
                "total_drift": 0.0,
                "average_drift_per_step": 0.0,
                "regime_changes": 0,
                "regime_change_points": [],
                "drift_trend": "N/A"
            }
        }
    
    trajectory = []
    cumulative_drift = 0.0
    drift_magnitudes = []
    regime_changes = 0
    regime_change_points = []
    prev_vector = None
    prev_regime = None
    
    for step, sig in enumerate(signatures):
        vector = np.array(sig.get("vector", []), dtype=float)
        regime_class = sig.get("signature", {}).get("regime_class", "UNKNOWN")
        timestamp = sig.get("timestamp")
        
        drift_magnitude = 0.0
        if prev_vector is not None and len(vector) > 0:
            drift_magnitude = float(np.linalg.norm(vector - prev_vector))
            cumulative_drift += drift_magnitude
            drift_magnitudes.append(drift_magnitude)
        
        regime_changed = False
        if prev_regime is not None and regime_class != prev_regime:
            regime_changed = True
            regime_changes += 1
            regime_change_points.append(step)
        
        trajectory.append({
            "step": step,
            "timestamp": timestamp,
            "vector": vector.tolist() if len(vector) > 0 else [],
            "drift_magnitude": drift_magnitude,
            "cumulative_drift": cumulative_drift,
            "regime_class": regime_class,
            "regime_changed": regime_changed
        })
        
        prev_vector = vector
        prev_regime = regime_class
    
    # Compute drift trend
    drift_trend = _classify_drift_trend(drift_magnitudes)
    
    average_drift = cumulative_drift / len(signatures) if signatures else 0.0;
    
    summary = {
        "total_steps": len(signatures),
        "total_drift": cumulative_drift,
        "average_drift_per_step": average_drift,
        "regime_changes": regime_changes,
        "regime_change_points": regime_change_points,
        "drift_trend": drift_trend
    }
    
    return {
        "trajectory": trajectory,
        "summary": summary
    }


def _classify_drift_trend(drift_magnitudes: List[float]) -> str:
    """
    Classify drift trend as 'accelerating', 'stable', or 'decelerating'.
    
    Uses simple heuristic: compare avg of first third vs last third.
    """
    if len(drift_magnitudes) < 3:
        return "stable"
    
    first_third = drift_magnitudes[:len(drift_magnitudes)//3 + 1]
    last_third = drift_magnitudes[-len(drift_magnitudes)//3 - 1:]
    
    avg_first = np.mean(first_third) if first_third else 0.0
    avg_last = np.mean(last_third) if last_third else 0.0
    
    threshold = 0.1  # 10% difference threshold
    
    if avg_last > avg_first * (1 + threshold):
        return "accelerating"
    elif avg_first > avg_last * (1 + threshold):
        return "decelerating"
    else:
        return "stable"