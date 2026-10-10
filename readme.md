# Python AI Agent 🤖

A terminal-based AI assistant powered by Google's Gemini 3.8 Flash, orchestrated with LangChain and LangGraph. This agent features conversational memory and custom, zero-dependency tools for interacting with the real world.

## Features
- **Conversational Memory:** Uses LangGraph's `MemorySaver` to track thread state and remember context across the chat session.
- **Custom Tools:** Equipped with Python-native tools to break out of the AI's isolated sandbox:
  - `get_current_time`: Aware of current dates and times.
  - `get_weather`: Fetches live, real-world weather data without requiring API keys (via wttr.in).
- **Fast & Modern:** Built using `uv` for lightning-fast dependency management.

## Prerequisites
1. Install [uv](https://docs.astral.sh/uv/) (The blazingly fast Python package manager).
2. Get a free [Google Gemini API Key](https://aistudio.google.com/app/apikey).

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GreenPlayerManghiam/Python-AI-Agent-in-VS-Code.git
   cd Python-AI-Agent-in-VS-Code
   ```

2. **Set up your environment variables:**
   Create a `.env` file in the root directory and add your API key:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

3. **Install dependencies and run the agent:**
   Because this project uses `uv`, you don't even need to manually create a virtual environment. Just run:
   ```bash
   uv run .\main.py
   ```

## Usage
Once the agent starts, simply type your messages in the terminal. The agent will automatically decide when to just chat and when to silently trigger its background tools to fetch live data. Type `quit` to exit the application.