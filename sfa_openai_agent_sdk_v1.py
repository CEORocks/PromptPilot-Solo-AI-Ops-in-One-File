#!/usr/bin/env -S uv run --script

# /// script
# dependencies = [
#   "openai",
#   "openai-agents",
#   "pydantic",
#   "typing_extensions",
#   "@modelcontextprotocol/server-filesystem"
# ]
# ///

"""
OpenAI Agent SDK Showcase

A single-file utility showcasing different features of the OpenAI Agent SDK.
Each function demonstrates a specific capability and can be run individually.

Examples:
    # Run basic agent example
    uv run sfa_openai_agent_sdk_v1.py --basic

    # Run agent with custom model settings (temperature, etc.)
    uv run sfa_openai_agent_sdk_v1.py --model-settings

    # Run agent with function tools (weather and mortgage calculator)
    uv run sfa_openai_agent_sdk_v1.py --tools

    # Run agent with complex data type tools
    uv run sfa_openai_agent_sdk_v1.py --complex-types

    # Run agent with handoffs to specialized agents
    uv run sfa_openai_agent_sdk_v1.py --handoffs

    # Run agent with input guardrails for filtering requests
    uv run sfa_openai_agent_sdk_v1.py --guardrails

    # Run agent with structured output using Pydantic models
    uv run sfa_openai_agent_sdk_v1.py --structured

    # Run agent with context data for state management
    uv run sfa_openai_agent_sdk_v1.py --context

    # Run agent with tracing for workflow visualization
    uv run sfa_openai_agent_sdk_v1.py --tracing

    # Run agent with streaming output capabilities
    uv run sfa_openai_agent_sdk_v1.py --streaming
    
    # Run agent with Model Context Protocol (MCP) server
    # Note: Requires npm for the MCP filesystem server
    uv run sfa_openai_agent_sdk_v1.py --mcp

    # Run all examples at once
    uv run sfa_openai_agent_sdk_v1.py --all
"""

import asyncio
import argparse
import json
import os
import tempfile
from typing import List, Dict, Any, Optional
from typing_extensions import TypedDict
from pydantic import BaseModel

from agents import (
    Agent,
    Runner,
    trace,
    handoff,
    function_tool,
    InputGuardrail,
    GuardrailFunctionOutput,
    FunctionTool,
    RunContextWrapper,
    ModelSettings,
)
from agents.mcp.server import MCPServerStdio, MCPServerSse


def run_basic_agent():
    """Run a simple agent with basic instructions."""
    agent = Agent(name="Assistant", instructions="You are a helpful assistant")

    result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
    print(f"Basic Agent Result:\n{result.final_output}\n")


def run_agent_with_model_settings():
    """Run an agent with custom model settings like temperature."""
    agent = Agent(
        name="Creative Assistant",
        instructions="You are a highly creative assistant who writes imaginative content.",
        model="gpt-4o",
        model_settings=ModelSettings(temperature=0.9, top_p=0.95),
    )

    result = Runner.run_sync(agent, "Write a short poem about artificial intelligence.")
    print(f"Agent with Custom Model Settings:\n{result.final_output}\n")


@function_tool
def get_weather(city: str) -> str:
    """Get the current weather for a city.

    Args:
        city: The name of the city to get weather for
    """
    # This would normally call a weather API
    weather_data = {
        "New York": "72°F and Sunny",
        "London": "65°F and Rainy",
        "Tokyo": "80°F and Partly Cloudy",
        "Sydney": "70°F and Clear",
    }
    return weather_data.get(city, f"Weather data for {city} is not available")


@function_tool
def calculate_mortgage(principal: float, interest_rate: float, years: int) -> str:
    """Calculate monthly mortgage payment.

    Args:
        principal: Loan amount in dollars
        interest_rate: Annual interest rate (percentage)
        years: Loan term in years
    """
    monthly_rate = interest_rate / 100 / 12
    num_payments = years * 12

    # Mortgage calculation formula
    if monthly_rate == 0:
        monthly_payment = principal / num_payments
    else:
        monthly_payment = (
            principal
            * (monthly_rate * (1 + monthly_rate) ** num_payments)
            / ((1 + monthly_rate) ** num_payments - 1)
        )

    return f"Monthly payment: ${monthly_payment:.2f} for a ${principal} loan at {interest_rate}% over {years} years"


def run_agent_with_tools():
    """Run an agent with function tools."""
    agent = Agent(
        name="Financial Assistant",
        instructions="You are a helpful assistant with expertise in finance and weather information.",
        tools=[get_weather, calculate_mortgage],
    )

    result = Runner.run_sync(
        agent,
        "What's the monthly payment on a $500,000 mortgage at 6.5% interest for 30 years? Also, what's the weather in London?",
    )
    print(f"Agent with Tools Result:\n{result.final_output}\n")


class Location(TypedDict):
    lat: float
    long: float


@function_tool
def get_location_weather(location: Location) -> str:
    """Get weather for a specific latitude and longitude.

    Args:
        location: A dictionary with lat and long keys
    """
    # This would normally call a weather API with coordinates
    return f"The weather at coordinates ({location['lat']}, {location['long']}) is sunny and 75°F"


