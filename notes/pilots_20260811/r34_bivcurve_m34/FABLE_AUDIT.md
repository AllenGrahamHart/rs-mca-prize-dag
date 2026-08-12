# FABLE_AUDIT — r34_bivcurve_m34 (round 34, bank 3/4)

Auditor: coordinator (Fable). Date: 2026-08-11.
Verdict: **BANKED — headline ACCEPTED ((BIV-CURVE) realizable at
m = 3), with two coordinator corrections to (OUT-m) and one
subtraction catch.** Node addendum applied to
`critical/nodes/rate_half_band_crossing_location/statement.md`
(round-34 (BIV-CURVE) addendum + RESOLVED marker on the round-33
open-fork line). No status flips; census unchanged.

## Replay

- `m3_build.py` (the core witness verification, both fields,
  deterministic seeds end-to-end) replayed under
  `tools/ramguard local` (RAMGUARD_TIMEOUT=280): EXIT=0 and the
  regenerated `m3_build_results.txt` is **byte-identical** to the
  banked copy. This covers the full incidence table, the direct
  (BIV-CURVE) check on the explicit G, and the bivariate system
  (rank 39 / nullity 1 / admissible kernel / recovered mu) at
  q = 97 and q = 193.
- `m4_search_results.txt`, `m4_budget_results.txt`,
  `m3_phi_results.txt`, `m4_ckpt.txt` (15 checkpoint lines):
  present; every number quoted in the REPORT (histograms, BEST = 7,
  trials 632/24939, supply/demand table) matches the files. Not
  re-run (randomised searches; the banked witnesses are what carry
  weight and the m=4 negative is graded as searched only).
- REPORT.md persisted from the task output via recover_report.py
  (WROTE line verified, 44,637 bytes; no HTML-entity corruption;
  tail intact).

## Hand-checks (mathematics)

1. **(OUT-m) display inequality: CORRECT.** Re-derived from
   scratch: outside demand (rho-X)(m-1) - eps against capacity
   (rho-1)(m-1) - sum_delta I_in with
   sum_delta I_in = (m-2)X' + (m-3)X'' - def_in(S_gamma)
   rearranges to X' + 2X'' >= m-1 - eps~_gamma with eps~_gamma =
   TOTAL deficiency on S_gamma (inside + outside), <= 1+O per
   slope. The (OV) per-pair cap and the all-outside-blocks-are-
   type-2 step both check.
2. **(OUT-m) aggregate rider: FALSE — corrected.** The pilot's
   "sum_gamma eps_gamma <= 1+O" fails whenever a deficient point
   sits outside W: it charges every type-2 block through it
   (d_x = m-1 of them), so the correct aggregate is (m-1)(1+O).
   **The pilot's own witness refutes the rider** (its unique
   deficient point is the outside PAIR: sum eps = 2 > 1+O = 1 at
   m = 3). Forced correction carried into the node addendum.
3. **(OUT-m) corollary "X_gamma = 0 impossible": OVER-BROAD —
   qualified.** X = 0 forces eps_gamma >= m-1, which the per-slope
   budget 1+O forbids iff O <= m-3. At m = 3 this requires O = 0 —
   true in the witness and in the pilot's profile-target
   derivation (so nothing downstream falls), but the unqualified
   "for every configuration" reading is wrong (O = 1 at m = 3
   re-admits it). Qualified in the node addendum.
