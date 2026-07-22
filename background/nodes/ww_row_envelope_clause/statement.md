# Direct worst-word challenger envelope

- **status:** TARGET (RETIRED FROM THE PRIZE REQUIREMENT PATH)
- **former consumer:** `worst_word_challenger_pricing`
- **scope counterexample:** `ww_spending_cell_fiber_layout_counterexample`

The binding W3 claim asserts, for every **safe-side** in-scope
planted-sunflower receiver `U`, that

```text
|List(U)| = p(U) + N_nonplant(U) <= B*,
B*=floor(q/2^128).
```

The exact two-class identity remains proved. The replayable rate-`1/4` row

```text
q=1705*2^120+1,       n=8192,       k=2048,       B*=6
```

has an **unsafe** spending cell with six distinct planted polynomials and the
additional non-planted codeword

```text
g(X)=L_(C\D)(X)(X^256-z_0).
```

It has at least `3328` agreements, above the threshold `3071`, so

```text
p(U)+N_nonplant(U) >= 7 > 6=B*.
```

The construction aligns allowed petals with distinct fibers of the rational
pencil `(X^256-z_0)/(X^256-z_c)`.  It uses a prime field, a 2-power
multiplicative evaluation subgroup, distinct nonzero labels, and background
size one. It is inside the row/layout/scalar quantifiers but outside W3's
literal safe-side quantifier.

Thus the construction does not refute W3 as written. It refutes the stronger
all-cell interpretation implicitly used by the old consumer. The repaired
prize route uses the proved unsafe witness and the independent safe corridor
directly, so the still-open safe-side W3 bound is no longer a requirement.

## Historical interface record

The proved identity `List=Plant disjoint_union NonPlant`, the parametric row
descriptor, and the QA.22/W3 currency separation remain valid support
results. They explain the scope mismatch and prevent reusing the MCA `16n^3`
reserve as a list-codeword upper bound. The retired `K_cell` and multi-column
formulations are preserved in the node history. No claim is made that the
remaining safe-side envelope is true.
