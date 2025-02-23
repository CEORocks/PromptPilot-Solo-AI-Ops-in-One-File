# /// script
# dependencies = [
#   "openai>=1.63.0",
#   "rich>=13.7.0",
#   "pydantic>=2.0.0",
#   "firecrawl-py>=0.1.0",
#   "python-dotenv>=1.0.0",
# ]
# ///

import os
import sys
import json
import argparse
from typing import List
from rich.console import Console
from rich.panel import Panel
import openai
from pydantic import BaseModel, Field
from openai import pydantic_function_tool
from firecrawl import FirecrawlApp
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize rich console
console = Console()

# Initialize Firecrawl
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")
if not FIRECRAWL_API_KEY:
    console.print(
        "[red]Error: FIRECRAWL_API_KEY not found in environment variables[/red]"
    )
    sys.exit(1)

firecrawl_app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

# Initialize OpenAI client
client = openai.OpenAI()


# Create our list of function tools from our pydantic models
class ScrapeUrlArgs(BaseModel):
    reasoning: str = Field(
        ..., description="Explanation for why we're scraping this URL"
    )
    url: str = Field(..., description="The URL to scrape")
    output_file_path: str = Field(..., description="Path to save the scraped content")


class ReadLocalFileArgs(BaseModel):
    reasoning: str = Field(
        ..., description="Explanation for why we're reading this file"
    )
    file_path: str = Field(..., description="Path of the file to read")


class UpdateLocalFileArgs(BaseModel):
    reasoning: str = Field(
        ..., description="Explanation for why we're updating this file"
    )
    file_path: str = Field(..., description="Path of the file to update")
    content: str = Field(..., description="New content to write to the file")


class CompleteTaskArgs(BaseModel):
    reasoning: str = Field(..., description="Explanation of why the task is complete")


# Create tools list
tools = [
    pydantic_function_tool(ScrapeUrlArgs),
    pydantic_function_tool(ReadLocalFileArgs),
    pydantic_function_tool(UpdateLocalFileArgs),
    pydantic_function_tool(CompleteTaskArgs),
]

AGENT_PROMPT = """<purpose>
    You are a world-class web scraping and content filtering expert.
    Your goal is to scrape web content and filter it according to the user's needs.
</purpose>

<instructions>
    <instruction>Run scrap_url, then read_local_file, then update_local_file as many times as needed to satisfy the user's prompt, then complete_task when the user's prompt is fully satisfied.</instruction>
    <instruction>For each step, use exactly one tool call and wait for its response before proceeding.</instruction>
    <instruction>When processing content, extract exactly what the user asked for - no more, no less.</instruction>
    <instruction>When saving processed content, use proper markdown formatting.</instruction>
    <instruction>Use tools available in 'tools' section.</instruction>
</instructions>

<tools>
    <tool>
        <n>scrape_url</n>
        <description>Scrapes content from a URL and saves it to a file</description>
        <parameters>
            <parameter>
                <n>reasoning</n>
                <type>string</type>
                <description>Why we need to scrape this URL</description>
                <required>true</required>
            </parameter>
            <parameter>
                <n>url</n>
                <type>string</type>
                <description>The URL to scrape</description>
                <required>true</required>
            </parameter>
            <parameter>
                <n>output_file_path</n>
                <type>string</type>
                <description>Where to save the scraped content</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <n>read_local_file</n>
        <description>Reads content from a local file</description>
        <parameters>
            <parameter>
                <n>reasoning</n>
                <type>string</type>
                <description>Why we need to read this file</description>
                <required>true</required>
            </parameter>
            <parameter>
                <n>file_path</n>
                <type>string</type>
                <description>Path of file to read</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <n>update_local_file</n>
        <description>Updates content in a local file</description>
        <parameters>
            <parameter>
                <n>reasoning</n>
                <type>string</type>
                <description>Why we need to update this file</description>
                <required>true</required>
            </parameter>
            <parameter>
                <n>file_path</n>
                <type>string</type>
                <description>Path of file to update</description>
                <required>true</required>
            </parameter>
            <parameter>
                <n>content</n>
                <type>string</type>
                <description>New content to write to the file</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
    
    <tool>
        <n>complete_task</n>
        <description>Signals that the task is complete</description>
        <parameters>
            <parameter>
                <n>reasoning</n>
                <type>string</type>
                <description>Why the task is now complete</description>
                <required>true</required>
            </parameter>
        </parameters>
    </tool>
</tools>

<user-prompt>
    {{user_prompt}}
</user-prompt>

<url>
    {{url}}
</url>

<output-file-path>
    {{output_file_path}}
</output-file-path>
"""


def log_function_call(function_name: str, function_args: dict):
    """Log a function call in a rich panel."""
    args_str = ", ".join(f"{k}={repr(v)}" for k, v in function_args.items())
    console.print(
        Panel(
            f"{function_name}({args_str})",
            title="[blue]Function Call[/blue]",
            border_style="blue",
        )
    )


def log_function_result(function_name: str, result: str):
    """Log a function result in a rich panel."""
    console.print(
        Panel(
            str(result),
            title=f"[green]{function_name} Result[/green]",
            border_style="green",
        )
    )


