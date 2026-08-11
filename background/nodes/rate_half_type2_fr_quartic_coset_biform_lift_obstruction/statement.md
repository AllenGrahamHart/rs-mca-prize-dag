# Quartic-coset biform lift obstruction for the type-2 FR countermodel

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_crossing_location`

Put `n=4m`, `N=4n=16m`, and `rho=n-1=4m-1`.  Let `F` contain the cyclic
smooth domain

```text
D=mu_N
```

and its subgroup `H=mu_n`.  Choose representatives `tau_0,...,tau_3` of
the four distinct cosets of `H` in `D`, and identify the four-copy point
set with `D` by

```text
(i,x) |-> tau_i x,             x in H.                (QBL1)
```

Assume `char F` does not divide `m`.  On three of the four copies, prescribe
the quartic-difference-family incidence row

```text
P_(i,x)(Gamma)=(Gamma-x)^m-c_i,                       (QBL2)
```

where the constant `c_i` does not affect the leading two coefficients.  No
biform

```text
Q(Gamma;X)=sum_(j=0)^m Q_j(X) Gamma^j,
deg_X Q_j<=rho                                        (QBL3)
```

can satisfy

```text
Q(Gamma;tau_i x)=lambda_(i,x) P_(i,x)(Gamma)          (QBL4)
```

on all points of those three copies with every `lambda_(i,x)` nonzero.

For the incidence witness in
`rate_half_type2_fr_incidence_only_route_fence`, take `m=64`,
`F` containing `F_(257^4)`, `H=F_257^*=mu_256`, and `D=mu_1024`.
The single deleted incidence lies in the fourth copy, so the other three
copies obey `(QBL2)`.  Therefore the witness has no coset-preserving lift to
the locator-degree-`255` biform required of the endpoint apolar generator,
even before imposing a Hankel-kernel equation.

This theorem does not prove the general max-intersection bound `(FR)`.  It
does not exclude an arbitrary, non-coset-preserving permutation of the
1024 incidence points, and it does not classify all abstract countermodels.
It proves that the most algebraically aligned lift of the explicit quartic
countermodel is impossible.
