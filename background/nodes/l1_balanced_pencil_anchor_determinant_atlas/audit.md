# Audit

- The balanced coefficient hyperplane and the determinant target both have
  dimension `s`; primitivity of the anchor makes the determinant map
  injective.
- Monicity is load-bearing in the injectivity proof. Without it, adding a
  constant multiple of the anchor preserves the determinant.
- Exactness is used twice: coefficient content is one, and `R` is nonzero on
  both exchanged root sets.
- `D` is the common **complement** locator. `G` is the common agreement
  locator. They are not interchangeable first owners.
- The identity `gcd(Delta_0,W_0)=D` uses squarefreeness of the domain locator.
- The Bezout dual `(-v,u)` is unimodular with the anchor coefficient pair.
  Its module determinant gives `K-JP_0=gamma L_0` without division in the
  interpolation module.
- `J` is a unit modulo `W_0`: a common root would force the dual numerator
  to be both zero by module evaluation and nonzero by squarefreeness.
- The universal congruence `W=Delta_0J mod W_0` proves owner recovery on the
  whole monic coefficient body, stronger than the exact-neighbor argument.
- Cancelling the fixed owner in that congruence gives the remainder graph
  `(DA7a)`; monicity supplies the added `X` term.
- Euclidean quotient/remainder against monic `W_0` forces
  `T=1-Q_Delta`; this is an identity, not a choice of normalization.
- The anchor/dual coefficient transformation is unimodular, so it preserves
  the coefficient-content ideal. The exact guard is therefore precisely
  `gcd(Delta,1-Q_Delta)=1`.
- For a split `W_Delta`, the common gcd with `W_0` cancels from `Delta`, and
  the remaining denominator divides `L_0`. This proves automatic numerator
  divisibility in `(DA4h)`.
- The deficiency identities have been checked in both coordinate systems:
  `j=k-1-deg G` and `h=w+1+j`.
- The quotient system contains `X=W_0/D`, which is nonzero on all anchor
  agreement points. This removes loops from every neighbor root matroid.
- Full splitting at exact degree `h` makes the evaluation kernel exactly the
  line spanned by the locator. No generic-rank assumption is imported.
- `(DA10)` counts each independent root basis only once. It does not count
  all root subsets as independent.
- `(DA11a)` uses all `(j+1)`-subsets for a different reason: two exact
  neighbor codewords cannot share more than `k-1` agreements, so their
  fixed-owner quotient root sets intersect in at most `j` points.
- Neither fixed-owner bound dominates uniformly; the theorem retains their
  minimum rather than silently assuming full projective rank.
- The exponential factor in `(DA12)` is printed rather than hidden. This is
  a bridge and a fixed-owner payment, not an L1 closure.
- No local large computation or Modal run is used.
