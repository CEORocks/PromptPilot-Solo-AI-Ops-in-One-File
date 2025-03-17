# Codebase Architectures

This directory contains examples of different codebase architectures, each implemented with simple, runnable code.

## Architectures Included

1. **Vertical Slice Architecture** - Feature-oriented organization where each feature contains all its necessary components
2. **Layered (N-Tier or MVC) Architecture** - Separation of concerns by technical layer
3. **Pipeline (Sequential Flow) Architecture** - Linear processing stages for data transformation
4. **Atomic/Composable Architecture** - Hierarchical organization from atomic modules to capabilities to endpoints

## Running the Examples

### Python Examples
```bash
cd <architecture-directory>
uv run main.py
```

### Node.js Examples
```bash
cd <architecture-directory>
node main.js
# or if bun is available:
bun run main.js
```

Each architecture directory contains its own README with specific details about the implementation.
