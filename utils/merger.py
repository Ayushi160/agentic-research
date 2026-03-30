from datetime import datetime

def merge_research(topic: str, results: dict) -> str:
    """
    Takes a dict of {agent_name: research_text} and merges
    them into one structured summary document.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = []
    lines.append("=" * 60)
    lines.append(f"RESEARCH REPORT: {topic.upper()}")
    lines.append(f"Generated: {timestamp}")
    lines.append(f"Sources: {', '.join(results.keys())}")
    lines.append("=" * 60)
    lines.append("")

    for agent_name, content in results.items():
        lines.append(f"## {agent_name.upper()} RESEARCH")
        lines.append("-" * 40)
        lines.append(content.strip())
        lines.append("")
        lines.append("")

    lines.append("=" * 60)
    lines.append("## COMBINED KEY INSIGHTS")
    lines.append("-" * 40)
    lines.append(
        "The above sections represent independent research from multiple AI systems. "
        "Each agent was prompted with the same topic but approaches it from its own perspective:\n"
        "- GPT focuses on structured facts and statistics\n"
        "- Gemini focuses on trends and analysis\n"
        "- Grok focuses on unique insights and contrarian views\n\n"
        "Together they provide a comprehensive, multi-perspective research base."
    )
    lines.append("=" * 60)

    return "\n".join(lines)