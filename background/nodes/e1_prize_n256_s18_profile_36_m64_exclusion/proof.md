# Proof

Write the positive-half integer autocorrelation as `(A_d)_(1<=d<64)` and put

```text
E=sum_d A_d^2,          L=sum_d |A_d|,
q=#{d:A_d is odd}.
```

The energy-adaptive parent leaves `E=2,...,65` for `m=64`.

## Complete support split

If the six singleton exponents contain an odd-separated pair, translation and
an odd unit normalize such a pair to `{0,1}` in `Z/128`. This is the primitive
branch.

The remaining branch has all six singleton exponents of one parity. Translate
one exponent to zero and divide every difference by two. The binary singleton
polynomial becomes a six-term polynomial on `Z/64`, and multiplicity six at
one before division is exactly multiplicity three afterward. Multiplicity
three is odd, so the divided support contains an odd-separated pair and may be
normalized to `{0,1}` in `Z/64`. Lifting by multiplication by two recovers a
complete set of all-one-parity representatives in `Z/128`.

These branches are disjoint and exhaustive. Global sign normalizes the
coefficient at zero to `+1` in both.

## Exact product chambers

Nine nonzero coefficients create at most `binom(9,2)=36` nonzero positive-half
autocorrelation classes. The certificate enumerates every integer magnitude
partition of `E=2,...,65` with at most 36 classes and every parity weight
present in the multiplicity-six atlas. It applies the exact product extremum
with

```text
y_u=|F(zeta^u)|^2 <= min(144,18+2L).
```

Square roots are enclosed between consecutive rationals of denominator
`2^192`. Across 128228 exact rational comparisons, 837 of the 1092
`(E,q,L)` chambers are excluded and 255 remain. Every live chamber has
`E<=46`. The q-specific energy frontiers are

```text
q=2:34, 3:35, 4:36, 5:37, 6:38, 7:39, 8:44,
q=9:45, 10:42, 11:43, 12:44, 13:45, 14:46, 15:43.       (1)
```

## Complete multiplicity-six atlases

On the primitive branch, enumeration of all `binom(126,4)=10009125` supports
containing `{0,1}` finds 122880 of multiplicity six. Affine canonicalization
leaves 8256 orbits, split by odd-chord weight as

```text
q=2:16, 3:56, 4:2, 5:8, 6:22, 7:130, 8:52,
q=9:366, 10:260, 11:1570, 12:170, 13:2034,
q=14:510, 15:3060.                                      (2)
```

On the all-one-parity branch, enumeration of all `binom(62,4)=557845` divided
supports containing `{0,1}` finds 71680 of multiplicity three.
Affine canonicalization in `Z/64` leaves 4480 orbits. After lifting, their
odd-chord weights are

```text
q=3:3, 4:8, 5:51, 6:58, 7:296, 8:178, 9:756,
q=10:306, 11:1181, 12:210, 13:881, 14:136, 15:416.      (3)
```

No free action is assumed: both certificates canonicalize and deduplicate.

## Dual complete radius search

On a parity-even lag, an odd value of `A_d/2` costs at least four units of
energy. Thus any vector in a live chamber has syndrome radius at most

```text
r=floor((E-q)/4).                                       (4)
```

The primary engine scans every heavy-position triple and all 32 normalized
singleton-sign assignments, applies (4), and replays all eight heavy-sign
choices exactly. The audit engine instead stores heavy-position pairs in
`r+1` disjoint lag blocks. A syndrome at distance at most `r` agrees on one
whole block, so the reverse hash-block search is exhaustive. It reverses the
position and sign orders and deduplicates triples before exact replay.

The engines agree on all proof-relevant totals:

```text
affine orbits:                12736
singleton sign assignments: 407552
unique radius triples:  10179448632
exact heavy-sign tests: 81435589056
low-energy vectors:       12140240
product-live vectors:      7191566.                    (5)
```

The primary additionally performs 3760176640 raw triple-syndrome and
120325652480 distance tests. The independent block engine records
659184718600 bucket hits before exact radius and deduplication.

## Certified norm separation

For all 64 odd roots and 128 positions, a 100-decimal generator rounds real
and imaginary components after scaling by `2^48`. A separate 256-bit
python-flint/Arb audit proves, in 16384 component checks, that every scaled
rounding error is strictly less than one.

Each vector has coefficient `L1` norm 12. Therefore summing the fixed root
table gives real and imaginary errors strictly below 12. Integer lower and
upper bounds for each squared modulus are multiplied over all 64 roots with
arbitrary-precision integers. They are compared with the exact scaled bounds

```text
64 B_P 2^128
and
64 ((B_P+1)2^128-1).
```

Of the 7191566 product-live vectors, 7191424 have upper norm bound below the
first endpoint and 142 have lower norm bound above the second. None is
unresolved. All high-side states are retained explicitly; their combined
energy distribution is

```text
E7=4, E8=8, E10=12, E11=10, E12=20, E13=12,
E14=24, E15=18, E16=20, E17=6, E18=4, E19=4.          (6)
```

A cofactor-64 collision requires `Norm(F)=64p` inside these endpoints, which
contradicts the exhaustive separation.
