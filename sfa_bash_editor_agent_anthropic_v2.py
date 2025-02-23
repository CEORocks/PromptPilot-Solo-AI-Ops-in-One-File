#!/usr/bin/env -S uv run --script

# /// script
# dependencies = [
#   "anthropic>=0.45.2",
#   "rich>=13.7.0",
# ]
# ///

"""
Usage:
    uv run sfa_bash_editor_agent_anthropic_v2.py --prompt "Create a new markdown file showcasing what you can do in markdown."
"""

import os
import sys
import argparse
import json
import traceback
from rich.console import Console
from rich.panel import Panel
import anthropic

# Initialize global console
console = Console()

current_bash_env = os.environ.copy()

AGENT_PROMPT = """<purpose>
    You are an expert integration assistant that can both edit files and execute bash commands.
</purpose>

<instructions>
    <instruction>Use the tools provided to accomplish file editing and bash command execution as needed.</instruction>
    <instruction>When you have completed the user's task, call complete_task to finalize the process.</instruction>
    <instruction>Provide reasoning with every tool call.</instruction>
    <instruction>When constructing paths use /repo to start from the root of the repository. We'll replace it with the current working directory.</instruction>
</instructions>

<tools>
    <tool>
        <name>view_file</name>
        <description>View the content of a file</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why you are viewing the file</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>path</name>
                <type>string</type>
                <description>Path of the file to view</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>

    <tool>
        <name>create_file</name>
        <description>Create a new file with given content</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Why the file is being created</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>path</name>
                <type>string</type>
                <description>Path where to create the file</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>file_text</name>
                <type>string</type>
                <description>Content for the new file</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>

    <tool>
        <name>str_replace</name>
        <description>Replace text in a file</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Explain why the replacement is needed</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>path</name>
                <type>string</type>
                <description>File path</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>old_str</name>
                <type>string</type>
                <description>The string to be replaced</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>new_str</name>
                <type>string</type>
                <description>The replacement string</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>

    <tool>
        <name>insert_line</name>
        <description>Insert text at a specific line in a file</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Reason for inserting the text</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>path</name>
                <type>string</type>
                <description>File path</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>insert_line</name>
                <type>integer</type>
                <description>Line number for insertion</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>new_str</name>
                <type>string</type>
                <description>The text to insert</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>

    <tool>
        <name>execute_bash</name>
        <description>Execute a bash command</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Explain why this command should be executed</description>
                <required>true</required>
            </parameter>
            <parameter>
                <name>command</name>
                <type>string</type>
                <description>The bash command to run</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>

    <tool>
        <name>restart_bash</name>
        <description>Restart the bash session with a fresh environment</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Explain why the session is being reset</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>

    <tool>
        <name>complete_task</name>
        <description>Finalize the task and exit the agent loop</description>
        <parameters>
            <parameter>
                <name>reasoning</name>
                <type>string</type>
                <description>Explain why the task is complete</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
</tools>

<user-request>
    {{user_request}}
</user-request>
"""


def tool_view_file(tool_input: dict) -> dict:
    try:
        reasoning = tool_input.get("reasoning")
        path = tool_input.get("path")

        if not path or not path.strip():
            error_message = "Invalid file path provided: path is empty."
            console.log(f"[tool_view_file] Error: {error_message}")
            return {"error": error_message}

        console.log(f"[tool_view_file] reasoning: {reasoning}, path: {path}")

        if not os.path.exists(path):
            error_message = f"File {path} does not exist"
            console.log(f"[tool_view_file] Error: {error_message}")
            return {"error": error_message}

        with open(path, "r") as f:
            content = f.read()
        return {"result": content}
    except Exception as e:
        console.log(f"[tool_view_file] Error: {str(e)}")
        console.log(traceback.format_exc())
        return {"error": str(e)}


