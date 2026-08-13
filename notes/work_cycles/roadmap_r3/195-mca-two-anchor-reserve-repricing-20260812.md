# Cycle 195: MCA two-anchor reserve repricing (2026-08-12)

Canonical `prize@c8d48cd4b` selected the cheapest route-comparison probe:
replay the active deployed MCA conditional endgame after replacing the false
one-slope near-rational payment by the proved `2w` charge.

The probe returns `SURVIVES_WITH_EXPLICIT_PRICE`.  The near-rational set
cannot be put inside the old 31-slope exception set because

```text
2w = 134944 on KoalaBear,
2w = 134896 on Mersenne-31.
```

Putting it in a separate earlier first-match owner changes the large-owner
target exactly to

```text
B_owner^(2w)(g) <= B*-(2w+31)-(n-g).
```

The exact revised endpoint table is

```text
row          target at g_min            target at g=n   floor(target/avg-ceil)
KoalaBear    274980728110346481          274980728111260112      4807520
Mersenne-31          15728609                   16642288                9
```

Every affine and smaller-owner branch retains a positive exact margin.  In
the large-owner branch the four charges sum identically to `B*` for every
integer owner size.  The direct S/A/E route is therefore not killed by
arithmetic, but the price is real: its `(A)` input and source interface must
be reissued at a target smaller by exactly `2w`.  No revised large-owner
maximum-fiber theorem is proved.

```text
start:                   046505a55
result:                  PROVED repricing; probe survives with explicit price
DAG delta:               +1 PROVED background node, +2 req edges
critical status delta:   none
upstream terminal delta: candidate threshold note for #1160/#1163 lineage
delta-star movement:     none
compute:                 exact integer replay only; no Modal spend
next route action:       run the shared d1=67473 K-adapter adjudication,
                         then the #1160-line P_BC rejection regression
```
