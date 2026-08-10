# FABLE_AUDIT — b_sparsity_pose (round 26)

Coordinator: Fable. Date: 2026-08-09. Pilot: Opus (task ad5f97df6688e10b3,
~38 min, 64 tool uses). Quarantine marker: ledger line 3872, observed.

## Verdict

**BANKED. The ratified (b) narrowing is executed beyond the brief: at
the prize cell it is a THEOREM (density <= 2^-93.93 elementary,
<= 2^-106.93 with the exact orbit count, v_2-uniform to VSPARSE =
113.93), not a conjecture — built from four banked ingredients plus a
zero-margin pigeonhole, with the union-bound route honestly subtracted
as in-repo prior art. The three teeth are the real finding: (b) has no
valid asymptotic parameter (numeric per-cell re-scope SURFACED), (a)
and (b) are complementary rather than primary/fallback (the deployed
stratum is exactly where the theorem is vacuous and the certificates
work), and the node's status ruling has no slot for a density theorem
(amendment SURFACED). Both named gaps from round 25 are discharged:
LAW 2 general-w is closed (linear digit law with computed tables), and
the box-depth gap moves 2^17 -> 2^40 with no structure.**

## Replays (all by me, under ramguard)

| what | result |
|---|---|
| d1_burnside.py | exact orbit count **2^135.6034** (excess over 5^h/8192: +0.0000 bits); h=8 anchor 3676.8 >= 1450 |
| d1_prize.py | ALL theorem numbers: -93.93 / -106.93, VSPARSE 113.93, the N'-collapse table (N'=256 **+42.7 VACUOUS**), the E-S_p heuristic reproduction |
| d1_toy.py (h=8 exhaustive) | CLASSES 1450, 554/536 divisors, LEM-1/LEM-2 **0 violations**, PI 9407, BADCOUNT 73, BADDENS 0.00776 |
| d2_law2.py | P1 homomorphism 0 violations (h=4..32); P2 general-w law 0 violations (h=4..64); P2' 0 violations |
| d2_digits.py | linear digit law **0/200 at every h**; c_k tables reproduced |
| d3_depth.py analyse (banked bins) | depth table exact: D=23 FULL 65536, D=40 1048512 (z=-0.0), D=44 as reported |
| d4_checks.py | LEM-1 h=64 0/4000; the consumer sub-family pricing incl. both VACUOUS flags (+61.51, +62.50); consistency headroom 3.60 bits |

Hand-verified by me: the zero-margin pigeonhole logic (strict
inequality does all the work — p1,p2 > 2^128 forces p1p2 > 2^256 >=
Norm, covering the p^2 case); the P1 two-line proof; the P2 reduction
to round-25's LAW 2 (valid since that law is a polynomial congruence,
applicable to 2-adic v).

## Audit judgements

- **The novelty subtraction is exemplary** (hard law 5): the pilot
  found the retired in-repo proof BEFORE computing, claimed no route
  novelty, and enumerated its increments exactly. Bonus: its script
  discharges the standing catch-#61 restore item (the retired proof's
  cited-but-missing script now exists in runnable form).
- **The three teeth convert a ratified slogan into an honest
  instrument.** Tooth (ii) matters most operationally: the deployed
  Proth stratum is where (b)'s theorem is vacuous by ~62 bits — the
  ratified "(b) primary, (a) fallback" should be read as "(b) for row
  selection, (a) for assigned rows," and the pose amendment says so.
- **Two SURFACED decisions filed, neither pre-empted**: the numeric
  per-cell re-scope of (b) (the asymptotic reading is heuristically
  false in the fixed window), and the status_ruling amendment needed
  before (b) can ever move the node (precedent:
  e1_official_typicality_or_certificate).
- **Misses handled correctly**: the wrong registered pigeonhole
  margin (an actual scope error, caught by its own census
  disagreeing with round-25's), the wrong first Burnside bound
  (replaced by exact computation, not patched), GUESS-G refuted and
  reported as such, F3 declared superseded rather than silently
  dropped.
- **One DRAFT-ONLY violation, disclosed and benign**: running the
  banked large_v2_hunt/d1_h8.py escape test rewrote that pilot's
  state JSON. I verified git shows the file byte-identical to the
  banked version. No rule change needed beyond the existing "run
  banked scripts from a scratch copy" practice — added to the
  round-27 brief template.
- **Compliance otherwise clean**: quarantine held (ledger never
  opened), compute law total (RAMGUARD_TIMEOUT never used), RAM
  discipline held (bins + checkpointed background sampling), no
  subagents.

## Corrections applied

- critical/nodes/integer_code_distance_cert/statement.md — round-26
  addendum: THEOREM B1 with proof sketch and provenance, the three
  teeth (two SURFACED decisions flagged), the consumer-bar mapping,
  the falsifier record (F1/F2 run, F4 standing), LAW-2 general-w
  closure, box depth 2^40. No status flip.

## Follow-ups filed (not executed)

- USER DECISION 1: adopt the numeric per-cell form of (b) (the
  asymptotic reading dies at N'=256).
- USER DECISION 2: amend integer_code_distance_cert/status_ruling.md
  to admit the density branch (else (b) can never move the node).
- Mint candidates: THEOREM B1; the LAW-2 linear digit law (P2 + the
  c_k tables) — both are clean, self-contained statements.
- The c_k low-half structure (no pattern found at h=32) — a small
  open question; the tables are banked for a future attempt.
- F4 stands armed: any collision at a deployed Proth row is a 2^27
  surprise — worth wiring into any future per-row certification run.
