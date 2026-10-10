"""Basic chat completion through LLM Gateway (Quickstart)."""

from common import DEFAULT_MODEL, client, print_usage

res = client.chat.completions.create(
    model=DEFAULT_MODEL,
    messages=[{"role": "user", "content": "Say hello and tell me one fun fact."}],
)

print(f"model: {res.model}")
print(res.choices[0].message.content)
print_usage(res.usage)
