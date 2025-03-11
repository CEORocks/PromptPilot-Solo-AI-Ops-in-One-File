#!/bin/bash

# Install all required dependencies for the examples
pip install openai-agents rich pytest markdown anthropic opentelemetry-api opentelemetry-sdk pydantic requests

# Set up environment variables if not already set
if [ -z "$OPENAI_API_KEY" ]; then
    echo "Warning: OPENAI_API_KEY environment variable not set"
    echo "Please set it with: export OPENAI_API_KEY=your_key_here"
fi

if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "Warning: ANTHROPIC_API_KEY environment variable not set"
    echo "Please set it with: export ANTHROPIC_API_KEY=your_key_here"
fi

echo "Dependencies installed successfully!"
