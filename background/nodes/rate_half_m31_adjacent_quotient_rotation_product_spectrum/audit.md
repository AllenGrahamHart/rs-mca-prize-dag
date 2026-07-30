# Audit - M31 adjacent quotient-rotation product spectrum

- Kept the object as ordinary LIST codewords, not MCA slopes.
- Used the auxiliary M31 target `2^-100`; did not relabel it as the Prize
  target `2^-128`.
- Checked that the two high coefficient blocks are disjoint because
  `s<c`, and that the monic coefficient of the fixed partial locator makes
  the product-to-prefix map injective.
- Counted subsets of `C_32\{1}` rather than all of `C_32`.
- Kept the exact class count as a structured lower contribution; arbitrary
  locators may enlarge the same received-word list.
- The independent replay sources use different methods: subset-sum dynamic
  programming and Ramanujan sums.
- Neither replay was executed locally, and no Modal task was launched. The
  closed formulas and weighted total provide the proof audit.
