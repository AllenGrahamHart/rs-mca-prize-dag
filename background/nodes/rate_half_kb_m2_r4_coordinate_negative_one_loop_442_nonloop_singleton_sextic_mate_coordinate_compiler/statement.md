# KoalaBear m2 r4 coordinate negative one-loop 442 nonloop-singleton sextic mate-coordinate compiler

- **status:** PROVED
- **scope:** the four rank-six sextic common quotients for matching orbit
  `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_quotient_classifier`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_explicit_involution_compiler`
- **consumer:** `rate_half_band_closure`

In every sign row, both rational denominators needed for the outside
involution interface are units in the rank-six quotient:

```text
Norm(D_c)=2^19,
Norm(D_m)=652=4*163,                               (KB41M-1)
```

where

```text
D_c=b(r^2+1)^2+r^4-6r^2+1,
D_m=b^3-b^2c+3bc+c^2.
```

In the representative sign row `(epsilon_1,epsilon_2)=(1,1)`, with basis
`(1,b,b^2,r,br,t)`, the reconstructed target product is

```text
c=-1+b-b^2/2+(i-1)r/4+(1-i)t/4,                 (KB41M-2)
```

and the forced singleton mate is

```text
163m=(50-54i)+(87+54i)b-(126+54i)b^2
     +(30+12i)r+(-54+54i)br+(12+30i)t.           (KB41M-3)
```

The other sign rows have the same two norms and are obtained by their exact
rank-six reductions.  Thus every forced-value and `Phi` template can be
evaluated using six-coordinate multiplication matrices, with no rational
or saturation branch.

This theorem does not evaluate any outside matching template, impose
outside sums or interpolation, classify another common orbit, close the
coordinate orientation or a row, or prove either Prize result.

## Falsifier

A sextic sign row where either denominator is a zero divisor, or failure of
the representative coordinate identities `(KB41M-2)--(KB41M-3)`.
