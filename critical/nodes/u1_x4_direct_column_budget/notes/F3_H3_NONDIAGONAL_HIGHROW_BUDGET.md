# F3 h=3 non-diagonal high-row budget lift

Status: CONDITIONAL ARITHMETIC COMPILER, NOT `RC-RANK` AND NOT `H3-ACT`.

This packet extends the non-diagonal bridge-budget pass from
`F3_H3_NONDIAGONAL_LOWROW_BUDGET.md` to the high official rows `s = 36..41`.
After the low/mid-row analytic-cap optimization, the aggregate interim replay
has enough margin to include this high-row check by default.

## Pre-registration

Question:

```text
For s = 36..41, do the same non-diagonal Stepanov boxes enlarge the conditional
bridge family size |Z| under RC-RED(13) + RC-RANK?
```

Success criterion:

- use the exact same integer inequalities as the low/mid-row non-diagonal
  packet;
- verify a pinned passing witness `(A,B,D)` at the improved `Z`;
- exhaustively scan `Z+1` up to the exact analytic `B` cap for any possible
  passing box;
- keep the result explicitly conditional on `RC-RANK` and the geometric
  batching contract.

Failure criterion:

- a printed witness fails either the coefficient count or rank-image cap;
- `Z+1` passes inside the declared search box;
- the packet is treated as a proof of the geometric bridge or of `H3-ACT`.

## Result

The optional high-row bridge-budget improvements are:

```text
s=36: 2337 -> 3400
s=37: 2944 -> 4284
s=38: 3710 -> 5397
s=39: 4674 -> 6800
s=40: 5889 -> 8568
s=41: 7420 -> 10795
```

For each row, the verifier checks that the improved `Z` passes and `Z+1` fails
over the whole possible `B` range for a passing box.  The exact caps used for
the `Z+1` scans are:

```text
s=36: B <= 19499
s=37: B <= 24568
s=38: B <= 30962
s=39: B <= 39010
s=40: B <= 49146
s=41: B <= 61923
```

The cap follows from the shared compiler inequality in
`F3_H3_NONDIAGONAL_LOWROW_BUDGET.md`.  By monotonicity in `Z`, the passing `Z`
and complete `Z+1` failure prove maximality for these six high rows under the
non-diagonal compiler inequalities, not merely inside the default
`B <= 50000` box.

## Interpretation

This reduces the high-row geometric batching burden in the same conditional
sense as the low/mid-row packet.  It still leaves the two h=3 proof gates
unchanged:

```text
RC-RANK
H3-BRIDGE(Z_budget)
```

No red node closes from this packet alone.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_nondiagonal_highrow_budget.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_flip_interim_report_replay.py
```

Expected digest:

```text
H3_NONDIAGONAL_HIGHROW_BUDGET_PASS
F3_FLIP_INTERIM_REPORT_REPLAY_PASS
```
