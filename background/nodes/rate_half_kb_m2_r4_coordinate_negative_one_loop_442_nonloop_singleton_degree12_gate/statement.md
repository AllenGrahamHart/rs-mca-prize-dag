# KoalaBear m2 r4 coordinate negative one-loop 442 nonloop-singleton degree-12 gate

- **status:** PROVED
- **scope:** the cubic-root common-`K` rows for the one-loop `(4,4,2)`
  matching orbit `[9,10,12,13]`
- **dependency:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_cubic_root_gate`
- **consumer:** `rate_half_band_closure`

In every root-sign row, the remaining common product equation and q weld
force

```text
G(b)=0,                                               (KB41D-1)

G(B)=(B^3-B^2-B-1)(B^3+B^2+B-1)
     (B^6-2B^5+7B^4-8B^3+7B^2-2B+1).
```

Together with the parent cubic for `r` and its rational formula for `c`,
this makes the common-`K` locus finite: before guards and coincidences,
there are at most `3*12*2=72` `(r,b,t)` triples per root-sign row, since
the remaining product equation is quadratic in the singleton root `t`.

This condition is exact as a necessary gate and includes all coefficient-
degenerate branches of the two singleton equations.  It does not assert
that every root of `G` is realizable.  The guarded `F_41` common witness has
`b=10` on the sextic factor, so the orbit remains live.

This theorem does not impose outside products or q equations, classify the
other common matching orbits, close the coordinate orientation or a row, or
prove either Prize result.

## Falsifier

A guarded common-`K` packet in the cubic-root orbit with `G(b)!=0`, or a
coefficient-degenerate branch omitted by the direct resultant.
