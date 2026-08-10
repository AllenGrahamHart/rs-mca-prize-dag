# Clean-endpoint two-axis resultant and Picard pin

- **status:** PROVED
- **closure:** exact reciprocal resultant and intersection divisor
- **consumer:** `rate_half_band_crossing_location`

Retain the boundary-saturated clean endpoint. A generic projective change of
the domain coordinate may be chosen so that the domain, `x_0`, every root of
`Q(S;X)`, and every root of `q_inf` remain finite. Put

```text
a(z)=[X^rho]Q(z;X),       d=deg_X W,
A_0(z)=product_(gamma in Z:Q(gamma;x_0)=0)(z-gamma).
```

Then the leading `X`-coefficient of the dual complement gives a second
Bezout identity

```text
a alpha+H beta=1,                                    (TAP1)
alpha=[X^(N-rho)]A,       beta=[X^N]B.               (TAP2)
```

The exact resultants in the domain variable are

```text
Res_X(Q,B)=d_B S(z),
Res_X(Q,W)=d_W a(z)^(d+N-1)A_0(z),
d_B d_W in Fbar^*.                                   (TAP3)
```

Choose parameter infinity additionally so that `q_inf` is squarefree, and
let `Y_inf=C intersect {z=infinity}` be its reduced degree-`rho` divisor on
the irreducible curve `C:Q=0`. If `P_*=(x_0,S)` denotes the unique affine
intersection of `Q` and `B`, including the repeated-supported-defect case,
then the complete intersection divisor is

```text
div_C(B)=P_*+(T+b)Y_inf.                             (TAP4)
```

Consequently

```text
O_C(N,-T) is isomorphic to O_C(P_*),
deg O_C(N,-T)=Nm-T rho=1.                            (TAP5)
```

Thus the clean failure supplies an effective degree-one Picard class coming
from the ambient mixed line bundle `O(N,-T)`.

## Scope

The degree-one class is necessary, not contradictory on an arbitrary
integral curve. The next gate translates its section into an explicit
multiplication-map rank defect and retains the Hankel frame as extra input.
