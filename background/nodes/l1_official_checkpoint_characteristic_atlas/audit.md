# Audit - L1 official checkpoint characteristic atlas

1. The atlas contains only `p<n`; rows with `p>=n` have no checkpoint depth.
2. The range `13<=s<=44` uses both the official minimum order and the
   rate/dimension cap.
3. The extension degree need not equal `ord_n(p)`, but the order divides it.
   Testing the minimal order gives an exact possibility filter.
4. The order is a power of two because the unit group modulo `2^s` is a
   2-group; `f<=23` therefore reduces it to at most 16.
5. Formula `(CAT3)` enumerates 32 residues, including possible duplicates
   only as a set; the verifier checks cardinality 32 at every `s`.
6. Primality testing is deterministic in this range, not probabilistic:
   every candidate is below `2^44`, inside the seven-base `<2^64` theorem.
7. Atlas rows are possible generated-field pairs. A larger challenge field
   or a nonminimal extension does not create a new characteristic residue.
8. The 33 `m=1` rows close only the `t=p` stratum. They do not close higher
   widths or L1.
9. The 10 `m=2` rows first route through square-quotient complements; the
   exact abc classification then empties six and solves four explicitly.
10. No Modal run or large local computation is load-bearing.
11. The exact `n/2` statement concerns only `t=p` pairs at depths `p,p+1`.
    Higher-width collisions on the same four rows remain open.
12. The six other `m=2` complement sizes grow with `n`, but their
    minimum-width strata are theorem-empty rather than compute targets.
