# PRE-REGISTRATION — the TERNARY MASTER STATEMENT (round 19, GENERATIVE)

Round 19, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. MANDATE: build the strongest
honest form of the round-18 unification — a single parametrized
object and statement whose specializations are the banked instances
EXACTLY, with the proved instruments organized around it. A blind
sibling attacks the same candidate; your job is to make the best
version attackable.

## 0. The candidate (the three-plus-one instances)

As in the minted nodes — quote them verbatim before formalizing:
- background/nodes/f2_z1_mass_knife_edge (I1: the weighted ternary
  mass of the GRS dual on the half-system; the knife edge; Z-FLOOR;
  Z-1; Z-NOGO; route (b)).
- background/nodes/crossing_dsa_refutation (I2: single-condition
  ternary relations at theta of order 2L; DSA; LEMMA TC/ROT/OE).
- background/nodes/es_ternary_suppression_instruments (I3: LEMMA AB
  ternary vectors in cyclic codes at half length; CS; SP-COVER;
  CATCH E-2's self-similarity).

## 1. Pre-registered deliverables

- **(M1) THE MASTER OBJECT.** Define the ternary relation module:
  for a point multiset P = (theta_1, ..., theta_M) in F_{p^d}^* and
  a condition set Lambda, T(P, Lambda) := {eps in {0,±1}^M :
  sum_j eps_j theta_j^l = 0 for all l in Lambda}. State the master
  question family (existence / count / weighted mass — as a
  PARAMETER, not a conflation: round-18 CATCH-Z1 proved the forms
  come apart) and derive each instance as an exact specialization
  with a full dictionary (P, Lambda, alphabet-weighting, target).
  Any instance that does NOT specialize exactly must be reported as
  such — do not force it.
- **(M2) THE SHARED SPINE, proved.** The candidate structural
  theorems that should hold at master level, in order of value:
  (i) CHAR-0 EMPTINESS at 2-power orders (the Z-basis property —
  SUBTRACT first: LEMMA Z / b1_char0_giant_coset_theorem and
  round-18 CATCH-Z6's observation are the banked forms; what is the
  exact master-level statement, and is it already proved?);
  (ii) the reduction of all instances to "p | N(ideal of the
  relation)" with the Galois-multiplicity mechanism (CS) stated at
  master level — does CS's proof read verbatim over T(P, Lambda)
  for ANY Frobenius-stable Lambda, or does it need the window
  structure?;
  (iii) the orbit/symmetry structure (ROT negacyclic; the dilate
  action) at master level;
  (iv) Z-FLOOR at master level (the collision identity is
  alphabet-agnostic — state its exact scope).
- **(M3) THE INSTRUMENT MATRIX (constructive side).** For each
  banked instrument, state and PROVE the master-level form where
  one exists (with the exact hypothesis class), or the exact
  obstruction where it does not. This is the same matrix the
  adversary sibling builds destructively — the coordinator
  reconciles the two at the bank.
- **(M4) THE VALUE TEST.** A master statement earns its place only
  if it does work: exhibit at least one NEW consequence — a theorem
  about one instance obtained by proving it at master level with
  another instance's technique (candidates: does CS's multiplicity
  squeeze say anything at I1's GRS dual? does Z-FLOOR give a floor
  at I2/I3? does SP-COVER's coset-coverage mechanism transfer to
  the half-system evaluation points?). One proved cross-transfer =
  the unification pays; zero = say so.
- **(M5) THE NODE DRAFT.** If (M1)-(M4) survive, draft the master
  node statement (statement.md style, DRAFT in your dir — the
  coordinator mints) with the honest scope: what is proved at
  master level, what is per-instance, what the open master
  questions are (the mass bound at I1; the mid-range primes at
  I2/I3).

## 2. Pre-registered falsifiers / honesty clauses

- If no exact common specialization exists (M1 fails), the honest
  deliverable is the PARTIAL family tree — which pairs unify, which
  do not, and why. Do not paper over a failed specialization.
- Every master-level "proof" must be checked against each instance's
  banked verifier data where available; a master theorem
  contradicting a banked count is WRONG.
- Subtraction (hard law 5): LEMMA Z, CS, Z-FLOOR, SP-COVER, DSA,
  ROT, AB are all banked — the master level adds value only where
  it genuinely generalizes or transfers; claim nothing else.

## 3. Rules of engagement

- DRAFT ONLY: write only inside
  notes/pilots_20260806/tern_master_statement/. Never edit dag.json,
  node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/tern_unification_adversary/ (sibling
  independence).
- COMPUTE LAW: never bare python3, INCLUDING file patching and JSON
  peeking — tools/ramguard tiny|local -- python3 ..., literal --,
  from repo root /home/u2470931/smooth-read-solomin/prize. Toy
  grids: 2-POWER LENGTHS ONLY (CATCH-Z6) unless testing that rule.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.

---

# PILOT PRE-REGISTRATIONS (appended by the Opus pilot BEFORE any computation)

