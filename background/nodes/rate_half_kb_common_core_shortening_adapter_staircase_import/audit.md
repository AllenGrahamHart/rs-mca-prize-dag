# Audit

Coordinator line audit + independent replay, 2026-08-12 PR-sweep session.

1. **Divisibility and transport** were re-derived by hand; the
   `G_C | (p_j - a_j)` direction is what makes the containment
   transport a bijection — the upstream prose states it for
   certificates, and the same two-slope evaluation argument gives it
   for explainers (checked mechanically in `verify_audit.py` (c)/(e)).
2. **Exchange-graph clause**: the connectivity and the `m-1 >= k`
   overlap are the load-bearing facts; both hold at the official row
   (`m-1 = 1116047 >= k`) and in every replay row here.
3. **Independence of the replay**: `verify_audit.py` does not reuse the
   upstream GF(17) atom. It builds a different record (quadratic
   shortened receive words, disjoint engineered maximal supports
   `{4,5,6,7,13}` / `{8,9,10,11,12}`, core `{1,2}`) via the converse
   embedding and then checks all operative clauses on the ORIGINAL row
   by brute force, including noncontainment of EVERY size-4 witness
   subset in BOTH rows (10 subsets).
4. **Walls**: every constant recomputed twice — `verify.py` by
   ceiling-division / `math.comb` / `Fraction`, `verify_audit.py` by a
   windowed scan and pure-integer cross-multiplication. The upstream
   figures `3765` bits and `1134` digits are exact, not estimates
   (a rough `4131*log2(n/m) ~ 3759` underestimates because the ratio
   `(n-i)/(m-i)` grows with `i`).
5. **Telescoping** is an exact binomial identity, verified at three
   stage splits; the "staged shortening does not help" claim is
   arithmetic, not heuristic.
6. **Status split**: only the adapter theorem and the walls are banked
   PROVED. The missing-selector framing (section 5 upstream) is a
   route-cut RECORD; the `c < k` non-affine clause is a cited source
   theorem, flagged in Scope.
7. **Consistency with the `#1160` import**: the 67,472-slope
   construction is globally affine, so it is a control for this
   adapter, and `d = m-k = 67472` here matches `w` there; `t = n-m =
   981104` equals the tangent atom `U_paid`, as upstream records.
8. **2026-08-13 correction:** PR #1165 refuted the final transversality
   factor behind the direction-separated `J_s` payment. PR #1166 replaces
   it by the actual-support margin `theta`. The adapter, interface wall,
   fixed-core `B_cell` wall, and Jo-transfer obstruction are unaffected.
