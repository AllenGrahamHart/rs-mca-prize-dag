# Proof

Suppose `(PO1)` holds. Since `union F_j` has at most `N` coordinates,

```text
h|F_j|>=2N-2a>=2|union F_j|-2a.
```

Hence at least one nonempty subfamily satisfies `(PO2)`. Finiteness and the
fixed order give a first inclusion-minimal one. Every residual `F_j` inherits
from `F_0` the one-per-slope condition, uniform block size, pairwise cap, and
extension-direction nondegeneracy. The uniform split-pencil reduction
therefore applies to that core and supplies a nonzero left relation and hence
a nonzero trade. Its rank is at least two.

If the rank is two, its Segre coefficient columns are dependent, so the
canonical basis has at least one active non-anchor. The fundamental-circuit
owner gives that block one unique four/five-block circuit. If the rank is at
least three, the relation has an active block by nonzeroness. Thus `p_j`
exists in either branch, and `(PO3)` removes exactly one block.

The family is finite, so repeated removal terminates. All choices are made by
fixed first-match rules, proving determinism. Every pivot belongs to its
recorded relation and core. Once removed, it is absent from every later
residual; in particular the same pointed certificate cannot recur. Pivots are
also pairwise distinct, so `(PO4)` gives an injection from removed blocks to
the produced records.

At termination `(PO1)` fails. Since both sides are integers,

```text
h|F_terminal|<=2N-2a-1,
```

which is exactly `(PO5)`. The punctured length is `N=n-k+a<=n`, and `h>=1`.
Therefore `B_0<2N/h<=2n`; the final inequality in `(PO6)` is immediate for
`n>=1`. Finally, `F_0` is the disjoint union of its pivots and terminal
residual, proving `(PO7)`. QED.
