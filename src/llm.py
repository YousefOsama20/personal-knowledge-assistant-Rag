import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

class GeminiLLM:
    def __init__(self,model: str = "gemini-3.1-flash-lite-preview",):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not set."
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = model

    def generate(
        self,
        prompt: str,
    ) -> str:
        """Generate an answer using Gemini."""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text
