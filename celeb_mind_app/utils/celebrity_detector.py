import os
import base64
import requests


class CelebrityDetector:
    """
    This class handles celebrity recognition using the Groq API
    powered by the LLaMA-4 model via image-to-text reasoning.
    """

    def __init__(self):
        # Load API key from environment variables
        self.api_key = os.getenv("GROQ_API_KEY")

        # Groq's OpenAI-compatible endpoint for chat completions
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"

        # Model ID for LLaMA-4 (Maverick variant)
        self.model = "meta-llama/llama-4-maverick-17b-128e-instruct"

    def identify(self, image_bytes):
        """
        Identify the celebrity in the given image bytes using LLaMA-4.

        Args:
            image_bytes (bytes): JPEG image in byte format.

        Returns:
            Tuple[str, str]:
                - Full structured response from the model.
                - Extracted celebrity name (or "Unknown").
        """

        # Encode the image as base64 for API input
        encoded_image = base64.b64encode(image_bytes).decode()

        # Prepare headers for the Groq API call
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        # Prompt payload with user message and image content
        prompt = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "You are a celebrity recognition expert AI. \n"
                                "Identify the person in the image. If known, respond in this format:\n\n"
                                "- **Full Name**:\n"
                                "- **Profession**:\n"
                                "- **Nationality**:\n"
                                "- **Famous For**:\n"
                                "- **Top Achievements**:\n\n"
                                'If unknown, return "Unknown".'
                            ),
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{encoded_image}"
                            },
                        },
                    ],
                }
            ],
            "temperature": 0.3,
            "max_tokens": 1024,
        }

        # Make the POST request to the Groq API
        try:
            response = requests.post(self.api_url, headers=headers, json=prompt)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"[ERROR] Groq API call failed: {e}")
            return "Unknown", ""

        # Parse response content
        result = (
            response.json()
            .get("choices", [{}])[0]
            .get("message", {})
            .get("content", "Unknown")
        )
        name = self.extract_name(result)

        return result, name

    def extract_name(self, content):
        """
        Extract the full name of the celebrity from the model's response.

        Args:
            content (str): Structured response from the model.

        Returns:
            str: Extracted name or "Unknown".
        """
        for line in content.splitlines():
            if line.lower().startswith("- **full name**:"):
                return line.split(":", 1)[1].strip()

        return "Unknown"
