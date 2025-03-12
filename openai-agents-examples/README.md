# OpenAI Agents SDK Examples

A comprehensive collection of single-file examples showcasing the capabilities of the OpenAI Agents SDK.

## Overview

This repository contains 13 examples demonstrating various features of the OpenAI Agents SDK, with a focus on research and blog agents working together to create markdown blogs. Each example is implemented as a self-contained UV Python script with built-in tests.

## Key Features Demonstrated

- Basic and multi-agent systems
- Synchronous and asynchronous execution
- Tracing and monitoring
- Function tools and custom tools
- Agent handoffs and agent-as-tool patterns
- Context management
- Guardrails for safety
- Agent orchestration
- Cross-provider integration (Anthropic)
- Complete research and blog generation system

## Examples

1. [Basic Agent](01_basic_agent.py) - A simple example of how to create and run an agent.
2. [Multi-Agent](02_multi_agent.py) - An example of how to create and run multiple agents.
3. [Synchronous Agent](03_sync_agent.py) - An example of how to run an agent synchronously.
4. [Agent with Tracing](04_agent_with_tracing.py) - An example of how to use tracing with agents.
5. [Agent with Function Tools](05_agent_with_function_tools.py) - An example of how to use function tools with agents.
6. [Agent with Custom Tools](06_agent_with_custom_tools.py) - An example of how to create custom tools for agents.
7. [Agent with Handoffs](07_agent_with_handoffs.py) - An example of how to use handoffs between agents.
8. [Agent with Agent as Tool](08_agent_with_agent_as_tool.py) - An example of how to use an agent as a tool for another agent.
9. [Agent with Context Management](09_agent_with_context_management.py) - An example of how to use context management with agents.
10. [Agent with Guardrails](10_agent_with_guardrails.py) - An example of how to use guardrails with agents.
11. [Agent Orchestration](11_agent_orchestration.py) - An example of how to orchestrate multiple agents for complex tasks.
12. [Anthropic Agent](12_anthropic_agent.py) - An example of how to use Anthropic's Claude model with the Agents SDK.
13. [Research Blog System](13_research_blog_system.py) - A complete system where research agents and blog agents work together.

## Usage

Each example is a self-contained single file that can be run using uv:

```bash
uv run example_name.py --prompt "Your prompt here"
```

You can also run all examples with the provided test script:

```bash
./test_all_examples.sh
```

## Setup

1. Install the dependencies: `./install_dependencies.sh`
2. Set up your OpenAI API key: `export OPENAI_API_KEY=your_key_here`
3. For Anthropic examples, set up your Anthropic API key: `export ANTHROPIC_API_KEY=your_key_here`

## Requirements

- Python 3.10+
- uv package manager
- OpenAI API key
- Anthropic API key (for cross-provider examples)

## Testing

All examples include tests that can be run with:

```bash
uv run pytest example_name.py
```

## Important Implementation Notes

- The OpenAI Agents SDK is installed via the `openai-agents` package but imported as `agents`
- Agent execution is handled through `Runner.run()` for async and `Runner.run_sync()` for sync operations
- Function tools cannot have default parameter values in their definitions
- The `RunResult` object has a `final_output` attribute instead of `output`
- All examples use GPT-4o-mini as the primary model for non-web search functionality
- Each example includes comprehensive docstrings and comments for clarity

## Documentation

For more information about the OpenAI Agents SDK, see the [official documentation](https://openai.github.io/openai-agents-python/).