Round 19, 2026-08-06. Appended before a single line of code was run and
before any tools/ramguard invocation in this pilot directory. Sources read
first (statements only, no computation): the three minted instance nodes and
their four provenance PROOFS.md files, plus
`critical/nodes/b1_char0_giant_coset_theorem/node.json`.

## T-A1. The master object I will define (M1)

`T(P, Lambda) := {eps in {0,±1}^M : sum_{j<M} eps_j theta_j^l = 0 for all
l in Lambda}` with `P = (theta_0,...,theta_{M-1})` a tuple in `F_{p^d}^*`.
I register in advance the SPECIALIZED form I expect to be the load-bearing
one — `P = the half-system (xi^j)_{j<h}` of `mu_n`, `n = 2h = 2^m`,
`Lambda ⊆ (Z/n)^*` — and the claim that in that form

```text
T(P, Lambda)  =  the ternary words of the negacyclic F_p-code of length h
                 with defining set Lambda^* := <p>·Lambda,
                 of F_p-codimension g := |Lambda^*|.
```

## T-A2. The target is a PARAMETER (round-18 CATCH-Z1), registered as a weight

I register the target as `Phi_omega(P,Lambda) := sum_{eps in T, eps != 0}
omega(eps)` with `omega` a weight depending on the support size
`U = wt(eps)`, and the four settings I expect to see:
`omega = 1` (count), `omega = 2^{-U}` (I1 mass), `omega = 2^{h-U}` (I3
census), `omega = C(h-U, (r'_a-U)/2)` (I2 crossing fibre).
**Falsifier:** if any instance's banked target is NOT of this form, I report
the failure and do not force it.

## T-A3. Registered predictions (each may fail; failures will be reported)

- **P1 (dictionary).** All three instances specialize EXACTLY, with I3
  specializing only onto its ODD-condition sub-object (the even conditions
  being a different-length instance). PRE-REGISTERED AS A PARTIAL: I expect
  I3 to be partial and I say so now.
- **P2 (CS reads verbatim).** THEOREM CS's proof transports to T(P,Lambda)
  for every `Lambda ⊆ (Z/n)^*`, with `|Z_w^odd| -> |Lambda^*|` and
  `(r' - a_{n/2}(S)) -> U(eps)`, and needs NO window/consecutivity
  hypothesis. Sub-prediction **P2a**: `r' - a_{n/2}(S) = wt(A-B)` exactly.
- **P3 (the master threshold).** The single quantity `g·log2 p` versus `h`
  is simultaneously I1's knife edge, I2's DSA regime boundary, and I3's
  stratum-0 odd-class existence boundary. Quantitative sub-prediction
  **P3a**: at the banked I1 constants `h - g log2 p = -46.02` bits and
  `+17.98` bits under the two t-readings. **P3b**: at I2, `h/g = n/w = L`
  and DSA's `L-2` agrees with `h/g` to within 2.
- **P4 (Z-FLOOR forces existence off-instance).** `g log2 p < h` forces a
  nonzero ternary codeword in I3's `C_odd`. **Falsifier: any banked I3 cell
  with `g log2 p < h` and an exact ternary count of 0 KILLS this and I
  report it as killed.**
- **P5 (CS at I1).** CS-M at I1 yields `U >= p^{4R/n}`, a factor-2 exponent
  improvement on the banked dead norm route `p^{2R/n}`, and is still
  dominated by Z-1's `2R+1`. Registered as an EXPECTED DOMINATED transfer:
  if it is dominated I say the transfer paid nothing.
- **P6 (SP-COVER at I1).** SP-COVER-M is VACUOUS at I1, by exactly the
  saturation factor `log2 p` (`coverage needs R >= S`, object has
  `R = S/log2 p`). Registered as an expected ZERO.

## T-A4. Falsifiers / honesty clauses I bind myself to

1. Any master theorem contradicting a banked exact count is WRONG and I
   retract it, naming the cell.
2. If the value test (M4) yields only dominated or vacuous transfers, I
   write "the unification pays nothing" in those words.
3. Every instrument in the M3 matrix gets one of exactly three verdicts:
   MASTER (proved at master level, with hypothesis class), INSTANCE-ONLY
   (with the exact obstruction), or NOT ATTEMPTED.
4. Novelty is claimed only after the subtraction sweep returns; anything the
   sweep finds banked is cited, not claimed.

## T-A5. Grid rules

Toy grids: 2-POWER `n` only (CATCH-Z6), EXCEPT one explicitly labelled
rule-test stage that runs composite `2N in {12,20,24}` for the sole purpose
of reproducing CATCH-Z6's own numbers (8 / 8 / 80 common vectors). That
stage's outputs are never used in any conclusion about the official rows.

## T-A6. Compute discipline

Every execution via `tools/ramguard tiny|local -- python3` from the repo
root. No bare `python3`, including for file patching or JSON peeking. All
checks fail-closed, exit nonzero on failure, with a permanent failclosed
stage that exits 1 by construction.
