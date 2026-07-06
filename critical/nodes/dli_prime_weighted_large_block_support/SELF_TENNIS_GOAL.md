# SELF-TENNIS GOAL (overnight autonomous mandate, set 2026-07-07)

**GOAL: close dli_prime_weighted_large_block_support by autonomous
self-tennis — playing BOTH chairs of the round protocol — or refute DLI-AGG.
If neither terminates, compress the node to an irreducible named core with
evidence dossiers. The user is asleep; do not block on input.**

## Round protocol (repeat until a termination condition)

1. **REFUTE FIRST** (adversary chair). Pick the sharpest live statement and
   attack it exactly as Pro would: engineered rows, lattice constructions,
   sieve-arithmetic stress, boundary probes, quantifier edge cases. A
   candidate counterexample counts ONLY after replay against the real
   objects — the exact D3 E-computation (notes/exact_E_worst_rows.py) is the
   ground-truth pricer; Pocklington for primes; volume RATIO checked, not
   just sub-volume.
2. **PROVE SECOND** (prover chair). Attempt the leaf with a written
   statement + proof in the node's notes, plus a machine-checkable verifier
   wherever the claim is finite/arithmetic (exact rational arithmetic;
   sympy for algebra). Labels are honest: PROVED needs a written proof AND
   replayed checks; otherwise CONDITIONAL/TARGET with the gap named in one
   sentence.
3. **ABSORB + RE-POSE.** Log the round in DLI_CLOSE_PINNED.md (same format
   as rounds 1-7); update the dag.json statement (one-writer rule; status
   flips only on verified replay); commit via tools/dag_commit.sh; fork sync
   (allen/prize-dag-delta) + artifact republish
   (https://claude.ai/code/artifact/ebb725d6-96a0-4e31-bb9b-14522786c58c,
   favicon 🗺️) + ./tools/publish_site.sh after every dag.json change;
   update the rs-mca-dli-tennis memory at meaningful state changes.
4. **Pacing.** Self-paced wakeups; prefer long sleeps (1200s+) over polling;
   Modal jobs must finish < 60 s each (shard by primes); local compute
   single-process < 1.5 GB. Do not edit PRO_DLI_CLOSE_6.md (Pro is working
   from it); self-round targets live in the pinned log.

## Leaf priority (re-derive each round; this is the opening book)

1. **A1-PROD (first theorem candidate — provable, do this first):**
   instantiate the weighted norm-sieve at production parameters
   (q ~ 2^255.9, L = 1..34, N = 256L, w* ~ 68L, lattice frame
   W_low(q) = Σ_{ternary v ∈ I_q, L+1 ≤ w ≤ w*} 2^-w). Deliverable: an
   unconditional theorem with explicit constants — density of q in a band
   with r·2N·W_low > T bounded by weighted Markov over the norm family —
   aggregated to "density of q violating the 100-bit form ≤ 2^-X", X
   explicit. Verifier: exact arithmetic instantiation script.
2. **Second moment / pair sieve:** two primes dividing one norm are
   constrained (resultant web, notes/resultant_gate_experiments.py is the
   evidence base). Any improvement sharpens X.
3. **A2 / R-BOUND (the hard core — the shared cancellation barrier):** the
   analytic route: for λ outside the low-weight lattice points,
   Σ_y log2 cos²(π a_y(λ)/q) ≤ -(256+δ)L + O(log q); the circle average is
   exactly -2/coordinate, requirement -1 (100% margin). Expect partial
   results; map every obstruction precisely (they feed L1/L2 too). Attack
   AND defend: a structured λ-family beating the margin would be a major
   refutation — hunt it first.
4. **LEVEL-INDEPENDENCE hypothesis** (flagged since round 1): the tower
   measure factorizes across levels (disjoint coordinate sets). Prove it or
   pin it as an explicit conditional with a verifier at toy scale.
5. **ENDPOINT EXCEPTIONAL RULE:** the honest statement of how the endpoint
   consumes "the deployed q is not exceptional" (engineering-hardness form;
   plus the strongest computable partial certificate at production q —
   low-weight windows that ARE searchable).

## Termination conditions

- **CLOSE:** every leaf proved + verified → flip the node on replay, full
  proof docs in the node folder, final round report.
- **REFUTE:** a verified counterexample to DLI-AGG within its quantifier
  scope → failure conversion (re-pose with the family priced / re-route),
  report loudly.
- **IRREDUCIBLE CORE:** a leaf that resists ≥ 3 genuinely distinct proof
  approaches AND ≥ 3 distinct attack families → freeze as a named
  conjecture with an evidence dossier and the sharpest surviving statement;
  when all remaining leaves are frozen, write the final structure report
  (what is proved, what is assumed, what would change either).

## Standing rules (unchanged, non-negotiable)

Verify-first; falsification-first; not-falsified ≠ true; honest labels; no
overclaiming. One-writer in canonical prize/. Only allen/* branches; never
merge/force-push/touch others' branches or PRs; do not edit tex/ or Papers
A-D. Commit as AllenGrahamHart with trailer
"Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"; push
--force-with-lease only. If the user relays a Pro DLI-CLOSE-6 reply at any
point, verifying it takes priority over everything else. Every round's
artifacts must be replayable by a stranger.
