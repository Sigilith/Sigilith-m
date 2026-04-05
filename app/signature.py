def compute_signature(segments, stability, drift):
    """Compute structural signature from segments."""
    return {
        "length": len(segments),
        "stability": stability,
        "drift": drift,
        "regex_class": "alphanumeric" if segments else "empty"
    }
