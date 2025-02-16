#!/usr/bin/env python3

# /// script
# dependencies = [
#   "google-genai>=1.1.0",
# ]
# ///

"""
/// Example Usage

# generates and executes DuckDB command (default)
uv run sfa_duckdb_gemini_v1.py --db ./data/analytics.db "Filter employees with salary above 50000 and export to high_salary_employees.csv"

# generates DuckDB command only without executing
uv run sfa_duckdb_gemini_v1.py --db ./data/analytics.db --no-exe "Select name and department from employees table and save to employees.json"

///
"""

import os
import sys
import argparse
import subprocess
from google import genai

DUCKDB_PROMPT = """<purpose>
    You are a world-class expert at crafting precise DuckDB CLI commands for database operations.
    Your goal is to generate accurate, minimal DuckDB commands that exactly match the user's data manipulation needs.
</purpose>

<instructions>
    <instruction>Return ONLY the DuckDB command - no explanations, comments, or extra text.</instruction>
    <instruction>Create the command that satisfies the user query against the duckdb-database-path (e.g., mydb.db).</instruction>
    <instruction>Ensure the command follows DuckDB best practices for efficiency and readability.</instruction>
    <instruction>When the user requests to output results to a file, generate a command that writes to the specified file, or create a filename based on a shortened version of the user request and the input database name.</instruction>
    <instruction>If output is requested in CSV format, use the DuckDB COPY command with WITH (FORMAT CSV, HEADER, DELIMITER ',').</instruction>
    <instruction>If output is requested in JSON format, use the DuckDB COPY command with WITH (FORMAT JSON) to export results as JSON.</instruction>
    <instruction>When filtering or processing data, embed the query inside a COPY command if exporting, or run the query directly if no export is needed.</instruction>
    <instruction>Output your response by itself, do not use backticks or markdown formatting. We're going to run your response as a shell command immediately.</instruction>
    <instruction>If your results involve a table or query result set, default to exporting as a valid CSV or JSON file as requested.</instruction>
    <instruction>If the user request is to export to a file, ensure the file is created in the same directory as the duckdb-database-path unless specified otherwise.</instruction>
</instructions>

<examples>
    <example>
        <duckdb-database-path>
            mydb.db
        </duckdb-database-path>
        <user-request>
            Select the "name" and "age" columns from table employees where age > 30
        </user-request>
        <duckdb-command>
            duckdb mydb.db -c "SELECT name, age FROM employees WHERE age > 30;"
        </duckdb-command>
    </example>
    <example>
        <duckdb-database-path>
            data/order_data.db
        </duckdb-database-path>
        <user-request>
            Filter records in table orders where total > 100 and export to orders_high.csv
        </user-request>
        <duckdb-command>
            duckdb data/order_data.db -c "COPY (SELECT * FROM orders WHERE total > 100) TO 'orders_high.csv' WITH (FORMAT CSV, HEADER, DELIMITER ',');"
        </duckdb-command>
    </example>
    <example>
        <duckdb-database-path>
            analytics.db
        </duckdb-database-path>
        <user-request>
            Convert table customers to JSON and save as customers.json
        </user-request>
        <duckdb-command>
            duckdb analytics.db -c "COPY (SELECT * FROM customers) TO 'customers.json' WITH (FORMAT JSON);"
        </duckdb-command>
    </example>
    <example>
        <duckdb-database-path>
            mydb.db
        </duckdb-database-path>
        <user-request>
            Export the result of a join between employees and departments from mydb.db to employees_departments.csv
        </user-request>
        <duckdb-command>
            duckdb mydb.db -c "COPY (SELECT e.name, d.department FROM employees e JOIN departments d ON e.dept_id = d.id) TO 'employees_departments.csv' WITH (FORMAT CSV, HEADER, DELIMITER ',');"
        </duckdb-command>
    </example>
    <example>
        <duckdb-database-path>
            mydb.db
        </duckdb-database-path>
        <user-request>
            Retrieve all records from table sales in mydb.db where region is 'North'
        </user-request>
        <duckdb-command>
            duckdb mydb.db -c "SELECT * FROM sales WHERE region = 'North';"
        </duckdb-command>
    </example>
</examples>

<duckdb-database-path>
    {{database_path}}
</duckdb-database-path>

<user-request>
    {{user_request}}
</user-request>

Your DuckDB command:"""


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Generate DuckDB CLI command using Gemini API"
    )
    parser.add_argument(
        "prompt",
        help="The DuckDB command request to send to Gemini",
    )
    parser.add_argument(
        "--db",
        required=True,
        help="Path to DuckDB database file",
    )
    parser.add_argument(
        "--no-exe",
        action="store_true",
        help="Generate the DuckDB command without executing it",
    )
    args = parser.parse_args()

    # Configure the API key
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY environment variable is not set")
        print("Please get your API key from https://aistudio.google.com/app/apikey")
        print("Then set it with: export GEMINI_API_KEY='your-api-key-here'")
        sys.exit(1)

    # Initialize client
    client = genai.Client(
        api_key=GEMINI_API_KEY, http_options={"api_version": "v1alpha"}
    )

    try:
        # Replace template variables in the prompt
        prompt = DUCKDB_PROMPT.replace("{{database_path}}", args.db)
        prompt = prompt.replace("{{user_request}}", args.prompt)

        # Generate DuckDB command
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", contents=prompt
        )
        duckdb_command = response.text.strip()
        print("\n🤖 Generated DuckDB command:", duckdb_command)

        # Execute the command unless --no-exe flag is present
        if not args.no_exe:
            print("\n🔍 Executing command...")
            # Execute the command using subprocess
            result = subprocess.run(
                duckdb_command, shell=True, text=True, capture_output=True
            )
            if result.returncode != 0:
                print(
                    f"\n❌ Error executing command (return code: {result.returncode}):",
                    result.stderr,
                )
                sys.exit(1)

            if result.stderr:
                print("❌ Error executing command:", result.stderr)

            if result.stdout:
                print("✅ Command executed successfully:")
                print(result.stdout)

    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
