# PRE-REGISTRATION — Z_1 TERNARY MASS (generative): attack SL-1b' on the explicit admissible object

Round 18, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. GENERATIVE lens: SL-1b' is
mystery 2's one honest mathematical terminal, and round 17 made it
fully explicit for the first time. Prove what can be proved.

## 0. The object (verbatim, f2_adm REPORT D4)

> SL-1b′ survives as THE terminal and is now **explicit**: bound the
> ternary mass of a `[2^38, 2^38 − R, R+1]_p` GRS code whose
> evaluation points are the half-system of `μ_{2^39} ≤ F_p^*`, with
> `R = 4.295e9`, `p ≈ 2^64`, and `Z(L) = Z_1^C`, `C ≤ 4` — a
> prime-field, MDS, single-class question.

Target: Z_1 <= 2^{o(m)} (equivalently L^perp ∩ T = {0} or nearly),
where T = ternary vectors ({0,±1}) and the dual is the GRS kernel.

## 1. Source surfaces (read ALL first; quote verbatim)

- notes/pilots_20260806/f2_adm/{REPORT.md, PROOFS.md} — LEMMA ADM-2
  (the direct-sum structure, exact dim L, Z(L) = Z_1^C), the ladder,
  the witness row (p = 18446735827372343297).
- notes/pilots_20260804/f2_sl1_powersums/PROOFS.md — THEOREM SL-1
  (wt >= ceil(t/2)+1 characteristic-free), the Z(L) mass framework,
  the random-subspace baseline (E[Z] heuristics), SL-1b's original
  posing and the (R-A)/(R-B) split.
- notes/pilots_20260806/f2_sl1b/{REPORT.md, PROOFS.md} — LEMMA
  SL-1b-DIM, the 61 witnesses (what ternary-mass FAILURE looks like
  at small scale), and THE HOT LEAD:
  **dli_wcl_newton_short_window_exclusion proves SL-1 STRONGER
  (wt >= 2R+1) under char > w — which failed on the KoalaBear tower
  (p ~ 2^31 < w up to 2^38) but on the admissible object p ~ 2^64
  while ternary weights are <= S = 2^38 < 2^64: CHECK WHETHER THE
  HYPOTHESIS NOW HOLDS.** If it does, the stronger distance law
  applies to the admissible object and the F2<->DLI crosswalk pays
  its first real dividend. Quote the DLI node's exact statement and
  hypothesis; also carry f2_sl1b's 6 counterexamples showing
  char > w is NECESSARY (scope honesty).
- critical/nodes/dli_wcl_newton_short_window_exclusion — the node
  itself (statement + proof), and the DLI lane's Z-mass instruments
  (the norm sandwich node
  background/nodes/dli_c1_ternary_relation_norm_sandwich, the
  weight3/weight4 ambient exclusions) — the DLI lane has spent
  months on ternary relations; SUBTRACT before proving anything.

## 2. Pre-registered deliverables

- **(Z1) The crosswalk check** (do this FIRST): does the DLI
  stronger law (wt >= 2R+1 under char > w) apply to the admissible
  GRS object? State the exact hypothesis match/mismatch. If it
  applies: the minimum ternary weight jumps from ceil(t/2)+1 to
  2R+1 ~ 8.6e9 — bank the transported theorem with full citation.
- **(Z2) The mass bound attempt.** With the best available distance
  floor (SL-1 or the transported 2R+1), bound Z_1: the number of
  ternary vectors of weight >= (floor) in the dual. Routes to try in
  order: (a) the DLI norm-sandwich (Parseval/AM-GM ceilings on
  ternary relations — already banked machinery; does it transport
  to the half-system evaluation points?); (b) second-moment /
  Weil-type sums over the GRS dual (the dual of GRS is GRS — use
  the explicit dual parametrization: Z_1 counts ternary-valued
  points of an explicit polynomial image; c) the C <= 4 class
  structure (Z = Z_1^C means any bound on Z_1 powers up — and
  conversely the factorization localizes the problem).
- **(Z3) Calibration at reachable scale.** Exhaustive Z_1 for GRS
  codes on half-systems at small (p', m') matching the shape
  (p' ≡ 1 mod 2^{e'}, evaluation on the half-system): measure the
  true decay law, compare with the random-subspace prediction and
  with the 61-witness failure modes. Pre-register the grid.
