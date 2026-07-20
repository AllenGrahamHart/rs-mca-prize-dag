# Audit

## Checked points

1. Both inequalities in `(NSB1)` are used; dropping `AB<=m` invalidates the
   discriminant argument.
2. All normalized parameters are positive, so every division preserves the
   strict inequality.
3. The floor is on the proof certificate, not on the actual affine
   intersection size.
4. The nodal product uses one order-`n` and one order-`3n` affine bound, so
   the factor is `C_1 C_3^2 3^(4/3)`.
5. The class-blind coefficient `17` is retained. Any improvement using the
   cheaper class, richness, or disjointness lies outside the barrier.
6. The live comparison is `76599/40`, not the historical stronger `892`.

The independent audit samples many exact rational feasible parameter tuples
and verifies the strict cubed form of `(NSB2)`.

## Weight-shortcut falsifier

The class-blind coefficient cannot simply be replaced by `10`. At the exact
control `(n,p)=(64,7937)`, nodal parameters `theta=3603`, `phi=7083` give
split triples

```text
(4337,2593,1010),       (3604,2595,1741)
```

with no positive or negative root collision and target `t=2596=1-853^2`.
Thus a signed-disjoint nodal antipodal record exists even when `p=2 mod 3`.
Its product richness is only `P(t)=10` and quotient weight is `R(t)=7`, so it
does not enter DSP8; it shows that any cheaper class payment must genuinely
use the `P>=25` cutoff rather than a false nodal-class exclusion.
