# F3 u1_x4 amber assembly

> **REPAIR AT IMPORT (2026-07-10, catch #71 — fresh-context amber audit of the
> worktree proposal):** the trace-zero envelope `A_3^0 <= binom(R,2)` is FALSE
> for the pair-orbit count the compiler consumes — counterexample at
> (p,n) = (7937,64): A_3^0 = 2 pair-orbits ({P,-P} class, missed by the
> binomial) vs binom(R,2) = 1 (exact enumeration; cx_amber_audit_20260710.py,
> 32 PASS incl. the counterexample). CORRECTED ENVELOPE:
> A_3^0 <= 2*binom(R,2) + R = R^2 <= I^2/36 < (4/9) n^(4/3) (the R-term
> cancels exactly). All displayed `8n^(4/3)` / `(2/9)` constants below are
> SUPERSEDED by `16n^(4/3)` / `(4/9)`; the closing identity re-lands at
> exactly n^3 (4/9 = 16/36). The 'combined 6986 < 8191, no retune' corollary
> DIES (corrected 5780 + 4096 = 9876 > 8191) — only the C36' identity route
> survives, which is the route the master assembly uses.

Status: PROVED CONDITIONAL COMPILER; DAG SURGERY PROPOSAL.

## Consumer-aligned conclusion

The proved consumer arithmetic accepts a fully stripped direct-column residue

```text
R_post<16n^3.                                   (U16)
```

The current `u1_x4_direct_column_budget` headline `R_post<=n^3` is a stronger
sufficient conjecture, not the weakest consumed floor. This surgery re-poses
the node at `(U16)` before changing it from TARGET to CONDITIONAL.

## Width partition

The ground-truth band derivation proves

```text
2<=h<=H_max(row)=min(k+t,floor(n/2)).
```

Width is intrinsic, so the stripped residue partitions disjointly as

```text
R_post=R_1+R_2+R_3+sum_(h=4)^H_max R_h.         (U-PART)
```

The four payments are:

```text
R_1=0,                                          (proved: singleton injectivity)
R_2<=T_2<n^3,                                   (proved h=2 theorem)
R_3<=T_3<n^3,                                   (conditional on H3-3TO1-C36)
sum_(h=4)^H_max R_h<=14n^3.                     (HGE4-14 premise)
```

Therefore

```text
R_post<0+n^3+n^3+14n^3=16n^3,
```

which proves `(U16)` without double spending.

## Proposed critical sub-DAG

```text
f3_h1_singleton_injectivity                 [PROVED]
f3_h2_stratum_theorem                       [PROVED]

f3_h3_three_to_one_c36                      [TARGET]
    -> f3_h3_direct_floor_conditional_close [CONDITIONAL]

f3_hge4_aggregate_budget                    [TARGET]

f3_h1_singleton_injectivity
f3_h2_stratum_theorem
f3_h3_direct_floor_conditional_close
f3_hge4_aggregate_budget
    -> u1_x4_direct_column_budget            [CONDITIONAL]
```

The proved band pin and consumer arithmetic are compiler inputs. The existing
h=3 rank/bridge route and `f3_active_core_width_cap` remain alternate/evidence
edges rather than additional required premises.

## Promotion effect

This surgery does not prove `u1_x4`. It changes one broad red into an amber
whose only open required leaves are:

```text
f3_h3_three_to_one_c36,
f3_hge4_aggregate_budget.
```

The maintainer owns the corresponding `dag.json` status, statement, and edge
edits. This worktree deliberately does not edit `dag.json`.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_u1_x4_amber_assembly.py
```

Expected digest:

```text
F3_U1_X4_AMBER_ASSEMBLY_PASS rows=29 total=16 tail=14
```

