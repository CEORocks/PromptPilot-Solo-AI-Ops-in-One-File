#!/usr/bin/env python3

# /// script
# dependencies = [
#   "anthropic>=0.18.0",
#   "rich>=13.7.0",
# ]
# ///

"""
/// Example Usage

# View a file
uv run sfa_file_editor_sonny37_v1.py --prompt "Show me the content of README.md"

# Edit a file
uv run sfa_file_editor_sonny37_v1.py --prompt "Fix the syntax error in sfa_poc.py"

# Create a new file
uv run sfa_file_editor_sonny37_v1.py --prompt "Create a new file called hello.py with a function that prints Hello World"

# Add docstrings to functions
uv run sfa_file_editor_sonny37_v1.py --prompt "Add proper docstrings to all functions in sfa_poc.py"

# Insert code at specific location
uv run sfa_file_editor_sonny37_v1.py --prompt "Insert error handling code before the API call in sfa_duckdb_openai_v2.py"

# Modify multiple files
uv run sfa_file_editor_sonny37_v1.py --prompt "Update all print statements in agent_workspace directory to use f-strings"

# Refactor code
uv run sfa_file_editor_sonny37_v1.py --prompt "Refactor the factorial function in agent_workspace/test.py to use iteration instead of recursion"

# Create new test files
uv run sfa_file_editor_sonny37_v1.py --prompt "Create unit tests for the functions in sfa_file_editor_sonny37_v1.py and save them in agent_workspace/test_file_editor.py"

# Run with higher thinking tokens
uv run sfa_file_editor_sonny37_v1.py --prompt "Refactor README.md to make it more concise" --thinking 5000

# Increase max loops for complex tasks
uv run sfa_file_editor_sonny37_v1.py --prompt "Create a Python class that implements a binary search tree with insert, delete, and search methods" --max-loops 20

# Use token-efficient tools (reduces token usage and latency)
uv run sfa_file_editor_sonny37_v1.py --prompt "Add error handling to all functions in sfa_poc.py" --efficient

///
"""

import os
import sys
import argparse
import time
from typing import List, Dict, Any, Optional
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.syntax import Syntax
from anthropic import Anthropic

# Initialize rich console
console = Console()

# Define constants
MODEL = "claude-3-7-sonnet-20250219"
DEFAULT_THINKING_TOKENS = 3000
WORKSPACE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_workspace")


def view_file(path: str, view_range=None) -> Dict[str, Any]:
    """
    View the contents of a file.
    
    Args:
        path: The path to the file to view
        view_range: Optional start and end lines to view [start, end]
    
    Returns:
        Dictionary with content or error message
    """
    try:
        if not os.path.exists(path):
            return {"error": f"File {path} does not exist"}
            
        with open(path, 'r') as f:
            lines = f.readlines()
        
        if view_range:
            start, end = view_range
            # Convert to 0-indexed for Python
            start = max(0, start - 1)
            if end == -1:
                end = len(lines)
            else:
                end = min(len(lines), end)
            lines = lines[start:end]
        
        content = ''.join(lines)
        
        # Display the file content (only for console, not returned to Claude)
        file_extension = os.path.splitext(path)[1][1:]  # Get extension without the dot
        syntax = Syntax(content, file_extension or "text", line_numbers=True)
        console.print(Panel(syntax, title=f"File: {path}"))
        
        return {"result": content}
    except Exception as e:
        error_msg = f"Error viewing file: {str(e)}"
        console.print(f"[red]{error_msg}[/red]")
        return {"error": error_msg}


def str_replace(path: str, old_str: str, new_str: str) -> Dict[str, Any]:
    """
    Replace a specific string in a file.
    
    Args:
        path: The path to the file to modify
        old_str: The text to replace
        new_str: The new text to insert
    
    Returns:
        Dictionary with result or error message
    """
    try:
        if not os.path.exists(path):
            return {"error": f"File {path} does not exist"}
            
        with open(path, 'r') as f:
            content = f.read()
        
        if old_str not in content:
            return {"error": f"The specified string was not found in the file {path}"}
        
        new_content = content.replace(old_str, new_str, 1)
        
        with open(path, 'w') as f:
            f.write(new_content)
        
        console.print(f"[green]Successfully replaced text in {path}[/green]")
        return {"result": f"Successfully replaced text in {path}"}
    except Exception as e:
        error_msg = f"Error replacing text: {str(e)}"
        console.print(f"[red]{error_msg}[/red]")
        return {"error": error_msg}


def create_file(path: str, file_text: str) -> Dict[str, Any]:
    """
    Create a new file with specified content.
    
    Args:
        path: The path where the new file should be created
        file_text: The content to write to the new file
    
    Returns:
        Dictionary with result or error message
    """
    try:
        # Check if the directory exists
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        with open(path, 'w') as f:
            f.write(file_text)
        
        console.print(f"[green]Successfully created file {path}[/green]")
        return {"result": f"Successfully created file {path}"}
    except Exception as e:
        error_msg = f"Error creating file: {str(e)}"
        console.print(f"[red]{error_msg}[/red]")
        return {"error": error_msg}


