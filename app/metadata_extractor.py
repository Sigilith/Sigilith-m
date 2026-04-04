class MetadataExtractor:
    def __init__(self, sequences):
        self.sequences = sequences

    def shannon_entropy(self):
        import math
        total_length = sum(len(seq) for seq in self.sequences)
        probabilities = [len(seq) / total_length for seq in self.sequences]
        return -sum(p * math.log2(p) for p in probabilities if p > 0)

    def character_classification(self):
        classification = {}
        for seq in self.sequences:
            for char in seq:
                classification[char] = classification.get(char, 0) + 1
        return classification

    def frequency_distribution(self):
        distribution = {}
        for seq in self.sequences:
            for char in seq:
                distribution[char] = distribution.get(char, 0) + 1
        return distribution