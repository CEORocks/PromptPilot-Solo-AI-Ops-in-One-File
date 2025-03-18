#!/usr/bin/env python3

"""
File editor for the Vertical Slice Architecture implementation of the file editor agent.
This module combines reading and writing capabilities for file editing.
"""

import sys
import os
from typing import Dict, Any, Tuple, Optional

# Add the parent directory to the Python path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.utils import log_info, log_error
from features.file_operations.model_tools import FileOperationResult
from features.file_operations.file_writer import FileWriter
from features.file_operations.read_tool import read_file

class FileEditor:
    """
    File editor that combines reading and writing capabilities for file editing.
    """
    
    @staticmethod
    def read(path: str, start_line: Optional[int] = None, end_line: Optional[int] = None) -> FileOperationResult:
        """
        Read the contents of a file.
        
        Args:
            path: The path to the file to read
            start_line: Optional start line (1-indexed)
            end_line: Optional end line (1-indexed, -1 for end of file)
            
        Returns:
            FileOperationResult with content or error message
        """
        log_info("file_editor", f"Reading file {path} with range {start_line}-{end_line}")
        return read_file(path, start_line, end_line)
    
    @staticmethod
    def view_file(path: str, view_range=None) -> FileOperationResult:
        """
        View the contents of a file with optional range.
        
        Args:
            path: The path to the file to view
            view_range: Optional tuple of (start_line, end_line)
            
        Returns:
            FileOperationResult with content or error message
        """
        start_line = None
        end_line = None
        
        if view_range:
            start_line, end_line = view_range
            
        log_info("file_editor", f"Viewing file {path} with range {start_line}-{end_line}")
        
        return FileEditor.read(path, start_line, end_line)
    
    @staticmethod
    def edit_file(path: str, old_str: str, new_str: str) -> FileOperationResult:
        """
        Edit a file by replacing one string with another.
        
        Args:
            path: The path to the file to edit
            old_str: The string to replace
            new_str: The string to replace it with
            
        Returns:
            FileOperationResult with result or error message
        """
        log_info("file_editor", f"Editing file {path}")
        
        # First, read the file to check if it exists
        read_result = FileEditor.read(path)
        if not read_result.success:
            log_error("file_editor", f"Cannot edit file that can't be read: {read_result.message}")
            return read_result
        
        # Then, use the file writer to replace the string
        return FileWriter.replace(path, old_str, new_str)
    
    @staticmethod
    def create_file(path: str, content: str) -> FileOperationResult:
        """
        Create a new file with the specified content.
        
        Args:
            path: The path to the file to create
            content: The content for the new file
            
        Returns:
            FileOperationResult with result or error message
        """
        log_info("file_editor", f"Creating file {path}")
        
        # Use the file writer to create the file
        return FileWriter.create(path, content)
    
    @staticmethod
    def insert_line(path: str, line_num: int, content: str) -> FileOperationResult:
        """
        Insert content at a specific line in a file.
        
        Args:
            path: The path to the file to modify
            line_num: The line number where to insert (1-indexed)
            content: The content to insert
            
        Returns:
            FileOperationResult with result or error message
        """
        log_info("file_editor", f"Inserting at line {line_num} in file {path}")
        
        # First, read the file to check if it exists
        read_result = FileEditor.read(path)
        if not read_result.success:
            log_error("file_editor", f"Cannot modify file that can't be read: {read_result.message}")
            return read_result
        
        # Then, use the file writer to insert the line
        return FileWriter.insert(path, line_num, content)