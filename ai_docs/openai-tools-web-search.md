# OpenAI Web Search Documentation

## Overview

OpenAI's Web Search tool allows models to search the web for the latest information before generating a response. This is implemented through the Responses API by configuring it in the `tools` array in an API request.

## Basic Implementation

```python
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?"
)

print(response.output_text)
```

```javascript
import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
    model: "gpt-4o",
    tools: [ { type: "web_search_preview" } ],
    input: "What was a positive news story from today?",
});

console.log(response.output_text);
```

## Tool Versioning

The current default version is `web_search_preview` which points to a dated version `web_search_preview_2025_03_11`.

You can force the use of the `web_search_preview` tool by using the `tool_choice` parameter.

## Output and Citations

Model responses include:
- A `web_search_call` output item with the search call ID
- A `message` output item containing the text result and annotations for cited URLs

Example response structure:
```json
[
  {
    "type": "web_search_call",
    "id": "ws_67c9fa0502748190b7dd390736892e100be649c1a5ff9609",
    "status": "completed"
  },
  {
    "id": "msg_67c9fa077e288190af08fdffda2e34f20be649c1a5ff9609",
    "type": "message",
    "status": "completed",
    "role": "assistant",
    "content": [
      {
        "type": "output_text",
        "text": "On March 6, 2025, several news...",
        "annotations": [
          {
            "type": "url_citation",
            "start_index": 2606,
            "end_index": 2758,
            "url": "https://...",
            "title": "Title..."
          }
        ]
      }
    ]
  }
]
```

## Location-Based Results

You can specify an approximate user location to refine search results using:
- `city` and `region` (free text strings like "Minneapolis" and "Minnesota")
- `country` (two-letter ISO country code like "US")
- `timezone` (IANA timezone like "America/Chicago")

Example:
```python
response = client.responses.create(
    model="gpt-4o",
    tools=[{
        "type": "web_search_preview",
        "user_location": {
            "type": "approximate",
            "country": "GB",
            "city": "London",
            "region": "London",
        }
    }],
    input="What are the best restaurants around Granary Square?",
)
```

## Search Context Size

The `search_context_size` parameter controls how much context is retrieved from the web and impacts:
- **Cost**: Higher context sizes are more expensive
- **Quality**: Higher context sizes provide richer, more accurate answers
- **Latency**: Higher context sizes require more processing time

Available values:
- `high`: Most comprehensive, highest cost, slower response
- `medium`: (default) Balanced context, cost, and latency
- `low`: Minimal context, lowest cost, fastest response

Example:
```python
response = client.responses.create(
    model="gpt-4o",
    tools=[{
        "type": "web_search_preview",
        "search_context_size": "low",
    }],
    input="What movie won best picture in 2025?",
)
```

## Limitations

- Does not support zero data retention or data residency
- The `gpt-4o-search-preview` and `gpt-4o-mini-search-preview` models only support a subset of API parameters
- Web search has tiered rate limits when used with the Responses API

*Content sourced from OpenAI documentation on March 15, 2025*