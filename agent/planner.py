import re

def intent_agent(goal: str) -> str:
    """
    Detects what the user wants to do.
    """
    goal = goal.lower()

    if any(word in goal for word in ["search", "find", "look", "get", "latest", "top", "best"]):
        return "search"

    return "unknown"


def planner_agent(goal: str) -> list:
    """
    Converts user goal into executable steps.
    """

    # Remove filler words
    cleaned_goal = re.sub(
        r"\b(search|find|look for|get|latest|top|best|show me|tell me)\b",
        "",
        goal,
        flags=re.IGNORECASE
    ).strip()

    return [f"Search DuckDuckGo for {cleaned_goal}"]


def plan(goal: str):
    """
    Multi-agent planner:
    Intent Agent → Planner Agent → Steps
    """

    print("[INTENT AGENT] Understanding goal...")
    intent = intent_agent(goal)

    if intent == "search":
        print("[PLANNER AGENT] Creating search plan...")
        return planner_agent(goal)

    print("[PLANNER AGENT] Unknown intent, defaulting to search")
    return [f"Search DuckDuckGo for {goal}"]
