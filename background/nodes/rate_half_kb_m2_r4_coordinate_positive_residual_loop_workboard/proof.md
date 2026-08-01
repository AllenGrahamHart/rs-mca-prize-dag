# Proof

For a cross-pair orbit occurring `m` times, split its records between the
two signed target edges.  Each record contributes weight two, so its least
possible collision defect is

```text
min_(0<=s<=m) [2 binom(s,2)+2 binom(m-s,2)].       (1)
```

This is `0,0,2,4` for `m=1,2,3,4`; every loop contributes defect one.
Applying `(1)` to the ten common orbits already proved by the loop gate
gives the defect column of `(KBPRW-1)`.  The global loop cap deletes the
four rows with two or three loops.  The remaining `442-1a` row has one
loop and a multiplicity-four cross pair, hence defect `1+4=5>3`.  The five
printed common orbits are exactly what remains.

The source-facet signature pairs ten outside `I-I` stars into five edge
orbits and four `I-J` stars into two colored edge orbits.  Every outside
target pair has degree four.  These facts give `(KBPRW-2)`.  The global
loop theorem permits no outside loop if a common loop is present and at
most one otherwise.  Exhausting the finite nonnegative solutions to
`(KBPRW-2)` yields six loop-free labeled rows in the two `O0` orbits and
eighteen one-loop labeled rows in the four `O1` orbits.  Formula `(1)`
plus the loop debit gives exactly the defects in `(KBPRW-3)`.

Finally add each outside defect to its common-row defect.  Retain a pair
exactly when the sum is at most three and its total loop count is at most
one.  Direct substitution gives the thirteen entries of `(KBPRW-4)`.  The
checker exhausts all integer ranges, verifies permutation closure, and
replays every degree and defect equation. QED.
