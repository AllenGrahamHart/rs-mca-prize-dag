# F3 h=3 activation symmetry

Status: PROVED SYMMETRY LEMMA / MACHINE-VERIFIED ON BANKED ACTIVATIONS.

This packet records a bridge-side algebraic fact used by the h=3 activation
orbit deduplication and any future geometric batching theorem.

## Pre-registration

Question:

```text
Does the affine/Galois action on exponent shapes preserve the h=3 activation
predicate?
```

Success criterion:

- prove the elementary-symmetric transformation formula;
- verify the predicate over several finite-field rows;
- check that the banked activation records are stable under the canonical
  affine/Galois/side-swap orbit map.

Failure criterion:

- use the symmetry to claim a new activation bound;
- silently assume non-unit exponent maps are Galois symmetries;
- ignore the unequal `e_3` condition.

## Lemma

Let `H = mu_n(F_p)` with primitive root `omega`, and let

```text
P = {omega^a, omega^b, omega^c}
Q = {omega^d, omega^e, omega^f}.
```

The h=3 activation predicate is

```text
e_1(P)=e_1(Q),    e_2(P)=e_2(Q),    e_3(P) != e_3(Q).
```

For an affine exponent map

```text
x -> u x + s,      gcd(u,n)=1,
```

the generator must be transformed contragrediently.  Put

```text
omega' = omega^(u^{-1}),      gamma = (omega')^s.
```

Then evaluating the transformed exponents at `omega'` sends `omega^x` to
`gamma omega^x`.  Hence

```text
e_j(gamma P') = gamma^j e_j(P')
```

for `j=1,2,3`.  Multiplication by `gamma^j` is invertible, so equality of
`e_1,e_2` and inequality of `e_3` are preserved.  Side swap is also harmless
because the predicate is symmetric in `(P,Q)`.

Thus activation is constant on affine/Galois pair-orbits in the correct
existential sense over primitive-root embeddings.  It need not be invariant at
a fixed chosen generator.

## Replay

The verifier checks the transformation formula directly on random disjoint
h=3 shape pairs over:

```text
n=96, p in {97,193,577,769}.
```

It also checks the `720` banked activation records from
`f3_h3_all_core_census_summary.json`: for each activated shape it finds an
activating primitive-root embedding, applies several affine/unit/side-swap
images, and verifies activation at the transformed embedding.

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_activation_symmetry.py
```

Expected digest:

```text
H3_ACTIVATION_SYMMETRY_PASS
```
