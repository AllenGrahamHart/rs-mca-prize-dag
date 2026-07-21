# Budget-three fiber-two c=2 one-antipodal barycentric support-polynomial compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_barycentric_negation_syndrome`

Retain the canonical notation and barycentric coloring from `(BNS1)`.  Write

```text
E=(1-z^2)Q_-,       Q_-=1-Sz+Pz^2,       Q_+=Q_-(-z),
V=z^H C,
Theta=HBC+z(BC'-B'C),
J=Q_- C^2 Theta+Q_+ C(-z)^2 Theta(-z).              (BSP1)
```

Then `J` is even and

```text
deg Theta<=3H-7,       deg J<=5H-11.                 (BSP2)
```

If

```text
uhat_j=sum_(a in mu_N)u(a)a^j,
```

the complete first-period moment polynomial is

```text
sum_(j=1)^(N-1) uhat_j z^(j-1)
 =-z^(3H-1)(1-z^2)J(z).                              (BSP3)
```

Equivalently, Fourier inversion gives the pointwise compiler

```text
u(x)=-N^(-1)x^(-3H)(1-x^(-2))J(x^(-1)),
x in mu_N.                                           (BSP4)
```

Thus the support in the barycentric direction is determined by `E,B,C`
without constructing any root cell or outer scalar.  The support bound
`|supp u|>=3H+1` follows again from `(BSP2)--(BSP4)`.

The minimum-support case is equivalent to the exact split-divisor gate

```text
deg J=5H-11,
J divides (z^N-1)/(z^2-1),
J(1)J(-1)!=0.                                        (BSP5)
```

Hence a minimum-support survivor must print one even, fully subgroup-split
polynomial `J` of the displayed degree; larger-support survivors have fewer
subgroup roots of `J`.  This compiler does not exclude either case or prove
the one-antipodal branch empty.
