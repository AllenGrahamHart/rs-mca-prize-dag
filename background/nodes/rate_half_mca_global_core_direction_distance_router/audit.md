# Audit

The primary checker validates the pinned source files and scans every
official `s` in the two direction-distance ranges.  It derives the exact
paid threshold from strict integer inequalities, checks both boundary
defects, and identifies the global maximum paid bound.

The independent checker reconstructs the threshold by direct denominator
and cross-product tests for every candidate `j`.  It separately derives the
positivity walls and the thirteen Mersenne spike cells, then rejects four
contract mutations.

Both checks are small integer loops under RAMguard.  No Modal compute is
used.
