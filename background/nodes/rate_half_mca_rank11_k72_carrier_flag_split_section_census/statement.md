# K'=72 carrier-flag split-section census

- **status:** TARGET
- **row:** `K'=72`
- **consumer:** the next rank-nine component payment beyond the closed prefix
  `10..71`

In the nonnested one-residual-overlap branch of
`rate_half_mca_sparse_circuit_k72_nested_carrier_flag_router`, fix

```text
D_3 subset D_45,
|D_3|=33,       dim H_3=8,
|D_45|=36,      dim W=5,       W<=H_3,
M_4=M_5=31.
```

Let `I_4` and `I_5` be the selected eleven-set incidences of minimal
support-four and support-five evaluation circuits after all exact
inside/outside strata, carrier multiplicities, and first-match ownership are
deduplicated. Prove the weighted bound

```text
21 I_4 + 15 I_5
 <= 20552964203529559475043545396584734873674935990.   (K72-SC)
```

The current independent fixed-union caps give instead

```text
21 I_4 + 15 I_5
 <= 21195887396614969832992972237166204779857211620,
```

so the required reduction is exactly

```text
642923193085410357949426840581469906182275630.
```

After dividing the 36-point common locator, the hard equality strata are:

- two-dimensional residual pencils with a common split degree-34 core
  (support four); and
- completely split degree-35 projective sections of a five-dimensional
  residual polynomial space (support five).

Thus `(K72-SC)` is a finite weighted split-section census, not an assertion
that every completion maximum drops uniformly.

## Falsifier

An admissible five-dimensional residual polynomial space and exact carrier
flag whose deduplicated weighted incidence exceeds `(K72-SC)`. A raw count of
deletions, a list of split polynomials without circuit minimality, or a count
that reuses one circuit through several owners does not test the statement.
