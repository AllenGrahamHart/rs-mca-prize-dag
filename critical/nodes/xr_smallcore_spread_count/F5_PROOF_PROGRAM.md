# F5 PROOF PROGRAM (opened 2026-07-07): from hardened floor to theorem by obstruction mining

**OBJECTIVE: prove the F5 floor — for every pair (u,v) at the official
candidates, the post-strip spread remainder satisfies R_spread(u,v;A) ≤
16n³ — by the classification-first obstruction-mining loop:**

1. PROVE the failure-mode classification (every family member / every
   potential budget violation carries one of k explicit structures).
2. Per mode: HUNT counterexamples adversarially; each failed hunt must
   yield its obstruction, FORMULATED as a lemma.
3. PROVE each obstruction lemma (verify-first standard: a lemma draft is
   tested against the banked adversarial data before proof effort; "we
   couldn't construct it" is NEVER banked as "provably blocked").
4. COMPOSE classification + per-mode lemmas into the theorem; verifier
   instantiates the proof's constants at toy rows against the banked
   measurements; flip F5 to PROVED on replay. STALL = an honest report
   naming exactly the unproved hole.

## The target theorem and its skeleton

**THEOREM (target).** At the official candidates, for every pair (u,v):
the number of aligned aperiodic supports in the post-strip remainder
(pairwise cores < k+t−1, same-slope and tangent-charged mass stripped)
is at most 16n³.

Skeleton (lemma inventory with status):

- **L1 (classification).** Every z-aligned support of (u,v) is exactly one
  of: (i) SAME-SLOPE mass — the exact-list object of u+zv (rung 2a,
  identity PROVED in the rungs verifier); (ii) TANGENT-CHARGED — a
  distinct-slope pair with common core r ≥ k+1 forces (u,v)|core to a
  codeword pair with depth d = r−k ≥ 1 interpolation constraints (rung 2b
  two-slope identity, PROVED); (iii) LIVE — distinct-slope with all
  pairwise cores ≤ k+t−2. The remainder consists of class (iii) only.
  STATUS: assembly of proved identities + convention pinning against
  verify_xr_smallcore_rungs_2a_2b.py. [P1]
- **L2 (alignment ledger).** Each live aligned support at a new slope
  imposes σ = A−k linear conditions on the 2n coordinates of (u,v),
  namely the top-coefficient obstructions Π_S(u + z v) = 0. STATUS:
  definitional given the conventions; state exactly. [P1]
- **L3 (live-syzygy lemma — THE CORE).** Any nontrivial linear dependence
  among the alignment conditions of a live family forces, on the solution
  locus, either Π_S(v) = 0 for some member (an INVALID alignment — the
  direction word in a local code kernel) or one of the charged structures
  of L1(i)/(ii). STATUS: candidate form stated by Pro's window-5 attack;
  held adversarially at 5 toy cells incl. k = 4,5,6 (dependencies found;
  all collapsed to Π_S(v) = 0). To be attacked harder [P2], then proved
  [P3].
- **L4 (count).** L1+L2+L3 ⟹ live family size ≤ 2n/σ + O(charged
  boundary terms) ≤ 16n³ with ~2^100 slack at the officials. STATUS:
  arithmetic once L3 lands; the Θ(n) cap was measured exactly (0.55n
  engineered maximum across three scales). [P4]

## Evidence base (the program's test suite)

- Banked: F5-A1 (spread slope-limited = q), F5-A2 (engineered cap
  Θ(n), dimension count confirmed), F5-A3 (strip-integrity spectra;
  random tangent cores collapse at d = 2), Pro window 5 (syzygy adversary
  incl. k ≥ 4: all dependencies died by Π_S(v) = 0; its toy table is the
  standing counterexample-hunt baseline), the rungs-2a/2b certificate
  (38 checks).
- Every L3 draft must survive: (a) replay against Pro's dependency table,
  (b) a fresh adversarial hunt targeted at the draft's exact hypotheses
  (the P2 instrument), before proof effort is spent.

## Phases

- **P1** — pin conventions and write L1/L2 exactly (source: the rungs
  verifier; no paraphrase). Deliverable: F5_SKELETON.md with formal
  statements.
- **P2** — attack L3 as stated: adversarial hunt for a LIVE syzygy
  (dependent live alignments with all Π_S(v) ≠ 0 and no charged
  structure), Modal, k ∈ {2..6}, engineered dependency constructions
  (not just greedy): if found, L3 is false as stated → weaken and
  re-enter the loop (that is the method working, not failing).
- **P3** — prove L3 (expected shape: a dependence vector λ over the
  family gives Σ λ_i Π_{S_i}(u + z_i v) ≡ 0 as a polynomial identity in
  (u,v); expand in the pencil variable; distinct slopes make the slope
  powers independent unless supports interact through a shared kernel —
  drive that interaction into Π_S(v) = 0 or an L1 structure).
- **P4** — compose, write the theorem verifier, flip F5 on replay; full
  ritual; report.

Standing rules: verify-first; honest labels (PROVED only with written
proof + replayed checks); Modal-first compute; one-writer; ritual after
dag changes; every artifact replayable.
