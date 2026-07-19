# proof: petal_squarefree_classification_counting_soundness

Let the uncharged classes in one corridor cell be indexed by

```text
i = 1, ..., r,
```

with `r` bounded independently of the excess `c`. By hypothesis, class `i`
has size at most

```text
C_i n^{A_i},
```

where `A_i` is independent of `c`.

Let

```text
A = max_i A_i,
C = sum_i C_i.
```

Since `r` and the exponents are independent of `c`, so are `A` and the finite
form of the constant `C` allowed by the corridor ledger. The total uncharged
squarefree count is bounded by

```text
sum_i C_i n^{A_i} <= (sum_i C_i) n^A = C n^A.
```

Charged classes are not part of the uncharged realizable-extra budget; they
are paid by their respective ledgers. Therefore a classification with these
properties implies the desired uniformly polynomial sparsity bound for
squarefree realizable locator points in the residue-line kernel.
