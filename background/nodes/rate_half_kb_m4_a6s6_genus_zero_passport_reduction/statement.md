# KoalaBear m4 A6/S6 genus-zero passport reduction

- **status:** PROVED
- **scope:** sole surviving inner-degree-four transverse type
- **dependency:** `rate_half_kb_m4_outer_a6s6_route_cut`
- **consumer:** `rate_half_band_closure`

Let `F:P^1->P^1` be the surviving degree-15 outer map, whose geometric
monodromy is `A6` or `S6` in the action on two-subsets of six letters. Assume
the imported source divisor forces a pole branch cycle of pair-cycle type
`5^3`, corresponding to letter-cycle type `5.1`.

Then the complete geometric genus-zero passport frontier consists of exactly
four letter-cycle class multisets:

```text
A6:  5.1, 2.2.1.1, 4.2
S6:  5.1, 2.1.1.1.1, 2.2.1.1, 2.2.2
S6:  5.1, 2.1.1.1.1, 6
S6:  5.1, 2.2.2, 3.2.1
```

The three rows with two residual classes are three-point covers. The other
row is a four-point cover. Both split `A6` classes of 5-cycles give the same
classification.

## Falsifier

A missing `S6` conjugacy class or induced pair-cycle type; another
parity-compatible partition of the residual ramification index 16; a
product-one generating tuple for one of the five deleted passports; or
failure of a printed retained tuple to generate order 360 or 720.
