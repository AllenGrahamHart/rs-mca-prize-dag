# `A=1` quadratic gap-four correction marked-jet route fence

- **status:** PROVED
- **closure:** exact marked orders and abstract symmetric-pencil countermodel
- **consumer:** `rate_half_band_crossing_location`

The correction-quartic identity sharpens the marked determinants to

```text
double root:
det(M_1+tau nu_*nu_*^T)=c tau g_*^3S_B^8,          (MJF1)

two simple:
det(M_1+tau nu_1nu_1^T)=c_1 tau G_1^5G_2S_1^7S_2,
det(M_1+tau nu_2nu_2^T)=c_2 tau G_1G_2^5S_1S_2^7. (MJF2)
```

Thus an unshared simple correction root has marked determinant order eight
in the double-root arm and order seven on its own marked row in the
two-simple arm.

These orders do not contradict abstract symmetric affine-pencil geometry.
For every `eta>=3`, let `L_eta(z)` be the `eta by (eta+1)` bidiagonal
matrix whose row `i` has `-z` in column `i` and `1` in column `i+1`, and put

```text
K_eta(z)=[ 0       L_eta(z) ]
         [ L_eta(z)^T   0   ].                      (MJF3)
```

It has generic corank one and primitive kernel vector

```text
q(z)=(0,...,0,1,z,...,z^eta)^T.                    (MJF4)
```

Choose a constant marking `v` with `v^Tq=z^3`. Then

```text
M_8(z)=K_eta(z) direct_sum [[0,z],[z,1]]
```

has regular factor `-z^2` and

```text
det(M_8+tau vv^T)=c tau z^8.                       (MJF5)
```

Likewise

```text
M_7(z)=K_eta(z) direct_sum [z]
```

has regular factor `z` and

```text
det(M_7+tau vv^T)=c' tau z^7.                      (MJF6)
```

## Route fence

Symmetry, affine parameter dependence, generic corank one, one primitive
minimal-index block, the adjugate factorization, and marked determinant
multiplicity cannot exclude `(MJF1)--(MJF2)`. A valid exclusion must use
additional structure of the prize packet, such as the Hankel anti-diagonal
relations, the three-class contracted source, simultaneous split fibers,
or the received-word/Forney identities.
