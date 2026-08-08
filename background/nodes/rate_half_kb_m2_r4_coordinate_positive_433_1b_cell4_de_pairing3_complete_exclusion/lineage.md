# Lineage

- The compact cell-4 kernel and exact four-basis tower supplied the source
  algebra.
- A SymPy rational-function implementation reached the quadratic cuts but
  stalled on the nested quartic.
- Porting only `F_p(r)` arithmetic to reduced python-flint fractions reduced
  complete rows to roughly 19-36 seconds on Modal.
- A division-free pseudo-remainder retained the leading-degree-drop branch.
- Direct exceptional-root lifting removed any assumption that elimination
  denominators or leading coefficients are units after specialization.
- Exact parallel-edge transport adds the second positive `DE` deletion.
