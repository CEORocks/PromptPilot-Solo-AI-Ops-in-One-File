#!/usr/bin/env python3

"""
Delete tool for the blog agent in the Vertical Slice Architecture.
This module provides blog post deletion capabilities.
"""

import sys
import os
import json
from typing import Dict, Any

# Add the parent directory to the Python path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.utils import log_info, log_error
from features.blog_agent.model_tools import BlogOperationResult
from features.blog_agent.read_tool import read_blog_post

# Path to store blog posts
BLOG_POSTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "data", "blog_posts")

def delete_blog_post(post_id: str) -> BlogOperationResult:
    """
    Delete a blog post by ID.
    
    Args:
        post_id: The ID of the blog post to delete
        
    Returns:
        BlogOperationResult with result or error message
    """
    log_info("delete_tool", f"Deleting blog post with ID: {post_id}")
    
    try:
        # Verify the blog post exists
        read_result = read_blog_post(post_id)
        
        if not read_result.success:
            return read_result
        
        # Get the blog post title for the response message
        blog_post_title = read_result.data["title"]
        
        # Delete the blog post file
        file_path = os.path.join(BLOG_POSTS_DIR, f"{post_id}.json")
        os.remove(file_path)
        
        log_info("delete_tool", f"Deleted blog post: {blog_post_title}")
        return BlogOperationResult(
            success=True, 
            message=f"Successfully deleted blog post: {blog_post_title}"
        )
    except Exception as e:
        error_msg = f"Failed to delete blog post: {str(e)}"
        log_error("delete_tool", error_msg)
        return BlogOperationResult(success=False, message=error_msg)