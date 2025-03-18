#!/usr/bin/env python3

"""
Read tool for the blog agent in the Vertical Slice Architecture.
This module provides blog post reading capabilities.
"""

import sys
import os
import json
import glob
from typing import Dict, Any, List, Optional

# Add the parent directory to the Python path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.utils import log_info, log_error
from features.blog_agent.model_tools import BlogPost, BlogOperationResult

# Path to store blog posts
BLOG_POSTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "data", "blog_posts")

def read_blog_post(post_id: str) -> BlogOperationResult:
    """
    Read a blog post by ID.
    
    Args:
        post_id: The ID of the blog post to read
        
    Returns:
        BlogOperationResult with the blog post or error message
    """
    log_info("read_tool", f"Reading blog post with ID: {post_id}")
    
    try:
        # Read the blog post from the JSON file
        file_path = os.path.join(BLOG_POSTS_DIR, f"{post_id}.json")
        
        if not os.path.exists(file_path):
            error_msg = f"Blog post with ID {post_id} not found"
            log_error("read_tool", error_msg)
            return BlogOperationResult(success=False, message=error_msg)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            blog_post_data = json.load(f)
        
        # Create a BlogPost object from the data
        blog_post = BlogPost.from_dict(blog_post_data)
        
        log_info("read_tool", f"Successfully read blog post: {blog_post.title}")
        return BlogOperationResult(
            success=True, 
            message=f"Successfully read blog post: {blog_post.title}", 
            data=blog_post.to_dict()
        )
    except Exception as e:
        error_msg = f"Failed to read blog post: {str(e)}"
        log_error("read_tool", error_msg)
        return BlogOperationResult(success=False, message=error_msg)

def list_blog_posts(tag: Optional[str] = None, author: Optional[str] = None, 
                   published_only: bool = False) -> BlogOperationResult:
    """
    List all blog posts, optionally filtered by tag, author, or publication status.
    
    Args:
        tag: Optional tag to filter by
        author: Optional author to filter by
        published_only: Whether to only return published posts
        
    Returns:
        BlogOperationResult with a list of blog posts or error message
    """
    log_info("read_tool", "Listing blog posts")
    
    try:
        # Create directory if it doesn't exist
        os.makedirs(BLOG_POSTS_DIR, exist_ok=True)
        
        # Get all JSON files in the blog posts directory
        file_paths = glob.glob(os.path.join(BLOG_POSTS_DIR, "*.json"))
        
        blog_posts = []
        
        for file_path in file_paths:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    blog_post_data = json.load(f)
                    
                # Apply filters
                if published_only and not blog_post_data.get("published", False):
                    continue
                    
                if author and blog_post_data.get("author") != author:
                    continue
                    
                if tag and tag not in blog_post_data.get("tags", []):
                    continue
                    
                blog_posts.append(blog_post_data)
            except Exception as e:
                log_error("read_tool", f"Error reading file {file_path}: {str(e)}")
                continue
        
        log_info("read_tool", f"Listed {len(blog_posts)} blog posts")
        return BlogOperationResult(
            success=True, 
            message=f"Successfully listed {len(blog_posts)} blog posts", 
            data=blog_posts
        )
    except Exception as e:
        error_msg = f"Failed to list blog posts: {str(e)}"
        log_error("read_tool", error_msg)
        return BlogOperationResult(success=False, message=error_msg)