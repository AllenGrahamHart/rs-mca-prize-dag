# Proof

Write the positive-half integer autocorrelation as `(A_d)_(1<=d<64)` and put

```text
E=sum_d A_d^2,          L=sum_d |A_d|,
q=#{d:A_d is odd}.
```

The energy-adaptive parent leaves `E=2,...,85` for `m=32`.

## Complete support reduction

Cofactor 32 forces multiplicity five in the six-singleton binary support. If
all singleton exponents had one parity, translation would write the support
polynomial as `G(x^2)`. Over `F_2`, `G(x^2)=G(x)^2`, so its multiplicity at
one would be even. Therefore every multiplicity-five support contains an
odd-separated pair. Translation and an odd unit normalize such a pair to
`{0,1}` in `Z/128`; global sign normalizes the coefficient at zero to `+1`.

Enumeration of all `binom(126,4)=10009125` supports containing `{0,1}` finds
317440 of multiplicity five. Affine canonicalization leaves 19840 orbits,
split by odd-chord weight as

```text
q=3:1, 4:6, 5:41, 6:24, 7:300, 8:148, 9:1430,
q=10:480, 11:4061, 12:358, 13:4097, 14:904, 15:7990.   (1)
```

## Exact product chambers

Nine nonzero coefficients create at most `binom(9,2)=36` nonzero
positive-half autocorrelation classes. The certificate enumerates every
integer magnitude partition of `E=2,...,85` with at most 36 classes and every
parity weight in (1). It applies the exact product extremum with

```text
y_u=|F(zeta^u)|^2 <= min(144,18+2L).
```

Square roots are enclosed between consecutive rationals of denominator
`2^192`. Across 173683 exact rational comparisons, 1360 of the 1834
`(E,q,L)` chambers are excluded and 474 remain. Every live chamber has
`E<=60`. The q-specific energy frontiers are

```text
q=3:55, 4:56, 5:57, 6:58, 7:55, 8:56, 9:57,
q=10:58, 11:59, 12:60, 13:57, 14:58, 15:59.            (2)
```

## Dual complete radius search

On a parity-even lag, an odd value of `A_d/2` costs at least four units of
energy. Thus any vector in a live chamber has syndrome radius at most

```text
r=floor((E-q)/4).                                       (3)
```

The primary engine scans every heavy-position triple and all 32 normalized
singleton-sign assignments, applies (3), and replays all eight heavy-sign
choices exactly. The audit reverses both outer orders, constructs its chord
columns separately, and directly rebuilds the full nine-term autocorrelation
for every low-energy survivor. A third reverse hash-block engine agrees on a
representative orbit at every parity weight.

The two complete engines agree on all proof-relevant totals:

```text
affine orbits:                  19840
singleton sign assignments:   634880
raw heavy-position triples: 5857561600
singleton-sign distance tests: 187441971200
unique radius triples:          84923111400
exact heavy-sign tests:        679384891200
low-energy vectors:               339892636
product-live vectors:             239131808.            (4)
```

## Certified norm separation

For all 64 odd roots and 128 positions, a 100-decimal generator rounds real
and imaginary components after scaling by `2^48`. A separate 256-bit
python-flint/Arb audit proves, in 16384 component checks, that every scaled
rounding error is strictly less than one.

Each vector has coefficient `L1` norm 12. Therefore summing the fixed root
table gives real and imaginary errors strictly below 12. Integer lower and
upper bounds for each squared modulus are multiplied over all 64 roots and
compared with the exact scaled bounds

```text
32 B_P 2^128
and
32 ((B_P+1)2^128-1).
```

Of the 239131808 product-live vectors, 239131588 have upper norm bound below
the first endpoint and 220 have lower norm bound above the second. None is
unresolved. All high-side states are retained explicitly; their energy
distribution is

```text
E9=4, E11=2, E12=4, E13=14, E14=4, E15=22, E16=28,
E17=48, E18=8, E19=26, E20=28, E21=24, E23=4, E24=4.  (5)
```

A cofactor-32 collision requires `Norm(F)=32p` inside these endpoints, which
contradicts the exhaustive separation.
