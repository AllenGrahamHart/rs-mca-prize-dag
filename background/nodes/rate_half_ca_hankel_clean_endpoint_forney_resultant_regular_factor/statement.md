# Clean-endpoint Forney resultant equals the regular factor

- **status:** PROVED
- **closure:** exact Padé numerator and normalized resultant
- **consumer:** `rate_half_band_crossing_location`

Write

```text
q(t;X)=sum_(j=0)^rho q_j(t)X^j,
a(t)=q_rho(t),
y_i(t)=y_i^(0)+t y_i^(1).                             (FRF1)
```

Form the reciprocal locator and truncated syndrome series

```text
q^vee(t;Z)=Z^rho q(t;Z^(-1)),
N(t;Z)=[q^vee(t;Z) sum_(i=0)^(rho-1)y_i(t)Z^i]_(<rho),
P(t;X)=X^(rho-1)N(t;X^(-1)).                          (FRF2)
```

Then

```text
deg_X P<=rho-1,       deg_t P<=m+1.                   (FRF3)
```

Let `Delta(t)` be the degree-`m-1` regular Kronecker determinant from the
marked adjugate theorem. The top square Hankel adjugate and the fixed-degree
resultant satisfy

```text
adj H_0(t)=c_0 a(t)Delta(t)q(t)q(t)^T,                (FRF4)

Res_X^(rho,rho-1)(q(t;X),P(t;X))
 =c_1 a(t)^(2rho+2)Delta(t),                          (FRF5)
```

for constants `c_0,c_1!=0`. The resultant in `(FRF5)` is the Sylvester
determinant with `P` padded to formal degree `rho-1`; the identity remains
valid when its actual degree drops.

At every generic supported slope `gamma`, write

```text
q(gamma;X)=a(gamma) Lambda_gamma(X),
Lambda_gamma=product_(x in S_gamma)(X-x).
```

There are unique nonzero Forney weights `theta_(gamma,x)` such that

```text
y_i(gamma)=sum_(x in S_gamma)theta_(gamma,x)x^i,
P(gamma;x)=theta_(gamma,x) partial_X q(gamma;x).       (FRF6)
```

For each of the at least `2m+3` supported slopes from the marked adjugate
theorem,

```text
c_0 Delta(gamma)a(gamma)^3
 =Vandermonde(S_gamma)^2
  product_(x in S_gamma)theta_(gamma,x)               (FRF7)
```

up to the fixed ordering sign absorbed in `c_0`. Thus the normalized Forney
resultant has only the degree-`m-1` factor `Delta`; all apparent
`Theta(m^2)` resultant degree is the printed leading-coefficient power.

## Scope

Nonvanishing of `(FRF7)` at the good slopes is necessary and already
accounted for by `Delta`. The theorem does not bound the values of the
Forney products or prove they cannot interpolate a degree-`m-1` polynomial.