- **(Z4) The conditional of record.** Whatever is proved: state
  exactly what Z_1 bound results, what (O1)/mystery-2 consequence it
  has at the moving rungs (cite f2_adm's shortfall arithmetic), and
  what remains.

## 3. Pre-registered falsifiers / honesty clauses

- If (Z1)'s hypothesis match fails (e.g. the DLI law needs the
  window structure, not just char > w), report the exact mismatch —
  do not transport on vibes.
- The 61 f2_sl1b witnesses live at p <= 19; any claimed mass bound
  must be consistent with them (they satisfied the dimension
  threshold and still carried ternary vectors — your bound must
  either exclude their parameter regime explicitly or bound their
  mass, not deny their existence).
- Subtraction (hard law 5): the DLI ternary instruments are banked —
  novelty claims only for what genuinely transports or is new.

## 4. Rules of engagement

- DRAFT ONLY: write only inside
  notes/pilots_20260806/z1_ternary_mass/. Never edit dag.json, node
  shards, tools/, or push. Do NOT read
  notes/pilots_20260806/o1_generating_adversary/ (sibling — it
  attacks the same object adversarially; independence required).
- COMPUTE LAW: never bare python3 — tools/ramguard tiny|local --
  python3 ..., literal --, from repo root
  /home/u2470931/smooth-read-solomin/prize. Includes file patching
  and JSON peeking (three round-17 pilots breached exactly there).
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.

---

# APPENDIX — PILOT'S OWN PRE-REGISTRATIONS (Opus 5, 2026-08-06)

Appended BEFORE any computation. Sources read first: the coordinator
brief above; `f2_adm/{REPORT,PROOFS}.md`; `f2_sl1b/{REPORT,PROOFS}.md`;
`f2_sl1_powersums/PROOFS.md`;
`background/nodes/dli_wcl_newton_short_window_exclusion/{statement,proof}.md`;
`background/nodes/dli_c1_ternary_relation_norm_sandwich/statement.md`;
plus a five-surface subtraction sweep (`critical/`, `background/`,
`notes/`, `archive/`, `experiments/`+`dag.json`+`upstream_dag/`+`formal/`)
run before any claim. `o1_generating_adversary/` NOT read.

## Object of record (from LEMMA ADM-2 / COROLLARY ADM-2.2)

`S = 2^38`, `R = ceil(t/2) = 4,294,967,340`, `p = 18446735827372343297`,
`m = C·S`, `dim L = C·min(S,R) = C·R`, `C <= 4`,
`Z(L) = Z_1^C`, and (`f2_sl1b/PROOFS.md:571` via `f2_adm/PROOFS.md:465`)
`Z(L) = sum_{eps in L^perp ∩ T} 2^{-wt(eps)}` — a WEIGHTED mass, not a
count. I register that distinction as load-bearing before using it.

## Registrations

- **Z-A1 (crosswalk).** The DLI hypotheses match the admissible object
  under the shift-0 reading `Lambda ⊇ {1,3,...,2R-1}`: char
  `p = 1.845e19 > w` for every `w <= S = 2.749e11` (margin 6.7e7);
  `omega` of exact order `2N = 2^39` in `F_p^*` (`e_p = 39`); exponents
  `e_i in {0..N-1}`, `N = 2^38 = S`. PREDICT: hypothesis HOLDS and the
  transported floor is min ternary weight `>= 2R+1 = 8,589,934,681`.
