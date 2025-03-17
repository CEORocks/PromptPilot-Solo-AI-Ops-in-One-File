# Layered (N-Tier or MVC) Architecture

This directory demonstrates a Layered Architecture implementation with a simple product catalog application.

## Structure

```
layered-architecture/
├── api/                   # Interfaces (controllers or endpoints)
│   ├── product_api.py
│   └── category_api.py
├── services/              # Business logic layer
│   ├── product_service.py
│   └── category_service.py
├── models/                # Data models and domain objects
│   ├── product.py
│   └── category.py
├── data/                  # Data access and persistence
│   └── database.py
├── utils/                 # Shared utilities
│   └── logger.py
└── main.py                # Application entry point
```

## Benefits

- Clear separation of concerns aids contributions
- Centralized shared logic promotes consistency and reduces duplication
- Clear role signaling (e.g., service vs. API vs. data)

## Cons

- Features spread across layers; context management can be challenging
- Tight coupling may occur between layers, complicating cross-layer changes

## Running the Example

```bash
uv run main.py
```
