# Proof

Let `m=B(-t^2)/A(-t^2)` be the source-forced missing product. In pairings
`0,1,2`, the first residual pair is the same in all three cases. If a
positive `DE` record is missing, it is `(m,-m)`; if `-DE` is missing,
it is `(-m,-m)`. The exact pair-resultant equation therefore gives the
necessary target-free cuts

```text
P(m,-m)=0,             P(-m,-m)=0.                (DE11-1)
```

Reduce each cut in the proved quadratic-in-`t`, quadratic-in-`b` common
algebra and take its four-dimensional multiplication norm over `F_p(r)`.
For each of four source-sign lanes, the positive cut has degree `400` and
seven deployed roots; the negative cut has degree `408` and four deployed
roots. Unioning these roots with every inverse numerator and denominator
root gives 11 positive and 9 negative candidates per sign, 80 case-labeled
candidates in total.

Direct replay through the original common tower accounts for all 80
candidates. The exact aggregate is 56 route-guard exits, eight
`b`-leading exits, 40 fibers with no deployed lift, and 32 finite guarded
rows. The parent common-locus theorem proves that each leading exit has no
deployed point. Of the finite rows, 16 have `A(-t^2)=0` and
`B(-t^2)!=0`, while direct evaluation makes the appropriate cut in
`(DE11-1)` nonzero at the other 16. No witness or unresolved branch
remains.

An independent implementation computes `gcd(f,r^p-r)` for the target norm
and every inverse-guard polynomial, factors only the square-free root part,
and recovers exactly the same 80 candidate unions across 72 profile visits.

The exchange of the two identical positive `DE` records pays both positive
missing roles, while the negative cut pays `xi=2`. Since the source cut
precedes all target variables, it pays pairings `0,1,2` simultaneously.
Hence all nine labels are empty. QED.
