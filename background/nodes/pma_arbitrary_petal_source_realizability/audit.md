# Audit - PMA arbitrary-petal maximal-source realizability

## Hypothesis Audit

| hypothesis | use | failure mode if removed |
|---|---|---|
| `|C|=k-1` | puts `c_iL_C` in the code and gives the exact threshold | a smaller core is below threshold |
| `c_i!=0` | prevents agreement on the zero background | the zero word gains background agreements |
| distinct `c_i` | prevents cross-petal agreements | equal labels merge petals |
| disjoint petals | makes pairwise intersections exactly the core | overlap enlarges the sunflower core |
| `b<ell` | proves packing maximality | `ell` unused points form another petal |

No interpolation theorem, smoothness property, quotient profile, or field
extension is used. The construction is a direct evaluation identity.

## Consumer-Backward Audit

The result blocks only this inference:

```text
maximal sunflower source  ==>  all petal locators are P-a_i.
```

That implication is false even on `F_17^*`. The result does not construct a
post-owner residual word touching three of four petals, so it does not
falsify `petal_mixed_amplification` and does not prevent a contributor-specific
rechart theorem.

The correct next alternatives are:

1. rechart every particular below-band residual into a common locator pencil,
   with bounded first-match multiplicity; or
2. count the arbitrary-locator fiber-pencil system directly.

## Required-to-Trip Mutations

The verifier checks that repeated labels create cross-petal agreement, a zero
label creates background agreement, `b=ell` leaves room for another petal,
and reducing the core by one loses the PMA agreement threshold.