def log_error(error_msg: str):
    """Log an error in a rich panel."""
    console.print(Panel(str(error_msg), title="[red]Error[/red]", border_style="red"))


def log_workflow_step(step: int, message: str):
    """Log a workflow step in a rich panel."""
    console.print(
        Panel(message, title=f"[yellow]Step {step}[/yellow]", border_style="yellow")
    )


def scrape_url(reasoning: str, url: str, output_file_path: str) -> str:
    """Scrapes content from a URL and saves it to a file."""
    log_function_call(
        "scrape_url",
        {"reasoning": reasoning, "url": url, "output_file_path": output_file_path},
    )

    try:
        response = firecrawl_app.scrape_url(
            url=url,
            params={
                "formats": ["markdown"],
            },
        )

        if response.get("success"):
            content = response["data"]["markdown"]
            with open(output_file_path, "w") as f:
                f.write(content)
            log_function_result(
                "scrape_url", f"Successfully scraped {len(content)} characters"
            )
            return content
        else:
            error = response.get("error", "Unknown error")
            log_error(f"Error scraping URL: {error}")
            return ""
    except Exception as e:
        log_error(f"Error scraping URL: {str(e)}")
        return ""


def read_local_file(reasoning: str, file_path: str) -> str:
    """Reads content from a local file.

    Args:
        reasoning: Explanation for why we're reading this file
        file_path: Path of the file to read

    Returns:
        String containing the file contents
    """
    log_function_call(
        "read_local_file", {"reasoning": reasoning, "file_path": file_path}
    )

    try:
        console.log(
            f"[blue]Reading File[/blue] - File: {file_path} - Reasoning: {reasoning}"
        )
        with open(file_path, "r") as f:
            return f.read()
    except Exception as e:
        console.log(f"[red]Error reading file: {str(e)}[/red]")
        return ""


def update_local_file(reasoning: str, file_path: str, content: str) -> str:
    """Updates content in a local file.

    Args:
        reasoning: Explanation for why we're updating this file
        file_path: Path of the file to update
        content: New content to write to the file

    Returns:
        String indicating success or failure
    """
    log_function_call(
        "update_local_file",
        {
            "reasoning": reasoning,
            "file_path": file_path,
            "content": f"{len(content)} characters",  # Don't log full content
        },
    )

    try:
        console.log(
            f"[blue]Updating File[/blue] - File: {file_path} - Reasoning: {reasoning}"
        )
        with open(file_path, "w") as f:
            f.write(content)
        log_function_result(
            "update_local_file", f"Successfully wrote {len(content)} characters"
        )
        return "File updated successfully"
    except Exception as e:
        console.log(f"[red]Error updating file: {str(e)}[/red]")
        return f"Error: {str(e)}"


