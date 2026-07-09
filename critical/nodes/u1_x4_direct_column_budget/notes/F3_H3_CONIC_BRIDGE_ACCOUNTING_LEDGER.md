# F3 h=3 conic bridge accounting ledger

Status: PROVED BRIDGE-SIDE ACCOUNTING LEDGER, NOT `H3-BRIDGE-RANKCAP`.

This packet compiles the conic-side facts that are already proved and states
exactly what remains for the h=3 bridge.  It is meant to prevent the bridge
from paying duplicate curve images caused only by different choices of base
point inside the same same-`(e1,e2)` fiber.

## Banked Inputs

The local h=3 same-fiber conic is

```text
G(u,v)=u^2+uv+v^2+a(u+v)+b=0.
```

After excluding the repaired degenerate cells, the existing packets prove:

- one row-field point on `G=0` gives a degree-2 rational chart
  `U(t),V(t),W(t)` over the row field;
- ordered `H`-triple count and finite chart count differ by at most one
  vertical/projective point:

```text
R_z = T_z + epsilon_z,        epsilon_z in {0,1};
```

- changing the base point changes the parametrization but not the projective
  conic image or the recovered ordered `H`-triple fiber;
- each nonempty same-`(e1,e2)` fiber should therefore be charged as one conic
  image/key, not once for each ordered triple inside that fiber.

## Pair Accounting

For one conic image/key `z`, let `R_z` be the ordered pairwise-distinct
same-fiber triple count.  Since unordered triples contribute with the six
orderings,

```text
N_z = R_z/6.
```

The local activated unordered triple-pair contribution is

```text
P_z = binom(N_z,2) = R_z(R_z-6)/72.
```

Thus the h=3 bridge target can be stated without any base-point multiplier:

```text
sum_z R_z(R_z-6) <= 1152 n,
```

equivalently,

```text
P_total <= 16 n.
```

This is exactly the target consumed by the current L2/level-set bridge
compiler.  The remaining theorem is global: assign activated non-toral
shape-pairs to repaired conic images/key classes with this L2 budget and then
to the official rank-capacity table.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_bridge_accounting_ledger.py
```

Expected digest:

```text
H3_CONIC_BRIDGE_ACCOUNTING_LEDGER_PASS
```

The replay imports only lightweight local verifiers:
`F3_H3_CONIC_DEGREE2_CHART.md`,
`F3_H3_CONIC_CHART_HPOINT_COVERAGE.md`,
`F3_H3_CONIC_BASEPOINT_EQUIVALENCE.md`,
`F3_H3_PAIR_COUNT_FROM_CHARTS_COMPILER.md`, and
`F3_H3_L2_LEVELSET_BRIDGE_COMPILER.md`.
