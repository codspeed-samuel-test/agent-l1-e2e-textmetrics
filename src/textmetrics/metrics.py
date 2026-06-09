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
    b_len = len(b)
    previous = list(range(b_len + 1))
    for i, char_a in enumerate(a, start=1):
        current = [i]
        prev_idx = 1
        for char_b in b:
            insert = current[-1] + 1
            delete = previous[prev_idx] + 1
            substitute = previous[prev_idx - 1] + (char_a != char_b)
            current.append(min(insert, delete, substitute))
            prev_idx += 1
        previous = current
    return previous[-1]


def ngram_counts(text: str, n: int = 2) -> dict[str, int]:
    """Count character n-grams in the given text."""
    if n < 1:
        raise ValueError("n must be >= 1")
    return dict(Counter(text[i : i + n] for i in range(len(text) - n + 1)))
