"""Shared client setup for all examples."""

import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

BASE_URL = "https://api.llmgateway.io/v1"
API_KEY = os.getenv("LLM_GATEWAY_API_KEY")

# Cheap default model used across examples. Override with LLM_GATEWAY_MODEL.
DEFAULT_MODEL = os.getenv("LLM_GATEWAY_MODEL", "gpt-4o-mini")

if not API_KEY or API_KEY.startswith("llmgtwy_your"):
    sys.exit("Set LLM_GATEWAY_API_KEY in .env (see .env.example)")

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


def print_usage(usage) -> None:
    """Print tokens plus the gateway's per-request cost fields."""
    if usage is None:
        return
    extra = usage.model_extra or {}
    cost = extra.get("cost")
    cost_str = f"${cost:.6f}" if isinstance(cost, (int, float)) else "n/a"
    print(
        f"  tokens: {usage.prompt_tokens} in / {usage.completion_tokens} out"
        f" | cost: {cost_str}"
    )