def tool_create_file(tool_input: dict) -> dict:
    try:
        reasoning = tool_input.get("reasoning")
        path = tool_input.get("path")
        file_text = tool_input.get("file_text")
        console.log(f"[tool_create_file] reasoning: {reasoning}, path: {path}")

        # Check for an empty or invalid path
        if not path or not path.strip():
            error_message = "Invalid file path provided: path is empty."
            console.log(f"[tool_create_file] Error: {error_message}")
            return {"error": error_message}

        dirname = os.path.dirname(path)
        if not dirname:
            error_message = (
                "Invalid file path provided: directory part of the path is empty."
            )
            console.log(f"[tool_create_file] Error: {error_message}")
            return {"error": error_message}
        else:
            os.makedirs(dirname, exist_ok=True)

        with open(path, "w") as f:
            f.write(file_text)
        return {"result": f"File created at {path}"}
    except Exception as e:
        console.log(f"[tool_create_file] Error: {str(e)}")
        console.log(traceback.format_exc())
        return {"error": str(e)}


def tool_str_replace(tool_input: dict) -> dict:
    try:
        reasoning = tool_input.get("reasoning")
        path = tool_input.get("path")
        old_str = tool_input.get("old_str")
        new_str = tool_input.get("new_str")

        if not path or not path.strip():
            error_message = "Invalid file path provided: path is empty."
            console.log(f"[tool_str_replace] Error: {error_message}")
            return {"error": error_message}

        if not old_str:
            error_message = "No text to replace specified: old_str is empty."
            console.log(f"[tool_str_replace] Error: {error_message}")
            return {"error": error_message}

        console.log(
            f"[tool_str_replace] reasoning: {reasoning}, path: {path}, old_str: {old_str}, new_str: {new_str}"
        )

        if not os.path.exists(path):
            error_message = f"File {path} does not exist"
            console.log(f"[tool_str_replace] Error: {error_message}")
            return {"error": error_message}

        with open(path, "r") as f:
            content = f.read()

        if old_str not in content:
            error_message = f"'{old_str}' not found in {path}"
            console.log(f"[tool_str_replace] Error: {error_message}")
            return {"error": error_message}

        new_content = content.replace(old_str, new_str)
        with open(path, "w") as f:
            f.write(new_content)
        return {"result": "Text replaced successfully"}
    except Exception as e:
        console.log(f"[tool_str_replace] Error: {str(e)}")
        console.log(traceback.format_exc())
        return {"error": str(e)}


def tool_insert_line(tool_input: dict) -> dict:
    try:
        reasoning = tool_input.get("reasoning")
        path = tool_input.get("path")
        insert_line_num = tool_input.get("insert_line")
        new_str = tool_input.get("new_str")

        if not path or not path.strip():
            error_message = "Invalid file path provided: path is empty."
            console.log(f"[tool_insert_line] Error: {error_message}")
            return {"error": error_message}

        if insert_line_num is None:
            error_message = "No line number specified: insert_line is missing."
            console.log(f"[tool_insert_line] Error: {error_message}")
            return {"error": error_message}

        if not new_str:
            error_message = "No text to insert specified: new_str is empty."
            console.log(f"[tool_insert_line] Error: {error_message}")
            return {"error": error_message}

        console.log(
            f"[tool_insert_line] reasoning: {reasoning}, path: {path}, insert_line: {insert_line_num}, new_str: {new_str}"
        )

        if not os.path.exists(path):
            error_message = f"File {path} does not exist"
            console.log(f"[tool_insert_line] Error: {error_message}")
            return {"error": error_message}

        with open(path, "r") as f:
            lines = f.readlines()

        # Check that the index is within acceptable bounds (allowing insertion at end)
        if insert_line_num < 0 or insert_line_num > len(lines):
            error_message = (
                f"Insert line number {insert_line_num} out of range (0-{len(lines)})."
            )
            console.log(f"[tool_insert_line] Error: {error_message}")
            return {"error": error_message}

        lines.insert(insert_line_num, new_str + "\n")
        with open(path, "w") as f:
            f.writelines(lines)
        return {"result": "Line inserted successfully"}
    except Exception as e:
        console.log(f"[tool_insert_line] Error: {str(e)}")
        console.log(traceback.format_exc())
        return {"error": str(e)}


