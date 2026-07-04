# unsafe_at_crossing

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#4']

## Statement

For each admissible row: B_C(a_safe - 1) > B* witnessed at the ADJACENT grid point — collision-free branch: qfloor value-set family; collided branch: averaged fiber-to-slope conversion.

## Attack surface

collision-free: count the qfloor family at the crossing scale; collided: prove averaged_slope_conversion

## Falsifier

n/a (existence claim; the branch dichotomy is exhaustive)

## Ledger (migrated notes)

two exhaustive routes: collision-free => qfloor-family witnesses; collided => averaged slope conversion | PREFERRED ROUTE: qfloor witness family (collision-free branch), per E1 + the typicality model. | DEFECT FIXED (Codex packet): the two named branches wired — collision-free = qfloor_exact (PROVED), collided = averaged_slope_conversion (RIPE). Re-referee for promotion next pass.
