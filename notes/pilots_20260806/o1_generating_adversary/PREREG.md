# PRE-REGISTRATION — (O1) ADVERSARY on GENERATING rows: is the surviving F2 claim true at zero margin?

Round 18, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. ADVERSARIAL lens: round 17
proved (O1) FALSE on non-generating admissible rows; the surviving
claim lives exclusively on generating rows (k = ord_n(p) = e), where
LEMMA 3 is EXACTLY SATURATED (margin 1.000). Your mandate: try to
break (O1) there too. A refutation on generating rows would make
mystery 2 false as posed regardless of the pending scope answer —
decisive either way for the Przemek note.

## 0. The state of record (sources; quote verbatim)

- notes/pilots_20260806/f2_adm/{REPORT.md, PROOFS.md} — THEOREM
  ADM-B (ratio = k/e nested / max(2,k)/e new-part, exact and
  scale-free; k = e => LEMMA 3 degenerates to Corollary 1.1's
  unconditional floor "and certifies nothing"), LEMMAS ADM-1/2/3,
  the exact dim L, the ladder at the witness row
  (p = 18446735827372343297, q = p^4, k = e = 4), the K1
  cancellation shortfall numbers, CATCH-6 (the coset domain).
- notes/pilots_20260804/f2_opening/PROOFS.md — (O1) as stated,
  LEMMA 3's derivation, what "certify" means in the chain.
- notes/pilots_20260804/f2_sl1_powersums/PROOFS.md — Z(L), the mass
  bounds, the random-subspace baseline.
- notes/pilots_20260806/t_naming/REPORT.md — the two live values of
  the Lambda parity convention (CATCH-E); your attack must state
  which reading each step uses and hold under BOTH or say which one
  it needs.

## 1. Pre-registered attack lines (run in this order; verdict each)

- **(V1) THE ZERO-MARGIN ATTACK.** At k = e the necessary condition
  holds with equality. Equality means ANY strict loss anywhere in
  the chain (a positive-entropy defect, a constant > 1, an o(n) that
  is really Theta(n)) kills (O1). Inventory the chain's steps on a
  generating row and hunt for one strict loss. Each candidate loss
  must be verified exact (is it truly lossless?) or exhibited as
  strictly lossy with the size of the loss.
- **(V2) THE COSET ATTACK.** f2_adm CATCH-6: the rules-level domain
  is a coset g·mu_n and the antipodal law fails off-subgroup. Does
  (O1) on the COSET domain lose a constant at generating rows? If
  the coset costs anything at zero margin, (O1) is false on the
  rules-level object even where it holds on the subgroup.
- **(V3) THE Z_1 LOWER-BOUND ATTACK.** (O1) at the moving rungs
  equals SL-1b' (Z_1 ternary mass of the explicit GRS code). Attack
  from below: construct ternary relations — CHECK FIRST whether the
  DLI stronger sibling applies: f2_sl1b found
  dli_wcl_newton_short_window_exclusion proves SL-1 STRONGER
  (wt >= 2R+1) under char > w, which FAILED on the KoalaBear tower
  (p ~ 2^31 < w) but on admissible rows p >= 2^39 (p ~ 2^64 at
  prize-max) — the hypothesis may now HOLD for the relevant weight
  range. If it applies, it CONSTRAINS your attack (and is a
  generative gift: cite it exactly, with the 6 counterexamples
  showing char > w is necessary). Then: does a ternary kernel
  element of weight in [2R+1, S] exist by counting/structure? An
  explicit family with Z_1 >= 2^{c·m} for any c > 0 refutes (O1) at
  zero margin.
- **(V4) THE EMPTY-CLASS SWEEP.** f2_adm CATCH-4 found one vacuous
  admissibility class. Enumerate ALL generating admissible classes
  (k = e, each e in {1,2,3,4,6} with v_2(e) <= 2 — note e = 3, 6
  need ord odd parts; derive exactly which (e_p, e) are generating
  AND non-empty, with a prime witness or a proof of emptiness each).
  If generating rows are EMPTY at prize-max (n = 2^41), (O1)'s
  surviving scope is vacuous — check this FIRST, it would decide
  everything (f2_adm's witness has k = e = 4, so at least one class
  is non-empty; verify its primality yourself, do not inherit).

## 2. Pre-registered falsifiers / honesty clauses

- Attacks that fail must be reported as SURVIVED-with-margin (state
  what the attack needed and by how much it missed), never silently
  dropped. The surviving minimal form of (O1) after all four attacks
  is the deliverable if no attack lands.
