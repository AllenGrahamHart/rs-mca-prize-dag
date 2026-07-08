# F3 h=3 RC-RANK small-H guardrail

Status: VERIFIED GUARDRAIL / ROUTE CUT, NOT `RC-RANK`.

This packet records a small but important correction to the future h=3
`RC-RANK` theorem statement.  The rank target cannot be stated uniformly down
to tiny subgroup orders, even after the constant-ratio degeneracy has been
removed.  The theorem needs an explicit lower floor on the subgroup order
`H`, or it must route those rows to finite certificates.

## Pre-registration

Question:

```text
Can the current non-collapsed private-divisor toy curve satisfy RC-RANK
uniformly for very small H?
```

Success criterion:

- reuse the private-divisor curve from the rank-stress packet;
- vary only the subgroup order `H` in the same finite field and Stepanov box;
- show both failure and later success of the exact `RC-RANK` inequality;
- keep the conclusion as a theorem-statement guardrail, not as a proof of
  large-`H` rank.

Failure criterion:

- confuse tiny-`H` failure with an official-row obstruction;
- weaken the degeneracy filters;
- treat eventual full rank in the sample as a proof of `RC-RANK`.

## Toy Family

The verifier uses the same finite field and Stepanov box as the rank-stress
packet:

```text
p = 769, A = 5, B = 4, D = 1,
conditions = 13 D (A + D) = 78,
coefficients = A B^3 = 320.
```

The non-collapsed private-divisor curve is

```text
(X-2)/(X-3), (X-5)/(X-7), (X-11)/(X-13).
```

Only the subgroup order `H` changes.  The exact ranks are:

```text
H=4:  rank 41   degree_dim 41   fails RC-RANK
H=8:  rank 77   degree_dim 77   fails RC-RANK by one
H=16: rank 149  degree_dim 149  passes with capacity 1
H=32: rank 293  degree_dim 293  passes with capacity 3
H=64: rank 320  degree_dim 581  full coefficient rank, capacity 4
```

The verifier also checks the exact model formula

```text
rank = min(A B^3, A + 3H(B - 1))
```

for this private-linear control.  Thus the rank deficit here is not mysterious:
before the coefficient box fills, it is exactly the one-variable degree-space
dimension of the cleared products.

Thus private divisors plus non-collapse are still not enough for a uniform
small-`H` `RC-RANK` theorem.  The large-row theorem should print the required
`H` floor explicitly.  This does not damage the official F3 rows, whose active
row sizes start at `2^13`; it prevents an overbroad theorem statement from
being smuggled into the dossier.

## Replay

Focused replay only; this is intentionally not added to the default aggregate
replay because the aggregate is already near the local 60-second cap.

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rc_rank_hfloor_guard.py
```

Expected digest:

```text
H3_RC_RANK_HFLOOR_GUARD_PASS
```
