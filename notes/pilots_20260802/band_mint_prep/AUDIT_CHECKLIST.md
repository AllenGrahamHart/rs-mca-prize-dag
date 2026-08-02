# AUDIT CHECKLIST — band-lane mint package (6 nodes)

What the coordinator should hand-verify before wiring, per package, plus
every place where I was uncertain of scope. **Flags are raised, not
guessed.**

Replay command for all six (from the repo root):

```text
tools/ramguard tiny -- python3 <node>/verify.py
```

Measured runtimes: 0.14 / 0.41 / 2.38 / 1.35 / 1.87 / 0.12 s (packages
1-6 in task order). All pure-python integers, deterministic, no
third-party imports, no reads outside their own directory (all pins
inlined; provenance paths appear in comments only), so they keep
passing after the move. Check totals: 16 / 10 / 19 / 20 / 17 / 17 —
**99 PASS, 0 FAIL** at draft time.

---

## 0. Cross-cutting flags (read first)

- *(F0.a — SOURCE-PATH DISCREPANCY, task list.)* Package 4's brief
  cites `notes/pilots_20260802/xr_band_occupancy/{REPORT,FABLE_AUDIT}.md`
  as the source of the KEY LEMMA + pencil mass identity + MC family.
  Those live in `notes/pilots_20260802/list_bound_transfer/` (its
  FABLE_AUDIT item 4 is the mint-queue entry). I drafted from the true
  source and said so in the node. **Confirm the brief meant
  list_bound_transfer** (the xr_band_occupancy audit carries the
  AMENDMENT that retires the reduction — related, but not the source).
- *(F0.b — Lemma 0 placement.)* The fibre identity (graded-band-ledger
  THEOREM 2, "core = support intersection EXACTLY") is consumed by
  packages 1, 2 and 5 but was not assigned to any package by the brief.
  I minted it INLINE in `xr_two_slope_cost_theorem` as Lemma 0 (with
  proof) and cite it from the others. Alternatives: move it into
  `xr_band_ledger_theorems` (its pilot of origin) or mint it
  standalone. **Coordinator's call; the current placement makes the
  cost theorem self-contained.**
- *(F0.c — SUPERSESSION / candidate SEVENTH node.)* The
  xr_band_occupancy pilot's audit (item 5) had queued its unified
  fibre-strip THEOREM 1 (+T2 high-depth injectivity, +T4
  partial-linear-space) as SUPERSEDING the ledger T4/T5 mint. The
  brief chose the ledger set; I drafted as briefed and recorded the
  supersession flag inside `xr_band_ledger_theorems`. If the unified
  T1/T2 is wanted later it is a natural seventh node (statement =
  band-occupancy REPORT section 1; T2 is correct — only its LIST
  consequence was retired). **Decide: leave as flagged, or commission
  the seventh node.**
- *(F0.d — cumulative counter, no correction needed.)* The
  occupancy-v2 REPORT's "371 witnessed events" for Theorem G is the
  CUMULATIVE final value of `hunt_e0.json`'s running counter
  (per-shape increments 61/129/57/113/11, sums 371). Not a
  discrepancy; documented in package 2's proof.md so nobody
  re-reads the per-shape numbers as independent 371s.
- *(F0.e — MC shell vs family at small q.)* `mc_c1.json`'s "7 pairs at
  depth 2" (q = 97) is the PAIR census; the u-side shell at q = 97
  actually has 9 members (7 coset-union + 2 accidental, which lack the
  `X | P_T` divisibility and so produce no v-side partner — hence 7
  pairs). My first draft of package 4's check D wrongly demanded
  shell = family and FAILED; the corrected check verifies MC-1
  (shell = indexed T-set, including accidentals — the theorem as
  stated), MC-3 (family = C(N,m)/N, contained), and P5 (excess
  2/2/0 at q = 97/193/12289, vanishing at q > C(16,10)). **Hand-verify
  this reading against the pilot's P5 and the package-3 scan.**
- *(F0.f — the escape-floor cap.)* The support-4 REPORT states S4-15
  as `rank >= sum min(h, |S_a \ S_a^inf|)`. My first derivation
  dropped the `min(h, .)` cap; the K_V fixture falsifies the uncapped
  form (40 > rank 35) and the drafted proof/statement now carry the
  capped form with the cap machine-verified as load-bearing
  (package 6 check F). This mirrors the pilot's own caught-and-fixed
  history. **Hand-verify the corrected two-line derivation
  (rank = Vh - dim Rel >= sum_a (h - (|S_a^inf|-k)^+)).**
