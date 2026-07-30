# Proof

By `(KBDM-9)`, the quartic indexed by `tau(eta)` is `q^2`, where
`q=P_(J_1)` is reduced. Both of its component stars are therefore `q`.
Whole-fiber transport gives the reciprocal square at `eta`, whose two stars
are `tau(q)`. The supports lie in disjoint label sets `J` and `I`, so these
are distinct vertices and contribute defect two.

If either vertex occurred once more, its contribution would rise from
`binom(2,2)=1` to `binom(3,2)=3`; together with the other doubled vertex the
total would be at least four. Thus both weights are exactly two and only one
defect unit remains. This proves `(KBS2-1)`.

The internal `K` orbit contains two labels and hence four reduced component
stars. By `(KBDM-4)` they are edges on `J_0`. The two remaining common-`K`
quartics transported to `L^c` have exactly two `J_1` roots each. If either
quartic had a `J_1-J_1` factor, that factor would be `q`, forbidden by the
preceding paragraph; its other factor would be on `J_0`. Therefore each
quartic instead has two `J_0-J_1` factors. Since both labels of `J_1` have
total common-`K` degree four and `q^2` contributes degree two to each, the
four mixed factors use each `J_1` label twice.

Pure and mixed edges are distinct vertex classes. Their collision defects
must sum to at most the one remaining unit, proving `(KBS2-2)`. The four
pure edges contribute eight `J_0` incidences and the four mixed edges four
more. The universal bounds `2<=d_j<=4` therefore give four integers in
`[2,4]` summing to twelve. Their three sorted partitions are exactly
`(KBS2-3)`.

For completeness, enumerate multisets of four edges from the six pure edges
and four edges from the eight mixed edges. Retain exactly those with mixed
`J_1` degrees `(2,2)`, total `J_0` degrees in `[2,4]`, and collision defect
at most one. This gives `1,560` labeled packets. The centralizer of the two-
pair involution on `J_0` has order eight; adjoining the swap of `J_1` gives
an order-16 group. Canonical orbit reduction gives `123` orbits, and an
independent Burnside calculation reproduces the same number.

In the source-line branch, `(KBDS-3)` pairs the four pure stars under the
involution on `J_0`. Hence nonfixed edge weights agree and each fixed edge
has even weight. If a mixed edge repeated, applying the source-line lift to
its two occurrences would repeat the same transported `I-J` edge. The two
collisions would exceed the one-unit residual budget. Thus the mixed edges
are distinct. Reapplying the exact multiset enumeration with these two
conditions leaves `96` labeled packets and `12` orbits. The transported
partners are four `I-J` stars, exactly the universal category count. QED.
