# Proof

Write `m=df`, `s=(d+f)^2`, `z=1/d`, and `q=de`. The source-product
identity is

```text
1+(2m-s)z^2+m^2z^4=0.
```

Matching 11 imposes the two quadratic equations

```text
Pair(q,bf)=0,
Pair(q,sigma_c*cf)=0.
```

Their Sylvester resultant eliminates `q`. Substitution of `f=mz`, followed
by the even/odd sign-free norm in `z`, gives a sixth-degree target before
reduction. Reducing modulo the missing quartic leaves a cubic sign-free cut;
the final pair leaves a linear remainder. The exact compiler norms these
division-free cuts through each four-basis source chart.

The full cover has four source signs, two `sigma_c` lanes, and six charts:
48 rows. Each row checks both `sigma_o` target lanes. External Frobenius-gcd
custody reconstructs 69 distinct norm/guard profiles, 312 deployed roots,
and degrees through 4,732.

An independent direct replay rebuilds 824 candidate roots and all 672
guarded source routes. It reconstructs all 1,440 field roots of the missing
quartics, recovers `d=1/z` and `f=mz`, and directly intersects the two
quadratic pair cuts in `q`. The intersections contain 144 common `q` roots.
Reconstructing `e=qz` gives 144 exact candidates, and both final `sigma_o`
lanes are then evaluated as `Pair(-q,sigma_o*ef)`. All 288 final-pair cuts
are nonzero.

The aggregate terminal census is

```text
target roots                          528
candidate roots                      824
source routes                        672
missing-impossible points             48
missing-free regularized points       96
target-product boundaries             48
ordinary checked routes              480
missing-quartic z roots              1440
z/d/f lifts                          1440
q intersections                      1440
common q roots                        144
final target-lane checks              288
final-pair solutions                    0
```

The 48 `b`-leading and 96 `c`-leading exits lie on proved tower boundaries;
the 96 missing-free rows are owned by the proved regularized-base packet.
No witness, free branch, remote error, or unresolved stratum remains.

Universal transport maps `(3,11)` to exactly
`{(3,11),(3,14),(4,11),(4,14)}`. All four labels are empty. QED.
