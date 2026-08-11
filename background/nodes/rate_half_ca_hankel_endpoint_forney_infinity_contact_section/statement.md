# Strict-endpoint Forney infinity-contact section

- **status:** PROVED
- **closure:** full-recurrence boundary divisibility
- **consumer:** `rate_half_band_crossing_location`

Retain any strict `A=3`, `e=m` endpoint profile, with arbitrary omission
defect `0<=O<=m-1`. Let

```text
C:Q(z;X)=0,       (deg_X Q,deg_z Q)=(rho,m),
rho=4m-1,         rank_F(z) M(z)=rho.                 (FIC1)
```

The component theorem makes `C` reduced and gives every component positive
degree in both coordinates. Define the canonical numerator

```text
q^vee(z;u)=u^rho Q(z;u^(-1)),
N(z;u)=[q^vee(z;u)sum_(i=0)^(rho-1)y_i(z)u^i]_(<rho),
P(z;X)=X^(rho-1)N(z;X^(-1)).                         (FIC2)
```

Then `P` is a nonzero biform of bidegree at most `(rho-1,m+1)`. If `H_X`
is the Cartier divisor cut out by `X=infinity`, its restriction to `C`
satisfies

```text
div_C(P)>=(2rho+2)H_X.                                (FIC3)
```

Therefore there is a nonzero global section

```text
s_F in H^0(C,L_F),
L_F=O_C(-rho-3,m+1),       deg_C L_F=m-1.             (FIC4)
```

The section can vanish identically on some irreducible components, but not
on all of `C`.

## Scope

This theorem is independent of root-omission defect and does not itself
exclude an endpoint. Its output is the universal low-degree section used by
the residual-pole interpolation theorem.
