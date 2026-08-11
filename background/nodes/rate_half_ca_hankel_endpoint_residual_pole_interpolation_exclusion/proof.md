# Proof

Every irreducible component of `C` has positive degree in both coordinates.
Thus the restrictions of `G` and `H` are nonzerodivisors on the reduced
curve.

Fix a supported slope `gamma`, write `h=z-gamma` locally, and let `A` be a
local ring of `C` over that fibre. The pole-cancellation ideal is

```text
J_gamma=(h:g),       g=G|_C.                          (1)
```

Because `h` is a nonzerodivisor, in the finite ring `B=A/(h)` one has

```text
J_gamma/(h)=ann_B(g),
length(A/J_gamma)=length(gB)
 =length(B)-length(B/(g)).                            (2)
```

The complete fibre has total length `rho`. Each of its `u_gamma` distinct
domain points belongs to the common zero scheme of `h` and `g`, contributing
at least one to `length(B/(g))`. Summing `(2)` over the fibre gives

```text
length(O_C/J_gamma)<=rho-u_gamma.                     (3)
```

Away from the supported fibres there is no pole. The global ideal
`J=(H:G)` therefore satisfies

```text
d=length(O_C/J)<=sum_gamma(rho-u_gamma)=O<=m-1,       (4)
```

which proves `(RPI3)`.

Twisting the quotient by `O_C(1,ell)` does not change its length. Restriction
to that quotient is a linear map from the `m`-dimensional space

```text
H^0(P^1 x P^1,O(1,ell)).                              (5)
```

Its target has dimension `d<m`, so its kernel contains a nonzero biform
`F`. By construction `FG` belongs locally to `H O_C`, and the quotients
glue to the regular section `(RPI5)`.

No component equation divides `F`: every residual component has domain
degree `4e_i>=4`, while the dominant component has domain degree
`4e_*-1>=7`, but `deg_X F=1`. The same mixed-component property prevents a
component from dividing `G` or `H`. Thus `FG/H` is nonzero at the generic
point of every component.

The Forney contact theorem supplies a section `s_F` that is nonzero on at
least one component. Since `s_G` is nonzero on every component and `C` is
reduced, `s_F^4s_G` is nonzero. Direct arithmetic gives

```text
4(-rho-3)+N+1=-7,
4(m+1)+ell-T=ell+3,                                   (6)
```

proving `(RPI6)`.

Finally twist the Cartier-divisor restriction sequence for the bidegree
`(rho,m)` curve:

```text
0 -> O(-rho-7,ell+3-m)
  -> O(-7,ell+3)
  -> O_C(-7,ell+3) -> 0.                             (7)
```

The middle surface has no sections because its first degree is negative.
For even `m>=6`,

```text
ell+3-m=2-m/2<0.                                     (8)
```

The Kunneth decomposition of `H^1` of the left surface term vanishes: one
summand contains `H^0(P^1,O(2-m/2))=0`, and the other contains
`H^0(P^1,O(-rho-7))=0`. The long exact sequence proves `(RPI7)`,
contradicting `(RPI6)`. QED.
