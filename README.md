# LLM Gateway Playground

Small, runnable Python examples for [LLM Gateway](https://docs.llmgateway.io/) — an
OpenAI-compatible gateway that routes to many LLM providers behind one API key.

## Setup

```bash
cp .env.example .env        # then paste your key into LLM_GATEWAY_API_KEY
uv sync
```

Get a key from the [dashboard](https://llmgateway.io/dashboard) → your project → API Keys.

## Run

```bash
cd examples
uv run python 01_hello.py      # one example
uv run python run_all.py       # all of them
./quickstart.sh                # raw curl version of the quickstart
```

| Example | Feature | Docs |
| --- | --- | --- |
| `01_hello.py` | Basic chat completion via the OpenAI SDK | [Quickstart](https://docs.llmgateway.io/quick-start) |
| `02_streaming.py` | Streaming (SSE) with usage on the final chunk | [Quickstart](https://docs.llmgateway.io/quick-start) |
| `03_routing.py` | Smart routing, `provider/model` pinning, `routing: "price"`, `model: "auto"` | [Routing](https://docs.llmgateway.io/features/routing) |
| `04_metadata_and_cost.py` | `X-LLMGateway-*` metadata headers + per-request cost in `usage` | [Metadata](https://docs.llmgateway.io/features/metadata), [Cost](https://docs.llmgateway.io/features/cost-breakdown) |
| `05_tool_calling.py` | Function / tool calling round-trip | — |
| `06_structured_output.py` | Strict JSON schema output | [Structured outputs](https://docs.llmgateway.io/learn/structured-outputs) |
| `07_reasoning.py` | `reasoning_effort` on a reasoning model | [Reasoning](https://docs.llmgateway.io/features/reasoning) |
| `08_embeddings.py` | Embeddings + tiny semantic search | [Embeddings](https://docs.llmgateway.io/features/embeddings) |
| `09_anthropic_endpoint.py` | Anthropic SDK against `/v1/messages`, with Claude *and* GPT | [Anthropic API](https://docs.llmgateway.io/features/anthropic-endpoint) |
| `10_list_models.py` | List available models (`python 10_list_models.py gemini` to filter) | [Models](https://llmgateway.io/models) |

## Config

- `LLM_GATEWAY_MODEL` — default chat model (default `gpt-4o-mini`)
- `REASONING_MODEL` — model for `07_reasoning.py` (default `gpt-oss-120b`)

After running, check the dashboard's **Activity** page to see each request's
provider, latency, cost and the metadata headers from example 04.
