# `A=1` quadratic gap-four cyclic-design spread exclusion

- **status:** PROVED
- **closure:** the Cycle-107 cyclic incidence witness violates the necessary two-slope spread
- **consumer:** `rate_half_band_crossing_location`

Retain the explicit cyclic block family of the quadratic gap-four abstract
incidence design. For every `e>=14`, it has a deficient block `E_t` such
that the adjacent pair `E_t,E_(t+1)` has exactly

```text
e+3                                                     (CDS1)
```

third blocks whose full locator union with that pair has size at least
`2rho+1`.

The first block has actual-error deficit one. Therefore the proved
two-slope coefficient-rank spread requires at least

```text
ceil((rho+7+r_(t+1))/2)
 >=ceil((3e+6)/2)>e+3.                               (CDS2)
```

Thus the explicit cyclic family cannot be the locator incidence table of
either retained quadratic `u=4` packet on the official row.

## Scope

This excludes only the explicit cyclic realization, not every abstract
block system with the same degree sequence. The original abstract-incidence
theorem remains valid: handshake and degree data alone are consistent.
