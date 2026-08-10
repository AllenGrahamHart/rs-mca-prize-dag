# BAND CHILD 2 (RH-AC): locate the adjacent crossing at the razor rows

- **status:** TARGET
- **parent:** `rate_half_band_closure` (req, gate all)
- **created:** 2026-08-09, the user-directed band decomposition
  (notes/band_decomposition_plan_20260809.md); pose adopted from the
  round-27 (RH-AC) draft with the decomposition ratification

## Statement (RH-AC, the pose of record; quantifier WIDENED 2026-08-10, e-axis WIDENED same day)

At every admissible row with n = 2^41, k = 2^40, **q = p^e (p prime,
e >= 1; exactly six strata e in {1,2,3,4,5,6} are admissible — the
round-31 stratum lemma), q = 1 mod n, 2^167 < q < 2^256** — the
entire undetermined range;

[E-AXIS WIDENING (2026-08-10, coordinator, executing the F4 ruling
per its own terms — "the audit decides the fork"): the pose read
"q prime". The round-31 rh_e_axis_audit found: (i) 13 of 14
instruments in the located-crossing stack are field-general BY THEIR
OWN PRINTED HYPOTHESES (inventory with file:line in the pilot
REPORT); (ii) the ONE primality-using instrument (the A=1
exceptional-core Legendre router) is UNREACHABLE by extension rows —
the PROVED rate_half_residual_prime_field_collapse contrapositive
puts every admissible extension row outside the residual-budget
window [2^167, 2^167+2^129) that is that machinery's sole territory;
(iii) the widening is FINITE: e in {1..6} exactly, with per-stratum
p-windows, and char = p > n = 2^41 on every admissible row (the
three sub-2^41 candidates at e=6 are all composite) — so every
degree bound in the Hankel/pair-Lagrange reductions holds with
primality never needed; (iv) the O3 import is VERIFIED FIELD-GENERAL
by the coordinator against the primary source: ABF26 Theorem 4.9
states the unique-decoding CA bound ([BCIKS20, Thm 1.4]:
eps_mca = eps_ca <= n/|F|) for RS[F, L, k] over an arbitrary field
(and Thm 4.8 "any linear code", Lemma 4.6 "any F-additive code") —
the HD1 bracket-top import carries no primality hypothesis; (v) the
first extension-field supply measurement in-repo finds NO EXCESS at
the analogue of the exhibited razor row (the only small-scale excess
is the full-multiplicative-group degeneracy D = F_q'^*, unreachable
at n = 2^41 since 2^41+1 = 3*83*8831418697); (vi) sub-2^167 was
already family-uniform in e, so this widening removes the
discontinuity at 2^167. STANDING OBLIGATIONS: O6 — any future
far-CA UPPER bound must not use "F_q has no proper subfield"
(pre-registered falsifier: a subfield-structured configuration
beating the prime-field maximum at matched (n,k,a)); O7 — the
prime-only evidence base (the 21,832-configuration census, the
collinearity census, F_LMAX/F_SSPARSE ladders) is flagged for
extension-field re-runs (the pilot's ffq.py field layer makes this
possible for the first time). The round-30 F4 flag below is
RESOLVED by this widening.]
below 2^167 the crossing is PROVED (the wave-10 staircase), and the
razor slice (2^255.9, 2^256) remains the hard corner — locate the
exact adjacent crossing a_RH(q) of (RH-ADJ):

[QUANTIFIER WIDENING (2026-08-10, coordinator, executing the
ratified tiling intent): the creation pose read "q prime in
(2^255.9, 2^256)" — razor rows only. The round-28 mca_safe_rewire
audit proved the decomposition's children did not tile the parent's
quantifier (rows with q in [2^167, 2^255.9] were located by
nothing — the E7 SCOPE SEAM flag on adjacency_closing). The parent's
consumers quantify over ALL admissible q; the sub-2^167 range is
proved; this child must own the rest. The widening EXPANDS this
node's obligation: the residual-budget interval [2^167, 2^167+2^129)
is exactly the apolar target's territory (budgets {2^39, 2^39+1}),
and (2^167+2^129, 2^255.9] carries the same bracket
[k+2^34, 3n/4 for q >= 2^169, n below] with no located crossing.
The E7 flag is RESOLVED by this widening, same day, recorded on
both nodes.]

```text
B_mca(a_RH) <= B*(q) = floor(q/2^128) < B_mca(a_RH - 1),
a_RH in [k + 2^34, 3n/4]          (the PROVED bracket).
```

The binding term is S_sparse alone — B_ca^far is free at razor rows
(B* ~ 2^128 >> n; the Hankel layer discharges the far-CA half) — so
the open content is exactly

```text
min { a : S_sparse(a) <= floor(q/2^128) }.
```

**[THIS PARAGRAPH IS FALSE — round-28 P0 correction below,
coordinator-verified from primary text: the Hankel layer's scope is
r < 2^39, i.e. a > 3n/4 ONLY; on the open bracket [k+2^34, 3n/4)
the far-CA term is not discharged and is in fact BINDING (the
PROVED simple-pole floor's pair is column-far, payload
B_ca^far(k+2^34-1) >= 2^216 vs B* = 2^128). The open content is
the FAR-CA crossing.]**

**No random-word quantity may appear in this statement** (the
round-27 forced correction: FLOOR v2 fell to its own falsifier via
the max-vs-mean type error; its four survivals were zero-power).

Named candidate endpoints — no discriminating evidence held:
- **(RH-AC-lo)**: a_RH = k + 2^34 (the quotient floor is tight);
- **(RH-AC-hi)**: a_RH = 3n/4 (the half-distance pincer HD1 is tight).

The determined-region ratio extrapolation (~2^38.9, near -hi) is a
heuristic across a mechanism change, labelled as such.

## Known structure at creation (round 27, all coordinator-replayed)

- Lower end COUNTING-EXHAUSTED: the next floor rung is 11.87 bits
  short with a provably tight normalizer; the simple-pole conversion
  goes lossless as q grows; no counting argument crosses n/log2 q.
