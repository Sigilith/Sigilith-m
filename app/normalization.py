def normalize_sequence(sequence):
    """Normalize input sequence."""
    if isinstance(sequence, str):
        return sequence.strip()
    return sequence
