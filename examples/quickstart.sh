#!/usr/bin/env bash
# Raw HTTP quickstart, straight from https://docs.llmgateway.io/quick-start
set -euo pipefail
cd "$(dirname "$0")/.."
[ -f .env ] && set -a && . ./.env && set +a

curl -sS -X POST https://api.llmgateway.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LLM_GATEWAY_API_KEY" \
  -d '{"model": "gpt-4o-mini", "messages": [{"role": "user", "content": "Hello"}]}'
echo
