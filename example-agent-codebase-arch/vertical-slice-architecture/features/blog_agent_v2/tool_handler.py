#!/usr/bin/env python3

"""
Tool handler for the Vertical Slice Architecture implementation of the blog agent.
This module handles tool use requests from the Claude agent.
"""

import sys
import os
import json
from typing import Dict, Any, List, Optional

# Add the parent directory to the Python path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.utils import log_info, log_error
from features.blog_agent.model_tools import ToolUseRequest
from features.blog_agent.blog_manager import BlogManager

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
        
        # Handle the command
        if request.command == "create_post":
            title = request.kwargs.get("title", "")
            content = request.kwargs.get("content", "")
            author = request.kwargs.get("author", "")
            tags = request.kwargs.get("tags", [])
            
            result = BlogManager.create_post(title, content, author, tags)
            
        elif request.command == "get_post":
            post_id = request.kwargs.get("post_id", "")
            
            result = BlogManager.get_post(post_id)
            
        elif request.command == "update_post":
            post_id = request.kwargs.get("post_id", "")
            title = request.kwargs.get("title")
            content = request.kwargs.get("content")
            tags = request.kwargs.get("tags")
            published = request.kwargs.get("published")
            
            result = BlogManager.update_post(post_id, title, content, tags, published)
            
        elif request.command == "delete_post":
            post_id = request.kwargs.get("post_id", "")
            
            result = BlogManager.delete_post(post_id)
            
        elif request.command == "list_posts":
            tag = request.kwargs.get("tag")
            author = request.kwargs.get("author")
            published_only = request.kwargs.get("published_only", False)
            
            result = BlogManager.list_posts(tag, author, published_only)
            
        elif request.command == "search_posts":
            query = request.kwargs.get("query", "")
            search_content = request.kwargs.get("search_content", True)
            tag = request.kwargs.get("tag")
            author = request.kwargs.get("author")
            
            result = BlogManager.search_posts(query, search_content, tag, author)
            
        elif request.command == "publish_post":
            post_id = request.kwargs.get("post_id", "")
            
            result = BlogManager.publish_post(post_id)
            
        elif request.command == "unpublish_post":
            post_id = request.kwargs.get("post_id", "")
            
            result = BlogManager.unpublish_post(post_id)
            
        else:
            log_error("tool_handler", f"Unknown command: {request.command}")
            return {"error": f"Unknown command: {request.command}"}
        
        # Return the result
        if result.success:
            # Convert complex objects to JSON serializable format
            if isinstance(result.data, dict) or isinstance(result.data, list):
                # Convert to JSON string and back to ensure serializability
                clean_data = json.loads(json.dumps(result.data))
                return {"result": result.message, "data": clean_data}
            else:
                return {"result": result.message}
        else:
            return {"error": result.message}
            
    except Exception as e:
        error_msg = f"Error handling tool use: {str(e)}"
        log_error("tool_handler", error_msg)
        return {"error": error_msg}