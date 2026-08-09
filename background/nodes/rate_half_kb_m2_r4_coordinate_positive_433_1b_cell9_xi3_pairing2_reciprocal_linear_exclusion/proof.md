# Proof

After deleting `xi=3`, matching two groups the residual products as

```text
(de,de), (-de,sigma_c cf), (sigma_o ef,bf).
```

Here `sigma_c` is an anchor sign and `sigma_o` indexes its two target
lanes. If `A_i,B_i`, `i=0,1,2`, are the compact-kernel coefficient pairs
and `L_i(q)=B_i-q A_i`, the first equation factors as

```text
Pair(q,q) = 4 L_0(q) L_1(q)^2 L_2(q),    q=de.
```

Thus every finite solution is on one of three branches `q=B_i/A_i`.
Every denominator root enters the exceptional census. At direct replay,
`A_i=0,B_i!=0` is empty and `A_i=B_i=0` would be free; no free branch
occurs.

Write `m=df`, `s=(d+f)^2`, and put `z=1/d`. The source-product identity
becomes

```text
M(z) = 1 + (2m-s)z^2 + m^2 z^4 = 0,
e = qz,  f = mz.
```

The second paired equation is

```text
P(z) = Pair(-q,sigma_c c m z) = 0.
```

In the exact four-dimensional source algebra, division of `M` by `P`
leaves a linear remainder `R(z)=r_0+r_1 z` in every row. If
`P(z)=p_0+p_1 z+p_2 z^2`, every common root satisfies the division-free
cut

```text
r_1^2 p_0 - r_1 r_0 p_1 + p_2 r_0^2 = 0.
```

For four source signs, two anchor signs, three `q` branches, and six exact
source charts, the compiler norms this cut through the four-dimensional
tower. This gives 144 rows; each row owns the two target lanes
`(sigma_c,-1)` and `(sigma_c,1)`. Every candidate `r` is a deployed-field
root of the target norm or a retained denominator and inverse-guard
profile.

External FLINT replay reconstructs all field roots of 121 distinct
profiles as `gcd(P(x),x^p-x)`. It finds 716 roots in total, with maximum
profile degree 773. A separate streaming audit rebuilds every source point,
the quartic `M`, and the quadratic `P` directly. None of the 1,584 ordinary
checked routes has a common `z` root. Hence no `d=1/z`, `e=qz`, `f=mz`
lift reaches the final equation `Pair(sigma_o ef,bf)=0`.

The exact aggregate terminal census is

```text
target roots                         1584
candidate roots                      2760
source routes                        2304
missing-impossible points             144
missing-free regularized points       288
target-product boundaries             144
empty q branches                      144
ordinary checked routes              1584
common z roots                           0
z/d/e/f lifts                            0
nonzero final colored cuts               0
final-pair solutions                     0
```

The 144 `b`-leading and 288 `c`-leading exits lie on proved unit-ideal
tower boundaries. The 288 missing-free rows are exactly regularized base
points whose all-role unit certificates include pairing `2`, direct role
`xi=3`. Every product-zero target row is guarded boundary. No witness, free
branch, remote error, or unresolved stratum remains.

Finally, the universal orbit compiler maps `(3,2)` to exactly
`{(3,2),(4,2)}`. Both labels are empty. QED.
