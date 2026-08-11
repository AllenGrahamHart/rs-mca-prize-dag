# Source and scope audit

Audited on 2026-07-20 against Paper D v13.2 promotion commit
`4bea7abb2d9455583c8864b980e39d11d550f51d`.

- TeX blob: `5ceff5dbc4b1ac4cef53eae7eada32046e4bafeb`
- revision-note blob: `2043c69a34b100a514366e5b0768777f28cf952f`
- source label: `cor:capfp-line`
- MCA definition: `def:mca` in the same source

The verifier evaluates the support-wise definition directly. It does not use
the paper's lattice implementation to decide MCA-badness. Low `d1` is
certified by explicit degree-one lattice vectors, and nonzero census is
certified by explicit supports.

The added `mu_16=F_17^*` regression is independent of shifted-lattice
implementation: every line word has Hamming weight at most `w=2`, so its
split error locator gives an explicit shifted-degree-at-most-two lattice
vector. The same-support obstruction follows from nine roots of a
degree-below-eight polynomial. It therefore falsifies the former displayed
`+1` inequality without needing to classify any reduced-basis output.
