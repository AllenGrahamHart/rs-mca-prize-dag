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
