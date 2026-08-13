# Audit

- The exact layer identity uses `1-J_h`, not `1`, because every direction
  class line repeats the anchor.
- Missing direction classes are padded by size-one slots, preserving the
  identity and the fixed `G_e`.
- The line bank uses no outside-core cap and remains legal when
  `m-h<=c`.
- The optional top slot is included exactly when `H<m`.
- Pigeonhole is applied to line-slot sizes only after subtracting `C_e`.
- The forced line has at least two members at every paid support.
- The final low-list payment absorbs all high-deficit layers, not merely the
  direction class that forced the core.
- The adjacent excess is a compiler wall, not an unsafe certificate.

The primary endpoint verifier is source-pinned and mutation-tested.  The C
replay checks all `23,650` support values including the adjacent wall, in
constant memory.  The independent audit recomputes both endpoints.
