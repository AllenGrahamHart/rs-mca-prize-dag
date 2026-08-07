# SPI Hankel Conjecture-F consumer descriptor

- **status:** PROVED
- **consumer:** `f_prize_consumer_flat_scope`

For a pair `(u,v)`, let

```text
M(Z)=Z_0 M_u+Z_1 M_v
```

be the Hankel slope pencil acting on degree-`j` locator coefficients. For
every projective slope `z`, define

```text
P_z=P(ker M(z)),       r_z=dim ker M(z)-1.
```

Then the slope-incidence points counted by `spi_point_counting` over `z` are
exactly

```text
P_z cap D_j(H).
```

The emitted descriptor is

```text
(H, j, r_z, exact split-root threshold j, no punctures,
 exceptional-component/payment owner before generic residual).
```

It preserves incidence multiplicity: if one locator is incident to several
slopes, it is emitted once for each slope, exactly as in the supported-slope
sum. Tangent/common-divisor, quotient/pullback, extension, degenerate, and
apolar-principal exceptional components are assigned before the generic
row-full residual by `payment_completeness`; no count for the residual
intersection is claimed here.
