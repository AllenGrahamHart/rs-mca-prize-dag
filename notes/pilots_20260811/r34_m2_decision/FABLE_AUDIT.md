# FABLE_AUDIT — r34_m2_decision (round 34, bank 4/4)

Auditor: coordinator (Fable). Date: 2026-08-11.
Verdict: **BANKED — the fields-searched negative ACCEPTED with its
own grading (NOT a theorem), the TCAP-DIM correction ACCEPTED, and
the (L2) gate PROMOTED to the question of record.** Node work:
UPDATED marker on the round-33 TCAP-DIM pose, the round-34 (SAT3)
m=2 decision addendum, and the ROUND 34 CLOSE reconciliation, all
on `critical/nodes/rate_half_band_crossing_location/statement.md`.
No status flips; census unchanged.

## Replay

- `d1_layers.py` (globally seeded 20260811; takes an output-path
  argv) replayed under `tools/ramguard local`
  (RAMGUARD_TIMEOUT=290) to a scratch path: EXIT=0,
  **byte-identical** to the banked `d1_results.txt`. This covers
  the design classification (420/1), the (L2) exact table, the
  nullity histograms, the e=m=2 scan (0 genuine), the Kummer e=2
  analytic kill's numeric confirmation, the (L1) rank histograms,
  and the corrected ledger.
- The pilot's replays of round 33's banked scripts
  (`replay_d1_m1_results.txt`, `replay_d2_realize_results.txt`)
  **re-diffed by me against the round-33 banked files:
  byte-identical both** — the m=1 realization theorem (16
  families, exhaustive at q=17) now carries independent replay
  evidence from a second code path, closing the replay gap round
  33 declared.
- `d2/d3/d4_results.txt`: every number quoted in the REPORT
  matches the files (n7 histograms, k=4's n7=8 with nullity 0,
  the degenerate-rate table). Not re-run (large randomised
  searches; the exact-layer facts are what carry weight and they
  replayed).
- REPORT.md persisted via recover_report.py (WROTE verified,
  39,076 chars; no entity corruption).

## Hand-checks (mathematics)

1. **(L2) overdetermination:** (m+2)(4m+1) - 16m = 4m^2-7m+2 =
   -1, +4, +17, +38 — CHECK; m=1 uniquely underdetermined, and
   round 33's own docstring ("a nonzero solution ALWAYS exists")
   confirms the mechanism reading of its m=1 success.
2. **TCAP excess polynomial:** 12m^2-24m-1-O reproduces the banked
   -13, -1, +35, +95 — CHECK; corrected +4/+6 gives +3/+5 at m=2;
   both positive controls verified preserved (m=1 negative; e=1
   ladder -8m-1 < 0). The finite-stabiliser argument (fixing 9
   slopes + 32 points forces triviality) is sound. NOTE: the
   independent locator-layer bookkeeping uses the OPPOSITE sign
   convention (params-minus-conditions; -5 = infeasible-expected)
   — "agreeing in sign" in the REPORT means agreeing in VERDICT;
   flagged as wording, not error.
3. **The exact witness detector:** 31 edges = 62 endpoints on 9
   vertices, degree cap 7: <= 7 full vertices gives <= 7*7+2*6 =
   61 < 62, so >= 8 slopes must be totally split — n7 <= 7 is an
   exact kill certificate. CHECK.
4. **Symmetry table:** spot-checked k = 3 (9 = 3*3, F = 0; |U| in
   {31,32} = 1,2 mod 3 with f <= 2: admissible), k = 4 (F = 1
   forced fixed slope, u in {6,7} = 2,3 mod 4: dead), k = 7
   (fixed u = 7 = 0 mod 7 fine but |U| = 3,4 mod 7 > f: dead).
   CHECK — {2,3} only. The MISS-3 disclosure (the printed
   d3_results.txt line "k=2 only" is superseded by the
   hand-corrected {2,3}) is honest and the correction direction is
   conservative (a LARGER escape hatch, still closed).
