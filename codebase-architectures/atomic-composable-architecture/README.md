# Atomic/Composable Architecture

This directory demonstrates an Atomic/Composable Architecture implementation with a simple notification system application.

## Structure

```
atomic-composable-architecture/
├── atom/                       # Smallest atomic reusable building blocks
│   ├── auth.py                 # Authentication utilities
│   ├── validation.py           # Data validation functions
│   └── notifications.py        # Notification helpers
│
├── molecule/                   # Combines multiple atoms into features
│   ├── user_management.py      # Uses auth + validation atoms
│   └── alerting.py             # Uses notifications + validation atoms
│
└── organism/                   # Combines molecules into user-facing APIs
    ├── user_api.py             # Uses user_management molecule
    └── alerts_api.py           # Uses alerting molecule
```

## Explanation

- **Atom**: Bottom-level reusable components that must remain general-purpose and independent. Atoms can only depend on other atoms, not molecules or organisms.
- **Molecule**: Compose atoms to build concrete functionality. Molecules can depend on multiple atoms, enabling reuse and rapid feature composition.
- **Organism**: The highest level, combining molecules to create user-facing APIs or interfaces.

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
