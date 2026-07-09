# F3 h=3 conic rational-curve multiplication interface

Status: PROOF-INTERFACE LEDGER, NOT `RC-RANK`.

This packet restates the conic binary-form rank target as a multiplication map
on `P^1`.

## Multiplication Map

For a same-fiber conic chart, set

```text
R_U = P_U^H,  R_V = P_V^H,  R_W = P_W^H,  R_Q = Q^H.
```

These are four sections of

```text
O(2H)
```

on `P^1`.  With

```text
M = 3(B-1),
```

the cleared rank columns are exactly

```text
X^a R_U^b1 R_V^b2 R_W^b3 R_Q^(M-b1-b2-b3),

0 <= a < A,   0 <= b_i < B.
```

Thus the conic rank theorem is a statement about the image of

```text
H0(O(A-1)) * boxed degree-M monomials in <R_U,R_V,R_W,R_Q>
  -> H0(O((A-1)+2HM)).
```

The box restriction `0 <= b_i < B` is part of the theorem.  Replacing it by the
full simplex would be a different, easier problem.
The companion dual-annihilator target rewrites the same theorem as a bound on
the coefficient functionals that kill all boxed shifted products.

## Official Arithmetic

For every official exact-profile row `s=13..41`, the replay verifies:

```text
box column count      > target dimension,
full simplex count    > target dimension,
linear-normality defect of the four O(2H) generators is positive.
```

The first two checks say there is no naive dimension-count obstruction.  The
last check says the four generators are not a complete linear series:

```text
h0(O(2H)) - 4 = 2H - 3 > 0.
```

So the proof cannot simply invoke the complete binary-form multiplication map
for `O(2H)`.  It must prove that this particular boxed subalgebra still has
codimension at most the official allowance:

```text
codim <= 1847.
```

The tight column-supply row is again `s=13`.

## Role

This interface separates three issues:

```text
1. span rank of P_U,P_V,P_W,Q as quadratics        already pinned;
2. dimension supply of the official boxed columns  proved here;
3. finite-field nonvanishing/codimension <=1847    still open.
```

It also prevents a false shortcut: the conic rank theorem is not a direct
consequence of normal generation of the complete `O(2H)` series, because only
four sections of `O(2H)` are available.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_rational_curve_interface.py
```

Expected digest:

```text
H3_CONIC_RATIONAL_CURVE_INTERFACE_PASS
```
