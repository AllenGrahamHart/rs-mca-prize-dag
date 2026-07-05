# GOAL (overnight): Adversarial audit of every critical CONDITIONAL

Author: roadmap owner. Date set: 2026-07-05 (night). Runs turn after turn until done.

## Mission

Every critical amber asserts a conditional proof: **"hypotheses A ⟹ claim B, and the
implication is PROVED."** Today three such ambers were falsified-as-stated (dli sup,
PRK, chargeability), two hidden reds were found wearing amber, and one stale gate had
made the root unsatisfiable. Audit ALL remaining critical conditionals **as adversarially
as possible**. The goal is to find **FATAL, non-repairable issues** — or, failing that,
to give each amber a survived-adversarial-audit certificate. In the morning the
landscape either changes or earns trust.

## Setup / hygiene

- Fresh worktree from the **latest `prize` master** (includes today's compressions,
  retractions, and the three validator laws). Work only there, own branch. Never touch
  canonical `prize/`, the artifact, or other branches.
- Modal available; **every run < 60 s wall**, checkpoint JSON before timeout.
- Ledger at `experiments/amber_audit/ledger.md`: per node — the implication as you
  understand it, the attack, the script, the replay command, wall time, verdict.
- Read `notes/EMPIRICAL_OBSERVATIONS.md` first: today's failure classes are your
  playbook. Read `notes/CHAIN_COMPRESSION_POLICY.md` for what packets/retractions mean.

## The audit surface (21 nodes, priority = dominated-swathe weight)

```
137 mca_grand              32 strip                    9 r2_clean_rates
 69 mca_safe               31 imgfib                   7 list_grand
 27 gap1_noneq_mass        24 tr_perleaf_list_ident    6 list_adjacency_closing
 23 x4_exactlist_staircase_split (HAS A REDUCTION PACKET — see below)
 21 ext_lift               21 adjacency_closing        4 list_safe
 16 f1_classification       2 xr_clean_residual_any_gate
  1 f1_case_pole            0 aperiodic_zero_at_crossing
  0 worst_word_planted      0 gap1_product_model
  0 f1_pole_list_threshold_location                    0 list_planted_arithmetic
```

Work highest weight first — a fatal issue at the top kills the most.

## Per-node protocol

1. **State the implication precisely.** From statement + conditional.md (+ packet):
   write down A (each wired hypothesis) and B (the claim). If you cannot state
   A ⟹ B crisply, that is itself a finding (verdict: ILL-POSED).
2. **Wiring check.** Every hypothesis the statement/proof actually uses must be a
   wired req edge. Prose conditions, "assuming the usual...", unnamed lemmas =
   violation (today's leaf-conditional and U2-C' precedents). Check the reverse too:
   wired reqs the statement never uses (cargo edges).
3. **Attack the IMPLICATION, not just A.** The strongest move: build a toy model
   where A HOLDS (or is granted at toy scale) and test whether B follows. A model
   with A true and B false is a FATAL refutation of the implication (the Gate N
   class). Use algebraic, analytic, and numerical means; be inventive.
4. **Attack the known quantifier pathologies** (today's harvest — check EVERY node
   for each):
   - sup-over-a-class where the endpoint needs only an average (dli sup class);
   - "absolute constant" that should be parameter-dependent (PRK B_pet class);
   - "every X" where degenerate/low-mass X breaks it (zero-heavy profile class);
   - a paid/charged class cited without a paid citation (Gate L class);
   - boundary rows / top-defect bands where generic arguments degenerate;
   - gate:any nodes whose alts include REFUTED or cut routes (rate_half gate class).
5. **Interface check on proved inputs.** Spot-check that each PROVED req actually
   delivers what this amber consumes — statement-of-producer vs use-by-consumer
   (the re-pose propagation class: a repaired input may no longer say what the
   consumer needs).
6. **Verdict** (one per node, in the ledger):
   - `SOUND` — survived genuine adversarial attack at its crux; say which attacks.
   - `REPAIRABLE` — issue found, a re-pose fixes it: re-pose in YOUR worktree with
     the reasoning; the owner replays in the morning.
   - `FATAL-CANDIDATE` — verified counterexample to the implication or a hypothesis
     that cannot be saved: flag LOUDLY, include the verified falsifier and replay
     command. Do NOT cascade-prune overnight; mark and move on (the morning replay
     decides surgery).
   - `ILL-POSED` — the implication cannot be stated crisply from the artifacts.
     OWNER DIRECTIVE (relayed 2026-07-05 night): if an amber is NOT of the form
     A => B (an identification A = B, or some other kind of claim), do not stop at
     classification — **just test the assertion directly and try to falsify it.**
     For A = B: compute both sides on toy rows and compare (one mismatch witness
     is a FATAL-CANDIDATE). For records/reports: replay the computation / verify
     the claimed half. The form classification below is for the morning repair,
     the direct attack is the night's work.
     For every ILL-POSED verdict, additionally CLASSIFY THE ACTUAL FORM and propose
     the fix:
       * IDENTIFICATION ("X is the same object as Y") -> restate as an implication
         with definitional hypotheses (state exactly which quantifiers/word classes/
         rows must align, and CHECK they do — misaligned identifications are how
         interface bugs breed);
       * COMPUTATION RECORD / CORRECTION ("the tables show...") -> the claim is the
         verified computation: propose PROVED-with-verifier (cite/write verify.py)
         or restate the residual implication;
       * STATUS REPORT ("half proved, in flight") -> extract the mathematical claim,
         restate it, and mark the unproved half honestly;
       * TITLE/STUB -> write the statement from the folder artifacts or flag FATAL.
     WHY THIS MATTERS: auto_discharge applies modus ponens when reqs turn green. A
     non-implication wearing amber gets auto-promoted to PROVED at the endgame
     cascade — the category error detonates exactly when the reds are finally
     resolved. Every amber must either BE an implication or stop being amber.

## Special: the reduction packet

`x4_exactlist_staircase_split` carries `REDUCTION_PACKET.md` — the composed dli-lane
conditional proof (7 compressed steps). **The packet's internal steps are part of the
implication**: audit them like nodes (they were validated pre-compression; your job is
to attack that validation). Same for any RETRACTION_MANIFEST advisory content that a
statement silently relies on.

## Verification discipline (the falsifier's falsifiers)

Every counterexample must be re-derived and tested against the REAL object before it
counts. Known traps that produced false verdicts this campaign: a z=1 primitive-root
bug (spurious mu_k catches); a whole-section PROXY instead of the true product object;
DEGENERATE samples (first basis vectors) instead of generic; LOWER-DEGREE embeddings
mistaken for exact-degree content; incomplete frequency sweeps. Also the reverse trap:
a "resisted" verdict only counts if the attack hit the node's actual crux — state
explicitly which obligation each attack tested.

## Morning report

End the ledger with a table: node | verdict | one-line reason | replay command.
Plus a short list: FATAL-CANDIDATES first, then REPAIRABLE with proposed re-poses,
then the SOUND set. "Not falsified" is not "true" — but a crux-level SOUND from this
audit is the trust certificate the board has been missing.
