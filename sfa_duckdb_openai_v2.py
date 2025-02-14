#!/usr/bin/env python3

# /// script
# dependencies = [
#   "openai>=1.1.0",
#   "rich>=13.7.0",
#   "pydantic>=2.0.0",
# ]
# ///

"""
/// Example Usage

# Run DuckDB agent with default compute loops (3)
uv run sfa_duckdb_openai_v2.py -d ./data/mock.db -p "Show me all users with score above 80"

# Run with custom compute loops
uv run sfa_duckdb_openai_v2.py -d ./data/mock.db -p "Show me all users with score above 80" -c 5

///
"""

import os
import sys
import json
import argparse
import subprocess
from typing import List
from rich.console import Console
from rich.panel import Panel
import openai
from pydantic import BaseModel, ValidationError

# Initialize rich console
console = Console()

# Define Pydantic schemas for tool arguments
class ListTablesArgs(BaseModel):
    reasoning: str

class DescribeTableArgs(BaseModel):
    reasoning: str
    table_name: str

class SampleTableArgs(BaseModel):
    reasoning: str
    table_name: str
    row_sample_size: int

class SQLQueryArgs(BaseModel):
    reasoning: str
    sql_query: str

def list_tables(reasoning: str) -> List[str]:
    """Returns a list of tables in the database.

    The agent uses this to discover available tables and make informed decisions.

    Args:
        reasoning: Explanation of why we're listing tables relative to user request

    Returns:
        List of table names as strings
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c ".tables"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(f"[blue]List Tables Tool[/blue] - Reasoning: {reasoning}")
        return result.stdout.strip().split("\n")
    except Exception as e:
        console.log(f"[red]Error listing tables: {str(e)}[/red]")
        return []

def describe_table(reasoning: str, table_name: str) -> str:
    """Returns schema information about the specified table.

    The agent uses this to understand table structure and available columns.

    Args:
        reasoning: Explanation of why we're describing this table
        table_name: Name of table to describe

    Returns:
        String containing table schema information
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "DESCRIBE {table_name};"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(
            f"[blue]Describe Table Tool[/blue] - Table: {table_name} - Reasoning: {reasoning}"
        )
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error describing table: {str(e)}[/red]")
        return ""

def sample_table(reasoning: str, table_name: str, row_sample_size: int) -> str:
    """Returns a sample of rows from the specified table.

    The agent uses this to understand actual data content and patterns.

    Args:
        reasoning: Explanation of why we're sampling this table
        table_name: Name of table to sample from
        row_sample_size: Number of rows to sample aim for 3-5 rows

    Returns:
        String containing sample rows in readable format
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "SELECT * FROM {table_name} LIMIT {row_sample_size};"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(
            f"[blue]Sample Table Tool[/blue] - Table: {table_name} - Rows: {row_sample_size} - Reasoning: {reasoning}"
        )
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error sampling table: {str(e)}[/red]")
        return ""

def run_test_sql_query(reasoning: str, sql_query: str) -> str:
    """Executes a test SQL query and returns results.

    The agent uses this to validate queries before finalizing them.
    Results are only shown to the agent, not the user.

    Args:
        reasoning: Explanation of why we're running this test query
        sql_query: The SQL query to test

    Returns:
        Query results as a string
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "{sql_query}"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(f"[blue]Test Query Tool[/blue] - Reasoning: {reasoning}")
        console.log(f"[dim]Query: {sql_query}[/dim]")
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error running test query: {str(e)}[/red]")
        return str(e)

