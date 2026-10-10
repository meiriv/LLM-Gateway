"""Structured output with a strict JSON schema
(https://docs.llmgateway.io/learn/structured-outputs)."""

import json

from common import DEFAULT_MODEL, client, print_usage

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "year": {"type": "integer"},
        "genres": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["name", "year", "genres"],
    "additionalProperties": False,
}

res = client.chat.completions.create(
    model=DEFAULT_MODEL,
    messages=[{"role": "user", "content": "Describe the movie The Matrix."}],
    response_format={
        "type": "json_schema",
        "json_schema": {"name": "movie", "strict": True, "schema": schema},
    },
)

data = json.loads(res.choices[0].message.content)
print(json.dumps(data, indent=2))
print_usage(res.usage)