- *(F0.g — not re-derived.)* Package 6's official-scale U-mechanism
  numbers (51 clusters x C(5,2) = 510 at RowC 1/4) are
  CONSISTENCY-CHECKED against `stage6_repricing.json`, not re-derived
  (the cluster packing formula lives in the pilot's advlib/stage6
  code). Same status for nothing else in the wave — every other
  number is re-derived from scratch.
- *(F0.h — cross-pilot pin agreement.)* The three prize-row
  band-proper sums agree byte-for-byte between
  `xr_occupancy_v2/arith.json` and `xr_graded_band_ledger/band_arith.json`
  (36839268578566 / 43010571891409 / 44764496190275) and are
  recomputed independently by package 5's divisor-block code
  (brute-forced at RowC scale). No discrepancy anywhere I checked
  between pilot prose and persisted JSONs, EXCEPT the readings flagged
  in F0.d/F0.e (prose fine, my initial misreading).
- *(F0.i — L_P reading in the verifiers.)* All fresh scans count
  `L_P` as "rays of agreement >= A whose agreement set contains
  `Z_P`" over ALL of `P^1` incl `(0:1)` — the banked toy reading. The
  selected-first-match distinction (definitions item 8) does not bite
  on these fixtures (no over-`A` rays inside gates; pilot record
  showed no divergence at toy scale), and package 3's statement pins
  the distinction where it is load-bearing (MC at scale). **Confirm
  this is acceptable verifier semantics.**
- *(F0.j — one new inference of mine.)* Package 3's BP(2) exclusivity
  is derived as: live shift class needs `g = h-d`, `g | j`,
  `j <= M-1 = d-1`, hence `2d >= h+1`, hence dichotomy T2(b) applies.
  The adjudication pilot asserted exclusivity via "the banked
  k-packing exclusivity"; my chain is sharper and creates the
  `dichotomy -> quantization` req edge. It is three lines —
  **hand-verify them** (this is pilot-plus-inference, the only place
  in the wave where I added a step rather than transplanting one).

## 1. `xr_two_slope_cost_theorem`

Hand-verify:

1. **Claim 1 Step 2 (block-sum transversality).** `c_2 = -c_1` forces
   `c_1` supported in `S_1 ^ S_2 = Z` (this uses L1's
   `C_{S_1} ^ C_{S_2} = C_Z`, which needs `|Z| >= k` — true, `|Z| =
   k+d`), then `(z_1 - z_2)c_1 = 0`. Check the `(0:1)` slope variant.
2. **The corollary's realisability step**: kernel strictly containing
   `RS_k x RS_k` iff rank `<= 2(n-k) - 1` — off-by-one is easy here;
   the verifier's check G (kernel dim `2n - 2h`) is the witness.
3. **The per-ray reading**: the six-row table's THREE different
   denominators (2h, 2h-2, h) and which is "the banked 191/223/479"
   (per-datum at prize, free-slope at RowC — both give the same
   numbers; the RAY-count reading is the amendment's). Check the
   statement keeps these straight.
4. **V\* formula**: `V* = floor((n-k+1)/(h-1))` is the `d = 1`
   sunflower/point-budget law; `C(V*,2)` matches
   `arith_repricing.json` exactly. Confirm V\* is the right pin for
   "the K_V re-pricing" (the pilot's RowC V\* differs — RAYCAP binds
   at toy scale; the statement quotes prize rows only).
5. **Flag (F1.a)**: Claim 2's free-slope codimension is stated in the
   informal determinantal sense (2-parameter slope family of
   codim-2h kernels, pairwise distinct). If the surface wants the
   scheme-theoretic phrasing, edit; the machine content (all 66
   slope pairs rank 2h; distinct kernels) is exact either way.

## 2. `xr_two_slope_deficit_dichotomy`

Hand-verify:

1. **Theorem 2(a)'s `P^1` conventions** (`z* = 0 <=> f_1 = f_2`,
   `(0:1) <=> g_1 = g_2`) and that (H3) pencil-wide incl `(0:1)` is
   genuinely needed (the `(0:1)` case of the proof).
2. **Theorem G(ii)'s use of Lemma 0** — equality (not containment) of
   the overlap with the witness core is the fibre identity; check the
   `2 x 2` inversion covers a `(0:1)` member.
