# SL-2 UNSTRUCTURED HIGH-WINDOW EXCLUSION — PRE-REGISTRATION

Opus 5, 2026-08-03. **Written BEFORE any code was run in this pilot
directory.** Sources read first (read-only):
`notes/pilots_20260803/listsize_program/REPORT.md` (SL-2's statement and
rank, the SHADOW LEMMA, the refutation anatomy, `rows.py` numerics);
`notes/pilots_20260803/sl1_windowed_projection/{FABLE_AUDIT.md,PREREG.md,
theory.py,mcdepth.py}` (THEOREM A/E/F, T-CELL, the windowed reduction,
the h-even fragility, M4 SPECTRAL EXCLUSION);
`background/nodes/xr_mc_depth_quantization/statement.md` (THEOREM 5,
BP(1)/BP(2)/BP(3), MC-4 scope, the h-even control);
`background/nodes/xr_band_key_lemma_pencil_mass/statement.md` (THEOREM
I/I', KEY LEMMA, MC-1 window conditions, MC-3 coset count, MC-5);
`notes/band_heart_consolidation_20260803/CONSOLIDATION.md` (the
CORE-DISJOINTNESS lemma, section 2, and its later CORRECTION);
`notes/BAND_LANE_DEFINITIONS.md` (items 2, 3, 5, 6, 8, 10 — band proper,
cascade tier, strip-freeness/P3, selected supports, structured family).

## 0. The question, pinned

`C = RS_k` on `H = mu_n` (`n | q-1`, split); `A = k + h`; received pair
`(u, v)`; a **joint-explanation pair** `P = (f,g)` has core
`Z_P = {x : f(x) = u(x), g(x) = v(x)}` of size `k+d` (**depth** `d`);
**band proper** = `d in [ceil(h/2), h-2]`; window = `[k+d, A-2]`.

**SL-2.** Can an UNSTRUCTURED (non-coset) admissible family of joint
pairs reach a band-proper depth with `> 0.68 n^2` members?

Standing context: the structured half is claimed PROVED excluded by
BP(1)/BP(3) + THEOREM F; the joint first moment has margin
(`d*_joint/h ~ 0.41 < 0.5`).

## 1. Predictions (P1-P8)

- **P1 (LEMMA W — the window system for a GENERAL word).** For
  `T <= H`, `|T| = r' = n-k-d`, with locator `E_T = prod_{t in T}(X-t)`:
  a codeword `P` (`deg < k`) with `u - P` vanishing on `H \ T` EXISTS iff
  the coefficients of `u E_T mod (X^n - 1)` in degrees `n-d, ..., n-1`
  all vanish — `d` equations, LINEAR in the coefficients of `E_T`, whose
  coefficient matrix is the Toeplitz matrix of the syndrome window
  `(u_k, ..., u_{n-1})`. The joint (pair) system is the same with `2d`
  equations (`d` from `u`, `d` from `v`). Predicted EXACT (iff, both
  directions), 0 violations on exhaustive toys.
- **P2 (MC-1 is the sparse-syndrome specialization).** For
  `u = X^{n-1} + c X^{k+w-1}` LEMMA W's system collapses to exactly
  `e_1(T) = ... = e_{w-1}(T) = 0` and `prod T = (-1)^{r'+1} c` at `d=w`.
  Predicted: identical solution sets, 0 mismatches (calibration against
  the banked MC-1).
- **P3 (COSET COLLAPSE / DESCENT).** If `T` is a union of `mu_M`-cosets
  (`M | n`) then `E_T(X) = G(X^M)`, and equation `j` of LEMMA W involves
  ONLY syndrome positions `= j (mod M)`. Hence if the syndrome window of
  `u` is supported in a single class `rho (mod M)`, exactly `d/M`
  equations survive (`M | d`), and they are LEMMA W's system for the
  QUOTIENT instance `RS_{k/M}` on `mu_{n/M}` at depth `d/M` with word
  `u^{(rho)}`. Predicted: an exact BIJECTION between scale-`M` cores
  upstairs and cores of the quotient instance.
- **P4 (BP(1) SCOPE CATCH).** The coset structure forces only `M | d`
  (`M | n`, `M | k`). BP(1) concludes "`d` is a power of two" only
  because definitions item 10 PINS `M = 2^ceil(log2 d) >= d`. For
  `M < d` there is no such conclusion. Predicted: at each PRIZE row there
  EXISTS `M = 2^j | gcd(n,k)` with a multiple of `M` strictly inside the
  band proper; the largest is `M = (h-1)/4 = 2^{m-2}` (`h = 2^m + 1`)
  with `d = 3M`. Predicted NOT to exist at the three RowC rows.
- **P5 (MARGIN COLLAPSE UNDER DESCENT).** The scale-`M` joint
  first-moment exponent is `Delta(d)/M` with
  `Delta(d) = log2 C(n, k+d) - 2 d log2 q`. Predicted: still negative at
  every row and every admissible `(M, d)`, but at `M = (h-1)/4`, `d = 3M`
  the margin collapses from `~3.6e11` bits to `O(10^2)` bits — the same
  order as the `log2(0.68 n^2) ~ 82`-bit budget, i.e. the descent is a
  `2^{31}`-fold amplifier that eats essentially the whole margin.
- **P6 (OFF-CLASS RANK PENALTY).** If the syndrome window is NOT
  supported in a single class mod `M`, the surviving off-class equations
  add `>= 1` to the rank of the system on the scale-`M` locus, costing a
  factor `>= q` in the count. Predicted: rank additivity exact on toys;
  rank(off-class) `= 0` iff exact `M`-quotient-periodicity of the
  syndrome window.
- **P7 ("SYNDROMES DESCEND" — the open adjudication item).** P3's
  bijection maps syndromes to syndromes, so the quotient convention of
  definitions item 6 is CORRECT for the window system and P3 (strip
  condition, quotient-periodicity at `M | gcd(n,k)`) formally fires on
  any exactly-degenerate scale-`M` adversary. Predicted: settled
  affirmatively, at the level of the window system only.
- **P8 (CRITICAL FIELD SIZE).** There is a threshold `log2 q_crit` below
  which the scale-`M_max` descent class beats the `0.68 n^2` budget in
  first moment. Predicted: `q_crit` is a 3-digit bit-count, well below
  the pin `q >= 2^250` but NOT below `q >= n` — i.e. the `q`-pin is
  LOAD-BEARING for SL-2 and must be carried in the residual.

## 2. Falsifiers (F1-F8), F1 as assigned

- **F1 [THE ASSIGNED FALSIFIER].** An unstructured admissible family
  (core complements not coset unions at any scale `M | gcd(n,k)`) at a
  band-proper depth with `> 0.68 n^2` members. **PREDICT: NOT FIRED by
  this pilot** — SL-3 sub-criticality means no toy fixture can exhibit
  the blow-up; a positive answer needs a construction, route (3).
  Recording in advance: if route (3) succeeds, SL-2 is answered
  affirmatively and the occupancy lemma DIES at the prize rows.
- **F2 [the catch].** A coset family at a scale `M < d` with `M | d`
  landing INSIDE the band proper at a prize row. **PREDICT: FIRES**
  (`M = (h-1)/4`, `d = 3(h-1)/4`) — a scope gap in "the structured half
  is PROVED excluded".
- **F3.** P3's descent bijection fails (a scale-`M` core with no quotient
  counterpart, or vice versa). **PREDICT: NEVER.**
