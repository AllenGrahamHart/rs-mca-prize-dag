# PREREG — pincer_formalization (round 27)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

The band-closure analytic half (rate_half_band_closure, critical
TARGET; the anti-concentration direction of the FLOOR v2) cannot
currently be STATED sharply at the razor rows: the WP5 verdict
(critical/nodes/rate_half_band_closure/notes/WP5_RATEHALF_VERDICT.md)
pinned that the row-local random-word first-moment crossing sits
BELOW the proved unsafe reach near the cap, so the floor's intended
model must be the WORST-WORD/PINCER object — "whose per-row crossing
is NOT yet formalized: an open item OF THE FLOOR." Your job: close
that formalization gap. This campaign has felled three
"missing-theorem" claims that were bookkeeping (rounds 24, 25, 26) —
check whether this is the fourth BEFORE building anything new
(CATCH-24A: own-repo grep for the pincer crossing under all its
names).

## Deliverables (ORDER IS BINDING)

**D0 — THE FOUNDATION AUDIT (first, before any formalization).** The
WP5 flag of record: "the safe-side-above-sigma* pincer machinery was
consumed from banked docs, not re-audited." Audit it now: read the
pincer/balance safe-side proof (P6_RATEHALF_SIBLING.md, the
pro_brief_razor.md sigma* provenance — sigma* = 8,592,912,738 =
t*-1, generic pincer; and whatever banked docs they cite), replay
its arithmetic exactly (the WP5 machine checks are your calibration:
sigma* replay, cap reach 2^33, band width 2,978,146, razor threshold
255.899990), and issue a verdict: SOUND / REPAIRABLE / BROKEN, with
the exact load-bearing steps listed. If BROKEN, stop and report —
everything downstream changes.

