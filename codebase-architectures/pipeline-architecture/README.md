# Pipeline (Sequential Flow) Architecture

This directory demonstrates a Pipeline Architecture implementation with a simple data processing application.

## Structure

```
pipeline-architecture/
├── steps/                       # Composable pipeline steps
│   ├── input_stage.py           # Input parsing and preparation
│   ├── processing_stage.py      # Core computation or transformation
│   └── output_stage.py          # Final formatting or response handling
├── pipeline_manager/            # Pipeline orchestration
│   ├── pipeline_manager.py      # Base pipeline manager
│   └── data_pipeline.py         # Data processing pipeline implementation
└── shared/
    └── utilities.py             # Common utilities across pipeline
```

This architecture follows a more functional approach, where:
- Steps are composable, independent units that can be mixed and matched
- Pipeline managers orchestrate the flow between steps
- Different pipeline implementations can be created for specific use cases
- Each step focuses on a single responsibility and can be tested in isolation

## Benefits

- Clearly defined linear execution simplifies reasoning and debugging
- Easy to scale or optimize individual pipeline stages independently
- Facilitates predictable context management

## Cons

- Rigid linearity limits branching and complex decision-making scenarios
- Major workflow changes can require extensive pipeline refactoring

## Running the Example

```bash
uv run main.py
```

This example demonstrates a data processing pipeline that:
1. Reads and validates input data
2. Processes and transforms the data
3. Formats and outputs the results
