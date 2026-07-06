# petal_mixed_amplification

- **status:** CONDITIONAL
- **closure:** proof from PMA stage predicates
- **refs:** `proof_sketch/s7_list_side.md#4`

## Statement

Count degree-`<= d` polynomials `W` with many zeros across the shifted-target
family

```text
W - c_i L_D on T_i.
```

Super-polynomial amplification must force quotient structure, low defect, or
another explicitly budgeted structured family.

## Ledger

CONDITIONAL (Codex fresh-base pass): `pma_aux_list_reduction` converts extras
to the auxiliary RS list, `pma_johnson_regime` covers the classical
few-petal range, and `pma_wide_residual` is the remaining many-petal primitive
residual.

AMBER STRESS 2026-07-06: `pma_correlated_target_search.py` varied the defect
locator and correlated petal scalar pattern in the `F_109, ell=3, d=5` toy
window.  It completed `10` exact profiles and `3` sampled `M=12` profiles under
the cap; exact `M=9` profiles had at most `176` threshold candidates, and no
large spread-residual alarm appeared.
