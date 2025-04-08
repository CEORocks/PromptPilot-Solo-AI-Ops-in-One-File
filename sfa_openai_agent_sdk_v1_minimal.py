#!/usr/bin/env -S uv run --script

# /// script
# dependencies = [
#   "openai",
#   "openai-agents",
# ]
# ///


from agents import Agent, Runner

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model="o3-mini",
)

result = Runner.run_sync(agent, "What's your top tip for maximizing productivity?")
print(result.final_output)
