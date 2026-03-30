import os
from dotenv import load_dotenv
from agents.orchestrator import Orchestrator
 
load_dotenv()  # Loads your .env file automatically
 
def main():
    print("\n" + "="*50)
    print("   AGENTIC RESEARCH SYSTEM")
    print("   GPT + Gemini + Grok + Auto Presentation")
    print("="*50 + "\n")
 
    topic = input("Enter your research topic: ").strip()
    if not topic:
        print("No topic entered. Exiting.")
        return
 
    orchestrator = Orchestrator()
    orchestrator.run(topic)
 
if __name__ == "__main__":
    main()