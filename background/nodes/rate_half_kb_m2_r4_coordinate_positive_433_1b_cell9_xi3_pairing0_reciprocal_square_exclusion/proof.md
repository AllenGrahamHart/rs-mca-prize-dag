# Proof

After deleting `xi=3`, the residual product list is

```text
de, de, -de, sigma_o ef, bf, sigma_c cf.
```

Matching zero pairs adjacent entries. If `A_i,B_i`, `i=0,1,2`, are the
three compact-kernel coefficient pairs and `L_i(q)=B_i-q A_i`, direct
substitution gives

```text
Pair(q,q) = 4 L_0(q) L_1(q)^2 L_2(q).
```

Thus every finite `q=de` solution is on one of the three branches
`q=B_i/A_i`. Roots of each denominator are retained in the exceptional
root census. At direct replay, `A_i=0,B_i!=0` is empty; `A_i=B_i=0` would
be a free branch. No free branch occurs.

Write `m=df`, `s=(d+f)^2`, and put `y=1/d^2`. Then

```text
1 + (2m-s)y + m^2 y^2 = 0,
ef = q m y.
```

The outside-pair equation is the second quadratic

```text
Pair(-q, sigma_o q m y) = 0.
```

For each of four source signs, three `q` branches, two `sigma_o` values,
and six exact source charts, the compiler norms the division-free
quadratic resultant through the four-dimensional source tower. This gives
144 rows. Every candidate `r` is a deployed-field root of the target norm
or one of the retained denominator and inverse-guard profiles.

External FLINT replay reconstructs all field roots of 113 distinct
profiles as `gcd(P(x),x^p-x)`. It finds 644 roots in total, with maximum
profile degree 764. A separate streaming audit then rebuilds the source
points and both scalar quadratics directly. For each common nonzero `y`, it
enumerates every root of `d^2=1/y`, recovers `e=q/d`, `f=m/d`, and checks
both remaining `sigma_c` colors in `Pair(bf,sigma_c cf)`.

The exact aggregate terminal census is

```text
target roots                         1392
candidate roots                      2424
source routes                        1968
missing-impossible points             144
missing-free regularized points       288
target-product boundaries             144
empty q branches                      144
ordinary checked routes              1248
common y roots                         288
d/e/f lifts                            576
nonzero final colored cuts            1152
final-pair solutions                     0
```

The 144 `b`-leading and 288 `c`-leading exits lie on proved unit-ideal
tower boundaries. The 288 missing-free rows are exactly regularized base
points whose all-role unit certificates include pairing `0`, direct role
`xi=3`. Every one of the 144 product-zero target rows is guarded boundary.
No witness, free branch, remote error, or unresolved stratum remains.

Finally, the universal orbit compiler maps `(3,0)` to exactly the two
labels printed in the statement. Both are empty. QED.
