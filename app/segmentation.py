def segment_sequence(sequence):
    """Segment sequence into tokens."""
    if isinstance(sequence, str):
        return list(sequence)
    return []
