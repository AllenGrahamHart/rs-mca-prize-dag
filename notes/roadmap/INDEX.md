# Prize Roadmap Index

This directory contains the editable source of the Prize resolution roadmap.
`notes/PRIZE_RESOLUTION_ROADMAP.md` is a generated compatibility view and
must not be edited directly.

## Active views

- [LIST](LIST.md): ordinary-list terminals and adjacent-unsafe obligations.
- [MCA](MCA.md): MCA terminals and shared asymptotic hearts.
- [Rate half](RATE_HALF.md): the deployed KoalaBear rate-half finite route.
- [Shared upstream](SHARED_UPSTREAM.md): harvest/export and terminology map.
- [Compute requests](../compute_requests/INDEX.md): deferred computations.

## Strategy source

The ordered source shards are declared in
`notes/roadmap/document.json`.  Stable strategy is in
`notes/roadmap/sections/`; dated work-cycle history is in
`notes/work_cycles/roadmap_r3/`.

After editing a shard, rebuild and check the compatibility view with:

```text
tools/ramguard tiny -- python3 tools/compile_sectioned_documents.py --write
tools/ramguard tiny -- python3 tools/verify_sectioned_documents.py
```

Mathematical status remains controlled by node-local `node.json` manifests
and the generated `dag.json`, not by any roadmap prose.
