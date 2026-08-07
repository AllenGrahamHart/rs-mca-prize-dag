# petal_growth

- **status:** PROVED (2026-07-13, P1 floor confirmation; see proof.md)
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s7_list_side.md#4']

## Statement

At every official row and for every received word, the layout-anchored
top-band full-petal contribution with

```text
d >= ell(M-2)
```

fits the polynomial/profile budget. Below-band full petals are not claimed;
their exact remaining FPC5 branch is
`l1_full_petal_fpc5_payment`.

## Attack surface

fixed-excess enumerations (Q2.9), growing-excess coset-chart scans, then the amplification / paid-family statement; CRT compression makes small cases finite

## Falsifier

an uncharged layout-anchored top-band family whose count cannot be bounded by
the stated polynomial/profile payment
