#!/usr/bin/env python3

"""
Write tool for the Vertical Slice Architecture implementation of the file editor agent.
This module provides file writing capabilities.
"""

import sys
import os

# Add the parent directory to the Python path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.utils import log_info, log_error
from features.file_operations.model_tools import FileOperationResult

def write_file(path: str, content: str) -> FileOperationResult:
    """
    Write content to a file.
    
    Args:
        path: The path to the file to write
        content: The content to write to the file
        
    Returns:
        FileOperationResult with result or error message
    """
    log_info("write_tool", f"Writing to file {path}")
    
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        log_info("write_tool", f"Successfully wrote to file {path}")
        return FileOperationResult(success=True, content="", message=f"Successfully wrote to file {path}")
    except Exception as e:
        error_msg = f"Failed to write to file {path}: {str(e)}"
        log_error("write_tool", error_msg)
        return FileOperationResult(success=False, content="", message=error_msg)