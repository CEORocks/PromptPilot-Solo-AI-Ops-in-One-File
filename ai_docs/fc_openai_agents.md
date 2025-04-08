# OpenAI Agents SDK Documentation

This file contains documentation for the OpenAI Agents SDK, scraped from the official documentation site.

## Overview

The [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) enables you to build agentic AI apps in a lightweight, easy-to-use package with very few abstractions. It's a production-ready upgrade of the previous experimentation for agents, [Swarm](https://github.com/openai/swarm/tree/main). The Agents SDK has a very small set of primitives:

- **Agents**, which are LLMs equipped with instructions and tools
- **Handoffs**, which allow agents to delegate to other agents for specific tasks
- **Guardrails**, which enable the inputs to agents to be validated

In combination with Python, these primitives are powerful enough to express complex relationships between tools and agents, and allow you to build real-world applications without a steep learning curve. In addition, the SDK comes with built-in **tracing** that lets you visualize and debug your agentic flows, as well as evaluate them and even fine-tune models for your application.

### Why use the Agents SDK

The SDK has two driving design principles:

1. Enough features to be worth using, but few enough primitives to make it quick to learn.
2. Works great out of the box, but you can customize exactly what happens.

Here are the main features of the SDK:

- Agent loop: Built-in agent loop that handles calling tools, sending results to the LLM, and looping until the LLM is done.
- Python-first: Use built-in language features to orchestrate and chain agents, rather than needing to learn new abstractions.
- Handoffs: A powerful feature to coordinate and delegate between multiple agents.
- Guardrails: Run input validations and checks in parallel to your agents, breaking early if the checks fail.
- Function tools: Turn any Python function into a tool, with automatic schema generation and Pydantic-powered validation.
- Tracing: Built-in tracing that lets you visualize, debug and monitor your workflows, as well as use the OpenAI suite of evaluation, fine-tuning and distillation tools.

### Installation

```bash
pip install openai-agents
```

### Hello world example

```python
from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.
```

## Quickstart

### Create a project and virtual environment

```bash
mkdir my_project
cd my_project
python -m venv .venv
source .venv/bin/activate
pip install openai-agents
export OPENAI_API_KEY=sk-...
```

### Create your first agent

```python
from agents import Agent

agent = Agent(
    name="Math Tutor",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)
```

### Add a few more agents

```python
from agents import Agent

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)
```

### Define your handoffs

```python
triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent, math_tutor_agent]
)
```

### Run the agent orchestration

```python
from agents import Runner

async def main():
    result = await Runner.run(triage_agent, "What is the capital of France?")
    print(result.final_output)
```

### Add a guardrail

```python
from agents import GuardrailFunctionOutput, Agent, Runner
from pydantic import BaseModel

class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking about homework.",
    output_type=HomeworkOutput,
)

async def homework_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
    final_output = result.final_output_as(HomeworkOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_homework,
    )
```

### Put it all together

```python
from agents import Agent, InputGuardrail,GuardrailFunctionOutput, Runner
from pydantic import BaseModel
import asyncio

class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking about homework.",
    output_type=HomeworkOutput,
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)

async def homework_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
    final_output = result.final_output_as(HomeworkOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_homework,
    )

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent, math_tutor_agent],
    input_guardrails=[
        InputGuardrail(guardrail_function=homework_guardrail),
    ],
)

async def main():
    result = await Runner.run(triage_agent, "who was the first president of the united states?")
    print(result.final_output)

    result = await Runner.run(triage_agent, "what is life")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

## Agents

Agents are the core building block in your apps. An agent is a large language model (LLM), configured with instructions and tools.

### Basic configuration

The most common properties of an agent you'll configure are:

- `instructions`: also known as a developer message or system prompt.
- `model`: which LLM to use, and optional `model_settings` to configure model tuning parameters like temperature, top_p, etc.
- `tools`: Tools that the agent can use to achieve its tasks.

```python
from agents import Agent, ModelSettings, function_tool

@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny"

agent = Agent(
    name="Haiku agent",
    instructions="Always respond in haiku form",
    model="o3-mini",
    tools=[get_weather],
)
```

### Context

Agents are generic on their `context` type. Context is a dependency-injection tool: it's an object you create and pass to `Runner.run()`, that is passed to every agent, tool, handoff etc, and it serves as a grab bag of dependencies and state for the agent run. You can provide any Python object as the context.

### Output types

By default, agents produce plain text (i.e. `str`) outputs. If you want the agent to produce a particular type of output, you can use the `output_type` parameter.

### Handoffs

Handoffs are sub-agents that the agent can delegate to. You provide a list of handoffs, and the agent can choose to delegate to them if relevant.

### Dynamic instructions

In most cases, you can provide instructions when you create the agent. However, you can also provide dynamic instructions via a function.

### Lifecycle events (hooks)

Sometimes, you want to observe the lifecycle of an agent. For example, you may want to log events, or pre-fetch data when certain events occur.

### Guardrails

Guardrails allow you to run checks/validations on user input, in parallel to the agent running.

### Cloning/copying agents

By using the `clone()` method on an agent, you can duplicate an Agent, and optionally change any properties you like.

## Handoffs

Handoffs allow an agent to delegate tasks to another agent. This is particularly useful in scenarios where different agents specialize in distinct areas.

### Creating a handoff

All agents have a `handoffs` param, which can either take an `Agent` directly, or a `Handoff` object that customizes the Handoff.

### Basic Usage

```python
from agents import Agent, handoff

