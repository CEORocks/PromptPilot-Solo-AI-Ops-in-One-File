# Projects Feature

This feature provides functionality for managing projects in the task management system.

## Components

- **model.py**: Defines the Project model with fields like name, description, user_id, and task_ids
- **service.py**: Contains business logic for project management
- **api.py**: Provides API endpoints for project operations

## Functionality

- Create, read, update, and delete projects
- Assign tasks to projects
- Remove tasks from projects
- Get all tasks for a specific project
- Get all projects for a specific user

## Relationships

- Projects are owned by users (one-to-many)
- Projects can contain multiple tasks (one-to-many)
