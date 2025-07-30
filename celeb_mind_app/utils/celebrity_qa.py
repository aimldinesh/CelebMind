import os
import requests


class QAEngine:
    """
    Handles question answering about celebrities using Groq's LLaMA-4 API.
    """

    def __init__(self):
        # Load the API key securely from environment variables
        self.api_key = os.getenv("GROQ_API_KEY")

        # Define the Groq API endpoint and model
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "meta-llama/llama-4-maverick-17b-128e-instruct"

    def ask_about_celebrity(self, name: str, question: str) -> str:
        """
        Ask a factual question about a specific celebrity.

        Args:
            name (str): Celebrity's full name.
            question (str): User's question.

        Returns:
            str: AI-generated answer or fallback message.
        """

        # Prepare request headers for Groq API
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        # Improved and structured prompt
        prompt = (
            f"You are a knowledgeable and concise AI assistant specialized in celebrities and public figures.\n"
            f"Your job is to accurately answer user questions about {name} using factual, verifiable information.\n"
            f"\n"
            f"Please answer the following question clearly and briefly:\n"
            f"Q: {question}\n"
            f"\n"
            f"If the answer is unknown or speculative, respond with 'I'm not sure about that.'"
        )

        # Construct the API request payload
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.5,
            "max_tokens": 512,
        }

        # Make the request to Groq API
        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"[ERROR] Failed to query Groq API: {e}")
            return "Sorry, I couldn't retrieve an answer at the moment."

        # Extract and return the AI's response
        return (
            response.json()
            .get("choices", [{}])[0]
            .get("message", {})
            .get("content", "No response.")
        )
