# Proof

Let `C` be a target support-`d` circuit and put `j=|C\D|`.

The `j=0` stratum has at most `C(u,d)` supports. Assume `j>=1` and delete
one of the `j` outside points. The remaining set `A` is independent, has
`d-j` points in `D`, and has `j-1` points outside `D`. Since every
polynomial in `W` already vanishes on `D`, only those `j-1` outside
evaluations can cut `W`. Therefore

```text
dim(W intersect H_A) >= g-(j-1)=g-j+1.             (1)
```

When `j<=g`, this is positive. The intersection vanishes on `D` and on the
complete carrier of `A`. The common-root bound gives at most

```text
K-(g-j+1)-u
```

carrier points outside `D`. Of these, `j-1` are already in `A`, so at most

```text
K-g-u                                                   (2)
```

outside completions remain. The global completion maximum gives `M_d` in
every stratum. Taking the smaller bound for `j<=g`, and only `M_d` for
`j>g`, proves `(CS1)`.

There are at most

```text
C(u,d-j) C(m-u,j-1)
```

exposed deletions in the `j`-th stratum. Each circuit is exposed once for
each of its `j` outside points. Multiplication by `B_j`, division by `j`,
integer flooring, and summation prove `(CS2)`.

For the parallel-class refinement, an independent deletion contains at most
one point of that class. A minimal circuit of support at least three also
contains at most one, since two such points already form a support-two
circuit. The number of eligible inside `r`-sets is therefore at most
`I_b(u,r)`, proving `(CS3)`. Finally, every circuit support extends to at
most `C(m-d,11-d)` selected eleven-sets. QED.
