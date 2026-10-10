"""Routing (https://docs.llmgateway.io/features/routing):

1. model id only      -> gateway picks the best provider for that model
2. provider/model     -> pin a specific provider
3. routing="price"    -> bias provider choice toward the cheapest healthy one
4. model="auto"       -> gateway picks the model itself
"""

from common import client, print_usage

PROMPT = [{"role": "user", "content": "In one sentence: what is an LLM gateway?"}]

cases = [
    ("model id (smart routing)", {"model": "gpt-4o-mini"}),
    ("pinned provider", {"model": "openai/gpt-4o-mini"}),
    ("routing=price", {"model": "gpt-4o-mini", "extra_body": {"routing": "price"}}),
    ("auto model", {"model": "auto"}),
]

for label, kwargs in cases:
    print(f"\n=== {label} ({kwargs['model']}) ===")
    try:
        res = client.chat.completions.create(messages=PROMPT, **kwargs)
        print(f"  served by: {res.model}")
        print(f"  {res.choices[0].message.content.strip()}")
        print_usage(res.usage)
    except Exception as e:  # keep going so one failure doesn't hide the others
        print(f"  error: {e}")
