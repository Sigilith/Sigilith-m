# Production-Ready MetadataExtractor Implementation

class MetadataExtractor:
    def __init__(self, sequences):
        self.sequences = sequences

    def detect_mode(self):
        # Implementation of mode detection
        pass

    def calculate_shannon_entropy(self):
        # Implementation of Shannon entropy
        pass

    def classify_characters(self):
        # Implementation of character classification
        pass

    def frequency_distribution(self):
        # Implementation of frequency distribution
        pass

    def process_sequences(self):
        # Process single or multiple sequences
        if isinstance(self.sequences, list):
            return [self.process_sequence(seq) for seq in self.sequences]
        else:
            return self.process_sequence(self.sequences)

    def process_sequence(self, sequence):
        # Implementation for processing a single sequence
        pass
