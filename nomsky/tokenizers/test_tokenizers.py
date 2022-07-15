from nomsky.tokenizers.tokenizer import nomsky_tokenizer


def test_tokenizer():
    tokenized = nomsky_tokenizer("I had a good day at the beach!")

    assert tokenized == [
        [("I", 44)],
        [("h", 17), ("a", 10), ("d", 13)],
        [("a", 10)],
        [("g", 16), ("o", 24), ("o", 24), ("d", 13)],
        [("d", 13), ("a", 10), ("y", 34)],
        [("a", 10), ("t", 29)],
        [("t", 29), ("h", 17), ("e", 14)],
        [("b", 11), ("e", 14), ("a", 10), ("c", 12), ("h", 17)],
        [("!", 62)],
    ]
