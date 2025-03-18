#!/usr/bin/env python3

"""
Replace tool for the Vertical Slice Architecture implementation of the file editor agent.
This module provides string replacement capabilities for files.
"""

import sys
import os

# Add the parent directory to the Python path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.utils import log_info, log_error
from features.file_operations.model_tools import FileOperationResult

def replace_in_file(path: str, old_str: str, new_str: str) -> FileOperationResult:
    """
    Replace a string in a file.
    
    Args:
        path: The path to the file to modify
        old_str: The string to replace
        new_str: The string to replace with
        
    Returns:
        FileOperationResult with result or error message
    """
    log_info("replace_tool", f"Replacing text in file {path}")
    
    try:
        # Read the existing content
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count occurrences to verify uniqueness
        occurrences = content.count(old_str)
        
        if occurrences == 0:
            error_msg = f"String not found in file {path}"
            log_error("replace_tool", error_msg)
            return FileOperationResult(success=False, content="", message=error_msg)
        
        if occurrences > 1:
            error_msg = f"Multiple occurrences ({occurrences}) of the string found in file {path}. Need a unique string to replace."
            log_error("replace_tool", error_msg)
            return FileOperationResult(success=False, content="", message=error_msg)
        
        # Replace the string and write back to the file
        new_content = content.replace(old_str, new_str, 1)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        log_info("replace_tool", f"Successfully replaced text in file {path}")
        return FileOperationResult(success=True, content="", message=f"Successfully replaced text in file {path}")
    except Exception as e:
        error_msg = f"Failed to replace text in file {path}: {str(e)}"
        log_error("replace_tool", error_msg)
        return FileOperationResult(success=False, content="", message=error_msg)