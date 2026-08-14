# Rank-eight nine-shadow kernel capacity cut

- **status:** PROVED
- **scope:** the dominant rank-deficient lane for `10<=K'<=17608`
- **units:** normalized `(record, eleven-subset)` incidences

Combine the ambient/record individual caps with the rank-preserving
nine-shadow resource and the rank-eight-deficit resource:

```text
sum_d w_d x_d <= C(m',9),
w_d=C(d+2,2)/C(K'-d-9,2),

v_1 x_1+v_2 x_2+55 sum_(d=3)^9 x_d
  <= E_0 C(m',9),
v_1=52+3E_0/E_1,
v_2=55+6*C(67474,2)/E_2.                           (LP8)
```

Exact rational optimization proves that the capacity is below the dominant
kernel demand for every `10<=K'<=17608`. At the endpoint, demand exceeds
the floored capacity by

```text
126547040539829546354916747965612889135249249684319416999204.
```

At `K'=17609`, capacity exceeds demand by

```text
165662859003771823867021831078593815988062146919602894849014,
```

so this method stops there. At both boundary rows coranks one and three are
at their individual caps, coranks two and four are fractional, and higher
coranks vanish.

## Falsifier

An omitted dual vertex, a mismatch between the independent primal ledger
and the dual optimum, a failed closed row, or a claim beyond `K'=17608`.
