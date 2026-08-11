# Audit

1. `S_gamma` is the actual nonzero-error support; `E_gamma` is the padded
   locator. The clone points are light, so membership in `E_delta` is actual
   membership in `S_delta`.
2. The full-locator triple bound retains all padded heavy rows. The
   two-simple zero-deficit endpoint case is handled separately, where the
   endpoint locators equal their actual supports.
3. The `e` clone-root slopes are distinct because the common row form is
   squarefree. The source endpoint is not among them, while the other
   endpoint is.
4. The fixed core point has degree `T`, not `e`; it is removed before the
   light missing-incidence count. This changes the forced line deficit from
   the incorrect `e-1` to the correct `e-2`.
5. Both packet-wide deficit sums equal `e-6`, including overlap in
   `Z_1,Z_2` with multiplicity, exactly as `r_gamma` is defined.
6. The projective formulation covers a possible slope at infinity: a
   nonzero homogeneous linear coordinate vanishes at at most one slope.
