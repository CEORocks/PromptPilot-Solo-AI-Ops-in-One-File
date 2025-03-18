#!/usr/bin/env python3

"""
Tool handler for the Vertical Slice Architecture implementation of the file editor agent.
This module handles tool use requests from the Claude agent.
"""

import sys
import os
from typing import Dict, Any

# Add the parent directory to the Python path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.utils import log_info, log_error, normalize_path
from features.file_operations.model_tools import ToolUseRequest
from features.file_operations.file_editor import FileEditor

def handle_tool_use(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Handle tool use requests from the Claude agent.
    
    Args:
        input_data: The tool use request data from Claude
        
    Returns:
        Dictionary with the result or error message
    """
    log_info("tool_handler", f"Received tool use request: {input_data}")
    
    try:
        # Parse the tool use request
        request = ToolUseRequest.from_dict(input_data)
        
        # Normalize the path
        path = normalize_path(request.path) if request.path else None
        
        # Handle the command
        if request.command == "view":
            start_line = request.kwargs.get("start_line")
            end_line = request.kwargs.get("end_line")
            
            if start_line is not None:
                start_line = int(start_line)
            if end_line is not None:
                end_line = int(end_line)
                
            result = FileEditor.read(path, start_line, end_line)
            
        elif request.command == "edit":
            old_str = request.kwargs.get("old_str", "")
            new_str = request.kwargs.get("new_str", "")
            
            result = FileEditor.edit_file(path, old_str, new_str)
            
        elif request.command == "create":
            content = request.kwargs.get("content", "")
            
            result = FileEditor.create_file(path, content)
            
        elif request.command == "insert":
            line_num = int(request.kwargs.get("line_num", 1))
            content = request.kwargs.get("content", "")
            
            result = FileEditor.insert_line(path, line_num, content)
            
        else:
            log_error("tool_handler", f"Unknown command: {request.command}")
            return {"error": f"Unknown command: {request.command}"}
        
        # Return the result
        if result.success:
            return {"result": result.content or result.message}
        else:
            return {"error": result.message}
            
    except Exception as e:
        error_msg = f"Error handling tool use: {str(e)}"
        log_error("tool_handler", error_msg)
        return {"error": error_msg}