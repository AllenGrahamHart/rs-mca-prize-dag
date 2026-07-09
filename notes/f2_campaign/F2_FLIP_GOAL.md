# F2 FLIP CAMPAIGN — STANDING GOAL (pre-registered 2026-07-09)
# Owner: Claude (kernel/Fourier lane). Codex stays on F3 — untouched.

## GOAL

Flip u2c_giant_tnull_dichotomy (F2, the EXTRAS-BUDGET floor) from
TARGET (red) to PROVED (green) on the critical surface.

This goal TERMINATES only on one of:

  T-WIN:   a dag_commit in which u2c_giant_tnull_dichotomy is PROVED,
           every lemma in the ladder below has a green verifier, and
           the consumer arithmetic (b2_modp_giant_extras -> the x4
           cluster: extras + trades <= n^3 = 2^123 at official
           prize-max rows, beta-normalized windows) is replayed green.
  T-FLOOR: the pre-registered falsifier fires — sub-balance scaled
           rows with extras exceeding the transported n^3-scaled
           budget, sustained across >= 3 scales (above-balance window
           accidents do NOT count). Outcome banked as
           COUNTEREXAMPLE_NEW_FLOOR, the node re-posed, campaign
           terminates as an honest refutation.

No other exit. Pausing for higher-priority maintainer work is allowed;
abandoning is not. Each session that touches the campaign appends to
F2_CAMPAIGN_LOG.md and updates the resume pointer in memory
(rs-mca-f2-flip-campaign).

## THE OBLIGATION (honest state at pre-registration)

Everything already banked (do NOT re-prove): complementation lemma
(27762/27762), top-band rigidity, (t+1)-support rigidity, the
giant-block surface closed by proof, the structural count pinned at
700 (q-independent), three hardening families absorbed (F2-A1/A2/A3b),
catch #11 beta-normalization (windows in the GENERATED field), and —
2026-07-09 — the HIGH-ENERGY branch closed with printed constants
(f2_effective_energy_dichotomy: super-budget families forced
E < |A|^3 / 2^7.75 even classical-safe).

THE ONE OPEN BRANCH (branch (b)): no super-budget additively-
dissociated t-null family in the sub-balance regime. Fourier-flatness
shape; the ~2% sub-balance margin (|F_p(D)|^t >= 2^n, beta-normalized)
is the resource.

## LEMMA LADDER (pre-registered; supersede only by a dated entry here
## stating what changed and why — the F3-brief discipline)

L1 EXPLORE (falsification-first, FIRST MOVE): the Fourier spectrum of
   the t-null moment map at toy sub-balance rows. Modal experiment,
   pre-registered here: for rows (q, n, t) spanning the 192/64/0
   window transition (the F2-A1 calibration family), compute the
   pushforward mu = Phi_* Unif({0,1}^n at weight b) character sums
   |mu-hat(chi)| exactly at small scale; classify the large-coefficient
   set against the algebraic suspects (coset/quotient/dihedral
   characters); measure the minor-arc mass. FALSIFIER: persistent
   large Fourier mass on NON-algebraic characters across >= 3 scales
   in sub-balance. (If it fires, branch (b) as posed is wrong — bank
   and re-pose before any proof work.)
L2 MAJOR-ARC ROUTING: prove that a large Fourier coefficient of the
   weight-b t-null census forces coset/quotient structure — the
   Fourier shadow of the PROVED coset-union classification. (Upstream
   C9 analogue; dual-use export candidate.)
L3 MINOR-ARC FLATNESS => FIBER BOUND: Fourier inversion converts
   spectral flatness + the sub-balance margin into the extras count.
   This is where the 2% margin is spent; exact big-integer form at
   official rows, no o(*) anywhere.
L4 EXPLICIT CONSTANTS: pin (c1, e1, c2, e2) from one specific
   published BSG proof (verify the derivation, not just the claim);
   harden the energy-dichotomy table from symbolic to numeric.
L5 ASSEMBLY + FLIP: branch (a) [banked] + branch (b) [L2+L3] + the
   700-count => extras <= n^3 at every official row; replay the
   consumer arithmetic; dag_commit the status change; artifact + site.

## LAWS BINDING THE CAMPAIGN (restated, immutable)

- Falsification before proof at every rung; pre-register per lemma.
- One verifier per lemma, Modal unless very small; digests named.
- Honest labels: EXPERIMENTAL/CONDITIONAL never promoted; external
  imports under standing order 12 (proof-read + replay before PROVED).
- One-writer rule: I write prize/master; Codex's F3 worktree/branch is
  never touched by this campaign.
- Node-local notes rule: results land in the u2c node + satellites;
  this file and the log are the campaign spine.
- Every dag.json-changing commit: dag_commit.sh, artifact refresh
  (ebb725d6, favicon unchanged), publish_site.sh.

## NON-GOALS

Asymptotic formalization (upstream's lane); F3 (Codex's); the F6/F7
certificate track (separate lane); upstream PRs are welcome dual-use
exports but never gate a rung.
