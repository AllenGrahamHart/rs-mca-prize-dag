# Proof

Write `m=df`, `s=(d+f)^2`, `z=1/d`, and `q=de`. The source-product
identity is

```text
1+(2m-s)z^2+m^2z^4=0.
```

Matching 5 first imposes the antipodal biquadratic

```text
Pair(q,-q)=0.
```

For fixed `sigma_c`, the second pair is
`Pair(q,sigma_c*cf)=0`. Eliminating the sign of `q`, reducing the
resulting nested polynomial modulo the antipodal equation, and then reducing
its sign-free `z` cut modulo the missing quartic leaves a linear remainder
in the exact four-basis source tower. The compiler norms its division-free
common-root cut through each exact chart.

The full cover has four source signs, two `sigma_c` lanes, and six charts:
48 rows. Each row checks both `sigma_o` target lanes. External
Frobenius-gcd custody reconstructs 69 distinct norm/guard profiles, 328
deployed roots, and degrees through 6,236.

An independent direct replay rebuilds 1,016 candidate roots and all 1,152
guarded source routes. It reconstructs all 2,976 field roots of the missing
quartics, recovers `d=1/z` and `f=mz`, and directly intersects the
antipodal quartic with the second-pair quartic in `q`. The intersections
contain 288 common `q` roots. Reconstructing `e=qz` gives 288 exact
candidates, and both final `sigma_o` lanes are then evaluated directly.
All 576 final-pair cuts are nonzero.

The aggregate terminal census is

```text
target roots                          576
candidate roots                     1016
source routes                       1152
missing-impossible points              48
missing-free regularized points        96
target-product boundaries              48
ordinary checked routes               960
missing-quartic z roots               2976
z/d/f lifts                           2976
q intersections                       2976
common q roots                         288
final target-lane checks               576
final-pair solutions                     0
```

The 48 `b`-leading and 96 `c`-leading exits lie on proved tower
boundaries; the 96 missing-free rows are owned by the proved
regularized-base packet. No witness, free branch, remote error, or unresolved
stratum remains.

Universal transport maps `(3,5)` to exactly
`{(3,5),(3,12),(4,5),(4,12)}`. All four labels are empty. QED.
