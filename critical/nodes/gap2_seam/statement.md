# gap2_seam

- **status:** see dag.json (single source of truth; dag status PROVED)
- **statement provenance:** written 2026-07-27 (empty-statement remediation / sketch-tagged re-grade);
  see notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md and SKETCH_TAGGED_REGRADE.md

## Statement

[lifted verbatim 2026-07-27 from this node's own proof.md Statement section] GAP-2 seam. In the normal-form / residue framework (`thm:normalform`,
`def:residue`, banked), a bad-slope datum on a residue line carries a
**denominator polynomial** `E in F[X]` of degree `t_denom` with
`1 <= t_denom <= r`, where `r = n - k`. Say the datum is a **pullback** if
`E = g(X^M)` for some `g in F[X]` and integer `M >= 2`. Claim:

1. **(Divisibility.)** A pullback denominator forces `M | t_denom`.
2. **(Strip coincidence.)** If moreover `M | gcd(n,k)`, then the line-side
   aperiodic strip (`rem:aper`: remove pullback denominators) coincides with
   the support-side **rate-preserving** quotient strip (the `Q_M = Q_1(H_{n/M})`
   recursion, banked): on every exact-agreement bucket `A`,
   `M | j  <=>  M | t_win`, where `j = n - A`, `t_win = A - k`.
3. **(Residual seam classified.)** The only strata that are periodic on the
   support side but *not* pulled back rate-preservingly are those with
   `M | gcd(n,j)` but `M !| k`: these are **non-rate-preserving folds** — the
   quotient row `(n/M, k/M)` is not integral, the syndrome conditions do not
   descend to a valid RS row, so they stay on the aperiodic side and carry no
   alignment boost (checker convention `rem:aper`).

Parts 1–2 are the load-bearing divisibility content and are proved here in full.
Part 3's classification is proved; its "no boost" clause is the banked
`rem:aper` convention, cited (not re-derived), and flagged as such.
