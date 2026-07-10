# Multiagent attack doctrine — lessons from the Sol/CDC prompt
# (2026-07-10; source: the published prompt behind GPT-5.6's proof
#  of the Cycle Double Cover Conjecture; banked for our kernel
#  attacks)

## The CDC prompt's core ideas, distilled

1. PORTFOLIO WITH ENFORCED INDEPENDENCE: many concurrent agents on
   genuinely different formulations; DO NOT tell most agents the
   currently favored approach — early-round independence prevents
   convergence on the attractive-but-incomplete reduction.
2. APPROACH-FAMILY REGISTRY: group agents by mathematical idea (not
   wording); monitor concentration; redirect when one family
   dominates.
3. THE ANTI-ELEGANCE GUARD: a route ending at a lemma EQUIVALENT IN
   STRENGTH to the target is not progress unless it supplies a
   genuinely new proof of that lemma. Mark such routes BLOCKED.
4. BLOCKED-ROUTE LEDGER with a reopening criterion: only a
   materially new mechanism/invariant/construction reopens a
   blocked route.
5. LATE CROSS-POLLINATION: keep incompatible routes alive across
   rounds; merge ideas only after independent development exposes
   real strengths and gaps.
6. ADVERSARIAL AGENTS THROUGHOUT, with a DOMAIN-SPECIFIC checklist
   (for CDC: exact-two multiplicity, closed trails masquerading as
   cycles, parallel-edge 2-cycles, bridges introduced by
   reductions, circular use of equivalent statements).
7. CONCRETE DELIVERABLES ONLY: reject status reports, vague
   optimism, and 'routine' claims for unproved global
   compatibility statements.
8. ROOT-AGENT SYNTHESIS LOOP: synthesize, challenge, redirect,
   relaunch; do not stop at the first failed wave.
9. HARD RETURN CONDITION + TIME FLOOR: return only a complete
   audited proof (or continue); 'assume a complete proof exists'
   as an anti-hedging device; forbid web-searching the answer.

## Overlap with our workflow (independently converged)

- (6)+(7) ARE our laws: falsification-first, one-verifier-per-
  claim, pre-registered reads, no unverified claims banked, the
  Sol adversarial checklist (complements/lifts/Frobenius/tensor/
  characteristic/multiplicity).
- (3)+(4) are our no-go ledger — arguably STRONGER in our form:
  our no-gos carry proofs of deadness with quantified margins
  (the annealed constant; the Parseval-isometry catch #23 is
  literally their guard 3 discovered empirically: our E3 'chain'
  ended at a bound equivalent to the trivial one).
- (8) is the one-writer/maintainer synthesis role.
- (9) is the stop-hook goal pattern (T-WIN/T-FLOOR only).

## Differences — what we now ADOPT

A. THREE DELEGATION MODES, formally distinguished:
   REPLAY (current; full context shared — correct for auditing
   known claims); FALSIFY (current; frozen target + guards only);
   ATTACK (NEW; the CDC mode): blind independent waves on a
   frozen kernel statement.
B. THE INFORMATION-SHARING RULE for ATTACK mode: PROVED NEGATIVES
   (no-gos, falsified routes) MAY be shared — they are theorems
   and save wasted effort. UNPROVED FAVORED ROUTES must NOT be
   shared in early waves — they are the bias vector. (Our current
   delegations share everything; fine for replay/falsify, wrong
   for attack.)
C. APPROACH-FAMILY REGISTRY per kernel attack: a live table of
   families tried, their status (live/blocked + reopening
   criterion), and concentration.
D. THE EQUIVALENT-STRENGTH TEST as an explicit gate on every
   'reduction' an attack wave returns (we already do this by
   instinct — catch #23, no-go #10; now it is a named gate).
E. WAVE ORCHESTRATION: for a funded kernel attack (user opt-in),
   use deterministic fan-out (the Workflow harness): round =
   {diverse blind attackers} -> {adversarial verifiers} ->
   registry synthesis -> next round; hard return condition; time/
   budget floor set by the user.

## Where our economy deliberately DIFFERS (and should stay so)

The CDC prompt optimizes a single all-or-nothing summit push:
partials are forbidden. Our campaign economy optimizes MONOTONE
BANKED PROGRESS: verified increments, catches, and structure from
failures (the aspect guard came from a failed target). Both are
right for their contexts. Rule of thumb: use ATTACK mode
(all-or-nothing, blind waves) on kernels that resist incremental
banking (the parity summit; H3-ACT's corridor); keep the banking
economy for everything else. The falsification rounds feed the
attack rounds: every proved negative sharpens the next wave's
statement without biasing its routes.

## Candidate first application

K2*'s hardest instances: (1) the parity summit (1B) — all
spectral bases closed, needs invention; (2) H3-ACT's middle
corridor (Codex's blocker #1) — incidence-geometry genre with a
rich toolbox. Both have frozen statements, proved-negative
ledgers to share, and no favored route worth biasing waves with.