def tool_execute_bash(tool_input: dict) -> dict:
    try:
        reasoning = tool_input.get("reasoning")
        command = tool_input.get("command")

        if not command or not command.strip():
            error_message = "No command specified: command is empty."
            console.log(f"[tool_execute_bash] Error: {error_message}")
            return {"error": error_message}

        console.log(f"[tool_execute_bash] reasoning: {reasoning}, command: {command}")
        import subprocess

        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, env=current_bash_env
        )
        if result.returncode != 0:
            error_message = (
                result.stderr.strip()
                or "Command execution failed with non-zero exit code."
            )
            console.log(f"[tool_execute_bash] Error: {error_message}")
            return {"error": error_message}
        return {"result": result.stdout.strip()}
    except Exception as e:
        console.log(f"[tool_execute_bash] Error: {str(e)}")
        console.log(traceback.format_exc())
        return {"error": str(e)}


def tool_restart_bash(tool_input: dict) -> dict:
    global current_bash_env
    try:
        reasoning = tool_input.get("reasoning")

        if not reasoning:
            error_message = "No reasoning provided for restarting bash session."
            console.log(f"[tool_restart_bash] Error: {error_message}")
            return {"error": error_message}

        console.log(f"[tool_restart_bash] reasoning: {reasoning}")
        current_bash_env = os.environ.copy()
        return {"result": "Bash session restarted."}
    except Exception as e:
        console.log(f"[tool_restart_bash] Error: {str(e)}")
        console.log(traceback.format_exc())
        return {"error": str(e)}


def tool_complete_task(tool_input: dict) -> dict:
    try:
        reasoning = tool_input.get("reasoning")

        if not reasoning:
            error_message = "No reasoning provided for task completion."
            console.log(f"[tool_complete_task] Error: {error_message}")
            return {"error": error_message}

        console.log(f"[tool_complete_task] reasoning: {reasoning}")
        return {"result": "Task completed"}
    except Exception as e:
        console.log(f"[tool_complete_task] Error: {str(e)}")
        console.log(traceback.format_exc())
        return {"error": str(e)}


