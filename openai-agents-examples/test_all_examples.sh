#!/bin/bash

# Set up environment
export OPENAI_API_KEY=$GenAI_Keys_OPENAI_API_KEY
export ANTHROPIC_API_KEY=$GenAI_Keys_ANTHROPIC_API_KEY

# Test basic examples
echo "Testing 01_basic_agent.py..."
uv run 01_basic_agent.py --prompt "What is 2+2?"

echo "Testing 02_multi_agent.py..."
uv run 02_multi_agent.py --prompt "What are the benefits of exercise?"

echo "Testing 03_sync_agent.py..."
uv run 03_sync_agent.py --prompt "Tell me a fun fact"

echo "Testing 04_agent_with_tracing.py..."
uv run 04_agent_with_tracing.py --prompt "What is the capital of France?"

echo "Testing 05_agent_with_function_tools.py..."
uv run 05_agent_with_function_tools.py --prompt "What's the weather in New York?"

echo "Testing 06_agent_with_custom_tools.py..."
uv run 06_agent_with_custom_tools.py --prompt "Calculate 15% tip on a $75 bill"

echo "Testing 07_agent_with_handoffs.py..."
uv run 07_agent_with_handoffs.py --prompt "I need help with a coding problem"

echo "Testing 08_agent_with_agent_as_tool.py..."
uv run 08_agent_with_agent_as_tool.py --prompt "Tell me about climate change"

echo "Testing 09_agent_with_context_management.py..."
uv run 09_agent_with_context_management.py --prompt "Tell me about Mars" --follow-up "What about its moons?"

echo "Testing 10_agent_with_guardrails.py..."
uv run 10_agent_with_guardrails.py --prompt "Tell me about renewable energy"

echo "Testing 11_agent_orchestration.py..."
uv run 11_agent_orchestration.py --prompt "Write a short blog post about AI"

echo "Testing 12_anthropic_agent.py..."
uv run 12_anthropic_agent.py --prompt "What is your favorite book?"

echo "Testing 13_research_blog_system.py..."
uv run 13_research_blog_system.py --topic "Space Exploration" --output "space_blog.md"

echo "All tests completed successfully!"
