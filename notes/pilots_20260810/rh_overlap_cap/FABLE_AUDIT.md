# FABLE_AUDIT — rh_overlap_cap (round 31)

Coordinator: Fable. Date: 2026-08-10. Pilot: Opus (~42 min, 59 tool
uses, 5 interpreter invocations, all ramguard; one superseded run
and one self-walled ladder run disclosed). REPORT.md persisted
verbatim by the coordinator (harness refused the pilot's write).

## Verdict

**BANKED — THE ROUND-29 NAMED OBJECT IS REFUTED, AND THE REFUTATION
IS WORTH MORE THAN THE ROUTE: the safe half's "one inequality" (a
pairwise-overlap cap below a^2/n at sigma = 2^34) is FALSE, for
three stacked reasons: (1) OBJECT SLIP — T5's cap constant k-1 is
the single-word list cap; the correct column-far ceiling is a-1,
already banked twice in-repo ((AP3), KEY LEMMA), and larger by
exactly 2^34; (2) ATTAINMENT — LB1 constructs, at every RH-AC row
(q > 2^167), a column-far pair whose bad slopes form one full
T1-line of r+1 slopes with every pairwise overlap exactly a-1;
(3) SELF-DEFEAT — a-1 > a^2/n for all 2 <= a <= n-2, so no such
cap exists anywhere in the open bracket. The 0.999748 "they end
together" coincidence is an identity artifact (true ratio with the
correct cap: 1.032006). THE POSITIVE YIELD: the campaign's first
LOWER bound on B_ca^far at the safe index (2^39.9773, 88.02 bits
under budget), tightness of the banked T <= r+1 on its whole
domain, and B_ca^far(3n/4) >= 2^39+1 exactly — budget 2^39
unattainable at the bracket top, settling the sliver question's
top end negatively.**

## Coordinator verifications (mine)

| what | result |
|---|---|
| the (AP3) + KEY-LEMMA cap anchors | verbatim (max joint pair agreement <= A-2, i.e. overlap <= a-1; s+t-r >= 1) — the a-1 cap IS banked; T5's k-1 was the wrong object |
| LB1's counting argument | HAND-VERIFIED: the (U_0,U_1) split, MDS determination of p_1 for |U_0| < k, the q^{k-a+|T|} bad-assignment count per subset pair, the 2^n union bound, the extra q factor for spurious witnesses -> (LB1-C) n < (a-k-1) log2 q; and the witness check A_{lam_j} = E u {j} exactly (distinct lam) |
| the self-defeat lemma | trivial and exact: a^2 - na + n < 0 for 2 <= a <= n-2 |
| d1_exact.py + d4_lb1.py replays | green; RATIO_CAP closed form matches at the razor; the S3 window arithmetic reproduced |
| CATCH-24C on the consumer | the divergence is real: E_P is a codeword-pair agreement (f_1 = u, f_2 = v on E_P per round-29's own T1 derivation); round-29 flagged the Johnson anchor as "bounds L_1, not B_ca^far" and then imported its constant anyway |
| claim-grep for the false object | exactly one carrying file (crossing_location statement) + zero node.json shards — pilot's grep independently re-run |

## Coordinator actions (forced-corrections authority)

- Inline FALSE marker on the T5 paragraph (the P0 pattern) +
  the round-31 overlap-cap addendum appended to
  crossing_location/statement.md: the refutation, LB1 and its
  consequences, the S3 delimitation, the residuals of record
  (R-LINEDEGREE / R-SECONDLEVEL / R-UPPERBOUND), live caveats.
  Chain green after. No status flips (the pose itself is
  untouched — the crossing remains the target; only the ROUTE to
  its safe half changed).
- MEMORY NOTE REQUIRED at close: the standing memory line "THE
  OBJECT OF RECORD: pairwise-overlap cap below a^2/n ... T3 then
  closes with 89 bits margin" is now FALSE and must be rewritten.

## Audit judgements

- **This is the round-28 P0 pattern one level deeper**: a
  coordinator-banked "named next object" survived one round before
  a pilot found the object slip — and the correct cap was banked
  in-repo all along (the campaign's own KEY LEMMA). CATCH-24A
  subtraction is exemplary: the pilot explicitly demotes its
  headline to "a corollary of a PROVED node" and claims only the
  audit + attainment + consequences.
- **LB1 is the round's genuine theorem.** The construction is
  simple in hindsight (the maximal-core pencil), admissible at
  every posed row, and converts the banked upper bound T <= r+1
  from "bound" to "value". The safe half now has a two-sided
  window: B_ca^far(k+2^34) in [2^39.9773, 2^128).
- **The pilot's own misses are load-bearing and honestly scored**:
  PR-7 (it registered the same wrong cap it was auditing — caught
  by its own exact table), R3(C) backwards (the monotonicity
  direction), and the discovery that the dead object sits in a
  CRITICAL node's statement (raising the stakes) scored as its own
  prediction miss.
- **The T3-guard skip inference is properly quarantined** as
  inference-not-measurement (the round-29 21,832-census "0
  violations" may be largely vacuous — the skip fraction is a
  cheap follow-up worth one targeted run).
- **Cross-pilot note**: (OV)/(NEWCAP) from bank 1 (type-2, w*
  window) and LB1 here live on DIFFERENT objects (list-side w*
  vs far-CA slope overlap) — no contradiction; both narrow the
  same endgame from opposite sides. The reconciliation paragraph
  goes in the round close.

## Follow-ups filed (not executed)

- R-UPPERBOUND is the new safe-half anchor (round 32): a
  code-theoretic upper bound on B_ca^far(k+2^34) with target
  window [2^39.9773, 2^128); the overlap-statistics door is closed.
- R-LINEDEGREE == the banked T2/(RR2) bottleneck — unify the two
  residual registers under one name at the next mint.
- The T3-guard skip-fraction measurement (one run, cheap).
- Mint candidates: LB1 (+ its tightness corollaries) as a PROVED
  node; S3 as a scope lemma on any future Fisher-type route.
