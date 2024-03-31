from datasets import load_dataset

dataset = load_dataset("wiki40b", "en")

for sample in dataset["train"]:
    print(sample)
    break