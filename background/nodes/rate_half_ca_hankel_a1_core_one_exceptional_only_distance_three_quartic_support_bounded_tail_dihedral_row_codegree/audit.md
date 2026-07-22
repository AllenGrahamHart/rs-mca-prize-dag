# Audit

1. Rows are divided by `A(x)` before comparison. In the reciprocal case this
   creates the `x^2/c` adjustment in both `beta_y` and `Dhat_j(y)`.
2. The common-root eliminant contains only `Phi` and the tail Lagrange
   polynomials. Every good internal slope is therefore an exact factor,
   leaving degree at most `t`.
3. No division by `beta_x-beta_y` is required in the final implication.
4. External slopes are nonzero and disjoint from internal slopes, so roots
   of `I_G` are not charged as row intersections.
5. The zero eliminant is treated separately. Linear independence of the
   restricted parameter basis gives identical normalized rows, not merely
   a failed degree bound.
6. The one-orbit exception is inherited from the cubic `B`; arbitrary tail
   equations can only remove it.
7. Codegree at most `t` does not by itself reproduce the squarefree
   degree-`e` complement used by the zero-tail trace proof.
