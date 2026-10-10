"""List models available through the gateway (/v1/models)."""

import sys

from common import client

needle = sys.argv[1].lower() if len(sys.argv) > 1 else ""
models = sorted(m.id for m in client.models.list() if needle in m.id.lower())
print(f"{len(models)} models" + (f" matching {needle!r}" if needle else ""))
for m in models:
    print(" ", m)
