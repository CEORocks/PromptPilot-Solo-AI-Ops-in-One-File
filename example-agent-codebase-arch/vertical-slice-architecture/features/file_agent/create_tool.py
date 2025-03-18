#!/usr/bin/env python3

"""
Create tool for the Vertical Slice Architecture implementation of the file editor agent.
This module provides file creation capabilities.
"""

import sys
import os

# Add the parent directory to the Python path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.utils import log_info, log_error
from features.file_operations.model_tools import FileOperationResult
from features.file_operations.write_tool import write_file

def create_file(path: str, content: str) -> FileOperationResult:
    """
    Create a new file with the specified content.
    
    Args:
        path: The path to the file to create
        content: The content to write to the file
        
    Returns:
        FileOperationResult with result or error message
    """
    log_info("create_tool", f"Creating file {path}")
    
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        
        # Use the write_file function to create the file
        return write_file(path, content)
    except Exception as e:
        error_msg = f"Failed to create file {path}: {str(e)}"
        log_error("create_tool", error_msg)
        return FileOperationResult(success=False, content="", message=error_msg)