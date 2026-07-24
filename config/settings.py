"""Configuration settings for the Hugging Face Streamlit micro-app."""

import os

HF_INFERENCE_BASE_URL = os.getenv("HF_INFERENCE_BASE_URL", "https://api-inference.huggingface.co/models")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "mistralai/Mistral-7B-Instruct-v0.2")
# Slightly higher timeout to account for model cold starts and inference latency.
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "30"))
DEFAULT_MAX_NEW_TOKENS = int(os.getenv("DEFAULT_MAX_NEW_TOKENS", "128"))
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.7"))
