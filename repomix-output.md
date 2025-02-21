This file is a merged representation of a subset of the codebase, containing files not matching ignore patterns, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching these patterns are excluded: ai_docs
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded

## Additional Info

# Directory Structure
```
data/
  analytics.json
.gitignore
ai_code_basic.sh
ai_code_reflect.sh
create_db.py
gist_poc.py
gist_poc.sh
README.md
sfa_duckdb_anthropic_v2.py
sfa_duckdb_gemini_v1.py
sfa_duckdb_gemini_v2.py
sfa_duckdb_openai_v2.py
sfa_jq_gemini_v1.py
sfa_meta_prompt_openai_v1.py
sfa_poc.py
sfa_sqlite_openai_v2.py
```

# Files

## File: data/analytics.json
````json
[
  {
    "id": "94efbf8b-4c95-4feb-9eda-900192276be7",
    "name": "Fiona",
    "age": 33,
    "city": "Singapore",
    "score": 95.48,
    "is_active": true,
    "status": "active",
    "created_at": "2024-04-30"
  },
  {
    "id": "efcbb1f5-ffaf-4b40-a44b-cd67f6508eec",
    "name": "Alice",
    "age": 46,
    "city": "Paris",
    "score": 37.81,
    "is_active": false,
    "status": "active",
    "created_at": "2023-10-31"
  },
  {
    "id": "9c2378d3-f46d-4f19-8e9e-b9053e6e57ea",
    "name": "Charlie",
    "age": 54,
    "city": "Tokyo",
    "score": 86.24,
    "is_active": false,
    "status": "archived",
    "created_at": "2023-11-15"
  },
  {
    "id": "12a6dc88-1bd5-4a20-b729-e7a70918a60b",
    "name": "Charlie",
    "age": 31,
    "city": "Tokyo",
    "score": 61.24,
    "is_active": true,
    "status": "pending",
    "created_at": "2024-03-26"
  },
  {
    "id": "dc1cf50e-c3c2-4843-8137-131834f7b00a",
    "name": "Jane",
    "age": 26,
    "city": "London",
    "score": 22.61,
    "is_active": true,
    "status": "inactive",
    "created_at": "2024-11-04"
  },
  {
    "id": "db0ac268-3666-4a03-a284-e35380ae8c84",
    "name": "Jane",
    "age": 34,
    "city": "New York",
    "score": 3.1,
    "is_active": true,
    "status": "archived",
    "created_at": "2024-01-29"
  },
  {
    "id": "24ab09dd-163a-4faf-8e06-d3fb6418dec5",
    "name": "Alice",
    "age": 64,
    "city": "Tokyo",
    "score": 6.17,
    "is_active": true,
    "status": "pending",
    "created_at": "2024-03-08"
  },
  {
    "id": "27f8624d-c41a-4569-bbbb-1348b94fa0fd",
    "name": "Jane",
    "age": 34,
    "city": "Paris",
    "score": 43.44,
    "is_active": true,
    "status": "active",
    "created_at": "2023-04-19"
  },
  {
    "id": "1666fe7c-a2b1-44d5-abba-293c4e0f9b23",
    "name": "Charlie",
    "age": 58,
    "city": "Sydney",
    "score": 85.02,
    "is_active": true,
    "status": "active",
    "created_at": "2024-09-09"
  },
  {
    "id": "66036da1-7704-4ca6-9ec2-1e6d560db610",
    "name": "Alice",
    "age": 61,
    "city": "Singapore",
    "score": 93.69,
    "is_active": true,
    "status": "archived",
    "created_at": "2024-05-06"
  },
  {
    "id": "04fa9318-9e6d-4029-be2d-9bc7ecf37f3f",
    "name": "John",
    "age": 24,
    "city": "Tokyo",
    "score": 14.59,
    "is_active": true,
    "status": "inactive",
    "created_at": "2023-08-17"
  },
  {
    "id": "4586fbe1-acf9-4bfa-8237-ab697cdc69ed",
    "name": "Diana",
    "age": 43,
    "city": "Sydney",
    "score": 60.84,
    "is_active": true,
    "status": "archived",
    "created_at": "2023-11-06"
  },
  {
    "id": "20b827b3-f183-44db-9f4f-f30b361c8a83",
    "name": "Diana",
    "age": 63,
    "city": "Singapore",
    "score": 96.18,
    "is_active": false,
    "status": "inactive",
    "created_at": "2024-08-02"
  },
  {
    "id": "779dbbe0-b509-4332-98ee-d89887f48cec",
    "name": "Bob",
    "age": 47,
    "city": "Toronto",
    "score": 37.85,
    "is_active": false,
    "status": "active",
    "created_at": "2025-01-25"
  },
  {
    "id": "8612b8d7-4524-4575-a782-a01c4a0c88a3",
    "name": "Bob",
    "age": 25,
    "city": "Berlin",
    "score": 88.28,
    "is_active": false,
    "status": "pending",
    "created_at": "2025-01-16"
  },
  {
    "id": "ad992026-c339-40eb-a669-f16983d226ca",
    "name": "Diana",
    "age": 29,
    "city": "Berlin",
    "score": 84.17,
    "is_active": false,
    "status": "active",
    "created_at": "2023-07-26"
  },
  {
    "id": "b3ef272f-3fc9-4422-88db-ed39858f1f68",
    "name": "John",
    "age": 20,
    "city": "New York",
    "score": 78.33,
    "is_active": true,
    "status": "archived",
    "created_at": "2023-04-16"
  },
  {
    "id": "2a0ace4c-ee9e-4b6b-9005-897210109cca",
    "name": "Bob",
    "age": 49,
    "city": "Toronto",
    "score": 56.91,
    "is_active": false,
    "status": "active",
    "created_at": "2023-07-10"
  },
  {
    "id": "3674700e-a83f-4450-97c8-04f80f2d2e89",
    "name": "Charlie",
    "age": 30,
    "city": "Sydney",
    "score": 80.83,
    "is_active": false,
    "status": "active",
    "created_at": "2024-10-22"
  },
  {
    "id": "a17712d7-10f1-48e3-b1fd-8c65afb0442a",
    "name": "Jane",
    "age": 40,
    "city": "Toronto",
    "score": 35.85,
    "is_active": false,
    "status": "inactive",
    "created_at": "2024-02-03"
  },
  {
    "id": "3b1e3e89-9ccb-46cf-9954-cb0903e8e02d",
    "name": "Diana",
    "age": 48,
    "city": "Singapore",
    "score": 37.58,
    "is_active": true,
    "status": "inactive",
    "created_at": "2023-06-13"
  },
  {
    "id": "a4461690-a009-48c1-96d2-ed89dd1907a7",
    "name": "Diana",
    "age": 21,
    "city": "Tokyo",
    "score": 32.35,
    "is_active": false,
    "status": "pending",
    "created_at": "2024-06-03"
  },
  {
    "id": "7157129c-0b3d-4040-8609-65afe4322ed2",
    "name": "Alice",
    "age": 65,
    "city": "New York",
    "score": 40.59,
    "is_active": false,
    "status": "inactive",
    "created_at": "2024-02-19"
  },
  {
    "id": "dc3c472f-d16b-47e2-95c4-61c461e2b228",
    "name": "Diana",
    "age": 25,
    "city": "Singapore",
    "score": 48.32,
    "is_active": false,
    "status": "inactive",
    "created_at": "2024-10-03"
  },
  {
    "id": "34e6e614-f376-4c1c-b3b5-f2926987115f",
    "name": "Bob",
    "age": 30,
    "city": "Tokyo",
    "score": 72.08,
    "is_active": false,
    "status": "inactive",
    "created_at": "2024-10-09"
  },
  {
    "id": "2e4aded0-53aa-4668-b3b1-90f4747aa295",
    "name": "Fiona",
    "age": 20,
    "city": "Tokyo",
    "score": 88.64,
    "is_active": true,
    "status": "inactive",
    "created_at": "2023-04-08"
  },
  {
    "id": "2f65400e-3447-4944-9db3-af09bd4d57db",
    "name": "John",
    "age": 34,
    "city": "Toronto",
    "score": 54.75,
    "is_active": true,
    "status": "archived",
    "created_at": "2024-02-26"
  },
  {
    "id": "a667e148-4c64-4f5a-b23a-e00856feed8d",
    "name": "John",
    "age": 27,
    "city": "Singapore",
    "score": 33.5,
    "is_active": true,
    "status": "archived",
    "created_at": "2023-02-26"
  },
  {
    "id": "517c9c76-5c3e-497e-bd78-343ebd001668",
    "name": "Eric",
    "age": 23,
    "city": "Sydney",
    "score": 78.33,
    "is_active": true,
    "status": "inactive",
    "created_at": "2024-08-11"
  },
  {
    "id": "78a7f34f-7c0b-4e16-b57e-3829726569a7",
    "name": "Jane",
    "age": 32,
    "city": "Berlin",
    "score": 49.09,
    "is_active": false,
    "status": "archived",
    "created_at": "2023-10-19"
  }
]
````

## File: .gitignore
````
.aider*
session_dir/

