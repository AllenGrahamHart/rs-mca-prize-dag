# active_core_count_bound

- **status:** CONDITIONAL
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/pa_active_core_probe.md']

## Statement

The fully stripped active-core count satisfies the compiler-sufficient bound
`R_PTE(row) <= n^3` at the official rows. Equivalently, after the full strip,
the uncharged active-core residue contributes no more than the direct compiler
column permitted by W4.

## Attack surface

The only live branch is the p-specific norm-gate event from the uniform x83
obstruction gate. A falsifier is an official row prime dividing one of the
cleared obstruction norms outside the paid full-fiber branch.

## Ledger

The h=3 cubic cap and W4 rewiring are proved. The complete x83 dichotomy says
every live minimal h-trade is paid full-fiber or a p-specific norm-gate event.
Thus the remaining condition is exactly the generalized `h4_sparse_norm_gate`
certifier.
