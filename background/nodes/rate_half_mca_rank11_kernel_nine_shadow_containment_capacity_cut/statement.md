# Kernel nine-shadow containment capacity cut

- **status:** PROVED
- **scope:** the dominant rank-deficient lane for `10<=K'<=15670`
- **units:** normalized `(record, eleven-subset)` incidences

Combine the ambient/record individual caps with the two proved nine-shadow
constraints:

```text
sum_d w_d x_d <= C(m',9),
w_d=C(d+2,2)/C(K'-d-9,2),

[52+3E_0/E_1]x_1+55 sum_(d=2)^9 x_d
  <= E_0 C(m',9),
E_0=C(m'-9,2), E_1=C(K'-10,2).                    (LP)
```

Here `x_d=I_d/R_actual`, and each individual ambient cap is evaluated at
the worst allowed record count `N_min=274980728111260126`.

Exact rational optimization of (LP) proves that its capacity is below the
dominant kernel demand for every `10<=K'<=15670`. At the endpoint the
scaled demand exceeds the integer capacity by

```text
60244744187647715538325354175068999745872308513185869854532.
```

At `K'=15671`, capacity exceeds demand by

```text
291105561463347587484268984669020036510369238771859813045635,
```

so the method stops there. At both boundary rows, only coranks 1 and 2 are
positive and both shadow inequalities bind; neither individual cap binds.

## Falsifier

An omitted LP vertex, a negative or invalid dual multiplier, failure of
either shadow equality at the boundary optimizer, a closed-row sign
failure, or a claim beyond `K'=15670`.
