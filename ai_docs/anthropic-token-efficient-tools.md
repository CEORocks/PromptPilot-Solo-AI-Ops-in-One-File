# Token-efficient tool use (beta)

The upgraded Claude 3.7 Sonnet model is capable of calling tools in a token-efficient manner. Requests save an average of 14% in output tokens, up to 70%, which also reduces latency. Exact token reduction and latency improvements depend on the overall response shape and size.

## How to use token-efficient tools

To use this beta feature, simply add the beta header `token-efficient-tools-2025-02-19` to a tool use request with `claude-3-7-sonnet-20250219`. If you are using the SDK, ensure that you are using the beta SDK with `anthropic.beta.messages`.

### Using the beta SDK
```python
from anthropic.beta import messages as beta_messages

response = beta_messages.create(
    api_key="YOUR_API_KEY",
    model="claude-3-7-sonnet-20250219",
    max_tokens=4096,
    messages=[...],
    tools=[...],
    betas=["token-efficient-tools-2025-02-19"]
)
```

### Using the API directly
```python
headers = {
    "x-api-key": "YOUR_API_KEY",
    "anthropic-beta": "token-efficient-tools-2025-02-19",
    "content-type": "application/json"
}

# Make the API request with these headers
```

## Benefits

Using token-efficient tools should, on average, use fewer input and output tokens than a normal request. This leads to:

1. Lower costs - fewer tokens means lower API costs
2. Reduced latency - smaller payloads process faster
3. Potentially improved performance - more efficient communication

To confirm the benefits, try making the same request with and without the `token-efficient-tools-2025-02-19` beta header and compare the token usage.

## Implementation Note

As of mid-2025, this feature is in beta and requires the beta SDK (`anthropic.beta.messages`). The standard SDK does not yet support this functionality. If you've implemented the flag but aren't seeing token efficiency improvements, make sure you're using the correct SDK version.

_Note: This documentation is based on limited information. For complete and up-to-date details, refer to the official Anthropic documentation._