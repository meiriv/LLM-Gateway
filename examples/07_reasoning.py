"""Reasoning models (https://docs.llmgateway.io/features/reasoning).

`reasoning_effort` is normalized by the gateway across providers. Some models
also return their reasoning text in `message.reasoning`.
"""

import os

from common import client, print_usage

MODEL = os.getenv("REASONING_MODEL", "gpt-oss-120b")

res = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "What is 2/3 + 1/4 + 5/6? Answer as a fraction."}],
    reasoning_effort="medium",
)

msg = res.choices[0].message
reasoning = (msg.model_extra or {}).get("reasoning")
if reasoning:
    print("--- reasoning ---")
    print(reasoning.strip())
print("--- answer ---")
print(msg.content)
details = res.usage.completion_tokens_details
if details and details.reasoning_tokens:
    print(f"  reasoning tokens: {details.reasoning_tokens}")
print_usage(res.usage)
