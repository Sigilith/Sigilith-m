def normalize_sequence(sequence):
    """Normalize input sequence."""
    return sequence.strip() if isinstance(sequence, str) else []
