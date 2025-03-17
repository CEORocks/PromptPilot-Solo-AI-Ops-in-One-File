# Vertical Slice Architecture

This directory demonstrates a Vertical Slice Architecture implementation with a simple task management application.

## Structure

```
vertical-slice-architecture/
├── features/
│   ├── tasks/
│   │   ├── api.py              # Feature-specific API endpoints
│   │   ├── service.py          # Core business logic
│   │   ├── model.py            # Data models/schema
│   │   └── README.md           # Feature documentation
│   └── users/
│       ├── api.py              # Feature-specific API endpoints
│       ├── service.py          # Core business logic
│       ├── model.py            # Data models/schema
│       └── README.md           # Feature documentation
├── shared/
│   ├── utils.py                # Shared utilities
│   └── db.py                   # Shared database connections
└── main.py                     # Application entry point
```

## Benefits

- Excellent feature isolation; clear and consistent structure
- Each feature is independently testable and maintainable
- Clear feature-level documentation enhances comprehension

## Cons

- Potential for duplicated logic across features
- Complexity increases when blending features; shared logic must be explicitly managed

## Running the Example

```bash
uv run main.py
```
