# petal_growth

- **status:** PROVED (2026-07-13, P1 floor confirmation; see proof.md)
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s7_list_side.md#4']

## Statement

Full-petal extras at cofactor excess d-ell = c are poly(n) uniformly in c (equivalently: the amplification bound closes the Thm 21/B11 escape route).

## Attack surface

fixed-excess enumerations (Q2.9), growing-excess coset-chart scans, then the amplification / paid-family statement; CRT compression makes small cases finite

## Falsifier

below-top Lemma-13 failures, exact realizable full-petal counts growing outside paid/top-band families, or an uncharged top-band family whose count cannot be bounded by a polynomial with exponent independent of c
