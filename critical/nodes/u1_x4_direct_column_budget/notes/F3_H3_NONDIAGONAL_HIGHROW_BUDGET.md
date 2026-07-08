# F3 h=3 optional non-diagonal high-row budget lift

Status: OPTIONAL CONDITIONAL ARITHMETIC COMPILER, NOT `RC-RANK` AND NOT
`H3-ACT`.

This packet extends the non-diagonal bridge-budget pass from
`F3_H3_NONDIAGONAL_LOWROW_BUDGET.md` to the next high official rows
`s = 36..39`.  It is intentionally not included in the aggregate interim replay:
the default gate is already close to the local 60-second comfort limit, and
this optional check is useful without making that gate heavier.

## Pre-registration

Question:

```text
For s = 36..39, do the same non-diagonal Stepanov boxes enlarge the conditional
bridge family size |Z| under RC-RED(13) + RC-RANK?
```

Success criterion:

- use the exact same integer inequalities and `B <= 50000` search cap as the
  low/mid-row non-diagonal packet;
- verify a pinned passing witness `(A,B,D)` at the improved `Z`;
- exhaustively scan `Z+1` over the same non-diagonal search box;
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
```

For each row, the verifier checks that the improved `Z` passes and `Z+1` fails
inside the stated non-diagonal search box.  By monotonicity in `Z`, this proves
maximality inside `B <= 50000` for these four high rows.

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
```

Expected digest:

```text
H3_NONDIAGONAL_HIGHROW_BUDGET_PASS
```
