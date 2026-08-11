# `A=1` core-free Forney infinity-contact section

- **status:** PROVED
- **closure:** full `A=1` recurrence boundary divisibility
- **consumer:** `rate_half_band_crossing_location`

Retain a failing core-free (`s=0`) half-distance `A=1` profile:

```text
rho=4m,       N=4rho,       m+1<=e<=rho,
T>=rho+2,     Delta=rho-e,  0<=O<=Delta.             (A1F1)
```

Let

```text
C:Q(z;X)=0,       (deg_X Q,deg_z Q)=(rho,e),
rank_F(z) M(z)=rho.                                   (A1F2)
```

Then `C` is reduced and every component has positive degree in both
coordinates. With

```text
q^vee(z;u)=u^rho Q(z;u^(-1)),
N_F(z;u)=[q^vee(z;u)sum_(i=0)^(rho-1)y_i(z)u^i]_(<rho),
P_F(z;X)=X^(rho-1)N_F(z;X^(-1)),                     (A1F3)
```

the nonzero biform `P_F` has bidegree at most `(rho-1,e+1)` and

```text
div_C(P_F)>=2rho H_X.                                 (A1F4)
```

Consequently it defines a nonzero section

```text
s_F in H^0(C,L_F),
L_F=O_C(-rho-1,e+1),       deg_C L_F=rho-e=Delta.     (A1F5)
```

The section is nonzero on at least one irreducible component; it need not be
nonzero on every component.

## Scope

The two fewer Hankel rows relative to strict `A=3` change the contact order
from `2rho+2` to `2rho`. This theorem is only for the core-free `A=1`
branch. It does not cover `s=1,2` or exclude a profile by itself.
