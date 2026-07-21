# Claim contract

- **claim:** an official `c=2` denominator already containing one antipodal
  pair has an exact sign-free `(X,P)` primary/torsion circuit, and `X=0` is
  exactly the second antipodal pair.
- **scope:** the maximal official normalized `c=2` denominator-mismatch
  chamber with `N=2^40`.
- **dependencies:** the normalized gap compiler and official torsion-field
  router.
- **falsifier:** an exactly-one-antipodal packet for which `(OAR3)--(OAR7)`
  fails, or a passing square `(X,P)` circuit that does not reconstruct the
  claimed root packet.
- **nonclaims:** the circuit is not proved empty; the secondary gap,
  canonical span, completion coupling, and the antipodal-free stratum remain
  open. C2-PAR is not promoted.
