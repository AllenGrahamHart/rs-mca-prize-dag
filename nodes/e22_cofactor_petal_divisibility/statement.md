# e22_cofactor_petal_divisibility

- **status:** PROVED
- **closure:** proof

## Statement

For each touched petal in an E22 mixed/full-petal challenger, the cofactor
equation

```text
U(x) L_{Z\C}(x) = a_i L_{C\Z}(x)
```

on the agreement subset `T_i` is equivalent to divisibility of

```text
H_i(X) = U(X)L_{Z\C}(X) - a_i L_{C\Z}(X)
```

by the locator `L_{T_i}(X)`. In particular, a full touched petal contributes
the full petal locator as a divisor of `H_i`.

## Falsifier

A touched-petal agreement set where `H_i` vanishes on every agreement point
but is not divisible by the agreement-set locator.
