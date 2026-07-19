# F3 h=3 conic boxed-product basepoint-free guard

Status: PROVED LOCAL GEOMETRIC GUARDRAIL, NOT `RC-RANK`.

This packet closes the basepoint-free prerequisite used by the conic
kernel-bundle reduction, under the repaired conic-chart pairwise-coprimality
condition.

## Statement

Let `P_U,P_V,P_W,Q` be pairwise coprime binary forms, and let `B >= 2`.  Put

```text
M = 3(B-1).
```

Then the boxed product series

```text
W = span{P_U^(H b1) P_V^(H b2) P_W^(H b3) Q^(H(M-b1-b2-b3))
         : 0 <= b_i < B}
```

has no common base point on `P^1`.

## Proof

At any point of `P^1`, pairwise coprimality implies that at most one of
`P_U,P_V,P_W,Q` vanishes.

If `P_U` vanishes, choose `b1=0`; then the `P_U` factor is absent.  The same
argument applies to `P_V` and `P_W`.

If `Q` vanishes, choose

```text
b1=b2=b3=B-1.
```

Then `b1+b2+b3=M`, so the `Q` exponent is zero.  Since no other factor
vanishes at the point, this boxed product is nonzero there.

Thus for every point there is at least one boxed product not vanishing at that
point, so `W` is basepoint-free.

## Replay

The replay verifies the already-banked same-fiber conic chart has six pairwise
gcd checks with maximum gcd degree `0`, and that every official exact-profile
row has `B>=34`.

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_box_basepoint_free.py
```

Expected digest:

```text
H3_CONIC_BOX_BASEPOINT_FREE_PASS
```
