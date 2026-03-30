import time

class ResearchFlow:
    def __init__(self, gpt, gemini, grok, logger):
        self.gpt = gpt
        self.gemini = gemini
        self.grok = grok
        self.logger = logger

    def run(self, topic: str) -> dict:
        results = {}

        agents = {
            "GPT": self.gpt,
            "Gemini": self.gemini,
            "Grok": self.grok
        }

        for name, agent in agents.items():
            if agent is None:
                self.logger.log(f"Skipping {name} — not configured.")
                print(f"⚠️  Skipping {name} (no API key).")
                continue

            # Retry logic — up to 3 attempts
            for attempt in range(1, 4):
                try:
                    self.logger.log(f"[{name}] Attempt {attempt}...")
                    result = agent.research(topic)
                    results[name] = result
                    self.logger.log(f"[{name}] Success.")
                    break
                except Exception as e:
                    self.logger.log(f"[{name}] Attempt {attempt} failed: {e}")
                    print(f"⚠️  [{name}] Error: {e}. Retrying..." if attempt < 3 else f"❌ [{name}] Failed after 3 attempts.")
                    time.sleep(2)

        return results