billing_agent = Agent(name="Billing agent")
refund_agent = Agent(name="Refund agent")

triage_agent = Agent(name="Triage agent", handoffs=[billing_agent, handoff(refund_agent)])
```

### Customizing handoffs

The `handoff()` function lets you customize various aspects like tool name, description, callbacks, and input filtering.

### Handoff inputs

You can have the LLM provide data when calling a handoff, which is useful for logging or other purposes.

### Input filters

When a handoff occurs, the new agent sees the entire previous conversation history by default. Input filters allow you to modify this behavior.

### Recommended prompts

To ensure LLMs understand handoffs properly, include information about handoffs in your agent instructions.

## Tools

Tools let agents take actions: things like fetching data, running code, calling external APIs, and even using a computer. There are three classes of tools in the Agent SDK:

- Hosted tools: run on LLM servers alongside the AI models
- Function calling: allow you to use any Python function as a tool
- Agents as tools: allow you to use an agent as a tool

### Hosted tools

OpenAI offers built-in tools like `WebSearchTool`, `FileSearchTool`, and `ComputerTool`.

### Function tools

You can use any Python function as a tool. The Agents SDK will automatically set up the tool with appropriate name, description and schema.

```python
import json
from typing_extensions import TypedDict

from agents import Agent, FunctionTool, RunContextWrapper, function_tool

class Location(TypedDict):
    lat: float
    long: float

@function_tool
async def fetch_weather(location: Location) -> str:
    """Fetch the weather for a given location.

    Args:
        location: The location to fetch the weather for.
    """
    # In real life, we'd fetch the weather from a weather API
    return "sunny"

@function_tool(name_override="fetch_data")
def read_file(ctx: RunContextWrapper[Any], path: str, directory: str | None = None) -> str:
    """Read the contents of a file."""
    # In real life, we'd read the file from the file system
    return "<file contents>"
```

### Agents as tools

In some workflows, you may want a central agent to orchestrate a network of specialized agents, instead of handing off control.

### Handling errors in function tools

You can customize error handling for function tools using the `failure_error_function` parameter.

## Results

When you call the `Runner.run` methods, you get either a `RunResult` or `RunResultStreaming` object containing information about the agent run.

### Final output

The `final_output` property contains the final output of the last agent that ran.

### Inputs for the next turn

You can use `result.to_input_list()` to turn the result into an input list that concatenates the original input you provided with items generated during the agent run.

### Last agent

The `last_agent` property contains the last agent that ran, which can be useful for subsequent user interactions.

### New items

The `new_items` property contains the new items generated during the run, including messages, tool calls, handoffs, etc.

## Running agents

You can run agents via the `Runner` class with three options:

1. `Runner.run()` - async method returning a `RunResult`
2. `Runner.run_sync()` - sync wrapper around `run()`
3. `Runner.run_streamed()` - async method that streams LLM events as they occur

### The agent loop

When you use the run method, the runner executes a loop:

1. Call the LLM for the current agent with the current input
2. Process the LLM output:
   - If it's a final output, end the loop and return the result
   - If it's a handoff, update the current agent and input, and re-run the loop
   - If it's tool calls, run the tools, append results, and re-run the loop
3. If max_turns is exceeded, raise an exception

### Run config

The `run_config` parameter lets you configure various global settings for the agent run.

### Conversations/chat threads

Each run represents a single logical turn in a chat conversation. You can use `RunResultBase.to_input_list()` to get inputs for the next turn.

## Tracing

The Agents SDK includes built-in tracing, collecting a comprehensive record of events during an agent run: LLM generations, tool calls, handoffs, guardrails, and custom events.

### Traces and spans

- **Traces** represent a single end-to-end operation of a "workflow"
- **Spans** represent operations that have a start and end time

### Default tracing

By default, the SDK traces the entire run, each agent execution, LLM generations, function tool calls, guardrails, and handoffs.

### Higher level traces

Sometimes, you might want multiple calls to `run()` to be part of a single trace:

```python
from agents import Agent, Runner, trace

