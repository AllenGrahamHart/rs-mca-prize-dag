# Proof - L1 marked common-pencil CRT fiber bound

The full locators `P-a_i` are pairwise coprime, so their divisors `S_i` are
pairwise coprime. The polynomial Chinese remainder theorem gives one residue
class modulo

```text
S=product_i S_i
```

satisfying `(CF3)`, and a unique representative `W_0` of degree below
`deg S`. Therefore every solution is `W_0+SH`. If `H` is nonzero, monicity
of `S` and `deg W_0<deg S` give

```text
deg(W_0+SH)=deg S+deg H.
```

This proves `(CF4)` and the exact affine-fiber dimension.

The proved Forney window gives `t>=m`. Suppose first that `t>=m+1`. From
`v<=p` and `(CF1)`,

```text
deg S=t ell-v
     >=(m+1)ell-p
     >d.                                                (1)
```

No nonzero `H` can then occur, so at most one degree-at-most-`d`
representative survives.

It remains to take `t=m`. Write `d=m ell+eta`; the strip condition gives
`eta>=1`. If the dense supports have total deficit `v`, all sparse supports
outside them have total size at most `p-v`. Hence total petal agreement is at
most

```text
h<=m ell-v+(p-v)<=m ell+p.                              (2)
```

The weaker last bound is enough. The exact list threshold and maximality
`r<=ell-1` give

```text
d<=h+r-ell<=m ell+p-1.                                 (3)
```

Thus `eta<=p-1`. Since `deg S=m ell-v`,

```text
d-deg S=eta+v<=2p-1,
```

proving `(CF5)`. A polynomial `H` of degree at most `eta+v` has exactly
`q^(eta+v+1)` possible coefficient vectors, which proves `(CF6)`.

For fixed `p<=P`, this is at most `q^(2P)`. The generated-field hypothesis
turns it into a fixed polynomial in `n`. Finally, the canonical marked-pencil
reduction reconstructs the listed codeword from the fixed chart, `F`, and
`W`, so no further multiplicity remains. This proves the claim.
