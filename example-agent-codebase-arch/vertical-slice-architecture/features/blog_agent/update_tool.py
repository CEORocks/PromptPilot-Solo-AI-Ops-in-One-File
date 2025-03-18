#!/usr/bin/env python3

"""
Update tool for the blog agent in the Vertical Slice Architecture.
This module provides blog post updating capabilities.
"""

import sys
import os
import json
from datetime import datetime
from typing import Dict, Any, List, Optional

# Add the parent directory to the Python path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.utils import log_info, log_error
from features.blog_agent.model_tools import BlogPost, BlogOperationResult
from features.blog_agent.read_tool import read_blog_post

# Path to store blog posts
BLOG_POSTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "data", "blog_posts")

def update_blog_post(post_id: str, title: Optional[str] = None, content: Optional[str] = None,
                    tags: Optional[List[str]] = None, published: Optional[bool] = None) -> BlogOperationResult:
    """
    Update a blog post by ID.
    
    Args:
        post_id: The ID of the blog post to update
        title: Optional new title
        content: Optional new content
        tags: Optional new tags
        published: Optional new publication status
        
    Returns:
        BlogOperationResult with the updated blog post or error message
    """
    log_info("update_tool", f"Updating blog post with ID: {post_id}")
    
    try:
        # Read the existing blog post
        read_result = read_blog_post(post_id)
        
        if not read_result.success:
            return read_result
        
        # Get the existing blog post data
        blog_post_data = read_result.data
        
        # Update the fields
        if title is not None:
            blog_post_data["title"] = title
            
        if content is not None:
            blog_post_data["content"] = content
            
        if tags is not None:
            blog_post_data["tags"] = tags
            
        if published is not None:
            blog_post_data["published"] = published
            
        # Update the updated_at timestamp
        blog_post_data["updated_at"] = datetime.now().isoformat()
        
        # Save the updated blog post to the JSON file
        file_path = os.path.join(BLOG_POSTS_DIR, f"{post_id}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(blog_post_data, f, indent=2)
        
        log_info("update_tool", f"Updated blog post: {blog_post_data['title']}")
        return BlogOperationResult(
            success=True, 
            message=f"Successfully updated blog post: {blog_post_data['title']}", 
            data=blog_post_data
        )
    except Exception as e:
        error_msg = f"Failed to update blog post: {str(e)}"
        log_error("update_tool", error_msg)
        return BlogOperationResult(success=False, message=error_msg)

def publish_blog_post(post_id: str) -> BlogOperationResult:
    """
    Publish a blog post by ID.
    
    Args:
        post_id: The ID of the blog post to publish
        
    Returns:
        BlogOperationResult with the published blog post or error message
    """
    log_info("update_tool", f"Publishing blog post with ID: {post_id}")
    return update_blog_post(post_id, published=True)

def unpublish_blog_post(post_id: str) -> BlogOperationResult:
    """
    Unpublish a blog post by ID.
    
    Args:
        post_id: The ID of the blog post to unpublish
        
    Returns:
        BlogOperationResult with the unpublished blog post or error message
    """
    log_info("update_tool", f"Unpublishing blog post with ID: {post_id}")
    return update_blog_post(post_id, published=False)