4. **Tightness claims: CHECK.** Tight exactly on the two degree-1
   H-slopes (t55, t57 at q=97: X' = 2 = m-1, X'' = 0); al0 = 92
   (X'' = 2, slack 2); consistent with the m = 2 exhibit's
   min X = 1 given its deficient point is INSIDE W.
5. **Profile arithmetic: CHECK.** sum X = (m-1)(7m-2) (38/78),
   capacity (4m-1)(2m-2) (44/**90** — the pilot's own catch of its
   R2.2 registration error "98" is right: 15*6 = 90), per-side
   (m-1)(4m-2) vs (4m-1)(m-1), slack m-1. X profile at m = 3:
   8*4 + 3*2 = 38 with n_4 = 8, n_2 = 3 — matches the witness
   (2,2,2,4,4,...,4). Outside completion: 83 = 121-38 = 27*3+2.
6. **The sigma/parity argument: SOUND.** sigma(x) = -x is
   fixed-point-free on mu_48 (0 not in mu_N); an involution on
   m-1 factors fixes one iff m-1 is odd (m even); a sigma-invariant
   factor is even in x, so deg_x <= 2 (odd top coefficient dies),
   i.e. Möbius in u = x^2, injective on orbits — the 3+3+2 split
   at m = 4 is forced, against every factor wanting degree 3
   (24 points into 15 slopes). Coherent; graded by the pilot as
   obstruction-for-one-class only, which I accept.
7. **Line anchors:** all four upstream quotes verified verbatim
   (statement.md:3043 open fork; :3136 orthogonality; :3014-3020
   TCAP-DIM; :585-588 m=1 disjoint).

## Subtraction catch (CATCH-24A)

The pilot's row 'grep "linear hypergraph", "partial Steiner":
zero files repo-wide' is literally true for its exact strings but
**misses a real prior on the concept**: the F3 h=3 flip campaign
banked a PROVED linear-3-uniform-hypergraph compiler at
`background/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LINEAR_HYPERGRAPH_COMPILER.md`
("The active coordinate hypergraph is a linear 3-uniform
hypergraph", pair-uniqueness forcing linearity) — the hyphenated
title and the "3-uniform" infix defeat the two-word grep. The
pilot's m=4 obstruction is therefore not the repo's first
linear-hypergraph object; different lane, different carrier, but
transportable machinery — recorded in the node addendum as a
transport candidate and as a fifth-surface lesson: **subtraction
greps must include hyphenated and infixed variants**
("linear-hypergraph", "3-uniform").

Other novelty claims survive re-grep: (SPLIT-m), the involution
device in this lane, and (OUT-m) (every banked type-2 X-bound is
an upper bound) are new.

## Compliance

- **Compute law: CLEAN.** Six invocations, all under ramguard with
  the literal `--`, RAMGUARD_TIMEOUT documented; **zero bare
  python3 for any purpose** — third consecutive round-34 pilot
  clean under the upgraded clause. Two ramguard events disclosed
  (a TypeError fixed via Edit; one wall kill at 290 s with a
  zero-byte output, rerun checkpointed).
- **Write discipline: ONE disclosed deviation** — a single
  `sed -i` patch to its own m4_search.py trial counts instead of
  the Edit tool. No mathematics computed by it; not a compute-law
  breach; CENSURED as a write-path deviation (the clause "file
  edits use Edit/Write" is not advisory). Round-35 CONSTRAINTS
  will name `sed -i` explicitly.
- **Quarantine: CLEAN** (ledger never opened; sibling r34 dirs
  never listed; --exclude-dir at the search level throughout).
  Write scope confined to the pilot dir (git status verified: no
  writes outside it beyond the still-running sibling's own dir).
  Banked scripts copied before use; biv_core.py used unmodified,
  so the witness is gated by bank 2's verifier, not the pilot's.
- **Registrations:** honest — the two registration errors (R2.2
  capacity 98, R2.4's powerless aggregate instrument) reported as
  misses, not edited; the MISS-2 guard fired in both directions
  exactly as designed.

## Mint queue (not yet minted)

1. (OUT-m) background node — with the CORRECTED statement
   (per-slope eps~ <= 1+O; aggregate (m-1)(1+O); corollary gated
   on O <= m-3) + both checks.
2. The m = 3 (BIV-CURVE) witness fence node (companion to the
   m = 2 exhibit fence already queued).
3. The (SPLIT-m) + involution construction template (with the
   m = 4 obstruction record and the u1_x4 transport pointer).

## Round-35 anchor candidates fed by this bank

- m = 4 decision (F2/F3 of the pilot): non-split G, sigma(x) = c/x,
  un-symmetrised (3,3,3); the u1_x4 linear-hypergraph compiler as
  imported machinery.
- Layer A on the m = 3 witness (the one unmeasured expectation —
  cheap, decisive for the orthogonality picture at m = 3).
- m = 5 parity falsifier ((SPLIT-5)+sigma all-swapped).
