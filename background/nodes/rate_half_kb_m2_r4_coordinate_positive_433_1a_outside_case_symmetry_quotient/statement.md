# KoalaBear m2 r4 positive 433-1a outside-case symmetry quotient

- **status:** PROVED
- **scope:** the formal `eta/xi/perfect-matching` ledger for each fixed
  common row and cycle sign of the positive route `433-1a -> O0b`
- **dependency:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_quadratic_paired_product_resultant_interface`
- **consumer:** `rate_half_band_closure`

Label the seven outside records

```text
DE+,DE-,DF+,DF-,EF,BE,CF
=de,-de,df,-df,sigma ef,be,cf.                    (KBOSQ-1)
```

The first five are the possible internal `eta` records.  After the target
sign gauge of the signed-edge atlas, the stabilizer of all common, colored,
and outside record multiplicities has order four in vertex signs.  Its
global-sign kernel has order two, so its faithful action on `(KBOSQ-1)` is
the order-two action

```text
tau: DE+ <-> DE-,  DF+ <-> DF-,
     EF,BE,CF fixed.                               (KBOSQ-2)
```

It is induced by changing the sign of `d` relative to the other target
representatives.  There is no further target-sign quotient preserving the
fixed route data.

The formal `525` cases split exactly as follows.

1. In the aligned branch `xi=eta`, choose one of five internal records at
   that source label and one of fifteen perfect matchings of the other six:
   `5*15=75` labeled cases.
2. In the near-aligned branch `xi!=eta`, choose one of five internal `eta`
   records, one of the other six records at `xi`, and one of fifteen
   perfect matchings of the residual six: `5*6*15=450` labeled cases.

Under `tau`, the aligned ledger has three fixed cases and hence

```text
(75+3)/2=39                                         (KBOSQ-3)
```

orbits.  The near-aligned ledger has six fixed cases and hence

```text
(450+6)/2=228.                                      (KBOSQ-4)
```

Thus the exact residual target-gauge quotient contains

```text
39+228=267                                          (KBOSQ-5)
```

formal cases per common row and cycle sign.

For missing-mate record `EF`, there are fifteen aligned labeled cases and
sixty near-aligned labeled cases.  They form respectively nine and thirty
orbits, so the exact `EF` subledger has 39 orbits.  The two currently
compiled target-free templates A and B are exchanged by `tau` after
permuting the three residual deck pairs.  Including every allowed `eta`
location, they cover one aligned and four near-aligned orbits, hence five
of the 39 formal `EF` orbits.  The remaining 34 `EF` orbits have not yet
received target-free sum compilers.

The generated certificate lists canonical representatives and orbit sizes
for all 267 orbits.  These are formal necessary cases, not algebraic
survivors.  This theorem does not compose the duplicate-common-role or
common-root-sign quotients, prove a representative realizable or empty,
delete either alignment branch or `433-1a -> O0b`, close positive
coordinate parity, K3, a Prize row, or either Prize result.

## Falsifier

A target-sign stabilizer inducing a record permutation outside
`{1,tau}`, a formal case absent from the 267 listed orbits, a duplicate
orbit in the certificate, a fixed-case count other than `3,6`, or failure
of the asserted gauge equivalence between templates A and B.