**D1 — THE FORMALIZATION.** Define the worst-word/pincer per-row
first-moment crossing as an exact object: for an admissible razor
row (q, k, n = 2^41-shape), a computable function sigma_FM(row) with
a stated domain, such that (i) it specializes to the machinery that
proved the safe side above sigma*, (ii) it does NOT reduce to the
random-word crossing (which is refuted near the cap — that
refutation is your negative control), and (iii) it is computable
exactly at scaled band-analogue rows (q <= ~2^40, the window-law
campaign's regime). Register the candidate definition BEFORE
computing with it.

**D2 — THE VERIFICATION AGAINST BANKED EVIDENCE.** Compute
sigma_FM at the banked crossing-fidelity cells (the 18/18 family,
notes: f6a2_results.json; the ~200-prime window-law grid cited in
the witness-hunt recon) and at the four upstream deployed pairs
(the regime-map replay — KB MCA/list 1116047/1116046, M31
1116023/1116022 at n = 2^21). The formalized object must reproduce
what the random-word model already got right AND fix what it got
wrong (the near-cap ordering vs the proved unsafe reach). Register
expected outcomes per cell family first.

**D3 — BAND-AC, THE CONJECTURE OF RECORD (draft).** State the
analytic half as ONE sharp conjecture: at every admissible razor
row, the band determination equals the sigma_FM prediction —
deficit below, safe above, no anti-concentration failure. Name the
quantifiers (which rows, which sigma range, what "equals" means —
exact count vs Poisson tolerance), the consumer bar per consumer
(adjacency_closing, list_adjacency_closing, mca_safe need the
LOCATED determination — read their statements and name each bar,
CATCH-24C), and pre-register at least two falsifiers with power
controls. If D1's object makes the old FLOOR v2 statement wrong in
any particular, say exactly where.

## Escape tests (before the main work)

- Replay the WP5 machine checks (sigma*, cap reach, band width,
  razor threshold, the four-pair margins to 4 decimals).
- Reproduce two f6a2 crossing cells from the banked script (SCRATCH
  COPY — see rules).

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4062; do not read the other round-27 pilot dirs
  (nonpoly_flank_census, staircase_extension, cancellation_recon).
  Pass this clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from
  /home/u2470931/smooth-read-solomin/prize — including file patching
  and JSON peeking. RAMGUARD_TIMEOUT documented per use.
- BANKED SCRIPTS RUN FROM SCRATCH COPIES ONLY (copy into your dir or
  the session scratchpad first) — a banked script may write into its
  own banked dir (the round-26 lesson).
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no bulk
  loads; checkpoint long runs; background batches with results files
  for >10-min runs.
- DRAFT-ONLY: writes only in notes/pilots_20260809/pincer_formalization/;
  no dag/nodes/tools writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing; misses
  first. Name every measured functional (CATCH-19C). Own-repo grep
  gates every "this object does not exist" claim (CATCH-24A).
- Your final message IS the report. End with a compliance paragraph.

## Pilot registrations (appended by the pilot before any computation)

*(pincer_formalization, round 27, 2026-08-09. Everything below was
written after READING ONLY — no interpreter had been invoked at the
time of writing. Reads performed: WP5_RATEHALF_VERDICT.md,
P6_RATEHALF_SIBLING.md, notes/pro_brief_razor.md, notes/floor_depth.md,
notes/upstream_determination_datum.md, node statement.md / proof.md /
conditional.md, node.json statement field, xr_radius_arithmetic/proof.md,
WAVE9_AUDIT_FINDINGS.md:185-239, the three consumer conditional.md
files, head of f6a2_results.json.)*

### R0 — Named functionals (CATCH-19C: every measured object named here)

Row shape throughout: `n = 2^41`, `k = 2^40` (rate 1/2), `q` prime,
`q = 1 mod n`, `L := log2 q`, agreement `a`, excess `sigma := a - k`,
co-support `j := n - a`, prize gate `B*(q) := floor(q / 2^128)`.

1. **`FM(a; q)`** — the RANDOM-WORD first-moment (union-bound) slope
   count at exact agreement `a`:
   `FM(a;q) = q * C(n, j) * q^{-(a-k)} = C(n, n-a) * q^{1-(a-k)}`.
   (Banked Lemma FM1 as used in `xr_radius_arithmetic/proof.md` §1,
   there written `E[X] = C(n,j)(1-q^{-t})q^{1-t}`.)
2. **`t*(q) := min { t : FM(k+t; q) <= B*(q) }`** — the corridor edge;
   equivalently `min { t : t*L >= log2 C(n, n-k-t) + 128 }`.
   **`sigma_FM^rand(q) := t*(q)`** is the random-word FM crossing
   excess; `s*(q) := t*(q) - 1` is the last FM-unsafe excess.
3. **`B_mca(a)`** — the EXACT worst-word object: max number of finite
   slopes carrying a failed support-wise MCA witness with agreement
   `>= a` (node statement.md, (RH-ADJ) block).
4. **`sigma_RH(q) := a_RH(q) - k`** where `a_RH(q)` is the exact
   adjacent crossing: `B_mca(a_RH) <= B*(q) < B_mca(a_RH - 1)`.
5. **`D(c, d; q)`** — quotient-remainder floor reach at 2-power scale
   `c`, depth `d`, i.e. the `d*c` of `pro_brief_razor.md` §Setup, with
   box charge `L` bits/fiber and trigger `L - 40`.
   **`Reach(q) := max_c max{ d*c : trigger met }`** (the "cap reach").
6. **`W(q) := s*(q) - Reach(q)`** — the FLOOR-v2 "band width".
7. **`rho(q) := sigma_RH(q) / sigma_FM^rand(q)`** — the model-fidelity
   ratio; the D2 negative control.
8. **Upstream pair margin** `mu(row) := log2 C(n,m) - log2( p^{m-K-s}
   * floor(q*eps*) )`, `s in {0,1}` (list/MCA), as in
   `upstream_determination_datum.md`.

### R1 — Candidate definition registered for D1 (registered BEFORE use)

**Candidate A (the brief's ask, "worst-word/pincer per-row FM
crossing")**: `sigma_FM^worst(q) := min { t : max_y N(y, k+t; q) <=
B*(q) }` where `N(y,a;q)` is the number of finite slopes with a failed
support-wise MCA witness for received word `y` at agreement `>= a`.
Note `max_y N(y,a;q) = B_mca(a)` **identically**, so Candidate A is
**definitionally equal** to `sigma_RH(q)` of R0.4. This equality is
registered as the CATCH-24A test: if it holds, D1's object already
exists in-repo under the name `a_RH(q)` / `(RH-ADJ)` and the
"not yet formalized" flag is bookkeeping, not mathematics.

**Candidate B (a genuinely new object, only if A is not already
in-repo)**: `sigma_FM^pin(q) := min { t : max(B_ca^far(k+t),
S_sparse(k+t)) <= B*(q) }` via the proved lossless split (RH-SPLIT).

### R2 — Predictions with numeric windows (pre-registered)

**Escape tests (calibration; exact integers / stated decimals):**

- **E1** `t*(L=255.9) = 8,592,912,739` and `s* = 8,592,912,738`
  EXACTLY; the other three rates `7,014,660,390 / 4,722,556,392 /
  2,943,177,800` exactly.
- **E2** `Reach` at `L=256`, box `2^256`, trigger `2^216`:
  `= 2^33 = 8,589,934,592` exactly, plateau over `c = 2^22 .. 2^33`.
- **E3** `W = s* - 2^33 = 2,978,146` exactly (banked radius count
  2,978,147 = inclusive endpoint convention).
- **E4** q-threshold `= 255.89999 +/- 0.00001`; depth at threshold
  `8,592,916,480`; depth just above `8,592,912,384`.
- **E5** four upstream pair margins `22.197 / 22.011 / 3.259 / 3.073`
  bits, each to 3 decimals (tolerance +/- 0.001).
- **E6** two f6a2 cells reproduced from a SCRATCH COPY:
  `lq=255.90000002 -> sigma_star 8,592,912,736, s1_best_reach
  8,592,912,738, n_s2_hits 0`; `lq=255.92 -> 8,592,241,265 /
  8,592,241,266`.

**D0 predictions (verdict-bearing):**

- **P1** `sigma*`'s provenance is NOT a pincer: it is `t*-1`, the
  RANDOM-WORD first-moment corridor edge of `xr_radius_arithmetic`
  (a computation node whose pair-ledger input `xr_ledger_qpower` is
  itself OPEN). Predicted: CONFIRMED. Consequence if confirmed: the
  node.json phrase "sigma* provenance: generic pincer,
  pro_brief_razor.md" and pro_brief_razor.md's "SAFE side proved for
  sigma > sigma* (half-distance/pincer machinery)" are both
  mis-attributions.
- **P2** No in-repo theorem proves an MCA-side or list-side SAFE
  bound at rate 1/2 above `sigma*`. Predicted: CONFIRMED (own-repo
  grep; wave-9 already recorded it as "planning prose").
- **P3** `sigma*` lies strictly INSIDE the proved-unsafe region:
  `sigma_0 - s* = 8,594,128,895 - 8,592,912,738 = 1,216,157` exactly,
  and the wave-10 optimized floor gives `(2^34 - 1) - s* =
  8,586,956,445` exactly. Predicted: CONFIRMED.
- **P4** Therefore D0 verdict = **BROKEN** (predicted before
  computation). Falsifier for P4: an in-repo PROVED node supplying
  `B_mca(a) <= B*(q)` or `L_q(a) <= q*2^-128` for some `a <= k +
  sigma* + 1` at a razor row. I will grep for exactly this.

**D1 / CATCH-24A prediction:**

- **P5** The "worst-word/pincer per-row crossing" is ALREADY
  formalized in-repo (since 2026-07-17 wave-9, refined 2026-07-18
  wave-10) as `(RH-ADJ)` / `a_RH(q)` / `B_mca` inside the same node,
  with a PROVED lossless split `B_mca = max(B_ca^far, S_sparse)` and
  a DETERMINED closed form on `2^128 < q < 2^167`. Predicted: this is
  the FOURTH bookkeeping "missing theorem" of the campaign.

**D2 negative-control predictions (the random-word model vs proof):**

- **P6** In the determined region the proved worst-word crossing is
  `sigma_RH(q) = n - k - B*(q) + 1 = 2^40 - floor(q/2^128) + 1`.
  Numeric anchors predicted: `q = 2^129 -> sigma_RH = 1,099,511,627,775`;
  `q = 2^166 -> sigma_RH = 2^40 - 2^38 + 1 = 824,633,720,833`.
- **P7** `rho(q) = sigma_RH / sigma_FM^rand` lies in the window
  **[30, 80]** for every `L` in `[129, 167)`, and is monotone-ish
  decreasing in `L`. Point predictions: `rho(2^129) = 64 +/- 6`,
  `rho(2^166) = 62 +/- 6`. If `rho` were in `[0.9, 1.1]` the
  random-word model would be VINDICATED and P4/P5 would be in doubt.
- **P8** At the razor rows the FLOOR-v2 crossing point `s*` sits
  BELOW the proved bracket `[k+2^34, 3n/4]`, i.e. `s* < 2^34` and the
  true residual band is `sigma in [2^34, 2^39]`, width `>= 2^39 -
  2^34 = 549,738,634,304`, i.e. `>= 2^17.49` times the FLOOR-v2 band
  width 2,978,146. Predicted ratio `184,590 +/- 5%`.
- **P9** The four upstream pairs (n = 2^21) will replay EXACTLY
  (E5) and will NOT discriminate: they are `n = 2^21` extension-field
  rows whose unsafe side is a theorem and whose safe side is upstream's
  CONJECTURE (per `upstream_determination_datum.md`). Predicted: they
  confirm FM location arithmetic at their own rows and are silent on
  the razor rows (the WP5 F2 quantifier mismatch). They are therefore
  NOT evidence for FLOOR v2 at rate 1/2, n = 2^41.

**D3 predictions:**

- **P10** Consumer bars, to be read and quoted: `adjacency_closing`
  needs the LOCATED field-dependent adjacent certificate;
  `mca_safe` needs only the SAFE HALF `B_mca(a_safe) <= B*`;
  `list_adjacency_closing` no longer consumes this node's MCA half
  (owner moved to `rate_half_list_adjacent_crossing` at wave-10).
  Predicted: exactly two live consumers of this node's MCA content,
  with DIFFERENT bars.

### R3 — Escape-test list (run first, in this order)

E1, E2, E3, E4 (own code, stdlib `math.lgamma`, exact integers where
integral); E6 (scratch copy of `f6a2_fullscale_sweep_modal.py` core);
E5 (own integer replay of the four upstream pairs). Only then D0.

### R4 — Stop rule

If D0 = BROKEN, I stop the D1 BUILD (per the brief) and instead
report: the exact load-bearing steps that fail, the CATCH-24A finding,
the D2 negative control that prices the failure, and a corrected
BAND-AC pose offered as a DRAFT recommendation, not as a fait
accompli. No new object is constructed on a broken foundation.

