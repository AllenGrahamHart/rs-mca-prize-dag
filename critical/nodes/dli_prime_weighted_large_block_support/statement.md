# dli_prime_weighted_large_block_support

- **status:** TARGET (the dli frontier; single arc into x4_exactlist_staircase_split)

## Statement

The pointwise/sup DLI-flatness formulation is refuted.  The live obligation is
the U-weighted primitive-core count consumed by `x4_exactlist_staircase_split`:
after summing central profiles with their actual profile multiplicity weights,
the product of level factors satisfies the required `q^{o(t)}` loss.  Equivalently,
the RES/resultant-survivor count must be controlled in weighted aggregate, not
uniformly profile by profile.

Exact reduction (PROVED, Lemma 1):

```text
rho_j(M) = q^{L_j} |Z_j(M)| / U_j(M),
```

where `Z_j(M)` is the set of bounded-coefficient kernel skews for the odd
evaluation matrix.  Any proof of this node must therefore control the
`U_j(M)`-weighted distribution of these kernel fibers/resultant survivors.

## Stress Evidence 2026-07-06

`experiments/amber_stress/dli_weighted_res_probe.py` is an exact small-scale
falsification probe for this reduction.  It reproduces the known low-mass
full-rank ternary refutation of the old sup premise:

- `n=16,L=4`, eight ternary active coordinates: `eta = 2.3299609146907123`.
- `n=32,L=4`, twelve ternary active coordinates: `eta = 1.4949413720360685`.

The same probe then checks larger active ternary cells by exact meet-in-the-middle
zero-fiber counts:

- `n=32,L=4`, sixteen ternary active coordinates: `eta = 0.6599218293814246`.
- `n=64,L=4`, twenty ternary active coordinates: `eta = -0.1750977132732192`.
- `n=64,L=4`, twenty-four ternary active coordinates: `rho = 1.0365770232770783`,
  `eta = 0.006826159202134505`, zero-fiber count `211`.

Thus the strengthened pointwise premise is false, while the weighted/large-active
obligation survived this bounded probe.  This remains evidence only; the node is
still `TARGET`.
