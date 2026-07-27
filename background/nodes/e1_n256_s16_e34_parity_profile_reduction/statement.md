# E1 N=256 E=34 parity-profile reduction

- **status:** PROVED
- **closure:** proof

Let a pair-feasible folded vector have coefficient profile `(3,4,0)` and
positive-half autocorrelation variance `V=68`. Then its autocorrelation
magnitude profile is exactly

```text
(n_1,n_2,n_3,...)=(6,7,0,...).                         (1)
```

Moreover, the six chords joining the four coefficient positions of absolute
value one have six distinct non-diameter circular lengths. Thus those four
positions form a circular Sidon set for unoriented differences modulo 128.

If `D_64` is the diameter square mass and `C` is the signed equal-chord cross
sum, then

```text
D_64 in {0,4,8,12,16,20},
C in {-34,-32,-30,-28,-26,-24},
C=-34+D_64/2.                                         (2)
```

This theorem does not exclude profile `(6,7)`, classify its 41 relaxed slack
signatures, or prove a value-set lower bound.
