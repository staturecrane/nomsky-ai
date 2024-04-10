import nltk
from bs4 import BeautifulSoup

nltk.download("punkt")


def parse_html(html: str, max_content: int = 1028):
    html_text = BeautifulSoup(html).text
    sentences = nltk.tokenize.sent_tokenize(html_text)

    stripped_sentences = [x.strip().replace("\n\n", "") for x in sentences if x.strip()]

    contexts = []
    current_context = ""
    for sentence in stripped_sentences:
        if len(current_context) >= max_content:
            contexts.append(current_context)
            current_context = ""

        current_context += sentence

    if current_context:
        contexts.append(current_context)

    return contexts
