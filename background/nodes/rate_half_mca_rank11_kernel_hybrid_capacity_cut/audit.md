# Audit

1. `R_actual` is not replaced by `N_min`; only the nonincreasing normalized
   bound is evaluated at `N_min`.
2. Both component capacities are in the same `(record,T)` unit.
3. Integer floors are applied before the per-corank minimum.
4. The demand uses an integer ceiling.
5. Every row through `11772` is replayed.
6. The reversal at `11773` is an explicit nonclaim boundary.
