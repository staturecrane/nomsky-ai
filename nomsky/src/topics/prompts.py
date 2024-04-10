TOPICS_PROMPT = """
Break up the provided content into short (1-3 sentence) section paragraphs that each correspond to a single topic of the content.
Ensure each section is a verbatim and contiguous paragraph from the original content.
Assign each section a 3-5 word topic title that can be understood outside of the content.
Do not return any text except the output schema. Do not add any formatting to the output text.

Return back your topics and sections formatted in JSON output. Enclose your output in ```json and ```, and use the following schema:

OUTPUT:
```json
{
    "sections": [{
        "topic": "topic here",
        "section_content": "section content here"
    }]
}
```
"""
