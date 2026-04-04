# Sequence Analyzer

class SequenceAnalyzer:
    def __init__(self, sequence):
        self.sequence = sequence
        self.metadata = self.extract_metadata()

    def extract_metadata(self):
        length = len(self.sequence)
        gc_content = self.calculate_gc_content()
        return {'length': length, 'gc_content': gc_content}

    def calculate_gc_content(self):
        g_count = self.sequence.count('G')
        c_count = self.sequence.count('C')
        total = len(self.sequence)
        return (g_count + c_count) / total if total > 0 else 0

    def classify_sequence(self):
        if self.metadata['gc_content'] > 0.6:
            return 'High-GC'
        elif self.metadata['gc_content'] < 0.4:
            return 'Low-GC'
        else:
            return 'Moderate-GC'