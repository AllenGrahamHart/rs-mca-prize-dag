# Audit

The primary verifier derives the recursive envelope independently from the
checkpoint list, checks monotonicity in the defect, and validates every
checkpoint and four mutations.

The second verifier uses exact rational comparisons for the direct bound and
reconstructs the recursion in the opposite loop order.  It checks the number
of defects extended beyond the affine base and the maximum extension depth.

The loops use constant-size integer state under RAMguard.  No Modal compute
is used.
