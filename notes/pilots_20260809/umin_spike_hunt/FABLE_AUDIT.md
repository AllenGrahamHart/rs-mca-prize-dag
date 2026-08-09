# FABLE_AUDIT — umin_spike_hunt (round 26)

Coordinator: Fable. Date: 2026-08-09. Pilot: Opus (task a207e541edbcda674,
~101 min, 86 tool uses). Quarantine marker: ledger line 3872, observed.

## Verdict

**BANKED. This is the round's — and arguably the campaign phase's —
falsification event: CONJECTURE Z-CEILING's ratio form is dead on its
own pinned family.** The kill-or-confirm brief got its kill: both
registered outcomes fired (CRATIO > 2 at 119/124 cells; the N-decay
direction refuted 3.3x over the exhaustive N=16 record). The
instrument exceeded its brief — THEOREM RS makes the search an exact
arithmetic characterization (recall 1.000 by proof, confirmed 0
mismatches on an entire exhaustive band), converting a 47-cell sample
problem into a complete 2.12e7-prime census. The mechanism (kernel =
ternary part of an ideal; mass multiplies; RC pins U_min while N
grows) explains both why the constant grows and why round 25's
body-statistics verdict could never have seen it. The FLOOR stands
(0/292); the CEILING falls.

## Replays and independent verifications (all by me)

| what | result |
|---|---|
| the record cell p=4337074369, FOURTH variant (my stride-5 permutation + RBUCK=113 — internals disjoint from all three pilot derivations) | **AGREE**: TNUM 49692303616, NKER 551489; CRATIO recomputed 5.8131644 |
| the weight-5 witness, directly | my own code (theta of order 64 recomputed, all 32 sign patterns x 32 odd k at support {0,1,3,12,25}): **4 kernel witnesses found** — the weight-5 vector exists independent of the sieve |
| THEOREM RS proof | verified BY HAND: for odd k, j -> jk is a bijection of Z/N and x^{jk} = +-x^{jk mod N}, so g(x) = f(x^k) is ternary of the same weight with g(theta) = f(theta^k) = 0; the (=>) direction is banked THEOREM RC |
| the kappa=2 exhaustive sweep | the pilot's background sweep DIED INCOMPLETE at 186/266 when its session ended (declared 168/266 in the report; 186 on disk). **COMPLETED BY THE COORDINATOR** from the pilot's own resume machinery (run32.py done-set resume, 6 shards): [K2-FINAL] |
| escape anchors | the pilot's from-scratch record replay (89.1 s, third variant) covers the round-25 record; its N=8/N=16 ground truths agree with the reference enumerator 0 mismatches; its power control hit the banked AU profiles exactly (64/32/0/0) |

Not replayed: the full U <= 7 sieve enumeration (7.7M leaves — certified
by THEOREM RS + the two whole-band ground truths + the 2880 weight-5
hits' individual at-p re-verification, which the pilot ran for all 90
UMIN=5 primes); the 98-cell two-way BBM table (the pilot's own, 0
disagreements, same machinery I have four-way-verified at both records).

## Audit judgements

- **The falsification is real and over-determined**: an exact
  arithmetic characterization (proved two ways), a four-way-derived
  record, a directly-verified witness, whole-band ground truths at two
  smaller N, and 119 independent cells over the bar. Nothing rests on
  a single code path.
- **The registered-outcome discipline worked**: the kill bars were
  fixed in the brief before any computation; outcome 3's recall
  requirement forced the instrument design toward the iff, which is
  what made the census (and hence the kill) possible.
- **The pilot's own headline prediction MISSED (registered [1.75,
  3.05], measured 5.81)** and it says so first — the additive
  predictor was structurally wrong; the multiplicative ideal mechanism
  was found in the data and is labelled unregistered. This is the
  correct posture: the miss is evidence the result was not
  retro-fitted.
- **The checkpoint-resume catch (self-correction 4) matters**: the
  pilot noticed its escape "replays" had resumed from round-25
  checkpoints (a checksum, not a derivation) and re-derived from
  scratch. Without that, the escape suite would have been circular.
- **Honest incompleteness**: the kappa=2 sweep was declared partial
  in the report rather than papered over; the U=8 full census was
  correctly gated off by the pilot's own registered throughput
  threshold, with the targeted U=8/U=9 arm run instead (complete
  enumerations, output-restricted).
- **Round-25 is superseded, not impugned**: its report explicitly
  flagged that the SD-law could not see the spike process and named
  this hunt as the follow-on. The system worked across rounds exactly
  as designed.
- **Compliance clean**: quarantine held, compute law total (walls
  lengthened via RAMGUARD_TIMEOUT on documented batches), RAM
  discipline held, draft-only held (new ckpt files only, per the
  brief's explicit exception), no subagents.

## Corrections applied

- background/nodes/f2_z1_mass_knife_edge/statement.md — round-26
  addendum: the falsification (record, census, THEOREM RS, mechanism,
  what survives), the round-24 repricing and round-25 ladder verdict
  superseded, the F2-terminal implication SURFACED (the non-local
  smoothness input has no named route again). No status flip (the
  conjecture was addenda-recorded evidence, not a DAG node; census
  unchanged).

## [K2-FINAL] kappa=2 exhaustive band — completed by coordinator, MEASURED

All 266 distinct in-band M2 kappa=2 primes (= the full JOBS.k2band
list) now computed exactly: the pilot's sweep died incomplete at 186
when its session ended; the coordinator completed the rest via the
pilot's own resume-safe driver (run32.py, same shard assignment).
77 primes were computed twice across the two runs — with ZERO
conflicting values (identical TNUM/NKER both times), a free
consistency check. FINAL, measured over all 266: max CRATIO =
1.3887176890 at p=63361 (reproducing the round-25 kappa=2 record;
the only U<=7 prime p=33409 sits at 1.1535); ZFLOOR violations: 0.
The kappa=2 band does NOT approach the kappa=1 spikes — consistent
with RESSIEVE's finding that the band carries exactly one low-weight
orbit. The round-25 declared-post-hoc sweep is now CLOSED.

## Follow-ups filed (not executed)

- The F2 terminal's smoothness input is open again with no named
  route — a round-27-scale question, SURFACED to the user with the
  board summary.
- THEOREM RS + the RESSIEVE census machinery are mint candidates
  (self-contained, two ground-truth bands, power-controlled).
- The ideal-mass mechanism (TMASS >= (1+2^{1-U})^N sketch) deserves a
  proof pass — it is currently a mechanism with overwhelming
  numerical support, not a theorem.
- The N=64 band is now priced by the same instrument (the sieve
  scales; BBM does not — a new algorithm question, NOT urgent given
  the verdict is already decided at N=32).
