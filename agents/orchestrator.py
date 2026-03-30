import os
from agents.gpt_agent import GPTAgent
from agents.gemini_agent import GeminiAgent
from agents.grok_agent import GrokAgent
from utils.merger import merge_research
from utils.logger import Logger
from workflows.research_flow import ResearchFlow
from workflows.presentation_flow import PresentationFlow

class Orchestrator:
    def __init__(self):
        self.logger = Logger()
        self.logger.log("Orchestrator initialized.")

        # Initialize agents (will raise if keys missing)
        try:
            self.gpt = GPTAgent()
            self.logger.log("GPT Agent ready.")
        except ValueError as e:
            self.logger.log(f"WARNING: {e}")
            self.gpt = None

        try:
            self.gemini = GeminiAgent()
            self.logger.log("Gemini Agent ready.")
        except ValueError as e:
            self.logger.log(f"WARNING: {e}")
            self.gemini = None

        try:
            self.grok = GrokAgent()
            self.logger.log("Grok Agent ready.")
        except ValueError as e:
            self.logger.log(f"WARNING: {e}")
            self.grok = None

    def run(self, topic: str):
        self.logger.log(f"Starting research workflow for topic: {topic}")
        print(f"\n{'='*50}")
        print(f"Topic: {topic}")
        print(f"{'='*50}\n")

        # Step 1: Run research flow
        research_flow = ResearchFlow(self.gpt, self.gemini, self.grok, self.logger)
        results = research_flow.run(topic)

        if not results:
            print("No results collected. Check your API keys.")
            return

        # Step 2: Merge all results
        self.logger.log("Merging research outputs...")
        merged = merge_research(topic, results)

        # Step 3: Save merged summary
        summary_path = f"outputs/summaries/{topic[:40].replace(' ', '_')}_summary.txt"
        os.makedirs("outputs/summaries", exist_ok=True)
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(merged)
        self.logger.log(f"Summary saved to {summary_path}")
        print(f"\n✅ Summary saved: {summary_path}")

        # Step 4: Generate presentation content
        pres_flow = PresentationFlow(self.logger)
        pres_flow.run(topic, merged)

        self.logger.log("Workflow complete.")
        print("\n✅ All done! Check the outputs/ folder.")