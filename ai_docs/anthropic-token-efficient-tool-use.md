# Token-Efficient Tool Use

The upgraded Claude 3.7 Sonnet model is capable of calling tools in a token-efficient manner. Requests save an average of 14% in output tokens, up to 70%, which also reduces latency. Exact token reduction and latency improvements depend on the overall response shape and size.

To use this beta feature, simply add the beta header `token-efficient-tools-2025-02-19` to a tool use request with `claude-3-7-sonnet-20250219`. If you are using the SDK, ensure that you are using the beta SDK with `anthropic.beta.messages`.

Here's an example of how to use token-efficient tools with the API:

```python
# Sample code to demonstrate token-efficient tools
import anthropic
from anthropic.beta import messages as beta_messages

client = anthropic.Anthropic()

# Use the beta messages endpoint with token-efficient tools
response = beta_messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1000,
    beta_features=["token-efficient-tools-2025-02-19"],
    tools=[{
        "name": "get_weather",
        "description": "Get the current weather for a location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state"
                }
            },
            "required": ["location"]
        }
    }],
    messages=[{
        "role": "user",
        "content": "What's the weather in San Francisco?"
    }]
)
```

The above request should, on average, use fewer input and output tokens than a normal request. To confirm this, try making the same request but remove `token-efficient-tools-2025-02-19` from the beta headers list.

# Text Editor Tool

Claude can use an Anthropic-defined text editor tool to view and modify text files, helping you debug, fix, and improve your code or other text documents. This allows Claude to directly interact with your files, providing hands-on assistance rather than just suggesting changes.

## Before using the text editor tool

### Use a compatible model

Anthropic's text editor tool is only available for Claude 3.5 Sonnet and Claude 3.7 Sonnet:

* **Claude 3.7 Sonnet**: `text_editor_20250124`
* **Claude 3.5 Sonnet**: `text_editor_20241022`

Both versions provide identical capabilities - the version you use should match the model you're working with.

### Assess your use case fit

Some examples of when to use the text editor tool are:

* **Code debugging**: Have Claude identify and fix bugs in your code, from syntax errors to logic issues.
* **Code refactoring**: Let Claude improve your code structure, readability, and performance through targeted edits.
* **Documentation generation**: Ask Claude to add docstrings, comments, or README files to your codebase.
* **Test creation**: Have Claude create unit tests for your code based on its understanding of the implementation.

## Text editor tool commands

The text editor tool supports several commands for viewing and modifying files:

### view

The `view` command allows Claude to examine the contents of a file. It can read the entire file or a specific range of lines.

Parameters:

* `command`: Must be "view"
* `path`: The path to the file to view
* `view_range` (optional): An array of two integers specifying the start and end line numbers to view. Line numbers are 1-indexed, and -1 for the end line means read to the end of the file.

### str_replace

The `str_replace` command allows Claude to replace a specific string in a file with a new string. This is used for making precise edits.

Parameters:

* `command`: Must be "str_replace"
* `path`: The path to the file to modify
* `old_str`: The text to replace (must match exactly, including whitespace and indentation)
* `new_str`: The new text to insert in place of the old text

### create

The `create` command allows Claude to create a new file with specified content.

Parameters:

* `command`: Must be "create"
* `path`: The path where the new file should be created
* `file_text`: The content to write to the new file

### insert

The `insert` command allows Claude to insert text at a specific location in a file.

Parameters:

* `command`: Must be "insert"
* `path`: The path to the file to modify
* `insert_line`: The line number after which to insert the text (0 for beginning of file)
* `new_str`: The text to insert

### undo_edit

The `undo_edit` command allows Claude to revert the last edit made to a file.

Parameters:

* `command`: Must be "undo_edit"
* `path`: The path to the file whose last edit should be undone

## Pricing and token usage

The text editor tool uses the same pricing structure as other tools used with Claude. It follows the standard input and output token pricing based on the Claude model you're using.

In addition to the base tokens, the following additional input tokens are needed for the text editor tool:

| Tool | Additional input tokens |
| --- | --- |
| `text_editor_20241022` (Claude 3.5 Sonnet) | 700 tokens |
| `text_editor_20250124` (Claude 3.7 Sonnet) | 700 tokens |

## Change log

| Date | Version | Changes |
| --- | --- | --- |
| March 13, 2025 | `text_editor_20250124` | Introduction of standalone Text Editor Tool documentation. This version is optimized for Claude 3.7 Sonnet but has identical capabilities to the previous version. |
| October 22, 2024 | `text_editor_20241022` | Initial release of the Text Editor Tool with Claude 3.5 Sonnet. Provides capabilities for viewing, creating, and editing files through the `view`, `create`, `str_replace`, `insert`, and `undo_edit` commands. |