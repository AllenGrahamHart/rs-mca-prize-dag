# Claim contract

## Inputs

- an admissible challenge row `C=RS[F,L,k]`;
- the proposed first-safe integer agreement `a_safe`;
- `q=|F|` and `B*=floor(q/2^128)`;
- the exact bad-slope count convention used by `mca_grand`.

## Output

One fail-closed `Q`, `V`, or `M` payload proving strictly more than `B*`
ambient-field bad slopes at `a_safe-1` after its supplier theorem is applied.

## Load-bearing checks

1. The row is inside the actual prize family.
2. Agreement and radius use the closed-ball endpoint convention.
3. Every counted value is a distinct slope in the ambient MCA challenge field.
4. Generated-field objects cannot spend the ambient denominator without a
   wired transfer theorem.
5. `Q` proves every `qfloor_exact` hypothesis and the strict count inequality.
6. `V` proves pairwise distinctness and badness for one received pair.
7. `M` proves post-paid ownership, computes every `Delta_d(A)` exactly, and
   proves `nu(A)>B*`; `nu(A)>B*-1` is insufficient.
8. The construction radius reaches exactly `a_safe-1`, directly or by a
   printed monotonicity direction.

## Nonclaims

No numerical survival test, typical-prime density theorem, named-field E1
certificate, or uninstantiated moment formula is a row payload.
