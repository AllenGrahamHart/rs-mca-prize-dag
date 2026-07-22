# Signed-core size-budget check

- **status:** REFUTED
- **closure:** explicit collision obstruction
- **consumer:** `generator_economy`

The proposed `N'=128` signed-8-core family has raw subset count

```text
19 binom(64,8) binom(56,28)=2^89.05547...>2^89.     (GSB1)
```

It does not meet the required cluster-center or value-set budget. For a
fixed signed core, every one of the `binom(56,28)` antipodal paddings has
zero sum and therefore gives exactly the same `e_1` value. Deduplication
leaves at most

```text
19 binom(64,8)=2^36.29133...<2^89.                  (GSB2)
```

distinct centers. Even allowing all `2^8` sign patterns on every 8-pair
support gives at most

```text
2^8 binom(64,8)=2^40.04341...<2^89.                 (GSB3)
```

Thus the padding factor in `(GSB1)` is exact collision multiplicity, not
certified value-set mass. The arithmetic raw count remains correct, but the
claimed implication to `generator_economy` is false.
