"""Metadata headers + cost breakdown.

X-LLMGateway-* headers show up in the dashboard's Activity log so you can
filter by user/tenant/feature. Every response's `usage` includes cost in USD.
"""

import json

from common import DEFAULT_MODEL, client

res = client.chat.completions.create(
    model=DEFAULT_MODEL,
    messages=[{"role": "user", "content": "Give me a 3-word motto for a startup."}],
    extra_headers={
        "X-LLMGateway-User-ID": "demo-user-42",
        "X-LLMGateway-Tenant-ID": "acme-corp",
        "X-LLMGateway-Feature": "motto-generator",
    },
)

print(res.choices[0].message.content)
print("\nusage (incl. gateway cost fields):")
print(json.dumps(res.usage.model_dump(), indent=2))
