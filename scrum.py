import os
import json
import requests
import typer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = typer.Typer()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("⚠️ Please set OPENAI_API_KEY in your .env file")

CHAT_URL = "https://api.openai.com/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
FILE = "scrum_updates.json"


def load_updates():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


def save_updates(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)


@app.command()
def add(
    update: str = typer.Option(None, prompt="Enter your daily update (Yesterday / Today / Blockers)"),
    member: str = typer.Option(None, prompt="Enter your name")
):
    """Add a daily scrum update from a team member."""
    data = load_updates()
    data.append({"member": member, "update": update})
    save_updates(data)
    print(f"✅ Saved update from {member}")


@app.command()
def list():
    """Show all updates collected so far."""
    data = load_updates()
    if not data:
        print("⚠️ No updates yet.")
        return
    print("\n--- Daily Scrum Updates ---")
    for item in data:
        print(f"[{item['member']}] {item['update']}")


@app.command()
def summarize():
    """Summarize scrum updates into per-person notes, common blockers, and team actions."""
    data = load_updates()
    if not data:
        print("⚠️ No updates to summarize.")
        return

    updates_text = "\n".join(f"[{item['member']}] {item['update']}" for item in data)

    # Scrum-specific prompt
    prompt = f"""
You are a Daily Scrum Meeting assistant.
Here are the team’s updates:

{updates_text}

Please provide the output in the following structured format:

1. **Per Team Member**
   - Summarize each member’s update (Yesterday, Today, Blockers).

2. **Common Blockers**
   - Identify recurring blockers or challenges across the team.

3. **Action Items**
   - Suggest clear, actionable steps for the team or Scrum Master to address blockers.
"""

    messages = [
        {"role": "system", "content": "You are a helpful Daily Scrum assistant."},
        {"role": "user", "content": prompt}
    ]

    try:
        response = requests.post(
            CHAT_URL,
            headers=HEADERS,
            json={"model": "gpt-4o-mini", "messages": messages, "temperature": 0.7},
            timeout=60
        )
        response.raise_for_status()
        summary = response.json()["choices"][0]["message"]["content"]

        print("\n--- Daily Scrum Summary ---")
        print(summary)

    except requests.exceptions.RequestException as e:
        print(f"❌ API request failed: {e}")
    except KeyError:
        print("❌ Unexpected response format from API")


@app.command()
def reset():
    """Clear all stored updates."""
    if os.path.exists(FILE):
        os.remove(FILE)
        print("🗑️ Cleared all updates.")
    else:
        print("⚠️ No updates file found.")


if __name__ == "__main__":
    app()