async def main():
    agent = Agent(name="Joke generator", instructions="Tell funny jokes.")

    with trace("Joke workflow"):
        first_result = await Runner.run(agent, "Tell me a joke")
        second_result = await Runner.run(agent, f"Rate this joke: {first_result.final_output}")
        print(f"Joke: {first_result.final_output}")
        print(f"Rating: {second_result.final_output}")
```

### Custom trace processors

You can customize tracing to send traces to alternative or additional backends:

1. `add_trace_processor()` adds an additional processor alongside the default one
2. `set_trace_processors()` replaces the default processor entirely

## Context Management

Context is an overloaded term with two main aspects:

1. **Local context**: Data and dependencies available to your code during tool function execution, callbacks, lifecycle hooks, etc.
2. **LLM context**: Data the LLM sees when generating a response

### Local context

This is represented via the `RunContextWrapper` class and allows you to pass any Python object to be available throughout the agent run:

```python
import asyncio
from dataclasses import dataclass

from agents import Agent, RunContextWrapper, Runner, function_tool

@dataclass
class UserInfo:
    name: str
    uid: int

@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:
    return f"User {wrapper.context.name} is 47 years old"

async def main():
    user_info = UserInfo(name="John", uid=123)

    agent = Agent[UserInfo](
        name="Assistant",
        tools=[fetch_user_age],
    )

    result = await Runner.run(
        starting_agent=agent,
        input="What is the age of the user?",
        context=user_info,
    )

    print(result.final_output)
    # The user John is 47 years old.
```

### Agent/LLM context

When an LLM is called, it can only see data from the conversation history. There are several ways to make data available:

1. Add it to the Agent `instructions` (system prompt)
2. Add it to the `input` when calling `Runner.run`
3. Expose it via function tools for on-demand access
4. Use retrieval or web search tools to fetch relevant contextual data

## Model Context Protocol (MCP)

The [Model Context Protocol](https://modelcontextprotocol.io/introduction) (aka MCP) is a way to provide tools and context to the LLM. MCP provides a standardized way to connect AI models to different data sources and tools.

### MCP Servers

The Agents SDK supports two types of MCP servers:

1. **stdio servers** run as a subprocess of your application (locally)
2. **HTTP over SSE servers** run remotely (connect via URL)

You can use `MCPServerStdio` and `MCPServerSse` classes to connect to these servers:

```python
from agents.mcp.server import MCPServerStdio, MCPServerSse

# Example using the filesystem MCP server
async with MCPServerStdio(
    params={
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", samples_dir],
    }
) as server:
    tools = await server.list_tools()
```

### Using MCP Servers with Agents

MCP servers can be added directly to Agents:

```python
agent = Agent(
    name="Assistant",
    instructions="Use the tools to achieve the task",
    mcp_servers=[mcp_server_1, mcp_server_2]
)
```

When the Agent runs, it will automatically call `list_tools()` on all MCP servers, making the LLM aware of all available tools. When the LLM calls a tool from an MCP server, the SDK handles calling `call_tool()` on that server.

### Caching Tool Lists

For better performance, especially with remote servers, you can cache the list of tools:

```python
mcp_server = MCPServerSse(
    url="https://example.com/mcp",
    cache_tools_list=True  # Enable caching
)

# Later, if needed, clear the cache
mcp_server.invalidate_tools_cache()
```

Only use caching when you're certain the tool list will not change during execution.

### Tracing MCP Operations

The Agents SDK's tracing system automatically captures MCP operations, including:

1. Calls to MCP servers to list tools
2. MCP-related information on function calls

This makes it easier to debug and analyze your agent's interactions with MCP tools.

### Use a different LLM

```python
import asyncio
import os

from openai import AsyncOpenAI

from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool, set_tracing_disabled

BASE_URL = os.getenv("EXAMPLE_BASE_URL") or ""
API_KEY = os.getenv("EXAMPLE_API_KEY") or ""
MODEL_NAME = os.getenv("EXAMPLE_MODEL_NAME") or ""

if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError(
        "Please set EXAMPLE_BASE_URL, EXAMPLE_API_KEY, EXAMPLE_MODEL_NAME via env var or code."
    )

"""This example uses a custom provider for a specific agent. Steps:
1. Create a custom OpenAI client.
2. Create a `Model` that uses the custom client.
3. Set the `model` on the Agent.

Note that in this example, we disable tracing under the assumption that you don't have an API key
from platform.openai.com. If you do have one, you can either set the `OPENAI_API_KEY` env var
or call set_tracing_export_api_key() to set a tracing specific key.
"""
client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)
set_tracing_disabled(disabled=True)

# An alternate approach that would also work:
# PROVIDER = OpenAIProvider(openai_client=client)
# agent = Agent(..., model="some-custom-model")
# Runner.run(agent, ..., run_config=RunConfig(model_provider=PROVIDER))


@function_tool
def get_weather(city: str):
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."


async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
        tools=[get_weather],
    )

    result = await Runner.run(agent, "What's the weather in Tokyo?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
```