The upgraded Claude 3.7 Sonnet model is capable of calling tools in a token-efficient manner. Requests save an average of 14% in output tokens, up to 70%, which also reduces latency. Exact token reduction and latency improvements depend on the overall response shape and size.

To use this beta feature, simply add the beta header `token-efficient-tools-2025-02-19` to a tool use request with `claude-3-7-sonnet-20250219`. If you are using the SDK, ensure that you are using the beta SDK with `anthropic.beta.messages`.

Here's an example of how to use token-efficient tools with the API:

The above request should, on average, use fewer input and output tokens than a normal request. To confirm this, try making the same request but remove `token-efficient-tools-2025-02-19` from the beta headers list.