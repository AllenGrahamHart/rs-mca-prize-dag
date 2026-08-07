# Audit

Two exact implementations use different enumeration organizations.

1. `verify.py` groups every subset by its elementary-prefix tuple and counts
   disjoint pairs inside each bucket.
2. `verify_audit.py` groups every record by its union and enumerates
   complementary set partitions directly.

Both use integer arithmetic reduced modulo 17 and assert the full census,
the witness coefficients, the absent width-2 subrecord, the non-null guard,
and the numerical pigeonhole obstruction.  The second script does not call
or import the first.

The mathematical conclusion is deliberately narrower than the computation:
the scripts do not implement the official first-owner strips, so the node
cuts only universal/strip-free minimalization routes.