3. **Scope of "rank sharing"**: the node claims the PAIRWISE channel
   only (dual overlap by L1 + witness), plus core transversality;
   family-level deficits are explicitly routed to
   `xr_support4_structure`. Check no sentence implies pairwise
   exhaustiveness (hunt.py E0 checked exactly the pairwise form).
4. **Flag (F2.a)**: Theorem 2 removes SHARING at `2d >= h`, not
   population; the statement says so ("does not empty the high
   band") — confirm consumers cannot misread it as a high-band
   emptiness claim.

## 3. `xr_mc_depth_quantization`

Hand-verify:

1. **Claim 1's exactness dependence**: "diagonal at EXACTLY `w`"
   needs MC-2's ceiling (no accidental extra agreement); the
   citation into package 4 must survive any renaming.
2. **BP(1)'s `M | k` step** needs `M < k`, supplied by
   `2(h-2) < k` at all six rows (verifier check C). This is a
   six-row-shape fact; the claim is scoped to it.
3. **BP(3)'s fibre computation** (`zeta_P(i) = -x_i^j`, fibres =
   `mu_g`-cosets, forced-ray agreement `(k+d) + g`) — the adjudication
   pilot's chain, transplanted; check against
   `exp_band_proper.py`'s docstring derivation.
4. **F0.j's three lines** (`2d >= h + 1` on the live shift class).
5. **Claim 5's `N_{h-1} <= n/2`** uses selected-support exclusivity;
   check the "any exact-A ray" non-example sentence stays verbatim
   from definitions item 8 (load-bearing).
6. **Flag (F3.a)**: the h-even control fixture pins (`N_4 = 2` at
   `j = 2`, `|Gamma| = 10`) were re-derived fresh and match
   `checkpoints/band_proper.json`; the checkpoint's `N_d_any`
   naming suggests the any-ray reading — my scan agrees at these
   fixtures (F0.i). Confirm.
7. **Flag (F3.b)**: MC-4 completeness (char-0 Lam-Leung) is INPUT,
   machine-checked empirically at one shape (q = 65537 census);
   BP(3) does not need it. If the surface wants BP(1) fully
   unconditional, re-scope BP(1) to "coset-union complements with
   `M = 2^ceil(log2 d)`" (the form actually used downstream) — the
   statement already phrases it that way; confirm it reads as
   intended.

## 4. `xr_band_key_lemma_pencil_mass`

Hand-verify:

1. **Theorem I vs the `(0:1)` member**: the sum is over `z in F_q`
   only; corollaries are stated over `F_q`. Check no consumer reads
   `q+1` members into the mass identity.
2. **KEY LEMMA rename**: every "cascade event" occurrence is now
   "joint-explanation event" (definitions item 5); grep the drafts
   to confirm none survives.
3. **The graded consequence's size threshold** (`>= A-1` for the
   below-cascade equivalence) — check against definitions items 3/5.
4. **MC-1/MC-2's coefficient-window derivation** in proof.md (the
   `G = reversal of V_T` computation, the `X^{k+w-1+t'}` coefficient
   giving `c = 0` for MC-2, the `s`-window giving `e_s = 0` and the
   product condition). This is my full write-out of the pilot's
   PK1(A)-at-general-`w` argument — the one proof in the wave that
   was reconstructed rather than transplanted verbatim. It is
   machine-checked exhaustively at three fields, but **the prose
   derivation deserves a line-audit**.
5. **MC-1 sufficiency (converse)** is by dimension count + exact
   division — check the paragraph, or accept it on the strength of
   the exhaustive census equality (check D).
6. **Flag (F4.a)**: the NOT-claimed section hard-blocks citing this
   node as a list bound (the retired reduction). Confirm the wording
   is strong enough for future consumers.
7. **Flag (F4.b)**: F0.e's small-`q` excess reading.

## 5. `xr_band_ledger_theorems`

Hand-verify:

1. **T3's subtraction note** against
   `critical/nodes/common_code_line_budget`: the hypothesis
   `a + b - n >= k` failing at all six rows is the ledger pilot's
   node-local finding (its audit wrote a node-local flag). Confirm
   the flag file exists on the banked node and the two statements
   cross-reference consistently.
2. **T4's ray keying** and the FALSE slope-keyed reading (15/76) —
   check the statement can't be quoted with "slope" substituted for
   "ray".
