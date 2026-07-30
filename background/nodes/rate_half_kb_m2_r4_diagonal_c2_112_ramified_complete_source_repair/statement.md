# KoalaBear m2 r4 diagonal c2 (1,1,2) ramified complete-source repair

- **status:** PROVED
- **scope:** saturated source-line `(1,1,2)` packets whose forced square
  orbit is the source branch orbit
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_112_source_line_odd_part_incidence_gate`
  and `rate_half_kb_m2_r4_source_row_interpolation_compiler`
- **consumer:** `rate_half_band_closure`

Orient the ramified reciprocal orbit as `w=0`, and put
`q(T)=P_(J_1)(T)`. The square fiber gives `U(T,0) in <q>`. Complete-source
row divisibility and local saturation sharpen this to

```text
U(T,0) in <q>,       V(T,0) in <q> minus {0}.       (KBRC-1)
```

Indeed the two endpoint rows indexed by the roots of `q` each have order
at most two at `X=0`, while their total order is four; both orders are
therefore exactly two. Thus the coefficient cut has rank four even at the
ramified square orbit, and the reciprocal source spaces have dimensions

```text
epsilon=+1: 4,       epsilon=-1: 3.                (KBRC-2)
```

After scaling `V(T,0)=q(T)`, the odd part is the `w=0` instance of
`(KBOI-2)`. Consequently the internal common-`K` incidence equation
`(KBOI-3)` applies to the ramified forced-square branch as well. Every
saturated source-line `(1,1,2)` packet now has the same `4/3` coefficient
cut and four-case odd-part label gate.

This repairs the coefficient escape; it does not assert that the source
branch fiber is geometrically unramified, delete a packet, aligned or
near-aligned quotient system, biquadratic branch, exceptional orbit,
`(1,1,2)` row, owner, payment, row, or Prize result.

## Falsifier

A ramified forced-square actual packet for which a root row of `q` has
order below two at the source branch point, `V(T,0)` is not a nonzero
multiple of `q`, or the rank/dimension is not `4/3`.
