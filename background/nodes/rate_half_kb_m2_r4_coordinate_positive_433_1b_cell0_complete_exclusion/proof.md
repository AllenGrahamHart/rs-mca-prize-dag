# Proof

The product-rank-drop complete-exclusion dependency removes every common
packet with product-row rank at most four, including cell `0`.  It remains
to treat product rank five.

Product rank five is covered by the six maximal-cofactor charts.  The chart
certificate contains every Cartesian-product row

```text
cell 0 * four source-sign rows * six charts.
```

The mixed-sign rows are unit.  For either equal source sign `s`, all six
charts have the same seven localization-free basis generators.  The first
generator factors as

```text
c^2+b^2=(c-s i b)(c+s i b).
```

The second is `(c-s i b)(r-b)`.  If `c=-s i b`, the first factor is
nonzero under the odd-characteristic and `b!=0` guards, so `r=b`.  If
`c=s i b`, substitution in the third generator gives `b(br-1)`; hence
`r=b^(-1)`.  The sixth generator is

```text
xr+alpha_s x+alpha_s r^2+s i r.
```

Substitution of the two values of `r`, followed in the first branch by
multiplication by `b^2`, gives exactly the two relations in `(KBP1BC0-4)`.
Thus every guarded equal-sign principal common point lies in `A_s` or
`B_s`.  No converse or radical-ideal equality is needed.

For each family the component compiler computes a division-free projective
kernel `(A_2,A_0,B_1)` and reduces all ten common rows to zero modulo the
component relation.  The outside ledger then uses the same exhaustive
necessary placement argument as the proved rank-drop outside ledger: pick
the outside record at the missing singleton mate, then one of the fifteen
perfect matchings of the residual six source labels.  The complete Vieta
equations supply the missing-product and squared-sum equations, and each
residual deck pair supplies one paired-product resultant.

The ledger is deliberately a superset of actual placements.  In every one
of the 1680 cases, sequential saturation by all unique nonconstant source,
denominator, leading-support, and target-distinctness guards ends at
dimension `-1`, basis size one, with basis `1`.  Therefore neither
component admits an outside target.  The principal branch is empty, and
the rank-drop dependency completes cell `0`. QED.
