# Proof: fixed-background FPC5 Hankel codimension

The touched petals and background are disjoint, so `L_R,L_1,...,L_t` are
pairwise coprime. CRT gives `chi_R`. The same argument as in the owner-free
Cauchy chart proves that `(FB4)` is the unique degree-below-`h_R` numerator
with the residues in `(FB3)`, and that `deg B_(G,R)<=d` is exactly the first
`h_R-d-1` weighted moments of `G` vanishing.

Using `(FB1)`,

```text
h_R-d-1=t ell+u-((t-1)ell+u)-1=ell-1,
```

which proves `(FB5)`.

Treat `L_R` as one additional interpolation block carrying label zero.
Since

```text
h_R-d=ell>0,
2d+1-h_R=d-ell+1>=0,
```

the saturated-slice dimension theorem applies to any primitive monic
member of the fixed-`R` cell. It gives pair and locator vector dimension

```text
2d+2-h_R=d-ell+2.
```

The monic hyperplane has dimension one less. Equivalently, rank-nullity
gives Hankel rank

```text
(d+1)-(d-ell+2)=ell-1.
```

This proves `(FB6)` and full row rank.

Finally, a fixed contributor `G` belongs to `F_R` for exactly
`binom(|R_G|,u)` choices of `R`. Double-counting the incidences `(G,R)`
proves `(FB7)`. The first-subset assignment is unique after fixing any total
order on the background, so it is a disjoint partition. QED.
