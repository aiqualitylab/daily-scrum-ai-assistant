# 🗣️ Daily Scrum AI Assistant

A powerful command-line tool powered by OpenAI that helps Scrum teams collect daily updates, identify blockers, and generate actionable insights for more effective daily standups.

## 📦 Installation

### 1. Clone this repository

```bash
git clone https://github.com/aiqualitylab/daily-scrum-ai-assistant.git
cd daily-scrum-ai-assistant
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up API key

- Open `.env` and paste your OpenAI API key:

```bash
OPENAI_API_KEY=sk-xxxxxx
```

## 🚀 Usage

### Add Daily Update

Collect a team member's daily scrum update:

```bash
python scrum.py add
```

You'll be prompted:

```
Enter your daily update (Yesterday / Today / Blockers): Fixed login bug, working on payment API, blocked by database access
Enter your name: Sarah
✅ Saved update from Sarah
```

Run the command for each team member participating in the daily standup.

### List All Updates

Show all collected daily updates:

```bash
python scrum.py list
```

Output:

```
--- Daily Scrum Updates ---
[Sarah] Fixed login bug, working on payment API, blocked by database access
[Mike] Completed user tests, starting mobile UI, no blockers
[Alex] Reviewed PRs yesterday, fixing flaky tests today, waiting for staging deployment
```

### Generate Scrum Summary

Create an AI-powered summary with individual updates, common blockers, and action items:

```bash
python scrum.py summarize
```

Example output:

```
--- Daily Scrum Summary ---

1. **Per Team Member**
- Sarah: Yesterday fixed login bug, today working on payment API, blocked by database access issues
- Mike: Completed user acceptance tests, starting mobile UI development, no current blockers
- Alex: Reviewed pull requests yesterday, focusing on flaky test fixes today, waiting for staging deployment

2. **Common Blockers**
- Infrastructure dependencies (database access, staging deployment)
- Testing reliability issues
- External system dependencies

3. **Action Items**
- Scrum Master: Follow up with DevOps team on database access permissions for Sarah
- Team: Prioritize staging deployment to unblock Alex
- Sarah & Alex: Collaborate on database-related testing issues
- Schedule technical debt discussion for flaky tests in next retrospective
```

### Reset Updates

Clear all stored updates to start fresh for the next day:

```bash
python scrum.py reset
```

Output:

```
🗑️ Cleared all updates.
```

## 🛠 Requirements

- **Python 3.8+**
- **OpenAI API key** (get one at [platform.openai.com](https://platform.openai.com))

## 📁 Project Structure

```
daily-scrum-ai-assistant/
├── scrum.py              # Main CLI application
├── requirements.txt      # Python dependencies
├── .env                 # Your API keys (create from .env.example)
├── scrum_updates.json   # Stored daily updates (auto-generated)
└── README.md           # This file
```

## 🎯 Features

- **Quick update collection** - Gather team updates in seconds via CLI
- **Structured format** - Follows Yesterday/Today/Blockers scrum format
- **AI-powered analysis** - Identifies patterns and blockers across team updates
- **Actionable insights** - Generates specific action items for Scrum Masters
- **Local storage** - All data stays on your machine
- **Daily reset** - Easy cleanup for fresh daily standups

## 💡 Use Cases

- **Remote daily standups** - Collect async updates before the meeting
- **Scrum Master preparation** - Get insights before facilitating the standup
- **Blocker tracking** - Identify and address team impediments quickly
- **Team communication** - Improve visibility across team members
- **Meeting efficiency** - Reduce standup time with pre-analyzed updates

## 🎪 Perfect Workflow

- **Before the daily standup** - Each team member runs `python scrum.py add`
- **During preparation** - Scrum Master runs `python scrum.py summarize`
- **In the meeting** - Focus on discussing blockers and action items
- **After the standup** - Run `python scrum.py reset` to prepare for tomorrow

**Happy sprinting! 🏃‍♂️💨**