def main():
    parser = argparse.ArgumentParser(
        description="Bash and Editor Agent using Anthropic API"
    )
    parser.add_argument("-p", "--prompt", required=True, help="The prompt to execute")
    parser.add_argument(
        "-c", "--compute", type=int, default=10, help="Maximum compute loops"
    )
    args = parser.parse_args()

    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    if not ANTHROPIC_API_KEY:
        Console().print(
            "[red]Error: ANTHROPIC_API_KEY environment variable is not set.[/red]"
        )
        sys.exit(1)

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    # Prepare the initial message using the detailed prompt
    initial_message = AGENT_PROMPT.replace("{{user_request}}", args.prompt)
    messages = [{"role": "user", "content": initial_message}]

    compute_iterations = 0

    # Begin the agent loop.
    # This loop processes Anthropic API responses, executes tool calls for both editor and bash commands,
    # and logs detailed information via rich logging.
    while compute_iterations < args.compute:
        compute_iterations += 1
        console.rule(f"[yellow]Agent Loop {compute_iterations}/{args.compute}[/yellow]")
        try:
            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=messages,
                tools=[
                    {
                        "name": "view_file",
                        "description": "View the content of a file",
                        "input_schema": {
                            "type": "object",
                            "properties": {
                                "reasoning": {
                                    "type": "string",
                                    "description": "Why view the file",
                                },
                                "path": {"type": "string", "description": "File path"},
                            },
                            "required": ["reasoning", "path"],
                        },
                    },
                    {
                        "name": "create_file",
                        "description": "Create a new file with given content",
                        "input_schema": {
                            "type": "object",
                            "properties": {
                                "reasoning": {
                                    "type": "string",
                                    "description": "Why create the file",
                                },
                                "path": {"type": "string", "description": "File path"},
                                "file_text": {
                                    "type": "string",
                                    "description": "Content for the file",
                                },
                            },
                            "required": ["reasoning", "path", "file_text"],
                        },
                    },
                    {
                        "name": "str_replace",
                        "description": "Replace text in a file",
                        "input_schema": {
                            "type": "object",
                            "properties": {
                                "reasoning": {
                                    "type": "string",
                                    "description": "Reason for replacement",
                                },
                                "path": {"type": "string", "description": "File path"},
                                "old_str": {
                                    "type": "string",
                                    "description": "Text to replace",
                                },
                                "new_str": {
                                    "type": "string",
                                    "description": "Replacement text",
                                },
                            },
                            "required": ["reasoning", "path", "old_str", "new_str"],
                        },
                    },
                    {
                        "name": "insert_line",
                        "description": "Insert text at a specific line in a file",
                        "input_schema": {
                            "type": "object",
                            "properties": {
                                "reasoning": {
                                    "type": "string",
                                    "description": "Reason for insertion",
                                },
                                "path": {"type": "string", "description": "File path"},
                                "insert_line": {
                                    "type": "integer",
                                    "description": "Line number",
                                },
                                "new_str": {
                                    "type": "string",
                                    "description": "Text to insert",
                                },
                            },
                            "required": ["reasoning", "path", "insert_line", "new_str"],
                        },
                    },
                    {
                        "name": "execute_bash",
                        "description": "Execute a bash command",
                        "input_schema": {
                            "type": "object",
                            "properties": {
                                "reasoning": {
                                    "type": "string",
                                    "description": "Reason for command execution",
                                },
                                "command": {
                                    "type": "string",
                                    "description": "Bash command",
                                },
                            },
                            "required": ["reasoning", "command"],
                        },
                    },
                    {
                        "name": "restart_bash",
                        "description": "Restart the bash session with fresh environment",
                        "input_schema": {
                            "type": "object",
                            "properties": {
                                "reasoning": {
                                    "type": "string",
                                    "description": "Why to restart bash",
                                }
                            },
                            "required": ["reasoning"],
                        },
                    },
                    {
                        "name": "complete_task",
                        "description": "Complete the task and exit the agent loop",
                        "input_schema": {
                            "type": "object",
                            "properties": {
                                "reasoning": {
                                    "type": "string",
                                    "description": "Why the task is complete",
                                }
                            },
                            "required": ["reasoning"],
                        },
                    },
                ],
                tool_choice={"type": "any"},
            )
        except Exception as e:
            console.print(f"[red]Error in API call: {str(e)}[/red]")
            console.print(traceback.format_exc())
            break

        console.log("[green]API Response:[/green]", response.model_dump())
        messages.append({"role": "assistant", "content": response.content})

        tool_calls = [
            block
            for block in response.content
            if hasattr(block, "type") and block.type == "tool_use"
        ]
        if tool_calls:
            # Map tool names to their corresponding functions
            tool_functions = {
                "view_file": tool_view_file,
                "create_file": tool_create_file,
                "str_replace": tool_str_replace,
                "insert_line": tool_insert_line,
                "execute_bash": tool_execute_bash,
                "restart_bash": tool_restart_bash,
                "complete_task": tool_complete_task,
            }
            for tool in tool_calls:
                console.print(
                    f"[blue]Tool Call:[/blue] {tool.name} with input {tool.input}"
                )
                func = tool_functions.get(tool.name)
                if func:
                    output = func(tool.input)
                    is_error = "error" in output
                    result_text = output.get("error") or output.get("result", "")
                    console.print(f"[green]Tool Result:[/green] {result_text}")
                    messages.append(
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "tool_result",
                                    "tool_use_id": tool.id,
                                    "content": result_text,
                                    "is_error": is_error,
                                }
                            ],
                        }
                    )
                    if tool.name == "complete_task":
                        console.print(
                            "[green]Task completed. Exiting agent loop.[/green]"
                        )
                        return
                else:
                    console.print(f"[red]Unknown tool: {tool.name}[/red]")

    console.print("[yellow]Reached compute limit without completing task.[/yellow]")


if __name__ == "__main__":
    main()
