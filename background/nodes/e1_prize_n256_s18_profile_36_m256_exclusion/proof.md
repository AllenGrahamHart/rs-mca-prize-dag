# Proof

Write the positive-half integer autocorrelation as `(A_d)_(1<=d<64)` and put

```text
E=sum_d A_d^2,          L=sum_d |A_d|.
```

The energy-adaptive parent leaves `E=2,...,23` for `m=256`.

## Exact product chambers

Let `q` be the weight of the autocorrelation parity mask. For each integer
magnitude partition of `E`, the certificate computes its exact `q` and `L`.
It then applies the parent product extremum with the sharper conjugate cap

```text
y_u <= min(144,18+2L).
```

Every square root is enclosed between consecutive rationals of denominator
`2^192`. Across 27176 exact rational comparisons, the certificate excludes
45 `(E,q,L)` triples and leaves 45. In particular, every chamber with
`E=21,22,23` is excluded; the live list ends at `E=20` and is pinned in the
certificate result.

## Complete multiplicity-eight atlas

Every six-term parity support contains an odd-separated pair. Translation
and an odd Galois multiplier normalize that pair to `{0,1}`. Enumeration of
all `binom(126,4)=10009125` normalized supports finds exactly 87856 with
multiplicity eight. Their odd-chord weights and raw counts are

```text
q=1:16, 3:288, 5:256, 6:128, 7:3584, 8:384, 9:8480,
q=10:3712, 11:26208, 12:1920, 13:8064, 14:10240, 15:24576.
```

Affine canonicalization leaves 5920 orbits, split as

```text
q=1:4, 3:32, 5:24, 6:8, 7:236, 8:24, 9:608,
q=10:296, 11:1648, 12:152, 13:504, 14:848, 15:1536.   (1)
```

## Complete radius search

Fix one orbit and singleton-sign assignment. On a parity-even lag, divide the
autocorrelation congruence by two modulo two. If an exact vector has energy
`E`, the number of such lags on which `A_d/2` is odd is at most

```text
r=(E-q)/4.                                               (2)
```

Taking the maximum of (2) over the 45 live triples gives radius three for
`q in {1,3,5}`, radius two for `6<=q<=12`, and radius one for
`13<=q<=15`.

For each possible third heavy position, the engine seeks a pair whose XOR
syndrome is within Hamming radius `r` of the required syndrome. Partition the
parity-even lag bits into `r+1` blocks. Any syndrome at distance at most `r`
agrees with the target on at least one whole block, so indexing pairs by every
block is exhaustive. The primary engine uses unordered multimaps; the audit
engine independently sorts each block table and uses binary equal ranges.
Both deduplicate heavy triples, replay all eight heavy-sign choices, recompute
the full integer autocorrelation, and retain only a certified `(E,q,L)` row.

The engines agree exactly:

```text
affine orbits:              5920
singleton sign choices:  189440
third-position queries: 23111680
block bucket hits:      2061796568
radius matches:          12206580
candidate heavy triples:  2833260
exact heavy-sign tests:   22666080
product-live vectors:           54
live energies: E13=8, E15=6, E17=12, E19=28.          (3)
```

## Exact norms

The 54 vectors in (3) are distinct. FLINT resultants and independent PARI/GP
resultants agree entry by entry. Every norm has 2-adic valuation eight. The
largest quotient is

```text
67404590334226659516226521627034983611828304342200684420570670966820124685313,
```

strictly below `B_P 2^128`. A cofactor-256 collision would have
`Norm(F)=256p` with `p>=B_P 2^128`, a contradiction.
