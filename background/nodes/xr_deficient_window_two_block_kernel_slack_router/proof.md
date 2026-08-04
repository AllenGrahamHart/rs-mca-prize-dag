# Proof

The primitive Pade router gives

```text
ell+g<=d-1.                                          (1)
```

The active-defect router gives `D subset G_d`. Every target has at least two
selected live slopes, whose active blocks are disjoint `r`-subsets of `D`.
Consequently

```text
2r<=e<=g<=d-ell-1=2r+sigma,                         (2)
```

which is `(TKS1)` and also proves `sigma>=0` whenever this branch is
nonempty.

If a target has `L` selected live slopes, its `L` active blocks are pairwise
disjoint, so

```text
Lr<=e<=2r+sigma.
```

When `sigma<r`, the right side is strictly below `3r`. Since `L>=2`, this
forces `L=2`. Their union has size `2r`, and `(2)` gives

```text
e-2r<=sigma,       g-2r<=sigma.
```

The blocks lie in `D subset G_d`, proving both assertions in `(TKS2)`.

For `(TKS3)`, the primitive router writes every kernel element as
`(SP,SQ)` and proves that every multiplier `S` vanishes on `G_d`. The points
of `G_d` are distinct, so their locator `Z_G` divides `S`. Write `S=Z_G U`.
Since `deg S<d-ell`,

```text
deg U<d-ell-g<=d-ell-2r=sigma+1.                    (3)
```

Multiplication by the nonzero pair `(P,Q)` and by `Z_G` is injective, so
the multiplier space has dimension at most `sigma+1`. Deficiency makes it
nonzero, giving `1<=dim K_d<=sigma+1`.

At the printed obstruction, substitute `r=2ell+1` and `d=h-r`:

```text
sigma=d-ell-1-2r=h-7ell-4.                          (4)
```

For `h=2^33+1`, division of `h-4` by seven has remainder five. For
`h=2^32+1`, it has remainder one. Hence `(4)` is respectively `5` and `1`.
Both are smaller than `r`, so the preceding conclusions apply and give
`(TKS4)`. QED.
