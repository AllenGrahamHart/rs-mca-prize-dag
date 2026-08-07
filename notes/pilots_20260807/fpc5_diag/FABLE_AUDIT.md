# FABLE_AUDIT — fpc5_diag (round 23, agent 3 of 4 to report)

**Auditor:** Fable, 2026-08-07. **Verdict: BANKED, MAINTAINER-LEVEL —
the classification question answered decisively: ALL THREE FPC5 reds
are MYSTERY-HARD against ONE wall, and the pilot proved it is one
wall by the shape-pun test — the single statement (MF) ("count
degree-d locators split on C inside a flat of projective dimension
e = 2d+1-t*ell, codim sigma") specializes exactly to all three reds
AND to upstream prob:capfr1-master-flatness. Two structural theorems
make the classification rigorous rather than vibes: the
CODIMENSION-RESERVE IDENTITY (codim = sigma identically — verified
exactly against both nodes' printed codimensions, making every FPC5
first moment <= 2^{-7.95e12} at the official row) and the e-IS-THE-
FLAT-DIMENSION reading of the FPC5 clause. None of the three is a
counting problem; all three are max-to-mean on a Theta(n)-dimensional
flat — which also kills the mystery-6-style rescue in advance (the
box here is binom(N, 0.4N), exponential, not n^6).**

Replay: fpc5_exact.py reproduces the identity table, the official
constants (ell = 219,902,325,556 and d = 439,804,651,109
cross-checked against the sharp_dyadic verifier's own pinned
values), and the -7.948e12 first-moment bound; the A1 replication
gate PASSES exactly (dim 3 / rank 3 / codim 3 at the banked cell);
the packing adversary reproduces max_packed = 4 at 5/5 trials with
the escape threshold not fired. REPORT.md persisted verbatim (task
a1f7a9281cb13bb84).

ADOPTED (addenda applied to all three red nodes):
- **Red 1 (m4_t2):** mystery-hard; THE CAP-4 LEAD (the pilot
  invented a strictly stronger adversary than the node's own
  attack surface — core-choosable set packing over the full monic
  chart, exhaustive sound BB — and it stops DEAD at 4,
  q-invariantly, with ~1200x adversarial gain over the mean and 0
  hits on the official domain); the SCOPE PIN (the banked
  nonemptiness census is label-free, factor ~q above the
  fixed-source object — correct for its job, not a density); the
  derived sharpened overlap cap |D cap D'| <= 2s - b (immediate
  from JD1 + the sharp-cell forcing r = b; checked on all
  witnesses; improves (RH0b) to 2^{1.61 ell}); the finite
  decidable ell = 4 probe named.
- **Red 2 (m4_t3):** mystery-hard + a strictly harder access
  problem (minimal live tail cell binom(42,17) — no census will
  ever reach it; 1.9M live cells); the OWNER-QUALITY finding
  (52.4% of the measured atom sits at the trivial owner G = 1
  where the fixed-owner charge is maximal — the binding problem is
  owner-quality, not the owner-count the attack list targets); the
  measured cap = the proved Bonferroni cap (the pair-determinant
  instrument is TIGHT); the base-cover probe named (minutes, from
  existing data).
- **Red 3 (large source):** mystery-hard and least defended — the
  registered exposure FIRED as an exposure (not a witness; the
  partition stands): 408 unsieved residual rows, e up to n/3, no
  t >= 4 overlap theorem, no background guard. The NAMED GATE: the
  t-petal overlap-cap lemma (proved verbatim at t = 2, 3) makes
  the already-computed J-sieve legal at a stroke. Also: t <= M
  always (H3, corrected by the pilot before registering), and
  touched-subset multiplicity is FREE — the node's own attack
  note aims at a non-obstruction.

HONEST LEDGER accepted: ONE COMPUTE-LAW SLIP disclosed (a bare
python3 -c pretty-printer that ERRORED and produced nothing; no
number descends from it — recorded, not hidden; the clause-
hardening precedent stands); the unsound prune caught and re-run
with the sound bound (answer unchanged); P6's vacuous threshold
self-identified; two registered cells honestly not run (ell=6
infeasible under the wall; A4 registered-not-run); the free-domain
relaxation and the unchecked maximality guard disclosed. P1-P8 all
confirmed (P3 at 3 of 4 cells); the 2-power reachability law P1
(sharp cells 2-power only at ell in {4, 52, 820}) explains WHY the
banked certificate sits at n = 32.

SURFACED TO THE USER (not decided here): the three reds classify
into the SAME new wall — (MF), the master split-locator flatness
obstruction, upstream-visible as prob:capfr1-master-flatness. This
is a MYSTERY-BOARD PROMOTION QUESTION (mystery 7?), which is the
user's call per the standing convention. The accounting today: 28
reds = 14 mystery-linked + 9 WCL-grind + 2 straddling + 3 FPC5
(now diagnosed mystery-hard, one shared wall).

BOARD EFFECT: wave 48's deliberately-unclassified reds are now
classified with quantitative handles (the q-invariant cap 4; the
52.4% trivial-owner concentration; the 408-row exposure) and three
cheap named probes. ROUND-24 CANDIDATES from this lane: the ell=4
finite decision (5-packing or <= 4); the base-cover number; the
t-petal overlap-cap lemma (the highest-leverage single lemma —
it legalizes the sieve for red 3 AND generalizes the instruments
of reds 1-2).
