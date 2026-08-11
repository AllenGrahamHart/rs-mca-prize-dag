# `A=1` quadratic nonreduced unshared corank-one jet router

- **status:** PROVED
- **closure:** elimination of both nonreduced jets on the simple corank-one locus
- **consumer:** `rate_half_band_crossing_location`

Retain the nonreduced unshared-correction setup at `tau`, with local
parameter `z`, divided heavy row `U(t,X)`, and obstruction jets
`kappa_2,kappa_3`. Let `N(z)` be the regular symmetric local block after
removing the permanent primitive kernel, and let `v(z)` be the regular class
of the coefficient vector of `U`.

Assume only

```text
corank N(0)=1.                                        (HCR1)
```

Let `P_tau` be the specialized minimal locator of the contracted source.
Then

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

Equivalently, any unshared nonreduced survivor with a nonzero obstruction
jet must satisfy

```text
corank N(0)>=2.                                     (HCR4)
```

Thus the two free jets cannot survive on the ordinary correction profile;
they require a genuine additional source-rank drop. A collision of `x_*`
with the quotient locator can occur only inside that higher-corank locus.

## Scope

The theorem is a router, not a proof that `(HCR1)` holds at every
nonreduced correction. A corank-two symmetric local block of determinant
order four can carry a nonzero order-two self-pairing, so `(HCR4)` cannot be
discarded by determinant order alone. Shared nonreduced roots are not
covered.
