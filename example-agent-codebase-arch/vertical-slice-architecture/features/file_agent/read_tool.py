#!/usr/bin/env python3

"""
Read tool for the Vertical Slice Architecture implementation of the file editor agent.
This module provides file reading capabilities.
"""

import sys
import os
from typing import Optional

# Add the parent directory to the Python path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.utils import log_info, log_error
from features.file_operations.model_tools import FileOperationResult

def read_file(path: str, start_line: Optional[int] = None, end_line: Optional[int] = None) -> FileOperationResult:
    """
    Read the contents of a file.
    
    Args:
        path: The path to the file to read
        start_line: Optional start line (1-indexed)
        end_line: Optional end line (1-indexed, -1 for end of file)
        
    Returns:
        FileOperationResult with content or error message
    """
    log_info("read_tool", f"Reading file {path} with range {start_line}-{end_line}")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
        
        # Handle line range
        if start_line is not None:
            start_idx = max(0, start_line - 1)  # Convert 1-indexed to 0-indexed
        else:
            start_idx = 0
            
        if end_line is not None:
            if end_line == -1:
                end_idx = len(all_lines)
            else:
                end_idx = min(end_line, len(all_lines))
        else:
            end_idx = len(all_lines)
            
        selected_lines = all_lines[start_idx:end_idx]
        content = ''.join(selected_lines)
        
        log_info("read_tool", f"Successfully read file {path}")
        return FileOperationResult(success=True, content=content, message=f"Successfully read file {path}")
    except Exception as e:
        error_msg = f"Failed to read file {path}: {str(e)}"
        log_error("read_tool", error_msg)
        return FileOperationResult(success=False, content="", message=error_msg)