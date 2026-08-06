# FABLE_AUDIT — es_coprimality (round 17, pilot 4 of 4)

**Auditor:** Fable, 2026-08-06. **Verdict: BANKED — THEOREM CS is the
campaign's first UNCONDITIONAL positive coverage of the (ES) crossing
terminal: at 256-bit characteristic it proves the instance outright on
71.16% of the crossing bracket (every w > 2^37.3131, including 2 of
the 6 power-of-two w), by an ideal-level Galois-multiplicity squeeze
(p^{|Z_w^odd|} | N(x_1) vs a SHARP AM-GM ceiling). The exceptional
class is exactly characterized (E_strat via LEMMA STRAT + E_floor),
contains all five round-16 witnesses with exponents matching on the
nose, and only E_floor SPARSITY remains conjectural.**

Replay (coordinator, under ramguard): self 65,613/0; floor/strat/wit
clean; failclosed exits 1 as designed (fail-closure proven, not
asserted); the rate stage's persisted output shows 21,282/0 at the
crossing shape (a fresh full-grid re-run subsequently COMPLETED in a
background replay, exit 0 — the live-replay chain is now complete
across all stages). Anchors verified by the
coordinator directly, verbatim-exact: the collapse identity
(archive/compressed_dli_lane_20260705/pcf_evaluation_flatness/statement.md:8-12)
and the pair-coprimality open lemma
(critical/nodes/u1_x4_direct_column_budget/notes/F3_SHALLOW_LADDER.md:200-202).

ADOPTED:
- **THEOREM CS** (novelty correctly scoped: the delta -> |Z_w^odd|
  multiplicity upgrade over round-16's banked M3 — one prime vs the
  full odd-closure orbit), **LEMMA STRAT** (exact stratum reduction),
  **LEMMA TWO** (r' even forces 2 | N(I_S) — so N_odd is the
  invariant of record; the naive conjecture is FALSE at every prize
  row, caught by the pilot against its own K1 draft), **COROLLARY
  CS-TOWER** (margins widen with stratum depth). CS2 SHARP (AM-GM
  equality attained at an explicit fixture) — the uncovered region
  CANNOT be closed by sharpening the archimedean side; the low-w gap
  needs a genuinely different idea.
- **The unconditional coverage statement of record**: the (ES)
  crossing instance HOLDS wherever ceil((w-1)/2)·log2 p >
  (n/4)·log2 r'. COORDINATOR SCOPE NOTE (consistent with the
  es_g_lanes bank): the crossing obligation quantifies over ALL
  admissible rows, and the threshold scales with log2 p — at the
  small-characteristic end of admissibility the covered fraction
  shrinks (39.57% at 128 bits). The discharge region is the exact
  (p, w) set above; NO STATUS FLIP — banked as strong partial
  coverage, mint-shaped.
- The measured rate table (monotone in w; crossing shape exactly
  1.00000 over all characteristics) and the closure of round-16's
  declared r' = 7 coverage gap (CATCH-17E).

CATCHES ACCEPTED:
- CATCH-17A (LEMMA TWO / N_odd) — load-bearing self-catch.
- **CATCH-17B**: "generically coprime" was NEVER banked mathematics
  (a CONDITIONAL node's empirical credit + a class-number-1-confounded
  toy); the repo itself had already named pair-coprimality as THE one
  open lemma with two consumers (u2c, u1_x4). CC-sparsity is hereby
  identified as the SHARPENED FORM of that existing open lemma —
  continuity, not a new obligation. Round-16's C4-c wording corrected
  in the ledger.
- CATCH-17C: the round-16 deep witnesses are w' = 2 PRINCIPAL
  instances in disguise — TRIANGULATES with the blind es_g_lanes
  sibling's independent finding that the binding stratum carries ONE
  surviving condition. Three pilots now agree: THE crossing hard core
  is the w = 2 / small-window principal-ideal regime.
- CATCH-17D: C4-c's gcd-of-norms mechanism was the wrong diagnosis
  (the proved collapse identity makes all odd-index norms equal);
  the true mechanism is ideal-level Galois multiplicity.

CROSS-PILOT CONVERGENCE (blind siblings, round 17): CS's uncovered
low-w region [2^34, 2^37.31] coincides with es_g_lanes' balance-
broken crossing regime {2^34..2^36} + the 2^37 boundary — two
independent lanes drew THE SAME frontier line. The named obligation
after this round: the LOW-w CROSSING CORE (w in [2^34, ~2^37.31]),
attackable at the n_a = 256 one-condition stratum instance and the
w = 2 principal-ideal question, plus E_floor sparsity (= the
pair-coprimality open lemma).

HONEST RESIDUALS accepted as stated (w = 3 NOT closed — CS
degenerates to M3 there and the 0.99 measured collapse is
unexplained; E_floor sparsity measured not proved; band rows outside
CS's hypotheses; toys validate machinery only). AK-UNIT self-check
verified structurally sound (norm of an individual S, never a count
congruence). Two bare-python3 breaches self-reported (the recurring
text-edit pattern) — accepted with disclosure. DRAFT-ONLY confirmed;
sibling dir never opened.

## ADDENDUM (2026-08-06, coordinator, from round-18 efloor_sparsity)

1. **CATCH E-1**: the (K5) conditional is RE-LABELLED — given THEOREM
   CS, E_floor = {N_odd > 1} exactly on strat = 0, so the
   E = E_strat u E_floor decomposition is a restatement and
   CC-sparsity is precisely as hard as the pair-coprimality lemma it
   sharpens. THEOREM CS and the unconditional 71.16% coverage are
   untouched.
2. **CATCH E-2**: CC-sparsity is structurally (ES) again — ternary
   vectors in a p-ary cyclic code at half length. Do not route the
   remaining 28.84% through CC-sparsity as if it were smaller.
3. Progress on it anyway: SP-COVER/SP-UNIFORM close the small-prime
   end (p <= sqrt(w+1)) unconditionally; the F1 densest-family attack
   fails; the range is two-sided with CS-EXCL. See
   notes/pilots_20260806/efloor_sparsity/.
