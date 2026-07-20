# Audit

- The `2n` count is global, not per target: the support-overlap proof makes
  the cover label and its root parameter unique for every generic overlapping
  edge. A parameter in one cover determines all four roots.
- The worst class weight `17/10` is applied to all generic overlap edges.
  This is conservative but sound; no class decorrelation is assumed.
- Edges incident to the antipodal vertex are not in the generic--generic
  covers. They are paid separately by `(17/5)S_A`.
- The affine theorem bounds each `R(t)` pointwise. Multiplying it by the
  global edge count is valid even when several edges have the same target.
- The adapter has `K_25^c=2D_c`; multiplying the disjoint ledger by `20`
  gives coefficients `10,17`, while the overlap terms become `867/4` and
  `68`.
- `(GOP2)` is a sufficient analytic target, not an identity for C36'. A
  violation does not by itself refute C36'.
