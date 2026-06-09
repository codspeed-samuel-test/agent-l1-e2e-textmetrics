from textmetrics import levenshtein, ngram_counts, word_frequencies

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


def test_ngram_counts_short(benchmark):
    benchmark(ngram_counts, SAMPLE_TEXT)


def test_ngram_counts_long(benchmark):
    benchmark(ngram_counts, LONG_TEXT)


def test_ngram_trigrams(benchmark):
    benchmark(ngram_counts, SAMPLE_TEXT, 3)
