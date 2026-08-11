# Strict `A=3` Forney infinity-contact section

- **status:** PROVED
- **closure:** full-recurrence boundary divisibility
- **consumer:** `rate_half_band_crossing_location`

Retain any failing strict `A=3` moving-kernel profile from the slope-slack
ledger:

```text
m<=e<=floor(rho/3),       delta=rho-3e,
T>=rho+2,                 0<=O<=delta.                (FIC1)
```

Let

```text
C:Q(z;X)=0,       (deg_X Q,deg_z Q)=(rho,e),
rank_F(z) M(z)=rho.                                   (FIC2)
```

The curve `C` is reduced and every component has positive degree in both
coordinates. Define

```text
q^vee(z;u)=u^rho Q(z;u^(-1)),
N(z;u)=[q^vee(z;u)sum_(i=0)^(rho-1)y_i(z)u^i]_(<rho),
P(z;X)=X^(rho-1)N(z;X^(-1)).                         (FIC3)
```

Then `P` is a nonzero biform of bidegree at most `(rho-1,e+1)`. If `H_X`
is the Cartier divisor cut out by `X=infinity`, its restriction to `C`
satisfies

```text
div_C(P)>=(2rho+2)H_X.                                (FIC4)
```

Therefore there is a nonzero global section

```text
s_F in H^0(C,L_F),
L_F=O_C(-rho-3,e+1),       deg_C L_F=delta.           (FIC5)
```

The section can vanish identically on some irreducible components, but not
on all of `C`.

## Scope

This theorem applies to the full strict slope-slack range, including the
old `e=m` endpoint as `delta=m-1`. It does not by itself exclude a profile;
its output is consumed by pole interpolation.
