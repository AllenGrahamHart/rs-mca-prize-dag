# Rank-eleven factor-flag two-threshold residual route wall

- **status:** PROVED
- **scope:** the exact ordered-basis charge family inside the `2 x 5`
  factor-flag router

Refining the residual transversality split by a second rich-flat threshold
cannot improve the proved `18166`-coordinate output.

For factor cutoff `T`, put `b=38385-T+1`. Choose thresholds
`0<=h<S<=b`. A residual `B_i` is either `h`-transverse, has a proper flat
containing between `h+1` and `S-1` of its at least `b` zero columns, or emits
a proper flat with at least `S` columns. In the intermediate branch, greedy
completion from one rich-flat label gives the additional class caps

```text
dim(B_i)=2: floor(m_fall_3 / ((h+1)(b-S+1)^2)),
dim(B_i)=3: floor(m_fall_2 / ((h+1)(b-S+1))).
```

If `S>=18167` and the intermediate band is nonempty, these two terms alone
cost at least

```text
187184 R_4 + 3381 R_6
=66303977459889028,
```

which exceeds the complete residual allowance `65167969673715470` by
`1136007786173558`, before any factor-heavy or transverse charge. If the
intermediate band is empty, `h=S-1` and the formula is exactly the original
one-threshold scan, whose largest payable output is `S=18166`.

Thus no member of this two-threshold ordered-basis charge family emits a
stronger residual flag than the existing router.

## Nonclaim

This is a route wall, not a counterexample to stronger factor synchronization,
Wronskian collision, weighted incidence, or chronology arguments.
