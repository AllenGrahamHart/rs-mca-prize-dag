# qme_findings — qa22_m_le_t_extension proof worker (2026-07-13)
# Catch ledger continues from #154. Repo READ-ONLY; packet lives in scratchpad qme_*.

## Task decomposition (from bsra_findings "What the extension must state" + bsr_consistency D3
## + bsr_gate_repromotion "single owed consumer item" + falsifier F(G)-3)

The extension = five clauses over the official grid (s = 13..44, four rates
rho in {1/2,1/4,1/8,1/16}, k = rho*n, t = (n-k)/2, sigma = 1):

- (i)  nondegeneracy: every own cell (M, A_own(M)), dyadic 2 <= M <= t, has
       Q_M(A_own) >= 1 (h_M <= n/M - 1); algebra A_own <= k+M <= n-M.
- (ii) COL landing fits the 719 line: n/(n - A_own) <= 4 <= 719 per cell
       (headroom 179.75x); csp cell (2, k+4) ratio n/(n-k-4) <= 4 in scope.
- (iii) dedup unchanged: extension cells disjoint from BOTH the 7-lemma
       composite's cells (scale ranges [2,t] vs (t,..] partition) AND the
       banked QA.22 M > t_res rows (parity: A_own even, banked A odd).
- (iv) first-scale dominance: sum_{dyadic 2<=M<=t} Q_M(A_own) <=
       (1 + 2^-690) * Q_2(k+2)  [constant CORRECTED, see catch #155].
- (v)  absorption scale: Q_2(k+2) = Q_2^planted(k) * (n/2-1-k/2)/(k/2+1),
       exact rational per row (bounded by ~15.6 grid-wide) — the extended
       top line is within a fixed constant of the PROVED v13 planted lower
       count; old M > t_res rows unchanged (replay old verify.py).

Verification split: Regime A exact bigint s = 13..20 (bsr_check-scale, tiny-
safe); Regime B certified integer-arithmetic entropy bounds s = 21..44
(C(a,b) <= 2^{aH(b/a)}, C(a,b) >= 2^{aH(b/a)}/(a+1), dyadic-rational log2
bounds via exact integer power comparisons, precision 1/128); overlap
s = 15..20 cross-checks certificates against exact values.

## CATCH #155 — the 2^-691 dominance figure is WRONG (bit-length rounding;
## the claimed inequality is FALSE at the worst cell)

Exact computation (qme_probe1.py, ramguard tiny, exact Fraction):

- worst cell over s = 13..20 x 4 rates: (s, rho) = (13, 1/16) — LOCATION
  CONFIRMED, and the excess is carried by the M = 4 term (term/tail =
  1.000000 to 6 dp) — MECHANISM CONFIRMED.
- but the exact worst excess = 2^-690.276507; exact integer comparisons:
  excess * 2^691 <= 1 is FALSE; excess * 2^690 <= 1 is TRUE.
- so "sum <= (1 + 2^-691) * Q_2(k+2)" (bsra_findings A4 + statement spec;
  bsr_check P5 banked print; dag qa22_m_le_t_extension statement;
  bsr_gate_repromotion; bsr_consistency D3) is FALSE at (13,1/16) by a
  factor 2^0.72. The correct grid-wide constant is (1 + 2^-690), exact.
- root cause: lg_frac(x) = num.bit_length() - den.bit_length() rounding
  (same family as catches #154a/#154c); for excess = 2^-690.2765 the bit-
  length difference happens to be -691. bsra A4's "= 2^-691.0" inherited it.
- direction/force unaffected (2^-690.28 is still astronomically small; the
  extension still costs ONE first-scale column + epsilon), but the packet
  and the dag statement must carry (1 + 2^-690) — number fix at surgery,
  and bsr_check P5's print string should be repaired alongside #154.

## CATCH #156 — rate-1/2 quotient-mass triviality must be SCOPED

The banked "rate 1/2 carries no dyadic quotient mass" (B_quot = 0 exact;
dyadic_profile_evaluation §4.1 parity kill, echoed at
xr_target_budget_audit) is a statement about the banked ODD-A M > t_res
rows only. The extension's rate-1/2 own-cell rows are NONZERO — A_own is
even, so the parity kill never touches them — and Q_2(k+2) =
C(n/2-1, n/4+1) at rho = 1/2 is the LARGEST first-scale column on the
grid; the COL cap also attains its maximum (exactly 4) there. Any consumer
citing the triviality unscoped would silently drop the biggest extended
row. (No banked node is currently wrong — the risk is citation drift;
scoping line added to the packet statement + claim contract.)

## Additional precision note (not a catch): D1's "disjoint ranges" and the
## banked QA.22 rows

bsr_consistency D1's disjointness claim ([2,t] vs (t,..]) concerns the
7-lemma COMPOSITE's cells and is correct. But the extension's scale range
DOES overlap the banked QA.22 rows' range (M > t_res, t_res = A_row - k
<< t; e.g. prize 1/4: banked M* = 2^34 <= extension max 2^39). Cell
disjointness there is by PARITY (A_own even, all seven banked A odd) —
newly proved in this packet (clause iii.b) and mutation-guarded (MUT4).
Scope pin: re-check if an even-reserve row is ever banked.

## VERDICT: PROVED (packet complete)

- qme_statement.md — the extension, five clauses, corrected constant.
- qme_proof.md — proofs: (i)/(ii) one-line algebra + grid equalities;
  (iii) partition + parity; (iv) Regime A exact (s = 13..20) + Regime B
  certified integer-only entropy bounds (s = 21..44; B1/B2 classical,
  dyadic log2 certificates at 1/128, cross-checked on 24 overlap rows);
  (v) allowance identity + planted-column Pascal identity + old-ledger
  negligibility.
- qme_verify.py + qme_verify_out.txt — exit 0, 26 PASS, 0 FAIL, 5/5
  mutations TRIP, ~18 s under ramguard tiny. Full grid: 3392/3392 own
  cells; worst excess 2^-690.2765 at (13,1/16) (M=4-carried, residual
  <= 2^-300); min certified margin 168245 bits at (21,1/16); certified
  L = 1.0952e12..2.9034e12 bits at the four official maximal rows; 719
  identity + slack line at s = 41..44 (FYI 719 also at s = 40, 45);
  per-rate cap maxima exactly {4, 2, 4/3, 4/3}; planted ratio
  [2047/2049, 15).
- qme_claim_contract.md — consumes/serves/pins/mutations/surgery items.
- dyadic_profile_evaluation/verify.py replayed ALL PASS (old rows
  untouched).

Surgery items for the maintainer (from the contract): the #155 number fix
in dag.json + three bsr docs + bsr_check P5 print; then the census gate's
re-promotion CONDITIONAL -> PROVED-pending-audit per bsr_gate_repromotion
(this was the gate's single remaining input).