def run_final_sql_query(reasoning: str, sql_query: str) -> str:
    """Executes the final SQL query and returns results to user.

    This is the last tool call the agent should make after validating the query.

    Args:
        reasoning: Final explanation of how this query satisfies user request
        sql_query: The validated SQL query to run

    Returns:
        Query results as a string
    """
    try:
        result = subprocess.run(
            f'duckdb {DB_PATH} -c "{sql_query}"',
            shell=True,
            text=True,
            capture_output=True,
        )
        console.log(
            Panel(
                f"[green]Final Query Tool[/green]\nReasoning: {reasoning}\nQuery: {sql_query}"
            )
        )
        return result.stdout
    except Exception as e:
        console.log(f"[red]Error running final query: {str(e)}[/red]")
        return str(e)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="DuckDB Agent using OpenAI API")
    parser.add_argument(
        "-d", "--db", required=True, help="Path to DuckDB database file"
    )
    parser.add_argument("-p", "--prompt", required=True, help="The user's request")
    parser.add_argument(
        "-c",
        "--compute",
        type=int,
        default=10,
        help="Maximum number of agent loops (default: 3)",
    )
    args = parser.parse_args()

    # Configure the API key
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        console.print(
            "[red]Error: OPENAI_API_KEY environment variable is not set[/red]"
        )
        console.print(
            "Please get your API key from https://platform.openai.com/api-keys"
        )
        console.print("Then set it with: export OPENAI_API_KEY='your-api-key-here'")
        sys.exit(1)
    
    openai.api_key = OPENAI_API_KEY

    # Set global DB_PATH for tool functions
    global DB_PATH
    DB_PATH = args.db

    # Initialize message history
    messages = [
        {
            "role": "system",
            "content": "You are a world-class expert at crafting precise DuckDB SQL queries. "
            "Your goal is to generate accurate queries that exactly match the user's data needs. "
            "Start by listing tables to understand what's available. "
            "Then describe tables to understand their schema and columns. "
            "Sample tables to see actual data patterns. "
            "Test queries before finalizing them. "
            "Only call run_final_sql_query when you're confident the query is perfect. "
            "Be thorough but efficient with tool usage. "
            "Think step by step about what information you need."
        }
    ]

    compute_iterations = 0

    # Main agent loop
    while True:
        console.rule(
            f"[yellow]Agent Loop {compute_iterations+1}/{args.compute}[/yellow]"
        )
        compute_iterations += 1

        if compute_iterations >= args.compute:
            console.print(
                "[yellow]Warning: Reached maximum compute loops without final query[/yellow]"
            )
            raise Exception(
                f"Maximum compute loops reached: {compute_iterations}/{args.compute}"
            )

        try:
            # Add the user's initial prompt if this is the first iteration
            if compute_iterations == 1:
                messages.append({"role": "user", "content": args.prompt})

            # Generate content with tool support
            response = openai.ChatCompletion.create(
                model="o3-mini",
                max_tokens=1024,
                messages=messages,
                functions=[
                    {
                        "name": "list_tables",
                        "description": "Returns list of available tables in database",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "reasoning": {"type": "string", "description": "Explanation for listing tables"}
                            },
                            "required": ["reasoning"]
                        }
                    },
                    {
                        "name": "describe_table",
                        "description": "Returns schema info for a table",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "reasoning": {"type": "string"},
                                "table_name": {"type": "string"}
                            },
                            "required": ["reasoning", "table_name"]
                        }
                    },
                    {
                        "name": "sample_table",
                        "description": "Returns sample rows of a table",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "reasoning": {"type": "string"},
                                "table_name": {"type": "string"},
                                "row_sample_size": {"type": "integer"}
                            },
                            "required": ["reasoning", "table_name", "row_sample_size"]
                        }
                    },
                    {
                        "name": "run_test_sql_query",
                        "description": "Runs a test SQL query and returns results",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "reasoning": {"type": "string"},
                                "sql_query": {"type": "string"}
                            },
                            "required": ["reasoning", "sql_query"]
                        }
                    },
                    {
                        "name": "run_final_sql_query",
                        "description": "Runs final validated SQL query and returns results",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "reasoning": {"type": "string"},
                                "sql_query": {"type": "string"}
                            },
                            "required": ["reasoning", "sql_query"]
                        }
                    },
                ],
                function_call={"name": "any"},  # always force a tool call
                temperature=0.0
            )

            if 'choices' in response and response.choices:
                message = response.choices[0].message
                if message.get("function_call"):
                    func_call = message["function_call"]
                    func_name = func_call.get("name")
                    func_args_str = func_call.get("arguments")
                    console.print(f"[blue]Function Call:[/blue] {func_name}({func_args_str})")
                    try:
                        # Validate and parse arguments using the corresponding pydantic model
                        if func_name == "list_tables":
                            args_parsed = ListTablesArgs.parse_raw(func_args_str)
                            result = list_tables(reasoning=args_parsed.reasoning)
                        elif func_name == "describe_table":
                            args_parsed = DescribeTableArgs.parse_raw(func_args_str)
                            result = describe_table(reasoning=args_parsed.reasoning, table_name=args_parsed.table_name)
                        elif func_name == "sample_table":
                            args_parsed = SampleTableArgs.parse_raw(func_args_str)
                            result = sample_table(reasoning=args_parsed.reasoning, table_name=args_parsed.table_name, row_sample_size=args_parsed.row_sample_size)
                        elif func_name == "run_test_sql_query":
                            args_parsed = SQLQueryArgs.parse_raw(func_args_str)
                            result = run_test_sql_query(reasoning=args_parsed.reasoning, sql_query=args_parsed.sql_query)
                        elif func_name == "run_final_sql_query":
                            args_parsed = SQLQueryArgs.parse_raw(func_args_str)
                            result = run_final_sql_query(reasoning=args_parsed.reasoning, sql_query=args_parsed.sql_query)
                            console.print("\n[green]Final Results:[/green]")
                            console.print(result)
                            return
                        else:
                            raise Exception(f"Unknown tool call: {func_name}")

                        console.print(f"[blue]Function Call Result:[/blue] {func_name}(...) -> {result}")

                        # Append the function call result into our messages as a tool response
                        messages.append({
                            "role": "tool",
                            "content": json.dumps({"result": str(result)}),
                            "name": func_name
                        })

                        # Also append the original assistant message so that context is maintained
                        messages.append(message)

                    except ValidationError as ve:
                        error_msg = f"Argument validation failed for {func_name}: {ve}"
                        console.print(f"[red]{error_msg}[/red]")
                        messages.append({
                            "role": "tool",
                            "content": json.dumps({"error": error_msg}),
                            "name": func_name
                        })
                else:
                    # No function call in this response; simply append the message as is
                    messages.append(message)

        except Exception as e:
            console.print(f"[red]Error in agent loop: {str(e)}[/red]")
            raise e

if __name__ == "__main__":
    main()
