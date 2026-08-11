# Proof

Cycle 127 proves that a pair in the strict branch has no third supported
center on its endpoint codeword line. Thus the line contains exactly the two
endpoints.

Subtract that codeword line from the received pencil. Its joint support is
`U`. Every coordinate of `U` is a nonzero parameter-linear form, so it can
vanish at at most one endpoint. The two sets in `(SBR3)` are therefore
disjoint. Since

```text
|U_0|=3p-1,
|S_gamma|=rho-r_gamma=2p-r_gamma,                   (1)
```

we have

```text
|M_gamma|
 =|U_0|-(|S_gamma|-1)
 =(3p-1)-(2p-r_gamma-1)
 =p+r_gamma.                                        (2)
```

Summing `(2)` and subtracting from `|U_0|` proves `(SBR4)`.

For an off-line slope, minimum distance gives `(SBR5)`. If

```text
I_delta=S_delta intersect U_0,                      (3)
```

then expanding the union cardinality in `(SBR5)` gives

```text
|I_delta|=p-2-r_delta-a_delta.                      (4)
```

We sum `(4)`. Every point of `U_0` is light and belongs to exactly `e`
actual supports globally. The two line supports contribute

```text
(2p-r_alpha-1)+(2p-r_beta-1)=4p-2-r_A              (5)
```

incidences. Hence the actual off-line incidence on `U_0` is

```text
e(3p-1)-(4p-2-r_A).                                 (6)
```

The sum of the zero-excess capacities in `(4)` is

```text
(p-2)(3e+1)-(e-6-r_A).                              (7)
```

Subtract `(6)` from `(7)`. Using `p=(3e-1)/2`, the result is

```text
5p-6e+2=p.                                          (8)
```

This difference is exactly `sum a_delta`, proving `(SBR6)`. At most `p`
of the nonnegative integer excesses can be positive, so `(SBR7)` follows.

Fix a zero-excess slope. Because its assigned center is not on `c^L`, the
codeword `g_delta` in `(SBR8)` is nonzero. The affine received-line identity
shows that it is supported inside `U union S_delta`. That union has size
`2rho+1`; RS minimum distance forces support equality and `(SBR9)`.

Finally the off-line deficit sum is `e-6-r_A`. No more than this many
off-line slopes can have positive deficit. Removing them from the at least
`p+2` zero-excess slopes leaves `(SBR10)`. The official substitutions are
direct. QED.
