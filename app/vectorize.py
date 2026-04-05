import numpy as np

def signature_to_vector(signature: dict) -> np.ndarray:
    return np.array([
        signature.get("length", 0) / 100.0,
        signature.get("stability", 0.5),
        signature.get("drift", 0.3)
    ], dtype=float)