# KoalaBear m2 r2 degree-three geometric realization fence

- **status:** PROVED
- **scope:** the sole residual full-V4 `n=3` dihedral profile
- **dependencies:**
  `rate_half_kb_m2_r2_dihedral_residual_source_cover_twist_classifier` and
  `rate_half_kb_m2_r2_dihedral_degree6_common_pole_exclusion`
- **consumer:** `rate_half_band_closure`

The last profile has a complete geometric model at the forced rational-source
parameter

```text
a=b=-1,       d=-1,       ell=identity.
```

Put

```text
D_3(y)=y^3-3y,
h(t)=(t^2+2)/(1-t^2),
psi(x)=2/(x^2+1),
U=x^2+1,
H(t,x)=2U t^2-2x(x^2+3)t+U^2.                     (KBM3G-1)
```

Then `H` has bidegree `(2,4)`, its coefficient map is birational to the
special residual quartic `Q_(-1,-1)`, and its normalization has genus zero.
The two deck-conjugate components satisfy the exact pullback identity

```text
C(h(t),h(psi(x)))
 =9 H(t,x)H(t,-x)
  /((t^2-1)^2 (x^2-1)^2 (x^2+3)^2),               (KBM3G-2)
C(y,z)=y^2+yz+z^2-3.
```

Since `(y-z)C(y,z)=D_3(y)-D_3(z)`, every rational function

```text
F(y)=G(D_3(y))
```

is common on this component. If `G` has two distinct generic poles of order
five, then `F` has six distinct order-five poles. Their twelve degree-two
source lifts and the degree-24 complete source form satisfy every row
divisibility and the exact saturation identity. Thus the abstract common
function, six-pole divisor, quartic component, genus passport, star graph,
and complete source locators are jointly realizable.

Consequently no theorem using only those geometric gates can delete `n=3`.
The live obstruction must use the fixed KoalaBear active pencil/endpoint
record or construct a chronology-valid recurrent owner/payment.

This is a route fence, not an actual endpoint-record producer. It constructs
no deployed record or owner, moves no payment, and closes no `m=2` type,
K3, endpoint row, KoalaBear row, or Prize problem.

## Falsifier

Failure of `(KBM3G-2)`, failure of the special coefficient quartic, a source
genus other than zero, or a generic pair of cubic pole fibers violating the
complete-source divisibility.
