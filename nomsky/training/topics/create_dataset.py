import re

from datasets import load_dataset


def parse_article(article: str):
    title = article.split("_START_ARTICLE_")[1].split("_START_SECTION_")[0].strip()

    if "_START_PARAGRAPH_" in title:
        title = title.split("_START_PARAGRAPH_")[0].strip()

    pattern = r"(?<=_START_SECTION_)(.*?)(?=_START_SECTION_|$)"

    matches = re.findall(pattern, article, re.DOTALL)

    return title, matches


dataset = load_dataset("wiki40b", "en").shuffle()
for sample in dataset["train"]:
    title, _ = parse_article(sample["text"])
    print(title)
