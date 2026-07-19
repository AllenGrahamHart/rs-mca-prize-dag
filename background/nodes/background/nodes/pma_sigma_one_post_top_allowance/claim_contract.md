# Claim contract

## Inputs

- the proved source-layout router `l1_program_frontier`;
- the layout-anchored G1 floor-band atlas and exact weighted census;
- K4's complete per-chart bound `m_chi+1`;
- the finite official `sigma=1` rows.

## Output

A source-uniform disjoint partition

```text
X_prim(U)=Top(U) disjoint_union Post(U)
```

with `#Top(U)<=N_top` and an exact unborrowed Post allowance

```text
B_post = n^6-N_top                    at rate 1/2,
B_post = n^6                          at rates 1/4, 1/8, 1/16.
```

## Consumer effect

`pma_wide_residual` no longer has to invent or justify a finite common
allowance. Its finite quantitative target is exactly `#Post(U)<=B_post` after
the global owners and proved B11 source cells are first-matched and every
source-chart multiplier is restored.

## Nonclaims

No Post count, chart-composition theorem, far-from-coset incidence bound,
later-defect payment, or asymptotic-reserve theorem is supplied here.