def insert_text(path: str, insert_line: int, new_str: str) -> Dict[str, Any]:
    """
    Insert text at a specific location in a file.
    
    Args:
        path: The path to the file to modify
        insert_line: The line number after which to insert the text
        new_str: The text to insert
    
    Returns:
        Dictionary with result or error message
    """
    try:
        if not os.path.exists(path):
            return {"error": f"File {path} does not exist"}
            
        with open(path, 'r') as f:
            lines = f.readlines()
        
        # Line is 0-indexed for this function, but Claude provides 1-indexed
        insert_line = min(max(0, insert_line - 1), len(lines))
        
        # Ensure new_str ends with newline
        if new_str and not new_str.endswith('\n'):
            new_str += '\n'
            
        lines.insert(insert_line, new_str)
        
        with open(path, 'w') as f:
            f.writelines(lines)
        
        console.print(f"[green]Successfully inserted text at line {insert_line + 1} in {path}[/green]")
        return {"result": f"Successfully inserted text at line {insert_line + 1} in {path}"}
    except Exception as e:
        error_msg = f"Error inserting text: {str(e)}"
        console.print(f"[red]{error_msg}[/red]")
        return {"error": error_msg}


def undo_edit(path: str) -> Dict[str, Any]:
    """
    Placeholder for undo_edit functionality.
    In a real implementation, you would need to track edit history.
    
    Args:
        path: The path to the file whose last edit should be undone
    
    Returns:
        Dictionary with message about undo functionality
    """
    message = "Undo functionality is not implemented in this version."
    console.print(f"[yellow]{message}[/yellow]")
    return {"result": message}


def handle_tool_use(tool_use: Dict[str, Any]) -> Dict[str, Any]:
    """
    Handle text editor tool use from Claude.
    
    Args:
        tool_use: The tool use request from Claude
    
    Returns:
        Dictionary with result or error to send back to Claude
    """
    command = tool_use.get("command")
    path = tool_use.get("path")
    
    # Normalize path to use workspace directory if not absolute
    if not os.path.isabs(path):
        path = os.path.join(WORKSPACE_DIR, path)
    elif path.startswith("/agent_workspace/"):
        # Handle the case when Claude uses "/agent_workspace/" prefix
        relative_path = path.replace("/agent_workspace/", "", 1)
        path = os.path.join(WORKSPACE_DIR, relative_path)
    
    console.print(f"[blue]Executing {command} command on {path}[/blue]")
    
    if command == "view":
        view_range = tool_use.get("view_range")
        return view_file(path, view_range)
    
    elif command == "str_replace":
        old_str = tool_use.get("old_str")
        new_str = tool_use.get("new_str")
        return str_replace(path, old_str, new_str)
    
    elif command == "create":
        file_text = tool_use.get("file_text")
        return create_file(path, file_text)
    
    elif command == "insert":
        insert_line = tool_use.get("insert_line")
        new_str = tool_use.get("new_str")
        return insert_text(path, insert_line, new_str)
    
    elif command == "undo_edit":
        return undo_edit(path)
    
    else:
        error_msg = f"Unknown command: {command}"
        console.print(f"[red]{error_msg}[/red]")
        return {"error": error_msg}


