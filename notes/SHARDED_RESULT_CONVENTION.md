# Sharded Exact-Result Convention

Use this format for new exact result ledgers that would otherwise produce a
large monolithic JSON file.  Historical pinned outputs are not rewritten
merely for layout.

## Mathematical ownership

**Rows are evidence, not DAG nodes.**  Mint a separate truth-apt node only
when a subclaim has an independently meaningful statement, proof boundary,
falsifier, and consumer.  Source signs, roots, fibers, and census rows remain
certificate records beneath the theorem they support.

## Layout

```text
<result>/
  manifest.json
  shards/
    part-00000.jsonl
    part-00001.jsonl
    ...
```

Each JSONL line is one compact ASCII JSON record.  `manifest.json` records
the global metadata, completeness bit, aggregate record/byte counts, and each
shard's path, count, byte size, and SHA-256 digest.

Use `tools/sharded_result.py:ShardedResultWriter` while computing.  The
default ceiling is 5,000 records per shard; a compiler may choose a smaller
value to keep individual shards comfortably reviewable and replayable.

## Completeness and crashes

The writer atomically finalizes each shard and refreshes an incomplete
manifest after every shard.  This provides **partial-result survival** under
Modal timeout, preemption, or client failure.  Only a manifest with
`complete: true` may support a `PROVED` computational claim.  An
incomplete manifest is evidence only.

## Replay

Before consuming records:

```text
tools/ramguard tiny -- python3 tools/sharded_result.py <result>/manifest.json
```

The verifier streams every shard, parses every record, checks path
containment, and reproduces all counts, byte sizes, and hashes.  Consumers
then use `iter_records()` and must not load the full ledger into memory.

The implementation is mutation-tested by
`tools/verify_sharded_result_convention.py`, including byte corruption and
path traversal.
