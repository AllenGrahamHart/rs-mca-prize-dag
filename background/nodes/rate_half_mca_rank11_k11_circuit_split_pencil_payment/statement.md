# Circuit shadows and split-pencil capacity pay K'=11

- **status:** PROVED
- **closed residual row:** `K'=11`
- **units:** `(record, eleven-subset)` component incidences

At `K'=11`, the ten-dimensional correction space is a hyperplane in
`RS_{<11}`.  Every eleven-set has evaluation rank ten, so every
positive-dimensional incidence is affine-owner.  Rank-nine shadow charts
have uniform selected-support capacity

```text
C_*=9275866238180030.
```

Split component incidences by the support size `c_T` of their unique
evaluation circuit.  Incidences with `c_T>=6` create at least `45` rank-nine
shadows.  Incidences with `c_T<=5` all use one fixed circuit support, because
two sparse representations of the same hyperplane functional have union
size at most ten and Vandermonde evaluation functionals are independent.
Consequently

```text
I_component
 <=floor(C(n',9)C_*/45)+R_actual*C(m'-1,10).
```

At `R_actual=N_min=274980728111260126`, this capacity is

```text
870719390190680409022824387604193486699840723094988553120053384,
```

while dense-locator incidence requires

```text
901408286315387898338134887980054663001598216883356906995509296.
```

The gap is

```text
30688896124707489315310500375861176301757493788368353875455912.
```

The gap increases with `R_actual`, so the `K'=11` component target is empty.

## Falsifier

A `K'=11` eleven-set of evaluation rank below ten; a circuit of size at
least six with fewer than 45 rank-nine shadows; two nonidentical circuit
representations of size at most five; a rank-nine chart above `C_*`; more
than `C(m'-c,11-c)` low-circuit subsets in one support; or failure of the
exact final comparison.
