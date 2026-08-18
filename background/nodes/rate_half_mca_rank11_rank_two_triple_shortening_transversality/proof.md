# Proof

Rank two of `ev_T` on the five-space `B` gives `dim H=3`. Every polynomial
in `H` vanishes at the three distinct deployed coordinates of `T`, so their
squarefree locator `L_T` divides it. Division is injective and proves
`(RT1)`.

Every residual class counted by the triple incidence satisfies `B_i<=H`.
Its corrections therefore lie in

```text
V=span(PH),       dim V<=dim P dim H=6.                 (1)
```

If `dim V<=4`, chronology-safe ownership puts every first-owned slope in
one correction space of dimension at most four. The exact cap is
`R_4=63397365764`, contradicting `M_T=388650911452`. Thus
`dim V in {5,6}`.

All three coordinates are anchor-good, and every associated explanation
equals the anchor and received pair there. Since `3<K<m`, the same-record
exchange argument supplies an actual noncontained size-`m` witness through
`T`: the size-`m` subsets containing `T` are connected by exchanges, and
pair containment on all of them would propagate one degree-`<K` pair to the
complete maximal support. The common-core cancellation and inverse lift
therefore preserve slopes and pair noncontainment and give `(RT2)`.
Multiplication by `L_T` is injective, so the correction dimension is
unchanged. Each counted residual class had a selected set of `37736` common
zeros containing `T`; after deletion at least `37733` remain.

It remains to apply the support-local compiler. On the shortened row,

```text
n'=2097149, K'=1048573, m'=1116045, w=m'-K'=67472.
```

For correction rank `r` and margin `theta`, its exact bound is

```text
floor(max{
 (n')_(r+1)/(m' theta (w+1)^(r-1)),
 (n'-K'+r)_(r+1)/(theta (w+1)^r)
}),                                                     (2)
```

where the first factorial is falling and the denominator products are
rising. Exact integer evaluation gives

```text
r=5, theta=  9: 408591854341
r=5, theta= 10: 367732668907 < M_T,
r=6, theta=294: 388738149260
r=6, theta=295: 387420392821 < M_T.                    (3)
```

The compiler's `theta` is the minimum support-wise discrepancy, truncated
only at `w+1=67473`. If rank five had `theta>=10`, or rank six had
`theta>=295`, `(2)` and `(3)` would contradict the retained bucket mass.
Therefore the untruncated discrepancy is at most 9 or 294 respectively,
which proves `(RT3)` and `(RT4)`. QED.
