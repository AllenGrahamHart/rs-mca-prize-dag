# integer_code_distance_cert

- **status:** TARGET
- **closure:** open row certificate
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

For every row that a downstream prize certificate assigns to this lattice
route, pin the prime field, quotient order and root, class cell and its exact
cardinality, support bound `2l'`, explicit integer kernel matrix, and allowed
cyclotomic-relation basis. Then bank a machine-checkable certificate that no
non-cyclotomic ternary kernel vector of weight at most `2l'` remains and check
that the certified cell cardinality is greater than the row budget `B*`.

There is no hidden finite registry of official row primes. Closure must
therefore be either uniform over every admissible row assigned to this route,
or explicitly exhibit-scoped with every downstream claim narrowed to the same
field. Exact finite search proves procedure totality but does not prove that
its verdict is collision-free. The C-4 toy anchor is a format exemplar only.

The proved `integer_code_distance_high_field_folded_box_exclusion` pays the
complete order-128 folded cube whenever the row characteristic satisfies
`p>253^32`: every ternary kernel vector is then antipodal/cyclotomic. This is
an exact branch theorem, not a promotion. Lower characteristics, other
quotient orders, the universal row assignment, and the row's value-set budget
remain open.

## Attack surface

Before computation, bind the literal row payload and prove that its class count exceeds `B*`. Apply the high-field order-128 theorem where available. On a residual pinned row use: (1) pseudo-Boolean/SAT with proof logging (VeriPB-style); (2) MITM bands as baseline; or (3) LP/Delsarte. A collision verdict is a valid route outcome but does not close this no-vector target. E24's BKZ hunt is search evidence only.

## Falsifier

a non-cyclotomic ternary kernel vector inside the declared support bound, or a declared cell whose exact cardinality is at most `B*`

## Addendum (2026-08-07, round-21 closability probe — NOT closable via the transported distance laws)

Probe verdict (notes/pilots_20260807/red_closability_probes/): the
Z-1/Z-2 transport CANNOT close this node — hypotheses H1-H3 hold
and the shift-0 scope check PASSES, but the system supplies ell = 1
odd-power condition against the ell = 65 the threshold needs, and
ell = 1 is PERMANENT: multi_multiplier_reduction (REFUTED) proves
the k-multiplier residue matrix is a rank-1 outer product for every
k. Z-2 at ell = 1 yields only "weight >= 3", attained. The PROVED
high-field branch (p > 253^32) covers 5.02% of the e = 1 prime-row
log-window; the four pinned Proth exhibits sit 84.5-88.5 bits below
it. This node remains the genuine open content of the (re-posed)
mystery-5/kernel-lattice line.
