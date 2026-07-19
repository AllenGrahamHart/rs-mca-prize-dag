# Audit

The lift subgroup has order `2d`, not `d`: the deleted roots are the squares
`b_i=a_i^2`. Distinct `b_i` excludes both equality and antipodality among the
chosen lifts.

Cross-ratio `-1` depends on ordering, but its six-value orbit is invariant.
The router permits relabeling before applying `(HFR2)`.

The fourth root used to define `Z` exists because the split pure outer quartic
provides a fourth power up to `-1`, and the official field contains eighth
roots of unity.

Complete tiny scans over lift subgroups of orders `8,16,32,64,128` find
respectively `0,4,40,500,3660` normalized non-antipodal harmonic sets. Thus a
claim that harmonicity alone empties the pure stratum would be false in the
finite-field setting. These counts are replayed by `verify_audit.py` and are
not used in the proof.
