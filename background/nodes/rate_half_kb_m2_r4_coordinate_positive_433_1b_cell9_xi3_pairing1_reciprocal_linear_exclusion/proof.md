# Proof

After deleting `xi=3`, the residual product list is

```text
de, de, -de, sigma_o ef, bf, sigma_c cf.
```

Matching one is

```text
(de,de), (-de,bf), (sigma_o ef,sigma_c cf).
```

If `A_i,B_i`, `i=0,1,2`, are the compact-kernel coefficient pairs and
`L_i(q)=B_i-q A_i`, the first equation factors as

```text
Pair(q,q) = 4 L_0(q) L_1(q)^2 L_2(q).
```

Thus every finite `q=de` solution is on one of three branches
`q=B_i/A_i`. All denominator roots enter the exceptional census. At direct
replay, `A_i=0,B_i!=0` is empty and `A_i=B_i=0` would be free. No free
branch occurs.

Write `m=df`, `s=(d+f)^2`, and put `z=1/d`. Then

```text
M(z) = 1 + (2m-s)z^2 + m^2 z^4 = 0,
e = qz,  f = mz.
```

The second paired equation is the quadratic

```text
P(z) = Pair(-q,bmz) = 0.
```

In the exact four-dimensional source algebra, division of `M` by `P`
leaves a linear remainder `R(z)=r_0+r_1 z` in every row. If
`P(z)=p_0+p_1 z+p_2 z^2`, every common root satisfies the division-free
cut

```text
r_1^2 p_0 - r_1 r_0 p_1 + p_2 r_0^2 = 0.
```

For four source signs, three `q` branches, and six exact source charts, the
compiler norms this cut through the four-dimensional tower. This gives 72
rows, each of which checks all four target colors. Every candidate `r` is a
deployed-field root of the target norm or a retained denominator and
inverse-guard profile.

External FLINT replay reconstructs all field roots of 121 distinct profiles
as `gcd(P(x),x^p-x)`. It finds 708 roots in total, with maximum profile
degree 768. A separate streaming audit rebuilds every source point, the
quartic `M`, and quadratic `P` directly. For each common nonzero `z`, it
recovers `d=1/z`, `e=qz`, `f=mz`, verifies the first two pair equations,
and checks `Pair(sigma_o ef,sigma_c cf)` in all four target lanes.

The exact aggregate terminal census is

```text
target roots                          744
candidate roots                      1332
source routes                        1296
missing-impossible points              72
missing-free regularized points       144
target-product boundaries              72
empty q branches                       72
ordinary checked routes               936
common z roots                         144
z/d/e/f lifts                          144
nonzero final colored cuts             576
final-pair solutions                     0
```

The 72 `b`-leading and 144 `c`-leading exits lie on proved unit-ideal tower
boundaries. The 144 missing-free rows are exactly regularized base points
whose all-role unit certificates include pairing `1`, direct role `xi=3`.
Every product-zero target row is guarded boundary. No witness, free branch,
remote error, or unresolved stratum remains.

Finally, the universal orbit compiler maps `(3,1)` to exactly the two
labels printed in the statement. Both are empty. QED.
