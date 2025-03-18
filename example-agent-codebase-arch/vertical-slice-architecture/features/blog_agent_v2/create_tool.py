#!/usr/bin/env python3

"""
Create tool for the blog agent in the Vertical Slice Architecture.
This module provides blog post creation capabilities.
"""

import sys
import os
import json
import uuid
from datetime import datetime
from typing import Dict, Any

# Add the parent directory to the Python path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.utils import log_info, log_error
from features.blog_agent.model_tools import BlogPost, BlogOperationResult

# Path to store blog posts
BLOG_POSTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "data", "blog_posts")

def create_blog_post(title: str, content: str, author: str, tags: list = None) -> BlogOperationResult:
    """
    Create a new blog post.
    
    Args:
        title: Title of the blog post
        content: Content of the blog post
        author: Author of the blog post
        tags: Optional list of tags
        
    Returns:
        BlogOperationResult with result or error message
    """
    log_info("create_tool", f"Creating blog post: {title}")
    
    try:
        # Create directory if it doesn't exist
        os.makedirs(BLOG_POSTS_DIR, exist_ok=True)
        
        # Generate a unique ID and timestamps
        post_id = str(uuid.uuid4())
        current_time = datetime.now().isoformat()
        
        # Create the blog post
        blog_post = BlogPost(
            id=post_id,
            title=title,
            content=content,
            author=author,
            tags=tags or [],
            published=False,
            created_at=current_time,
            updated_at=current_time
        )
        
        # Save the blog post to a JSON file
        file_path = os.path.join(BLOG_POSTS_DIR, f"{post_id}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(blog_post.to_dict(), f, indent=2)
        
        log_info("create_tool", f"Created blog post: {title} with ID: {post_id}")
        return BlogOperationResult(
            success=True, 
            message=f"Successfully created blog post: {title}", 
            data=blog_post.to_dict()
        )
    except Exception as e:
        error_msg = f"Failed to create blog post: {str(e)}"
        log_error("create_tool", error_msg)
        return BlogOperationResult(success=False, message=error_msg)