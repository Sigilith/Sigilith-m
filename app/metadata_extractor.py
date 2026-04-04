import math
from collections import Counter
import string


class MetadataExtractor:
    """
    Computes structural metadata for one or more sequences.
    Case‑sensitive, punctuation‑sensitive, whitespace‑preserving.
    """

    def __init__(self, sequences):
        # Accept either a single string or a list of strings
        if isinstance(sequences, str):
            self.sequences = [sequences]
        else:
            self.sequences = sequences

    # ------------------------------------------------------------
    # Mode Detection
    # ------------------------------------------------------------
    def detect_mode(self):
        """
        Token mode if any sequence contains whitespace-separated tokens.
        Otherwise character mode.
        """
        for seq in self.sequences:
            if " " in seq.strip():
                return "token"
        return "character"

    # ------------------------------------------------------------
    # Entropy
    # ------------------------------------------------------------
    def shannon_entropy(self):
        """
        Shannon entropy across all symbols in all sequences.
        """
        all_chars = []
        for seq in self.sequences:
            all_chars.extend(list(seq))

        total = len(all_chars)
        if total == 0:
            return 0.0

        counts = Counter(all_chars)
        entropy = 0.0

        for c in counts.values():
            p = c / total
            entropy -= p * math.log2(p)

        return entropy

    # ------------------------------------------------------------
    # Character Classification
    # ------------------------------------------------------------
    def classify_char(self, c: str) -> str:
        if c.isalpha():
            return "alphabetic"
        if c.isdigit():
            return "numeric"
        if c.isspace():
            return "whitespace"
        return "symbolic"

    def character_classification(self):
        """
        Returns a dict of character classes → counts.
        Only meaningful in character mode.
        """
        class_counts = Counter()
        for seq in self.sequences:
            for c in seq:
                class_counts[self.classify_char(c)] += 1
        return dict(class_counts)

    # ------------------------------------------------------------
    # Frequency Distribution
    # ------------------------------------------------------------
    def frequency_distribution(self):
        """
        Returns a dict of symbol → count across all sequences.
        """
        distribution = Counter()
        for seq in self.sequences:
            for char in seq:
                distribution[char] += 1
        return dict(distribution)

    # ------------------------------------------------------------
    # Unified Metadata Extraction
    # ------------------------------------------------------------
    def extract(self):
        mode = self.detect_mode()

        # Flatten sequences into elements
        if mode == "token":
            elements = []
            for seq in self.sequences:
                elements.extend(seq.split())
        else:
            elements = []
            for seq in self.sequences:
                elements.extend(list(seq))

        total = len(elements)
        unique = len(set(elements))
        diversity = unique / total if total > 0 else 0

        freq = Counter(elements)
        freq_table = [
            {"symbol": sym, "count": cnt, "percent": (cnt / total) * 100}
            for sym, cnt in freq.most_common()
        ]

        class_breakdown = self.character_classification() if mode == "character" else {}

        return {
            "mode": mode,
            "length": total,
            "unique_symbols": unique,
            "diversity_ratio": diversity,
            "entropy": self.shannon_entropy(),
            "frequency_table": freq_table,
            "class_breakdown": class_breakdown,
        }
