"""Hugging Face API client used by the Streamlit frontend."""

from typing import Any, Dict
import requests
from config import settings


def _extract_generated_text(payload: Any) -> str:
    """Best-effort extraction of generated text from Hugging Face responses."""
    if isinstance(payload, list) and payload:
        first = payload[0]
        if isinstance(first, dict):
            if "generated_text" in first:
                return str(first["generated_text"])
            if "summary_text" in first:
                return str(first["summary_text"])
            if "translation_text" in first:
                return str(first["translation_text"])

    if isinstance(payload, dict):
        if "generated_text" in payload:
            return str(payload["generated_text"])
        if "error" in payload:
            raise RuntimeError(str(payload["error"]))

    return str(payload)


def generate_text(
    prompt: str,
    token: str,
    model: str,
    max_new_tokens: int = 128,
    temperature: float = 0.7,
) -> Dict[str, Any]:
    """Call the Hugging Face Inference API for text generation."""
    if not token:
        raise ValueError("A Hugging Face token is required.")
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")
    if not model.strip():
        raise ValueError("Model cannot be empty.")

    url = f"{settings.HF_INFERENCE_BASE_URL.rstrip('/')}/{model.strip()}"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
    }
    body = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": int(max_new_tokens),
            "temperature": float(temperature),
            "return_full_text": False,
        },
    }

    response = requests.post(url, headers=headers, json=body, timeout=settings.DEFAULT_TIMEOUT)
    response.raise_for_status()

    try:
        parsed: Any = response.json()
    except ValueError:
        parsed = response.text

    return {
        "model": model.strip(),
        "prompt": prompt,
        "raw_response": parsed,
        "generated_text": _extract_generated_text(parsed),
    }
