# F3 h=3 conic-chart linear-relation guard

Status: PROVED ALGEBRAIC GUARDRAIL, NOT `RC-RANK`.

This packet records why a tempting rank proof for same-fiber conic charts is
false.  The conic-chart numerator divisors can be pairwise coprime while the
three coordinate functions still satisfy a linear affine relation.

## Relation

For the same-fiber conic chart

```text
U(t)=P_U(t)/Q(t),
V(t)=P_V(t)/Q(t),
W(t)=P_W(t)/Q(t),
```

the ordered triples lie in the fiber with elementary sum `-a`, so

```text
U(t) + V(t) + W(t) = -a.
```

After clearing the common denominator this is the polynomial identity

```text
P_U + P_V + P_W + a Q = 0.
```

The replay checks this identity on the pinned same-fiber conic chart

```text
p=769, a=37, b=706, base=(101,333).
```

It also verifies that the four quadratics `P_U,P_V,P_W,Q` are pairwise
coprime over `F_769`.  Thus the rank deficits in the conic-chart guardrails
are not explained by shared roots.

## Consequence

A proof route based only on separated numerator/denominator divisors is not
strong enough.  The actual conic rank theorem must handle the affine-plane
relation among the three coordinate functions.  This is consistent with the
existing rank data:

```text
degree-space guard cases: 7, failures: 4, max deficit: 46
official-ratio pilot cases: 6, failures: 4, max deficit: 69
```

The exact-profile route remains viable because it only needs rank above
`C_exact=DA+6D(D-1)`, or equivalently a bounded-deficit theorem with
`Delta <= 1847` on the official boxes.  But that theorem must be proved in the
presence of this linear relation.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_chart_linear_relation_guard.py
```

Expected digest:

```text
H3_CONIC_CHART_LINEAR_RELATION_GUARD_PASS
```
