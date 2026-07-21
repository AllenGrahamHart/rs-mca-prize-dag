# Audit

## Forward audit

1. Primitivity is used exactly to keep the first cyclotomic lift nonzero.
2. Strict `p>m^2` and odd-frequency Parseval give the stated strict defect
   ceiling; the positive fourth-order Taylor remainder makes the cubic
   truncation a lower bound for `exp(-x)`.
3. The even moments include `j=0` because both supports have size `h`.
4. The points `eta^t` are distinct because `eta` has exact order `m/2`.
5. The Vandermonde matrix uses only rows already present in the prefix, and
   `p` is odd so the integer coefficients `+-1,+-2` remain nonzero.
6. Zero defect is exactly the antipodal-swap class, not an emptiness claim by
   itself.
7. The guard `x<=1` implies the proved swap-norm inequality before that
   dependency is used to conclude full emptiness.
8. On the guarded interval the cubic ceiling increases with `d`, so adjacent
   exact endpoint checks certify the whole initial interval.

## Consumer-backward audit

The complete Vandermonde band contributes zero to the exact-level ledger.
Below its cutoff, the swap-norm band remains free-only. Below the swap cutoff,
both free and swap classes remain open. No count is claimed in either region.

## Scope checks

- The proof applies at exact dyadic ratio level and does not confuse ambient
  order `n` with exact level `m`.
- Natural logarithms are used throughout.
- The numerical ranges are consequences of exact rational interval checks,
  not floating-point theorem premises.
- The result is uniform in every compatible prime and is not a finite-census
  promotion.

## Independent replay

The main verifier checks the endpoint table, monotonicity, swap-band
inclusion, moment identities, and DAG wiring. The audit verifier certifies
every adjacent endpoint with rational bounds for `log 2`, exhausts small
Vandermonde determinants, and checks the integer defect-energy parity floor.
