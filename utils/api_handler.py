"""
Functions for communicating with Groq API
This file manages API calls and error handling
"""

import os
import requests  # For HTTP requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Groq API information
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Get API key from .env file
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  # Groq API endpoint


def generate_text(prompt, content_type, tone, length):
    """
    Generates text using Groq API

    Args:
        prompt (str): Topic or instruction written by user
        content_type (str): Content type description
        tone (str): Tone description
        length (tuple): Minimum and maximum word count

    Returns:
        str: Generated text or error message
    """

    try:
        # Create system prompt (telling AI its role)
        system_prompt = f"""You are a professional content writer. 
        Your task is to create {content_type} type content.
        Tone: {tone}
        Length: Must be between {length[0]}-{length[1]} words."""

        # Required headers for API request
        # Authorization header sends the API key
        # Bearer keyword specifies token type
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        # Data to send to API
        # model: One of the available models in Groq
        # llama-3.1-8b-instant is a fast and lightweight model
        data = {
            "model": "llama-3.1-8b-instant",  # Groq's best general-purpose model
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,  # Creativity level (0-2 range, 0.7 is balanced)
            "max_tokens": 2000  # Maximum number of tokens to generate
        }

        # Send POST request to API
        # timeout parameter means wait 30 seconds, then timeout
        response = requests.post(GROQ_API_URL, headers=headers, json=data, timeout=30)

        # Check response
        # 200 status code means success
        if response.status_code == 200:
            result = response.json()  # Parse JSON response
            generated_text = result["choices"][0]["message"]["content"]  # Get generated text
            return generated_text
        else:
            # If there's an error, return error code and message
            return f"API Error: {response.status_code} - {response.text}"

    except Exception as e:
        # If an exception occurs (internet disconnected, timeout, etc.)
        return f"Error occurred: {str(e)}"