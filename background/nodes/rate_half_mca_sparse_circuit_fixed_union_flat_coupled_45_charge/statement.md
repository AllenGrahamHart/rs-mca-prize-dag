# Fixed-union flat-coupled support-4/5 charge

- **status:** PROVED
- **correction dimension:** `10`
- **selected size:** `11`

Let `V<=F[X]_{<K}` have dimension ten and empty common zero set on an
`m`-point domain.  Let a fixed `g`-dimensional subspace `W<=V` vanish on a
fixed `u`-point set `D`.  Assume

```text
g>=5, R=K-u-g>=0, N=m-u>B=R+3, and K>=g+5.         (FU1)
```

For `d in {4,5}`, put

```text
L_d=C(u,d)+sum_(j=1)^(d-1)
    floor(C(u,d-j) C(N,j-1) R/j).                  (FU2)
```

Define

```text
X_4=min(floor(R C(N,3)/4),
        floor(R C(N,4)/(N-B))),
X_5=floor((R C(N,4)-(N-B)X_4)/5).                 (FU3)
```

If `I_4,I_5` are the selected-eleven-set incidences of the original
evaluation matroid's support-four and support-five circuits, then

```text
21 I_4+15 I_5
 <=21 (L_4+X_4) C(m-4,7)
   +15 (L_5+X_5) C(m-5,6).                        (FU4)
```

The circuits in `(FU4)` belong to the original evaluation matroid.  The
residual polynomial subspace certifies its flat-size bounds; circuits are
not transferred to the evaluation matroid of `W`.

## Falsifier

An original-matroid rank-three outside flat larger than `B`; a rank-four
outside flat larger than `B+1`; a lower inside/outside stratum omitted by
`(FU2)`; failure of endpoint monotonicity; or an admissible weighted census
above `(FU4)`.