def run_agent_with_complex_types():
    """Run an agent with tools that accept complex types."""
    agent = Agent(
        name="Geo Assistant",
        instructions="You help users with geographic information and weather data.",
        tools=[get_location_weather],
    )

    result = Runner.run_sync(
        agent, "What's the weather at coordinates 40.7128, -74.0060?"
    )
    print(f"Agent with Complex Types Result:\n{result.final_output}\n")


def create_handoff_agents():
    """Create a set of agents with handoff capabilities."""
    math_agent = Agent(
        name="Math Agent",
        handoff_description="Expert at solving mathematical problems",
        instructions="You are an expert at solving mathematical problems. Provide step-by-step solutions.",
    )

    history_agent = Agent(
        name="History Agent",
        handoff_description="Expert on historical topics",
        instructions="You provide detailed information about historical events, figures, and contexts.",
    )

    triage_agent = Agent(
        name="Triage Agent",
        instructions="You determine whether a question is about math or history and hand off to the appropriate specialist.",
        handoffs=[math_agent, history_agent],
    )

    return triage_agent


def run_agent_with_handoffs():
    """Run an agent that can hand off to specialized agents."""
    triage_agent = create_handoff_agents()

    # Math question
    result1 = Runner.run_sync(
        triage_agent, "What is the quadratic formula and how do I use it?"
    )
    print(f"Handoff Result (Math Question):\n{result1.final_output}\n")

    # History question
    result2 = Runner.run_sync(
        triage_agent, "Who was the first president of the United States?"
    )
    print(f"Handoff Result (History Question):\n{result2.final_output}\n")


class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str


def create_guardrail_agent():
    """Create an agent with input guardrails."""
    guardrail_agent = Agent(
        name="Guardrail check",
        instructions="Check if the user is asking for homework help. If they are just asking for explanation of concepts, that's OK.",
        output_type=HomeworkOutput,
    )

    async def homework_guardrail(ctx, agent, input_data):
        result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
        final_output = result.final_output_as(HomeworkOutput)
        return GuardrailFunctionOutput(
            output_info=final_output,
            tripwire_triggered=final_output.is_homework  # Trigger if IS homework
        )

    tutor_agent = Agent(
        name="Tutor Agent",
        instructions="You help students understand academic concepts. Do not solve homework problems directly. If a student asks for a direct homework answer, respond: 'I can't provide direct homework answers, but I can help explain concepts.'",
        input_guardrails=[
            InputGuardrail(guardrail_function=homework_guardrail),
        ],
    )

    return tutor_agent


def run_agent_with_guardrails():
    """Run an agent with input guardrails for filtering requests."""
    tutor_agent = create_guardrail_agent()

    # Conceptual question (should pass guardrail)
    result1 = Runner.run_sync(tutor_agent, "Can you explain how photosynthesis works?")
    print(f"Guardrail Result (Conceptual Question):\n{result1.final_output}\n")

    # Homework question (should trigger guardrail)
    result2 = Runner.run_sync(
        tutor_agent,
        "Solve this problem for my homework: If x^2 + 5x + 6 = 0, what are the values of x?",
    )
    print(f"Guardrail Result (Homework Question):\n{result2.final_output}\n")


@function_tool
def search_database(query: str) -> List[Dict[str, Any]]:
    """Search a database for information.

    Args:
        query: The search query
    """
    # Mock database results
    if "product" in query.lower():
        return [
            {"id": 1, "name": "Smartphone", "price": 699.99},
            {"id": 2, "name": "Laptop", "price": 1299.99},
            {"id": 3, "name": "Tablet", "price": 499.99},
        ]
    elif "customer" in query.lower():
        return [
            {"id": 101, "name": "Alice Smith", "email": "alice@example.com"},
            {"id": 102, "name": "Bob Jones", "email": "bob@example.com"},
        ]
    else:
        return []


def run_agent_with_structured_output():
    """Run an agent that returns structured data."""

    class ProductRecommendation(BaseModel):
        best_product: str
        price: float
        reason: str

    agent = Agent(
        name="Product Advisor",
        instructions="You help customers find the best product for their needs. Return a structured recommendation.",
        tools=[search_database],
        output_type=ProductRecommendation,
    )

    result = Runner.run_sync(
        agent, "I need a recommendation for a portable computing device"
    )
    output = result.final_output_as(ProductRecommendation)

    print(f"Structured Output Result:\n")
    print(f"Best Product: {output.best_product}")
    print(f"Price: ${output.price}")
    print(f"Reason: {output.reason}\n")


@function_tool
def log_conversation(ctx: RunContextWrapper[Dict[str, Any]], message: str) -> str:
    """Log a message with the current conversation ID.

    Args:
        ctx: The context wrapper containing conversation metadata
        message: The message to log
    """
    conv_id = ctx.context.get("conversation_id", "unknown")
    print(f"[LOGGING] Conversation {conv_id}: {message}")
    return f"Message logged for conversation {conv_id}"


