import streamlit as st
import os

from stt.speech_to_text import transcribe_audio
from llm.intent_classifier import classify_intent
from tools.file_ops import create_file
from tools.code_generator import generate_code
from tools.summarizer import summarize_text

st.title("Voice AI Agent")

uploaded_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

if uploaded_file is not None:
    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.read())

    st.info("Processing audio...")

    text = transcribe_audio("temp.wav")
    intent = classify_intent(text)

    st.subheader("Transcription")
    st.write(text)

    st.subheader("Detected Intent")
    st.write(intent)

    result = ""

    if intent == "create_file":
        result = create_file("new_file.txt")

    elif intent == "write_code":
        code = generate_code(text)
        file_path = "output/generated_code.py"

        os.makedirs("output", exist_ok=True)
        with open(file_path, "w") as f:
            f.write(code)

        result = f"Code saved at {file_path}"

    elif intent == "summarize":
        result = summarize_text(text)

    else:
        result = "Chat response not implemented yet."

    st.subheader("Result")
    st.write(result)