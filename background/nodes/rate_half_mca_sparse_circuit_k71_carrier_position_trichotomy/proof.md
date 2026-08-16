# Proof

Write `v_x` for evaluation at a domain point as a functional on `V`.  The
empty common-zero hypothesis makes every `v_x` nonzero.  If `A_2={a}` is
an attaining support-two deletion, every completion is parallel to `v_a`.
Conversely, every domain evaluation parallel to `v_a` completes `a` to a
two-circuit.  Thus `B_2` is the full ground-set intersection with one
projective point `P`, and `|B_2|=M_2+1`.

Let `A_c`, `c=3,4`, be an attaining independent deletion and let
`F_c=span{v_x:x in A_c}`.  If `P` is not contained in `F_c`, then
`B_2` is disjoint from `B_c`.  The two vanishing spaces have dimensions
`9` and `11-c`, so

```text
dim(H_2 intersect H_c) >= 9+(11-c)-10=10-c.       (1)
```

Now suppose `P<=F_c`.  Then every polynomial vanishing on `A_c` vanishes
on `P`, so `H_c<=H_2`.  If `P` is the projective point of one anchor, the
chosen anchor is the only point of `B_2` in `B_c`: any second parallel
point would make a two-circuit inside the purported support-`c` circuit.
If `P` lies in the span of a proper subset of rank at least two, no point
of `B_2` is an exact support-`c` completion, because that proper subset
already becomes dependent.  Finally, if `P` lies in no proper deletion
span, every point of `B_2` completes `A_c` to a minimal support-`c`
circuit.  This last case forces

```text
M_c >= |B_2|=M_2+1.                               (2)
```

For `c=3`, `(1)` and the anchor case give `(PT1)`.  If `M_3<=M_2`,
`(2)` excludes the completion position.  In the transverse case the
seven-dimensional fixed space vanishes on `b_2+b_3` points; in the anchor
case the eight-dimensional `H_3` vanishes on `b_2+b_3-1` points.  The
common-root bound in either case gives `s_2+s_3>=q`, so smaller defect sums
are impossible.

Assume now `M_3=M_4=M_2+1`.  If support three is transverse or anchored,
the first two alternatives of `(PT2)` follow from the preceding paragraph.
Otherwise all `M_3=|B_2|` completions are precisely `B_2`, and

```text
B_3=B_2 union A_3.                                  (3)
```

Apply the same position analysis to `A_4`.  Its transverse and anchor
cases give `T24` and `A24`; the proper-subspan case is stronger than
`T24`.  In the remaining case all support-four completions are `B_2`, so

```text
B_4=B_2 union A_4.                                  (4)
```

Both `H_3` and `H_4` now lie in the nine-dimensional space `H_2`; hence

```text
dim(H_3 intersect H_4) >= 8+7-9=6.                 (5)
```

The anchor sets `A_3` and `A_4` cannot share both points of `A_3`, because
then `P<=span(A_3)` would lie in a proper span of `A_4`, contradicting
that every point of `B_2` is an exact support-four completion.  If they
are disjoint, `(3)--(5)` give `(u,g)=(M_2+6,6)`.  If they share one anchor
`x`, then `span(A_3)=span(P,x)<=span(A_4)`, so `H_4<=H_3`; this gives
`(u,g)=(M_2+5,7)`.  These are `N34` and `N34A`, and the six cases are
exhaustive.  QED.
