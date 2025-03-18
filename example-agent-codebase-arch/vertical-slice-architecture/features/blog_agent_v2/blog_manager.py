#!/usr/bin/env python3

"""
Blog manager for the Vertical Slice Architecture implementation of the blog agent.
This module combines various blog tools to provide comprehensive blog management capabilities.
"""

import sys
import os
from typing import Dict, Any, List, Optional

# Add the parent directory to the Python path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.utils import log_info, log_error
from features.blog_agent.model_tools import BlogOperationResult
from features.blog_agent.create_tool import create_blog_post
from features.blog_agent.read_tool import read_blog_post, list_blog_posts
from features.blog_agent.update_tool import update_blog_post, publish_blog_post, unpublish_blog_post
from features.blog_agent.delete_tool import delete_blog_post
from features.blog_agent.search_tool import search_blog_posts

class BlogManager:
    """
    Blog manager that combines various tools to provide blog management capabilities.
    """
    
    @staticmethod
    def create_post(title: str, content: str, author: str, tags: List[str] = None) -> BlogOperationResult:
        """
        Create a new blog post.
        
        Args:
            title: The title of the blog post
            content: The content of the blog post
            author: The author of the blog post
            tags: Optional list of tags
            
        Returns:
            BlogOperationResult with result or error message
        """
        log_info("blog_manager", f"Creating blog post: {title}")
        return create_blog_post(title, content, author, tags)
    
    @staticmethod
    def get_post(post_id: str) -> BlogOperationResult:
        """
        Get a blog post by ID.
        
        Args:
            post_id: The ID of the blog post to get
            
        Returns:
            BlogOperationResult with the blog post or error message
        """
        log_info("blog_manager", f"Getting blog post: {post_id}")
        return read_blog_post(post_id)
    
    @staticmethod
    def update_post(post_id: str, title: Optional[str] = None, content: Optional[str] = None,
                   tags: Optional[List[str]] = None, published: Optional[bool] = None) -> BlogOperationResult:
        """
        Update a blog post.
        
        Args:
            post_id: The ID of the blog post to update
            title: Optional new title
            content: Optional new content
            tags: Optional new tags
            published: Optional new publication status
            
        Returns:
            BlogOperationResult with the updated blog post or error message
        """
        log_info("blog_manager", f"Updating blog post: {post_id}")
        return update_blog_post(post_id, title, content, tags, published)
    
    @staticmethod
    def delete_post(post_id: str) -> BlogOperationResult:
        """
        Delete a blog post.
        
        Args:
            post_id: The ID of the blog post to delete
            
        Returns:
            BlogOperationResult with result or error message
        """
        log_info("blog_manager", f"Deleting blog post: {post_id}")
        return delete_blog_post(post_id)
    
    @staticmethod
    def list_posts(tag: Optional[str] = None, author: Optional[str] = None, 
                  published_only: bool = False) -> BlogOperationResult:
        """
        List blog posts, optionally filtered by tag, author, or publication status.
        
        Args:
            tag: Optional tag to filter by
            author: Optional author to filter by
            published_only: Whether to only return published posts
            
        Returns:
            BlogOperationResult with a list of blog posts or error message
        """
        log_info("blog_manager", "Listing blog posts")
        return list_blog_posts(tag, author, published_only)
    
    @staticmethod
    def search_posts(query: str, search_content: bool = True, 
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
        log_info("blog_manager", f"Searching blog posts for: {query}")
        return search_blog_posts(query, search_content, tag, author)
    
    @staticmethod
    def publish_post(post_id: str) -> BlogOperationResult:
        """
        Publish a blog post.
        
        Args:
            post_id: The ID of the blog post to publish
            
        Returns:
            BlogOperationResult with the published blog post or error message
        """
        log_info("blog_manager", f"Publishing blog post: {post_id}")
        return publish_blog_post(post_id)
    
    @staticmethod
    def unpublish_post(post_id: str) -> BlogOperationResult:
        """
        Unpublish a blog post.
        
        Args:
            post_id: The ID of the blog post to unpublish
            
        Returns:
            BlogOperationResult with the unpublished blog post or error message
        """
        log_info("blog_manager", f"Unpublishing blog post: {post_id}")
        return unpublish_blog_post(post_id)