- Upper end GATED by residual budget 2^39+1: diagnosed to the unit
  (one slope past the provable incidence limit; the m=1 fence);
  evidence-grade TRUE on the forced prime-field axis; proof needs
  the APOLAR ORIGIN. Closing it extends the bracket top from
  q >= 2^169 to q >= 2^167 + 2^128 [PRECISION FIX 2026-08-10,
  derived independently by BOTH round-28 pilots (mca_safe_rewire
  and apolar_origin) under quarantine: the sliver
  (2^167, 2^167 + 2^128) is budget 2^39's own interval, so "all
  q > 2^167" needs the budget PAIR; the 2-bit extension figure
  survives exactly (2^169/(2^167+2^128) = 4.000000)].
- Supply flank censused: THEOREM CAP is slack-0-scoped; the
  arbitrary-word maximum's scaling is the one undetermined number
  (named decisive run: the Modal-class n=32 t=1 maxscan).

## Falsifiers (pre-registered, round 27, with power controls)

- **F1** (high power, fires against -lo): push the quotient-remainder
  floor's razor reach beyond 2^34 - 1.
- **F2** (fires against -lo from the safe side): exhibit one received
  word y and razor row with N(y, k+2^34; q) > floor(q/2^128).
- **F3** (ZERO-POWER DECLARATION): any random-word or window-law
  count check at q < 2^128 has no power over this pose — it measures
  the mean object. This guard is load-bearing text.

## Consumer bars (CATCH-24C, round-27 verified)

- `adjacency_closing`: needs the LOCATED crossing (adjacent certified
  indices — the moving bar). The full pose serves it.
- `mca_safe`: needs the safe half AT THE LOCATED INDEX — the SAME
  moving bar, not a weaker one. (ROUND-28 CORRECTION, 2026-08-10:
  the 2026-08-09 reading "a_safe is textually free, so PROVED HD1
  discharges the bar at q >= 2^169" is WITHDRAWN. a_safe is unbound
  in mca_safe's own prose but bound by its consumers — the
  unsafe-side claim of record is stated at a_safe - 1 and mca_grand
  must EXHIBIT the crossing. HD1 is an upper bracket END at 3n/4 and
  B_mca is nonincreasing, so it bounds nothing below 3n/4. Reductio:
  a free a_safe would be discharged unconditionally at a = n by the
  PROVED mca_full_agreement_endpoint (FA1: B_mca(n) = 1), with no
  field floor at all — strictly stronger than HD1 and obviously not
  what the consumer needs. The premise-weakening surgery is RETIRED
  as unsound.)
- `list_adjacency_closing`: no longer consumes this content (owner
  moved at wave 10).

## Round-28 addendum (2026-08-10, coordinator-applied on replay: maxscan_algorithm — the named supply-side computation EXECUTED BY ALGORITHM; the delta=1 branch COLLAPSES)

**The wall broke by algorithm (the BBM pattern, second instance):**
the n=32 t=1 delta=1 whole-word-space maxscan priced "Modal-class,
out of stdlib reach" ran in 4 minutes / ~130 MB on one core, via
(i) SIGNAL SEPARATION (the comparator is the plateau 6435, so mean
line-weight up to ~20 is harmless — q ~ 3e7 suffices, collapsing
RAM to one dense counter) and (ii) THE ANTIPODAL IDENTITY (pairing
mu_n into antipodal pairs makes e2 depend on the sign vector only
through P^2 at alpha=0 — the subset space streams in N/2
increments). A mid-run PARITY THEOREM then reached n=64.

**THE VERDICT (delta=1 branch DECIDED — COLLAPSE at four scales,
char-0 exact, coordinator-replayed identical at n=8/16/32):**
surplus over the slack-0 plateau +1.000 / +0.394 / -1.705 / -7.270
bits at n = 8/16/32/64 — monotone, accelerating, crossing below
the plateau between n=16 and 32, ~12 bits short of the razor need
and moving away. The round-27 conflict is RESOLVED on this branch.

**PARITY THEOREM (proved; mint candidate):** splitting the
antipodal pairs by index parity, the odd part of E(S, sigma)
factors as zeta*X*Y with X, Y supported on a Q-basis of Q(omega);
hence E lands in Z[omega] iff S lies entirely in one parity class.
Corollary: only strata s <= n/4 contribute to the antipodal
targets (a 155x exact reduction at n=32; the enabling structure at
n=64). Closed form for the |S|=1 family, tolerance 0 at four
scales: STRAT_1^max(n) = (M+2)*C(M/2-1, M/4-1), M = n/2 — the
round-27 antipodal-pair-locator family, now exactly counted, dying
on its own (ratio to plateau 2 -> 7.3e-4).

**Two-field discipline held:** MAXSCAN_0(32) = 1988 identical at
q=30000001 and q=30000193 (mod-q), char-0 value 1974 confirmed
three ways with the 14-unit collision background decomposed by
stratum; alpha=0 is the argmax at n=8/16/32 (off-axis families
strictly below in both fields).

**HONEST RESIDUALS:** (i) the MAXIMAL-SLACK curve (arbitrary
received words; the round-27 sampled values 67 > 46 at n=16) is
NOT directly decided by the delta=1 collapse — it remains
sampled-only; the collapse plus the parity theorem's recursion
note (E on one parity class is itself an e2 one level down — the
route to n=128) make the same fate likely but UNMEASURED; (ii)
alpha=0-is-argmax at n=64 is assumed, not scanned; (iii) the full
(alpha, beta) exhaustion at n=32 is now OPTIONAL and cheap — the
pilot's MODAL_REQUEST.md prices it at ~8-28 core-hours (<$5) with
four cross-check gates — it upgrades the argmax claim to
by-exhaustion but does NOT gate the collapse verdict. Pilot
disclosures: 2 registered misses reported first (the background
model over-dispersed; the reachable-point call too pessimistic);
one compute-law near-violation caught and undone by the pilot
itself (an unguarded pipeline stopped before yielding output).
Source: notes/pilots_20260810/maxscan_algorithm/ (REPORT.md,
FABLE_AUDIT.md; E_exact ladder coordinator-replayed identical).

