#!/usr/bin/env python3

"""
File writer for the Vertical Slice Architecture implementation of the file editor agent.
This module provides file writing capabilities by composing various tools.
"""

import sys
import os
from typing import Dict, Any

# Add the parent directory to the Python path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.utils import log_info, log_error
from features.file_operations.model_tools import FileOperationResult
from features.file_operations.write_tool import write_file
from features.file_operations.replace_tool import replace_in_file
from features.file_operations.insert_tool import insert_in_file
from features.file_operations.create_tool import create_file

class FileWriter:
    """
    File writer that composes various tools to provide file writing capabilities.
    """
    
    @staticmethod
    def write(path: str, content: str) -> FileOperationResult:
        """
        Write content to a file.
        
        Args:
            path: The path to the file to write
            content: The content to write to the file
            
        Returns:
            FileOperationResult with result or error message
        """
        log_info("file_writer", f"Writing to file {path}")
        return write_file(path, content)
    
    @staticmethod
    def replace(path: str, old_str: str, new_str: str) -> FileOperationResult:
        """
        Replace a string in a file.
        
        Args:
            path: The path to the file to modify
            old_str: The string to replace
            new_str: The string to replace with
            
        Returns:
            FileOperationResult with result or error message
        """
        log_info("file_writer", f"Replacing text in file {path}")
        return replace_in_file(path, old_str, new_str)
    
    @staticmethod
    def insert(path: str, insert_line: int, new_str: str) -> FileOperationResult:
        """
        Insert text at a specific line in a file.
        
        Args:
            path: The path to the file to modify
            insert_line: The line number after which to insert the text (1-indexed)
            new_str: The text to insert
            
        Returns:
            FileOperationResult with result or error message
        """
        log_info("file_writer", f"Inserting text at line {insert_line} in file {path}")
        return insert_in_file(path, insert_line, new_str)
    
    @staticmethod
    def create(path: str, content: str) -> FileOperationResult:
        """
        Create a new file with the specified content.
        
        Args:
            path: The path to the file to create
            content: The content to write to the file
            
        Returns:
            FileOperationResult with result or error message
        """
        log_info("file_writer", f"Creating file {path}")
        return create_file(path, content)