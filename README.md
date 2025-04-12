# PromptPilot: Solo AI Ops in One File

PromptPilot is your launchpad for building and running lean, purpose-driven AI scripts – each packed into a single Python file. Designed to be fast, focused, and framework-free, these micro-agents are engineered for speed and clarity.

Each script solves a real-world task using structured prompting and GenAI function calling. Whether you're filtering a CSV, scraping web content, analyzing SQL, or transforming JSON, PromptPilot keeps things tight and tidy.

---

## ✨ Features

- **Single-File Simplicity** – One script, one purpose, zero clutter.
- **Model-Agnostic** – Support for OpenAI, Claude, Gemini, and others.
- **Plug-and-Play** – Run instantly with no need for complex project setup.
- **Prompt-Pattern Driven** – Built around reusable patterns, not fragile hacks.
- **Data-Ready** – Comes with test datasets for local experimentation.

---

## 🚀 Project Overview

PromptPilot is inspired by the idea of minimalism in GenAI. Instead of monolithic tools, it offers sharp, isolated agents that can be slotted into any developer workflow. With baked-in prompt structure and real input/output examples, each file acts as both tool and tutorial.

From database querying and file editing to content extraction and data transformation, PromptPilot helps you prototype and ship AI-powered utilities quickly and clearly.

---

## 📦 Installation

### Step 1 – Install `uv` (Modern Python Package Manager)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Step 2 – Clone the Repository

```bash
git clone https://github.com/CEORocks/promptpilot.git
cd promptpilot
```

### Step 3 – Set Up API Keys

```bash
export OPENAI_API_KEY="your-openai-key"
export ANTHROPIC_API_KEY="your-anthropic-key"
export GEMINI_API_KEY="your-gemini-key"
export FIRECRAWL_API_KEY="your-firecrawl-key"
```

---

## 🛠 Requirements

- Python 3.8 or newer  
- `uv` package manager  
- Relevant API keys for supported AI models  
- `jq` (for JSON agent)  
- DuckDB or SQLite CLI tools (for database agents)  

---

## 📂 Example Agents

### 🔍 CSV Analyzer (Polars + OpenAI)

```bash
uv run csv_analyzer_openai.py -i "data/users.csv" -p "Show average score for users above age 30"
```

### 🧠 Meta Prompt Generator (OpenAI)

```bash
uv run prompt_builder_openai.py \
    --purpose "Build flowcharts" \
    --instructions "Use mermaid.js syntax, keep structure clear and organized" \
    --variables "diagram-type,user-input"
```

### 💾 DuckDB Query Bot (Claude)

```bash
uv run db_query_claude.py -d data/analytics.db -p "List all users with a score over 90"
```

### 🔧 JSON Filter Agent (Gemini)

```bash
uv run json_filter_gemini.py --exe "Extract users with status active from data/users.json"
```

### 🌐 Web Scraper + Filter (OpenAI + Firecrawl)

```bash
uv run scraper_openai.py \
    --url "https://example.com" \
    --prompt "Extract all headings and descriptions" \
    --output results.md
```

### 🧑‍💻 Bash File Editor (Anthropic)

```bash
uv run bash_ops_anthropic.py --prompt "Append 'Thank you!' to summary.txt"
```

---

## 🧬 How It Works

Each script is a complete micro-agent:
- Prompts are structured and customizable
- Responses are parsed into precise tool actions
- Designed to loop and self-correct based on API output
- Can be extended or embedded into pipelines

---

## 📊 Test Data

This repo includes realistic datasets for testing:

- `data/analytics.db` – DuckDB sample with 30 mock users  
- `data/analytics.json` – JSON file with structured user data  
- `data/analytics.sqlite` – SQLite version of the above  

Attributes include: name, age, city, score, activity status, and creation date across diverse cities and scenarios.

---

## 🤝 Licensing and Credits

**License:** MIT License  
Use, fork, modify freely. Credit appreciated but not required.

**Built With:**
- [uv](https://github.com/astral/uv) for dependency isolation  
- [Polars](https://pola.rs/) for blazing fast CSV analytics  
- [DuckDB](https://duckdb.org/) for embedded SQL  
- [jq](https://stedolan.github.io/jq/) for structured JSON handling  
- Claude, Gemini, and OpenAI APIs for language model power  

---

## 🎯 Philosophy

PromptPilot isn’t a framework. It’s a mindset: start small, stay sharp, solve a need.  
Each agent is designed to teach by doing – and to run anywhere with almost no setup.  
Test, tweak, and build your own fleet of file-sized AI utilities.

---

> “AI doesn’t need more layers. It needs more clarity.”

Happy Piloting 🚀


