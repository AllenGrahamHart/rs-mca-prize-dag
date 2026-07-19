# Audit

- Rational maps are treated projectively, so poles are ordinary fibers over
  infinity.  Coprime homogeneous coordinate pairs have no base points.
- The equation `f(x)=g(gamma)` gives the exact dot product
  `I_*=sum_y a_y b_y`; no multiplicity or transversality assumption is used.
- The capacity estimate optimizes jointly over all admissible fiber-size
  sequences.  Concentrating `a` first is an upper bound for every actual map,
  not an assumption that the maps have maximally concentrated fibers.
- The official congruence `2^37=2 mod 5` is load-bearing only in the `q=5`
  integer endpoint, where it strengthens the leftover domain mass to at
  least `17`.
- The contradiction uses `C_*<=sum_i C_i<=m`; it does not assume the
  residual component degree is zero.
- For the separation-rank corollary, irreducibility removes common factors
  from each rank-two coefficient pair.  Homogenization then gives two
  base-point-free maps of the full bidegrees, so no lower-degree pullback is
  silently consumed.
- For the full generator, core-freeness and parameter primitivity replace
  irreducibility in removing those common factors.  Its exact column deficit
  is `1+O`, so the direct rank-two contradiction is stronger than the
  componentwise one.
- The verifier checks every admissible degree for smaller powers of two with
  the same residue class, the two symbolic cases, official constants, and
  DAG wiring.  It does not test arbitrary mixed biforms.