def complete_task(reasoning: str) -> str:
    """Signals that the task is complete.

    Args:
        reasoning: Explanation of why the task is complete

    Returns:
        String confirmation message
    """
    log_function_call("complete_task", {"reasoning": reasoning})
    console.log(f"[green]Task Complete[/green] - Reasoning: {reasoning}")
    result = "Task completed successfully"
    log_function_result("complete_task", result)
    return result


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Web scraper agent that filters content based on user query"
    )
    parser.add_argument("--url", "-u", required=True, help="The URL to scrape")
    parser.add_argument(
        "--output-file-path",
        "-o",
        default="scraped_content.md",
        help="Path to save the scraped content",
    )
    parser.add_argument(
        "--prompt", "-p", required=True, help="The prompt to filter the content with"
    )
    parser.add_argument(
        "--compute-limit",
        "-c",
        type=int,
        default=20,  # Increased default compute limit
        help="Maximum number of tokens to use for response",
    )

    args = parser.parse_args()

    # Create a temporary file for the raw scraped content
    temp_file = "temp_scraped_content.md"

    # Format the prompt with the user's arguments
    formatted_prompt = (
        AGENT_PROMPT.replace("{{user_prompt}}", args.prompt)
        .replace("{{url}}", args.url)
        .replace("{{output_file_path}}", args.output_file_path)
    )

    # Track workflow state
    workflow_state = {
        "step": 1,
        "temp_file": temp_file,
        "output_file": args.output_file_path,
        "url": args.url,
        "prompt": args.prompt,
        "scraped_content": None,  # Store scraped content
        "processed_content": None,  # Store processed content
    }

    # Initialize conversation with system prompt and workflow start
    messages = [
        {"role": "system", "content": formatted_prompt},
        {
            "role": "user",
            "content": f"Start with step 1: Use the scrape_url tool to scrape {args.url} and save it to {temp_file}. You MUST use the scrape_url tool for this step.",
        },
    ]

    # Track number of iterations
    iterations = 0
    max_iterations = args.compute_limit

    while iterations < max_iterations:
        try:
            current_step = workflow_state["step"]
            log_workflow_step(
                current_step,
                f"Processing step {current_step}: "
                + {
                    1: "Scraping URL",
                    2: "Reading scraped content",
                    3: "Processing content",
                    4: "Saving results",
                    5: "Completing task",
                }.get(current_step, "Unknown step"),
            )

            # Get completion from OpenAI
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                tools=tools,
                tool_choice="auto",
            )

            response_message = completion.choices[0].message

            # Print the assistant's response
            if response_message.content:
                console.print(Panel(response_message.content, title="Assistant"))

            # Handle tool calls
            if response_message.tool_calls:
                # Add assistant's message to conversation
                messages.append(
                    {
                        "role": "assistant",
                        "content": response_message.content,
                        "tool_calls": [
                            {
                                "id": tool_call.id,
                                "type": tool_call.type,
                                "function": {
                                    "name": tool_call.function.name,
                                    "arguments": tool_call.function.arguments,
                                },
                            }
                            for tool_call in response_message.tool_calls
                        ],
                    }
                )

                # Process each tool call
                for tool_call in response_message.tool_calls:
                    function_name = tool_call.function.name
                    function_args = json.loads(tool_call.function.arguments)

                    console.print(
                        Panel(
                            f"Processing tool call: {function_name}({function_args})",
                            title="[yellow]Tool Call[/yellow]",
                            border_style="yellow",
                        )
                    )

                    # Execute the appropriate function and store result
                    result = None
                    try:
                        if function_name == "scrape_url":
                            if current_step != 1:
                                log_error(
                                    f"Invalid step for scrape_url: expected step 1, got step {current_step}"
                                )
                                continue
                            result = scrape_url(**function_args)
                            if result:  # If scraping succeeded
                                workflow_state["scraped_content"] = result
                                workflow_state["step"] = 2
                                messages.append(
                                    {
                                        "role": "user",
                                        "content": f"Good. Now proceed with step 2: Use the read_local_file tool to read the content from {temp_file}. You MUST use the read_local_file tool for this step.",
                                    }
                                )
                            else:
                                log_error("Scraping failed - no content returned")
                                return

                        elif function_name == "read_local_file":
                            if current_step != 2:
                                log_error(
                                    f"Invalid step for read_local_file: expected step 2, got step {current_step}"
                                )
                                continue
                            result = read_local_file(**function_args)
                            if result:  # If reading succeeded
                                workflow_state["step"] = 3
                                messages.append(
                                    {
                                        "role": "user",
                                        "content": "Good. Now proceed with step 3: Process the content to extract lesson names and descriptions, and use the update_local_file tool to save them in a markdown table format. You MUST use the update_local_file tool for this step.",
                                    }
                                )
                            else:
                                log_error("Reading failed - no content returned")
                                return

                        elif function_name == "update_local_file":
                            if current_step != 3:
                                log_error(
                                    f"Invalid step for update_local_file: expected step 3, got step {current_step}"
                                )
                                continue
                            result = update_local_file(**function_args)
                            if (
                                result and "success" in result.lower()
                            ):  # If update succeeded
                                workflow_state["processed_content"] = function_args.get(
                                    "content"
                                )
                                workflow_state["step"] = 4
                                messages.append(
                                    {
                                        "role": "user",
                                        "content": "Good. Now proceed with step 4: Use the complete_task tool to signal completion. You MUST use the complete_task tool for this step.",
                                    }
                                )
                            else:
                                log_error("Update failed")
                                return

                        elif function_name == "complete_task":
                            if current_step != 4:
                                log_error(
                                    f"Invalid step for complete_task: expected step 4, got step {current_step}"
                                )
                                continue
                            result = complete_task(**function_args)
                            # Clean up temp file
                            try:
                                if os.path.exists(temp_file):
                                    os.remove(temp_file)
                            except:
                                pass
                            return

                    except Exception as e:
                        error_msg = f"Error executing {function_name}: {str(e)}"
                        log_error(error_msg)
                        return  # Exit on error

                    # Add the tool response to messages
                    messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "name": function_name,
                            "content": str(result),
                        }
                    )

            else:
                # No tool calls, just add the response to messages
                messages.append(
                    {"role": "assistant", "content": response_message.content}
                )
                # Remind the agent of the current step with explicit tool requirement
                step_messages = {
                    1: f"You MUST use the scrape_url tool to scrape {args.url} and save it to {temp_file}.",
                    2: f"You MUST use the read_local_file tool to read the content from {temp_file}.",
                    3: "You MUST use the update_local_file tool to save the processed content in markdown table format.",
                    4: "You MUST use the complete_task tool to signal completion.",
                }
                messages.append(
                    {
                        "role": "user",
                        "content": f"Please proceed with step {current_step}: {step_messages.get(current_step, 'Unknown step')}",
                    }
                )

            iterations += 1

        except Exception as e:
            log_error(f"Error: {str(e)}")
            console.print("[yellow]Messages at error:[/yellow]")
            for msg in messages:
                console.print(msg)
            # Clean up temp file
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            except:
                pass
            break

    if iterations >= max_iterations:
        log_error("Reached maximum number of iterations")
        # Clean up temp file
        try:
            if os.path.exists(temp_file):
                os.remove(temp_file)
        except:
            pass


if __name__ == "__main__":
    main()
