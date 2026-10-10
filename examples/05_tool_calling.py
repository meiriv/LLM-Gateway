"""Tool / function calling with the standard OpenAI tools format."""

import json

from common import DEFAULT_MODEL, client, print_usage


def get_weather(city: str) -> dict:
    # Fake implementation for the demo.
    return {"city": city, "temp_c": 22, "conditions": "sunny"}


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        },
    }
]

messages = [{"role": "user", "content": "What's the weather in Tel Aviv?"}]
res = client.chat.completions.create(model=DEFAULT_MODEL, messages=messages, tools=tools)
msg = res.choices[0].message

if msg.tool_calls:
    messages.append(msg)
    for call in msg.tool_calls:
        args = json.loads(call.function.arguments)
        print(f"model called {call.function.name}({args})")
        messages.append(
            {
                "role": "tool",
                "tool_call_id": call.id,
                "content": json.dumps(get_weather(**args)),
            }
        )
    res = client.chat.completions.create(model=DEFAULT_MODEL, messages=messages, tools=tools)

print(res.choices[0].message.content)
print_usage(res.usage)
