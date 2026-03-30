import os
from google import genai

class GeminiAgent:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-2.0-flash"   # current working model

    def research(self, topic: str) -> str:
        print(f"[Gemini] Researching: {topic}")
        prompt = (
            f"You are an expert analyst. Research the following topic and provide "
            f"a detailed analysis including current trends, challenges, opportunities, "
            f"and future outlook. Use ## headings for each section.\n\nTopic: {topic}"
        )
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        result = response.text
        print("[Gemini] Done.")
        return result