#!/usr/bin/env python3

"""
Insert tool for the Vertical Slice Architecture implementation of the file editor agent.
This module provides line insertion capabilities for files.
"""

import sys
import os

# Add the parent directory to the Python path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.utils import log_info, log_error
from features.file_operations.model_tools import FileOperationResult

def insert_in_file(path: str, insert_line: int, new_str: str) -> FileOperationResult:
    """
    Insert text at a specific line in a file.
    
    Args:
        path: The path to the file to modify
        insert_line: The line number after which to insert the text (1-indexed)
        new_str: The text to insert
        
    Returns:
        FileOperationResult with result or error message
    """
    log_info("insert_tool", f"Inserting text at line {insert_line} in file {path}")
    
    try:
        # Read the existing content
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if insert_line < 1 or insert_line > len(lines) + 1:
            error_msg = f"Invalid line number {insert_line} for file {path} with {len(lines)} lines"
            log_error("insert_tool", error_msg)
            return FileOperationResult(success=False, content="", message=error_msg)
        
        # Insert the new string at the specified position
        lines.insert(insert_line - 1, new_str if new_str.endswith('\n') else new_str + '\n')
        
        # Write the modified content back to the file
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        log_info("insert_tool", f"Successfully inserted text at line {insert_line} in file {path}")
        return FileOperationResult(success=True, content="", message=f"Successfully inserted text at line {insert_line} in file {path}")
    except Exception as e:
        error_msg = f"Failed to insert text at line {insert_line} in file {path}: {str(e)}"
        log_error("insert_tool", error_msg)
        return FileOperationResult(success=False, content="", message=error_msg)