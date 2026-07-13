# qme_claim_contract — qa22_m_le_t_extension
# (proof packet 2026-07-13; fresh-context proof worker; catch ledger #155-#156)

## Claim

**qa22_m_le_t_extension: PROVED** (pending the house-law fresh-context
replay before dag status flips). The exact statement is qme_statement.md's
THEOREM, clauses (i)-(v): the QA.22 quotient-profile ledger extends from
dyadic M > t to ALL dyadic 2 <= M <= t at the P1-OWN cells
(M, A_own(M) = M*ceil((k+1)/M)), each priced 719 * Q_M(A_own), plus the
csp cell (2, k+4) at 719 * Q_2(k+4) if consumed; every row is
nondegenerate; the COL-priced landing fits every row's allowance with
719/4 = 179.75 headroom; the M > t rows' dedup is unchanged (scale-range
disjointness vs the composite; PARITY disjointness vs the banked QA.22
rows); and the whole extension costs the profile clause ONE first-scale
column + epsilon per band cell:

    sum_{M dyadic, 2<=M<=t} Q_M(A_own(M)) <= (1 + 2^-690) * Q_2(k+2)

— CONSTANT CORRECTED from the pre-computed 2^-691 (catch #155; the 2^-691
form is FALSE at the worst cell (13, 1/16), exact excess 2^-690.2765).
Grid: s = 13..44 x four rates (supersets every narrower official-grid
reading; the four official maximal rows (41,1/2), (42,1/4), (43,1/8),
(44,1/16) included).

## Proof class

Pure ledger arithmetic, as pre-classified: exact big-integer evaluation
(s = 13..20) + certified integer-only entropy bounds (s = 21..44; classical
inequalities B1/B2 with one-line proofs, dyadic-rational log2 certificates
at precision 1/128, machine-asserted; certificates cross-checked against
exact values on 24 overlap rows). No new mathematics, no conjecture, no
float in any load-bearing comparison.

## Consumes (all PROVED)

- `dyadic_profile_evaluation` — the ledger being extended (Q_M convention,
  banked M > t_res rows; its verify.py replayed ALL PASS this session:
  the old rows are UNTOUCHED).
- `petal_column_lemma` (Lemma COL) — identifies WHAT lands at the own
  cells (<= [n/(n-A_own)] * Q_M); this packet supplies the grid-wide cap
  arithmetic n/(n-A_own) <= 4 and the allowance absorption.
- `petal_g2_support_forcing` (stabilizer partition) — the exact-scale
  partition behind dedup clause (iii.a) (inherited via bsr_consistency D1,
  unchanged).
- `v13_capf_planted_lower_count` — clause (v.b)'s planted column
  Q_2^planted(k) = C(n/2-1, k/2) (the unavoidable mass the 719 line is
  calibrated against).
- petal_growth r2 exact allowance: 719 = floor(n^6/C(n+6,6)) at the four
  official maximal rows (re-verified here, incl. the slack line
  719*C(n+6,6) <= n^6).

## Serves

- `petal_small_scale_staircase_census` (the census gate) — this was its
  SINGLE remaining input (dag edge qa22_m_le_t_extension -> gate, kind
  req). With this packet the gate's re-promotion spec
  (bsr_gate_repromotion.md) says CONDITIONAL -> PROVED-pending-audit.
- Falsifier F(G)-3 (bsr_falsifiers.md): EXECUTED grid-wide — no fire
  (with the corrected constant; the 2^-691 form fires exactly as #155
  records and is kept as mutation control MUT2).

## Verification record (all 2026-07-13, tools/ramguard tiny; scratchpad)

- qme_verify.py: exit 0, 26 PASS, 0 FAIL, 5/5 mutations TRIP, ~18 s.
  Output banked at qme_verify_out.txt. Key numbers: 3392/3392 own cells
  nondegenerate + capped; per-rate cap maxima exactly {4, 2, 4/3, 4/3};
  worst exact excess 2^-690.2765 at (13, 1/16), M=4-carried (residual
  <= 2^-300 relative); 96 large rows certified with min margin 168245
  bits at (21, 1/16); certified L at the official maximal rows 1.0952e12
  .. 2.9034e12 bits; planted ratio in [2047/2049, 15).
- qme_probe1.py / qme_probe2.py: discovery runs (worst cell; certificate
  machinery validation).
- critical/nodes/dyadic_profile_evaluation/verify.py: replayed ALL PASS.

## Mutation controls (all TRIP; any future re-verifier must keep them)

MUT1 allowance 719 -> 3 (per-cell cap breach at rho=1/2, M=t);
MUT2 the pre-computed (1 + 2^-691) constant (FALSE at (13,1/16) — the
     #155 regression guard);
MUT3 A_own -> M*floor(k/M) (band-floor breach);
MUT4 banked QA.22 row A made even (parity dedup breach);
MUT5 dominance against the wrong top term Q_4(A_own(4)).

## Scope pins / honesty

- Ledger side ONLY. The count side (what lands) is Lemma COL's and the
  gate's; nothing here prices non-OWN cells (the F(G)-2 widest-ALL seam is
  unchanged and NOT covered).
- The csp cell is priced only IF consumed (#152 band scope); its row
  arithmetic is verified unconditionally.
- Parity disjointness verified at the seven banked QA.22 rows; a future
  EVEN-reserve corridor row would need the one-line re-check (the banked
  reserves are 2^j + 1 shapes).
- k even (official rows) is used only through A_own(2) = k+2; clause (i)'s
  algebra covers M !| k own cells (odd-k caveats closed by COL, not here).
- CATCH #156 (scoping): the banked "rate 1/2 carries no dyadic quotient
  mass" (B_quot = 0; dyadic_profile_evaluation §4.1, xr_target_budget_audit)
  applies to the odd-A M > t_res rows ONLY — the extended ledger's
  rate-1/2 own rows are NONZERO (largest first-scale column of the grid;
  COL cap exactly 4 there). Consumers must not cite the triviality
  unscoped.

## Number fixes owed at surgery (do NOT merge without them)

1. dag.json qa22_m_le_t_extension statement: "excess 2^-691" -> "excess
   2^-690.28 (bound (1 + 2^-690))" (#155).
2. bsr_gate_repromotion.md owed-item paragraph, bsr_consistency.md D3,
   bsra_findings.md A4 record: same constant fix.
3. bsr_check.py P5 print string ("2^-691" via lg_frac): repair alongside
   the #154 lg_frac items (the check itself passes — it tested 2^-10).

## Re-surgery criteria (this packet's own)

1. Any official row consumed outside s in [13, 44] or a fifth rate — re-run
   qme_verify.py with the enlarged grid (pure re-execution).
2. The P1-OWN consumption pin changes — re-run E1/E2 at the new band
   (mirrors the gate's criterion 2; widest-ALL must NOT be consumed).
3. An even-reserve QA.22 row is banked — re-check parity dedup (iii.b).
4. Lemma COL's chain contradicted anywhere (F(G)-1) — escalates upstream,
   and this packet's clause (ii) consumption story re-opens with it.
