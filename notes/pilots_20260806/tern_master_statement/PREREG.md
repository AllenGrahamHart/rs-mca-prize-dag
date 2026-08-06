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
