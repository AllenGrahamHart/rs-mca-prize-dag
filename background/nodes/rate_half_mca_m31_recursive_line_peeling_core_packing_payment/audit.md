# Audit

- Every peel is conditional on the residual exceeding its exact remaining
  budget; otherwise the line charge already proves safety.
- A selected slot has at least two members, so it determines an actual
  affine line and a codeword pair `(a,b)`.
- The entire selected line is removed before the bank is recomputed.  Later
  selected lines are therefore distinct even when absorption does not lower
  the deficit ceiling.
- Pairwise core intersection uses the nonzero difference of the codeword
  pairs, not an unproved direction-separation occupancy claim.
- The inclusion-exclusion test uses only a lower bound on each inside core
  and the proved pairwise intersection ceiling `K-1`.
- The adjacent row is retained as a method wall.  No unsafe or maximality
  statement is inferred from verifier failure.

The independent audit recomputes the endpoint arithmetic without importing
the primary verifier.  The C replay uses fixed-size arrays below 1 MiB and
runs under RAMguard; no Modal computation was required.
