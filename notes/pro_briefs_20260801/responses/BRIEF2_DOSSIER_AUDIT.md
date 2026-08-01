# Fable audit of the Brief-2 Pro dossier — 2026-08-01

**Verdict: SOUND.** All five principal corrections verified and accepted;
one is a confirmed defect in our own experimental code. The proposed
Bellman/owner architecture is accepted for Phase-0 evaluation; the
discipline list in the dossier's §20.2 is accepted as binding on any C2''
campaign. No DAG status changes.

## Replay and verification record

- Companion script: full PASS under `ramguard local`. The F_2^11 trap is
  checked EXHAUSTIVELY (2048 points; 33 mean-one factors; all 528 pairs
  exactly independent; joint normalized product exactly 2^22 = 4,194,304),
  plus exact fixtures for telescoping, Bellman-vs-enumeration, first-owner
  additivity, the class-correlation identity, the 2+2^-60 float
  misclassification, the granularity flip (51/50), sum-vs-max, absolute
  composition, and the printed C2R2 proxy (3.0508 bits = 14.53% of
  reserve).
- Hand checks: the trap's derivation (distinct nonzero forms have rank-2
  pairs, spanning family has trivial common kernel — 2^33·2^-11 = 2^22);
  the tilted-increment telescoping and Bellman recursion are standard and
  correctly stated; 34 levels/33 junctions with g_0 = 1; 2^21·2^100 =
  2^121 (catch-#40 half-band endpoint).
- **Import audit against our tree:**
  - Correction D CONFIRMED at source:
    `m1_dli_m1_tower_census_modal.py:571` — `Eck = cs[k] / cn[k]` in
    binary64 on the classification branch. Diagnostic-grade code, measured
    cells far from the boundary, no banked verdict alleged to flip — but
    the exact rule `cs*an > 2*cn*asum` is mandatory for anything
    proof-facing. Recorded as a dated node-local note beside the script.
  - Evidence count CONFIRMED: two rounds exist
    (`M1_RESULT_AUDIT.md` + `notes/c2r2_fround2_20260713/` with
    falsifiers/results/findings/report). Our brief said "first survived
    adversarial round" — undercount, corrected in the brief addendum.
  - The catch-#165 reserve-credit precedent and the C2R2 deferral of the
    true multi-junction product are as the dossier describes.

## Corrections to Brief 2 (addendum written into the brief)

1. **Route 3 (row-family finiteness): DEAD** — same universal-quantifier
   fence as Brief 1. Finiteness lives in witness types/chambers, never in
   primes.
2. **Route 1 (accident typology): SHARPENED, not refuted.** The
   enumeration our brief asked for cannot be the observed theta=2
   k-classes (granularity-dependent, tilt-blind, float-decided). It must
   be a canonical owner grammar: structural properties of the concrete
   path (support-minimal circuits / connected conflict clusters),
   invariant under regrouping, symmetry, and discovery order, stable
   under arbitrary prefix tilt.
3. **Our "sharpest question" (short telescoping series): REFINED.** The
   sound version is the tilted-increment identity + Bellman supersolution
   (no cancellation entitlement without an exact sign identity — dossier
   §6.12). The unsound naive reading (bound each junction, multiply) dies
   on the trap.

## What I accept beyond the corrections

- **The trap as a permanent fence.** It is elementary, exact, and kills
  an entire inference family (pairwise/adjacent/one-junction control =>
  joint control) that both our F-b proxy reads and any future "check the
  neighbors" shortcut would be tempted by. It goes into every C2''
  composition checker as a mandatory mutation control.
- **The four generic lemmas (PP2.2)** are provable now, are pure finite
  probability, and force the correct language on everything downstream.
  Worker-shaped.
- **Gate 0 (the exact seam) is genuinely OUR open item.** The prose
  ambiguity between X_full / staircase / "reduced" is real; C2PP_POSED
  and the consumer face use different presentations. Nothing (including
  pilots) should become a DAG premise before the seam node is PROVED.
- **The A >= 1 floor** must be cited from the zero-frequency marginal
  identity, not assumed — correct, and cheap to bank.

## Points of caution

- The dossier's own §20.1 admission stands: this is LESS finite than
  Briefs 4 and 1. The crux (canonical compression controlling the
  Bellman future under arbitrary tilt) is a genuine open research
  question, and the descriptor-collision protocol (PP2.4) is where it
  will live or die.
- The illustrative 2^10 + 2^20 budget split is planning arithmetic only.
- The Johnson-scheme/harmonic route is one candidate implementation of
  the bulk theorem, not a selected engine.

## Adopted posture

CONDITIONAL GO under the dossier's discipline, with sequencing:

1. **PP2.0 exact seam** — ours to draft (with Codex), the lane owner
   decision Pro requests. Nothing else counts before this.
2. **PP2.2 generic theorem suite** — bankable now, worker-shaped.
3. **PP2.1 true multi-junction toy compiler** — extend the archived exact
   tower; ground truth before any descriptor talk.
4. Owner grammar and descriptor collision audits only after 1-3; no
   fleet indexed by observed ratio classes, ever.

Reusable across the lane: the trap fixture, the exact-threshold rule, and
the seam discipline all apply to any future C1 packet-owner extension
(Brief 1's optional Phase 4) as well.