## Round-28 addendum (2026-08-10, coordinator-applied on replay: apolar_origin — the theorem did NOT land; the mechanism, three theorems, and a third of the sharp face did)

**HONEST HEADLINE: neither residual budget closed; both stay open,
status unchanged.** And a mandate correction (CATCH-24A, the fifth
instance): the "apolar origin" is NOT a missing ingredient — the
Hankel suite already names the apolar generator and the
catalecticant (rate_half_ca_hankel_minimal_index_budget), already
names the residual gate verbatim ("a rigidity theorem for this
rational normal kernel curve together with its Hankel/apolar
origin"), and the m=1 fence's own statement says the failure
survives "even after imposing core-freeness and the full
Hankel/apolar origin." The QMU/QMP quotient nodes (PROVED) already
run the minimum-support-uniqueness species of argument on the A=1
core-one face — the round-28 mechanism is a PORT to the full
strict A=3 pencil, not an invention.

**What landed (all coordinator-replayed byte-identical):**
**(1) THE MECHANISM C** (min-weight coset uniqueness legal on both
official profiles with margins exactly 3 and 1; slope-to-support
injectivity C1; the type-1/type-2 dichotomy C2; T_1 <= e+1 C3) —
it separates both banked certificates with no linear algebra (the
m=1 fence: all six numbers exact; the N=28 design 9-line: refuted
with contradiction margin exactly 6, matching nullity 0 without
touching the Hankel system).
**(2) CYCLOTOMIC EXCLUSION AT OFFICIAL SCALE (R3, new theorem):**
by C1, coset-structured root sets force T <= N/rho = 4 at the
official A=1 half-distance profile — against a target of 2^39+1,
margin 549,755,813,885. Round-27's one field-independent threat to
budget 2^39+1 is now dead AT THE OFFICIAL PARAMETERS BY PROOF
(previously: small-scale census only). The A=3 family is empty by
divisibility.
**(3) THE w* WINDOW (new):** the joint support is forced into
[4m+2, 8m-2] — killing the naive clean case w* <= rho+1 (empty),
a self-caught vacuous first theorem.
**(4) THE PER-STRATUM CLOSURE (the bankable partial):** T <= rho+1
on the strict e=m endpoint whenever O=0, m >= 2, and w* <= a_max(m)
with a_max/m -> 16/3 — asymptotically ONE THIRD of the admissible
w* range. The m=1/q=17 violation is excluded by explicit
hypothesis (m >= 2; q=17 forces m=1), as the brief required. The
closure does NOT move either budget: the average configuration
sits at large w* (~7m-1 > 16m/3).
**(5) THE RECIPROCAL-LOCATOR NORMAL FORM:** extremal type-2 slopes
are exactly points of {P_S = [1/(sigma'_W(x) sigma_S(x))]} on the
pencil line. The structured collinear families (rho+1 points,
present at EVERY field — the flat 840 count that falsified the
pilot's own registered heuristic) are killed by the banked
counting layer; everything else is SPORADIC and dies with q
(measured 0.000 per word at q >= 97). **The q=17 fence violation
is now mechanically located: one sporadic collinearity, exactly
its three type-2 supports.** Official-scale sporadic heuristic
q^{-(3m-2)4m} — nil, FLAGGED AS HEURISTIC, not proof.
**(6) THE DISJOINT-SUPPORT FENCE (R4):** A <= rho and T*rho <= N
— one criterion refuting both banked certificates ((4m+1)(4m-1)
<= 16m only at m=1; the 9-line via A = 9 > 3).

**The remaining gap, sharpened:** the unclosed stratum is
large-w*, where the mass sits; the sporadic-collinearity heuristic
is the shape of what a full proof must control. Pilot record: the
uniform theorem registered at miss-likely and it missed (P10 hit
as a registered miss); A2's heuristic falsified at every field —
producing the structured/sporadic dichotomy, the session's best
finding; the D4 sliver catch converged with mca_safe_rewire's
under quarantine (applied above). Source:
notes/pilots_20260810/apolar_origin/ (REPORT.md, FABLE_AUDIT.md;
d2_scan/d6_stratum/d5_sporadic coordinator-replayed identical).

## Round-28 addendum (2026-08-10, coordinator-applied on replay: ssparse_endpoints — P0: the pose's reduction CORRECTED; both falsifiers silent; the endpoint evidence lands hard on -lo)

**P0 (FORCED CORRECTION, coordinator-verified from primary text):
the "binding term is S_sparse alone" reduction — inherited from the
round-27 (RH-AC) draft — is FALSE on the entire open bracket
[k+2^34, 3n/4).** Three primary-text facts: (1) the Hankel far-CA
layer's own scope hypothesis is r < R/2 = 2^39
(rate_half_ca_hankel_fullrank_branch:10, split_pencil_equivalence:
44-46 — verified verbatim), i.e. a > 3n/4 ONLY; at razor rows
B* ~ 2^128 >> 2^39, so the layer never touches the bracket
interior. (2) The PROVED simple-pole floor's received pair is
COLUMN-FAR (its own proof establishes no code explanation on more
than k positions), so its payload lands in B_ca^far — measured by
exact integer replay: B_ca^far(k+2^34-1) >= 2^216.0000 vs
B* = 2^128, 88 bits inside unsafe. (3) The rider reduction needs
L_2 at 2^35 << k — hopeless there. **THE OPEN CONTENT OF RH-AC IS
THE FAR-CA CROSSING on [k+2^34, 3n/4); S_sparse is dominated.**
Own-repo grep: nothing in-repo carried this correction before.

**F1 DOES NOT FIRE — and the mechanism space is now EXHAUSTED, not
merely unsearched:** seven attack surfaces enumerated and priced
(the exact rung lattice over all N = 2^i <= 256 x all legal d, both
families, with N >= 512 closed by a pruning theorem; the non-2-power
scale EMPTY by divisibility; depth d >= 2 dead twice — admissibility
scaling AND the structural additive/multiplicative collapse, largest
(a_0,a_1) class 4-9 vs the 2519 needed; rotation exponents closed
exactly at d+1 constrained coefficients; hybrid/rider/overflow
priced dead; the pilot's own mid-run subgroup route closed exactly).
Max admissible reach over EVERYTHING: **exactly 2^34 - 1**, at the
printed rung only, margin 114.6503 bits (coordinator-replayed).
**(RH-AC-lo) HARDENS from "no discriminating evidence" to
"mechanism-space-exhausted floor".** F2 does not fire (priced
unreachable BEFORE attempting; the scaled sharp form F_COLL is
9.1x under the scaled budget at the one meaningful cell).

**THE ENDPOINT VERDICT (margin ladder banked in the report):**
best current estimate **a_RH(q) = k + 2^34 + O(1)** — the 114.65
bits of family slack buy 0.65-3.09 units of sigma against the
measured max-profile decay; the three separating scaled cells all
track the -lo image; and — TRANSPORT-FREE ARITHMETIC — **(RH-AC-hi)
requires the max list profile flat over 532,575,944,705 consecutive
agreements at average decay <= 2.15e-10 bits/unit, a factor 2^40.11
below the mean rate.** -hi is not a rival endpoint; it is a demand
for 2^40-fold flatness. Caveats stated: the decay measurement is
scaled across a mechanism change with a NAMED downward bias; the
2^40 flatness figure is not.

**CONSUMER CONSEQUENCE (FLAGGED, not applied):** with P0 in place,
the safe half at a = k + 2^34 is a far-CA problem, and
adjacency_closing's moving LOWER bar would be met exactly by the
already-PROVED floor at a - 1 — IF the crossing is located at
k + 2^34. **THE NAMED NEXT OBJECT: an upper bound on the max list
profile just above sigma = 2^34** — not the sparse coupled system.

Pilot record: 11 HITS / 2 MISSES reported first (incl. F_COLL
10-34 vs registered <= 4 — the locator set carries real collinear
structure, 7-9x random, though 2^126 short of F2's need) / 4
declared deviations; ESC-1 registered AS A MISS before running
(the brief's difference-form escape was ill-posed against the max
decomposition — the corrected escape 6/6); one disclosed
compute-law breach (an empty heredoc, no program ran; 13/14
compliant); two wall-hits re-scoped rather than extended. Replays:
d1_rungs + d4_margins + escapes green (114.6503 / -11.8737 / the
ladder reproduced). Source:
notes/pilots_20260810/ssparse_endpoints/ (REPORT.md,
FABLE_AUDIT.md; data/).

## Working hypothesis of record (2026-08-10, adopted at the round-29 launch with user endorsement of the round-28 verdict)

**a_RH(q) = k + 2^34 + O(1)** — (RH-AC-lo) plus a small constant is
the working hypothesis; (RH-AC-hi) is DEMOTED from candidate to
refuted-modulo-transport (the 2^40.11-fold flatness demand). The
falsifiers F1/F2/F3 remain armed unchanged (F1's firing would still
kill the hypothesis; the mechanism-space exhaustion makes that a
new-mathematics event, which is exactly what a falsifier should
price). The open theorem target under this hypothesis: the
max-list-profile upper bound just above sigma = 2^34 (the round-29
list_profile_bound brief).

## Round-29 addendum (2026-08-10, coordinator-applied on replay: list_profile_bound — no UB landed; the target TRANSFORMED into one exact inequality; a round-28 transport REFUTED)

**THE CONSUMER-BAR CORRECTION (CATCH-24C, sharpens the working
hypothesis's operational meaning):** the round-28 flagged
consequence ("the PROVED floor supplies the unsafe half IF the
crossing lands at k+2^34+c") holds ONLY AT c = 0 — for any c >= 1
the required unsafe index k+2^34+c-1 exceeds the floor's
mechanism-space-exhausted reach of 2^34-1, so every c >= 1
re-opens the unsafe half and demands a NEW floor. **c = 0 is the
only value that serves adjacency_closing.** Sharpest honest
bracket on c: [0, 532,575,944,704] (the HD1 top, unbeaten).

**A ROUND-28 TRANSPORT REFUTED (the q-ladder miss, reported as
such):** the round-28 decay figure was transported as a RATIO
(0.6865 * log2 q); the three-field exact ladder shows F_LMAX at
the cell is a q-INDEPENDENT ABSOLUTE constant (7/7/7 at
q = 17/41/97; decay exactly 2.8074 bits; the ratio falls
0.687 -> 0.425 as a saturated cap must). The ratio transport
overstated the razor decay by 62.6x; the corrected absolute
transport gives c ~ 32, not c ~ 1. ALSO: F_LMAX and B_ca^far are
NOT equivalent objects (measured: one q-independent, the other
grows 17/37/51) — the "equivalently" in the round-29 brief was
wrong. AND: the round-28 "0.1451 -> ~217 units" line has a 91x
two-readings discrepancy — DO NOT QUOTE until resolved. AND: the
(FLAT) falsifier and (RH-AC-hi)'s 2^40 flatness demand are NESTED,
not equivalent — the -hi refutation supplies NO part of the UB
target (power ratios 2^30.8-2^38.6).

**THE STRUCTURE THEOREM (the instrument survey's real finding):**
all seven in-repo far-CA instruments share ONE domain for ONE
reason — each is the unique-decoding threshold 2(n-a) <= n-k,
i.e. a >= 3n/4, of the difference code, seen seven ways. The open
bracket [k+2^34, 3n/4) is precisely its non-uniqueness region;
0 of 7 reach below. The unique threshold-crosser
(rate_half_list_integer_johnson_safe_anchor, PROVED, reaching
0.70711n) bounds L_1, not B_ca^far. The Hankel moving-kernel
branch is ABSENT (the a > 3n/4 discharge is itself incomplete —
a residual sentence, no node).

**BANKED THEOREMS (validated 0 violations / 21,832 exhaustive
column-far configurations; T4 tight at its threshold):** T1
SUNFLOWER RIGIDITY (bad-slope pairs partition into lines; all
pairwise intersections on a line coincide; petals disjoint;
m_P <= 1 + r/(a - e_P)); T2 STRATIFIED RIDER (halves the banked
(RR2) exponent — L_2 -> L_1 — and replaces the blanket r+1 by a
per-stratum weight = 1 at the minimal core; changes nothing about
reach, ~2.7e14 bits above target, stated plainly); T3 FISHER
SUB-STRATUM (pairwise overlaps <= theta < a^2/n give
#slopes <= (a-theta)/(a^2/n - theta): at sigma = 2^34, <= 32 with
123 bits margin at theta = n/4; <= 2^39-2^27+1 with 89 bits at
theta = a^2/n - 1); T4 elementary thresholds (one-line at
a >= 5n/6; Fisher-finite at a/n > 0.8202 — both worse than the
banked 3n/4, reported as re-derivation).

**[THE FOLLOWING T5 PARAGRAPH IS FALSE — round-31 rh_overlap_cap refutation, coordinator-verified against the banked (AP3) and KEY-LEMMA caps and the replayed LB1 construction; see the round-31 overlap-cap addendum below. The cap constant k-1 was the WRONG OBJECT (single-word list cap), the correct column-far ceiling is a-1 and it is ATTAINED; the 0.999748 coincidence is an artifact; the named next object does not exist at any a in the open bracket.]**

**T5 — THE EXACT OBSTRUCTION (the number to carry forward):**
GAP_FISHER = (k-1) - a^2/n = 532,441,726,975 vs the open bracket
532,575,944,704 — **ratio 0.999748. The open bracket IS the region
where the MDS pairwise-overlap cap exceeds the Fisher threshold;
they end together.** THE NAMED NEXT OBJECT IS SUPERSEDED AND
SHARPENED: not "an upper bound on the max list profile" but **a
pairwise-overlap cap below a^2/n = 2^39 + 2^34 + 2^27 (exact
integer) at sigma = 2^34** — the moment it lands, T3 closes
(UB-far) with 89 bits of margin. No honest conditional UB exists
on the rider route (the required hypothesis is false, not
unproved — T6). The scaled-cell program is STRUCTURALLY INCAPABLE
of resolving c (bracket interior width 1 at n_s = 8; n_s >= 44
for ten interior points) and is DECOMMISSIONED for that purpose.

Pilot record: 14 HITS / 1 hard MISS + 1 partial (both its own
slips, disclosed with direction); a real bug in its own validator
caught and fixed WITHOUT weakening the theorem (1.68M spurious
violations diagnosed to a leaked-degree functional; 0 after);
CATCH-24A fired three times including against its own mandate.
Replays: d1_core (GAP_FISHER exact) + d2_sunflower (0/21,832) +
d3_ladder (the exact F_LMAX section identical; the sampled section
differs only by sample count) — coordinator-verified. Source:
notes/pilots_20260810/list_profile_bound/ (REPORT.md,
FABLE_AUDIT.md).

## Round-29 addendum (2026-08-10, coordinator-applied on replay: slack_recursion — the supply side does NOT close; it closes THE OTHER WAY, and the model is the casualty)

**The round-28 maxscan addendum's residual line ("the collapse plus
the parity theorem's recursion note make the same fate likely") is
FALSIFIED TWICE:** the recursion is KILLED (REC-STRONG false by
explicit counterexamples — 88/103 contributing nodes at n=32 mix
parity classes; only the weaker REC-BOX prune survives, measured
1.0/1.25/2.7, leaving n=128 Modal-class-dead and now valueless);
and the maximal-slack curve GROWS. **THE ARBITRARY-WORD MAXIMUM IS
NOW A THEOREM, pinned within one bit at every scale:** THEOREM A
(the PRODUCT WORD y = x^{-1} + c*x^{n/2}: agreement sets = exactly
the a-subsets with prescribed product -1/c; flat profile; count
C(n,a)/n — the classical Graham-Sloane prescribed-sum construction
realized as ONE explicit word, char-0, field-independent, OUTSIDE
the coset/dressing universe THEOREM CAP scopes) + THEOREM B (the
matching constant-weight distance-4 upper bound 2C(n,a)/n).
Surplus over the plateau: +1.222 / +4.352 / +11.424 / +26.461 bits
at n = 8/16/32/64 — **crossing the razor's +4.73..4.83-bit need
between n=16 and n=32**, and over-satisfying it by ~115 bits at
the razor's model scale. Exact at n=8 by 3-field exhaustion over
EVERY received word; verified at n=32/64 by criterion +
planted-subset checks, two fields.

**THE HONEST STING — A MODEL CRITIQUE, NOT AN F2 FIRING:** nobody
believes a 115-bit over-satisfaction transports; the correct
reading is that **the t=1 model rounds 27-28 measured is NOT a
faithful transport of the razor's supply question** — the razor
has t = 2^34 (t = M, the coset scale), where the constraint
universe differs. First coset-faithful data point measured exactly
(n=16, t=2: SLACK0 = 3 vs PRODW = 7, both formulas confirmed
against the coset picture); **the banked razor plateau C(127,64)
matches NEITHER coset-level formula, so the transport dictionary
needs the banked derivation before ANY razor-scale statement.**
THE NAMED NEXT OBJECT: fix the (t,M) correspondence, then re-run
the two-sided pinning in the coset-faithful regime. Also
corrected: the round-27 sampling frame under-measured by design
(frame gap 6.4x at n=16: in-frame max 111 vs sampled 67 vs true
715); the n=8 "5 vs 6" conflict dissolved (F_LIST vs F_SUBSET).
Mint package (Theorems A-D, proofs, harness) at
notes/pilots_20260810/slack_recursion/MINT_PACKAGE.md. Pilot
record: its OWN registered supply direction refuted by its own
measurement (the R6 fallback rule fired and was followed); one
disclosed no-op compute-law breach. Source:
notes/pilots_20260810/slack_recursion/ (REPORT.md, FABLE_AUDIT.md).

## Round-29 addendum (2026-08-10, coordinator-applied on replay: collinearity_object — the sporadic bound LANDS UNCONDITIONALLY on the top TWO THIRDS; the two round-28 sides unified as ONE identity)

**THE UNIFICATION (U1, proved + 1024/1024 two fields two N):** for
subgroup domains, P_S = diag(x/N) * L_T with T = (D\W)\S — the
reciprocal-locator set (apolar) and the direct-locator set
(ssparse) are THE SAME POINT SET up to a fixed collineation.
ssparse's 7-9x-random excess is a THIRD CLASS — a small-ambient
(a <= 4) floppy-regime artifact where the index map is not even
injective; at a >= 5 the excess VANISHES (max F_COLL = s+1 in all
1152 sampled configurations, six fields). The official ambient is
w* >= 2^39+2 — deep in the rigid regime. **The round-28 F_COLL
flag is RESOLVED as zero-power at official parameters** (the
pilot's own declaration, stated against its own headline).

**T4 (THE SPORADIC BOUND — unconditional, uniform in q):** if
RIG = a-1-2s >= 0, sporadic collinearities of {P_S} DO NOT EXIST:
three collinear points force two degree-2s polynomials to agree at
a > 2s points, hence a polynomial identity, hence
sigma_{S_i} | sigma_{S_1}sigma_{S_2} — every S_i lies in
G = S_1 u S_2 and the complements are pairwise-disjoint fibres of
a degree-k map, so M <= 1 + s/k <= s+1: EVERY collinear family is
a pencil (coordinator hand-verified the argument). With the banked
counting layer (SAT2-SAT4, verified verbatim): M <= m+1, hence
T <= 2m+2 <= rho+1 for every m >= 1 — contradicting SAT3. **On the
official profile the hypothesis reads w* >= ceil((16m+3)/3): the
TOP TWO THIRDS of the admissible window — exactly complementary to
apolar's (AO1) one-third.** The q=17 fence violation is explained
TO THE UNIT: the hypothesis fails by exactly one (2s = 6 = a), and
the forbidden boundary term is measured as 4*sigma_W.

**THE COMPLETE STRUCTURED CENSUS + THE SAFETY ANSWER: NO** — every
collinear family in the rigid regime (linear, mu_2-coset, dihedral
[a port: dihedral_quotient_stratum has the family in-repo],
non-Galois, cyclotomic, general degree-k) satisfies the d_x law
(zero violations), so the banked layer caps EVERY structured
family at M <= m+1. No structured family threatens the budgets.

**NEITHER BUDGET CLOSES — the three named residuals, exactly:**
(i) the tiling gap between the (AO1) band and T4's band is 1 OR 3
integers of w* per m (P11 miss: never 0); (ii) type-2 slopes whose
difference codeword is NOT minimum-weight — the normal form does
not apply, and the counting cap there is 5.04e22 vs the 2^39
target; (iii) m = 1. All three open; any one keeps both budgets
open. FOURTH independent derivation of the sliver constant; one
precision nit on the round-28 fix as banked here: the extension
factor is 4 - 7.28e-12 (4.000000 to six decimals, NOT exactly 4).
Pilot record: two self-caught bugs (a normalization-basis error
producing a false contradiction; a mislabelled violation counter
reported as a mislabel), one arithmetic slip corrected by its own
measurement, CATCH-24A subtraction on the dihedral family, and a
zero-power declaration against its own headline. Replays: d1_unify
+ d3_coverage IDENTICAL (the identity 1024/1024; the 12/12 (AO1)
re-derivation; the payoff arithmetic). Source:
notes/pilots_20260810/collinearity_object/ (REPORT.md,
FABLE_AUDIT.md).

## Round-30 F4 flag: the e-axis (q prime vs q = p^e) — FLAGGED, NOT RESOLVED

The round-30 seam hunt (notes/pilots_20260810/k3_chain_seams/,
finding F4) exhibits a NEW uncovered direction, orthogonal to the
round-29 s-axis flag: this pose reads "q prime", while the item-13
admissible family (notes/BAND_LANE_DEFINITIONS.md) is q = p^e, and
the sub-2^167 determination covers every admissible q. Exhibited by
exact integer arithmetic (replay:
notes/pilots_20260810/k3_chain_seams/exhibit_extension_rows.py):
p = 340282366920938463463374556854233333761 (prime), q = p^2 with
q.bit_length() = 256, q > floor(2^255.9) (INSIDE the razor slice),
v_2(q-1) = 42 so n = 2^41 | q-1, k = 2^40 — an admissible rate-1/2
family row that no child of rate_half_band_closure locates. A second
exhibit sits at q ~ 2^201. Nothing in-repo flags the exclusion
(own-repo grep banked in the REPORT). RESOLUTION SURFACED: either
(a) widen this pose to q = p^e (requires auditing which of the
rounds-27..29 instruments are primality-sensitive — the WP5 verdict's
"31-bit prefix charges" note suggests extension rows differ
materially), or (b) restrict the lane's family claim to prime q and
open a separate extension-row child. Until ruled, every consumer
reading "each admissible row" must count e >= 2 as UNCOVERED.

## Round-31 type-2 stratum addendum (2026-08-10, coordinator-audited)

**RESIDUAL (ii) RE-PRICED BY 10.61 DECIMAL ORDERS.** The round-31
rh_type2_stratum pilot (REPORT + FABLE_AUDIT in
notes/pilots_20260810/rh_type2_stratum/; coordinator hand-verified
the algebra and independently re-derived every ledger number):

- **(OV)** For every pair of distinct supported slopes,
  w* <= |S_gamma u S_gamma'| (the round-28 apolar union bound with
  the every-pair quantifier made explicit — a direction-reversal of
  banked material, not new arithmetic).
- **(NEWCAP), conditional on (SAT1)-(SAT4) with T = rho+2:**
  summing (OV) over all C(T,2) pairs through the incidence identity
  sum_{pairs} |S ^ S'| = sum_x C(d_x,2) and the SAT4 convexity
  minimum gives w* <= 2rho - (Lmin(O)+(T-1)O)/C(T,2), tightest
  universal form at O = 0: **w* <= 7m-1** asymptotically — the SAME
  7m-1 that the round-28 apolar bank computed as the location of
  the MEAN configuration and read as "does not move either budget."
- **THE SHARPENED LEDGER at m = 2^37** (exact, replayed +
  coordinator re-derived): a_max = 7m-1 = 962072674303; spend floor
  R+1-a_max = m+2; residual-(ii) cap = floor((9m+1)m/(m+2)) =
  **1,236,950,581,231** (banked figure was 50371909150701174915072;
  shrink 40,722,652,881x); AO1 = 1,236,950,581,233 vs rho+1 = 2^39:
  **residual factor 9/4 exactly.** The w* window share drops
  2/3 -> 5/12.
- **VACUITY LEMMA:** a = 8m-2 (where the old cap was evaluated) is
  vacuous for every m >= 2 — w* = 2rho forces pairwise-disjoint
  full-size supports, i.e. T*rho <= N, true only at m = 1 (the R4
  fence, now forced rather than assumed).
- **m = 1 IS STRUCTURALLY DISJOINT from residual (ii)** (proof:
  p in [3,3] and wt(kappa) = 9 - n_0 >= 9 forces j = 0) — the q=17
  fence contains none of this stratum; residual (iii) and residual
  (ii) do not overlap.
- **THE HONEST FRONTIER — (FR), the one missing inequality:**
  |S_gamma ^ W| <= ~2m against ALL of W at once (the max-vs-mean
  upgrade; (OV) gives it pairwise only). CAUTION: the l1_fpc5
  distance-only no-go ("support weights + pairwise overlaps cannot
  close this consumer") is an in-repo precedent from a sibling lane
  — if it transports, 9/4 is the CEILING of the combinatorial route
  and the next instrument is algebraic ((GNF) f_gamma polynomials
  or the Hankel pencil).
- **(GNF)** the generalized reciprocal-locator normal form
  kappa_x = f(x)/sigma'_Z(x), deg f <= wt(kappa)-(R+1), a port of
  the xr-lane RS duality basis, verified 280/280: j >= 1 does NOT
  break the normal form, it breaks UNIQUENESS (dimension j+1) —
  the honest reason T4 does not transport to this stratum.
- **SUPERSESSIONS:** the banked "counting cap there is 5.04e22"
  line (round-29, above) and the "2/3 of the w* window" share are
  SUPERSEDED by this addendum. The round-31 brief's "~39-order gap"
  phrasing was WRONG (coordinator's own error, conflating 2^39
  with decimal orders): the true gap was 11 decimal / 36 binary
  orders, now 9/4.
- **LIVE CAVEATS:** (NEWCAP) is conditional on (SAT3); falsifier F1
  (a realizable T = rho+2 configuration with w* > 7m-1) is live and
  unexercised (the census sampler never reached T > 3); (EQ)'s
  converse is sampled (121/121), not proved. No status flips;
  neither budget closes.

## Round-31 overlap-cap addendum (2026-08-10, coordinator-audited): THE SAFE-HALF ROUTE IS DEAD; LB1 REPLACES IT

The round-31 rh_overlap_cap pilot (REPORT + FABLE_AUDIT in
notes/pilots_20260810/rh_overlap_cap/) REFUTED the round-29 T5 named
object. Coordinator verification: the banked cap anchors quoted
verbatim ((AP3) s+t-r >= 1; the KEY-LEMMA graded consequence — max
joint pair agreement <= A-2, i.e. overlap <= a-1), the LB1 counting
argument hand-verified, d1/d4 replayed exactly.

- **OBJECT SLIP (CATCH-24C, on the round-29 bank):** T5's cap
  constant k-1 is the SINGLE-WORD list cap (Agr(z,c_i) ^ Agr(z,c_j)
  subset Agr(c_i,c_j)) — the wrong object. The T1 core E_P of a
  column-far pair is a CODEWORD-PAIR joint agreement; its correct
  ceiling is a-1, banked twice ((AP3); KEY LEMMA), and a-1 exceeds
  k-1 by exactly 2^34 at the razor.
- **THE CEILING IS ATTAINED — LB1 (new, unconditional):** for the
  razor row and every a in the open bracket, B_ca^far(a) >= n-a+1 =
  r+1: an explicit column-far pair (d_2 = 1_T, d_1 = -lam_j on T)
  whose bad-slope set is one full T1-line of r+1 slopes, EVERY
  pairwise overlap exactly a-1, unique witness each. Admissibility
  (LB1-C): n < (a-k-1) log2 q — holds at EVERY row of the widened
  quantifier q > 2^167 (margin 670,014,898,009 at the bottom; fails
  only below ~2^129). Verified exhaustively at (8,4,17) (46,656
  witness assignments — the hypothesis fails under every one) and
  at 6 more cells over 3 scales; the refutation STRENGTHENS with
  scale (RATIO_FAR -> 1.969231 at the razor).
- **SELF-DEFEAT:** a-1 > a^2/n for every 2 <= a <= n-2 — no cap
  below a^2/n exists at ANY agreement in the open bracket. The T3
  closure route (the "89 bits margin") is dead on the whole bracket,
  not just at sigma = 2^34.
- **THE 0.999748 IS AN ARTIFACT:** GAP_ALG = BRACKET - 1 -
  sigma^2/(2k) evaluated where sigma^2/(2k) = 2^27 is negligible;
  the two ends differ by 94,323,185,676 and with the correct cap
  the ratio is 1.032006. "They end together" is FALSE.
- **WHAT LB1 BUYS (the positive yield):** (i) the campaign's FIRST
  lower bound on B_ca^far at the safe index: B_ca^far(k+2^34) >=
  1,082,331,758,593 = 2^39.9773 — 88.02 bits below the 2^128
  budget; (ii) the banked upper bound T <= r+1 is TIGHT on its
  whole proved domain (B_ca^far(n-r) = r+1 exactly); (iii)
  B_ca^far(3n/4) >= 2^39+1, matching the D4-precision-fix budget
  EXACTLY — the residual budget 2^39 is UNATTAINABLE at a = 3n/4
  (the "one slope past the provable incidence limit" is a real
  slope, not proof slack).
- **S3 (new):** T3's hypothesis FORCES every bad slope to error
  weight s > a(n-a)/n = 2^39-2^27 — empty on 50.78% of the s-range;
  one slope at agreement >= 3n/4 + 2^27 kills it outright. And the
  round-29 "0 violations / 21,832 configurations" validation is
  structurally consistent with the T3 test being SKIPPED on most of
  the census (the guard theta*n < a*a fails on the planted
  maximal-core family); the skip fraction was NOT measured — flagged
  inference, not a claim.
- **RESIDUALS OF RECORD for the safe half:** R-LINEDEGREE (bound
  T1-lines through one slope by 2^88 — exactly the banked T2/(RR2)
  bottleneck, unmoved); R-SECONDLEVEL (the second Fisher level is
  ~2^10 FARTHER than the first — not the cheaper door);
  R-UPPERBOUND (the only remaining shape: a code-theoretic upper
  bound with target window [2^39.9773, 2^128) at sigma = 2^34).
- **CAVEATS LIVE:** LB1's razor step is a verified human proof
  (machine-checked arithmetic, exhaustive only at small cells);
  (16,8,9) returned a sampled negative (zero power); (16,8,10) not
  measured. No status flips; NEITHER half of RH-AC closes.

## Round-31 supply addendum (2026-08-10, coordinator-audited): the (t,M) dictionary lands — and the supply lane closes as posed

The round-31 rh_transport_dictionary pilot (REPORT + FABLE_AUDIT in
notes/pilots_20260810/rh_transport_dictionary/; the razor ladder
hand-checked by the coordinator, all quotes verified verbatim):

- **THE C(127,64) PUZZLE IS RESOLVED** by an exact integer identity:
  PLATEAU(n) = C(n/2-1, n/4) = QCORE(n, sigma=1) = C(n/M-1, k/M) at
  M = 2 (verified at seven scales). The round-29 model and the razor
  are two points of ONE family — (M,sigma) = (2,1) vs (2^34,
  2^34-1) — and only the plateau coincided.
- **THE ROUND-29 "t = M" IDENTIFICATION IS OFF BY ONE**: the banked
  qcore requires sigma < M (ww_lower_witnesses/proof.md:18,
  extremal at sigma = M-1). The step matters: sigma = 2^34 is
  itself a coset scale, exactly where the two coset families
  separate. THE LADDER AT THE RAZOR ROW: qcore at 2^34-1 =
  C(127,64) = 2^123.17; qcore at 2^34 = C(63,32) = 2^59.67 (a
  63.503-bit cliff); the CPW full-coset product-word family cuts
  the drop to 6.02 bits with C(128,65)/128 = 2^117.15 (exact
  integer) — 57.480 bits above qcore at the crossing index and
  **10.75-10.85 bits BELOW the need**.
- **THE "+115 BITS OVER-SATISFACTION" (round 29) IS RETIRED AS A
  SCALE ARTIFACT**: the same sigma=1 law at the razor's own n gives
  a 1.1e12-bit surplus — a quantity that moves ten orders under a
  scale change transports in neither direction. THE DIRECTION
  INVERTS: the faithful coset transport UNDERSHOOTS the need.
  Decisive small-scale datum: the first exact global maximum at
  sigma >= 2 in a structure-dominated field (n=12, q=37) is
  L_1 = 5 vs the naive C(n,a)/n transport's 41.25 — the sigma=1
  law dies at sigma >= 2 (the extra matching conditions are
  F_q-valued, not cyclic).
- **THE LANE LANDS ON THE LIST SIDE**: F_LIST is L_1 (the
  list-adjacent contract's own object), and the audited guard
  (literature map) FORBIDS the list-threshold-as-MCA-surrogate. So
  the supply lane CANNOT reach this node's open content without a
  proved CA/MCA conversion — **the missing dictionary entry is the
  CA/MCA CONVERSION, not more (t,M) entries.** (Candidate door,
  unverified: ABF26 Lemma 4.6's field-general eps_mca = eps_ca at
  delta < delta_min/2.)
- **POSITIVE CONFIRMATION OF THE BANKED CAP**: the char-0
  minimal-slack maximum is EXACTLY the qcore value at every 2-power
  n measured (the razor's regime) and fails off 2-powers precisely
  at the Lam-Leung boundary — the banked THEOREM CAP verified
  independently in its own stratum, with its domain hypothesis
  (2-power coset structure) shown load-bearing.
- **THE SLACK AXIS (Q6) is where all surplus lives**: the banked
  razor witness is slack-0, the stratum where the cap is tight;
  the measured surplus is entirely the climb to maximal slack.
- **Falsifiers armed**: F-CAP (char-0 2-power cap exact; untested
  n >= 32), F-CPW (the two-family ladder + sporadic excess +2),
  F-SIGMA1 (L_1(k+1) = C(n,a)/n exactly; verified n = 8, 12),
  F-OBJECT (a proved CA/MCA conversion re-prices the crossing-index
  supply from 2^59.67 to 2^117.15 — a 57.5-bit gap-anatomy change).
- **Zero-power of record**: no exact global max at 2-power n with
  sigma >= 2; nothing measures B_mca/B_ca^far/S_sparse; q window
  ends at 10^6 (regime membership transports; the 2^256 arithmetic
  does not). No status flips.
