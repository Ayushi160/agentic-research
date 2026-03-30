import os
import requests
from openai import OpenAI

class GPTAgent:
    """
    Tries OpenAI GPT-4o first.
    If quota is exceeded or key is missing, falls back to Ollama.
    Make sure Ollama is running: `ollama run llama3` in a separate terminal.
    """
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.use_ollama = False

        if not self.api_key:
            print("[GPT] No OpenAI key found — using Ollama (llama3) instead.")
            self.use_ollama = True
        else:
            self.client = OpenAI(api_key=self.api_key)
            self.model = "gpt-4o"

    def research(self, topic: str) -> str:
        if self.use_ollama:
            return self._ollama_research(topic)
        try:
            return self._openai_research(topic)
        except Exception as e:
            if "insufficient_quota" in str(e) or "429" in str(e):
                print("[GPT] OpenAI quota exceeded — switching to Ollama (llama3).")
                self.use_ollama = True
                return self._ollama_research(topic)
            raise

    def _openai_research(self, topic: str) -> str:
        print(f"[GPT/OpenAI] Researching: {topic}")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert research assistant. "
                        "Provide a thorough, well-structured research summary "
                        "with key facts, statistics, recent developments, and subtopics. "
                        "Use ## headings for each section."
                    )
                },
                {"role": "user", "content": f"Research this topic in depth: {topic}"}
            ],
            max_tokens=1500,
            temperature=0.7
        )
        result = response.choices[0].message.content
        print("[GPT/OpenAI] Done.")
        return result

    def _ollama_research(self, topic: str) -> str:
        print(f"[GPT/Ollama llama3] Researching: {topic}")
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3",
                    "prompt": (
                        f"You are an expert research assistant. "
                        f"Research this topic thoroughly and provide a structured summary "
                        f"with key facts, statistics, and subtopics. "
                        f"Use ## headings.\n\nTopic: {topic}"
                    ),
                    "stream": False
                },
                timeout=120
            )
            result = response.json().get("response", "No response from Ollama.")
            print("[GPT/Ollama] Done.")
            return result
        except requests.exceptions.ConnectionError:
            raise Exception(
                "Ollama is not running! Open a new terminal and run: ollama run llama3\n"
                "Then try again."
            )