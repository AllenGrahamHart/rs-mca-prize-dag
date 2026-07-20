# Proof - L1 marked common-pencil next-strip boundary fiber bound

Let `h` be the total petal agreement count and `r` the background agreement
count. Dense petals contribute at most `t ell`; replacing each exact support
by its dense/empty baseline changes the total by at most the polarized entropy
`p`. Hence

```text
h<=t ell+p.                                             (1)
```

The exact list threshold and maximal background remainder give

```text
d<=h+r-ell<=h-1<=t ell+p-1.                            (2)
```

Suppose `t<=m`. From `(NB2)` and `(2)` one would obtain

```text
(m+1)ell-g=d<=m ell+p-1,
ell<=p+g-1<=2p-1<=2P_0-1,
```

contradicting `ell>2P_0`. Therefore `t>=m+1`, proving `(NB3)`.

The selected support locators are pairwise coprime, so the congruences in
`(NB4)` determine one residue class `W_0 mod S`, with `deg W_0<deg S`.
Every degree-at-most-`d` solution is uniquely

```text
W=W_0+SH.
```

Using `t>=m+1` and `(NB2)`,

```text
d-deg S
 <=(m+1)ell-g-((m+1)ell-v)
 =v-g.                                                  (3)
```

If `v<g`, then `deg S>d` and only the reduced representative can occur. If
`v>=g`, equation `(3)` leaves at most `v-g+1` free coefficients in `H`, so
there are at most `q^(v-g+1)` solutions. Since `g>=1` and `v<=p`,

```text
v-g+1<=v<=p,
```

which proves `(NB5)`.

