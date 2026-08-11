# Final strict `A=3` corner integral Picard pin

- **status:** PROVED
- **closure:** univariate descent and component-degree rigidity
- **consumer:** `rate_half_band_crossing_location`

Retain the sole strict corner

```text
rho=3e+1,       T=rho+2=3e+3,
delta=1,        0<=O<=1.                              (FCP1)
```

Let `C:Q=0` be the reduced bidegree-`(rho,e)` endpoint curve and let

```text
L_F=O_C(-rho-3,e+1).                                  (FCP2)
```

Then `C` is absolutely irreducible and

```text
L_F is isomorphic to O_C(P_*)                         (FCP3)
```

for one effective degree-one Cartier point `P_*`.

More precisely, let `J=(H:G)` be the pole-cancellation ideal for
`G=X^N-1` and the supported-slope polynomial `H`, and put

```text
d=length(O_C/J) in {0,1}.                             (FCP4)
```

There is a biform `F` of bidegree `(d,0)` such that `FG/H` is regular, and a
nonzero univariate section `A_d(X)` satisfying on `C`

```text
s_F^3 (F G/H)=A_d(X),
deg A_d<=rho-5+d.                                     (FCP5)
```

Here `s_F` is the universal contact section; its divisor is exactly `P_*`.

## Scope

This pins the geometry and divisor identity of the final corner but does not
yet exclude it. Both `O=0` and `O=1` remain in scope, as do the separate
`A=1` and adjacent-unsafe obligations.
