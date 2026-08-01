# Proof

The loop-ramification parent proves that a three-loop packet has two loops
at the ramified quotient values and one at the unique root of the nonzero
linear form `B_1`.  A positive outside loop would either reuse a ramified
quotient label or give a second nonramified root of `B_1`; both are
impossible.  Thus all five outside internal records are cross edges.

The source-facet census supplies exactly two colored edge orbits and five
internal `I-I` edge orbits.  On the outside signed pairs, degree four gives

```text
r_D+m_DE+m_DF=4,
r_E+m_DE+m_EF=4,
r_F+m_DF+m_EF=4,
sum r_i=2,       sum m_ij=5.                      (1)
```

Exact nonnegative enumeration of `(1)`, modulo `S_3`, has only

```text
(0,0,2;3,1,1),       (0,1,1;2,2,1),              (2)
```

each with orbit size three.

Each common antipodal edge orbit contributes target-edge weight two and
defect one.  The three common loops therefore spend the entire defect
budget three.  For a cross pair there are only two signed deck-orbit types.
A multiplicity-three cross pair distributes as `2+1` at best; the repeated
type repeats two target edges and contributes additional defect

```text
2*binom(2,2)=2.                                   (3)
```

Therefore the first record in `(2)` is impossible.  In the second, each
multiplicity-two pair must use its two different signed types, producing no
additional defect; the multiplicity-one pair is free.  This proves
`(KBP3S-1)` and its sign description.

The colored common-pair attachments are forced by the profile deficits:
`(4,4,2)` has two deficits on its degree-two pair, whereas `(4,3,3)` has
one on each degree-three pair.  This proves the final assertions. QED.
