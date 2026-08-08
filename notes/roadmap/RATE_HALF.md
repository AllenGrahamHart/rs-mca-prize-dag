# Rate-Half Finite Lane

This lane attacks the deployed KoalaBear rate-half band required by
`rate_half_band_closure`.

## Current decomposition

The positive `433-1b -> O0a` role-cell ledger has closed:

```text
[0], [1,2], [3,6], [14]
```

and retains:

```text
[4,7], [5,8], [9,10], [11], [12,13].
```

For representative cell 4, the common locus is an exact genus-two base with
a four-element localized tower and a global coefficient kernel.  The
`xi=0,pairing=0` slice is proved empty, exact parallel-copy transport pays
`xi=1,pairing=0`, and a separate equal-`DE` norm/lift theorem pays
`xi=2,pairing=0`. Thus all three parallel-`DE` omissions are closed at
matching `0`. Canonical matchings `1` and `2` share the same first pair, so
the three exclusions extend to the complete first-pair block. Exact direct
and quotient closures have since completed matching blocks `3/6`, `4/9`,
`5/12`, `7/10`, `8/13`, and `11/14`. In total all `3*15=45` parallel-`DE`
slices are paid. A source-only endpoint theorem then pays every missing
`bf` and missing `sigma_c cf` slice before matching specialization. Cell 4
is therefore 75/105 paid; 30 labels in 18 of the 60 quotient orbits remain.
These are exactly missing `df` and missing `sigma_o ef`, `xi in {3,4}`,
across all 15 matchings.

## Node hierarchy

```text
cell-4 four-basis tower
        |
        +-- xi0/pairing0 exclusion
        +-- xi1/pairing0 transport
        +-- xi2/pairing0 exclusion
                     |
                     v
       parallel-DE pairing0 closure      [PROVED]
                     |
            DE first-pair block           [PROVED]
                     |
            matching-orbit quotient       [PROVED]
                     |
            pairing-3 through 13 blocks   [PROVED as scoped]
                     |
          all parallel-DE matchings       [PROVED]
                     |
          xi5/xi6 endpoint roles          [PROVED]
                     |
           xi3/xi4 variable roles         [next exact decision]
                     |
             complete cell 4
                     |
             role orbit [4,7]
```

This hierarchy is intentional: each child has a reusable exact statement,
while source-sign rows and norm roots remain certificate records.

## Compute posture

Use symmetry and source-only cuts before launching a census.  Modal jobs must
be route-deciding and remain within the active protocol budget.  Larger
campaigns go to the deferred compute ledger.
