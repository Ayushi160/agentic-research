# 🤖 Agentic AI Research System

An automated multi-agent system that performs deep research using multiple AI models, combines insights, and generates presentation-ready outputs.

---

## 🚀 Overview

This project simulates a human-like research workflow by:

* Querying multiple AI models (GPT, Gemini, Ollama)
* Comparing and merging responses
* Generating structured summaries
* Creating presentation-ready content automatically
* Handling failures with retry and fallback mechanisms

---

## 🧠 Features

* 🔹 Multi-agent architecture (Research + Summary + Output)
* 🔹 Multi-model integration (OpenAI GPT, Google Gemini, Ollama fallback)
* 🔹 Automated workflow execution
* 🔹 Retry & fallback handling for API failures
* 🔹 Presentation generation (.pptx)
* 🔹 Logging system for transparency

---

## 🛠️ Tech Stack

* Python
* OpenAI API (GPT)
* Google Gemini API
* Ollama (local LLM fallback)
* PyAutoGUI (basic UI automation)
* python-pptx (presentation generation)

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/agentic-research.git
cd agentic-research
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API Keys

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
```

### 4. Run the system

```bash
python main.py
```

---

## 🔄 Workflow

1. User enters a research topic
2. System queries multiple AI models
3. Responses are collected and compared
4. A structured summary is generated
5. Presentation slides are created
6. Outputs are saved automatically

---

## 📊 Example Workflows

* AI in Healthcare and Diagnostics
* Hydrogen in Clean Energy Transition
* AI in Cybersecurity

---

## 📁 Output Structure

```
outputs/
│
├── summaries/
│   └── topic_summary.txt
│
├── presentations/
│   └── topic_presentation.pptx
│
└── logs/
    └── execution_log.txt
```

---

## 🎥 Demo

The demo video demonstrates:

* System setup
* Execution of workflow
* Multi-model interaction
* Output generation (summary + presentation)

---

## ⚠️ Notes

* Gemini and Grok APIs may require billing or credits
* Fallback mechanisms are implemented for reliability
* Grok may be replaced due to limited API access

---

## 🧪 Evaluation Focus

This project demonstrates:

* Multi-step workflow automation
* Integration of multiple AI systems
* Error handling and resilience
* Practical usability of AI agents

---

## 👩‍💻 Author

Ayushi Joshi

---

## ⭐ Conclusion

This system showcases how AI agents can autonomously perform research, synthesize information, and generate structured outputs — simulating real-world intelligent workflows.

---
