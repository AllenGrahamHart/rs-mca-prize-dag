# Mystery briefs — six conversion asks (2026-08-01)

Six briefs, one per remaining "mystery-tier" red on the critical board. Each
asks the same question: **can this problem be decomposed into a finite case
program of the kind this repository has repeatedly closed?** The reader is
assumed to be a strong mathematician with no prior exposure to this project;
each brief is self-contained, with repository pointers for depth.

**Live repository (single source of truth):**
<https://github.com/AllenGrahamHart/rs-mca-prize-dag> (branch `master`).
The critical DAG is `dag.json` (statuses: PROVED / CONDITIONAL / TARGET);
each node has a folder `critical/nodes/<id>/` or `background/nodes/<id>/`
with `statement.md`, `proof.md` or `attack.md`, and machine verifiers
(`verify*.py`, exact rational/integer arithmetic throughout).

## The conversion pattern (what "success" looks like)

Three conversions this project has executed, as templates:

1. **K3 / m2 (the endpoint-map campaign).** A monolithic barrier
   ("cancellation") became: Galois inner-degree cases `{2,3,4,6,10,12}` →
   stabilizer rows `(r,delta)` → skeleton families → six-orbit symmetry
   partitions of 15 matching cells → per-cell exact Groebner/resultant
   deletions in named quotient algebras. Every leaf is a bounded exact
   computation with a pre-registered falsifier; composition nodes weld the
   leaves back into the classification. Status: the negative-parity
   coordinate sector fully closed; the whole inner-degree classification is
   within reach. See `background/nodes/rate_half_kb_m2_r4_*`.
2. **dli slots (partial conversion — briefs 1-2 ask to finish it).** A
   single opaque floor conjecture became ten mechanical slot-emptiness
   TARGETs (`dli_wcl_slot_*_emptiness`) plus two calibrated heads. The
   mechanical part is fleet-sized; the heads are briefs 1 and 2.
3. **E1 payoff ladder.** An unbounded-looking profile space became an exact
   ladder of 271 eligible profiles, each with a sharp sufficient cap
   `floor(2E/M)`, paying into an aggregate budget `P <= K - B* - 1`. The
   key move: **replace per-case emptiness by a budget the cases pay into**
   — closure of the worst case measurably loosens the requirement on the
   rest. See `notes/E1_PROFILE_WEIGHT_PAYOFF_LADDER.md`.

A successful answer to any brief specifies:

- a **finite index set** of cases (with the enumeration proved complete);
- a **per-case decision procedure** that is bounded exact computation
  (integer/rational; no floats, no unquantified asymptotics);
- a **composition theorem**: how the cases reassemble into the target
  statement (or into a budget that implies it);
- a **falsifier per case** and one global falsifier, pre-registered.

Partial answers are valuable: a correct finiteness/enumeration theorem
without the per-case procedure, or a budget reformulation without the
enumeration, each unblock a fleet of worker-agents on this side.

## Ground rules (hard-won; please respect them)

- **Check the death ledger first.** Each brief lists refuted ancestors and
  withdrawn claims. Do not resurrect a refuted form with cosmetic changes;
  strengthenings must state why the refuting instance no longer applies.
- **Exact arithmetic only.** Every claim this project banks is verified in
  exact rationals/integers. Proposals whose cases are decided by "numerical
  evidence" will not be accepted as case programs.
- **Constants explicit.** No `O(.)` without a named constant and a stated
  domain where it applies.
- **Falsifier-first.** A pose without a pre-registered falsifier is
  planning prose, not a conjecture, in this project's discipline.

## The briefs

| # | file | node | one-line mystery |
|---|------|------|------------------|
| 1 | `BRIEF_1_dli_c1r3_gated_envelope.md` | `dli_c1r3_gated_envelope_bound` | why does the extended-ledger envelope `E-1 <= 4r(1+W_ext)` hold on official-gated rows? |
| 2 | `BRIEF_2_dli_c2pp_joint_reserve.md` | `dli_c2pp_joint_reserve` | why is the joint staircase loss within 21 bits of the iid product? |
| 3 | `BRIEF_3_xr_highcore_collision_count.md` | `xr_highcore_collision_count` | why are there at most `8n^3` high-core colliding slopes (and `16n^3` mismatch total)? |
| 4 | `BRIEF_4_xr_lowcore_spread_heart.md` | `xr_lowcore_spread_heart` | why are there at most `8n^3` low-core spread slopes? |
| 5 | `BRIEF_5_f2_growing_order_myerson.md` | `f2_growing_order_myerson` | Myerson-type equidistribution at growing subgroup order, at astronomically weak tolerance |
| 6 | `BRIEF_6_rate_half_list_adjacent_crossing.md` | `rate_half_list_adjacent_crossing` | locate the ordinary-list crossing `a_L(C)` field-dependently |

Upstream context (the canonical project repo is `przchojecki/rs-mca`): briefs
1-2 have **no upstream counterpart** (OURS_ONLY in
`notes/correspondence/JOINT_CROSSWALK.json`); 3-4 overlap his open
`prob:mca-spread-routing` (grande_finale v4); 5 is IDENTICAL to his open K2
"row-sharp Q atom" (Sidon-Fourier payment); 6 overlaps his Lane L
`prob:list-completion`. None has an active upstream attack as of 2026-08-01.
