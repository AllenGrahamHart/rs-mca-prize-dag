# Proof

Comparing coefficients of `X^i` in `(PMG2)` gives

```text
h_i(delta)=zeta_delta f_(i,delta).                  (1)
```

Each `h_i` has degree at most `m`, so its evaluation vector on `Z` belongs
to `RS[F,Z,m+1]`. This proves `(PMG3)`.

The dual-GRS parity checks for this code are

```text
sum_(delta in Z) v_delta delta^l/L_Z'(delta)=0,
0<=l<=C-m-2.                                       (2)
```

Indeed, if `v_delta=h(delta)` with `deg h<=m`, then the numerator in `(2)`
has degree at most `C-2`, and the Lagrange leading-coefficient identity
makes the sum zero. There are `C-(m+1)` independent checks, so they
characterize the code. Substituting `(1)` into `(2)` yields

```text
Kpar zeta=0.                                        (3)
```

The root polynomial is monic, so `f_(n,delta)=1` and `(1)` gives
`zeta_delta=h_n(delta)`. Dividing the other coefficient identities by this
nonzero value proves `(PMG5)`.

The paired padded-fiber factorization supplies at least `2e` extremal
fibers of exact degree `p-3`. Select any `C=2e` of them. The checks per
coefficient are

```text
C-(m+1)=2e-(e-1)=e+1,                              (4)
```

and there are `n+1=p-2` coefficient indices. This proves `(PMG6)`.

At the strict boundary, select the guaranteed `C=p+2` exact-degree fibers.
The checks per coefficient are

```text
C-(m+1)=(p+2)-e=p+2-e,                             (5)
```

and there are `n+1=p-1` coefficient indices. This proves `(PMG7)`.
Substituting the official `e=183251937963` and `p=274877906944` gives
`(PMG8)`. QED.
