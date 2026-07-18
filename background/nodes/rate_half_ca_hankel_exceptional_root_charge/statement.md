# Exceptional-slope root charge for Hankel pencils

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

Use the notation of `rate_half_ca_hankel_minimal_index_budget`.  Thus the
generic Hankel rank is `rho`,

```text
A=R+1-2rho,       delta=rho-Ae,
```

the primitive generic apolar generator `Q_Z` has parameter degree `e>=1`,
and, after deleting its `s` fixed evaluation-domain factors, its residual
degree is `d=rho-s>0`.  If `T` finite slopes carry a squarefree degree-`r`
locator split over the evaluation domain `D`, then

```text
T*d <= (N-s)e+delta,                                  (ERC1)
T <= floor(((N-s)e+rho-Ae)/(rho-s)).                  (ERC2)
```

This strengthens the earlier estimate

```text
T<=delta+floor((N-s)e/d).
```

The point is that a supported rank-drop slope is not free.  If its rank loss
from the generic rank is `c`, the specialized `Q_Z` still has at least
`max(0,d-c)` residual domain roots.  The same slope consumes at least `c`
orders from the degree-`delta` regular Kronecker determinant.  Root incidence
and rank loss can therefore be charged together.

If at least one generic-rank slope is supported, the fixed domain factors are
simple and the contracted residual pencil has regular size

```text
delta_res=d-(A+s)e.
```

Charging omitted fixed roots to `Qbar_Z` and the remaining rank loss to this
residual determinant strengthens `(ERC1)` to

```text
T*d <= (N-s)e+delta_res.                              (ERC1R)
```

## Official `A=3` consequence

Put

```text
m=2^37,       rho=2^39-1=4m-1,       N=2^41=4rho+4.
```

These are the generic-rank data for the unresolved `A=3` profile at both
first-transition budgets.  If no generic-rank slope is supported, all
supported slopes are rank drops and `T<=delta<=rho`, so the official target
is already closed.  Otherwise the residual minimal-index inequality is

```text
s(e+1)<=rho-3e.                                      (ERC3)
```

For every

```text
1<=e<=m-1=2^37-1,
```

`(ERC2)` gives `T<=rho+1`.  Hence this entire parameter-degree range is
closed at both budgets.

If `e>=m`, `(ERC3)` forces `s=0`, and `(ERC2)` becomes the exact printed
upper bound

```text
T<=4e+1.                                             (ERC4)
```

Consequently the strict budget `B=2^39` leaves only

```text
s=0,       2^37<=e<=floor((2^39-1)/3),
```

where `(ERC4)` misses the required `rho+1` bound.  Every live pencil in this
range has a generic-rank supported slope, so `s=0` also excludes every
nonconstant parameter-independent factor of `Q_Z`: such a factor would have
to split over `D` at that slope and would contribute to `s`.  At the half-distance
budget `B=2^39+1`, the target is `rho+2`; the endpoint `e=2^37` is therefore
also closed, and its `A=3` residue begins at `e=2^37+1`.  The separate
`A=1` profile at that budget also contracts sharply under `(ERC2)`.

## Official `A=1` consequence

For the half-distance `A=1` profile, put

```text
h=rho=2^39=4m,       m=2^37,       N=4h.
```

The residual constraint and strongest coupled count are

```text
s(e+1)<=h-e,
T<=floor(((N-s)e+h-s-(1+s)e)/(h-s)).                   (ERC5)
```

Every `e<=m` is closed.  For `e>=m`, the residual constraint forces `s<=2`.
Consequently the entire remaining `A=1` profile is the disjoint union

```text
s=2,       m+1<=e<=floor((h-2)/3);
s=1,       m+1<=e<=floor((h-1)/2);
s=0,       m+1<=e<=h.                                 (ERC6)
```

No claim is made that the displayed ranges are populated by actual Hankel
pencils.

## Route fence: the regular tail need not be fixed

The remaining `A=3` problem cannot be reduced by asserting that the regular
Kronecker size `delta` is the degree of a fixed factor of `Q_Z`.  Over
`F_101` there is an exact `R=10,r=rho=4,e=1,delta=1` Hankel pencil whose
primitive generator is `Q_Z=Q_0+ZQ_1` with

```text
Q_0=(31,86,85,70,86),
Q_1=(22,16,11,20,68)
```

in ascending binary-affine coefficient order, and `gcd(Q_0,Q_1)=1`.  Its
rank is four at `100` finite slopes and three at one slope.  Thus even a
nonzero regular tail can coexist with a genuinely coprime moving generator.

The bounds use no pullback classification, characteristic hypothesis, or
numerical census.  The separate route fence is one exact finite-field
certificate.
