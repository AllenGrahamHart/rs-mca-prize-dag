# Audit

- The joint charge uses actual unknown core sizes only through a proved upper
  bound on their sum; it does not replace them by the forced lower bounds.
- Convex concentration is applied to the unfloored rational line cap, then
  floored once because the total number of slopes is integral.
- The residual target is `B-L_r`; using an upper bound on removed slopes
  preserves the strict unsafe inequality.
- Only positive forced-core lower bounds enter the packing subtraction.
  Zero lower bounds are represented by empty subsets.
- At the adjacent row the threshold drop to `13` is monotone because the
  joint charge is nondecreasing and the deficit ceiling no longer changes.

The independent audit uses exact rational arithmetic.  The full C replay
uses fixed-size arrays below 1 MiB and runs under RAMguard.