- Any successful attack needs a self-contained ramguard-tiny
  reproduction script and an exact statement of which (O1) reading
  (Lambda parity, window reading, coset vs subgroup) it kills.
- No attack may consume the t-naming identification (refuted); use
  the interval and both parity readings.

## 3. Rules of engagement

- DRAFT ONLY: write only inside
  notes/pilots_20260806/o1_generating_adversary/. Never edit
  dag.json, node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/z1_ternary_mass/ (sibling this round —
  it works the same object generatively; independence required).
- COMPUTE LAW: never bare python3 — tools/ramguard tiny|local --
  python3 ..., literal --, from repo root
  /home/u2470931/smooth-read-solomin/prize. Includes file patching
  and JSON peeking (three round-17 pilots breached exactly there).
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.

---

# APPENDIX (pilot's own pre-registrations, appended BEFORE any computation)

Opus 5, round 18, 2026-08-06. Registered after reading only:
`f2_adm/{REPORT,PROOFS}.md`, `f2_opening/{REPORT,PROOFS}.md`,
`f2_sl1_powersums/PROOFS.md`, `f2_sl1b/REPORT.md`, `t_naming/REPORT.md`,
`f2_tq_pin/PROOFS.md:100-215`,
`background/nodes/dli_wcl_newton_short_window_exclusion/{statement,proof}.md`.
No computation of any kind has been run. `z1_ternary_mass/` NOT read.

## Naming used below

- **reading A** (`f2_adm`'s, `t_naming`'s 5-to-1 favourite): `t` is the
  largest Newton index, the full condition set is `Lambda_full = {1..t}`,
  and the K1 sector is its ODD part, `R := |Lambda_K1| = ceil(t/2)`.
- **reading B** (the one `t_naming` CATCH-E refutes 5-to-1 but leaves
  live): `R := |Lambda_K1| = t`.
- `Delta := dim_{F_p} L * log2 p - m` (bits). LEMMA 3 holds iff
  `Delta >= -o(n)`; `(O1)` is FALSE by `2^{-Delta}` when `Delta < 0` and
  `-Delta = Theta(n)`.

## A1 (V4, run first). Generating admissible classes: exactly three, all non-empty.

`ord_{2^41}(p)` lies in the 2-group `(Z/2^41)^*`, so `k` is ALWAYS a
2-power. Hence `k = e` forces `e in {1,2,4}` and `e in {3,5,6}` can NEVER
generate. Predicted census: `(e_p,e,k) in {(>=41,1,1),(40,2,2),(39,4,4)}`,
each NON-EMPTY. **Falsifier:** any generating class with `e` not a power
of 2, or any of the three classes empty. I predict the vacuity attack
FAILS and (O1)'s surviving scope is non-vacuous.

## A2 (V1). The zero-margin premise is TOO STRONG as briefed.

`(O1)`'s target carries `+o(n)`, so a multiplicative loss of `2^{O(1)}`
or `2^{o(n)}` does NOT kill it at zero margin; only a `Theta(n)` loss in
the EXPONENT does. I predict the brief's "a constant > 1 kills it" is
wrong and I will report it as a catch against the brief.

## A3 (V1). Integer/ceiling effects are O(L) and cannot kill.

With `t` at the (C)-threshold, `Delta` is an O(L) residue of the
irrationality of `n/L`. Prediction: `|Delta| <= L/2 <= 128` bits over the
whole non-vacuous regime, sign possibly either way, at the banked witness
`Delta > 0` (LEMMA 3 HOLDS). **Falsifier:** `|Delta| > L` at any
generating class, or `Delta < -Theta(n)` from rounding alone.

## A4 (V1, the real attack). The ensemble dichotomy is a Theta(n) loss.

`(C)` calibrates `t` against entropy `n` (ALL subsets, `2^n`); the exact
FM+gate `(T*)` calibrates it against the fixed-size slice
`log2 C(n, n-k-t) + 128`. LEMMA 3's requirement is calibrated to
`m = n/2` and is ensemble-free. Prediction: at generating rows under
reading A the two calibrations differ by exactly
`n - t*L = 2n/(L^2 ln 2) + O(log n)`, so
`Delta = -n/(L^2 ln 2) = -Theta(n)` — i.e. **(O1) is FALSE under the
slice calibration** by at least `2^{n/45426} = 2^{4.84e7}` at `L -> 256`
and up to `2^{n/1165} = 2^{1.89e9}` at `L = 41`. I further predict the
relative gap equals `f2_tq_pin`'s banked `0.0044%` EXACTLY, i.e. the
number the campaign has been reading as "agreement" is, at zero margin,
the sign of `(O1)`. **Falsifier:** `n - t*L` is `O(polylog n)`, or the
relative gap is not `2/(L^2 ln 2)`, or `Delta >= 0` under the slice
calibration. **Reading dependence, registered in advance:** under reading
B this attack must FAIL (predicted `Delta = +n/2 - Theta(n) > 0`); if it
also fires under reading B I have made an error.

