# Proof: SPI Hankel Conjecture-F consumer descriptor

Fix `(u,v)`. A locator coefficient vector `ell` belongs to the alignment
variety `X_(u,v)` exactly when the two vectors `M_u ell` and `M_v ell` are
linearly dependent. Equivalently, there is a projective slope
`z=[z_0:z_1]` such that

```text
(z_0 M_u+z_1 M_v)ell=M(z)ell=0.
```

For fixed `z`, this condition is linear in `ell`; its projectivization is
exactly `P_z=P(ker M(z))`. Intersecting with `D_j(H)` imposes exactly that
the degree-`j` locator split into `j` distinct roots on the evaluation
domain. Hence the incidence fiber over `z` is exactly `P_z cap D_j(H)`, with
projective dimension `r_z=dim ker M(z)-1`, unchanged domain `H`, and no
punctures.

This is an equality of incidence sets, not merely a support injection. The
sum in `spi_point_counting` is over supported slopes, so a locator incident
to multiple slopes must occur with that same multiplicity. Emitting one
descriptor occurrence per pair `(z,ell)` preserves it automatically.

The proved component and payment classification processes vertical,
rank-excess, tangent/common-divisor, quotient/pullback, extension,
degenerate, and apolar-principal components before the generic row-full
residual. Retaining that chronology assigns the first owner without changing
the fiber equality. The remaining generic incidence fiber is therefore an
exact Conjecture-F linear-flat call with the printed descriptor. This proves
the interface; it does not bound `P_z cap D_j(H)` or the number of supported
slopes.
