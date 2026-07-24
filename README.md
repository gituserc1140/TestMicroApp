# Hugging Face Streamlit Micro App

This repository is a Streamlit app where the end user provides a Hugging Face token in the frontend and uses it to run model inference through Hugging Face's Inference API.

## Features
- Streamlit frontend for prompt input
- Frontend token entry (password field)
- Configurable Hugging Face model name
- Adjustable generation settings (`max_new_tokens`, `temperature`)
- Generated output plus expandable raw API response

## Project structure
- `/home/runner/work/TestMicroApp/TestMicroApp/app.py` — Streamlit entrypoint
- `/home/runner/work/TestMicroApp/TestMicroApp/api_client.py` — Hugging Face request logic
- `/home/runner/work/TestMicroApp/TestMicroApp/ui.py` — rendering helpers
- `/home/runner/work/TestMicroApp/TestMicroApp/config/settings.py` — defaults and env config
- `/home/runner/work/TestMicroApp/TestMicroApp/requirements.txt` — dependencies

## Quick start
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   streamlit run app.py
   ```

3. In the UI, provide:
   - a Hugging Face token
   - model id (default is `mistralai/Mistral-7B-Instruct-v0.2`)
   - prompt and generation settings

## Environment variables
- `HF_INFERENCE_BASE_URL` (default: `https://api-inference.huggingface.co/models`)
- `DEFAULT_MODEL`
- `DEFAULT_TIMEOUT`
- `DEFAULT_MAX_NEW_TOKENS`
- `DEFAULT_TEMPERATURE`

## Notes
- Tokens are not persisted by the app.
- Ensure your Hugging Face token has access to the selected model.
