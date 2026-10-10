"""Anthropic-compatible /v1/messages endpoint: use the Anthropic SDK with
*any* model in the catalog (https://docs.llmgateway.io/features/anthropic-endpoint)."""

import os

from anthropic import Anthropic

from common import API_KEY

client = Anthropic(base_url="https://api.llmgateway.io", auth_token=API_KEY)

for model in ["claude-haiku-4-5", "gpt-4o-mini"]:
    print(f"\n=== {model} via Anthropic API format ===")
    try:
        msg = client.messages.create(
            model=os.getenv("ANTHROPIC_DEMO_MODEL", model),
            max_tokens=200,
            messages=[{"role": "user", "content": "Name three primary colors, comma-separated."}],
        )
        print(msg.content[0].text)
        print(f"  tokens: {msg.usage.input_tokens} in / {msg.usage.output_tokens} out")
    except Exception as e:
        print(f"  error: {e}")
