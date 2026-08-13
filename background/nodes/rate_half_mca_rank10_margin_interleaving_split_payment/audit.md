# Audit

The main proof-risk points were checked explicitly:

1. The low-margin condition is applied slope by slope; it is not inferred
   from the existence of one exceptional support.
2. The high and low parts are disjoint subfamilies, so their caps may be
   added.
3. Passing to the affine span of the high part only shrinks the direction
   space, hence cannot lower its support-local margins.
4. The low pair lies in `(c_0+C') x C'`; translating the first component
   makes the interleaving theorem applicable to the linear code `C'`.
5. The multiplicity factor is `n-A`, not a moment or an assumed slope
   count: pair noncontainment supplies an actual exception coordinate and
   the support equation recovers the slope.
6. The primary verifier includes the direct rank-zero cap and maximizes the
   high cap over every rank `0..9`,
   scans every legal threshold, and checks `M^2<|F|` before using collapse.
7. The independent verifier reconstructs the three decisive thresholds
   and the rank-eleven nonpayment without importing primary code.

The exact scan is small constant-memory integer arithmetic and requires no
Modal computation.