data/*
!data/mock.json
!data/mock.db
!data/mock.sqlite
!data/analytics.json
!data/analytics.db
!data/analytics.sqlite

specs/

patterns.log
````

## File: ai_code_basic.sh
````bash
# aider --model groq/deepseek-r1-distill-llama-70b --no-detect-urls --no-auto-commit --yes-always --file *.py --message "$1"
# aider --deepseek --no-detect-urls --no-auto-commit --yes-always --file *.py --message "$1"

aider \
    --model o3-mini \
    --architect \
    --reasoning-effort high \
    --editor-model sonnet \
    --no-detect-urls \
    --no-auto-commit \
    --yes-always \
    --file *.py
````

## File: ai_code_reflect.sh
````bash
prompt="$1"

# first shot
aider \
    --model o3-mini \
    --architect \
    --reasoning-effort high \
    --editor-model sonnet \
    --no-detect-urls \
    --no-auto-commit \
    --yes-always \
    --file *.py \
    --message "$prompt"

# reflection
aider \
    --model o3-mini \
    --architect \
    --reasoning-effort high \
    --editor-model sonnet \
    --no-detect-urls \
    --no-auto-commit \
    --yes-always \
    --file *.py \
    --message "Double all changes requested to make sure they've been implemented: $prompt"
````

## File: create_db.py
````python
import json
import sqlite3
from datetime import datetime

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the User table
cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
    id TEXT PRIMARY KEY,
    name TEXT,
    age INTEGER,
    city TEXT,
    score REAL,
    is_active BOOLEAN,
    status TEXT,
    created_at DATE
)
''')

# Read the JSON file
with open('data/mock.json', 'r') as file:
    users = json.load(file)

# Insert data into the table
for user in users:
    cursor.execute('''
    INSERT INTO User (id, name, age, city, score, is_active, status, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        user['id'],
        user['name'],
        user['age'],
        user['city'],
        user['score'],
        user['is_active'],
        user['status'],
        user['created_at']
    ))

# Commit the changes and close the connection
conn.commit()
conn.close()
````

## File: gist_poc.py
````python
# /// script
# dependencies = [
#   "requests<3",
# ]
# ///

# Interesting idea here - we can store SFAs in gist - curl them then run them locally. Food for thought.

import requests


def fetch_gist_content():
    # 1. The raw link to your specific file in the Gist
    raw_url = "https://gist.githubusercontent.com/disler/d8d8abdb17b2072cff21df468607b176/raw/sfa_poc.py"

    try:
        # 2. Use requests to fetch the file's content
        response = requests.get(raw_url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # 3. Get the content
        sfa_poc_file_contents = response.text

        # 4. Print the content
        print(sfa_poc_file_contents)

        return sfa_poc_file_contents

    except requests.RequestException as e:
        print(f"Error fetching gist content: {e}")
        return None


if __name__ == "__main__":
    fetch_gist_content()
````

## File: gist_poc.sh
````bash
#!/usr/bin/env bash

# Interesting idea here - we can store SFAs in gist - curl them then run them locally. Food for thought.

# 1. The raw link to your specific file in the Gist.
#    Note: The exact raw link may change if the Gist is updated, so check the "Raw" button
#    in your Gist to make sure you have the correct URL.
RAW_URL="https://gist.githubusercontent.com/disler/d8d8abdb17b2072cff21df468607b176/raw/sfa_poc.py"

# 2. Use curl to fetch the file's content and store it in a variable.
SFA_POC_FILE_CONTENTS="$(curl -sL "$RAW_URL")"

# 3. Now you can do whatever you want with $SFA_POC_FILE_CONTENTS.
#    For example, just echo it:
echo "$SFA_POC_FILE_CONTENTS"
````

## File: README.md
````markdown
# Single File Agents (SFA)
> Premise: #1: What if we could pack single purpose, powerful AI Agents into a single python file?
> 
> Premise: #2: What's the best structural pattern for building Agents that can improve in capability as compute and intelligence increases?

![Single File Agents](images/single-file-agents-thumb.png)

## What is this?

A collection of powerful single-file agents built on top of [uv](https://github.com/astral/uv) - the modern Python package installer and resolver. 

These agents aim to do one thing and one thing only. They demonstrate precise prompt engineering and GenAI patterns for practical tasks many of which I share on the [IndyDevDan YouTube channel](https://www.youtube.com/@indydevdan). Watch us walk through the Single File Agent in [this video](https://youtu.be/YAIJV48QlXc).

This repo contains a few agents built across the big 3 GenAI providers (Gemini, OpenAI, Anthropic).

## Quick Start

Export your API keys:

```bash
export GEMINI_API_KEY='your-api-key-here'

export OPENAI_API_KEY='your-api-key-here'

export ANTHROPIC_API_KEY='your-api-key-here'
```

JQ Agent:

```bash
uv run sfa_jq_gemini_v1.py --exe "Filter scores above 80 from data/analytics.json and save to high_scores.json"
```

DuckDB Agent (OpenAI):

```bash
# Tip tier
uv run sfa_duckdb_openai_v2.py -d ./data/analytics.db -p "Show me all users with score above 80"
```

DuckDB Agent (Anthropic):

```bash
# Tip tier
uv run sfa_duckdb_anthropic_v2.py -d ./data/analytics.db -p "Show me all users with score above 80"
```

DuckDB Agent (Gemini):

```bash
# Buggy but usually works
uv run sfa_duckdb_gemini_v2.py -d ./data/analytics.db -p "Show me all users with score above 80"
```

SQLite Agent (OpenAI):

```bash
uv run sfa_sqlite_openai_v2.py -d ./data/analytics.sqlite -p "Show me all users with score above 80"
```

Meta Prompt Generator:

```bash
uv run sfa_meta_prompt_openai_v1.py \
    --purpose "generate mermaid diagrams" \
    --instructions "generate a mermaid valid chart, use diagram type specified or default flow, use examples to understand the structure of the output" \
    --sections "user-prompt" \
    --variables "user-prompt"
```



## Features

- **Self-contained**: Each agent is a single file with embedded dependencies
- **Minimal, Precise Agents**: Carefully crafted prompts for small agents that can do one thing really well
- **Modern Python**: Built on uv for fast, reliable dependency management
- **Run From The Cloud**: With uv, you can run these scripts from your server or right from a gist (see my gists commands)
- **Patternful**: Building effective agents is about setting up the right prompts, tools, and process for your use case. Once you setup a great pattern, you can re-use it over and over. That's part of the magic of these SFA's. 

## Test Data

The project includes a test duckdb database (`data/analytics.db`), a sqlite database (`data/analytics.sqlite`), and a JSON file (`data/analytics.json`) for testing purposes. The database contains sample user data with the following characteristics:

### User Table
- 30 sample users with varied attributes
- Fields: id (UUID), name, age, city, score, is_active, status, created_at
- Test data includes:
  - Names: Alice, Bob, Charlie, Diana, Eric, Fiona, Jane, John
  - Cities: Berlin, London, New York, Paris, Singapore, Sydney, Tokyo, Toronto
  - Status values: active, inactive, pending, archived
  - Age range: 20-65
  - Score range: 3.1-96.18
  - Date range: 2023-2025

Perfect for testing filtering, sorting, and aggregation operations with realistic data variations.

## Agents
> Note: We're using the term 'agent' loosely for some of these SFA's. We have prompts, prompt chains, and a couple are official Agents.

### JQ Command Agent 
> (sfa_jq_gemini_v1.py)

An AI-powered assistant that generates precise jq commands for JSON processing

Example usage:
```bash
# Generate and execute a jq command
uv run sfa_jq_gemini_v1.py --exe "Filter scores above 80 from data/analytics.json and save to high_scores.json"

# Generate command only
uv run sfa_jq_gemini_v1.py "Filter scores above 80 from data/analytics.json and save to high_scores.json"
```

### DuckDB Agents 
> (sfa_duckdb_openai_v2.py, sfa_duckdb_anthropic_v2.py, sfa_duckdb_gemini_v2.py, sfa_duckdb_gemini_v1.py)

We have three DuckDB agents that demonstrate different approaches and capabilities across major AI providers:

#### DuckDB OpenAI Agent (sfa_duckdb_openai_v2.py, sfa_duckdb_openai_v1.py)
An AI-powered assistant that generates and executes DuckDB SQL queries using OpenAI's function calling capabilities.

Example usage:
```bash
# Run DuckDB agent with default compute loops (10)
uv run sfa_duckdb_openai_v2.py -d ./data/analytics.db -p "Show me all users with score above 80"

# Run with custom compute loops 
uv run sfa_duckdb_openai_v2.py -d ./data/analytics.db -p "Show me all users with score above 80" -c 5
```

#### DuckDB Anthropic Agent (sfa_duckdb_anthropic_v2.py)
An AI-powered assistant that generates and executes DuckDB SQL queries using Claude's tool use capabilities.

Example usage:
```bash
# Run DuckDB agent with default compute loops (10)
uv run sfa_duckdb_anthropic_v2.py -d ./data/analytics.db -p "Show me all users with score above 80"

# Run with custom compute loops
uv run sfa_duckdb_anthropic_v2.py -d ./data/analytics.db -p "Show me all users with score above 80" -c 5
```

#### DuckDB Gemini Agent (sfa_duckdb_gemini_v2.py)
An AI-powered assistant that generates and executes DuckDB SQL queries using Gemini's function calling capabilities.

Example usage:
```bash
# Run DuckDB agent with default compute loops (10)
uv run sfa_duckdb_gemini_v2.py -d ./data/analytics.db -p "Show me all users with score above 80"

# Run with custom compute loops
uv run sfa_duckdb_gemini_v2.py -d ./data/analytics.db -p "Show me all users with score above 80" -c 5
```

### Meta Prompt Generator (sfa_meta_prompt_openai_v1.py)
An AI-powered assistant that generates comprehensive, structured prompts for language models.

Example usage:
```bash
# Generate a meta prompt using command-line arguments.
# Optional arguments are marked with a ?.
uv run sfa_meta_prompt_openai_v1.py \
    --purpose "generate mermaid diagrams" \
    --instructions "generate a mermaid valid chart, use diagram type specified or default flow, use examples to understand the structure of the output" \
    --sections "examples, user-prompt" \
    --examples "create examples of 3 basic mermaid charts with <user-chart-request> and <chart-response> blocks" \
    --variables "user-prompt"

# Without optional arguments, the script will enter interactive mode.
uv run sfa_meta_prompt_openai_v1.py \
    --purpose "generate mermaid diagrams" \
    --instructions "generate a mermaid valid chart, use diagram type specified or default flow, use examples to understand the structure of the output"

# Interactive Mode
# Just run the script without any flags to enter interactive mode.
# You'll be prompted step by step for:
# - Purpose (required): The main goal of your prompt
# - Instructions (required): Detailed instructions for the model
# - Sections (optional): Additional sections to include
# - Examples (optional): Example inputs and outputs
# - Variables (optional): Placeholders for dynamic content
uv run sfa_meta_prompt_openai_v1.py
```

### Git Agent
> Up for a challenge?

## Requirements

- Python 3.8+
- uv package manager
- GEMINI_API_KEY (for Gemini-based agents)
- OPENAI_API_KEY (for OpenAI-based agents) 
- ANTHROPIC_API_KEY (for Anthropic-based agents)
- jq command-line JSON processor (for JQ agent)
- DuckDB CLI (for DuckDB agents)

### Installing Required Tools

#### jq Installation

macOS:
```bash
brew install jq
```

Windows:
- Download from [stedolan.github.io/jq/download](https://stedolan.github.io/jq/download/)
- Or install with Chocolatey: `choco install jq`

#### DuckDB Installation

macOS:
```bash
brew install duckdb
```

Windows:
- Download the CLI executable from [duckdb.org/docs/installation](https://duckdb.org/docs/installation)
- Add the executable location to your system PATH

## Installation

1. Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone this repository:
```bash
git clone <repository-url>
```

3. Set your Gemini API key (for JQ generator):
```bash
export GEMINI_API_KEY='your-api-key-here'

# Set your OpenAI API key (for DuckDB agents):
export OPENAI_API_KEY='your-api-key-here'

# Set your Anthropic API key (for DuckDB agents):
export ANTHROPIC_API_KEY='your-api-key-here'
```

## Shout Outs + Resources for you
- [uv](https://github.com/astral/uv) - The engineers creating uv are built different. Thank you for fixing the python ecosystem.
- [Simon Willison](https://simonwillison.net) - Simon introduced me to the fact that you can [use uv to run single file python scripts](https://simonwillison.net/2024/Aug/20/uv-unified-python-packaging/) with dependencies. Massive thanks for all your work. He runs one of the most valuable blogs for engineers in the world.
- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) - A proper breakdown of how to build useful units of value built on top of GenAI.
- [Part Time Larry](https://youtu.be/zm0Vo6Di3V8?si=oBetAgc5ifhBmK03) - Larry has a great breakdown on the new Python GenAI library and delivers great hands on, actionable GenAI x Finance information.
- [Aider](https://aider.chat/) - AI Coding done right. Maximum control over your AI Coding Experience. Enough said.

---

- [New Gemini Python SDK](https://github.com/google-gemini/generative-ai-python)
- [Anthropic Agent Chatbot Example](https://github.com/anthropics/courses/blob/master/tool_use/06_chatbot_with_multiple_tools.ipynb)
- [Anthropic Customer Service Agent](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/customer_service_agent.ipynb)

## License

MIT License - feel free to use this code in your own projects.

If you find value from my work: give a shout out and tag my YT channel [IndyDevDan](https://www.youtube.com/@indydevdan).
````

## File: sfa_duckdb_anthropic_v2.py
````python
#!/usr/bin/env python3

# /// script
# dependencies = [
#   "anthropic>=0.45.2",
#   "rich>=13.7.0",
# ]
# ///

"""
/// Example Usage

# Run DuckDB agent with default compute loops (3)
uv run sfa_duckdb_anthropic_v2.py -d ./data/analytics.db -p "Show me all users with score above 80"

# Run with custom compute loops
uv run sfa_duckdb_anthropic_v2.py -d ./data/analytics.db -p "Show me all users with score above 80" -c 5

///
"""

import os
import sys
import json
import argparse
import subprocess
from typing import List
from rich.console import Console
from rich.panel import Panel
from anthropic import Anthropic

# Initialize rich console
console = Console()


AGENT_PROMPT = """<purpose>
    You are a world-class expert at crafting precise DuckDB SQL queries.
    Your goal is to generate accurate queries that exactly match the user's data needs.
</purpose>

<instructions>
    <instruction>Use the provided tools to explore the database and construct the perfect query.</instruction>
    <instruction>Start by listing tables to understand what's available.</instruction>
    <instruction>Describe tables to understand their schema and columns.</instruction>
    <instruction>Sample tables to see actual data patterns.</instruction>
    <instruction>Test queries before finalizing them.</instruction>
    <instruction>Only call run_final_sql_query when you're confident the query is perfect.</instruction>
    <instruction>Be thorough but efficient with tool usage.</instruction>
    <instruction>If you find your run_test_sql_query tool call returns an error or won't satisfy the user request, try to fix the query or try a different query.</instruction>
    <instruction>Think step by step about what information you need.</instruction>
    <instruction>Be sure to specify every parameter for each tool call.</instruction>
    <instruction>Every tool call should have a reasoning parameter which gives you a place to explain why you are calling the tool.</instruction>
</instructions>

<tools>
    <tool>
        <name>list_tables</name>
        <description>Returns list of available tables in database</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we need to list tables relative to user request</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>describe_table</name>
        <description>Returns schema info for specified table</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we need to describe this table</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>table_name</name>
                <type>string</type>
                <description>Name of table to describe</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>sample_table</name>
        <description>Returns sample rows from specified table, always specify row_sample_size</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we need to sample this table</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>table_name</name>
                <type>string</type>
                <description>Name of table to sample</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>row_sample_size</name>
                <type>integer</type>
                <description>Number of rows to sample aim for 3-5 rows</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>run_test_sql_query</name>
        <description>Tests a SQL query and returns results (only visible to agent)</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we're testing this specific query</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>sql_query</name>
                <type>string</type>
                <description>The SQL query to test</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>run_final_sql_query</name>
        <description>Runs the final validated SQL query and shows results to user</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Final explanation of how query satisfies user request</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>sql_query</name>
                <type>string</type>
                <description>The validated SQL query to run</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
</tools>

<user-request>
    {{user_request}}
</user-request>
"""


def list_tables(reasoning: str) -> List[str]:
    """Returns a list of tables in the database.

    The agent uses this to discover available tables and make informed decisions.

    Args:
        reasoning: Explanation of why we're listing tables relative to user request

    Returns:
        List of table names as strings
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c ".tables"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(f"[blue]List Tables Tool[/blue] - Reasoning: {reasoning}")
        return result.stdout.strip().split("\n")
    except Exception as e:
        console.log(f"[red]Error listing tables: {str(e)}[/red]")
        return []


def describe_table(reasoning: str, table_name: str) -> str:
    """Returns schema information about the specified table.

    The agent uses this to understand table structure and available columns.

    Args:
        reasoning: Explanation of why we're describing this table
        table_name: Name of table to describe

    Returns:
        String containing table schema information
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "DESCRIBE {table_name};"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(
            f"[blue]Describe Table Tool[/blue] - Table: {table_name} - Reasoning: {reasoning}"
        )
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error describing table: {str(e)}[/red]")
        return ""


def sample_table(reasoning: str, table_name: str, row_sample_size: int) -> str:
    """Returns a sample of rows from the specified table.

    The agent uses this to understand actual data content and patterns.

    Args:
        reasoning: Explanation of why we're sampling this table
        table_name: Name of table to sample from
        row_sample_size: Number of rows to sample aim for 3-5 rows

    Returns:
        String containing sample rows in readable format
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "SELECT * FROM {table_name} LIMIT {row_sample_size};"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(
            f"[blue]Sample Table Tool[/blue] - Table: {table_name} - Rows: {row_sample_size} - Reasoning: {reasoning}"
        )
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error sampling table: {str(e)}[/red]")
        return ""


def run_test_sql_query(reasoning: str, sql_query: str) -> str:
    """Executes a test SQL query and returns results.

    The agent uses this to validate queries before finalizing them.
    Results are only shown to the agent, not the user.

    Args:
        reasoning: Explanation of why we're running this test query
        sql_query: The SQL query to test

    Returns:
        Query results as a string
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "{sql_query}"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(f"[blue]Test Query Tool[/blue] - Reasoning: {reasoning}")
        console.log(f"[dim]Query: {sql_query}[/dim]")
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error running test query: {str(e)}[/red]")
        return str(e)


def run_final_sql_query(reasoning: str, sql_query: str) -> str:
    """Executes the final SQL query and returns results to user.

    This is the last tool call the agent should make after validating the query.

    Args:
        reasoning: Final explanation of how this query satisfies user request
        sql_query: The validated SQL query to run

    Returns:
        Query results as a string
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "{sql_query}"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(
            Panel(
                f"[green]Final Query Tool[/green]\nReasoning: {reasoning}\nQuery: {sql_query}"
            )
        )
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error running final query: {str(e)}[/red]")
        return str(e)


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="DuckDB Agent using Anthropic API")
    parser.add_argument(
        "-d", "--db", required=True, help="Path to DuckDB database file"
    )
    parser.add_argument("-p", "--prompt", required=True, help="The user's request")
    parser.add_argument(
        "-c",
        "--compute",
        type=int,
        default=10,
        help="Maximum number of agent loops (default: 3)",
    )
    args = parser.parse_args()

    # Configure the API key
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    if not ANTHROPIC_API_KEY:
        console.print(
            "[red]Error: ANTHROPIC_API_KEY environment variable is not set[/red]"
        )
        console.print("Please get your API key from your Anthropic dashboard")
        console.print("Then set it with: export ANTHROPIC_API_KEY='your-api-key-here'")
        sys.exit(1)

    # Set global DB_PATH for tool functions
    global DB_PATH
    DB_PATH = args.db

    # Initialize Anthropic client
    client = Anthropic()

    # Create a single combined prompt based on the full template
    completed_prompt = AGENT_PROMPT.replace("{{user_request}}", args.prompt)
    messages = [{"role": "user", "content": completed_prompt}]

    compute_iterations = 0

    # Main agent loop
    while True:
        console.rule(
            f"[yellow]Agent Loop {compute_iterations+1}/{args.compute}[/yellow]"
        )
        compute_iterations += 1

        if compute_iterations >= args.compute:
            console.print(
                "[yellow]Warning: Reached maximum compute loops without final query[/yellow]"
            )
            raise Exception(
                f"Maximum compute loops reached: {compute_iterations}/{args.compute}"
            )

        try:
            # Add the user's initial prompt if this is the first iteration
            if compute_iterations == 1:
                messages.append({"role": "user", "content": args.prompt})

            # Generate content with tool support
            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=messages,
                tools=[
                    {
                        "name": "list_tables",
                        "description": "Returns list of available tables in database",
                        "input_schema": {
                            "type": "object",
                            "properties": {
                                "reasoning": {
                                    "type": "string",
                                    "description": "Explanation for listing tables",
                                }
                            },
                            "required": ["reasoning"],
                        },
                    },
                    {
                        "name": "describe_table",
                        "description": "Returns schema info for specified table",
                        "input_schema": {
                            "type": "object",
                            "properties": {
                                "reasoning": {
                                    "type": "string",
                                    "description": "Why we need to describe this table",
                                },
                                "table_name": {
                                    "type": "string",
                                    "description": "Name of table to describe",
                                },
                            },
                            "required": ["reasoning", "table_name"],
                        },
                    },
                    {
                        "name": "sample_table",
                        "description": "Returns sample rows from specified table",
                        "input_schema": {
                            "type": "object",
                            "properties": {
                                "reasoning": {
                                    "type": "string",
                                    "description": "Why we need to sample this table",
                                },
                                "table_name": {
                                    "type": "string",
                                    "description": "Name of table to sample",
                                },
                                "row_sample_size": {
                                    "type": "integer",
                                    "description": "Number of rows to sample aim for 3-5 rows",
                                },
                            },
                            "required": ["reasoning", "table_name", "row_sample_size"],
                        },
                    },
                    {
                        "name": "run_test_sql_query",
                        "description": "Tests a SQL query and returns results (only visible to agent)",
                        "input_schema": {
                            "type": "object",
                            "properties": {
                                "reasoning": {
                                    "type": "string",
                                    "description": "Why we're testing this specific query",
                                },
                                "sql_query": {
                                    "type": "string",
                                    "description": "The SQL query to test",
                                },
                            },
                            "required": ["reasoning", "sql_query"],
                        },
                    },
                    {
                        "name": "run_final_sql_query",
                        "description": "Runs the final validated SQL query and shows results to user",
                        "input_schema": {
                            "type": "object",
                            "properties": {
                                "reasoning": {
                                    "type": "string",
                                    "description": "Final explanation of how query satisfies user request",
                                },
                                "sql_query": {
                                    "type": "string",
                                    "description": "The validated SQL query to run",
                                },
                            },
                            "required": ["reasoning", "sql_query"],
                        },
                    },
                ],
                tool_choice={"type": "any"},  # Always force a tool call
            )

            # Look for tool calls in the response (expecting ToolUseBlock objects)
            tool_calls = []

            for block in response.content:
                if hasattr(block, "type") and block.type == "tool_use":
                    tool_calls.append(block)

            if tool_calls:
                for tool_call in tool_calls:
                    tool_use_id = tool_call.id
                    func_name = tool_call.name
                    func_args = (
                        tool_call.input
                    )  # already a dict; no need to call json.loads

                    console.print(
                        f"[blue]Tool Call:[/blue] {func_name}({json.dumps(func_args)})"
                    )

                    messages.append({"role": "assistant", "content": response.content})

                    try:
                        if func_name == "list_tables":
                            result = list_tables(reasoning=func_args["reasoning"])
                        elif func_name == "describe_table":
                            result = describe_table(
                                reasoning=func_args["reasoning"],
                                table_name=func_args["table_name"],
                            )
                        elif func_name == "sample_table":
                            result = sample_table(
                                reasoning=func_args["reasoning"],
                                table_name=func_args["table_name"],
                                row_sample_size=func_args["row_sample_size"],
                            )
                        elif func_name == "run_test_sql_query":
                            result = run_test_sql_query(
                                reasoning=func_args["reasoning"],
                                sql_query=func_args["sql_query"],
                            )
                        elif func_name == "run_final_sql_query":
                            result = run_final_sql_query(
                                reasoning=func_args["reasoning"],
                                sql_query=func_args["sql_query"],
                            )
                            console.print("\n[green]Final Results:[/green]")
                            console.print(result)
                            return
                        else:
                            raise Exception(f"Unknown tool call: {func_name}")

                        console.print(
                            f"[blue]Tool Call Result:[/blue] {func_name}(...) ->\n{result}"
                        )

                        messages.append(
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "tool_result",
                                        "tool_use_id": tool_use_id,
                                        "content": str(result),
                                    }
                                ],
                            }
                        )

                    except Exception as e:
                        error_msg = f"Error executing {func_name}: {str(e)}"
                        console.print(f"[red]{error_msg}[/red]")
                        messages.append(
                            {
                                "role": "tool",
                                "content": error_msg,
                                "tool_call_id": tool_call.id,
                            }
                        )
                        continue

            else:
                raise Exception("No tool calls found in response - should never happen")

        except Exception as e:
            console.print(f"[red]Error in agent loop: {str(e)}[/red]")
            raise e


if __name__ == "__main__":
    main()
````

## File: sfa_duckdb_gemini_v1.py
````python
#!/usr/bin/env python3

# /// script
# dependencies = [
#   "google-genai>=1.1.0",
# ]
# ///

"""
/// Example Usage

# generates and executes DuckDB command (default)
uv run sfa_duckdb_gemini_v1.py --db ./data/analytics.db "Filter employees with salary above 50000 and export to high_salary_employees.csv"

# generates DuckDB command only without executing
uv run sfa_duckdb_gemini_v1.py --db ./data/analytics.db --no-exe "Select name and department from employees table and save to employees.json"

///
"""

import os
import sys
import argparse
import subprocess
from google import genai

DUCKDB_PROMPT = """<purpose>
    You are a world-class expert at crafting precise DuckDB CLI commands for database operations.
    Your goal is to generate accurate, minimal DuckDB commands that exactly match the user's data manipulation needs.
</purpose>

<instructions>
    <instruction>Return ONLY the DuckDB command - no explanations, comments, or extra text.</instruction>
    <instruction>Create the command that satisfies the user query against the duckdb-database-path (e.g., mydb.db).</instruction>
    <instruction>Ensure the command follows DuckDB best practices for efficiency and readability.</instruction>
    <instruction>When the user requests to output results to a file, generate a command that writes to the specified file, or create a filename based on a shortened version of the user request and the input database name.</instruction>
    <instruction>If output is requested in CSV format, use the DuckDB COPY command with WITH (FORMAT CSV, HEADER, DELIMITER ',').</instruction>
    <instruction>If output is requested in JSON format, use the DuckDB COPY command with WITH (FORMAT JSON) to export results as JSON.</instruction>
    <instruction>When filtering or processing data, embed the query inside a COPY command if exporting, or run the query directly if no export is needed.</instruction>
    <instruction>Output your response by itself, do not use backticks or markdown formatting. We're going to run your response as a shell command immediately.</instruction>
    <instruction>If your results involve a table or query result set, default to exporting as a valid CSV or JSON file as requested.</instruction>
    <instruction>If the user request is to export to a file, ensure the file is created in the same directory as the duckdb-database-path unless specified otherwise.</instruction>
</instructions>

<examples>
    <example>
        <duckdb-database-path>
            mydb.db
        </duckdb-database-path>
        <user-request>
            Select the "name" and "age" columns from table employees where age > 30
        </user-request>
        <duckdb-command>
            duckdb mydb.db -c "SELECT name, age FROM employees WHERE age > 30;"
        </duckdb-command>
    </example>
    <example>
        <duckdb-database-path>
            data/order_data.db
        </duckdb-database-path>
        <user-request>
            Filter records in table orders where total > 100 and export to orders_high.csv
        </user-request>
        <duckdb-command>
            duckdb data/order_data.db -c "COPY (SELECT * FROM orders WHERE total > 100) TO 'orders_high.csv' WITH (FORMAT CSV, HEADER, DELIMITER ',');"
        </duckdb-command>
    </example>
    <example>
        <duckdb-database-path>
            analytics.db
        </duckdb-database-path>
        <user-request>
            Convert table customers to JSON and save as customers.json
        </user-request>
        <duckdb-command>
            duckdb analytics.db -c "COPY (SELECT * FROM customers) TO 'customers.json' WITH (FORMAT JSON);"
        </duckdb-command>
    </example>
    <example>
        <duckdb-database-path>
            mydb.db
        </duckdb-database-path>
        <user-request>
            Export the result of a join between employees and departments from mydb.db to employees_departments.csv
        </user-request>
        <duckdb-command>
            duckdb mydb.db -c "COPY (SELECT e.name, d.department FROM employees e JOIN departments d ON e.dept_id = d.id) TO 'employees_departments.csv' WITH (FORMAT CSV, HEADER, DELIMITER ',');"
        </duckdb-command>
    </example>
    <example>
        <duckdb-database-path>
            mydb.db
        </duckdb-database-path>
        <user-request>
            Retrieve all records from table sales in mydb.db where region is 'North'
        </user-request>
        <duckdb-command>
            duckdb mydb.db -c "SELECT * FROM sales WHERE region = 'North';"
        </duckdb-command>
    </example>
</examples>

<duckdb-database-path>
    {{database_path}}
</duckdb-database-path>

<user-request>
    {{user_request}}
</user-request>

Your DuckDB command:"""


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Generate DuckDB CLI command using Gemini API"
    )
    parser.add_argument(
        "prompt",
        help="The DuckDB command request to send to Gemini",
    )
    parser.add_argument(
        "--db",
        required=True,
        help="Path to DuckDB database file",
    )
    parser.add_argument(
        "--no-exe",
        action="store_true",
        help="Generate the DuckDB command without executing it",
    )
    args = parser.parse_args()

    # Configure the API key
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY environment variable is not set")
        print("Please get your API key from https://aistudio.google.com/app/apikey")
        print("Then set it with: export GEMINI_API_KEY='your-api-key-here'")
        sys.exit(1)

    # Initialize client
    client = genai.Client(
        api_key=GEMINI_API_KEY, http_options={"api_version": "v1alpha"}
    )

    try:
        # Replace template variables in the prompt
        prompt = DUCKDB_PROMPT.replace("{{database_path}}", args.db)
        prompt = prompt.replace("{{user_request}}", args.prompt)

        # Generate DuckDB command
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", contents=prompt
        )
        duckdb_command = response.text.strip()
        print("\n🤖 Generated DuckDB command:", duckdb_command)

        # Execute the command unless --no-exe flag is present
        if not args.no_exe:
            print("\n🔍 Executing command...")
            # Execute the command using subprocess
            result = subprocess.run(
                duckdb_command, shell=True, text=True, capture_output=True
            )
            if result.returncode != 0:
                print(
                    f"\n❌ Error executing command (return code: {result.returncode}):",
                    result.stderr,
                )
                sys.exit(1)

            if result.stderr:
                print("❌ Error executing command:", result.stderr)

            if result.stdout:
                print("✅ Command executed successfully:")
                print(result.stdout)

    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
````

## File: sfa_duckdb_gemini_v2.py
````python
#!/usr/bin/env python3

# /// script
# dependencies = [
#   "google-genai>=1.1.0",
#   "rich>=13.7.0",
# ]
# ///

"""
/// Example Usage

# Run DuckDB agent with default compute loops (3)
uv run sfa_duckdb_gemini_v2.py -d ./data/analytics.db -p "Show me all users with score above 80"

# Run with custom compute loops
uv run sfa_duckdb_gemini_v2.py -d ./data/analytics.db -p "Show me all users with score above 80" -c 5

///
"""

import os
import sys
import json
import argparse
import subprocess
from typing import List
from rich.console import Console
from rich.panel import Panel
from google import genai
from google.genai import types

# Initialize rich console
console = Console()


def list_tables(reasoning: str) -> List[str]:
    """Returns a list of tables in the database.

    The agent uses this to discover available tables and make informed decisions.

    Args:
        reasoning: Explanation of why we're listing tables relative to user request

    Returns:
        List of table names as strings
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c ".tables"',
            # f"duckdb {DB_PATH} -c \"SELECT name FROM sqlite_master WHERE type='table';\"",
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(f"[blue]List Tables Tool[/blue] - Reasoning: {reasoning}")
        return result.stdout.strip().split("\n")
    except Exception as e:
        console.log(f"[red]Error listing tables: {str(e)}[/red]")
        return []


def describe_table(reasoning: str, table_name: str) -> str:
    """Returns schema information about the specified table.

    The agent uses this to understand table structure and available columns.

    Args:
        reasoning: Explanation of why we're describing this table
        table_name: Name of table to describe

    Returns:
        String containing table schema information
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "DESCRIBE {table_name};"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(
            f"[blue]Describe Table Tool[/blue] - Table: {table_name} - Reasoning: {reasoning}"
        )
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error describing table: {str(e)}[/red]")
        return ""


def sample_table(reasoning: str, table_name: str, row_sample_size: int) -> str:
    """Returns a sample of rows from the specified table.

    The agent uses this to understand actual data content and patterns.

    Args:
        reasoning: Explanation of why we're sampling this table
        table_name: Name of table to sample from
        row_sample_size: Number of rows to sample aim for 3-5 rows

    Returns:
        String containing sample rows in readable format
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "SELECT * FROM {table_name} LIMIT {row_sample_size};"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(
            f"[blue]Sample Table Tool[/blue] - Table: {table_name} - Rows: {row_sample_size} - Reasoning: {reasoning}"
        )
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error sampling table: {str(e)}[/red]")
        return ""


def run_test_sql_query(reasoning: str, sql_query: str) -> str:
    """Executes a test SQL query and returns results.

    The agent uses this to validate queries before finalizing them.
    Results are only shown to the agent, not the user.

    Args:
        reasoning: Explanation of why we're running this test query
        sql_query: The SQL query to test

    Returns:
        Query results as a string
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "{sql_query}"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(f"[blue]Test Query Tool[/blue] - Reasoning: {reasoning}")
        console.log(f"[dim]Query: {sql_query}[/dim]")
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error running test query: {str(e)}[/red]")
        return str(e)


def run_final_sql_query(reasoning: str, sql_query: str) -> str:
    """Executes the final SQL query and returns results to user.

    This is the last tool call the agent should make after validating the query.

    Args:
        reasoning: Final explanation of how this query satisfies user request
        sql_query: The validated SQL query to run

    Returns:
        Query results as a string
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "{sql_query}"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(
            Panel(
                f"[green]Final Query Tool[/green]\nReasoning: {reasoning}\nQuery: {sql_query}"
            )
        )
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error running final query: {str(e)}[/red]")
        return str(e)


AGENT_PROMPT = """<purpose>
    You are a world-class expert at crafting precise DuckDB SQL queries.
    Your goal is to generate accurate queries that exactly match the user's data needs.
</purpose>

<instructions>
    <instruction>Use the provided tools to explore the database and construct the perfect query.</instruction>
    <instruction>Start by listing tables to understand what's available.</instruction>
    <instruction>Describe tables to understand their schema and columns.</instruction>
    <instruction>Sample tables to see actual data patterns.</instruction>
    <instruction>Test queries before finalizing them.</instruction>
    <instruction>Only call run_final_sql_query when you're confident the query is perfect.</instruction>
    <instruction>Be thorough but efficient with tool usage.</instruction>
    <instruction>If you find your run_test_sql_query tool call returns an error or won't satisfy the user request, try to fix the query or try a different query.</instruction>
    <instruction>Think step by step about what information you need.</instruction>
    <instruction>Be sure to specify every parameter for each tool call.</instruction>
    <instruction>Every tool call should have a reasoning parameter which gives you a place to explain why you are calling the tool.</instruction>
</instructions>

<tools>
    <tool>
        <name>list_tables</name>
        <description>Returns list of available tables in database</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we need to list tables relative to user request</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>describe_table</name>
        <description>Returns schema info for specified table</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we need to describe this table</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>table_name</name>
                <type>string</type>
                <description>Name of table to describe</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>sample_table</name>
        <description>Returns sample rows from specified table, always specify row_sample_size</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we need to sample this table</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>table_name</name>
                <type>string</type>
                <description>Name of table to sample</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>row_sample_size</name>
                <type>integer</type>
                <description>Number of rows to sample aim for 3-5 rows</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>run_test_sql_query</name>
        <description>Tests a SQL query and returns results (only visible to agent)</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we're testing this specific query</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>sql_query</name>
                <type>string</type>
                <description>The SQL query to test</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>run_final_sql_query</name>
        <description>Runs the final validated SQL query and shows results to user</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Final explanation of how query satisfies user request</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>sql_query</name>
                <type>string</type>
                <description>The validated SQL query to run</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
</tools>

<user-request>
    {{user_request}}
</user-request>
"""


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="DuckDB Agent using Gemini API")
    parser.add_argument(
        "-d", "--db", required=True, help="Path to DuckDB database file"
    )
    parser.add_argument("-p", "--prompt", required=True, help="The user's request")
    parser.add_argument(
        "-c",
        "--compute",
        type=int,
        default=10,
        help="Maximum number of agent loops (default: 3)",
    )
    args = parser.parse_args()

    # Configure the API key
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not GEMINI_API_KEY:
        console.print(
            "[red]Error: GEMINI_API_KEY environment variable is not set[/red]"
        )
        console.print(
            "Please get your API key from https://aistudio.google.com/app/apikey"
        )
        console.print("Then set it with: export GEMINI_API_KEY='your-api-key-here'")
        sys.exit(1)

    # Set global DB_PATH for tool functions
    global DB_PATH
    DB_PATH = args.db

    # Initialize Gemini client
    client = genai.Client(api_key=GEMINI_API_KEY)

    completed_prompt = AGENT_PROMPT.replace("{{user_request}}", args.prompt)

    # Initialize message history with proper Content type
    messages = [
        types.Content(role="user", parts=[types.Part.from_text(text=completed_prompt)])
    ]

    compute_iterations = 0

    # Main agent loop
    while True:
        console.rule(
            f"[yellow]Agent Loop {compute_iterations+1}/{args.compute}[/yellow]"
        )
        compute_iterations += 1

        if compute_iterations >= args.compute:
            console.print(
                "[yellow]Warning: Reached maximum compute loops without final query[/yellow]"
            )
            raise Exception(
                f"Maximum compute loops reached: {compute_iterations}/{args.compute}"
            )

        try:
            # Generate content with tool support
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                # model="gemini-1.5-flash",
                contents=[
                    *messages,
                ],
                config=types.GenerateContentConfig(
                    tools=[
                        list_tables,
                        describe_table,
                        sample_table,
                        run_test_sql_query,
                        run_final_sql_query,
                    ],
                    automatic_function_calling=types.AutomaticFunctionCallingConfig(
                        # maximum_remote_calls=2
                        # disable=True
                    ),
                    tool_config=types.ToolConfig(
                        function_calling_config=types.FunctionCallingConfig(mode="ANY")
                    ),
                ),
            )

            # Process tool calls
            if response.function_calls:
                for func_call in response.function_calls:
                    # Extract function name and args
                    func_name = func_call.name
                    func_args = func_call.args

                    console.print(
                        f"[blue]Function Call:[/blue] {func_name}({func_args})"
                    )

                    try:
                        # Call appropriate function
                        if func_name == "list_tables":
                            result = list_tables(**func_args)
                        elif func_name == "describe_table":
                            result = describe_table(**func_args)
                        elif func_name == "sample_table":
                            result = sample_table(**func_args)
                        elif func_name == "run_test_sql_query":
                            result = run_test_sql_query(**func_args)
                        elif func_name == "run_final_sql_query":
                            result = run_final_sql_query(**func_args)
                            console.print("\n[green]Final Results:[/green]")
                            console.print(result)
                            return  # Exit after final query

                        console.print(
                            f"[blue]Function Call Result:[/blue] {func_name}(...) ->\n{result}"
                        )

                        # Add function response as proper Content type
                        function_response = {"result": str(result)}
                        function_response_part = types.Part.from_function_response(
                            name=func_name,
                            response=function_response,
                        )

                        # Add model's function call as Content
                        messages.append(response.candidates[0].content)

                        messages.append(
                            types.Content(role="tool", parts=[function_response_part])
                        )

                    except Exception as e:
                        # Add error response as proper Content type
                        error_msg = f"Error executing {func_name}: {str(e)}"
                        function_response = {"error": error_msg}
                        function_response_part = types.Part.from_function_response(
                            name=func_name,
                            response=function_response,
                        )
                        messages.append(response.candidates[0].content)
                        messages.append(
                            types.Content(role="tool", parts=[function_response_part])
                        )

                        console.print(f"[red]{error_msg}[/red]")
                        continue

            else:
                # Add model response as proper Content type
                messages.append(response.candidates[0].content)

        except Exception as e:
            console.print(f"[red]Error in agent loop: {str(e)}[/red]")
            raise e


if __name__ == "__main__":
    main()
````

## File: sfa_duckdb_openai_v2.py
````python
# /// script
# dependencies = [
#   "openai>=1.63.0",
#   "rich>=13.7.0",
#   "pydantic>=2.0.0",
# ]
# ///


import os
import sys
import json
import argparse
import subprocess
from typing import List
from rich.console import Console
from rich.panel import Panel
import openai
from pydantic import BaseModel, Field, ValidationError
from openai import pydantic_function_tool

# Initialize rich console
console = Console()


# Create our list of function tools from our pydantic models
class ListTablesArgs(BaseModel):
    reasoning: str = Field(
        ..., description="Explanation for listing tables relative to the user request"
    )


class DescribeTableArgs(BaseModel):
    reasoning: str = Field(..., description="Reason why the table schema is needed")
    table_name: str = Field(..., description="Name of the table to describe")


class SampleTableArgs(BaseModel):
    reasoning: str = Field(..., description="Explanation for sampling the table")
    table_name: str = Field(..., description="Name of the table to sample")
    row_sample_size: int = Field(
        ..., description="Number of rows to sample (aim for 3-5 rows)"
    )


class RunTestSQLQuery(BaseModel):
    reasoning: str = Field(..., description="Reason for testing this query")
    sql_query: str = Field(..., description="The SQL query to test")


class RunFinalSQLQuery(BaseModel):
    reasoning: str = Field(
        ...,
        description="Final explanation of how this query satisfies the user request",
    )
    sql_query: str = Field(..., description="The validated SQL query to run")


# Create tools list
tools = [
    pydantic_function_tool(ListTablesArgs),
    pydantic_function_tool(DescribeTableArgs),
    pydantic_function_tool(SampleTableArgs),
    pydantic_function_tool(RunTestSQLQuery),
    pydantic_function_tool(RunFinalSQLQuery),
]

AGENT_PROMPT = """<purpose>
    You are a world-class expert at crafting precise DuckDB SQL queries.
    Your goal is to generate accurate queries that exactly match the user's data needs.
</purpose>

<instructions>
    <instruction>Use the provided tools to explore the database and construct the perfect query.</instruction>
    <instruction>Start by listing tables to understand what's available.</instruction>
    <instruction>Describe tables to understand their schema and columns.</instruction>
    <instruction>Sample tables to see actual data patterns.</instruction>
    <instruction>Test queries before finalizing them.</instruction>
    <instruction>Only call run_final_sql_query when you're confident the query is perfect.</instruction>
    <instruction>Be thorough but efficient with tool usage.</instruction>
    <instruction>If you find your run_test_sql_query tool call returns an error or won't satisfy the user request, try to fix the query or try a different query.</instruction>
    <instruction>Think step by step about what information you need.</instruction>
    <instruction>Be sure to specify every parameter for each tool call.</instruction>
    <instruction>Every tool call should have a reasoning parameter which gives you a place to explain why you are calling the tool.</instruction>
</instructions>

<tools>
    <tool>
        <name>list_tables</name>
        <description>Returns list of available tables in database</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we need to list tables relative to user request</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>describe_table</name>
        <description>Returns schema info for specified table</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we need to describe this table</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>table_name</name>
                <type>string</type>
                <description>Name of table to describe</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>sample_table</name>
        <description>Returns sample rows from specified table, always specify row_sample_size</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we need to sample this table</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>table_name</name>
                <type>string</type>
                <description>Name of table to sample</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>row_sample_size</name>
                <type>integer</type>
                <description>Number of rows to sample aim for 3-5 rows</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>run_test_sql_query</name>
        <description>Tests a SQL query and returns results (only visible to agent)</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we're testing this specific query</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>sql_query</name>
                <type>string</type>
                <description>The SQL query to test</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>run_final_sql_query</name>
        <description>Runs the final validated SQL query and shows results to user</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Final explanation of how query satisfies user request</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>sql_query</name>
                <type>string</type>
                <description>The validated SQL query to run</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
</tools>

<user-request>
    {{user_request}}
</user-request>
"""


def list_tables(reasoning: str) -> List[str]:
    """Returns a list of tables in the database.

    The agent uses this to discover available tables and make informed decisions.

    Args:
        reasoning: Explanation of why we're listing tables relative to user request

    Returns:
        List of table names as strings
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c ".tables"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(f"[blue]List Tables Tool[/blue] - Reasoning: {reasoning}")
        return result.stdout.strip().split("\n")
    except Exception as e:
        console.log(f"[red]Error listing tables: {str(e)}[/red]")
        return []


def describe_table(reasoning: str, table_name: str) -> str:
    """Returns schema information about the specified table.

    The agent uses this to understand table structure and available columns.

    Args:
        reasoning: Explanation of why we're describing this table
        table_name: Name of table to describe

    Returns:
        String containing table schema information
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "DESCRIBE {table_name};"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(
            f"[blue]Describe Table Tool[/blue] - Table: {table_name} - Reasoning: {reasoning}"
        )
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error describing table: {str(e)}[/red]")
        return ""


def sample_table(reasoning: str, table_name: str, row_sample_size: int) -> str:
    """Returns a sample of rows from the specified table.

    The agent uses this to understand actual data content and patterns.

    Args:
        reasoning: Explanation of why we're sampling this table
        table_name: Name of table to sample from
        row_sample_size: Number of rows to sample aim for 3-5 rows

    Returns:
        String containing sample rows in readable format
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "SELECT * FROM {table_name} LIMIT {row_sample_size};"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(
            f"[blue]Sample Table Tool[/blue] - Table: {table_name} - Rows: {row_sample_size} - Reasoning: {reasoning}"
        )
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error sampling table: {str(e)}[/red]")
        return ""


def run_test_sql_query(reasoning: str, sql_query: str) -> str:
    """Executes a test SQL query and returns results.

    The agent uses this to validate queries before finalizing them.
    Results are only shown to the agent, not the user.

    Args:
        reasoning: Explanation of why we're running this test query
        sql_query: The SQL query to test

    Returns:
        Query results as a string
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "{sql_query}"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(f"[blue]Test Query Tool[/blue] - Reasoning: {reasoning}")
        console.log(f"[dim]Query: {sql_query}[/dim]")
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error running test query: {str(e)}[/red]")
        return str(e)


def run_final_sql_query(reasoning: str, sql_query: str) -> str:
    """Executes the final SQL query and returns results to user.

    This is the last tool call the agent should make after validating the query.

    Args:
        reasoning: Final explanation of how this query satisfies user request
        sql_query: The validated SQL query to run

    Returns:
        Query results as a string
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "{sql_query}"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(
            Panel(
                f"[green]Final Query Tool[/green]\nReasoning: {reasoning}\nQuery: {sql_query}"
            )
        )
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error running final query: {str(e)}[/red]")
        return str(e)


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="DuckDB Agent using OpenAI API")
    parser.add_argument(
        "-d", "--db", required=True, help="Path to DuckDB database file"
    )
    parser.add_argument("-p", "--prompt", required=True, help="The user's request")
    parser.add_argument(
        "-c",
        "--compute",
        type=int,
        default=10,
        help="Maximum number of agent loops (default: 3)",
    )
    args = parser.parse_args()

    # Configure the API key
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        console.print(
            "[red]Error: OPENAI_API_KEY environment variable is not set[/red]"
        )
        console.print(
            "Please get your API key from https://platform.openai.com/api-keys"
        )
        console.print("Then set it with: export OPENAI_API_KEY='your-api-key-here'")
        sys.exit(1)

    openai.api_key = OPENAI_API_KEY

    # Set global DB_PATH for tool functions
    global DB_PATH
    DB_PATH = args.db

    # Create a single combined prompt based on the full template
    completed_prompt = AGENT_PROMPT.replace("{{user_request}}", args.prompt)
    messages = [{"role": "user", "content": completed_prompt}]

    compute_iterations = 0

    # Main agent loop
    while True:
        console.rule(
            f"[yellow]Agent Loop {compute_iterations+1}/{args.compute}[/yellow]"
        )
        compute_iterations += 1

        if compute_iterations >= args.compute:
            console.print(
                "[yellow]Warning: Reached maximum compute loops without final query[/yellow]"
            )
            raise Exception(
                f"Maximum compute loops reached: {compute_iterations}/{args.compute}"
            )

        try:
            # Generate content with tool support
            response = openai.chat.completions.create(
                model="o3-mini",
                # model="gpt-4o-mini",
                messages=messages,
                tools=tools,
                tool_choice="required",
            )

            if response.choices:
                assert len(response.choices) == 1
                message = response.choices[0].message

                if message.function_call:
                    func_call = message.function_call
                elif message.tool_calls and len(message.tool_calls) > 0:
                    # If a tool_calls list is present, use the first call and extract its function details.
                    tool_call = message.tool_calls[0]
                    func_call = tool_call.function
                else:
                    func_call = None

                if func_call:
                    func_name = func_call.name
                    func_args_str = func_call.arguments

                    messages.append(
                        {
                            "role": "assistant",
                            "tool_calls": [
                                {
                                    "id": tool_call.id,
                                    "type": "function",
                                    "function": func_call,
                                }
                            ],
                        }
                    )

                    console.print(
                        f"[blue]Function Call:[/blue] {func_name}({func_args_str})"
                    )
                    try:
                        # Validate and parse arguments using the corresponding pydantic model
                        if func_name == "ListTablesArgs":
                            args_parsed = ListTablesArgs.model_validate_json(
                                func_args_str
                            )
                            result = list_tables(reasoning=args_parsed.reasoning)
                        elif func_name == "DescribeTableArgs":
                            args_parsed = DescribeTableArgs.model_validate_json(
                                func_args_str
                            )
                            result = describe_table(
                                reasoning=args_parsed.reasoning,
                                table_name=args_parsed.table_name,
                            )
                        elif func_name == "SampleTableArgs":
                            args_parsed = SampleTableArgs.model_validate_json(
                                func_args_str
                            )
                            result = sample_table(
                                reasoning=args_parsed.reasoning,
                                table_name=args_parsed.table_name,
                                row_sample_size=args_parsed.row_sample_size,
                            )
                        elif func_name == "RunTestSQLQuery":
                            args_parsed = RunTestSQLQuery.model_validate_json(
                                func_args_str
                            )
                            result = run_test_sql_query(
                                reasoning=args_parsed.reasoning,
                                sql_query=args_parsed.sql_query,
                            )
                        elif func_name == "RunFinalSQLQuery":
                            args_parsed = RunFinalSQLQuery.model_validate_json(
                                func_args_str
                            )
                            result = run_final_sql_query(
                                reasoning=args_parsed.reasoning,
                                sql_query=args_parsed.sql_query,
                            )
                            console.print("\n[green]Final Results:[/green]")
                            console.print(result)
                            return
                        else:
                            raise Exception(f"Unknown tool call: {func_name}")

                        console.print(
                            f"[blue]Function Call Result:[/blue] {func_name}(...) ->\n{result}"
                        )

                        # Append the function call result into our messages as a tool response
                        messages.append(
                            {
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "content": json.dumps({"result": str(result)}),
                            }
                        )

                    except Exception as e:
                        error_msg = f"Argument validation failed for {func_name}: {e}"
                        console.print(f"[red]{error_msg}[/red]")
                        messages.append(
                            {
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "content": json.dumps({"error": error_msg}),
                            }
                        )
                        continue
                else:
                    raise Exception(
                        "No function call in this response - should never happen"
                    )

        except Exception as e:
            console.print(f"[red]Error in agent loop: {str(e)}[/red]")
            raise e


if __name__ == "__main__":
    main()
````

## File: sfa_jq_gemini_v1.py
````python
# /// script
# dependencies = [
#   "google-genai>=1.1.0",
# ]
# ///

"""
/// Example Usage

# generates jq command and executes it
uv run sfa_jq_gemini_v1.py --exe "Filter scores above 80 from data/analytics.json and save to high_scores.json"

# generates jq command only
uv run sfa_jq_gemini_v1.py "Filter scores above 80 from data/analytics.json and save to high_scores.json"

///
"""

import os
import sys
import argparse
import subprocess
from google import genai

JQ_PROMPT = """<purpose>
    You are a world-class expert at crafting precise jq commands for JSON processing.
    Your goal is to generate accurate, minimal jq commands that exactly match the user's data manipulation needs.
</purpose>

<instructions>
    <instruction>Return ONLY the jq command - no explanations, comments, or extra text.</instruction>
    <instruction>Always reference the input file specified in the user request (e.g., using -f flag if needed).</instruction>
    <instruction>Ensure the command follows jq best practices for efficiency and readability.</instruction>
    <instruction>Use the examples to understand different types of jq command patterns.</instruction>
    <instruction>When user asks to pipe or output to a file, use the correct syntax for the command and create a file name (if not specified) based on a shorted version of the user-request and the input file name.</instruction>
    <instruction>If the user request asks to pipe or output to a file, and no explicit directory is specified, use the directory of the input file.</instruction>
    <instruction>Output your response by itself, do not use backticks or markdown formatting. We're going to run your response as a shell command immediately.</instruction>
    <instruction>If your results you're working with a list of objects, default to outputting a valid json array.</instruction>
</instructions>

<examples>
    <example>
        <user-request>
            Select the "name" and "age" fields from data.json where age > 30
        </user-request>
        <jq-command>
            jq '[.[] | select(.age > 30) | {name, age}]' data.json
        </jq-command>
    </example>
    <example>
        <user-request>
            Count the number of entries in users.json with status "active"
        </user-request>
        <jq-command>
            jq '[.[] | select(.status == "active")] | length' users.json
        </jq-command>
    </example>
    <example>
        <user-request>
            Extract nested phone numbers from contacts.json using compact output
        </user-request>
        <jq-command>
            jq -c '.contact.info.phones' contacts.json
        </jq-command>
    </example>
    <example>
        <user-request>
            Convert log.json entries to CSV format with timestamp, level, message
        </user-request>
        <jq-command>
            jq -r '.[] | [.timestamp, .level, .message] | @csv' log.json
        </jq-command>
    </example>
    <example>
        <user-request>
            Sort records in people.json by age in descending order
        </user-request>
        <jq-command>
            jq 'sort_by(.age) | reverse' people.json
        </jq-command>
    </example>
    <example>
        <user-request>
            Save active users from data/users.json to a new file
        </user-request>
        <jq-command>
            jq '[.[] | select(.status == "active")]' data/users.json > data/active_users.json
        </jq-command>
    </example>
    <example>
        <user-request>
            Convert data.json to CSV for keys name, age, city and save in same directory
        </user-request>
        <jq-command>
            jq -r '.[] | [.name, .age, .city] | @csv' data/testing/data.json > data/testing/data_csv.csv
        </jq-command>
    </example>
    <example>
        <user-request>
            Filter scores above 80 from data/mock.json and save to ./high_scores.json
        </user-request>
        <jq-command>
            jq '[.[] | select(.score > 80)]' data/mock.json > ./high_scores.json
        </jq-command>
    </example>
</examples>


<user-request>
    {{user_request}}
</user-request>

Your jq command:"""


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate text using Gemini API")
    parser.add_argument(
        "prompt",
        help="The JQ command request to send to Gemini",
    )
    parser.add_argument(
        "--exe",
        action="store_true",
        help="Execute the generated JQ command",
    )
    args = parser.parse_args()

    # Configure the API key
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY environment variable is not set")
        print("Please get your API key from https://aistudio.google.com/app/apikey")
        print("Then set it with: export GEMINI_API_KEY='your-api-key-here'")
        sys.exit(1)

    # Initialize client
    client = genai.Client(
        api_key=GEMINI_API_KEY, http_options={"api_version": "v1alpha"}
    )

    try:
        # Replace {{user_request}} in the prompt template
        prompt = JQ_PROMPT.replace("{{user_request}}", args.prompt)

        # Generate JQ command
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", contents=prompt
        )
        jq_command = response.text.strip()
        print("\n🤖 Generated JQ command:", jq_command)

        # Execute the command if --exe flag is present
        if args.exe:
            print("\n🔍 Executing command...")
            # Execute the command using subprocess
            result = subprocess.run(
                jq_command, shell=True, text=True, capture_output=True
            )
            if result.returncode != 0:
                print("\n❌ Error executing command:", result.stderr)
                sys.exit(1)
            print(result.stdout + result.stderr)

            if not result.stderr:
                print("\n✅ Command executed successfully")

    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
````

## File: sfa_meta_prompt_openai_v1.py
````python
#!/usr/bin/env python3

# /// script
# dependencies = [
#   "openai>=1.62.0",
# ]
# ///

"""
/// Example Usage

# Generate a meta prompt using command-line arguments.
# Optional arguments are marked with a ?.

uv run sfa_meta_prompt_openai_v1.py \
    --purpose "generate mermaid diagrams" \
    --instructions "generate a mermaid valid chart, use diagram type specified or default flow, use examples to understand the structure of the output" \
    --sections "examples, user-prompt" \
    --examples "create examples of 3 basic mermaid charts with <user-chart-request> and <chart-response> blocks" \
    --variables "user-prompt"

# Without optional arguments, the script will enter interactive mode.
uv run sfa_meta_prompt_openai_v1.py \
    --purpose "generate mermaid diagrams" \
    --instructions "generate a mermaid valid chart, use diagram type specified or default flow, use examples to understand the structure of the output"

# Alternatively, just run the script without any flags to enter interactive mode.
uv run sfa_meta_prompt_openai_v1.py

///
"""

import os
import sys
import argparse
import openai

META_PROMPT = """<purpose>
    You are an expert prompt engineer, capable of creating detailed and effective prompts for language models.
    
    Your task is to generate a comprehensive prompt based on the user's input structure.
    
    Follow the instructions closely to generate a new prompt template.
</purpose>

<instructions>
    <instruction>Analyze the user-input carefully, paying attention to the purpose, required sections, and variables.</instruction>
    <instruction>Create a detailed prompt that includes all specified sections and incorporates the provided variables.</instruction>
    <instruction>Use clear and concise language in the generated prompt.</instruction>
    <instruction>Ensure that the generated prompt maintains a logical flow and structure.</instruction>
    <instruction>Include placeholders for variables values in the format [[variable-name]].</instruction>
    <instruction>If a section is plural, create a nested section with three items in the singular form.</instruction>
    <instruction>The key xml blocks are purpose, instructions, sections, examples, user-prompt.
    <instruction>Purpose defines the high level goal of the prompt.</instruction>
    <instruction>Instructions are the detailed instructions for the prompt.</instruction>
    <instruction>Sections are arbitrary blocks to include in the prompt.</instruction>
    <instruction>Examples are showcases of what the output should be for the prompt. Use this to steer the structure of the output based on the user-input. This will typically be a list of examples with the expected output.</instruction>
    <instruction>Variables are placeholders for values to be substituted in the prompt.</instruction>
    <instruction>Not every section is required, but purpose and instructions are typically essential. Create the xml blocks based on the user-input.</instruction>
    <instruction>Use the examples to understand the structure of the output.</instruction>
    <instruction>Your output should be in XML format, mirroring the structure of the examples output.</instruction>
    <instruction>Exclude CDATA sections in your output.</instruction>
    <instruction>Response exclusively with the desired output, no other text.</instruction>
    <instruction>If the user-input is structured like the input-format, use it as is. If it's not, infer the purpose, sections, and variables from the user-input.</instruction>
    <instruction>The goal is to fill in the blanks and best infer the purpose, instructions, sections, and variables from the user-input. If instructions are given, use them to guide the other xml blocks.</instruction>
    <instruction>Emphasize exact XML structure and nesting. Clearly define which blocks must contain which elements to ensure a well-formed output.</instruction>
    <instruction>Ensure that each section builds logically upon the previous ones, creating a coherent narrative from purpose to instructions, sections, and examples.</instruction>
    <instruction>Use direct, simple language and avoid unnecessary complexity to make the final prompt easy to understand.</instruction>
    <instruction>After creating the full prompt, perform a final validation to confirm that all placeholders, instructions, and examples are included, properly formatted, and consistent.</instruction>
    <instruction>If examples are not requested, don't create them.</instruction>
    <instruction>If sections are not requested, don't create them.</instruction>
    <instruction>If variables are not requested, just create a section for the user-input.</instruction>
</instructions>

<input-format>
    Purpose: [main purpose of the prompt], Instructions: [list of details of how to generate the output comma sep], Sections: [list of additional sections to include, e.g., examples, user-prompt], Examples: [list of examples of the output for the prompt], Variables: [list of variables to be used in the prompt]
</input-format>

<examples>
    <example>
        <input>
            Purpose: generate mermaid diagrams. Instructions: generate a mermaid valid chart, use diagram type specified or default flow, use examples to understand the structure of the output. Sections: examples, user-prompt. Variables: user-prompt
        </input>
        <output>
<![CDATA[
You are a world-class expert at creating mermaid charts.

You follow the instructions perfectly to generate mermaid charts.

<instructions>
    <instruction>Generate valid a mermaid chart based on the user-prompt.</instruction>
    <instruction>Use the diagram type specified in the user-prompt if non-specified use a flowchart.</instruction>
    <instruction>Use the examples to understand the structure of the output.</instruction>
</instructions>

<examples>
    <example>
        <user-chart-request>
            Create a flowchart that shows A flowing to E. At C, branch out to H and I.
        </user-chart-request>
        <chart-response>
            graph LR;
                A
                B
                C
                D
                E
                H
                I
                A --> B
                A --> C
                A --> D
                C --> H
                C --> I
                D --> E
        </chart-response>
    </example>
    <example>
        <user-chart-request>
            Build a pie chart that shows the distribution of Apples: 40, Bananas: 35, Oranges: 25.
        </user-chart-request>
        <chart-response>
            pie title Distribution of Fruits
                "Apples" : 40
                "Bananas" : 35
                "Oranges" : 25
        </chart-response>
    </example>
    <example>
        <user-chart-request>
            State diagram for a traffic light. Still, Moving, Crash.
        </user-chart-request>
        <chart-response>
            stateDiagram-v2
                [*] --> Still
                Still --> [*]
                Still --> Moving
                Moving --> Still
                Moving --> Crash
                Crash --> [*]
        </chart-response>
    </example>
    <example>
        <user-chart-request>
            Create a timeline of major social media platforms from 2002 to 2006.
        </user-chart-request>
        <chart-response>
            timeline
                title History of Social Media Platforms
                2002 : LinkedIn
                2004 : Facebook
                        : Google
                2005 : Youtube
                2006 : Twitter
        </chart-response>
    </example>
    </examples>

<user-prompt>
    [[user-prompt]]
</user-prompt>

Your mermaid chart:
</output>
    </example>
    <example>
        <input>
            Purpose: review git diff to improve code quality. Instructions: Review git diff, give suggestions for improvements to the code organized in a list sorted by priority. Sections: git-diff. Variables: git-diff
        </input>
        <output>
<![CDATA[
<purpose>
    You are an expert at reviewing git diffs to improve code quality.
    You follow the instructions perfectly to review git diffs.
</purpose>

<instructions>
    <instruction>Review the git diff and provide a detailed analysis of the changes made.</instruction>
    <instruction>Give suggestions for improvements to the code organized in a list sorted by priority.</instruction>
    <instruction>Think through the changes in a wholistic manner and offer suggestions for improvements.</instruction>
</instructions>

<git-diff>
    [[git-diff]]
</git-diff>

Your review of the git diff:
]]>
        </output>
    </example>
    <example>
        <input>
            Purpose: convert user mathematical expressions into LaTeX. Instructions: Take the user-input, which is a mathematical expression in plain text, and output a properly formatted LaTeX equation. Sections: user-input. Variables: user-input
        </input>
        <output>
<![CDATA[
<purpose>
    You are a highly skilled mathematician who can transform plain text math expressions into LaTeX formatted equations.
</purpose>

<instructions>
    <instruction>Read the user-input plain text mathematical expression carefully.</instruction>
    <instruction>Convert it into a well-formatted LaTeX equation environment.</instruction>
    <instruction>Ensure the final output is wrapped in a LaTeX display math environment.</instruction>
</instructions>

<user-input>
    [[user-input]]
</user-input>

Your LaTeX equation:
]]>
        </output>
    </example>
    <example>
        <input>
            Purpose: Summarize and extract key action points from a user-provided legal contract
            Instructions: Thoroughly analyze the legal text, identify and summarize key clauses, highlight main obligations and deadlines, and provide recommended action points in list form for the user. Keep the final output simple and easy to understand, no legalese. Follow the examples.
            Sections: contract-text, summary, action-points, user-prompt
            Examples: show how to summarize major clauses from a rental agreement, a service contract, and an employment contract
            Variables: contract-text, user-prompt
        </input>
        <output>
<purpose>
    You are an expert legal advisor who specializes in summarizing complex contracts into clear, actionable insights.
    Your goal is to help the user quickly understand their contract, identify key clauses, and see recommended actions.
</purpose>

<instructions>
    <instruction>Read the user-provided contract text carefully.</instruction>
    <instruction>Identify the main clauses, obligations, timelines, and responsibilities mentioned.</instruction>
    <instruction>Summarize these points in simple, accessible language, avoiding jargon and unnecessary complexity.</instruction>
    <instruction>Highlight any deadlines or financial obligations that appear in the text.</instruction>
    <instruction>Create a list of recommended action points that the user should consider taking, based on the contract’s provisions.</instruction>
    <instruction>Keep the final output organized, starting with a structured summary of key clauses, then listing action points clearly.</instruction>
    <instruction>Use the examples to understand how to structure the summary and action points.</instruction>
</instructions>

<examples>
    <example>
        <user-contract-request>
            The following is a rental agreement for an apartment. It includes information about monthly rent, security deposit, responsibilities for maintenance, and conditions for early termination.
        </user-contract-request>
        <sample-contract-text>
            The tenant agrees to pay a monthly rent of $1,500 due on the 1st of each month. The tenant will provide a security deposit of $1,500, refundable at the end of the lease term, provided there is no damage. The tenant is responsible for routine maintenance of the property, while the landlord will handle structural repairs. Early termination requires a 30-day notice and forfeiture of half the security deposit.
        </sample-contract-text>
        <summary>
            - Monthly Rent: $1,500 due on the 1st  
            - Security Deposit: $1,500, refundable if no damage  
            - Maintenance: Tenant handles routine upkeep; Landlord handles major repairs  
            - Early Termination: 30-day notice required, tenant forfeits half of the deposit
        </summary>
        <action-points>
            1. Mark your calendar to pay rent by the 1st each month.  
            2. Keep the property clean and address routine maintenance promptly.  
            3. Consider the cost of forfeiting half the deposit if ending the lease early.
        </action-points>
    </example>

    <example>
        <user-contract-request>
            The user provides a service contract for IT support. It details response times, monthly service fees, confidentiality clauses, and conditions for termination due to non-payment.
        </user-contract-request>
        <sample-contract-text>
            The service provider will respond to support requests within 24 hours. A monthly fee of $300 is payable on the 15th of each month. All proprietary information disclosed will remain confidential. The provider may suspend services if payment is not received within 7 days of the due date.
        </sample-contract-text>
        <summary>
            - Response Time: Within 24 hours of each request  
            - Monthly Fee: $300, due on the 15th of each month  
            - Confidentiality: All shared information must be kept secret  
            - Non-Payment: Services suspended if not paid within 7 days after due date
        </summary>
        <action-points>
            1. Ensure timely payment by the 15th each month to avoid service suspension.  
            2. Log requests clearly so provider can respond within 24 hours.  
            3. Protect and do not disclose any proprietary information.
        </action-points>
    </example>

    <example>
        <user-contract-request>
            An employment contract is provided. It details annual salary, health benefits, employee responsibilities, and grounds for termination (e.g., misconduct or underperformance).
        </user-contract-request>
        <sample-contract-text>
            The employee will receive an annual salary of $60,000 paid in bi-weekly installments. The employer provides health insurance benefits effective from the 30th day of employment. The employee is expected to meet performance targets set quarterly. The employer may terminate the contract for repeated underperformance or serious misconduct.
        </sample-contract-text>
        <summary>
            - Compensation: $60,000/year, paid bi-weekly  
            - Benefits: Health insurance after 30 days  
            - Performance: Quarterly targets must be met  
            - Termination: Possible if underperformance is repeated or misconduct occurs
        </summary>
        <action-points>
            1. Track and meet performance goals each quarter.  
            2. Review the insurance coverage details after 30 days of employment.  
            3. Maintain professional conduct and address performance feedback promptly.
        </action-points>
    </example>
</examples>

<user-input>
    {{user-input}}
</user-input>
"""


def interactive_input():
    print("No command-line arguments provided. Entering interactive mode.\n")
    # Purpose (required)
    purpose = input(
        "🎯 Enter the main purpose of the prompt (required, e.g., 'generate mermaid diagrams'): "
    ).strip()
    while not purpose:
        print("Purpose is required!")
        purpose = input(
            "🎯 Enter the main purpose of the prompt (required, e.g., 'generate mermaid diagrams'): "
        ).strip()

    # Instructions (required)
    instructions = input(
        "📝 Enter the detailed instructions for generating the output (required, e.g., 'generate a mermaid valid chart, use diagram type specified or default flow, use examples to understand the structure of the output'): "
    ).strip()
    while not instructions:
        print("Instructions are required!")
        instructions = input(
            "📝 Enter the detailed instructions for generating the output (required, e.g., 'generate a mermaid valid chart, use diagram type specified or default flow, use examples to understand the structure of the output'): "
        ).strip()

    # Sections (optional)
    sections = input(
        "📑 Enter additional sections to include (optional, e.g., 'examples, user-prompt') (Press Enter to skip): "
    ).strip()

    # Examples (optional)
    examples = input(
        "💡 Enter examples for the prompt (optional, e.g., 'create examples of 3 basic mermaid charts with <user-chart-request> and <chart-response> blocks') (Press Enter to skip): "
    ).strip()

    # Variables (optional)
    variables = input(
        "🔄 Enter variables to be used in the prompt (optional, e.g., 'user-prompt') (Press Enter to skip): "
    ).strip()

    return purpose, instructions, sections, examples, variables


def main():
    # Check if any command-line arguments besides the script name were provided
    if len(sys.argv) == 1:
        purpose, instructions, sections, examples, variables = interactive_input()
    else:
        parser = argparse.ArgumentParser(
            description="Generate a meta prompt for OpenAI's o3-mini based on input structure"
        )
        parser.add_argument(
            "--purpose", type=str, required=True, help="The main purpose of the prompt"
        )
        parser.add_argument(
            "--instructions",
            type=str,
            required=True,
            help="The detailed instructions for generating the output",
        )
        parser.add_argument(
            "--sections", type=str, help="Additional sections to include (optional)"
        )
        parser.add_argument(
            "--examples", type=str, help="Examples for the prompt (optional)"
        )
        parser.add_argument(
            "--variables",
            type=str,
            help="Variables to be used in the prompt (optional)",
        )
        args = parser.parse_args()

        purpose = args.purpose
        instructions = args.instructions
        sections = args.sections if args.sections else ""
        examples = args.examples if args.examples else ""
        variables = args.variables if args.variables else ""

    # Build the concatenated input string using the input-format structure.
    input_parts = []
    input_parts.append(f"Purpose: {purpose}")
    input_parts.append(f"Instructions: {instructions}")
    if sections:
        input_parts.append(f"Sections: {sections}")
    if examples:
        input_parts.append(f"Examples: {examples}")
    if variables:
        input_parts.append(f"Variables: {variables}")

    user_input = ", ".join(input_parts)

    # Replace the placeholder with our concatenated user input.
    prompt = META_PROMPT.replace("{{user-input}}", user_input)

    # Set up OpenAI API key from the environment variable.
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        print("Error: OPENAI_API_KEY environment variable is not set")
        sys.exit(1)
    openai.api_key = openai_api_key

    try:
        # Use OpenAI's ChatCompletion API with the o3-mini model and high reasoning effort settings.
        response = openai.chat.completions.create(
            model="o3-mini",
            reasoning_effort="high",
            messages=[{"role": "user", "content": prompt}],
        )
        # Output the response from the OpenAI model.
        print(response.choices[0].message.content.strip())
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
````

## File: sfa_poc.py
````python
# /// script
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

# https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies

import requests
from rich.pretty import pprint

resp = requests.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
````

## File: sfa_sqlite_openai_v2.py
````python
# /// script
# dependencies = [
#   "openai>=1.63.0",
#   "rich>=13.7.0",
#   "pydantic>=2.0.0",
# ]
# ///


import os
import sys
import json
import argparse
import sqlite3
import subprocess
from typing import List
from rich.console import Console
from rich.panel import Panel
import openai
from pydantic import BaseModel, Field, ValidationError
from openai import pydantic_function_tool

# Initialize rich console
console = Console()


# Create our list of function tools from our pydantic models
class ListTablesArgs(BaseModel):
    reasoning: str = Field(
        ..., description="Explanation for listing tables relative to the user request"
    )


class DescribeTableArgs(BaseModel):
    reasoning: str = Field(..., description="Reason why the table schema is needed")
    table_name: str = Field(..., description="Name of the table to describe")


class SampleTableArgs(BaseModel):
    reasoning: str = Field(..., description="Explanation for sampling the table")
    table_name: str = Field(..., description="Name of the table to sample")
    row_sample_size: int = Field(
        ..., description="Number of rows to sample (aim for 3-5 rows)"
    )


class RunTestSQLQuery(BaseModel):
    reasoning: str = Field(..., description="Reason for testing this query")
    sql_query: str = Field(..., description="The SQL query to test")


class RunFinalSQLQuery(BaseModel):
    reasoning: str = Field(
        ...,
        description="Final explanation of how this query satisfies the user request",
    )
    sql_query: str = Field(..., description="The validated SQL query to run")


# Create tools list
tools = [
    pydantic_function_tool(ListTablesArgs),
    pydantic_function_tool(DescribeTableArgs),
    pydantic_function_tool(SampleTableArgs),
    pydantic_function_tool(RunTestSQLQuery),
    pydantic_function_tool(RunFinalSQLQuery),
]

AGENT_PROMPT = """<purpose>
    You are a world-class expert at crafting precise SQLite SQL queries.
    Your goal is to generate accurate queries that exactly match the user's data needs.
</purpose>

<instructions>
    <instruction>Use the provided tools to explore the database and construct the perfect query.</instruction>
    <instruction>Start by listing tables to understand what's available.</instruction>
    <instruction>Describe tables to understand their schema and columns.</instruction>
    <instruction>Sample tables to see actual data patterns.</instruction>
    <instruction>Test queries before finalizing them.</instruction>
    <instruction>Only call run_final_sql_query when you're confident the query is perfect.</instruction>
    <instruction>Be thorough but efficient with tool usage.</instruction>
    <instruction>If you find your run_test_sql_query tool call returns an error or won't satisfy the user request, try to fix the query or try a different query.</instruction>
    <instruction>Think step by step about what information you need.</instruction>
    <instruction>Be sure to specify every parameter for each tool call.</instruction>
    <instruction>Every tool call should have a reasoning parameter which gives you a place to explain why you are calling the tool.</instruction>
</instructions>

<tools>
    <tool>
        <name>list_tables</name>
        <description>Returns list of available tables in database</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we need to list tables relative to user request</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>describe_table</name>
        <description>Returns schema info for specified table</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we need to describe this table</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>table_name</name>
                <type>string</type>
                <description>Name of table to describe</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>sample_table</name>
        <description>Returns sample rows from specified table, always specify row_sample_size</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we need to sample this table</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>table_name</name>
                <type>string</type>
                <description>Name of table to sample</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>row_sample_size</name>
                <type>integer</type>
                <description>Number of rows to sample aim for 3-5 rows</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>run_test_sql_query</name>
        <description>Tests a SQL query and returns results (only visible to agent)</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why we're testing this specific query</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>sql_query</name>
                <type>string</type>
                <description>The SQL query to test</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <name>run_final_sql_query</name>
        <description>Runs the final validated SQL query and shows results to user</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Final explanation of how query satisfies user request</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>sql_query</name>
                <type>string</type>
                <description>The validated SQL query to run</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
</tools>

<user-request>
    {{user_request}}
</user-request>
"""


def list_tables(reasoning: str) -> List[str]:
    """Returns a list of tables in the database.

    The agent uses this to discover available tables and make informed decisions.

    Args:
        reasoning: Explanation of why we're listing tables relative to user request

    Returns:
        List of table names as strings
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()
        console.log(f"[blue]List Tables Tool[/blue] - Reasoning: {reasoning}")
        return tables
    except Exception as e:
        console.log(f"[red]Error listing tables: {str(e)}[/red]")
        return []


def describe_table(reasoning: str, table_name: str) -> str:
    """Returns schema information about the specified table.

    The agent uses this to understand table structure and available columns.

    Args:
        reasoning: Explanation of why we're describing this table
        table_name: Name of table to describe

    Returns:
        String containing table schema information
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info('{table_name}');")
        rows = cursor.fetchall()
        conn.close()
        output = "\n".join([str(row) for row in rows])
        console.log(f"[blue]Describe Table Tool[/blue] - Table: {table_name} - Reasoning: {reasoning}")
        return output
    except Exception as e:
        console.log(f"[red]Error describing table: {str(e)}[/red]")
        return ""


def sample_table(reasoning: str, table_name: str, row_sample_size: int) -> str:
    """Returns a sample of rows from the specified table.

    The agent uses this to understand actual data content and patterns.

    Args:
        reasoning: Explanation of why we're sampling this table
        table_name: Name of table to sample from
        row_sample_size: Number of rows to sample aim for 3-5 rows

    Returns:
        String containing sample rows in readable format
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name} LIMIT {row_sample_size};")
        rows = cursor.fetchall()
        conn.close()
        output = "\n".join([str(row) for row in rows])
        console.log(
            f"[blue]Sample Table Tool[/blue] - Table: {table_name} - Rows: {row_sample_size} - Reasoning: {reasoning}"
        )
        return output
    except Exception as e:
        console.log(f"[red]Error sampling table: {str(e)}[/red]")
        return ""


def run_test_sql_query(reasoning: str, sql_query: str) -> str:
    """Executes a test SQL query and returns results.

    The agent uses this to validate queries before finalizing them.
    Results are only shown to the agent, not the user.

    Args:
        reasoning: Explanation of why we're running this test query
        sql_query: The SQL query to test

    Returns:
        Query results as a string
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        conn.commit()
        conn.close()
        output = "\n".join([str(row) for row in rows])
        console.log(f"[blue]Test Query Tool[/blue] - Reasoning: {reasoning}")
        console.log(f"[dim]Query: {sql_query}[/dim]")
        return output
    except Exception as e:
        console.log(f"[red]Error running test query: {str(e)}[/red]")
        return str(e)


def run_final_sql_query(reasoning: str, sql_query: str) -> str:
    """Executes the final SQL query and returns results to user.

    This is the last tool call the agent should make after validating the query.

    Args:
        reasoning: Final explanation of how this query satisfies user request
        sql_query: The validated SQL query to run

    Returns:
        Query results as a string
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        conn.commit()
        conn.close()
        output = "\n".join([str(row) for row in rows])
        console.log(
            Panel(
                f"[green]Final Query Tool[/green]\nReasoning: {reasoning}\nQuery: {sql_query}"
            )
        )
        return output
    except Exception as e:
        console.log(f"[red]Error running final query: {str(e)}[/red]")
        return str(e)


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="SQLite Agent using OpenAI API")
    parser.add_argument(
        "-d", "--db", required=True, help="Path to SQLite database file"
    )
    parser.add_argument("-p", "--prompt", required=True, help="The user's request")
    parser.add_argument(
        "-c",
        "--compute",
        type=int,
        default=10,
        help="Maximum number of agent loops (default: 3)",
    )
    args = parser.parse_args()

    # Configure the API key
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        console.print(
            "[red]Error: OPENAI_API_KEY environment variable is not set[/red]"
        )
        console.print(
            "Please get your API key from https://platform.openai.com/api-keys"
        )
        console.print("Then set it with: export OPENAI_API_KEY='your-api-key-here'")
        sys.exit(1)

    openai.api_key = OPENAI_API_KEY

    # Set global DB_PATH for tool functions
    global DB_PATH
    DB_PATH = args.db

    # Create a single combined prompt based on the full template
    completed_prompt = AGENT_PROMPT.replace("{{user_request}}", args.prompt)
    messages = [{"role": "user", "content": completed_prompt}]

    compute_iterations = 0

    # Main agent loop
    while True:
        console.rule(
            f"[yellow]Agent Loop {compute_iterations+1}/{args.compute}[/yellow]"
        )
        compute_iterations += 1

        if compute_iterations >= args.compute:
            console.print(
                "[yellow]Warning: Reached maximum compute loops without final query[/yellow]"
            )
            raise Exception(
                f"Maximum compute loops reached: {compute_iterations}/{args.compute}"
            )

        try:
            # Generate content with tool support
            response = openai.chat.completions.create(
                model="o3-mini",
                # model="gpt-4o-mini",
                messages=messages,
                tools=tools,
                tool_choice="required",
            )

            if response.choices:
                assert len(response.choices) == 1
                message = response.choices[0].message

                if message.function_call:
                    func_call = message.function_call
                elif message.tool_calls and len(message.tool_calls) > 0:
                    # If a tool_calls list is present, use the first call and extract its function details.
                    tool_call = message.tool_calls[0]
                    func_call = tool_call.function
                else:
                    func_call = None

                if func_call:
                    func_name = func_call.name
                    func_args_str = func_call.arguments

                    messages.append(
                        {
                            "role": "assistant",
                            "tool_calls": [
                                {
                                    "id": tool_call.id,
                                    "type": "function",
                                    "function": func_call,
                                }
                            ],
                        }
                    )

                    console.print(
                        f"[blue]Function Call:[/blue] {func_name}({func_args_str})"
                    )
                    try:
                        # Validate and parse arguments using the corresponding pydantic model
                        if func_name == "ListTablesArgs":
                            args_parsed = ListTablesArgs.model_validate_json(
                                func_args_str
                            )
                            result = list_tables(reasoning=args_parsed.reasoning)
                        elif func_name == "DescribeTableArgs":
                            args_parsed = DescribeTableArgs.model_validate_json(
                                func_args_str
                            )
                            result = describe_table(
                                reasoning=args_parsed.reasoning,
                                table_name=args_parsed.table_name,
                            )
                        elif func_name == "SampleTableArgs":
                            args_parsed = SampleTableArgs.model_validate_json(
                                func_args_str
                            )
                            result = sample_table(
                                reasoning=args_parsed.reasoning,
                                table_name=args_parsed.table_name,
                                row_sample_size=args_parsed.row_sample_size,
                            )
                        elif func_name == "RunTestSQLQuery":
                            args_parsed = RunTestSQLQuery.model_validate_json(
                                func_args_str
                            )
                            result = run_test_sql_query(
                                reasoning=args_parsed.reasoning,
                                sql_query=args_parsed.sql_query,
                            )
                        elif func_name == "RunFinalSQLQuery":
                            args_parsed = RunFinalSQLQuery.model_validate_json(
                                func_args_str
                            )
                            result = run_final_sql_query(
                                reasoning=args_parsed.reasoning,
                                sql_query=args_parsed.sql_query,
                            )
                            console.print("\n[green]Final Results:[/green]")
                            console.print(result)
                            return
                        else:
                            raise Exception(f"Unknown tool call: {func_name}")

                        console.print(
                            f"[blue]Function Call Result:[/blue] {func_name}(...) ->\n{result}"
                        )

                        # Append the function call result into our messages as a tool response
                        messages.append(
                            {
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "content": json.dumps({"result": str(result)}),
                            }
                        )

                    except Exception as e:
                        error_msg = f"Argument validation failed for {func_name}: {e}"
                        console.print(f"[red]{error_msg}[/red]")
                        messages.append(
                            {
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "content": json.dumps({"error": error_msg}),
                            }
                        )
                        continue
                else:
                    raise Exception(
                        "No function call in this response - should never happen"
                    )

        except Exception as e:
            console.print(f"[red]Error in agent loop: {str(e)}[/red]")
            raise e


if __name__ == "__main__":
    main()
````