## A5 (V1). Structural resolution of CATCH-E, registered as a prediction.

The K1/K2/G parity TRICHOTOMY presupposes an ambient condition set
containing both parities; therefore reading A is forced internally, not
merely by source-count. Prediction: no F2 file defines K2 or G in a way
compatible with reading B. **Falsifier:** a source in which `Lambda_full`
is odd-only and K2/G are still non-empty.

## A6 (V2). The coset costs EXACTLY nothing for (O1).

Prediction: `phi_g : (C_l) -> (g^l C_l)` is a bijection of `K1(Lambda)`
with `chi_{phi_g(c)}(x) = chi_c(gx)`, hence
`E_{c in K1}[T_{gW}] = E_{c in K1}[T_W]` EXACTLY (not up to constants),
and `L`, `dim L`, `Z(L)`, min ternary weight are literally the same
objects. Consequence predicted: `f2_adm` CATCH-6's gap is confined to the
parity/descent machinery, which LEMMA 5 already proved is the wrong
functional for (O1). Second prediction: the coset does NOT rescue `k < e`
rows (so `f2_adm` CATCH-1 is coset-robust) even though
`F_p(g mu_n)` can equal `F_q` when `F_p(mu_n)` does not. **Falsifier:**
any toy coset row on which `dim L`, `Z`, or the K1 average differs.

## A7 (V3, checked FIRST as mandated). The DLI stronger law APPLIES on admissible rows.

Prediction: on EVERY admissible row `p >= 3*2^{e_p} > 2^40 >= m >= w`,
because `c = 1` would need `2^{e_p}+1` prime with `39 <= e_p < 256`,
i.e. a Fermat prime `F_6` or `F_7`, both composite. Hence
`char > w` HOLDS and `dli_wcl_newton_short_window_exclusion` gives
`wt >= 2R+1`, twice SL-1's `R+1`. This is the first row in the campaign
where the banked node applies. **Falsifier:** an admissible row with
`p <= m`.

## A8 (V3). The gift halves the (M3) shortfall but does not close it.

With distance `d`, (M2)/(M3) give `Z < 2` iff `d > 0.61315(S+1)`.
Predicted: at generating rows `R/S = 1/log2 p` EXACTLY, so SL-1 needs
`log2 p < 1.63` and DLI needs `log2 p < 3.26`; admissible `log2 p >= 39`
misses by `>= 23.9x` / `>= 11.96x` respectively. **Falsifier:**
`R/S != 1/log2 p`, or (M3) closes on some admissible generating row.

## A9 (V3). The attack from below fails, and I register WHY in advance.

To force `Z_1 >= 2` with all weights `>= 2R+1` one needs at least
`2^{2R+1}` distinct nonzero ternary codewords. The code is NEGACYCLIC, so
its ternary set carries a symmetry group of order `4S` (shift x sign)
— predicted `4S = 2^{e_p+1} <= 2^42`, short of `2^{2R+1} = 2^{2^33+1}` by
an astronomical factor. Prediction: no orbit/symmetry construction can
refute (O1) at generating rows, and the random-subspace baseline predicts
`Z_1 ~ 2` and `Z(L) = Z_1^C <= 2^C <= 16`, i.e. (O1) TRUE with
`o(n) <= 4` bits. **Falsifier:** an explicit ternary kernel element at
prize scale, or a symmetry group of the code of size `2^{Omega(S)}`.

## A10 (V1/V3 interaction). Heuristic min ternary weight vs the DLI bound.

Predicted heuristic minimum ternary weight `gamma* S` with
`H(gamma*) + gamma* = 1`, `gamma* ~ 0.227`, versus `2R+1 = 2S/log2 p`
`~ 0.031 S` at prize-max — so at ADMISSIBLE scale DLI is ~7x BELOW the
heuristic true minimum (the opposite of the toy scale of
`f2_sl1_powersums` S13, where `2R+1` is attained). **Falsifier:** the two
orders coincide at prize scale.

## A11 (scope). What I will NOT claim.

I will not claim any bound on `Z_1`; I will not choose between the two
`Lambda`-parity readings or between the two ensemble calibrations; I will
not propose a status flip. Every verdict is reported per reading.
