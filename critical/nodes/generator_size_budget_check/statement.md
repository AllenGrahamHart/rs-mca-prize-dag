# generator_size_budget_check
- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: TARGET]
## Statement
Numeric check: the Brief-F family size |F| = N' * C(N'/2-2, N'/4-1) is
>= B*/2^33 at the prize quotient rows (N' in {128,256}), so the verified
O(N')-base construction covers the required cluster-center budget. |F| =
2^65.69 (N'=128), 2^130.18 (N'=256); confirm against B*/2^33 per row.