3. **The master inequality's chain**
   (`|Gamma_band| <= SUM_P L_P <= SUM_d N_d L(d)`) — the middle step
   needs every `Gamma_band` slope to be live for SOME counted pair;
   check the `Gamma_band` definition matches the TARGET's.
4. **Pricing**: the divisor-block identity
   `SUM_{d=1}^{h-2} L(d) = (h-2) + SUM_{g=2}^{h-1} floor((R-h)/g)`
   and the three prize pins; RowC brute-forced in-verifier. Also
   `L(h-1) = n-A+1` and the 5-of-6 printed-column kill pattern
   `[T,T,F,T,T,T]`.
5. **W's phrasing**: worst-case TIGHT (slack 1.0 / 2.0) coexists with
   "lossy generically" — confirm the corrected amendment wording is
   what the surface wants on record (the pre-amendment "arbitrarily
   lossy" must not survive anywhere).
6. **Flag (F5.a)**: the slack-2.000 witness here is the FULL sunflower
   (all `C(m,2)` forced slopes), not package 1's cycle variant; the
   two constructions differ (cycle: M = m data; full: `L_P = m-1`).
   Check the two statements name them distinctly.

## 6. `xr_support4_structure`

Hand-verify:

1. **S4-1's pointwise argument** (0-or->=3) — one paragraph, carries
   the whole localisation theory.
2. **S4-3's proportionality cascade** (two proportional => all four
   => quadruple intersection >= k+1 => (T) violated) and hypothesis
   (T)'s sourcing from the banked pair-core k-packing via the fibre
   identity — check the conditional wording ("when the pairwise
   intersections are distinct pair cores").
3. **S4-4's Segre/(1,1)-divisor equivalence** with cross-ratio — the
   z_4 sweep (check C) is the machine witness (dim Rel = 1 exactly at
   CR matches); the prose equivalence (graph of a Mobius map)
   deserves a look.
4. **S4-14's connectivity induction** ("adding supports one at a
   time, each new S_a meets ONE existing support in >= k points") —
   pairwise-intersecting gives this for ANY ordering; fine — but
   check the finite-slope caveat (`pi_1(G_inf) = 0`) is stated.
5. **Claim 7's status line**: MEASURED-NOT-PROVED, named open
   sub-items verbatim from the audit. Confirm the falsifier section's
   "(would upgrade claim 7, not falsify this node)" parenthesis is
   the right legal reading.
6. **Flags (F0.f, F0.g)** above.

---

## 7. Candidate SEVENTH node — not written, flagged

The xr_band_occupancy pilot's **unified fibre strip (T1) + high-depth
injectivity (T2) + partial-linear-space (T4)** were mint-queued by its
own audit and are consumed nowhere in this wave. T1 contains the
ledger T4/T5 mechanism with weaker hypotheses and the `z in {0,(0:1)}`
extension; T2 is CORRECT (only its list-bound consequence was retired
— the retirement is recorded in package 4). If the coordinator wants
the unified statements banked, the statement/proof are a short delta
on packages 2 and 5, and the verifier is a small extension of their
shared scan engine. Until then, the supersession flag inside
`xr_band_ledger_theorems` is the record.

## 8. Cross-cutting things I did NOT do

- No `dag.json`, `background/`, `critical/`, `tools/` or m2-related
  file was touched; the verifier manifest was not regenerated (it
  must be, after the move).
- I did not run any pilot's own scripts; every number cited was
  re-derived in a fresh implementation inside each `verify.py` and
  cross-checked against the pilots' persisted JSONs (never against
  prose alone). Where prose and JSON could be misread against each
  other, the reading is flagged (F0.d, F0.e), not silently chosen.
- I did not attempt the two named open sub-items (the zero-escape
  collapse proof; `V <= m/2`), the group-theoretic amplification
  lane, or the double-hole family — all remain open/pilot-record.
- **Compute-law self-report (violation, flagged not hidden):** every
  verifier run and every fixture computation ran under
  `tools/ramguard tiny`. However, during source triage BEFORE
  drafting, ~8 short read-only JSON-inspection heredocs (printing
  fields of `dag.json` and the pilots' checkpoint JSONs) ran as bare
  `python3` in violation of the standing compute law. No computation
  of record depends on those runs — every pin they surfaced is
  re-derived or re-read inside the ramguarded verifiers — but the law
  is absolute and the lapse is recorded here for the coordinator.