def run_agent(client: Anthropic, prompt: str, max_thinking_tokens: int = DEFAULT_THINKING_TOKENS, max_loops: int = 10, use_efficient_tools: bool = False) -> str:
    """
    Run the Claude agent with file editing capabilities.
    
    Args:
        client: The Anthropic client
        prompt: The user's prompt
        max_thinking_tokens: Maximum tokens for thinking
        max_loops: Maximum number of tool use loops
        use_efficient_tools: Whether to use token-efficient tool calling
    
    Returns:
        Final response from Claude
    """
    system_prompt = """You are a helpful AI assistant with text editing capabilities.
You have access to a text editor tool that can view, edit, and create files.
Always think step by step about what you need to do before taking any action.
Be careful when making edits to files, as they can permanently change the user's files.
Follow these steps when handling file operations:
1. First, view files to understand their content before making changes
2. For edits, ensure you have the correct context and are making the right changes
3. When creating files, make sure they're in the right location with proper formatting
"""

    # Define text editor tool
    text_editor_tool = {
        "name": "str_replace_editor",
        "type": "text_editor_20250124"
    }

    messages = [
        {
            "role": "user",
            "content": f"""I need help with editing files. Here's what I want to do:

{prompt}

Please use the text editor tool to help me with this. First, think through what you need to do, then use the appropriate tool.
"""
        }
    ]

    loop_count = 0
    tool_use_count = 0
    thinking_start_time = time.time()
    
    while loop_count < max_loops:
        loop_count += 1
        
        console.rule(f"[yellow]Agent Loop {loop_count}/{max_loops}[/yellow]")
        
        # Create message with text editor tool
        message_args = {
            "model": MODEL,
            "max_tokens": 4096,
            "tools": [text_editor_tool],
            "messages": messages,
            "system": system_prompt,
            "thinking": {
                "type": "enabled",
                "budget_tokens": max_thinking_tokens
            }
        }
        
        # Add beta header for token-efficient tools if enabled
        if use_efficient_tools:
            message_args["betas"] = ["token-efficient-tools-2025-02-19"]
            console.print("[cyan]Using token-efficient tools[/cyan]")
        
        response = client.messages.create(**message_args)
        
        # Process response content
        thinking_block = None
        tool_use_block = None
        text_block = None
        
        for content_block in response.content:
            if content_block.type == "thinking":
                thinking_block = content_block
                # Access the thinking attribute which contains the actual thinking text
                if hasattr(thinking_block, 'thinking'):
                    console.print(Panel(
                        thinking_block.thinking,
                        title=f"Claude's Thinking (Loop {loop_count})",
                        border_style="blue"
                    ))
                else:
                    console.print(Panel(
                        "Claude is thinking...",
                        title=f"Claude's Thinking (Loop {loop_count})",
                        border_style="blue"
                    ))
            elif content_block.type == "tool_use":
                tool_use_block = content_block
                tool_use_count += 1
            elif content_block.type == "text":
                text_block = content_block
        
        # If we got a final text response with no tool use, we're done
        if text_block and not tool_use_block:
            thinking_end_time = time.time()
            thinking_duration = thinking_end_time - thinking_start_time
            
            console.print(f"\n[bold green]Completed in {thinking_duration:.2f} seconds after {loop_count} loops and {tool_use_count} tool uses[/bold green]")
            
            # Add the response to messages
            messages.append({
                "role": "assistant",
                "content": [
                    *([thinking_block] if thinking_block else []),
                    {"type": "text", "text": text_block.text}
                ]
            })
            
            return text_block.text
        
        # Handle tool use
        if tool_use_block:
            console.print(f"\n[bold blue]Tool Use #{tool_use_count}:[/bold blue]")
            console.print(f"Command: {tool_use_block.input.get('command')}")
            
            # Add the tool use to messages
            messages.append({
                "role": "assistant",
                "content": [
                    *([thinking_block] if thinking_block else []),
                    tool_use_block
                ]
            })
            
            # Handle the tool use
            tool_result = handle_tool_use(tool_use_block.input)
            
            # Format tool result for Claude
            if "error" in tool_result:
                messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use_block.id,
                            "content": tool_result["error"]
                        }
                    ]
                })
            else:
                messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use_block.id,
                            "content": tool_result["result"]
                        }
                    ]
                })
    
    # If we reach here, we hit the max loops
    console.print(f"\n[bold red]Warning: Reached maximum loops ({max_loops}) without completing the task[/bold red]")
    return "I wasn't able to complete the task within the allowed number of thinking steps. Please try a more specific prompt or increase the loop limit."


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Claude 3.7 File Editor Agent")
    parser.add_argument("--prompt", required=True, help="The prompt for what file operations to perform")
    parser.add_argument("--max-loops", type=int, default=15, help="Maximum number of tool use loops (default: 15)")
    parser.add_argument("--thinking", type=int, default=DEFAULT_THINKING_TOKENS, help=f"Maximum thinking tokens (default: {DEFAULT_THINKING_TOKENS})")
    parser.add_argument("--efficient", action="store_true", help="Enable token-efficient tool use (reduces token usage and latency)")
    args = parser.parse_args()
    
    # Make sure agent_workspace directory exists
    os.makedirs(WORKSPACE_DIR, exist_ok=True)
    
    # Get API key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        console.print("[red]Error: ANTHROPIC_API_KEY environment variable is not set[/red]")
        console.print("Please set it with: export ANTHROPIC_API_KEY='your-api-key-here'")
        sys.exit(1)
    
    # Initialize Anthropic client
    client = Anthropic(api_key=api_key)
    
    console.print(Panel.fit(
        "Claude 3.7 File Editor Agent",
        subtitle="Powered by Anthropic Claude 3.7 Sonnet"
    ))
    
    console.print(f"\n[bold]Prompt:[/bold] {args.prompt}\n")
    console.print(f"[dim]Thinking tokens: {args.thinking}[/dim]")
    console.print(f"[dim]Max loops: {args.max_loops}[/dim]\n")
    
    try:
        # Run the agent
        response = run_agent(
            client, 
            args.prompt, 
            args.thinking, 
            args.max_loops,
            args.efficient
        )
        
        # Print the final response
        console.print(Panel(Markdown(response), title="Claude's Response"))
        
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()