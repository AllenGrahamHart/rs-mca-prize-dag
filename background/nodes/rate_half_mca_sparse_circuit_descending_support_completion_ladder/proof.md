# Proof

The universal completion theorem gives `0<=M_c<=q` for every source
support.  At stage `c`, either

```text
M_c in {q,q-1,...,q-(9-c)},
```

in which case there is a unique defect `s=q-M_c` in `0..9-c`, or

```text
M_c<=q-(10-c).
```

These alternatives are disjoint and exhaustive.  In the second alternative
retain its deletion ceiling and descend to `c-1`.  The source sequence
`5,4,3,2` therefore contributes `5,6,7,8` terminal alternatives and one
all-fallback alternative, for 27 leaves total.

At a terminal `(c,s)` leaf, choose a deletion attaining `M_c=q-s`.  The
cross-support completion-defect carrier theorem confines every support-`d`
circuit whenever

```text
c+(s+1)d-s-1<=10.
```

The same branch also has the ordinary source deletion ceiling `q-s`.
Every fallback ceiling inherited from an earlier stage remains valid and
may be intersected with these new caps.  If all four stages fall back, the
retained ceilings are `q-5,q-6,q-7,q-8`, respectively.  This proves the
claimed ladder.  QED.
