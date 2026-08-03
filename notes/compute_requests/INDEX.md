# Deferred Compute Index

`notes/PRIZE_COMPUTE_REQUESTS.md` is the generated compatibility ledger.
Its editable ordered shards are declared in
`notes/compute_requests/document.json`.

The source sections separate:

- policy, budget, and handoff conventions;
- H3/DSP8 requests;
- quotient-pencil and WCL requests;
- rate-half requests;
- L1, E1, and K3 exact-certificate campaigns.

Resolved and retired requests remain in their source shard for provenance.
New requests belong in the mathematically relevant shard and must print the
decision, expected output, partial-result behavior, timeout, container count,
memory, and cost cap.

Rebuild both generated documents with:

```text
tools/ramguard tiny -- python3 tools/compile_sectioned_documents.py --write
```
