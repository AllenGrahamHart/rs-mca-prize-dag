# Proof

Write the positive-half integer autocorrelation as `(A_d)_(1<=d<64)` and put

```text
E=sum_d A_d^2,          L=sum_d |A_d|,
q=#{d:A_d is odd}.
```

The imported product window leaves `E=2,...,108` for `m=16`.

## Exhaustive support branch

Cofactor 16 forces exact multiplicity four at `X=1` in the six-singleton
binary support polynomial `P`. If all exponents have one parity, divide them
by two after translation. The resulting support has exact multiplicity two.
If its exponents again have one parity, divide once more. In characteristic
two,

```text
Q(X^4)=Q(X)^4,
```

so the final quotient has exact multiplicity one. Another parity division is
impossible because a polynomial in `X^2` has even multiplicity. This gives an
exhaustive primitive / once-divided / twice-divided trichotomy.

For the twice-divided branch, translation and an odd unit normalize the
quotient support in `Z/32` to contain `{0,1}`. Enumeration of all
`binom(30,4)=27405` six-term supports containing this pair finds 13755 of
exact multiplicity one. Affine canonicalization and multiplication by four
leave 903 orbits. Their odd-chord weights are

```text
q=1:8, 2:1, 3:52, 4:23, 5:101, 6:124, 7:214,
q=8:144, 9:163, 10:43, 11:28, 12:1, 13:1.          (1)
```

## Exact product chambers

The 36 raw coefficient-pair products consist of three magnitudes four,
eighteen magnitudes two, and fifteen magnitudes one. Thus their total absolute
weight and square weight are

```text
W=63,                  Q=135.
```

At one lag, let `H_d` and `Q_d` be the corresponding raw weights. For signed
summands of magnitudes in `{1,2,4}` one has

```text
4|A_d| <= A_d^2 + 4H_d-Q_d.
```

For `|A_d|>=4` this is immediate. For values one, two, or three, the required
residual is supplied respectively by an odd summand, a magnitude-two summand
or two odd summands, and an odd summand. Summing over lags gives

```text
4L <= E+4W-Q = E+117.                               (2)
```

The exact certificate enumerates every integer magnitude partition of
`E=2,...,108` with at most 36 classes, every parity weight in (1), and applies
(2). It then uses the exact fixed-mean/fixed-variance product extremum with

```text
|F(zeta^u)|^2 <= min(144,18+2L).
```

Across 295256 exact rational comparisons, 2718 of 3685 `(E,q,L)` chambers
are excluded and 967 remain. Every live chamber has `E<=89`; the parity-class
energy frontiers are

```text
q=1:73, 2:70, 3:71, 4:72, 5:73, 6:74, 7:75, 8:76,
q=9:77, 10:78, 11:79, 12:80, 13:89, 14:86, 15:87.  (3)
```

## Dual complete radius search

On a parity-even lag, an odd value of `A_d/2` costs at least four units of
energy. Thus a vector in a live chamber has syndrome radius at most
`floor((E-q)/4)`. The primary engine scans every heavy-position triple and all
32 normalized singleton-sign assignments, then replays all eight heavy-sign
choices exactly. The audit reverses both outer orders, constructs its chord
columns separately, and directly rebuilds the full nine-term autocorrelation
for every low-energy survivor.

The two engines agree on all proof-relevant totals:

```text
affine orbits:                     903
singleton sign assignments:     28896
raw heavy-position triples: 266601720
singleton-sign distance tests: 8531255040
unique radius triples:         7422374296
exact heavy-sign tests:       59378994368
low-energy vectors:             497496976
product-live vectors:           205513652.          (4)
```

## Certified norm separation

The fixed table contains all 64 odd roots and 128 positions, scaled by
`2^48`. Its independent 256-bit Arb audit proves all 16,384 real and imaginary
component errors strictly below one. Every vector has coefficient `L1` norm
12, so integer lower and upper squared-modulus bounds use component error 12
and are multiplied over all 64 roots.

The exact scaled cofactor-16 endpoints are

```text
16 B_P 2^128
and
16 ((B_P+1)2^128-1).
```

Of the 205513652 product-live vectors, 205486644 have upper norm bound below
the first endpoint and 27008 have lower norm bound above the second. None is
unresolved. The verifier independently reconstructs every retained high-side
state and its lower product interval. A cofactor-16 collision in this support
branch would require `Norm(F)=16p` inside these endpoints, contradicting the
exhaustive separation.