def run_agent_with_context():
    """Run an agent with custom context data."""
    agent = Agent(
        name="Support Agent",
        instructions="You help customers with their support requests. Use the log_conversation tool to track important information.",
        tools=[log_conversation],
    )

    # Create context with conversation metadata
    context = {
        "conversation_id": "CONV-12345",
        "user_info": {"name": "John Doe", "customer_tier": "premium"},
    }

    result = Runner.run_sync(
        agent, "I'm having issues with my account login", context=context
    )

    print(f"Context-Aware Agent Result:\n{result.final_output}\n")


async def run_tracing_example():
    """Run an agent with tracing for the entire workflow."""
    agent = Agent(
        name="Tracing Example Agent", instructions="You provide helpful responses."
    )

    async with trace("Multi-turn conversation"):
        first_result = await Runner.run(agent, "Tell me a short story about a robot.")
        print(f"First Response:\n{first_result.final_output}\n")

        # Use the first result to inform the second query
        second_result = await Runner.run(
            agent, f"Give that story a happy ending: {first_result.final_output}"
        )
        print(f"Second Response:\n{second_result.final_output}\n")


def run_streaming_example():
    """Run an agent with streaming output."""
    agent = Agent(
        name="Streaming Agent",
        instructions="You write creative stories with lots of detail.",
    )

    # This would normally be used in an async context
    # For this example, we'll use the sync wrapper
    result = Runner.run_sync(
        agent, "Write a short story about an AI that becomes self-aware."
    )

    print(f"Streaming Agent Result (final output):\n{result.final_output}\n")
    print(
        "Note: In a real application, you would use Runner.run_streamed() to get the tokens as they're generated."
    )


async def run_agent_with_mcp():
    """Run an agent with Model Context Protocol (MCP) server for tools."""
    # Create a temporary directory for the filesystem MCP server
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a sample file in the temporary directory
        sample_file_path = os.path.join(temp_dir, "sample.txt")
        with open(sample_file_path, "w") as f:
            f.write("This is a sample file created by the OpenAI Agent SDK MCP example.")
        
        print(f"Created temporary directory at {temp_dir} with a sample file")
        
        # Start an MCP filesystem server pointing to our temporary directory
        async with MCPServerStdio(
            params={
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-filesystem", temp_dir],
            }
        ) as server:
            # List available tools from the MCP server
            tools = await server.list_tools()
            print(f"MCP Server initialized with {len(tools)} tools")
            
            # Create an agent with access to the MCP server
            agent = Agent(
                name="MCP File Explorer",
                instructions="You help users navigate and read files in a directory. Use the provided MCP tools to explore the filesystem and read files when requested.",
                mcp_servers=[server],
            )
            
            # Run the agent
            result = await Runner.run(
                agent, 
                "What files are available in the current directory? Please read the contents of any text files you find."
            )
            
            print(f"MCP Agent Result:\n{result.final_output}\n")
            
            # Second query using the same agent
            result2 = await Runner.run(
                agent,
                "Could you tell me the character count in the sample file?"  
            )
            
            print(f"MCP Agent Follow-up Result:\n{result2.final_output}\n")


def main():
    parser = argparse.ArgumentParser(description="OpenAI Agent SDK Examples")
    parser.add_argument("--all", action="store_true", help="Run all examples")
    parser.add_argument("--basic", action="store_true", help="Run basic agent example")
    parser.add_argument(
        "--model-settings",
        action="store_true",
        help="Run agent with custom model settings",
    )
    parser.add_argument("--tools", action="store_true", help="Run agent with tools")
    parser.add_argument(
        "--complex-types", action="store_true", help="Run agent with complex type tools"
    )
    parser.add_argument(
        "--handoffs", action="store_true", help="Run agent with handoffs"
    )
    parser.add_argument(
        "--guardrails", action="store_true", help="Run agent with guardrails"
    )
    parser.add_argument(
        "--structured", action="store_true", help="Run agent with structured output"
    )
    parser.add_argument("--context", action="store_true", help="Run agent with context")
    parser.add_argument("--tracing", action="store_true", help="Run agent with tracing")
    parser.add_argument(
        "--streaming", action="store_true", help="Run agent with streaming"
    )
    parser.add_argument(
        "--mcp", action="store_true", help="Run agent with MCP server"
    )

    args = parser.parse_args()

    # If no arguments provided, show help
    if not any(vars(args).values()):
        parser.print_help()
        return

    # Run selected examples
    if args.all or args.basic:
        run_basic_agent()

    if args.all or args.model_settings:
        run_agent_with_model_settings()

    if args.all or args.tools:
        run_agent_with_tools()

    if args.all or args.complex_types:
        run_agent_with_complex_types()

    if args.all or args.handoffs:
        run_agent_with_handoffs()

    if args.all or args.guardrails:
        run_agent_with_guardrails()

    if args.all or args.structured:
        run_agent_with_structured_output()

    if args.all or args.context:
        run_agent_with_context()

    if args.all or args.tracing:
        asyncio.run(run_tracing_example())

    if args.all or args.streaming:
        run_streaming_example()
        
    if args.all or args.mcp:
        asyncio.run(run_agent_with_mcp())


if __name__ == "__main__":
    main()
