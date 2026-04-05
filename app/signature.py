def compute_signature(segments, stability, drift):
    """Compute structural signature."""
    return {
        "length": len(segments),
        "stability": stability,
        "drift": drift
    }
