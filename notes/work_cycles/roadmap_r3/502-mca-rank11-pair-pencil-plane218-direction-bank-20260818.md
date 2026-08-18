# Cycle 502: the 218-plane projective direction bank

## Result: PROVED near-saturated endpoint

Any affine plane attaining the cap 218 has common received-pair core
`1043551<=c<=1046532`. After reversible shortening,

```text
2044<=K'<=5025,
F_full>=28396+204K'.
```

The full coordinates are 15-point affine-line fibers. Point-line incidence
and direction-polynomial degree give 210 to 218 full lines and at least 210
distinct projective directions. Across those directions the unused root
capacity is at most 41,736, and aggregate root saturation is uniformly
greater than 0.9618.

Dualizing the 218 scalar points yields at least 210 multiplicity-15 points
among 218 lines. These consume 22,050 of the 23,653 line pairs, leaving at
most 1,603 pair intersections elsewhere.

## Burn-down

```text
starting local pin:       daa149d91
canonical prize pin:      0dd5b3244
upstream frontier pin:    PR #1173 at 2788d5ec3
DAG delta:                +1 PROVED endpoint direction-bank node, +2 edges
critical status delta:    none
closed interface:         generic affine-plane endpoint to Q/BC fiber bank
compute spend:            none
next action:              finite-characteristic arrangement transfer or quotient-periodic pricing
```

## Scope fence

The classical complex Hirzebruch inequality would contradict the dual
ledger by a gap of 925. It is not imported: the official configuration is
over a finite field, and no characteristic-transfer theorem has yet been
proved for this incidence matroid.

## Nonclaims

- the 218-plane endpoint is not excluded over the official field;
- the quotient-periodic fiber bank is not paid;
- no rank-eleven closure or MCA closure.
