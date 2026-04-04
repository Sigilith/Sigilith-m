import numpy as np

def signature_to_vector(signature: dict) -> np.ndarray:
    return np.array([
        signature["segment_count"],
        signature["avg_segment_length"],
        signature["boundary_stability"],
        signature["drift_index"]
    ], dtype=float)