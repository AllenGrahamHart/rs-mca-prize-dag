# Critical harness coverage census

Status: **AUDIT AND N11 TRUTH REMEDIATION COMPLETE.** This is a packaging
audit, not a proof and not a node-status change. Reproduce it with:

```bash
tools/ramguard tiny -- python3 tools/verify_critical_harness_coverage.py
```

## Scope and interpretation

The census covers the 261-node critical orbit after commit `85d3e860`. Of its
210 `PROVED` nodes:

| coverage class | count | meaning |
|---|---:|---|
| local verifier | 49 | at least one manifest-discoverable `verify*.py` under the node |
| folder, markdown only | 156 | a critical node folder exists, but no discoverable local checker |
| legacy reference only | 5 | no node folder; the DAG cites an older proof source |
| no artifact | 0 | neither a node folder nor a DAG reference |

These numbers must not be read as “only 47 theorems are proved.” Most
mathematical proofs do not acquire truth by being restated in Python. A
checker is load-bearing when the claim is exact arithmetic, a finite census,
a generated table, a computation certificate, or a fragile assembly
contract. Adding ceremonial scripts to prose theorems would increase the
count without increasing confidence.

The initially artifact-free `xr_strip_classification_rungs` node is now
repaired. Its conventional proof records the field-generic two-slope forcing
argument, and its registered checker replays the surviving 69-check official
consumption audit and 88-check line/ray audit. No green critical-orbit node is
now wholly artifact-free.

## Completed N6 repairs

1. `xr_highcore_collision_count` now has a top-level fail-closed verifier for
   all six rows, both currencies, the paid/open rank tables, 28 proved input
   paths, and ten mutations.
2. KB #107 is repaired: the local weight-5 MITM verifier checks the complete
   pinned result/certificate ledger, while the full 64-row search remains in
   the registered Modal launcher.
3. This census is reproducible and manifest-registered. Its pinned classes
   force an explicit refresh when coverage changes.

## Truth-status review

The sweep found four contradictions that could not be repaired by adding a
wrapper. N11 has now adjudicated all four and propagated every status change
through the requirement graph.

| node | conflict | N11 ruling |
|---|---|---|
| `generator_economy` | DAG status was `PROVED`, but its authoritative statement called the subset-sum lift open | restored to `TARGET`; the later signed-8-core discharge is explicitly refuted because `binom(56,28)` zero-sum paddings repeat each `e_1` center; `generator_size_budget_check` is `REFUTED` with an exact checker |
| `far_pair_separation` | unconditional green conflicted with its open design premise | restored to `CONDITIONAL`; its implication proof remains banked |
| `integer_code_distance_cert` | only a toy result was banked; no consumed exhibit-row matrix or full certificate existed | restored to `TARGET`; `lattice_cone_certificate` and `certifier_uniformity` regress to `CONDITIONAL` |
| `u2_per_row_certifier` | no claimed two-prime output or independent certificate checker was banked | restored to `TARGET`; its existing conditional descendants remain amber |

The corrected critical surface is `201 PROVED / 36 CONDITIONAL / 23` open
mathematical leaves. The previous `210 / 31 / 20` count is retired. The green
law in `critical/CRITICAL.md` requires a true claim with a proof artifact, and
computation claims require a pinned result plus replayable verifier.

## Packaging queue

Fourteen green critical nodes have no conventional `proof.md`; the executable
census pins the exact set. Some are thin proxy folders whose proof and checker
live elsewhere. The highest-value repairs are:

1. `qa22_m_le_t_extension` is REPAIRED: its conventional statement/proof and
   registered wrapper now hash-pin the original packet and require a
   byte-identical 3,392-cell replay (26 checks, five mutations).
2. `xr_strip_classification_rungs` is REPAIRED with a self-contained proof
   packet and registered verifier for the six-row consumption arithmetic and
   two-slope forcing contract.
3. `petal_small_scale_staircase_census`: do not register the historical
   `qrl_verify.py` as if it proved the final node. Its own header states that
   it proves three windows and leaves the sub-Johnson band open; the later
   column-relative proof needs its own assembly packet.
4. `generator_size_budget_check` is repaired by an exact refutation packet:
   the signed-8-core raw count treats every zero-sum padding as a new `e_1`
   center, although all `binom(56,28)` paddings of a fixed signed core collide.
   Its consumer `generator_economy` is honestly restored to `TARGET`.

The auto-discharge regression lookup is now partition-aware and verified.
This removed stale generated proofs from `generator_economy` and the already-
amber `worst_word_challenger_pricing` node; future premise demotions fail
closed instead of searching the obsolete top-level `nodes/` path.

Two green nodes still contain verifier-like filenames without a registered
node checker. `petal_small_scale_staircase_census` has an explicitly partial
historical checker; `petal_growth` has falsification-witness verifiers, not a
proof checker for its final theorem. Other mid-name verifier files are
subordinate to registered wrappers. Bulk-renaming any of them would turn
evidence into apparent theorem checkers.

## Upstream discipline

When vendoring a result to Przemek's repository, include its theorem statement,
proof, compact certificate/checker where applicable, and this audit's status
qualification. Expensive regeneration remains a compute request in
`notes/PRIZE_COMPUTE_REQUESTS.md`; it is not evidence until a complete result
and deterministic checker are returned.
