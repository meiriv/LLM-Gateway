"""Streaming: the gateway normalizes every provider to OpenAI-style SSE chunks.
The final chunk carries `usage` (including cost)."""

from common import DEFAULT_MODEL, client, print_usage

stream = client.chat.completions.create(
    model=DEFAULT_MODEL,
    messages=[{"role": "user", "content": "Write a haiku about API gateways."}],
    stream=True,
    stream_options={"include_usage": True},
)

usage = None
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
    if chunk.usage:
        usage = chunk.usage
print()
print_usage(usage)
