import os
from openai import OpenAI

class GrokAgent:
    def __init__(self):
        api_key = os.getenv("GROK_API_KEY")
        if not api_key:
            raise ValueError("GROK_API_KEY not found in .env")
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.x.ai/v1"
        )
        self.model = "grok-3"   # current working model

    def research(self, topic: str) -> str:
        print(f"[Grok] Researching: {topic}")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a cutting-edge research AI. "
                        "When given a topic, provide unique insights, contrarian viewpoints, "
                        "real-world examples, and practical implications. "
                        "Be concise but comprehensive. Use ## headings for each section."
                    )
                },
                {
                    "role": "user",
                    "content": f"Give me deep research insights on: {topic}"
                }
            ],
            max_tokens=1500,
            temperature=0.8
        )
        result = response.choices[0].message.content
        print("[Grok] Done.")
        return result