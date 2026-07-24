"""Small, pure text-statistics functions."""

from collections import Counter


def word_frequencies(text: str) -> dict[str, int]:
    """Count case-insensitive word occurrences."""
    words = [w.strip(".,;:!?\"'()[]") for w in text.lower().split()]
    return dict(Counter(w for w in words if w))


def levenshtein(a: str, b: str) -> int:
    """Classic dynamic-programming edit distance."""
    if not a:
        return len(b)
    if not b:
        return len(a)
    previous = list(range(len(b) + 1))
    for i, char_a in enumerate(a, start=1):
        current = [i]
        for j, char_b in enumerate(b, start=1):
            insert = current[j - 1] + 1
            delete = previous[j] + 1
            substitute = previous[j - 1] + (char_a != char_b)
            current.append(min(insert, delete, substitute))
        previous = current
    return previous[-1]


def ngram_counts(text: str, n: int = 2) -> dict[str, int]:
    """Count character n-grams in the given text."""
    if n < 1:
        raise ValueError("n must be >= 1")
    return dict(Counter(text[i : i + n] for i in range(len(text) - n + 1)))


def jaccard_similarity(left: str, right: str) -> float:
    """Measure overlap between the unique words in two strings."""
    left_words = set(left.lower().split())
    right_words = set(right.lower().split())
    union = left_words | right_words
    return len(left_words & right_words) / len(union) if union else 1.0
