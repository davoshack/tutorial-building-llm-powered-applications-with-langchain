# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv
from IPython.display import display, Markdown

def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key

def get_gemini_api_key():
    load_env()
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    return gemini_api_key

def get_deeplake_api_key():
    load_env()
    deeplake_api_key = os.getenv("DEEPLAKE_API_KEY")
    return deeplake_api_key

def print_response(text):
    display(Markdown(text))