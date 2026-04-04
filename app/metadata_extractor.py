import numpy as np
import matplotlib.pyplot as plt

class MetadataExtractor:
    def __init__(self, sequence: str):
        self.sequence = sequence
        self.length = len(sequence)
        self.nucleotide_counts = self.count_nucleotides()
        self.gc_content = self.calculate_gc_content()

    def count_nucleotides(self):
        counts = {
            'A': self.sequence.count('A'),
            'T': self.sequence.count('T'),
            'C': self.sequence.count('C'),
            'G': self.sequence.count('G')
        }
        return counts

    def calculate_gc_content(self):
        gc = self.nucleotide_counts['G'] + self.nucleotide_counts['C']
        return (gc / self.length) * 100 if self.length > 0 else 0

    def length_analysis(self):
        return self.length

    def base_frequency_distribution(self):
        bases = list(self.nucleotide_counts.keys())
        frequencies = list(self.nucleotide_counts.values())
        plt.bar(bases, frequencies, color=['blue', 'red', 'green', 'orange'])
        plt.title('Base Frequency Distribution')
        plt.xlabel('Nucleotide')
        plt.ylabel('Frequency')
        plt.show()

# Example usage
if __name__ == '__main__':
    sequence = 'ATGCATGCAATGC'
    extractor = MetadataExtractor(sequence)
    print(f'Length: {extractor.length_analysis()}')
    print(f'GC Content: {extractor.gc_content:.2f}%')
    print(f'Nucleotide Counts: {extractor.nucleotide_counts}')
    extractor.base_frequency_distribution()