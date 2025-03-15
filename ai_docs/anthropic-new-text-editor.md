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

---

## Use the text editor tool

Provide the text editor tool (named `str_replace_editor`) to Claude using the Messages API:

The text editor tool can be used in the following way:

### Text editor tool commands

The text editor tool supports several commands for viewing and modifying files:

#### view

The `view` command allows Claude to examine the contents of a file. It can read the entire file or a specific range of lines.

Parameters:

* `command`: Must be "view"
* `path`: The path to the file to view
* `view_range` (optional): An array of two integers specifying the start and end line numbers to view. Line numbers are 1-indexed, and -1 for the end line means read to the end of the file.

#### str\_replace

The `str_replace` command allows Claude to replace a specific string in a file with a new string. This is used for making precise edits.

Parameters:

* `command`: Must be "str\_replace"
* `path`: The path to the file to modify
* `old_str`: The text to replace (must match exactly, including whitespace and indentation)
* `new_str`: The new text to insert in place of the old text

#### create

The `create` command allows Claude to create a new file with specified content.

Parameters:

* `command`: Must be "create"
* `path`: The path where the new file should be created
* `file_text`: The content to write to the new file

#### insert

The `insert` command allows Claude to insert text at a specific location in a file.

Parameters:

* `command`: Must be "insert"
* `path`: The path to the file to modify
* `insert_line`: The line number after which to insert the text (0 for beginning of file)
* `new_str`: The text to insert

#### undo\_edit

The `undo_edit` command allows Claude to revert the last edit made to a file.

Parameters:

* `command`: Must be "undo\_edit"
* `path`: The path to the file whose last edit should be undone

### Example: Fixing a syntax error with the text editor tool

This example demonstrates how Claude uses the text editor tool to fix a syntax error in a Python file.

First, your application provides Claude with the text editor tool and a prompt to fix a syntax error:

Claude will use the text editor tool first to view the file:

Your application should then read the file and return its contents to Claude:

Claude will identify the syntax error and use the `str_replace` command to fix it:

Your application should then make the edit and return the result:

Finally, Claude will provide a complete explanation of the fix:

---

## Implement the text editor tool

The text editor tool is implemented as a schema-less tool, identified by `type: "text_editor_20250124"`. When using this tool, you don't need to provide an input schema as with other tools; the schema is built into Claude's model and can't be modified.

### Handle errors

When using the text editor tool, various errors may occur. Here is guidance on how to handle them:

### Follow implementation best practices

---

## Pricing and token usage

The text editor tool uses the same pricing structure as other tools used with Claude. It follows the standard input and output token pricing based on the Claude model you're using.

In addition to the base tokens, the following additional input tokens are needed for the text editor tool:

| Tool | Additional input tokens |
| --- | --- |
| `text_editor_20241022` (Claude 3.5 Sonnet) | 700 tokens |
| `text_editor_20250124` (Claude 3.7 Sonnet) | 700 tokens |

For more detailed information about tool pricing, see [Tool use pricing](about:/en/docs/build-with-claude/tool-use#pricing).

## Integrate the text editor tool with computer use

The text editor tool can be used alongside the [computer use tool](/en/docs/agents-and-tools/computer-use) and other Anthropic-defined tools. When combining these tools, you'll need to:

1. Include the appropriate beta header (if using with computer use)
2. Match the tool version with the model you're using
3. Account for the additional token usage for all tools included in your request

For more information about using the text editor tool in a computer use context, see the [Computer use](/en/docs/agents-and-tools/computer-use).

## Change log

| Date | Version | Changes |
| --- | --- | --- |
| March 13, 2025 | `text_editor_20250124` | Introduction of standalone Text Editor Tool documentation. This version is optimized for Claude 3.7 Sonnet but has identical capabilities to the previous version. |
| October 22, 2024 | `text_editor_20241022` | Initial release of the Text Editor Tool with Claude 3.5 Sonnet. Provides capabilities for viewing, creating, and editing files through the `view`, `create`, `str_replace`, `insert`, and `undo_edit` commands. |

## Next steps

Here are some ideas for how to use the text editor tool in more convenient and powerful ways:

* **Integrate with your development workflow**: Build the text editor tool into your development tools or IDE
* **Create a code review system**: Have Claude review your code and make improvements
* **Build a debugging assistant**: Create a system where Claude can help you diagnose and fix issues in your code
* **Implement file format conversion**: Let Claude help you convert files from one format to another
* **Automate documentation**: Set up workflows for Claude to automatically document your code

As you build applications with the text editor tool, we're excited to see how you leverage Claude's capabilities to enhance your development workflow and productivity.