- **F4.** The scale-`M` first-moment count EXCEEDS the `0.68 n^2` budget
  at some row at the pinned field `q >= 2^250`. **PREDICT: NEVER** — but
  predict the surviving gap is under 2x in the exponent (tight).
- **F5.** LEMMA W or the MC-1 specialization mismatches on a toy.
  **PREDICT: NEVER.**
- **F6.** A scale-`M` family whose off-class equations vanish WITHOUT the
  syndrome window being `M`-quotient-periodic. **PREDICT: NEVER**
  (equivalence, P6).
- **F7 [h-even control].** At an `h`-even row the band proper contains a
  power of two, so the `M >= d` (BP(1)) class also fires, in ADDITION to
  the sub-depth class. **PREDICT: FIRES** at `h` even — the parity
  protection is lost twice over, and this pilot's descent finding is the
  strictly larger loss.
- **F8.** The quotient instance at `M = M_max` lands at a quotient depth
  that is band-proper for the quotient (so the occupancy lemma at the
  quotient row would close it by induction). **PREDICT: does NOT fire —
  it lands at the quotient's CASCADE tier `d' = h'-1`** (`h' =
  floor(h/M)`), i.e. in the one tier the banked theory explicitly does
  NOT protect. If F8 instead does not fire in the other direction (i.e.
  `d'` IS band-proper), SL-2's structured-descent half closes by
  self-reduction and this pilot's verdict upgrades.

## 3. What each outcome means

| outcome | verdict |
|---|---|
| F1 fires (construction) | SL-2 AFFIRMATIVE; occupancy lemma dead at the prize rows |
| F2 fires, F4 does not | PARTIAL: the structured half needs re-proving at sub-depth scales; first moment survives with a collapsed margin; residual = the aperiodic case |
| F2 and F4 both fire | the structured half is REFUTED at the prize rows (subject to realizability), a major flag |
| F2 does not fire | BP(1)'s exclusion is complete as stated; residual is the aperiodic case alone |
| F8 fires | structured-descent half closes by induction on the quotient row |

## 4. Compute discipline

Every run `tools/ramguard {tiny,local} -- python3 ...` from the repo
root, literal `--`. No network, no Modal. Nothing outside
`notes/pilots_20260803/sl2_unstructured/` is written; every other file is
read-only. Toy fixtures test the ALGEBRA (LEMMA W, the specialization,
the descent bijection, rank additivity) — NOT the count: by SL-3
sub-criticality a toy cannot exhibit the blow-up, and no count claim will
be based on a fixture.

## 5. Subtraction notice (hard law 5), stated up front

CONSUMED, not re-derived: MC-1/MC-2/MC-3/MC-5 and the KEY LEMMA
(`xr_band_key_lemma_pencil_mass`); THEOREM 5, BP(1), BP(2), BP(3), the
`h`-even control and MC-4's scope (`xr_mc_depth_quantization`); the
e22 coset locator factorization; the six-row table and the `q`-envelope
(`listsize_program/rows.py`, `tools/prize_row_descriptor.py`);
THEOREM A/E/F and the SPECTRAL EXCLUSION (`sl1_windowed_projection`);
CORE-DISJOINTNESS and its correction (`band_heart_consolidation`).
NEW here, if the predictions hold: LEMMA W for a general word (the
Toeplitz syndrome form), the DESCENT theorem P3 with its bijection, the
scope catch P4, the margin arithmetic P5/P8, and the rank penalty P6.
