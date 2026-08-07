# Critical-node document refactor audit

## Scope

Four append-only critical-node documents were replaced by short live indexes
and 36 bounded packets:

- `l1_mixed_petal_amplification/{statement,attack}.md`;
- `rate_half_list_adjacent_crossing/statement.md`;
- `rate_half_band_closure/attack.md`.

The packets follow existing mathematical ownership: global exact-shell versus
local first-owner L1 routes, the rate-half list cycle/Fourier chains, and the
rate-half MCA residual-budget and signed-coordinate programs.  No theorem was
split into a new truth claim merely to reduce file size.  The named owners are
already independent nodes in the DAG.

## Integrity

`tools/refactor_critical_node_documents.py` records the original line ranges,
SHA-256 digests, and owning DAG node IDs.  Its fail-closed verifier proves:

- all 36 packets reassemble byte-for-byte to the four pre-refactor documents;
- every packet is below 50 KB;
- every named owner exists in `dag.json`;
- each short parent index links every packet; and
- the checked indexes and manifests have not drifted.

The four preserved pre-refactor digests are:

```text
b584bf55b8e02310637fd59ed67494b7049cdc0af8d645c16c030db50986321f  L1 statement
6b1287214fbf161c2baabbb571a8b19d5dd6275b4c8b687ccb2938761c69ed46  L1 attack
ce6bc78cb6f9135a596c9e0caa5fadf923f77447430b834e0b33911e65d23cf1  rate-half LIST statement
26f1d1c5015a99cabbbd0abda13f046da317f2aafa04e9856733c818640b58cd  rate-half MCA attack
```

The parent verifiers now read their packet sequences.  While replaying the
rate-half LIST verifier, six already-PROVED incoming evidence suppliers were
found in the compiled DAG but absent from the verifier's exact edge ledger.
The checker now verifies their statuses and includes them as `ev`; no edge was
added or promoted.

## Nonclaim

This is a presentation and auditability refactor.  It changes no proposition,
status, requirement, alternative, evidence edge, critical-orbit census, or
Prize threshold.  New mathematics belongs in the narrowest owning theorem
node; the parent indexes change only when the live residual partition changes.

## Replay

```text
tools/ramguard tiny -- python3 tools/verify_sectioned_critical_node_documents.py
tools/ramguard tiny -- python3 critical/nodes/rate_half_list_adjacent_crossing/verify.py
tools/ramguard tiny -- python3 critical/nodes/rate_half_band_closure/verify_attack_contract.py
tools/ramguard tiny -- python3 tools/verify_dag_manifests.py
tools/ramguard tiny -- python3 tools/verify_orbit_census.py
```
