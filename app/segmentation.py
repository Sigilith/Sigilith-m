def segment_sequence(sequence):
    """Segment sequence into character tokens."""
    if isinstance(sequence, str):
        return list(sequence)
    return []
