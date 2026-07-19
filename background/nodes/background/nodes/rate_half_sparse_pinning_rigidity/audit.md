# Audit

The reduction uses the maximal agreement locus of one witness polynomial. It
does not select unrelated codewords at different active coordinates. The
same radius budget simultaneously pays unmatched support positions and
off-support weight, producing `(PR3)`; replacing this by independent value
sets would lose the load-bearing coupling.

The tiny verifier enumerates every sparse pair, slope, and maximal failing
witness for an `RS[F_5,D,1]` row. It checks tangent exhaustion below the
support threshold, active pinning, the root/cofactor bound, match rigidity,
and the at-most-`A` slopes per ambiguity polynomial. It also checks the exact
official tangent-budget arithmetic.
