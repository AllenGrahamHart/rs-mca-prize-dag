# Rank-eleven heavy-plane minimal-field stratification fence

- **status:** PROVED
- **scope:** the official KoalaBear sextic row and the proved heavy Segre
  bucket

Let `B` be the domain-generated base field and let `F/B` be the deployed
extension of degree six. For each used projective factor `[g]`, form the
projective datum

```text
x_g=(P,Q,[g]),
```

where `P,Q` are regarded as Grassmannian points through their Plucker
coordinates. The coefficient ratios of `x_g` generate a unique minimal
field `K_g` over `B`. Its relative degree satisfies

```text
e_g=[K_g:B] in {1,2,3,6}.                              (MF1)
```

Partition the first-owned factor masses by `e_g`. One degree stratum has
mass at least

```text
ceil(9965407986/4)=2491351997.                         (MF2)
```

Since each fixed projective factor owns at most `R_2=248644099`, that
stratum uses at least 11 factors:

```text
10 R_2=2486440990<2491351997.                          (MF3)
```

The `e=1` output is base-rational. The other outputs are exactly the
quadratic, cubic, and full sextic minimal-field branches.

Automatic selection of `e=1` is false at the current algebraic interface.
For any `p>41`, take `B=F_p`, `F=F_(p^6)`, and an element `alpha` of degree
six over `B`. In `F[X]_{<7}`, put

```text
r=X^2+alpha X,
P=<1,r>,
Q=<1,X^4>.
```

Then `P,Q` are base-free and

```text
P tensor Q -> <1,r,X^4,rX^4>
```

is an isomorphism onto a four-space, but `P` and the product four-space are
not Frobenius-stable and hence are not defined over `B`. Forty-one distinct
factors `g_t=1+t r`, with nonzero `t in B`, realize 41 projective ruling
planes. Giving 40 of them mass `R_2` and the last mass `19644026` realizes
the printed total and cap in the degree-six stratum.

## Nonclaim

The symbolic packet is a countermodel only to descent from the field-internal
Segre/factor-count interface. It is not an MCA witness and does not model the
received-line, first-owner, agreement-support, or noncontainment semantics.
Those extra semantics may still force descent or pay an extension stratum.
Even the `e=1` branch still needs the upstream fixed-cell and aggregate-owner
interfaces before it is paid.
