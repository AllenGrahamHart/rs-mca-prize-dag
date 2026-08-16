# Support-2/3/4 carrier-position trichotomy

- **status:** PROVED
- **correction dimension:** `10`
- **payment specialization:** `K'=71`

Let `M_c=q-s_c>0` be exact support-`c` completion maxima, with attaining
carriers `B_c`.  The support-two carrier is one full nonzero parallel class
of size `b_2=M_2+1`.

For an attaining support-`c` deletion, `c=3,4`, the projective point of
`B_2` is in exactly one of the following positions.

1. It is outside the span of the deletion.  Then `B_2` and `B_c` are
   disjoint and `H_2 intersect H_c` has dimension at least `10-c`.
2. It lies in the span of a proper deletion subset.  Then `H_c<=H_2`.
   The carriers share one anchor if the subset has rank one and are
   otherwise disjoint.
3. It lies in the deletion span but in no proper deletion span.  Then every
   point of `B_2` is an exact support-`c` completion, so
   `M_c>=M_2+1`.

Hence, when `M_3<=M_2`, only the first two positions occur.  Their fixed
unions have respectively

```text
(u,g)=(b_2+b_3,7), (b_2+b_3-1,8),                 (PT1)
```

and `s_2+s_3<q` is impossible.

When `M_3=M_4=M_2+1`, the remaining completion position is exhausted by
the following six fixed-union alternatives:

```text
T23:  (u,g)=(2M_2+4,7)       A23:  (2M_2+3,8)
T24:  (u,g)=(2M_2+5,6)       A24:  (2M_2+4,7)
N34:  (u,g)=(M_2+6,6)        N34A: (M_2+5,7).     (PT2)
```

Each pair `(u,g)` feeds the fixed-union multicarrier collision charge.
At `K'=71`, `(M_2,M_3,M_4)=(29,30,30)`, so `(PT2)` gives unions
`62,61,63,62,35,34`.

## Falsifier

A support-two carrier containing two nonparallel evaluations; a carrier
position outside the three listed projective cases; an exact support-`c`
completion containing a smaller circuit; or a nested support-three and
support-four anchor pair sharing two anchors.
