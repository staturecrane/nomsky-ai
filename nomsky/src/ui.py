import io
import streamlit as st


from unstructured.chunking.title import chunk_by_title
from unstructured.partition.auto import partition

from topics import predict as topics_predict
from embed import predict as embed_predict

st.title("Nomsky")

col_one, col_two = st.columns(2)

if "contexts" not in st.session_state:
    st.session_state["contexts"] = {}

with st.form("Add sources"):
    uploaded_files = st.file_uploader("Add files", accept_multiple_files=True)
    website = st.text_input("Add a website", key="website")

    submit_button = st.form_submit_button("Go!")

    if submit_button:
        for file in uploaded_files:
            if st.session_state["contexts"].get(file.name) is None:
                with st.spinner(f"Analyzing {file.name}"):
                    st.session_state["contexts"][file.name] = chunk_by_title(
                        partition(file=io.BytesIO(file.read()))
                    )

        if website:
            if st.session_state["contexts"].get(website) is None:
                st.session_state["contexts"][website] = chunk_by_title(
                partition(url=website)
            )

for filename, context in st.session_state["contexts"].items():
    progress_bar = st.progress(0)

    with st.container(border=True):
        for idx, element in enumerate(context):
            progress_bar.progress((idx + 1) * (1 / len(context)))
            predictions = topics_predict.predict_topics(element.text)

            if predictions is not None:
                topics = [x["topic"] for x in predictions]
                contents = [x["section_content"] for x in predictions]

                embed_predict.insert_vectors(topics, contents)

if st.session_state["contexts"]:
    search_query = st.text_input("Search for something")