#!/usr/bin/env python3

"""
Search tool for the blog agent in the Vertical Slice Architecture.
This module provides blog post searching capabilities.
"""

import sys
import os
import json
import glob
import re
from typing import Dict, Any, List, Optional

# Add the parent directory to the Python path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.utils import log_info, log_error
from features.blog_agent.model_tools import BlogOperationResult

# Path to store blog posts
BLOG_POSTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "data", "blog_posts")

def search_blog_posts(query: str, search_content: bool = True, 
                     tag: Optional[str] = None, author: Optional[str] = None) -> BlogOperationResult:
    """
    Search blog posts by query string, optionally filtered by tag or author.
    
    Args:
        query: The search query
        search_content: Whether to search in the content (otherwise just title and tags)
        tag: Optional tag to filter by
        author: Optional author to filter by
        
    Returns:
        BlogOperationResult with a list of matching blog posts or error message
    """
    log_info("search_tool", f"Searching blog posts for: {query}")
    
    try:
        # Create directory if it doesn't exist
        os.makedirs(BLOG_POSTS_DIR, exist_ok=True)
        
        # Get all JSON files in the blog posts directory
        file_paths = glob.glob(os.path.join(BLOG_POSTS_DIR, "*.json"))
        
        # Compile the search regex for case-insensitive search
        search_regex = re.compile(query, re.IGNORECASE)
        
        matching_posts = []
        
        for file_path in file_paths:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    blog_post_data = json.load(f)
                
                # Apply filters
                if author and blog_post_data.get("author") != author:
                    continue
                    
                if tag and tag not in blog_post_data.get("tags", []):
                    continue
                
                # Check for match in title
                if search_regex.search(blog_post_data.get("title", "")):
                    matching_posts.append(blog_post_data)
                    continue
                
                # Check for match in tags
                if any(search_regex.search(t) for t in blog_post_data.get("tags", [])):
                    matching_posts.append(blog_post_data)
                    continue
                
                # Check for match in content if requested
                if search_content and search_regex.search(blog_post_data.get("content", "")):
                    matching_posts.append(blog_post_data)
                    continue
                
            except Exception as e:
                log_error("search_tool", f"Error processing file {file_path}: {str(e)}")
                continue
        
        log_info("search_tool", f"Found {len(matching_posts)} matching blog posts")
        return BlogOperationResult(
            success=True, 
            message=f"Found {len(matching_posts)} matching blog posts", 
            data=matching_posts
        )
    except Exception as e:
        error_msg = f"Failed to search blog posts: {str(e)}"
        log_error("search_tool", error_msg)
        return BlogOperationResult(success=False, message=error_msg)