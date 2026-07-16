# Mixed-petal scope audit — universal imgfib

Status: `SCOPE DEFECT CONFIRMED / DAG REPAIRED / NO COUNTEREXAMPLE CLAIMED`.

Historical note: the 2026-07-15 r76 audit later refuted the intervening
`pma_wide_residual` exponent-six allocation and re-posed
`petal_mixed_amplification` as the direct red target. The scope finding below
remains valid; its old node-status diagram is provenance, not the live DAG.

## Question

Does the green 2026-07-13 `imgfib` chain prove its universal conclusion for
all received words, or only the full-petal contribution supplied by
`petal_growth`?

## Evidence read

1. `imgfib/statement.md` quantifies over all received words and all image-fiber
   contributors.
2. `petal_growth/proof.md` states twice that its theorem is full-petal and that
   mixed-petal contributions are separate and untouched.
3. `petal_growth/conditional.md` proves only the top-band full-petal split;
   its scope section again excludes mixed petals.
4. `petal_mixed_amplification` already exists as a conditional theorem. Its
   two proved stages reduce to an auxiliary RS list and pay the Johnson-safe
   range; `pma_wide_residual` is TARGET.
5. `payment_completeness/proof.md` proves taxonomy exhaustiveness but
   explicitly does not pay the generic quantitative count. It cannot replace
   mixed-petal amplification.
6. Przemek upstream `c35a6da3`, Theorem B11 and the Development Ledger in
   `l1_full_list_quotient_proof_program.md`, leave two residual mechanisms:
   growing-excess full petals and diffuse partial petals. Upstream PR `#757`
   independently reached the same conclusion.
7. The local independent census
   `petal_g1_layer_maps/.../cpa_checks.py` replayed `37 PASS / 0 FAIL` and
   found `43` mixed-petal floor-band contributors at `(n,k,q)=(16,8,97)`
   outside clause (P), versus `10` full-petal classes. This proves the omitted
   bucket is nonempty; it does not prove super-polynomial growth.

## Verdict

The 2026-07-13 promotion was not justified at universal scope. No proved
child is false: the defect is a missing requirement edge. In particular,
`petal_growth` remains PROVED exactly as stated.

The repaired logic is

```text
petal_growth [PROVED] ---------------------\
                                                  -> imgfib [CONDITIONAL]
pma_wide_residual [TARGET]
  -> petal_mixed_amplification [CONDITIONAL] -----/
```

The existing structural and arithmetic suppliers remain wired as the other
four `imgfib` requirements. The only new red leaf is `pma_wide_residual`.

## Propagation

`list_safe` and `m_le3_route` return from PROVED to CONDITIONAL because their
implications consume `imgfib`. Their downstream nodes were already
CONDITIONAL, so no further status changes are needed. The critical validator
must report nine unproved leaves after this repair.

## Crosswalk correction

The old upstream crosswalk's blanket official-row discharge is withdrawn.
Its clause 6 incorrectly assigned mixed petals to the full-petal off-band
argument. Its clause 4 also incorrectly said the entropy condition forces
`sigma=Omega(n)` at official rows; the correct scale is
`Theta(n/log n)`. The proved portable statement is the full-petal component,
with the blanket L1 claim held on `pma_wide_residual`.

## Nonclaims

- No counterexample to `imgfib` or to `pma_wide_residual` is claimed.
- The toy count `43` is a scope witness, not an asymptotic lower bound.
- No arbitrary-RS-list conjecture is inserted into the critical DAG.
- This repair does not weaken the full-petal, quotient, primitive, or
  fixed-excess theorems.
