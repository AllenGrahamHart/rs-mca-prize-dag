# KoalaBear m2 r4 positive coordinate loop-ramification gate

- **status:** PROVED
- **scope:** every positive-parity coordinate-order-two component in the
  residual `(m,r,delta)=(2,4,2)` row
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler` and
  `rate_half_kb_m2_r4_coordinate_k_fiber_vieta_rank_compiler`
- **consumer:** `rate_half_band_closure`

Let `l_i` count the common-`K` antipodal edge orbits on the three signed
target pairs.  Every positive coordinate packet satisfies

```text
l_i<=1 for i=0,1,2.                                (KBPQ-1)
```

The linear odd coefficient `B_1` is nonzero.  Every nonramified loop label
is a root of `B_1`, so at most one loop is nonramified.  Consequently a
two-loop skeleton uses at least one of the two ramified quotient values,
and a three-loop skeleton uses both.

Solving the degree equations under `(KBPQ-1)` gives exactly ten orbits and
thirteen labeled skeletons:

```text
(4,4,2):
  (0,0,0;3,1,1), (0,0,1;4,0,0),
  (0,1,0;2,2,0) [orbit 2],
  (1,1,0;1,1,1), (1,1,1;2,0,0);

(4,3,3):
  (0,0,0;2,2,1),
  (0,0,1;3,1,0) [orbit 2],
  (1,0,0;1,1,2),
  (1,0,1;2,0,1) [orbit 2],
  (1,1,1;1,1,0).                                 (KBPQ-2)
```

The orbit-two action swaps the equal-degree target pairs.  This census does
not assume product injectivity; cross-pair multiplicities three and four
are retained.

This theorem does not delete a skeleton, classify its common product/q
rows, exclude positive coordinate parity, close another orientation, close
a Prize row, or prove either Prize result.

## Falsifier

A positive packet repeating one antipodal edge type, with `B_1=0`, with two
nonramified loop labels, or with a degree skeleton outside `(KBPQ-2)`.
