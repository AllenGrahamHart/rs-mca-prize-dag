# F3 residual frontier ledger

Status: REPLAYED RESIDUAL LEDGER, NOT `F3_FLIP_DOSSIER`.

This packet aggregates the current T3, h=3, and T4 frontier ledgers for
`notes/codex_briefs/F3_FLIP_20260708.md`.  It launches no search.  To keep the
replay under the local 60-second policy, it replays T3 and h=3 directly and
checks the pinned T4 residual ledger state instead of re-running the heavier
T4 audit.  Its purpose is to keep the remaining F3 blockers explicit before
the next proof attack.

## Current State

```text
T3:
  h=2 external import closes all 29 official rows.
  h=2 in-house chain still has four accounting-only residual rows, 2^19..2^22.
  H3-ACCIDENT(16) would cover all 29 official h=3 rows from n>=17.
  Official-row h=3 arithmetic would also accept any uniform accident constant
  C <= 8191, with C=4096 leaving about a factor-two first-row margin.

h=3:
  H3-ACT-COMPILER is conditional; the official-row target can be weakened to
  H3-ACT(4096), while H3-ACT(16) remains a stronger sufficient target.
  F3-RANK-AVOID / RC-NV remains open.
  H3-BRIDGE-RANKCAP remains open.
  F3-PRIVATE-LINEAR-RANK-AVOID remains an open alternate.
  H3-REPEAT-BOUNDARY-STAR remains open.

T4:
  h=4 structural localization is proved.
  h=5 is paid for the direct n^3 budget.
  h=6/h=7 are paid for the current budget.
  h=8 n=64 non-antipodal x83 remains open.
```

## Residual Frontier

The top-level F3 flip is still open for two reasons.

First, the h=3 route still needs a proof of `H3-ACT(16)` or a replacement by
official-row activation certificates.  The current route to `H3-ACT(16)` is
not a single numerical gap: it runs through rank/nonvanishing, rank-capacity
bridge accounting, and the repeat-boundary star route.  The strongest current
degree-2 budget has `Z_exact=33..21421`; a bounded rank-deficit theorem with
`Delta <= 1847` would suffice for those official boxes.  The private-linear
alternate has `Z_private=23..15267`, with required bounded deficit
`Delta <= 25`.
The current bridge/rank interfaces target `H3-ACT(16)`, but the official-row
T3 arithmetic can be retuned to a weaker target; `H3-ACT(4096)` keeps about a
factor-two first-row margin, and `H3-ACT(8191)` is the largest uniform integer
accepted by this compiler.

Second, T4 has been reduced to the h=8 non-antipodal x83 branch.  The current
remaining certificate scale is

```text
122,131,731,640,320 anchored non-antipodal 16-supports
7,633,233,227,520 aperiodic rotation orbits.
```

The h=5 central work no longer blocks the direct `n^3` budget: the central
projective-infinity exclusion plus finite-scheme payment route pays that
stratum.  Stronger h=5 norm-gate emptiness is optional for this F3 objective.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_residual_frontier_ledger.py
```

Companion lightweight replays:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_frontier_ledger.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_t3_constant_campaign_ledger.py
```

Expected digest:

```text
F3_FLIP_RESIDUAL_FRONTIER_LEDGER_PASS
H3_FRONTIER_LEDGER_PASS
F3_T3_CONSTANT_CAMPAIGN_LEDGER_PASS
```
