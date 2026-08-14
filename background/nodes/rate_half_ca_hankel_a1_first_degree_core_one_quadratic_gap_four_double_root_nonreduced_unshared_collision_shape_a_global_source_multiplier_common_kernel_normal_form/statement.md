# `A=1` shape-A global source-multiplier common-kernel normal form

- **status:** PROVED
- **closure:** the three residue kernels are one three-multiplier Padé
  intersection in the full source algebra
- **consumer:** `rate_half_band_crossing_location`

Choose an affine parameter coordinate `z` in which the three centers are
finite and write

```text
B_src(z,X)=J(X)z+K(X).                             (GSM1)
```

Then `J` is nonzero on `U_0`. In the split residue algebra

```text
A=F[X]/(L_U0),       tau(F)=sum_(x in U_0)F(x)/L_U0'(x),
```

put

```text
varphi=-K/J in A.                                  (GSM2)
```

For every classified point,

```text
J(x)=eta_x L_U0'(x),       varphi(x)=gamma
                                      (x in M_gamma). (GSM3)
```

Thus `varphi` obeys the exact cubic split relation

```text
(varphi-alpha)(varphi-beta)(varphi-gamma_0)=0
                                                        in A. (GSM4)
```

Let `W_X subset S_n` be the domain coefficient space of `G`, and define

```text
E_3=W_X+varphi W_X+varphi^2 W_X subset A.          (GSM5)
```

Then

```text
dim E_3=3r.                                        (GSM6)
```

The three classwise interpolation kernels have the single exact
description

```text
K_cap=intersection_gamma ker T_gamma
     =S_n intersect J E_3^perp,                    (GSM7)
```

where orthogonality is for the nondegenerate residue pairing
`(F,H)|->tau(FH)` in `A`.

Equivalently, `h in K_cap` if and only if, for every `f in W_X` and
`s=0,1,2`,

```text
sum_(x in U_0)
 f(x)h(x)varphi(x)^s/[J(x)L_U0'(x)]=0.             (GSM8)
```

If `B_src=H B_prim`, then `J=H J_prim`, `K=H K_prim`, and
`varphi=-K_prim/J_prim`; hence `(GSM7)` is intrinsic to the primitive
source pencil and its fixed factor.

At the current lower rank boundary,

```text
dim E_3=3(e+1)/2=n+5=274877906946,
dim E_3^perp=2n+2=549755813884,                    (GSM9)
```

while Shape A requires

```text
dim(S_n intersect J E_3^perp)>=e-3=183251937960.  (GSM10)
```

## Scope

This theorem does not bound the intersection in `(GSM7)`. It identifies
the exact owner-sensitive Padé alignment that a lower-boundary survivor
must sustain; dimension heuristics or projective distinctness are not a
proof that the intersection is small.
