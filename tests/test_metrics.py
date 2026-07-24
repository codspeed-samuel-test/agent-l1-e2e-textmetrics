from textmetrics import jaccard_similarity, levenshtein, ngram_counts, word_frequencies


def test_word_frequencies():
    assert word_frequencies("the cat and the hat") == {"the": 2, "cat": 1, "and": 1, "hat": 1}


def test_word_frequencies_strips_punctuation():
    assert word_frequencies("Hello, hello!") == {"hello": 2}


def test_levenshtein():
    assert levenshtein("kitten", "sitting") == 3
    assert levenshtein("", "abc") == 3
    assert levenshtein("same", "same") == 0


def test_ngram_counts():
    assert ngram_counts("abab") == {"ab": 2, "ba": 1}


def test_jaccard_similarity():
    assert jaccard_similarity("red green blue", "green blue yellow") == 0.5
    assert jaccard_similarity("", "") == 1.0
