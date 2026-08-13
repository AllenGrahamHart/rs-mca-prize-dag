# `A=1` quadratic squarefree shared-correction third-jet gate

- **status:** PROVED
- **closure:** exact one-scalar obstruction to extending the cubic quotient through a shared root
- **consumer:** `rate_half_band_crossing_location`

Retain the double-root extremal profile with `S_B` squarefree, but allow a
simple common root `tau` of `g_*` and `S_B`. Let `z` be a base uniformizer at
`tau`. Then

```text
ord_tau Q(t,x_*)=4,
ord_tau D_1=3.                                      (HSJ1)
```

For the divided heavy row and contracted moments

```text
U(t,X)=[Q(t,X)-Q(t,x_*)]/(X-x_*),
F_i(t)=Phi_t(X^iU(t,X)),                            (HSJ2)
```

one always has

```text
z^2 divides F_0.                                    (HSJ3)
```

Define the shared third-jet obstruction

```text
kappa_tau=[z^2]F_0
          = (F_0/z^2) mod z.                        (HSJ4)
```

The moment recurrence gives, for every `i`,

```text
(F_i/z^2) mod z=x_*^i kappa_tau.                   (HSJ5)
```

Moreover,

```text
kappa_tau=0
 iff D_1 divides F_0 locally at tau
 iff D_1 divides every F_i locally at tau.         (HSJ6)
```

On the vanishing branch the local cubic quotient extends exactly and the
regular Smith type at `tau` is `[3]`. On the nonvanishing branch the
canonical divided-row image has exact order two with leading direction
`kappa_tau nu(x_*)`; the unmodified cubic quotient does not extend through
the shared root.

## Scope

The theorem is a local dichotomy, not a proof that `kappa_tau` vanishes or
is nonzero in every admissible packet. It does not treat a nonreduced
correction root. No branch-coalescence assumption on the normalized curve
is made.
