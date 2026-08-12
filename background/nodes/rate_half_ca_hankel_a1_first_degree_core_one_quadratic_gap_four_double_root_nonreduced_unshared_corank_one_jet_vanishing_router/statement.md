# `A=1` quadratic nonreduced unshared corank-one jet router

- **status:** PROVED
- **closure:** elimination of both nonreduced jets on the separated corank-one locus
- **consumer:** `rate_half_band_crossing_location`

Retain the nonreduced unshared-correction setup at `tau`, with local
parameter `z`, divided heavy row `U(t,X)`, and obstruction jets
`kappa_2,kappa_3`. Let `N(z)` be the regular symmetric local block after
removing the permanent primitive kernel, and let `v(z)` be the regular class
of the coefficient vector of `U`.

Assume

```text
corank N(0)=1,       P_tau(x_*)!=0,                  (HCR1)
```

where `P_tau` is the specialized minimal recurrence polynomial. Then

```text
deg P_tau=d-1,
Q(tau,X)=c(X-x_*)P_tau(X),
U_tau(x_*)=cP_tau(x_*)!=0.                          (HCR2)
```

Consequently

```text
kappa_2=kappa_3=0.                                 (HCR3)
```

Consequently `D_1` divides every divided-row moment locally, the cubic
quotient extends through `tau`, and the local regular Smith type is `[4]`.

Equivalently, any regular-corank-one survivor with a nonzero obstruction
jet must lie on the compressed-recurrence collision

```text
P_tau(x_*)=0.                                      (HCR4)
```

Thus the two free jets cannot survive on the ordinary correction profile;
they require a collision of `x_*` with the compressed minimal recurrence
or a genuine additional source-rank drop.

## Scope

The separation `P_tau(x_*)!=0` is a hypothesis, not a consequence of
`x_* notin U_0`: truncated moments can have a compressed minimal recurrence
whose roots lie outside the original fixed source. The theorem is a router,
not an exclusion of the compressed-recurrence collision or higher corank.
Shared nonreduced roots are not covered.
