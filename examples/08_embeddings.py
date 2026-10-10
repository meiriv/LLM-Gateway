"""Embeddings + a tiny semantic search over three sentences."""

import math

from common import client

docs = [
    "The cat sat on the mat.",
    "Stocks rallied after the earnings report.",
    "A kitten is napping on the rug.",
]
query = "small feline sleeping"

res = client.embeddings.create(model="text-embedding-3-small", input=[query, *docs])
vecs = [d.embedding for d in res.data]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


print(f"query: {query!r}  (dim={len(vecs[0])})")
for doc, score in sorted(((d, cosine(vecs[0], v)) for d, v in zip(docs, vecs[1:])), key=lambda t: -t[1]):
    print(f"  {score:.3f}  {doc}")
