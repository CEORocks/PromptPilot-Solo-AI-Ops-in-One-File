#!/usr/bin/env python3

"""
Models for the blog agent in the Vertical Slice Architecture.
"""

import os
import sys
from typing import Dict, Any, Optional, List, Union
from dataclasses import dataclass

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


@dataclass
class BlogPost:
    """Model representing a blog post."""
    
    title: str
    content: str
    author: str
    tags: List[str]
    published: bool = False
    id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the blog post to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "tags": self.tags,
            "published": self.published,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BlogPost':
        """Create a blog post from a dictionary."""
        return cls(
            id=data.get("id"),
            title=data.get("title", ""),
            content=data.get("content", ""),
            author=data.get("author", ""),
            tags=data.get("tags", []),
            published=data.get("published", False),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at")
        )


class BlogOperationResult:
    """
    Model representing the result of a blog operation.
    """
    
    def __init__(self, success: bool, message: str, data: Any = None):
        """
        Initialize a blog operation result.
        
        Args:
            success: Whether the operation was successful
            message: A message describing the result
            data: Optional data returned by the operation
        """
        self.success = success
        self.message = message
        self.data = data
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the result to a dictionary.
        
        Returns:
            Dictionary representation of the result
        """
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data
        }


class ToolUseRequest:
    """
    Model representing a tool use request from Claude.
    """
    
    def __init__(self, command: str, **kwargs):
        """
        Initialize a tool use request.
        
        Args:
            command: The command to execute
            **kwargs: Additional arguments for the command
        """
        self.command = command
        self.kwargs = kwargs
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ToolUseRequest':
        """
        Create a tool use request from a dictionary.
        
        Args:
            data: Dictionary containing the tool use request
            
        Returns:
            A ToolUseRequest instance
        """
        command = data.get("command")
        
        # Extract all other keys as kwargs
        kwargs = {k: v for k, v in data.items() if k != "command"}
        
        return cls(command, **kwargs)