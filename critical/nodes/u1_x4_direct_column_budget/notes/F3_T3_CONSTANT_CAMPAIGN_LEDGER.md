# F3 T3 constant-campaign ledger

Status: REPLAYED CONSTANT-CAMPAIGN LEDGER, NOT AN F3 FLIP DOSSIER.

This packet aggregates the current T3 arithmetic requested by
`notes/codex_briefs/F3_FLIP_20260708.md`.  It launches no search and proves no
new Stepanov theorem.  It keeps the theorem / certificate / residual split
explicit for the h=2 in-house chain and the conditional h=3 accident route.

## h=2

The optimized in-house h=2 chain uses `K=66` and gives

```text
T_2 < h^3 for integer h >= 7639006.
```

Therefore, among official powers `h=2^s`, `13 <= s <= 41`,

```text
theorem-covered by in-house chain: 2^23..2^41;
feasible exact-census rows:        2^13..2^18;
residual in-house midrange rows:   2^19..2^22.
```

The feasible/residual split uses the explicit planning model from
`F3_H2_MIDRANGE_CERTIFICATE_COSTS.md`: shard unit `2^26` ordered differences
and threshold `< 2000` shards.  The external Cochrane--Pinner import still
closes all official h=2 rows; the in-house residual is only T3 accounting.

## h=3

The per-row accident compiler proves the arithmetic implication

```text
H3-ACCIDENT(16) => T_3 < n^3 for all n >= 17.
```

Since every official row has `n=2^s >= 2^13`, the conditional accident theorem
would cover all `29` official h=3 rows.  At the first official row, the
compiled bound is below `0.001955 n^3` (floor `1954` parts per million).

The residual is not a finite low-row problem:

```text
prove H3-ACCIDENT(16), or replace it with official-row activation certificates.
```

## Role

This ledger does not change the h=3 frontier gates.  Its purpose is to make
the T3 state machine-readable:

```text
h=2: external import closes all rows; in-house chain covers 2^23..2^41,
     with feasible exact-census accounting for 2^13..2^18 and residual
     in-house midrange 2^19..2^22.

h=3: conditional H3-ACCIDENT(16) covers every official row; the proof of that
     accident theorem remains open.
```

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_t3_constant_campaign_ledger.py
```

Expected digest:

```text
F3_T3_CONSTANT_CAMPAIGN_LEDGER_PASS
```
