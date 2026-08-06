# PRE-REGISTRATION — the LOW-w CROSSING CORE (generative): the deep stratum and the w = 2 principal question

Round 18, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. GENERATIVE lens: prove
suppression on (part of) the uncovered low-w crossing region, or
characterize exactly what is true there.

## 0. The target (the round-17 convergent frontier)

THEOREM CS (banked, notes/pilots_20260806/es_coprimality/) proves the
(ES) crossing instance unconditionally wherever
ceil((w-1)/2)·log2 p > (n/4)·log2 r'; at 256-bit p that is every
w > w* = 2^37.3131. The UNCOVERED region is w in [2^34, ~2^37.31] —
and three blind round-17 pilots converged on its structure:
- es_g_lanes §3: the binding obstruction is the DEEPEST stratum
  a = v-1, where exactly ONE condition survives; at w = 2^34 the
  instance is n_a = 256, |Z^(a)| in {1,2}, and no admissible row
  clears the balance requirement (log2 p >= 256 = the rules cap).
- es_coprimality LEMMA STRAT + CATCH-17C: the deep exceptional
  witnesses reduce to w' = 2 PRINCIPAL instances — the reduced ideal
  is principal and non-coprimality is generic there.
- CS2 is SHARP (AM-GM equality attained), so the gap CANNOT be closed
  by sharpening the archimedean side. A different idea is required.

## 1. Source surfaces (read ALL first; quote verbatim)

- notes/pilots_20260806/es_coprimality/{REPORT.md, PROOFS.md} —
  THEOREM CS, LEMMA STRAT, LEMMA TWO (N_odd is the invariant; r'
  even forces 2 | N), the E_floor definition, the residual bad-prime
  list {3,7,17,47,97,193,257,353,449}, COROLLARY CS-TOWER.
- notes/pilots_20260806/es_g_lanes/{REPORT.md, PROOFS.md} — the
  stratum table (§3), the |Z_w| closed forms per admissible p-class,
  the 19 admissible (p-class, e) pairs, the w = 2^34 exhibit row.
- notes/pilots_20260806/es_boundary_adversary/REPORT.md — the five
  witnesses and the census method (ground truth machinery).
- critical/nodes/b1_char0_giant_coset_theorem — LEMMA Z (cited).

## 2. Pre-registered deliverables

- **(G1) THE w = 2 PRINCIPAL QUESTION, stated exactly.** At a w' = 2
  instance the ideal is (x_1), principal, and non-coprimality is
  "generic" — but the OBLIGATION is not coprimality, it is the
  original count statement transported down the stratum. State
  exactly what the crossing lane needs at the reduced instance
  (n' = n/2^a, one condition, weight r'/2^a): which S' are
  admissible members, what the structural family is there, and what
  "no accidents" means. Do NOT inherit the balance frame — it is
  provably unavailable here.
- **(G2) THE n_a = 256 INSTANCE, attacked directly.** At w = 2^34,
  the binding stratum is n_a = 256, ONE surviving condition
  (x_1' = 0 or the single closure orbit), weight r'_a = r'/2^a.
  This is small enough for exact structure: the solutions of
  p_1(S') = 0 with S' <= mu_256, |S'| = r'_a mod p — LEMMA Z
  characterizes char-0; what survives mod p is a vanishing-sum
  question at n' = 256. Enumerate/characterize EXACTLY which
  reduced-instance solutions LIFT to admissible members of the
  original crossing window system (the lift constraint is the
  un-collapsed even-index conditions — they are not free; LEMMA
  STRAT tells you which survive). The conjecture to test: the lift
  constraints kill every non-structural reduced solution — i.e. the
  deep stratum is EMPTY of accidents for a reason invisible to
  balance. Toy-verify the lift mechanism exhaustively at
  (n, n_a) = (32, 8), (64, 8), (64, 16) before claiming anything.
- **(G3) The covered/uncovered split refined.** With (G2)'s lift
  constraints priced, recompute which part of [2^34, 2^37.31]
  becomes covered by CS + stratum-emptiness. State the exact
  remaining set.
- **(G4) If the lift conjecture FAILS** (a reduced solution lifts):
  that is a constructive path toward a crossing accident — follow it
  UP: does it lift all the way to a genuine accident at a scaled
  row? That would be a campaign-critical catch on the crossing lane
  (report witness + reproduction script, stop).

## 3. Pre-registered falsifiers / honesty clauses

- The toy lift-mechanism verification is a GATE: no claim about the
  prize rows unless the mechanism is exhaustively correct at all
  three toy shapes.
- If the deep stratum is empty for balance-invisible reasons, the
  proof must not smuggle balance back in — self-check the argument
  against the es_g_lanes verdict that no admissible row clears it.
- AK-UNIT check as in round 17: no congruence conclusions about
  counts.

## 4. Rules of engagement

- DRAFT ONLY: write only inside notes/pilots_20260806/crossing_low_w/.
  Never edit dag.json, node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/efloor_sparsity/ (sibling this round).
- COMPUTE LAW: never bare python3 — tools/ramguard tiny|local --
  python3 ..., literal --, from repo root
  /home/u2470931/smooth-read-solomin/prize. This includes file
  patching and JSON peeking (three round-17 pilots breached exactly
  there; use Edit-style heredocs under ramguard).
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report;
  the coordinator persists it verbatim.
