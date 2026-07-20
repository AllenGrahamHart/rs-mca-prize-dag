# Audit

1. The official value `H=2^37+1` is odd, so `2H-2` is divisible by four.
   At even toy values of `H`, the two primary zero positions instead miss the
   support of `(1-z^4)^(-1/4)` and the pure quartet can pass the primary gate.
2. Nonvanishing uses `p>2^40`; a formal rational coefficient alone is not a
   finite-field proof.
3. Common scaling multiplies the supported coefficient by a nonzero fourth
   power and cannot create a zero.
4. Primary-only fourth-root rigidity is false. The bounded sweep contains
   twelve non-pure primary-gap survivors. None passes the secondary gate, but
   that observation is heuristic and is not a premise of this node.
5. The node excludes a geometry; it does not close the full `c=2` chamber.
