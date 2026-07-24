"""Streamlit app for Hugging Face text generation using user-provided token."""

import streamlit as st
import api_client
import ui
from config import settings

st.set_page_config(page_title="Hugging Face Micro App", layout="centered")

st.title("Hugging Face Micro App")
st.write("Use your Hugging Face token on the frontend to run inference against a model.")

hf_token = st.text_input("Hugging Face token", type="password", help="Token is sent only for this request.")
model = st.text_input("Model", value=settings.DEFAULT_MODEL)
prompt = st.text_area("Prompt", value="Write a short product description for a reusable water bottle.")
max_new_tokens = st.slider("Max new tokens", min_value=16, max_value=1024, value=settings.DEFAULT_MAX_NEW_TOKENS, step=8)
temperature = st.slider("Temperature", min_value=0.1, max_value=2.0, value=settings.DEFAULT_TEMPERATURE, step=0.1)

if st.button("Generate"):
    try:
        result = api_client.generate_text(
            prompt=prompt,
            token=hf_token,
            model=model,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
        )
        ui.render_generation_result(result)
    except Exception as exc:
        st.error(str(exc))
else:
    st.info("Enter your token, choose a model, add a prompt, then click Generate.")
