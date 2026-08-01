# Fable audit of the Brief-1 Pro dossier — 2026-08-01

**Verdict: SOUND — and it contains the single most valuable structural
observation anyone has produced about C1.** One route in our brief is
refuted and corrected; the proposed re-architecture is accepted for
Phase-0 evaluation. No DAG status changes.

## Replay and verification record

- Companion script: full PASS under `ramguard local`. Highlights: the
  `E = rZ` and fibre-variance identities checked against an **exhaustive**
  enumeration of all 2^8 Boolean fibres and all 3^8 ternary vectors at
  q=97 (genuine two-engine agreement, not self-confirmation); the 256-block
  factorisation `A_a = D_a F` verified block-by-block (256 x 3 fields,
  L=1,2,4, every determinant nonzero); `41^34 < 2^202`; the allowance-6/7
  fence; the accident-row repricing fraction; the schedule
  (34 levels, 33 distinct, sum 2^33, duplicate terminal L=1).
- Hand checks: `k_max = floor((2^256-2)/2^41) = 2^215-1`; Theta(q) DP
  needs >= 8*2^41 = 2^44 bytes at the smallest official scale; the orbit
  identity `C_a = (F^T D_1 F^(-T))^a C_0` follows from `D_a = D_1^a`;
  `theta = omega^256` has order `512L/gcd(512L,256) = 2L`; Newton covers
  the whole window iff `L+7 <= 2L` iff `L >= 7`, and every schedule level
  above 4 is >= 8. All correct.
- Import audit: `official_row_primes_pinning` says exactly what Pro claims
  (universal family, no hidden finite list). The consumer's
  `conditional.md` already assembles on exactly the proposed C1-SCHED
  scope (N=256L, q<2^256, 33/8, 41/8, 34 levels) — the scope reduction
  matches existing wiring rather than weakening anything. **Pro's
  independently derived ten-cell residual matches our ten
  `dli_wcl_slot_*_emptiness` TARGETs cell-for-cell** — a strong
  faithfulness check on both sides.

## Correction to Brief 1 (accepted; addendum written into the brief)

Our brief's "route 3" — prove the gated official row family finite and
enumerable, convert C1 to a certified census — is **dead as stated**. The
family is universal (PROVED node), and even capped it is a 2^215-sized
progression with a Theta(q) per-row decision procedure. The finiteness
that exists is in **witness types** (level types L in {1,2,4} + uniform
L>=8; short-owner cells; spectrum regimes; constraint-circuit grammar),
never in primes. Our own round-2 census machinery is falsification
apparatus, not a decision procedure — we knew this operationally but the
brief's route 3 implied otherwise.

## What I accept beyond the correction

1. **The variance/ideal reframe.** `E-1 <= 4r(1+W_ext)` is exactly
   "the Boolean cube is L^2-flat modulo a split cyclotomic ideal, priced
   by its sparse vectors." The `-1/r` baseline subtraction as load-bearing
   (work with `Z - 1/r`, never `Z - 1`) is exactly right.
2. **The 256-basis factorisation** — new, short, verified, and it converts
   the empirical phrase "iid saturation" into a theorem-shaped object:
   every block marginal is EXACTLY iid; the entire mystery is the
   dependence structure of one deterministic 256-step linear orbit; short
   relations are the low-complexity certificates of that dependence.
   This should be banked as a background node regardless of what happens
   to the rest of the program.
3. **The C1-ZERO re-architecture.** Making zero-window inverse flatness
   (SWIF-4) the first theorem fuses the mystery head with the already
   mechanical slot program: ten slots + Newton + C1-ZERO ==> the consumer,
   with W_ext = 0 (stronger than the 1/32 the assembly uses). It also
   evades the two deepest burdens (short-relation cluster interaction;
   unused aspect scope). The broad C1'-r3 becomes a stronger successor —
   which matches how the node was always consumed.
4. **The top-level v2 warning (stress 8.4)**: at 2N = 2^41 the ambient
   split has zero surplus, so no uniform v2-surplus argument can cover the
   schedule. This is a fence we had not written down anywhere.

## Points of caution

- SWIF-4 is a conjecture with NO current evidence beyond consistency with
  the falsification rounds (every known accident has a short owner). The
  class-5 falsification campaign (engineered dense-relation primes,
  multi-orbit norm-gcd stacks) is genuinely the first gate and could kill
  it — which would itself be a major structural discovery (a new
  high-weight accident class).
- The profile-grammar completeness theorem (Phase 2) is where I judge the
  hidden difficulty lives; Pro says the same (Gate 3).
- The engine menu (13.1-13.7) is honest about every engine's risk; none is
  selected, and none should be until the pilot.

## Answers to Pro's eight questions (relayed via maintainer)

1. **Scope replacement: YES.** A consumer-exact sibling (C1-SCHED /
   C1-ZERO) may take the critical-path wiring through a composition node;
   the broad node remains a background stronger sibling. This matches our
   established scope-node pattern; rewiring itself is surfaced to the
   maintainer at execution time.
2. **Field scope:** both clauses are real and bound opposite ends. The
   reframe certificate pins `for every choice of F, L, and k` with printed
   bounds (`k <= 2^40`, `|F| < 2^256`) plus the sufficiently-large-field
   proviso as a FLOOR. The proviso trims small fields; it does not create
   rows above the cap. Uniformity target: all admissible q in that
   interval.
3. **Galois/root-choice invariance: NOT banked.** Embedding orbits were
   handled operationally inside the round-2 census (CRT replays), never as
   a named theorem. Mint it in Phase 0 as proposed.
4. **Wiring:** C1-ZERO as a background theorem feeding a NEW composition
   node (per our partition law); do not fold into WCL-ZONE. The slot
   leaves stay independent premises.
5. **256-block orbit prior art: NONE.** The factorisation and companion
   operator are new to the tree; mint PP1.3 fresh.
6. **Ten slots closing independently: YES, realistic.** They are
   pre-registered TARGETs, exactly the mechanical half of the dli
   conversion, and worker-shaped (finite exact algebra per cell).
7. **C1-STRONG not required.** Consumer-exact closure retires the mystery
   from the critical board; the strong form stays background. (Matches our
   submission discipline: the red is the consumer's premise.)
8. **Upstream map: NONE.** dli is OURS_ONLY in the crosswalk; the proved
   K2 equivalence chain (`f2_zero_prefix_q_equivalence`) is the F2 lane —
   a different object. Any Fourier-side analogy to upstream work is
   currently unproved and must not be cited as a payment.

## Adopted posture

CONDITIONAL GO, Pro's shape: Phase 0 (four cheap interface nodes — scope
reduction, variance equivalence, ideal interface, 256-block factorisation)
is authorized planning-wise and worker-shaped; then the SWIF-4
falsification campaign BEFORE any theorem fleet. No official-q-indexed
computation ever. The 256-block node and the variance-equivalence node are
bankable now and useful even if SWIF-4 dies.
