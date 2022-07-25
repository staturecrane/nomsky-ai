import os

import tensorflow as tf
import tensorflow_datasets as tfds
import tqdm

from typing import List

from nomsky.tokenizers.tokenizer import pre_tokenizer


def generate_dataset():
    dataset: tf.python.data.ops.dataset_ops.PrefetchDataset = tfds.load(
        "lm1b", data_dir="data"
    )["train"]

    root_dir: str = "data/local/wikipedia"
    os.makedirs(root_dir, exist_ok=True)

    with open(os.path.join(root_dir, "fasttext.txt"), "w") as fasttext_file:
        for sample in tqdm.tqdm(dataset):
            text: List[str] = [
                x[0]
                for x in pre_tokenizer.pre_tokenize_str(
                    sample["text"].numpy().decode("utf-8")
                )
            ]
            fasttext_file.write(" ".join(text) + "\n")


if __name__ == "__main__":
    generate_dataset()