- **Z-A2 (the shift is load-bearing).** PREDICT the `2R+1` law FAILS for
  shifted runs (`a >= 1`) even under char `> w`, and that f2_sl1b's own
  smallest witness (`p=7, n=12, Lambda={5,7}`, min ternary wt 3 < 5`) is
  such a failure with char `7 > w = 3`. The transport is therefore valid
  only because the official `Lambda` starts at `l = 1`.
- **Z-A3 (l1 extension of the DLI theorem).** PREDICT the Newton proof
  extends verbatim to INTEGER coefficients with `w := sum_i |c_i|` (the
  l1 weight) in place of the support size, under char `> w`. Consequence:
  distinct ternary codewords satisfy `||c - c'||_1 >= 2R+1`.
- **Z-A4 (the unconditional mass floor).** PREDICT `Z(L) >= 2^m/p^{dim L}`
  for EVERY `F_p`-subspace `L ⊆ F_p^m` (no MDS, no GRS, no randomness),
  via the banked collision identity + Cauchy-Schwarz; and that this is
  exactly the non-negativity of the banked fibre-variance identity, hence
  NOT new as an identity — new only as an inequality drawn and transported.
- **Z-A5 (three-way seam).** PREDICT floor-vacuity, LEMMA 3, and the
  counting balance (C) `tL >= n` are the SAME inequality, with
  `ratio = dim L·log2 p/m = (k/e)·(tL/n)`.
- **Z-A6 (the dichotomy).** PREDICT `Z(L) >= 2^{m(1 - (k/e)(tL/n))}`, so at
  `k < e` with `tL = n`, `Z >= 2^{m(1-k/e)} = 2^{Θ(n)}` and (O1) is FALSE
  at the level of the OBJECT, not merely of a necessary condition. PREDICT
  this reproduces f2_adm CATCH-1's `2^{5n/12}` EXACTLY at `(k,e) = (1,6)`
  nested — a cross-check between two independent routes.
- **Z-A7 (the knife edge at k = e).** PREDICT `R·log2 p - S ∈ (0, log2 p)`
  at the witness — the floor is vacuous by fewer than 64 bits out of
  2.75e11 (relative margin < 2.4e-10). Registered point estimate: **46 bits**.
- **Z-A8 (the brief's own equivalence is false).** PREDICT `Z_1 <= 2^{o(m)}`
  and `L^perp ∩ T = {0}` are NOT equivalent here: the first is
  heuristically TRUE (`Z_1 ≈ 1 + 2^{-46}`), the second heuristically FALSE
  by `≈ (3/2)^S = 2^{0.585·2^38}`. Registered as a catch against §0 of this
  brief and against `f2_sl1b/REPORT.md:62`.
- **Z-A9 (route (a) is dead).** PREDICT the DLI norm sandwich yields only
  `w >= p^{2R/n_class} = p^{1/64} = 2` at the admissible object — dominated
  by the transported `2R+1` by a factor `4.29e9`.
- **Z-A10 (the discharge ladder).** PREDICT the (M3)-type criterion improves
  from `R/S > 0.61315` (banked) to `0.44210` (with the `2R+1` floor) to
  `≈ 0.2565` (with l1 sphere-packing), against a FORCED `R/S = 1/log2 p =
  0.015625`: shortfalls `39.2x`, `28.3x`, `16.4x`.
- **Z-A11 (structural no-go).** PREDICT that because saturation pins
  `R/S = 1/log2 p`, NO bound in the "min-distance + counting" family can
  discharge SL-1b' at any admissible row with `log2 p > ~3.9` (`p >= 17`).
- **Z-A12 (calibration grid, fixed now).** `2N ∈ {8,16,32}` so
  `N = S ∈ {4,8,16}`; primes `p ≡ 1 mod 2N`, `p < 1000`; `R ∈ 1..min(6,N)`;
  shifts `a ∈ {0,1,2}`; evaluation on the FULL half-system (and, as a
  control, proper sub-windows). Exhaustive over `3^N` for `N <= 8`;
  meet-in-the-middle over two halves for `N = 16`. Measured per row: exact
  weighted `Z_1`, exact count `|T ∩ ker|`, exact min ternary weight, exact
  `dim ker`. Compared against: the floor `2^N/p^R`; the random-subspace
  first moment `1 + (2^N-1)(p^{N-d}-1)/(p^N-1)`; the count prediction
  `3^N/p^R`; the transported `2R+1` at `a = 0` and its failure at `a > 0`;
  the l1-packing bound. PREDICT: 0 violations of the floor; at saturation
  (`R log2 p ≈ N`) the measured `Z_1` is within a small constant factor of
  the floor; the count tracks `3^N/p^R` where that exceeds 1.
- **Z-A13 (falsifier, pre-registered).** If measured `Z_1` at saturation
  systematically EXCEEDS the random-subspace prediction by a factor growing
  with `N`, that is evidence AGAINST (O1) at `k = e` and I will report it as
  the headline regardless of how it reads for the lane. Conversely, if the
  GRS half-system code is systematically BELOW the random prediction, I will
  report that as the first positive evidence for SL-1b'.
- **Z-A14 (consistency with the 61 witnesses).** Any bound I state must be
  checked against f2_sl1b's 61 `(R-A)`-satisfying ternary-carrying
  configurations. PREDICT my floor is consistent with them (it is a LOWER
  bound, so it cannot deny their existence) and that my upper bounds are not
  violated by any of them.
