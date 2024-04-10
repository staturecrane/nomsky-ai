import json
import typing

from langchain_community.chat_models import ChatOllama
from topics import prompts


llm = ChatOllama(
    model="gemma:2b-instruct-q4_0",
    base_url="http://host.docker.internal:11434",
    num_gpu=-1,
)


def extract_topics_and_sections(input_string: str) -> typing.Any:
    if "```json" in input_string:
        response_json = input_string.split("```json")[1].split("```")[0].strip()
    else:
        response_json = input_string.strip()

    return json.loads(response_json)


def predict_topics(content: str) -> typing.Any:
    temperature = 0.0

    for _ in range(10):
        try:
            ollama_response = llm.invoke(
                f"{prompts.TOPICS_PROMPT}\n{content}", temperature=temperature
            )
            parsed = extract_topics_and_sections(ollama_response.content)
            sections = parsed["sections"]

            [x["topic"] and x["section_content"] for x in sections]

            return sections
        except:
            temperature += 0.05

    return None
