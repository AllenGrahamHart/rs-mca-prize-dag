# Frontier

This exhausts every case reachable from the target-free first pair of the two
residual `DE` records.  For pairing indices `3,...,14`, those records are
separated, so the existing common-point ledgers do not apply directly.

The `xi=3,pairing=0` colored/missing-sum common resultant was attempted by
both an `8 x 8` Sylvester determinant and a degree-four Euclidean resultant.
Each one-sign pilot hit the 300-second cap; the Euclidean run reached two
quartic cuts after 117 seconds but did not finish their resultant.  This is a
computational route no-go, not evidence about truth.

Pairing index 3 is now paid by `(KBP1B3-DE-P3-1)`.  Next compare:

1. adapt its FLINT-backed nested-quadratic and exceptional-root replay to
   pairing index 4; or
2. derive a lower-degree subresultant or exploit the shared-`f` structure for
   `xi=3,pairing=0`.
