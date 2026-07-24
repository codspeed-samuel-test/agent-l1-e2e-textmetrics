from textmetrics import jaccard_similarity, levenshtein, ngram_counts, word_frequencies

SAMPLE_TEXT = (
    "the quick brown fox jumps over the lazy dog "
    "the quick brown fox jumps over the lazy dog "
    "the quick brown fox jumps over the lazy dog"
)

LONG_TEXT = " ".join(["Lorem ipsum dolor sit amet consectetur adipiscing elit"] * 50)


def test_word_frequencies_short(benchmark):
    benchmark(word_frequencies, SAMPLE_TEXT)


def test_word_frequencies_long(benchmark):
    benchmark(word_frequencies, LONG_TEXT)


def test_levenshtein_similar(benchmark):
    benchmark(levenshtein, "kitten", "sitting")


def test_levenshtein_long(benchmark):
    benchmark(levenshtein, "abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba")


def test_levenshtein_short_vs_long(benchmark):
    short_string = "hi"
    long_paragraph = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
        "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
        "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
        "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
        "culpa qui officia deserunt mollit anim id est laborum."
    )
    benchmark(levenshtein, short_string, long_paragraph)


def test_ngram_counts_short(benchmark):
    benchmark(ngram_counts, SAMPLE_TEXT)


def test_ngram_counts_long(benchmark):
    benchmark(ngram_counts, LONG_TEXT)


def test_ngram_trigrams(benchmark):
    benchmark(ngram_counts, SAMPLE_TEXT, 3)


def test_jaccard_similarity(benchmark):
    benchmark(jaccard_similarity, SAMPLE_TEXT, LONG_TEXT)
