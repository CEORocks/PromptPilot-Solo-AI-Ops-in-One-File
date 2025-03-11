# OpenAI Agents SDK Examples Summary

## Overview
This repository contains 13 examples demonstrating various features of the OpenAI Agents SDK.

## Key Learnings
1. The OpenAI Agents SDK is installed via the 'openai-agents' package but imported as 'agents'
2. Agent execution is handled through Runner.run() for async and Runner.run_sync() for sync operations
3. Function tools cannot have default parameter values in their definitions
4. The RunResult object has a final_output attribute instead of output
5. The SDK supports various capabilities including multi-agent systems, tracing, and guardrails

## Testing
All examples include built-in tests that can be run with pytest:
```bash
uv run pytest example_name.py
```

## Running Examples
Each example can be run using uv:
```bash
uv run example_name.py --prompt "Your prompt here"
```

## Environment Setup
1. Install dependencies: `./install_dependencies.sh`
2. Set up API keys: `export OPENAI_API_KEY=your_key_here`

## Documentation
For more information, see the [official documentation](https://openai.github.io/openai-agents-python/).
