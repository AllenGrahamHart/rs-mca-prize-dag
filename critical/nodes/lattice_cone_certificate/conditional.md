# lattice_cone_certificate conditional proof

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: CONDITIONAL]
- **closure:** proof from predicate nodes

## Predicate nodes

- `kernel_lattice_reframing`
- `weight_graded_mitm`
- `integer_code_distance_cert`

## Claim

Conditional on the predicate nodes, each knife-edge row has a printed lattice
certificate proving full injectivity for the relevant class cell.

## Proof

By `kernel_lattice_reframing`, equality of two `e1` values over a row with
`p = 1 mod N'` is equivalent to a ternary vector

```text
v in {-1,0,1}^{N'}
```

lying in the explicit kernel

```text
K_p = {v : sum_x v_x zeta^x = 0 mod p},
```

with support at most `2l'`, modulo the known cyclotomic relations. Thus full
injectivity is exactly the assertion that `K_p` contains no non-cyclotomic
ternary vector of support `<= 2l'`.

`weight_graded_mitm` proves the certificate semantics for direct mod-`p`
search: the meet-in-the-middle verifier is sound and complete for its printed
weight range, discards the known cyclotomic relation lattice, and emits a
checkable certificate when no survivor exists.

The remaining predicate `integer_code_distance_cert` supplies the row-specific
certificate that the explicit lattice has no non-cyclotomic ternary vector up
to the full required support bound `2l'`. Combining that certificate with the
linear equivalence above proves that no two class indicators in the cell
collide under `e1`.

Therefore the row has the required lattice/cone certificate. The BKZ/search
route remains a falsifier: finding such a sparse vector is an actual collision,
not merely a failure of this proof method.
