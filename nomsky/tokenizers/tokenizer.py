import string

from typing import List, Tuple

from tokenizers.pre_tokenizers import BertPreTokenizer

CHAR_TO_IDX = {char: idx for idx, char in enumerate(string.printable)}
IDX_TO_CHAR = {idx: char for char, idx in CHAR_TO_IDX.items()}

pre_tokenizer = BertPreTokenizer()


def nomsky_tokenizer(text: str) -> List[List[Tuple[str, int]]]:
    word_tokens: List[Tuple[str, Tuple[int, int]]] = pre_tokenizer.pre_tokenize_str(
        text
    )

    char_tokens: List[List[Tuple[str, int]]] = [
        [(char, char_idx) for char in chars[0] if (char_idx := CHAR_TO_IDX.get(char))]
        for chars in word_tokens
    ]

    return char_tokens
