# Audit - M31 rank-seven two-block incidence router

## Load-bearing checks

1. `B_i` deletes the already fixed line `S`; otherwise the pairwise degree
   bound would double-count common roots.
2. The planted and external domains are disjoint, so their common-agreement
   intersections add before applying the degree bound.
3. The tail argument chooses constant-size subsets before applying Cauchy;
   it does not replace varying support sizes inside a nonmonotone expression.
4. The mean inequality counts unordered pair intersections exactly once.
5. Fixed-`G` singleton rigidity is used only at `q>=k`.

## Dependency status

- **Imported from the source packet:** normalized-label representation,
  split squarefree `P,G_i`, zero excess, `S subset Z(H_i)`, and the exact
  deployed constants.
- **Proved here:** (TB1)--(TB5).
- **Unproved:** the middle-band aggregate upper bound and every global
  payment.

## Verdict

**GREEN locally / OPEN GAP globally.** The previous 19-slice scalar picture
is superseded for this terminal by a distinct-locator middle-band census.