5. **Coset mechanism = R4 fence:** tau = id => members are
   mu_rho-cosets => distinct cosets disjoint => d_x <= 1 =>
   T*rho <= N, the banked round-31 fence, 63 > 32. CHECK — the
   identification is exact and it retro-explains why every
   structured success in the campaign lived at e = 1.
6. **Degenerate-family rate:** (49/32)/q = 1.58%/0.79% vs
   1.43%/0.71% measured — CHECK, two fields; and (SAT1)'s s = 0
   (`saturation_rigidity/statement.md:13`) forbids the family, so
   the certification pass's zero is genuine.
7. **P8(a) irreducibility proof:** rational factorisation forces
   saturated points <= 9*min(d_1,d_2) <= 27 < 31 — CHECK.
8. **P8(b) withdrawal:** verified the flaw is real (the design
   makes the fibre UNION invariant, not each fibre) — the
   withdrawal is correct and correctly graded (rationality
   UNDECIDED, not resolved).

## Cross-pilot reconciliation (coordinator-only; both pilots were
quarantined)

**(DEF-ID):** bank 3's (BIV-G) W-layer deficit
(7m^2-9m+2)-(3m^2-2m) and this bank's (L2) overdetermination
(m+2)(4m+1)-16m are the SAME quadratic 4m^2-7m+2 — two mutually
blind pilots, two ostensibly different objects, one polynomial.
Banked in the round close as an observed identity with unexplained
mechanism (round-35 question), NOT as a theorem.

## Subtraction (CATCH-24A)

The pilot's table re-checked: the RNC-curve reduction is banked
(its honest MISS 8), the coefficient-chain gate is the named next
gate of three claim-contracts (its MISS 9), the Kummer exclusion
is banked-PROVED at the endpoint and the pilot correctly grades
its own m=2 argument as agreeing-not-extending. My re-greps
confirm the two novelty claims: "automorphism" appears only in
unrelated lanes (no moduli-quotient prior), and no
"overdetermin*" prior exists in the endpoint lane. CLEAN — and
the pilot's five live subtractions are correctly load-bearing.

## Compliance

- **Compute law: CLEAN.** 8/8 invocations under ramguard with the
  literal `--`; zero bare python3; two in-guard deaths (MemoryError
  from its own unbounded enumeration — the guard contained them,
  disclosed as MISS 4). Fourth consecutive clean pilot under the
  upgraded clause. NOTE: the REPORT's "two `sed` call-site patches
  were shell text edits, not interpreter runs" — this repeats bank
  3's write-path deviation class (sed instead of Edit/Write);
  CENSURED the same way; round-35 CONSTRAINTS must name sed/awk
  in-place edits explicitly.
- **Quarantine: CLEAN** (search-level --exclude-dir throughout;
  ledger never opened; no sibling r34 dir touched; the round-33
  sat3 dir read as explicitly permitted).
- **Write scope: CLEAN** — everything inside the pilot dir; banked
  scripts copied before running; AUDIT-AND-DRAFT respected.
- **Registrations:** followed in the registered route order; the
  three self-falsifications (P8(b), the premature naive-count
  refutation, the crude printed symmetry line) reported misses-
  first. P5 hit exactly; P2/P6/P7 hit; P3 unexercisable (zero
  power declared in advance).

## Mint queue additions (not yet minted)

1. The (L2) gate node — the exact realization count, the m=1 sign
   uniqueness, the degenerate-family classification, and the e=m
   nonemptiness question as target of record (R-L2).
2. The corrected TCAP-DIM re-pose (boundary m <= 1) with the
   automorphism-quotient bookkeeping and both preserved controls.
3. The symmetry classification k in {2,3} + the coset-mechanism =
   R4-fence identification (elementary; low novelty confidence
   outside the repo — graded as such).

## Round-35 anchors fed by this bank

R-L2 (the decisive question — construct or refute e=m=2); the T
measurement on any witness (first real m >= 2 data; F1 finally
live); DEF-ID.
