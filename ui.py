"""UI layout helpers for the Hugging Face Streamlit app."""

from typing import Any, Dict
import streamlit as st


def render_generation_result(data: Dict[str, Any]) -> None:
    """Render generated output and optional raw payload."""
    st.subheader("Generated Output")
    st.write(data.get("generated_text", ""))

    with st.expander("Response metadata"):
        st.write(f"Model: {data.get('model', '')}")
        st.json(data.get("raw_response", {}))
