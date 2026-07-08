# F3 h=3 private-linear resultant degree guard

Status: PROVED GUARDRAIL, NOT THE PRIVATE-LINEAR RANK THEOREM.

The two-factor resultant packet explains a small-H rank loss: for

```text
u = ((X-alpha)/(X-beta))^H,
v = ((X-gamma)/(X-delta))^H,
```

eliminating `X` gives a relation of bidegree `(H,H)` in `u,v`.  At
`H=2,B=3`, this relation lies inside the `0<=i,j<B` exponent box and causes the
rank drop from `9` to `8`.

This packet checks that the same obstruction is outside every official
private-linear compiler box.

## Resultant Profile

The replay verifies symbolically for `H=1,2,3` that

```text
Res_X((X-alpha)^H-u(X-beta)^H,
      (X-gamma)^H-v(X-delta)^H)
```

has bidegree `(H,H)` and `(H+1)^2` monomials in `u,v`.

Thus the known two-factor resultant relation can be supported inside a
`B x B` exponent box only if

```text
B - 1 >= H.
```

## Official Private-Linear Boxes

For every row in the retuned official private-linear compiler,

```text
H = n = 2^s,  13 <= s <= 41.
```

The replay checks both the passing `Z_private` witness and the stored
`Z_private+1` failure witness.  In every case,

```text
B - 1 < H.
```

The smallest margins are:

```text
passing witness:       H - (B-1) >= 8128
next-failure witness:  H - (B-1) >= 8129
```

So the small-H bidegree-resultant loss is not literally present in the
official private-linear boxes.

## Consequence

This does not prove the private-linear rank theorem.  It only separates the
known structural two-factor obstruction from the official parameter regime.
The remaining private-linear theorem still needs finite-row minor
nonvanishing on the three-parameter normal-form image, plus the matching
rank-capacity bridge.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_resultant_degree_guard.py
```

Expected digest:

```text
H3_PRIVATE_LINEAR_RESULTANT_DEGREE_GUARD_PASS
```
