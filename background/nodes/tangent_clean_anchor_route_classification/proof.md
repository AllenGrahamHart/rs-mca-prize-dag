# Proof

By `rs_tangent_flexible_budget_unsafe_floor`, agreement `a` supplies
`e=n-a` distinct bad slopes. At target `2^-128`, this is a strict unsafe
certificate precisely when

```text
e > floor(q/2^128).
```

For positive integers, the floor inequality is equivalent to

```text
q < e*2^128,
```

and hence to `q<=e*2^128-1`. Substituting each pinned `(n,a)` pair gives the
six printed cutoffs.

At the RowC envelope, `B*=2^122`, while every listed `e` is below `2^10`.
At the prize envelope, the printed `B*` has 128 bits, while every listed `e`
is below `2^41`. Therefore `e>B*` fails on all six named anchors.

The equivalence also proves the positive branch: for every actual field order
at or below the row cutoff, the tangent construction gives more than `B*`
bad slopes at the predecessor. No converse safety statement is used.
