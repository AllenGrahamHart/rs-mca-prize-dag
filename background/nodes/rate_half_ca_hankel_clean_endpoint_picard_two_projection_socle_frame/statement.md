# Clean-endpoint Picard two-projection socle frame

- **status:** PROVED
- **closure:** reciprocal finite-pushforward direction
- **consumer:** `rate_half_band_crossing_location`

Retain `P_*=(x_0,S)` and define the two fibre quotients

```text
A_0(z)=Q(z;x_0)/S(z),
C_0(X)=Q(S;X)/(X-x_0).                                  (PSF1)
```

The chosen two-axis normalization makes both quotients nonzero of exact
degrees `m-1` and `rho-1`. For the projections

```text
pi_X:C->P^1_X,       pi_z:C->P^1_z,
```

the positive modification `O_C -> O_C(P_*)` has the paired fibre-socle
directions

```text
[A_0] |-> [ev_S] in P(H^0(P^1_z,O(m-2))^*),
[C_0] |-> [ev_x0] in P(H^0(P^1_X,O(rho-2))^*).          (PSF2)
```

The unmodified pushforwards and their modified splittings are

```text
(pi_X)_*O_C=O direct_sum O(-rho)^(m-1),
(pi_X)_*O_C(P_*)
 =O direct_sum O(1-rho) direct_sum O(-rho)^(m-2),       (PSF3)

(pi_z)_*O_C=O direct_sum O(-m)^(rho-1),
(pi_z)_*O_C(P_*)
 =O direct_sum O(1-m) direct_sum O(-m)^(rho-2).         (PSF4)
```

Both statements retain ramification. If either fibre root is repeated, the
corresponding quotient in `(PSF1)` is the local socle generator and still
maps to the same evaluation functional.

## Hankel interface

The second projective direction is the truncated domain Veronese vector

```text
ev_x0=(1,x_0,...,x_0^(rho-2)).                          (PSF5)
```

Thus the remaining clean endpoint is not merely a curve with an abstract
degree-one class: its marked point selects rational-normal evaluation
directions on both axes. A closing theorem must combine `(PSF2)` with the
four-Hankel common isotropic plane and the supported-locator incidence; this
node does not assert that incompatibility.
