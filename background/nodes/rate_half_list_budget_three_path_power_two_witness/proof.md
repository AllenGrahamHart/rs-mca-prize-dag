# Proof

All arithmetic is in `F_17`. Direct evaluation of the four printed
polynomials against `u` gives the supports

```text
S_0={4,5,6,7,8,9,10,11,12,13,15},
S_1={1,2,3,6,7,8,10,11,13,15,16},
S_2={1,2,3,4,5,6,9,10,11,12,16},
S_3={1,2,3,4,5,7,8,12,13,14,15}.
```

Each set has size eleven. Reading the membership labels coordinate by
coordinate gives exactly the four triple blocks, two edge points, and one
singleton printed in the statement. In particular, every pair intersection
has size at most `k-1=7`, as required for distinct degree-less-than-eight
polynomials.

The monic triple-block locators, again in ascending coefficient order, are

```text
A_0=(11,11,11,1),
A_1=(15,9,13,1),
A_2=(6,12,8,8,1),
A_3=(3,15,7,1).
```

With `r=9` and `s=16`, direct coefficient comparison gives

```text
8 A_2 + 13 (X-16) A_0 = 4 (X-9) A_1,
8 A_3 + 10 A_0 = A_1.                              (1)
```

These are precisely the two path-pencil identities. The Plucker identity
then gives `q_23=15+14X`. Multiplying `(1)` by the complementary block
locators recovers

```text
f_1-f_0 = 8 A_2 A_3,
f_2-f_0 = 4 (X-9) A_1 A_3,
f_3-f_0 = A_1 A_2,
```

and the other three pair differences have the required path factors.

Finally, form the intersection matrix by writing the equal-value equations at
each selected coordinate after subtracting `f_0`. Exact Gaussian elimination
over `F_17` gives rank `23` in `24` columns. The concatenated coefficient
vector of `(f_1,f_2,f_3)` is a nonzero kernel vector. The verifier performs
all evaluations, factor identities, incidence checks, and row reduction from
the printed data. QED.
