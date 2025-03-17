# Atomic/Composable Architecture

This directory demonstrates an Atomic/Composable Architecture implementation with a simple notification system application.

## Structure

```
atomic-composable-architecture/
├── modules/                    # Smallest atomic reusable building blocks
│   ├── auth.py                 # Authentication utilities
│   ├── validation.py           # Data validation functions
│   └── notifications.py        # Notification helpers
│
├── capabilities/               # Combines multiple modules into features
│   ├── user_management.py      # Uses auth + validation modules
│   └── alerting.py             # Uses notifications + validation modules
│
└── endpoints/                  # Combines capabilities into user-facing APIs
    ├── user_api.py             # Uses user_management capability
    └── alerts_api.py           # Uses alerting capability
```

## Explanation

- **Atomic (modules)**: Bottom-level reusable components that must remain general-purpose and independent. Modules can only depend on other modules, not capabilities or endpoints.
- **Capabilities**: Compose modules to build concrete functionality. Capabilities can depend on multiple modules, enabling reuse and rapid feature composition.
- **Endpoints**: The highest level, combining capabilities to create user-facing APIs or interfaces.

## Benefits

- Maximizes code reuse and composability; reduces duplication and accelerates feature development.
- Clear hierarchical structure makes it easy to reason about what building blocks are available.
- Promotes small, focused, and easily understandable code units.

## Cons

- Indirection introduced by composability can make dependency tracing challenging.
- Understanding module usage patterns (what uses what) may require navigating through multiple files or explicit documentation.
- Requires discipline and careful adherence to dependency rules to avoid cyclic or unintended dependencies.

## Running the Example

```bash
uv run main.py
```
