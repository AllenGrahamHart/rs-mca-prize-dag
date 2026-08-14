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
a_RH in [k + 2^34, 3n/4]          (the PROVED bracket; TOP
IMPROVED 2026-08-10 for q >= Q_9*2^128 ~ 2^232.65 by the Haboeck
staircase — a_RH <= a_m(q), razor rows a_94/a_95; see the
Haboeck-Johnson addendum and the round-32 staircase addendum below).
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
- **THE HONEST FRONTIER — (FR), CALIBRATED:** the original pilot's
  `|S_gamma ^ W| <= ~2m` phrase is arithmetically insufficient after
  `NEWCAP` moves the worst case to `a=7m-1`. The exact spend needed by
  the printed outside-capacity ledger is
  `p_req=floor((9m+1)m/(4m-1))+1`; on the official row this is
  `9m/4+1`, equivalently `|S_gamma intersect W|<=7m/4-2` for a clean
  locator. The old `2m+2` spend leaves an asymptotic `9/8` residual.
  This is still a max-vs-mean upgrade against ALL of W; `(OV)` gives
  only pairwise control. CAUTION: the l1_fpc5
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
  CA/MCA conversion valid beyond half distance. The specifically
  suggested ABF26/BCIKS unique-decoding door is now **RULED OUT BY
  SCOPE** by the proved
  `rate_half_unique_decoding_ca_mca_scope_fence`: its exact gate is
  `2(n-a)<=n-k`, equivalently `a>=3n/4`, while the whole live
  interval has `a<3n/4`. It recovers only the already-proved endpoint.
  A genuinely beyond-half-distance conversion would be new mathematics;
  **more (t,M) entries are still not the missing step.**
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

## Haboeck-Johnson safe-bracket addendum (2026-08-10)

The proved quadratic Johnson-range MCA theorem now supplies a direct
safe-side bound below `3n/4`; it does not use the fenced unique-decoding
CA-to-MCA transfer. With the source convention corrected to
`rho=(k-1)/n`, the exact integer specialization is banked as
`rate_half_haboeck_quadratic_johnson_safe_bracket`.

For every razor row `q>2^255.9`, its `m=94` member gives

```text
a_RH(q) <= 1563215236073 = 0.7108679874... n.
```

At

```text
q >= 330298791207625937408605578064099942258 * 2^128,
```

the strongest member affordable below the strict `2^256` field cap is
`m=95`, giving

```text
a_RH(q) <= 1563128173124 = 0.7108283958... n.
```

The previous upper bracket was `3n/4=1649267441664`; the maximal gain is
`86,139,268,540` agreement steps. This is a real bracket movement but no
status flip: Haboeck supplies no adjacent-unsafe witness at `a_m-1`, and the
gap to the proved lower endpoint `k+2^34` remains large.

## Type-2 FR incidence-only route fence (2026-08-10)

The proved node `rate_half_type2_fr_incidence_only_route_fence` answers the
Round-31 `(FR)` route question negatively at the level of the currently
banked support inequalities. At the power-of-two scale `m=64`, an explicit
quartic-difference-family set system satisfies

```text
N=16m, rho=4m-1, T=rho+2, a=7m-1,
sum_x(m-d_x)=1,
min pair union=a,
min |S_gamma\W|=m+2,
```

while

```text
max |S_gamma intersect W|=3m-3=189>128=2m.
```

Thus saturation, `(OV)`, and the individual `(C2)` distance spend cannot by
themselves prove even the old max-vs-mean upgrade, and hence cannot prove the
stronger calibrated cap `7m/4-2=110` at `m=64`. This is not a realizable
Hankel-pencil counterexample and does not refute algebraic `(FR)`. It removes
the incidence-only continuation: the positive residual-(ii) attack must now
use the generalized locator polynomials `f_gamma`, the common syndrome
pencil, or the apolar Hankel equations. The `9/4` official residual and both
crossing budgets remain open.

## Quartic-countermodel biform-lift obstruction (2026-08-10)

The proved node
`rate_half_type2_fr_quartic_coset_biform_lift_obstruction` tests the most
natural algebraic continuation of the preceding incidence witness. Identify
its four copies of `F_257^*` with the four multiplicative cosets of
`mu_256` in `mu_1024`. On each of the three copies untouched by the deleted
incidence, the parameter-root polynomial is

```text
(Gamma-x)^64-c_i.
```

If these rows came from a biform of locator degree at most `rho=255`, its
leading two parameter coefficients would give degree-at-most-255 polynomials
`A,B` satisfying

```text
B(tau_i x)=x A(tau_i x)
```

on three full `mu_256` cosets. Root counting forces `A=B=0`, contradicting
the nonzero row scales. Thus this countermodel has no coset-preserving
degree-255 apolar-biform lift, even before the Hankel equations are imposed.

This is evidence that the algebraic constraint excluded by the incidence
fence is material, but it is not `(FR)`: arbitrary point permutations and
other incidence geometries remain open. The next positive route is now a
classification or aggregate near-minimum-fiber bound for arbitrary
realizable shortened-apolar families, not another audit of this quartic
construction.

## Small-endpoint product-lift falsifier sweep (2026-08-10)

The preregistered `m=2` sweep tested the exact forced `O=0`, `T=rho+2`
incidence shape over `F_97`: 31 double-root rows form `K_9` minus five
edges, and one row has one supported plus one residual root. Across eight
bounded Modal workers, all `599,897` random placements had product-code
parity rank `32`; no nonzero row scaling existed, so none reached Hankel
compatibility.

This is recorded as a **zero-power null**, not evidence of universal
nonrealizability. Generic placements overwhelmingly have full rank; any
lift must be highly structured. The route decision is to stop random
placement sampling and seek an exact classification of the near-saturated
biform or a coverage-defined structured search.

## Type-2 FR spend-calibration correction (2026-08-10)

The proved node `rate_half_type2_fr_exact_spend_calibration` corrects a
load-bearing arithmetic target in the Round-31 report. At `a=7m-1`, the
type-1 term is at most two and a uniform outside spend `p` gives only

```text
T<=2+floor(((9m+1)m)/p).
```

The exact least spend closing this inequality at `T<=4m` is

```text
p_req=floor(((9m+1)m)/(4m-1))+1.
```

For the official `m=2^37`,

```text
p_req=9m/4+1=309237645313,
clean max intersection=7m/4-2=240518168574.
```

By contrast the old proposal `p=2m+2` gives total cap
`618475290622>549755813888`, leaving `68719476734` slopes of residual
room and an asymptotic factor `9/8`. Future algebraic attacks must target the
calibrated spend; proving only the old `~2m` max-intersection statement would
not close the printed counting route.

## Two-type-1 fibre calibration (2026-08-10)

The proved node
`rate_half_type2_fr_two_type1_fibre_spend_calibration` composes the
projective-fibre structure of the minimum-support representation pencil with
the corrected capacity threshold. If the endpoint stratum has two type-1
slopes, their two fibres each have size at least `3m`. For every type-2
slope this proves

```text
outside spend >= 2m+1.
```

Inserted into the printed outside-capacity ledger, this gives the exact cap

```text
T<=2+floor(((9m+1)m)/(2m+1))=9m/2,
```

still an exact factor `9/8` above the target `4m`. Thus the two-type-1
argument is valid but does not close `(FR)` after the spend correction.

For that same fibre lower bound to reach the required spend `9m/4+1`, the
two named fibres must total at least

```text
25m/4,
```

which is `m/4` above their automatic `6m` baseline. Equivalently, the two
type-1 root sets must have total size deficit at least `m/4` below `2rho`,
or all other fibres must carry at most `3m/4-1` points. This is now the exact
concentration target. It is not yet proved to hold, and no critical status
changes.

## Round-32 Haboeck staircase addendum (2026-08-10, coordinator-audited): the import chain CERTIFIED; the full staircase recorded (F1)

The round-32 adversarial `rh_haboeck_seam` packet (`FABLE_AUDIT.md`
plus four replay scripts in `notes/pilots_20260810/rh_haboeck_seam/`) ran
28 attacks on the
wave-57 import chain. **NO KILL on the mathematics** — certified on
object identity (Haboeck's E_m exclusion is word-for-word the repo's
own (SL1) support-wise MCA-bad predicate, same support, same
conjunction; the pair-explained class I feared E_m dropped does not
exist), convention (d = k-1 verified independently; the
counterfactual rho = k/n would make the banked a_m UNSAFE BY
EXACTLY 1 — the correction was load-bearing and applied), rounding
(both directions safe, verifier-characterized), the full ladder
(every banked integer reproduced from (HJ1) alone, m = 3..96), the
Johnson non-crossing, the field scope (no subfield/primality
hypothesis; all six e-strata covered; O6 untripped), the BCHKS25
exclusion boundary (no leak), and the second consumer's CA <= MCA
transport (valid — epsilon_ca is far-branch by construction).
COORDINATOR CLOSURE OF THE PILOT'S ONE ZERO-POWER ITEM (F6): the
pinned upstream audit (przchojecki/rs-mca @ 93fba1be,
audit_bchks25_thm46_conditional_johnson_import.md, read directly)
contains, in its "resolved one level further" section, the
INDEPENDENT PROOF AUDIT of ePrint 2025/2110 Theorem 2 (external
trail github.com/latifkasuli/mca, section "Hab25 proof audit"):
the quadratic mechanism PROVED, the same ell_m constant form, the
linear refinement the sole remaining condition. The import's
"statement and proof audit" closure line is ACCURATE. [Hab25] =
2025/2110 is also ABF26's own bibliography entry. THE HABOECK
PACKET IS EXPORT-READY.

**F1 — THE STAIRCASE OF RECORD (the pilot's finding, now the
consumer text):** the supplier proves, and its verifier checks, the
FULL ladder m = 9..95, not only the razor members. For every
admissible q with q >= Q_9 * 2^128 (log2 q >= 232.650530):

```text
a_RH(q) <= a_{m(q)},   m(q) = max{ m : Q_m * 2^128 <= q },
```

with the named landmarks (exact integers, coordinator-replayed):
m=9 from log2 q ~ 232.6505 (a_9 = 1641330047987, first strict
improvement over 3n/4); m=20 @ ~240.42 (a_20 = 1593817862387);
m=40 @ ~247.54 (a_40 = 1573574783987); m=60 @ ~251.46
(a_60 = 1568006769587); m=80 @ ~254.14 (a_80 = 1565216767187);
m=94 on every razor row (a_94 = 1563215236073); m=95 above
Q_95*2^128 (a_95 = 1563128173124); m=96 unaffordable. The ~23-bit
window log2 q in [232.65, 255.9) carries 86 proved bracket steps
previously unrecorded on this node. Below 2^232.65 the top remains
3n/4 (q >= 2^169) / n (below).

Remaining stale-text items applied elsewhere this bank: F2
(adjacency_closing's "only proved bracket tops" sentence
superseded), F4 (the 232.650531 -> 232.650530 printed-constant fix
on the supplier, safe direction). F5 (16 conflicting-kind doubled
edges, a standing repo pattern) and the supplier-side (RHJ7)
generalization go to the wave-58 Codex brief. No status flips.

Custody note: canonical commit `31aa1e684` says a separate `REPORT.md` was
persisted, but that file is absent from the commit. No claim here depends on
it; the retained audit and deterministic replay scripts are the evidence
surface imported into this tree.

## Round-32 close addendum (2026-08-10, coordinator-audited): banks 2-4 — the bracket's anatomy, the residual ledger, and (FR) proved-but-insufficient

**BANK 2 (rh_farca_upper) — THE OPEN BRACKET'S STRUCTURAL ANATOMY.**
The bracket [k+2^34, 3n/4) is the gap between two classical radii:
3n/4 IS the unique-decoding radius (r <= R/2 <=> a >= n-R/2 = 3n/4
exactly — the Hankel layer's scope is not a technical limit but the
tall/wide pencil boundary), and sqrt(nk) = 0.70710678n is the
common wall of ALL counting instruments (k-subset short by 32
exactly; Johnson by 45.25 at the worst anchor, by 1.3924564 even at
the best). The razor (0.5078n) is below both: counting void, and
the algebra's single-generator step (MI1) REFUTED in the wide
regime by exhibition (see the minimal_index_budget round-32 scope
correction; the deployed tall-regime corollary untouched). FIRST
INTERIOR BOUNDS: **UB-NEAR (unconditional)** — #{bad slopes of
agreement >= 3n/4+2} <= 2^39-1 (scope-monotonicity of column-
farness + the banked tall corollary; 89.00 bits under budget; the
whole exposure is now the DEEP stratum, error weight past R/2-2);
**UB-FIXED (conditional on (HK1))** — B_ca^far(a) <= a-k on the
fixed-kernel class ((HK2) carries NO radius hypothesis; 94.00 bits
at the razor) — but the class is thin (0/1700 sampled) and LB1 is
moving-kernel. **THE FLOOR IS NOT TIGHT INTERIOR**: B_ca^far =
n-a+1 is REFUTED (measured 2x-2.5x (r+1) at small cells,
exhaustive at (7,2,4,q=7); and the banked 2^216 >= at k+2^34-1) —
the -lo shortcut via floor-tightness is dead. NEW LAW CANDIDATE:
the extremal count is q-INDEPENDENT (two cells, five fields;
zero-power beyond). RESIDUALS OF RECORD: R-DEEP (bound the deep
stratum), R-MOVING [THIS MECHANISM IS FALSE — round-33 rh_moving_kernel, coordinator-replayed: the forced-fixed step misapplies the Kronecker identity (the shift set is not a MINIMAL basis; Forney's inequality runs the other way), refuted by exhibition + a 221/221 census (zero fixed generators under round 32's own hypothesis) + round 32's own 0/1700 (HK1) data; generically NEITHER generator is fixed (p* = floor((2R-1)/3)+1 > p_gen = floor((R+1)/2), missing the sufficient condition p* + p_gen <= R by a factor 7/6 at the razor). R-MOVING is WITHDRAWN; see the round-33 close addendum below for what replaces it (the FG stratum, R-PSTAR, R-KER)], R-KER (the >= r+1-2rho ~ 2^40-dim common kernel
with no D-split member; count slopes where a <= 2^34-dim increment
acquires one). CORRECTIONS: the round-32 brief's "2^216 upper
bound" misread the banked LOWER bound (coordinator's error); the
P0 phrase "the layer never touches the bracket interior" is too
strong by UB-NEAR (the P0 conclusion itself stands).

**BANK 3 (rh_residuals_close) — THE RESIDUAL LEDGER, EXACT.**
Residual (i) IS ONE INTEGER at the official profile:
w* = (2^41+1)/3 = 733007751851, certified exhaustively by divisor-
block enumeration (1,482,906 blocks, O in {0,1,m/2,m-2} alike) —
(AO1) returns rho+2 there (deficit exactly 1, the q=17-fence
signature) and T4's hypothesis fails by exactly one point of W
(RIG = -2; the obstruction is sigma_W*(linear)). GAP LAW (m in
[1,300]): 3 integers iff m = 1 mod 3, else 1, exceptions
{1,5,8} — CORRECTING the banked round-29 "1 or 3" claim: **at
m = 8 the (AO1) band has a HOLE (gap = {41,43}, size 2)** — the
band is not always an interval (floor(a/(a-rho)) steps), and
banked range-notation hid it. Residual (i) is INCIDENCE-FENCED
(K_7-vertex-star system at m=2 satisfies every banked axiom at the
gap integer with T = rho+2): residuals (i) and (ii) are THE SAME
ALGEBRAIC FRONTIER. What would close (i): T4's conclusion
transported at RIG = -2 (margin 5/3) — CONDITIONAL on the
collinearity transport not needing S^W = 0 (unresolved, flagged).
**RESIDUAL (iii) IS RETIRED**: m=1 is not open — it is the PROVED
five-slope counterexample node; independently replayed by a
disjoint route (support configs, disjointness PROVED not assumed;
16 configurations, one per omitted point). NEW: **the m=1 failure
is a q=17 ARTIFACT** — exhaustive at ten admissible fields: 16
configs at q=17 (where D = F_q^*), ZERO at q in {97..433} (D a
proper subgroup) — matching round-29's RIG=-1 decay; the fence
node's "uniformly in m" sharpens to "uniformly in (m,q)"
(measurement, ten fields, zero power at official q). THE
BUDGET x REGION TABLE is banked in the pilot's D3 (S1/S2/S3
regions; budget 2^39 DEAD at a = 3n/4 by LB1; every open cell
reduces to the two w* residuals). PRECISION NIT: the "9/4 exactly"
is 9/4 - 15/(4m) (asymptotic; integers exact). **D4 DISCHARGED:
the T3 skip fraction is MEASURED = 19518/21832 = 0.894009** —
the guard passes 0/5842 at a=5 (T3 100% vacuous exactly where
M_max = 17 most needed a cap); the round-31 flagged inference was
right and is now a number.

**BANK 4 (rh_fr_algebraic) — (FR) PROVED, AND INSUFFICIENT.**
**FR-CANONICAL (proved, two lines, no saturation needed): at a
minimising pair union W* = S_g u S_h (a* = |W*| = the min pair
union — an admissible joint support per the banked round-28
convention), every supported slope has |S_gamma ^ W*| <=
4rho - 2a* - 2o_gamma - o_g - o_h; at a* = 7m-1, O = 0: <= 2m-2.**
The (FR) quantifier over W was simply never fixed: for ARBITRARY
joint supports (FR) is REALIZABLY FALSE already at m=3 (j >= 1
stratum; T=3, so (SAT3) untested), and the wave-57 fence's own
system satisfies FR-canonical at every one of its 32896 pair
unions (max 115 <= 128, EXHAUSTIVE — its 189 lives at a W that is
no pair union; see the fence node's round-32 addendum). LEDGER
EFFECT: residual (ii)'s factor drops 9/4 -> 7/4 over the band
(9/4 -> 9/8 at the banked point a = 7m-1); the argmax MOVES to
a = (20m-2)/3; the closed sub-band is UNCHANGED to the integer;
NEITHER BUDGET MOVES. THE MISSING STEP, named to the constant:
closure needs X <= a/4 on (16m/3, 7m-1]; proved is
min(a-(4m+2), 4rho-2a); at the argmax 5m/3 needed vs 8m/3 proved —
**a factor of exactly 8/5**. The round-31 "9/4 is the combinatorial
ceiling" caution is REFUTED IN PART (a pure cardinality move
reached 7/4); the next instrument is D2.4's DEGREE COUNT (psi_gamma
mean weight 5.25m vs the 5m-1 need — NOT self-defeating, ~5%
headroom) or the deficiency-aware bivariate kernel system. At a saturated
coordinate its column is
P_x(Z) = lambda_x L_x(Z) prod_{A_x}(Z-gamma); at a deficient coordinate
the product carries an additional quotient polynomial of degree at most
m-d_x. Thus the exact unknown count is |W|+Delta_W, not always |W|, with
Delta_W<=1+O<=m and only one possible extra column when O=0. This correction
is the proved node `rate_half_bivariate_deficiency_clone_kernel_reduction`;
raw overdetermination is not itself a rank proof. The census's
(SAT3) zero-power carries: T = 3 everywhere; F2 (a T = rho+2
configuration with a* > 7m-1) remains the live falsifier. Pilot
process note: it caught its own false vacuity fence mid-session
(min <= mean does not kill proven floors) — the check that saved
a live route.

## Cycle-57 bivariate rank-count fence (2026-08-10, Codex)

The deficiency-aware matrix has now been evaluated on the proved `m=1`,
`q=17` five-slope Hankel failure. For all ten canonical pair unions, the
unique deficient point lies outside `W`, so the scalar-column model is exact;
nevertheless every matrix has shape `15 x 6`, rank `5`, and nullity `1`.
Each rank has both an explicit all-nonzero kernel vector and a nonzero `5 x 5`
minor certificate. Thus even a `5/2` row surplus plus saturation of every
coordinate in `W` does not imply full column rank. The general route remains
live, but its rank theorem must use an official `m>1` structural exclusion or
be restricted to incidence patterns violating the required `5m/3` cap. The
proved fence is `rate_half_bivariate_row_surplus_route_fence`; no critical
status changes.

## Cycle-58 bounded `m=2` bad-pattern search (2026-08-10, Codex)

A 32-worker, 45-second-per-worker Modal campaign tested the next precise
falsifier at `m=2` over `F_97`. It generated `1,276,996` random incidence
trials, of which `841,449` met the exact row-degree/column-deficit ledger.
Across their minimum pair unions it tested `1,795,113` open-band cases that
all violated the closing intersection cap. Every deficiency-aware matrix had
full column rank: `rank_deficient=0`, hence no blockwise kernel, degree-`rho`
extension, or Hankel witness survived.

This is substantial heuristic support for a bad-pattern rank theorem at the
first nontrivial scale, not a proof. It is one field and a random sample; the
zero downstream counts mean the extension gates had no opportunity to add
evidence. The complete per-worker packet and deterministic aggregate verifier
are `rh_bivariate_m2_badpattern_result.json` and
`verify_rh_bivariate_m2_badpattern.py`. No critical status changes.

## Cycle-59 top-coefficient Schur reduction (2026-08-10, Codex)

After a projective parameter-basis change avoiding the at most `|W|<q`
coordinate fibre roots, every `L_x` has nonzero leading coefficient. The
`j=m+1` rows of the deficiency-aware matrix then contain one scaled
Vandermonde column per point of `W`, so they pay exactly `4m+1` columns.
Block elimination gives

```text
rank(M_W)=4m+1+rank(S_W),
columns(S_W)=|W|+Delta_W-(4m+1).
```

The residual width is at most `4m-2` over the whole `a<=7m-1` band and at
most `3m-1` when `O=0`. For the `m=1` failure it is one and its residual rank
is zero; for the sampled `m=2` open band it is only `2..5`. The proved node is
`rate_half_bivariate_top_vandermonde_schur_reduction`. The remaining theorem
is now the structured full-column-rank problem for `S_W`, not the original
large matrix. No critical status changes.

## Cycles 60-61: exact interpolation defect and rational trace criterion (2026-08-10, Codex)

The Schur matrix now has an exact entry formula. If
`H_x(Y)=sum_j h_j(x)Y^j` is the normalized highest-clone root product and
`P` is a `4m+1`-point pivot set, a nonpivot highest clone contributes

```text
c_(1,x)(x^i h_j(x)-sum_(p in P) ell_p(x)p^i h_j(p)).
```

Lower deficiency clones remain direct monomial columns. The proved node is
`rate_half_bivariate_schur_interpolation_defect_formula`.

The coefficient block one below the top admits a pivot-free characterization.
Writing `r=|W|-(4m+1)`, it has full rank exactly when there are no
`0!=P,Q` of degrees below `r` satisfying

```text
Q(x)=h_m(x)P(x),
h_m(x)=-(mu_x+sum_(gamma in A_x)gamma),
```

on `W`; when the unique deficient point lies in `W`, that one equation is
punctured. This is the proved node
`rate_half_bivariate_single_coefficient_rational_interpolation_criterion`.
The unresolved rank step is therefore the explicit official-scale exclusion
of this low-degree rational trace interpolant.

A bounded `m=2`, `F_97` Modal profile tested `125,335` bad pair unions
(`105,574` saturated, `19,761` deficient). Every full matrix had full rank,
and both tested trace-related blocks independently had full residual rank in every
case; there were no exceptions. This is strong one-scale falsification
evidence, not a proof, so the critical status remains unchanged.

## Cycles 62-63: locator extension added; incidence-only rank refuted (2026-08-10, Codex)

The old matrix omitted an official linear condition. Writing
`Q_Y(x)=A_x(Y)R_x(Y)`, every coefficient must extend on `W` to an
`X`-polynomial of degree at most `rho`. Dual Reed-Solomon interpolation gives
the exact additional rows

```text
E_W[(i,j),(x,t)]
 =x^i [Y^j](A_x(Y)Y^t)/sigma'_W(x),
0<=i<|W|-rho-1,  0<=j<=m.
```

Every actual failure therefore has a blockwise-nonzero kernel for the
strengthened matrix `C_W=[M_W;E_W]`. This is the proved node
`rate_half_bivariate_locator_extension_kernel_reduction`. The new rows retain
the genuine `m=1` failure on all ten pair unions (`rank 5/6`).

They also diagnose a new adversarial fence. At `m=2` over `F_97`, an explicit
`T=rho+2` one-deficit incidence pattern uses six inverse pairs and
`nu_x=x+x^(-1)=(x^2+1)/x`. Its chosen `|W|=12` pair is minimum, all pair
intersections are at most two, and bad overlap is `2>1`, yet
`rank(M_W)=11/12` with an all-nonzero kernel. Thus the earlier random
zero-exception profile cannot support an incidence-only rank theorem. The
witness fails locator extension and `rank(C_W)=12/12`; it is not a Hankel or
Prize counterexample. The proved fence is
`rate_half_bivariate_incidence_only_rational_trace_route_fence`.

The live theorem is now structured full rank, or exclusion of blockwise
nonzero kernels, for `C_W` under the remaining outside-root and Hankel
constraints. Critical status remains unchanged.

## Cycle 64: clean branch is one irreducible cyclic-norm curve (2026-08-10, Codex)

The omission-sensitive component ledger sharpens completely at `O=0`. Its
overlap correction and residual parameter degree both vanish, so the generic
apolar generator is absolutely irreducible of bidegree `(4m-1,m)`. The exact
deficit identity leaves one point `x_0` with `d_(x_0)=m-1` and saturates every
other domain point. The norm and complementary identities become

```text
R=H^(4m-1)S,       deg S=1,
Q Vbar+((X^(16m)-1)/(X-x_0))W=H.
```

At least `3m+1` supported slopes are also generic-rank, fully split, and
parameter-transverse. The proved node is
`rate_half_ca_hankel_clean_endpoint_irreducible_norm_corollary`. Hence no
reducible or product-of-rational-moving-branches continuation remains on the
clean branch; the live geometric object is the irreducible near-perfect
cyclic norm. Positive-`O` branches are outside this corollary, and critical
status remains unchanged.

## Cycle 65: clean two-sided weld and linear unit-resultant gate (2026-08-10, Codex)

The clean irreducible norm now has an exact dual complement. Interpolating
`(X^N-1)/Q_gamma` over all `4m+1` supported slopes and eliminating against
the domain-side complement gives

```text
Q A+H B=X^N-1,       deg_z B<=m-1,
W B-(X-x_0)=Q K.
```

Hence `WB=X-x_0` on the irreducible curve. Taking the parameter resultant,
with `q_inf=[z^m]Q` and actual degrees `b=deg_z B`, `w=deg_z W`, gives

```text
Res_z(Q,W)Res_z(Q,B)=q_inf^(w+b)(X-x_0)^m.
```

The exceptional fibre factors as `Q(z;x_0)=c A_0(z)S(z)` with
`deg A_0=m-1`. The two complements force the exact resultant allocation

```text
ord_(X-x_0)Res_z(Q,B)=1,
ord_(X-x_0)Res_z(Q,W)=m-1,
```

and every remaining factor is supported on the single parameter-infinity
specialization `q_inf`. An `m`th-power valuation argument further proves
`1<=deg_z B<=m-1`, `deg_z W>=1`, and
`deg_z K=deg_z W+deg_z B-m>=0`. The proved leaves are
`rate_half_ca_hankel_clean_endpoint_two_sided_complement_weld` and
`rate_half_ca_hankel_clean_endpoint_linear_unit_resultant_gate`. The live
clean theorem is now the incompatibility of this degree-`<m` linear
unit-resultant with the maximal-separation-rank Hankel/apolar kernel curve;
general curve theory alone does not supply that incompatibility. No critical
status changes.

## Cycle 66: clean boundary saturation and Picard dichotomy (2026-08-10, Codex)

The clean weld now has exact two-axis resultants. Its top coefficient gives

```text
deg_z W=T,
q_inf nu+P_sat omega=1,
Res_z(Q,W)=c_W(X-x_0)^(m-1),
Res_z(Q,B)=c_B q_inf^(T+b)(X-x_0),
deg_X B=N.
```

Thus the entire parameter-infinity fibre belongs to `B`; the former
boundary-free shortcut is impossible. Reciprocally,

```text
Res_X(Q,B)=constant*S,
Res_X(Q,W)=constant*a^(deg_X W+N-1)A_0.
```

The complete intersection divisor yields the degree-one Picard identity

```text
O_C(N,-T)=O_C(P_*).
```

The associated multiplication kernel is exactly `pi_*O_C(P_*)`. Since

```text
pi_*O_C=O+O(-rho)^(m-1),
```

it is a one-point positive elementary modification with only two splitting
types. The `O(1)+O(-rho)^(m-1)` type would make `C` isomorphic to `P^1` and
is excluded by the positive smooth adjunction genus `(4m-2)(m-1)`. Hence the
sole clean Picard branch is

```text
K_Q=O+O(1-rho)+O(-rho)^(m-2),       h^0(K_Q)=1.
```

Independently, the `m+1` coefficient vectors of `Q` form a common totally
isotropic plane for four adjacent endpoint Hankel forms, with `q_inf` as the
two infinity radicals. The live clean theorem is now incompatibility of this
four-Hankel frame and supported-locator incidence with the unique-section
elementary modification. Six proved leaves record the reductions and route
fences; no critical status changes.

## Cycle 67: clean socle frame and marked Veronese reduction (2026-08-11, Codex)

The unique-section modification now has explicit directions on both axes.
Writing

```text
Q(z;x_0)=A_0(z)S(z),
Q(S;X)=(X-x_0)C_0(X),
```

the fibre-socle classes `[A_0]` and `[C_0]` map under the two Serre-dual
connecting maps to the rational-normal evaluation directions `ev_S` and
`ev_x0`. This remains exact in the repeated-root branch and independently
forces the unique-section splitting under both finite projections.

The domain direction permits an exact deletion of the deficient row from
the Hankel frame. If `U` is the remaining generic joint source support, a
Vandermonde-radical argument excludes `|U|=rho` and `|U|=rho+1`; hence

```text
|U|>=rho+2=4m+1.
```

A generic source combination therefore gives a full-support relation

```text
sum_(x in U) lambda_x v_xv_x^T=0,       lambda_x!=0,
v_x=(Q_0(x),...,Q_m(x)),
```

on at least `4m+1` fully saturated squarefree locators split on the common
supported set. The proved nodes are
`rate_half_ca_hankel_clean_endpoint_picard_residual_evaluation_direction`,
`rate_half_ca_hankel_clean_endpoint_picard_two_projection_socle_frame`, and
`rate_half_ca_hankel_clean_endpoint_marked_row_split_veronese_dependency`.
The live clean theorem is incompatibility of this tensor dependence with
the simultaneous degree-`rho` domain interpolation and supported-root
incidence. No critical status changes.

## Cycle 68: clean marked adjugate subset ledger (2026-08-11, Codex)

Contracting the full rectangular Hankel pencil at the marked domain point
gives the square pencil

```text
L(t)=H_1(t)-x_0H_0(t),       rank_F(t)L(t)=rho.
```

Its adjugate and scalar factor are exact:

```text
adj L(t)=D(t)q(t)q(t)^T,
D(t)=c Delta(t)Q(t;x_0)=c Delta(t)A_0(t)S(t),
deg Delta=m-1,       deg D=2m-1.
```

Factoring `L` through the marked Vandermonde support gives a printed
Cauchy-Binet expansion of every cofactor over all `rho`-subsets. The corner
minors are ordinary nonzero Vandermondes; interior generalized minors may
vanish and no termwise positivity is used. Since the marked fibre factor has
exactly `m-1` distinct supported roots and `Delta` has degree `m-1`, at least
`2m+3` supported slopes specialize the subset ledger to the nonzero outer
square of a fully split locator.

The proved node is
`rate_half_ca_hankel_clean_endpoint_marked_adjugate_subset_ledger`. The next
clean gate is to combine the corner subset identity, or its sparse
Forney-weight form, across those `2m+3` slopes with the degree-`m` motion of
`q`. No critical status changes.

## Cycle 69: clean Forney resultant normalization (2026-08-11, Codex)

The sparse moment representation now has a canonical polynomial numerator.
For the reciprocal locator `q^vee`, set

```text
N(t;Z)=[q^vee(t;Z)sum_(i=0)^(rho-1)y_i(t)Z^i]_(<rho),
P(t;X)=X^(rho-1)N(t;X^(-1)).
```

Then `P` has bidegree at most `(rho-1,m+1)`, and at every good supported
slope its values are the exact Forney evaluations

```text
P(gamma;x)=theta_(gamma,x)partial_X q(gamma;x).
```

The top Hankel cofactor identifies their product, and formal resultant
homogeneity gives the global polynomial identity

```text
Res_X^(rho,rho-1)(q(t;X),P(t;X))
 =c a(t)^(2rho+2)Delta(t),       deg Delta=m-1.
```

Thus the apparent quadratic-degree resultant has only the already isolated
degree-`m-1` regular factor after its explicit leading-coefficient power is
removed. The proved node is
`rate_half_ca_hankel_clean_endpoint_forney_resultant_regular_factor`. The
remaining clean theorem is a low-degree interpolation obstruction for these
Forney products across the at least `2m+3` good split slopes, using their
shared supported-root incidence and the degree-`m` motion of `q`. No critical
status changes.

## Cycle 70: clean Picard--Forney endpoint close (2026-08-11, Codex)

The clean strict endpoint is now excluded. On the domain-infinity chart
`u=X^(-1)`, the full `rho+2` Hankel recurrence rows give

```text
q^vee(z;u)sum_(i=0)^(2rho+1)y_i(z)u^i
 =N(z;u)+u^(2rho+2)R(z;u).
```

Since `N=u^(rho-1)P(z;u^(-1))`, restriction to `C:Q=0` makes the nonzero
Forney section vanish to order `2rho+2` along the full `X=infinity` divisor.
Its residual line bundle is

```text
L_F=O_C(-rho-3,m+1),       deg L_F=m-1.
```

The proved clean Picard point satisfies `O_C(P_*)=O_C(N,-T)`. Consequently

```text
L_F^4 tensor O_C(P_*)=O_C(-8,3).
```

The residual and point sections would make the right side effective. But
the restriction sequence

```text
0 -> O(-rho-8,3-m) -> O(-8,3) -> O_C(-8,3) -> 0
```

and Kunneth give `H^0(C,O_C(-8,3))=0` for `m>3`. This contradiction uses
only integrality and applies to the official `m=2^37` row. The proved node
is `rate_half_ca_hankel_clean_endpoint_picard_forney_contact_exclusion`.
The live strict endpoint is now confined to positive omission defect
`1<=O<=m-1`; the `O=0` branch needs no further casework. The critical node
remains open because those defect strata and the adjacent unsafe witness are
not yet closed.

## Cycle 71: full first strict endpoint close (2026-08-11, Codex)

The contact argument now closes every `e=m` omission-defect stratum. The
full Hankel recurrence gives, without a clean or irreducibility assumption,
a nonzero residual section

```text
s_F in H^0(C,O_C(-rho-3,m+1)).
```

For the grid ratio `G(X)/H(z)`, the pole-cancellation ideal `J=(H:G)` has

```text
length(O_C/J)<=sum_(gamma in Z)(rho-u_gamma)=O<=m-1.
```

On the official even row, `ell=m/2-1` and
`h^0(O(1,ell))=m`. A nonzero biform `F` of degree `(1,ell)` therefore clears
the entire pole scheme and gives a regular section

```text
s_G=FG/H in H^0(C,O_C(N+1,ell-T)).
```

Every component has domain degree at least four, so `s_G` is nonzero on
every component. Since `C` is reduced, `s_F^4s_G` is a nonzero section of

```text
O_C(-7,ell+3).
```

The Cartier restriction sequence and Kunneth give zero sections because
`ell+3-m=2-m/2<0`. This contradiction excludes all
`0<=O<=m-1`, including every reducible positive-defect pattern. The proved
nodes are `rate_half_ca_hankel_endpoint_forney_infinity_contact_section` and
`rate_half_ca_hankel_endpoint_residual_pole_interpolation_exclusion`.

The first strict `A=3`, `e=m` endpoint is closed. The live strict frontier
now starts at `e>m`, alongside the residual `A=1` profiles and the independent
adjacent-unsafe obligation. The critical node itself remains open.

## Cycle 72: strict `A=3` single-corner reduction (2026-08-11, Codex)

The Forney contact section extends to every strict moving degree:

```text
s_F in H^0(C,O_C(-rho-3,e+1)),
deg L_F=delta=rho-3e.
```

For `T=4e+1-h`, a biform of degree
`(1,floor(delta/2))` clears the full pole scheme of `G/H`, whose length is at
most `O<=delta`. Three contact copies then give a nonzero section of

```text
O_C(rho-4,-e+floor(delta/2)+h+2).
```

Surface cohomology makes this impossible whenever

```text
floor(delta/2)+h+2<e.
```

The official integer range has exactly one exception:

```text
e=floor(rho/3)=(4m-2)/3,
delta=1,
h=e-2,
T=rho+2=4m+1.
```

Thus all strict `A=3` profiles except this minimal-violation corner are now
excluded; the survivor has `O<=1` and total rank loss at most one. The proved
node is `rate_half_ca_hankel_strict_a3_slope_slack_contact_exclusion`, using
the generalized
`rate_half_ca_hankel_endpoint_forney_infinity_contact_section`.

The critical node remains open only through this strict corner, the residual
`A=1` profiles, and the independent crossing/unsafe obligations.

## Cycle 73: final strict-corner Picard pin (2026-08-11, Codex)

The sole corner is now integral. If `d<=1` is the actual pole length of the
grid ratio `G/H`, a form of bidegree `(d,0)` clears it. Three contact sections
then descend through

```text
H^0(C,O_C(rho-5+d,0))=H^0(P^1_X,O(rho-5+d))
```

to the exact identity

```text
s_F^3(FG/H)=A_d(X).
```

Because an `X`-only polynomial cannot vanish on a mixed component, `s_F` is
nonzero on every component. Writing a component bidegree as `(r_i,e_i)` and
`a_i=4e_i-r_i`, its contact degree is

```text
l_i=e e_i-(e+1)a_i>=0,       sum_i l_i=1.
```

Coprimality makes `l_i=0` impossible, so there is exactly one component.
Thus `C` is absolutely irreducible and

```text
O_C(-rho-3,e+1)=O_C(P_*)
```

for one effective degree-one Cartier point. The proved node is
`rate_half_ca_hankel_strict_a3_final_corner_integral_picard_pin`.

The live strict theorem is now only incompatibility of this point and the
univariate identity with the supported-grid divisor, separately for
`d=0,1`. The critical node remains open.

## Cycle 74: strict `A=3` branch closure (2026-08-11, Codex)

On the normalized final-corner curve, decompose the grid divisors as

```text
D_G=K+Z_+,       D_H=K+P_-,       p=deg P_-<=O<=1.
```

The support of `K` is exactly the distinct grid incidence set, so its total
multiplicity in excess of one per incidence is `O-p<=1-p`. The Picard-pin
identity has divisor

```text
3P_*+Z_+ + dE_F-P_-=pi_X^* div(A_d),       d<=1.
```

Every fibre on the right is complete. If the clearing fibre is absent from
`P_*`, completeness forces `K=3P_*` and costs two excess units. If the two
fibres coincide, completeness forces `K+P_-=3P_*` and costs `2-p` excess
units. The ledger permits only `1-p`, a contradiction in both cases.

The proved node is
`rate_half_ca_hankel_strict_a3_final_corner_divisor_exclusion`. Together
with the slope-slack theorem, it excludes every strict `A=3` moving-kernel
profile. Only the residual `A=1` profiles and the independent crossing and
adjacent-unsafe obligations remain live in this critical target.

## Cycle 75: `A=1` core-free contact reduction (2026-08-11, Codex)

The core-free half-distance branch has a canonical Forney section. The
`rho` available Hankel recurrence rows give contact order `2rho`, hence

```text
s_F in H^0(C,O_C(-rho-1,e+1)),       deg L_F=rho-e.
```

Let `p` be the actual pole-ideal colength and put `ell=4e-T`. Adaptive pole
interpolation, with domain degree `alpha` equal to `2`, `1`, or `0` in the
three ranges cut by `e=rho/2` and `e=rho`, combines with three contact
sections to exclude every profile satisfying

```text
floor(p/(alpha+1))+ell+3<e.
```

Every survivor therefore has `p>=(alpha+1)(e-ell-3)`. At the first live
degree `e=m+1`, only `ell=0,1,2` occur and the remaining pole deficiencies
`Delta-p` are at most `5`, `8`, and `11`. The proved nodes are
`rate_half_ca_hankel_a1_core_free_forney_contact_section` and
`rate_half_ca_hankel_a1_core_free_pole_slack_exclusion`.

This narrows but does not close `A=1`: the three finite-deficiency chambers,
higher core-free degrees failing the inequality, and fixed-core `s=1,2`
profiles remain live.

## Cycle 76: `A=1` fixed-core-two closure (2026-08-11, Codex)

Fixed-core contraction preserves the contact construction. If `s` is the
core size and `d=rho-s`, the residual pencil still has `rho` rows, so its
contact order is `d+rho` and

```text
s_F in H^0(C,O_C(-rho-1,e+1)),
deg L_F=d-(s+1)e=Delta.
```

For `s=1,2`, a pole-clearing form of bidegree `(2,floor(p/3))` and three
contact sections exclude every profile satisfying

```text
floor(p/3)+ell+3-beta<e,       beta=T_max-4e.
```

The inequality holds for every `s=2` integer profile, including the
`Delta=0,beta=2` boundary. It also excludes the first `s=1` degree
`e=m+1`; any higher `s=1` survivor must satisfy `p>=3(e-ell-2)`. The proved
nodes are `rate_half_ca_hankel_a1_core_stripped_forney_contact_section` and
`rate_half_ca_hankel_a1_fixed_core_pole_slack_exclusion`.

The complete `A=1` core-two branch is closed. The remaining `A=1` frontier
is core-free `s=0` plus higher fixed-core-one `s=1` profiles.

## Cycle 77: `A=1` low-degree prefix exclusions (2026-08-11, Codex)

Using four rather than three contact copies makes the target domain degree
negative and permits a degree-three pole interpolant. When
`3(e+1)<rho+1`, a profile is impossible if

```text
floor(p/4)+ell+4-beta<e.
```

At the official `m=2^37`, this excludes

```text
s=0: m+1<=e<=floor(12m/11)-1,
s=1: m+1<=e<=floor(6m/5)-1.
```

The first unexcluded degrees are `149933403787` and `164926744166`.
In particular, the three finite pole-deficiency chambers formerly retained
at core-free degree `e=m+1` are all empty. The proved node is
`rate_half_ca_hankel_a1_four_contact_low_degree_exclusion`.

The live `A=1` frontier consists of the upper core-free and core-one degree
ranges starting at these two exact thresholds; core two remains closed.

## Cycle 78: `A=1` sharp-cap closure (2026-08-11, Codex)

No `A=1` failure can attain its Euclidean slope cap `ell=0`. For core one,
the three-contact theorem gives

```text
ell>=e-2-floor(Delta/3)>=1.
```

For core-free profiles, four contacts exclude `e=m+1,m+2` and three
contacts exclude every sharp profile from `e=m+3` through `e=rho`. Core two
is already empty. The proved node is
`rate_half_ca_hankel_a1_all_core_sharp_cap_exclusion`.

This retires the historical maximal-degree core-one corrected-square route
as a live frontier: its necessary reductions remain valid, but their
sharp-cap parent is now impossible. All remaining `A=1` profiles have
positive slope slack and lie in the upper `s=0,1` degree ranges.

## Cycle 79: core-one quartic-carrier exclusion (2026-08-11, Codex)

The four-contact argument admits one more domain degree on the core-one
branch. A biform of bidegree `(4,floor(p/5))` clears the pole scheme, and
four contact copies would produce a section of

```text
O_C(-1,floor(p/5)+ell+3).
```

Containment creates no exceptional branch. If the clearing form contains
every contact-active component, their product has domain degree at most
four. All other components are contact-inactive and divide the Forney
numerator, so cancelling their product from the full recurrence leaves a
degree-at-most-four kernel vector for the generic rank-`d` contracted Hankel
pencil. Its unique primitive kernel has degree `d=rho-1>4`.

The proved node
`rate_half_ca_hankel_a1_core_one_quartic_carrier_exclusion` excludes every
official core-one degree

```text
m+1<=e<=floor(16m/13)-1.
```

Thus the first live core-one degree moves from `164926744166` to
`169155635042`. At every later degree a survivor must satisfy

```text
ell>=e-3-floor(Delta/5)
```

in addition to the prior three-contact bound. The core-free threshold
remains `149933403787`.

## Cycle 80: general core-one adjugate and first cubic corner (2026-08-11, Codex)

For every core-one degree, contraction gives a square symmetric middle
Hankel pencil of size `d+1` and generic corank one. Its primitive degree-`e`
kernel vector satisfies

```text
adj M=D q q^T,       deg D=Delta=d-2e.
```

The common cofactor factor `D` is the regular Kronecker determinant. Local
pole length is bounded by local rank loss and then by `ord(D)`, so the
pushed-forward pole divisor is an effective subdivisor of `div(D)`.

At the first remaining official core-one degree

```text
e=floor(16m/13)=169155635042,
```

the carrier inequality meets the maximal slack exactly. Every failure is
therefore forced to

```text
ell=126866726279,       T=rho+2,
Delta-3<=p<=O<=sum c_gamma<=Delta.
```

Thus `D=P_pE_3` with `deg E_3<=3`, and at least `T-Delta=2e+3` supported
fibres are clean and completely split. The proved nodes are
`rate_half_ca_hankel_a1_core_one_general_middle_adjugate_factorization` and
`rate_half_ca_hankel_a1_core_one_first_surviving_cubic_residual_corner`.
The next finite-defect target is the cubic residual factor coupled to those
clean fibres; the corner itself is not yet excluded.

## Cycle 81: Forney pole absorption and direct three-contact close (2026-08-11, Codex)

The Forney numerator clears the pole scheme without interpolation. On each
supported residual fibre, write

```text
Qbar=Q_min R,       G=Q_min G_1.
```

The recurrence numerator factors as `N_F=R N_min`, so
`Qbar` divides `N_FG`. In the full fibre algebra this is exactly

```text
N_F in (H:G).
```

Thus one contact copy makes `s_FG/H` regular. Three copies give a nonzero
section of

```text
O_C(d-3,ell-e+3-beta).
```

Restriction-sequence vanishing forces `ell>=e-3+beta`. Combining this with
the maximal-slack ledger excludes both `s=0` and `s=1` whenever
`3e<rho-1`.

The two live core ranges now share the first degree

```text
e_0=ceil((rho-1)/3)=183251937963.
```

At `e_0` there are exactly six profiles:

```text
s=0: ell=e_0-3,e_0-2,e_0-1;
s=1: ell=e_0-2,e_0-1,e_0;
T=rho+4,rho+3,rho+2.
```

The proved nodes are `rate_half_ca_hankel_a1_forney_pole_ideal_absorption`
and `rate_half_ca_hankel_a1_direct_three_contact_exclusion`. They retire the
earlier cubic-residual corner at `e=floor(16m/13)` as a live target.

## Cycle 82: six bounded first-degree residuals (2026-08-11, Codex)

At the six boundary profiles, put

```text
j=ell-e+3-beta in {0,1,2}.
```

The direct three-contact section lies in `O_C(d-3,j)`. Since

```text
H^0(O(-3,j-e))=H^1(O(-3,j-e))=0,
```

it extends uniquely to a nonzero ambient biform `A_j` of bidegree
`(d-3,j)`. At every residual domain row `x`, the full missing-root factor

```text
R_x=Qbar(x)/gcd(Qbar(x),H),       deg R_x=e-d_x,
```

divides `A_j(x)`. Thus every row with deficit greater than `j` is a common
split `X`-factor of all coefficients of `A_j`.

Removing the product of these heavy rows and applying the exact capacity
ledger leaves only

```text
s=0: (5,0), (12,1), (18,2);
s=1: (2,0), (9,1), (15,2).
```

The proved nodes are
`rate_half_ca_hankel_a1_first_degree_ambient_defect_factorization` and
`rate_half_ca_hankel_a1_first_degree_bounded_residual_table`. The next proof
should classify these six small residual biforms, starting with the two
parameter-constant cases.

## Cycle 83: constant residual heavy-incidence pin (2026-08-11, Codex)

For `j=0`, cancel the split heavy-row factor from both the ambient identity
and residual domain locator. At every supported incidence on a removed row,
regularity forces the Forney numerator to vanish. In the fibre factorization

```text
Qbar_gamma=Q_min R_gamma,       N_F=R_gamma N_min,
```

such an incidence belongs to the excess factor `R_gamma`. Therefore the
total heavy incidence count `I_H` satisfies `I_H<=sum c_gamma<=Delta`.

The remaining `3rho+3+a` rows are saturated. Exact incidence balance gives

```text
s=0: I_H+O=(6-a)e-3,       Delta=2e-1;
s=1: I_H+O=(3-a)e-6,       Delta=e-2.
```

Together with the bounded residual table, this leaves

```text
s=0,j=0: a in {2,3,4,5};
s=1,j=0: a in {1,2}.
```

At `s=0,a=2`, the two gaps from `I_H,O<=Delta` total one; at `s=1,a=1`
they total two. The proved node is
`rate_half_ca_hankel_a1_first_degree_constant_heavy_incidence_pin`.

## Cycle 84: constant-residual triple-tangency packets (2026-08-11, Codex)

After cancelling the heavy factor, write the scalar residual as `R_a(X)`.
At a heavy supported incidence on a row where `R_a` is nonzero, the exact
cube identity has local form

```text
L_gamma=unit*s_F^3.
```

The horizontal intersection length is therefore divisible by three. The
minimal split recurrence factor contributes one simple root, so the excess
factor consumes at least two degrees at every such ordinary incidence.
Incidences on heavy roots of `R_a` consume at least one degree. Hence

```text
2I_0+I_E<=sum_gamma c_gamma<=Delta.
```

This classifies the two smallest scalar residuals. For `s=0,a=2`, `R_2`
has two distinct heavy domain roots, `O=Delta`, and the row-deficit packets
are

```text
({1,1}, I_0=0),       ({1,2}, I_0=1).
```

For `s=1,a=1`, the unique root of `R_1` is a heavy row of deficit `2..6`.
There are exactly six gap packets and at most two ordinary heavy
incidences. The proved node is
`rate_half_ca_hankel_a1_first_degree_constant_triple_tangency_packets`.

## Cycle 85: first core-one packet becomes a two-point Picard obstruction (2026-08-11, Codex)

In the core-one packet `(u,v,I_0,c)=(0,2,0,2)`, all `Delta=e-2` excess
degrees occur at the distinguished row `x_*`. Exactly `e-4` slopes make
`x_*` a repeated minimal root and exactly two slopes `alpha,beta` make it a
new simple excess root. The local cube identity fixes the vertical
multiplicities, giving

```text
D=P_ord L_alpha L_beta,
Qbar(U,V;x_*)=P_ord L_alpha^2 L_beta^2.
```

The adjugate factor `D` is squarefree. Moreover

```text
N_F(U,V;x_*)=D C_3,       deg C_3<=3,
partial_X Qbar(U,V;x_*)=P_ord S_4,       deg S_4<=4.
```

The contact zero divisor is the vertical fibre minus one extra copy at each
double parameter root. Equivalently,

```text
O_C(rho+2,-e-1)=O_C(P_alpha+P_beta),
```

an effective degree-two Picard relation. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_gap_zero_two_point_normal_form`.

## Cycle 86: two-point pushforward dichotomy (2026-08-11, Codex)

Push the degree-two Picard line bundle along the finite domain projection.
The two points lie above the same row but are distinct on `C`, so they give
a rank-two exponent-`(1,1)` elementary modification of

```text
pi_*O_C=O direct_sum O(-d)^(e-1).
```

There are exactly two splittings:

```text
O(1) direct_sum O(1-d) direct_sum O(-d)^(e-2),
O direct_sum O(1-d)^2 direct_sum O(-d)^(e-3).
```

The first has two sections and yields a degree-at-most-two pencil after
removing its base divisor. The second has only the canonical section
cutting out the two points. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_two_point_pushforward_dichotomy`.

## Cycle 87: all six core-one packets have bounded divisor tails (2026-08-11, Codex)

For any core-one scalar packet, let `x_*` be the unique distinguished heavy
row, `P_*` its squarefree supported-slope locator, and

```text
c=2+u+I_0<=6.
```

The complete official-size factors reduce to

```text
Qbar(U,V;x_*)=P_* K_c,
D=P_* E_(c-2),
N_F(U,V;x_*)=P_* C_(c+1),
```

with tail degrees at most `6`, `4`, and `7`. If `R_0` is the divisor of the
at-most-two ordinary heavy incidences, then the contact divisor gives

```text
O_C(rho+2,-e-1)=O_C(Z_c-R_0-E_u),
deg Z_c=c<=6,       deg E_u=u<=2,
deg(Z_c-R_0-E_u)=2.
```

Thus all six tangent packets are bounded signed-divisor problems. The
proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_six_packet_bounded_divisor_normal_form`.

## Cycle 88: both core-free packets have a degree-one Picard normal form (2026-08-11, Codex)

Let `P_1,P_2` be the supported-slope radicals of the two distinguished
heavy rows. Their row tails have degrees `{1,1}` or `{1,2}`, and

```text
Qbar(U,V;x_i)=P_i K_i,
N_F(U,V;x_i)=P_i C_i,       deg C_i<=3,
```

with the two Forney quotients not both zero. If `D_reg` is the regular
Kronecker determinant and `I_0` is zero or one, then

```text
D_reg=P_1P_2 L_0^(2I_0)E_(1-I_0).
```

Thus the packet with one ordinary triple incidence completely factors the
regular determinant; the other leaves one root. The contact divisor yields

```text
O_C(rho+3,-e-1)=O_C(Z_1+Z_2-R_0-E_1),
deg(Z_1+Z_2-R_0-E_1)=1.
```

The proved node is
`rate_half_ca_hankel_a1_first_degree_core_free_two_packet_bounded_divisor_normal_form`.

## Cycle 89: core-free residual degree two is excluded (2026-08-11, Codex)

Both core-free packets have `O=Delta`, so equality holds throughout the
omission and regular-determinant budget. Every excess root must therefore
overlap the squarefree minimal split locator; no new simple domain root is
available.

Each packet has a distinguished row of deficit one. With one minimal and
one excess copy, every supported horizontal root has multiplicity two. The
local cube identity forces the corresponding vertical multiplicities to be
`1 mod 3`, while unsupported vertical roots have multiplicity `0 mod 3`.
The resulting vertical degree is `e-1 mod 3`, not the official
`e=0 mod 3`.

In the packet with no ordinary incidence, the sole remaining determinant
order cannot repair this: spending it at one row root raises the minimum
vertical multiplicity from one to three, producing total degree `e+1`.
The other packet has no unspent determinant order. Thus both are empty and

```text
s=0,j=0: a in {3,4,5}.
```

The proved node is
`rate_half_ca_hankel_a1_first_degree_core_free_degree_two_packet_exclusion`.

## Cycle 90: first tangent packet has only the canonical Picard section (2026-08-11, Codex)

In the vertical fibre at `x_*`, the two doubled parameter roots give local
algebras `Fbar[s_alpha]/(s_alpha^2)` and
`Fbar[s_beta]/(s_beta^2)`. The two positive elementary-modification
directions are the nilpotent classes `s_alpha,s_beta`. They vanish on all
other `e-4` fibre factors, while the constant direction does not.

Thus their span misses the constant line and projects with rank two to the
negative block of `pi_*O_C`. The PENCIL splitting is impossible; necessarily

```text
pi_*O_C(P_alpha+P_beta)
 =O direct_sum O(1-d)^2 direct_sum O(-d)^(e-3),
h^0(C,O_C(P_alpha+P_beta))=1.
```

The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_two_point_pencil_branch_exclusion`.

## Cycle 91: all no-ordinary tangent packets are unique-section classes (2026-08-11, Codex)

For each core-one packet with `I_0=0`, the nonbaseline regular-rank budget is
at most two. The local horizontal multiplicity is therefore at most four.
The cube congruence `m+n=0 mod 3` gives `2n>=m` at every point of the
distinguished vertical fibre.

An exact omission lower bound forces all residual contact degree `u` onto
that fibre. Coefficientwise,

```text
H_2=Z_c-E_u
```

is therefore an effective degree-two proper subdivisor of the vertical
fibre. Its length-two modification directions lie in the fibre nilpotent
ideal and miss the constant line. Thus all three packets

```text
(u,v,I_0,c)=(0,2,0,2),(1,1,0,3),(2,0,0,4)
```

have the CANONICAL pushforward splitting and exactly one section. The
proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_no_ordinary_effective_canonical_packets`.

## Cycle 92: exact normal forms for all signed tangent packets (2026-08-11, Codex)

The excess-degree and omission identities are exact in all three packets
with `I_0>0`. They force every ordinary incidence to have one minimal and
two excess copies, horizontal multiplicity three, and contact multiplicity
one. The sole spare rank-loss copy in `(2,0,1,5)` is forced onto one
distinguished incidence.

The vertical cube ledger then gives effective divisors `A,B` of bounded
degree and the exact signed classes

```text
(1,1,1,4): O_C(rho+2,-e-1)=O_C(A+2B-R_0), deg A=deg B=1;
(2,0,1,5): O_C(rho+2,-e-1)=O_C(A+2B-R_0), deg A=deg B=1;
(2,0,2,6): O_C(rho+2,-e-1)=O_C(2B-R_0),   deg B=2.
```

No rank-loss or contact degree remains unallocated. The classes are still
signed and are not asserted effective. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_signed_packet_local_normal_forms`.

## Cycle 93: signed tangent packets have no degree-two section (2026-08-11, Codex)

In each signed normal form, the positive divisor `P_pos` is coefficientwise
a proper subdivisor of the distinguished vertical fibre. Its degree is
`r=3` in the first two packets and `r=4` in the last. The `r`
elementary-modification directions lie in the fibre nilpotent ideal and miss
the constant line. Therefore

```text
pi_*O_C(P_pos)=O direct_sum O(1-d)^r direct_sum O(-d)^(e-1-r),
h^0(C,O_C(P_pos))=1.
```

The unique section cuts out `P_pos`. The nonempty ordinary divisor `R_0` lies
on other domain fibres, so subtracting it kills that section. Hence all
three signed packets satisfy

```text
h^0(C,O_C(rho+2,-e-1))=0.
```

Together with cycle 91, the six tangent packets have complete section table
`1,1,1,0,0,0`, grouped by `I_0=0` and `I_0>0`. This classifies but does not
exclude them. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_signed_packet_section_vanishing`.

## Cycle 94: scalar residual-root rows have an exact correction law (2026-08-11, Codex)

For any heavy row `x` at a root of the scalar residual, let `c_x` be its row
deficit, `t_x` the number of distinguished excess roots outside the minimal
locator, and `epsilon_x` the excess multiplicity beyond one copy per
distinguished incidence. Summing the cancelled cube identity over the
complete vertical fibre and using `3|e` gives

```text
c_x+epsilon_x-t_x=0 mod 3.
```

Thus a full-overlap row of deficit `0,1,2 mod 3` costs respectively
`0,2,1` correction copies, and the global rank budget gains the sum of these
row costs. This packages the mechanism that killed core-free degree two and
now applies uniformly to the remaining scalar degrees `3,4,5`. It is a
necessary constraint, not an exclusion. The proved node is
`rate_half_ca_hankel_a1_first_degree_constant_root_row_mod_three_correction`.

## Cycle 95: the first fifth of the cubic gap has two root patterns (2026-08-11, Codex)

For the core-free scalar residual `a=3`, exact omission accounting and the
simple-root vertical bound give

```text
u+v=e+1,
(3-r)e<=3u+2I_0<=5u
```

whenever all `r` heavy residual roots are simple. A triple-root residual
requires `2u>=e`. Therefore throughout

```text
5u<e
```

the cubic is forced into exactly one of two patterns:

```text
SQUAREFREE: three distinct heavy roots;
DOUBLE:     one double and one simple root, both heavy.
```

This excludes triple roots and roots outside the heavy set for
`0<=u<=36650387592`. Both retained patterns remain live. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_free_cubic_root_multiplicity_router`.

## Cycle 96: the gap-one double-root cubic has four exact packets (2026-08-11, Codex)

In the core-free cubic branch at `u=1`, retain a double residual root and a
simple residual root. Exact excess-degree accounting, ordinary cube
divisibility, and the root-row correction congruences leave exactly

```text
I_0  c_s c_d  epsilon_s epsilon_d  w   t_s   t_d
 0    1   1       0         0      1    1    e-2
 0    1   1       1         0      0    2    e-2
 0    1   1       0         1      0    1    e-1
 1    2   1       0         0      0    2    e-2.
```

All vertical and contact degree is then forced. The first three packets have

```text
O_C(rho+3,-e-1)=O_C(A),       h^0=1,
```

while the ordinary packet has

```text
O_C(rho+3,-e-1)=O_C(A+B-R_0), h^0=0.
```

This is a complete normal-form and section classification; it does not yet
exclude any packet. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_free_cubic_double_root_gap_one_normal_forms`.

## Cycle 97: the squarefree gap-one cubic has one corrected row (2026-08-11, Codex)

For the squarefree cubic branch at `u=1`, put

```text
q_i=c_i+epsilon_i-t_i
```

on its three simple heavy root rows. The exact outside-degree audit leaves
only the global charge regimes

```text
(I_0,w,sum epsilon_i)=(0,1,0),(0,0,1),(1,0,0).
```

Every `q_i` is a nonnegative multiple of three, while exact omission gives

```text
q_1+q_2+q_3=3.
```

Thus exactly one row has `q_i=3`. Its unaugmented, augmented-new, and
augmented-overlap vertical/contact divisors are respectively forced to the
forms

```text
(R+N+3P, R+P),
(R+N-J+3P, R+P),
(R+N+2J, R+J).
```

The complete contact divisor is `R_1+R_2+R_3+P_h+I_0R_0`. Unlike the
double-root branch, the induced Picard class has degree `e+1`; bounded-degree
section vanishing is therefore not a closing route. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_free_cubic_squarefree_gap_one_correction_normal_forms`.

## Cycle 98: the core-one quadratic starts with two exact root patterns (2026-08-11, Codex)

For the remaining core-one scalar quadratic, the exact gap identity is

```text
u+v=e+2,
```

so `u>=4`. At `u=4`, omission vanishes. Every excess root is simple and new,
ordinary incidences disappear, and the complete excess degree is `e-6`.

If the quadratic has a double root, that heavy row has deficit six and

```text
V_*=R_*+3B,
div(s_F)=R_*+2B,
O_C(rho+2,-e-1)=O_C(B),       deg B=2,       h^0=1.
```

If the quadratic is squarefree, both roots are heavy. Parity and the local
cube correction force, up to exchange,

```text
(c_1,c_2)=((e+3)/2,(e+9)/2),
(q_1,q_2)=(3,9).
```

Their vertical/contact forms are `V_i=2R_i+3P_i` and `D_i=R_i+P_i`, with
`deg(P_1,P_2)=(1,3)`. The induced effective Picard class has degree `e+2`.
Both patterns remain live. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_root_normal_forms`.

## Cycle 99: the first fifth of the core-one quadratic has two root patterns (2026-08-11, Codex)

For every core-one scalar quadratic gap, exact heavy-incidence accounting
gives

```text
u+v=e+2,       O=u-4.
```

If `E` is the set of heavy residual-root rows, new-root capacity gives

```text
t_E>=e+2-2u-I_0+epsilon_E.
```

At a simple residual root, vertical degree gives
`t_x<=c_x+epsilon_x`. Hence if `r` heavy residual roots are simple,

```text
(2-r)e<=3u+2I_0<=5u.
```

Throughout `5u<e`, a squarefree residual with only one heavy root is
impossible. Since the heavy incidence count is positive, the complete
dichotomy is

```text
DOUBLE:     one heavy double root;
SQUAREFREE: two heavy simple roots.
```

This holds for every official integer `4<=u<=36650387592`. It routes but
does not exclude either branch. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_root_multiplicity_router`.

## Cycle 100: retained double-root branches are exact global cube problems (2026-08-11, Codex)

For any parameter-constant scalar residual with multiplicities at most
three, let `J=rad(R_a)`. The cancelled ambient identity gives, in the total
quotient ring of `C`,

```text
(J/s_F)^3=(J^3/R_a)(G_L/H).
```

The two retained double-root branches therefore satisfy

```text
core-free cubic:
 ((X-x_s)(X-x_d)/s_F)^3
  =(X-x_s)^2(X-x_d)G_L/H;

core-one quadratic:
 ((X-x_d)/s_F)^3=(X-x_d)G_L/H.
```

Their bounded Picard sections are exactly these cube roots: `O_C(A)` in the
no-ordinary cubic packets and `O_C(B)` in the quadratic double packet. The
ordinary cubic root instead has divisor `A+B-R_0` and its predicted pole.

Thus section uniqueness is compatible with the scalar ambient equation.
Closing either double-root branch now requires a Hankel/apolar theorem that
the printed separated locator ratio is not a cube. The strict `A=3`
separated-pullback theorem does not apply to this mixed rational cube root,
and characteristic three must be treated separately in any Kummer-cover
argument. The proved node is
`rate_half_ca_hankel_a1_first_degree_double_root_radical_cube_bridge`.

## Cycle 101: the global cube obstruction has an exact resultant test (2026-08-11, Codex)

Let `q_d(z)` be the leading `X` coefficient of `Q`, and let `P(X)` be the
explicit numerator in either double-root cube identity. Taking the norm from
the finite reduced total-quotient algebra of `C` over `F(z)` gives

```text
Xi_P(z)=Res_X(Q,P)/(q_d(z)^deg(P) H(z)^d)
       =Norm(W)^3.
```

Thus `Xi_P` must be a cube in `F(z)`. In characteristic different from
three, every irreducible valuation must be divisible by three and the
remaining constant must be a base-field cube. In characteristic three,
perfectness of the finite field gives the exact test

```text
d Xi_P/dz=0.
```

Failure excludes the corresponding scalar double-root branch. Passing is
only necessary and does not reconstruct `W` or the recurrence. The actual
leading coefficient factor is essential, and no irreducibility of `C` is
assumed. The proved node is
`rate_half_ca_hankel_a1_first_degree_double_root_resultant_cube_gate`.

## Cycle 102: the double-root resultants have residual degree at most two (2026-08-11, Codex)

Taking the norm of the actual bounded Picard section removes the unknown
rational cube from cycle 101. In every retained double-root packet, the
locator numerator degree is exactly three times the first coordinate of the
cube-root line bundle, so the complete leading-coefficient factor cancels.

For each no-ordinary cubic packet,

```text
Res_X(Q,P_3)=c^3 H^rho S_A^3,       deg S_A=1.
```

For the ordinary cubic packet, if `H=L_0H_0`,

```text
Res_X(Q,P_3)=c^3 L_0^(rho-3) H_0^rho S_AB^3,
deg S_AB=2.
```

For the core-one quadratic double packet,

```text
Res_X(Q,P_2)=c^3 H^(rho-1) S_B^3,   deg S_B=2.
```

The three residual forms are the parameter pushforwards of `A`, `A+B`, and
`B`; they are outputs, not free variables. All total degrees agree exactly.
Any different supported multiplicity or residual degree kills the packet.
The proved node is
`rate_half_ca_hankel_a1_first_degree_double_root_low_degree_resultant_factorization`.

## Cycle 103: the double-root gates are explicit marked Hankel determinants (2026-08-11, Codex)

The low-degree resultant factors now have an exact interface with the
actual syndrome Hankel pencils. In the core-free branch, let `M_0` be the
`rho x (rho+1)` residual Hankel pencil and let `nu(x)` be the coefficient
evaluation row. There is a nonzero regular-block factor `D_0` of degree
`2e-1` such that

```text
det stack(M_0,nu(x))=D_0 Q(U,V;x).
```

Thus the complete cubic resultant is the product of these marked
determinants over the light rows, with multiplicities two and one at the
simple and double residual-root rows, divided by the corresponding power
of `D_0`.

In the core-one quadratic branch, the symmetric middle Hankel pencil
satisfies `adj M_1=D_1qq^T`, with `deg D_1=e-2`. Hence

```text
det(M_1+tau nu(x)nu(x)^T)=tau D_1Q(U,V;x)^2.
```

At the `u=4` double heavy root `x_*`, the classified vertical divisor gives

```text
Q(U,V;x_*)=c g_*S_B^3,
det(M_1+tau nu(x_*)nu(x_*)^T)
 =tau c^2D_1g_*^2S_B^6,
```

where `g_*` is the squarefree degree-`e-6` supported factor and `S_B` is
quadratic. In characteristic three, `Q(z;x_*)/g_*(z)` has zero derivative.
This is a concrete determinant gate, not yet an exclusion: any use of its
Vandermonde/source expansion must retain signs and possible cancellation.
The proved node is
`rate_half_ca_hankel_a1_first_degree_double_root_marked_hankel_determinant_gate`.

## Cycle 104: the core-one determinant has an exact source subset sum (2026-08-11, Codex)

Write `q(z)=sum_i z^iq_i` for the primitive kernel of the first-degree
core-one symmetric middle Hankel pencil. The `e+1` coefficient vectors are
independent and form a common totally isotropic plane for both endpoint
Hankel forms:

```text
q_i^TM_sq_j=0,       s in {0,1}.
```

In contracted source coordinates, with
`v_x=(Q_0(x),...,Q_e(x))^T`, these are the two exact frame cancellations

```text
sum_x omega_x^(s)v_xv_x^T=0.
```

For the quadratic double heavy row `x_*`, Cauchy--Binet gives the marked
determinant as the explicit subset sum

```text
sum_(J subset D_res\{x_*}, |J|=d)
 Vand(x_*,J)^2 product_(x in J)mu_x(U,V)
 =c^2D_1g_*^2S_B^6.
```

This couples the sixth-order quadratic residual to the actual contracted
RS source weights. It is not yet an exclusion: the Vandermonde squares are
nonzero, but the field-valued terms may cancel. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_marked_source_frame`.

## Cycle 105: source coordinates alone cannot close the packet (2026-08-11, Codex)

The contracted source weights do not carry an unspent smooth-domain
noncancellation property. If `s_0` is the fixed core root and `v_x` are the
nonzero dual RS multipliers, contraction gives

```text
omega_x=(x-s_0)v_xa_x,       x in D\{s_0}.
```

This is an invertible diagonal change of arbitrary endpoint word values.
Moreover

```text
|D_res|=4rho-1,       2d+1=2rho-1,
```

so the residual Vandermonde map onto the complete middle-Hankel moment
vector is surjective. Every endpoint Hankel pair therefore has a contracted
RS source representation.

Consequently the Cycle-104 subset sum cannot be excluded from source
smoothness or dual multipliers alone. A valid next theorem must couple it to
column-farness, the simultaneous supported split-locator incidence, the
primitive minimal-index profile, or the Forney identities. This fence does
not say that an arbitrary represented pair is column-far or realizes the
packet. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_source_weight_surjectivity_fence`.

## Cycle 106: the quadratic packet has exact locator and center spread (2026-08-11, Codex)

At `u=4`, zero omission makes every one of the `T=rho+4` supported
specializations a squarefree split degree-`rho` locator. Their root blocks
have the exact degree sequence

```text
one fixed core point:       degree rho+4;
3rho+5 light points:        degree e;
one double heavy point:     degree e-6;
rho-7 other heavy points:   degree zero.
```

The rate-half code has minimum distance `2rho+1`, so every supported
received word has a unique codeword center within radius `rho`. If `h`
assigned centers lie on one affine codeword line, subtracting that line from
the received pencil gives an affine error pair with joint support at least
`rho+1`. Each active coordinate is nonzero at at least `h-1` slopes. The
`e-6` slopes through the heavy point have exact error weight `rho-1`; all
others have weight `rho`. Hence a center line containing `r` deficient
slopes has at most `rho+1-r` assigned centers.

It follows that a pair of supported locator blocks has at least three, four,
or five other blocks with triple union of size at least `2rho+1`, according
as the pair contains zero, one, or two deficient slopes. Otherwise their
centers would lie on the line through the first two. This is a joint
incidence/coding constraint, not yet an exclusion of the exact design. The
proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_incidence_center_spread`.

## Cycle 107: the exact block degrees have an abstract cyclic realization (2026-08-11, Codex)

The Cycle-106 degree sequence is not itself contradictory. For every
`e>=7`, take `3e+3` cyclic starts and mark seven of them with the balanced
mechanical word

```text
sigma_j=floor(7(j+1)/(3e+3))-floor(7j/(3e+3)).
```

Start three light rows at every unmarked position and two at every marked
position; each row occupies `e` consecutive blocks. Every `e`-window has
two or three marks, so a block has `3e-2` or `3e-3` light rows. Exactly
`e-6` blocks have the smaller size. Adding `x_*` to those blocks, adding
the fixed core to every block, and adjoining `rho-7` inactive points
realizes all Cycle-106 block sizes and point degrees exactly.

Thus handshake, divisibility, and degree-only support arguments cannot close
the packet. A bounded toy probe for `7<=e<=30` also found at least `e+3`
triple-union expanders for every pair, but that is numerical evidence only.
No RS word pair, center assignment, Hankel pencil, or cube identity is
constructed. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_abstract_incidence_design`.

## Cycle 108: the two-simple quadratic arm has weighted center spread (2026-08-11, Codex)

In the other `u=4` root pattern, the two heavy rows occur in exactly

```text
(e-3)/2       and       (e-9)/2
```

supported locator blocks. Their incidence sets may overlap. If
`r_gamma in {0,1,2}` counts the heavy padded roots at a slope, zero omission
and the exact excess ledger give actual unique-error weight

```text
rho-r_gamma.
```

For an affine codeword line containing a slope set `A` of assigned centers,
the column-far support argument sharpens to

```text
|A|<=rho+1-sum_(gamma in A)r_gamma.
```

Consequently a fixed locator pair has at least
`3+r_alpha+r_beta` third blocks whose triple union has size at least
`2rho+1`, between three and seven expanders. This supplies the exact joint
incidence/coding constraint for both `u=4` quadratic root patterns. It does
not constrain the overlap of the two heavy incidence sets or exclude the
packet. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_two_simple_center_spread`.

## Cycle 109: the two-simple heavy rows are square-times-cube forms (2026-08-11, Codex)

The exact vertical divisors of the two heavy rows push to base-field
parameter factorizations

```text
Q(U,V;x_1)=c_1G_1^2S_1^3,
deg G_1=(e-3)/2,       deg S_1=1;

Q(U,V;x_2)=c_2G_2^2S_2^3,
deg G_2=(e-9)/2,       deg S_2=3.
```

Here `G_i` is the squarefree supported incidence factor and `S_i` is the
pushforward of the correction divisor. The core-one marked-Hankel identity
therefore becomes

```text
det(M_1+tau nu(x_i)nu(x_i)^T)
 =tau c_i^2D_1G_i^4S_i^6.
```

In characteristic three, `Q(z;x_i)/G_i(z)^2` has zero derivative. Shared
roots among `G_1,G_2,S_1,S_2` remain allowed, so these are exact necessary
gates rather than exclusions. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_two_simple_marked_factorization`.

## Cycle 110: all unallocated quadratic regular degree is quartic (2026-08-11, Codex)

The residual regular Kronecker determinant `D_1` has degree `e-2`. At
`u=4`, the named heavy incidences account for exact rank-loss degree `e-6`.
Local Smith divisibility therefore leaves one binary quartic `E_4`:

```text
double root: D_1=a g_*E_4;
two simple:  D_1=a G_1G_2E_4,
```

where a common root of `G_1,G_2` is counted twice. Combining this with the
row factorizations gives

```text
double:   det marked=tau ac^2E_4g_*^3S_B^6;
simple 1: det marked=tau ac_1^2E_4G_1^5G_2S_1^6;
simple 2: det marked=tau ac_2^2E_4G_1G_2^5S_2^6.
```

Thus every unallocated regular rank-drop slope lies in a degree-four
divisor. The quartic may be nonreduced or share roots with all named factors;
it is not identified with `S_B^2` or `S_1S_2`. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_regular_quartic_pin`.

## Cycle 111: three cubic packets have completely supported regular determinants (2026-08-11, Codex)

For a core-free cubic double-plus-simple `u=1` packet, let

```text
P_C=product_gamma L_gamma^c_gamma
```

record the complete supported excess-recurrence divisor with multiplicity.
The regular Kronecker determinant `D_0` has degree `Delta=2e-1`. Local Smith
divisibility and the exact packet gap `w=Delta-sum c_gamma` give

```text
D_0=a P_C E_w,       deg E_w=w.
```

In the four packet rows, `w=1,0,0,0`. Therefore the last three regular
determinants are exactly `a P_C`; the first has only one additional linear
factor. Every bordered determinant sharpens to

```text
det M_0[x]=a P_C E_w Q(U,V;x).
```

The linear factor may repeat an already supported slope and is not
identified with the degree-one Picard correction. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_free_cubic_gap_one_regular_factor_pin`.

## Cycle 112: the completely supported cubic packets are first-jet transverse (2026-08-11, Codex)

Fix a supported slope with recurrence loss `c`, specialized factorization
`Q_gamma=Q_min R_gamma`, and no zero of the residual `E_w` factor. Exact
regular-determinant order forces all `c` positive local Smith exponents to
equal one. The derivative moment form therefore gives the perfect pairing

```text
B_gamma(A,B)=dot Phi(Q_min^2AB),
deg A<=c-1,       deg B<=c,

rank B_gamma=c,
rad_right(B_gamma)=span{R_gamma}.
```

At rank loss one this is the explicit first-jet test

```text
dot Phi(Q_min^2(X-r_gamma))=0,
dot Phi(Q_min^2)!=0.
```

The pairing holds at every supported slope in the three `w=0` packets. The
first `w=1` packet has at most the single slope cut out by `E_1` as an
exception. This turns the exact determinant factors into field-valued local
constraints; it is not yet a packet exclusion. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_free_cubic_gap_one_first_jet_perfect_pairing`.

## Cycle 113: the cubic first jet lives on a two-error support difference (2026-08-11, Codex)

Let `S_gamma` be the exact support of the unique error at a supported slope,
so `|S_gamma|=rho-c_gamma`. Subtract the affine codeword line through the
unique centers at distinct slopes `alpha,beta`. The derivative moment form
at a transverse positive-loss slope `alpha` becomes

```text
B_alpha(A,B)
 =sum_(x in S_beta\S_alpha) mu_x A(x)B(x),
mu_x!=0.
```

Since this pairing has rank `c_alpha`,

```text
|S_beta\S_alpha|>=c_alpha.
```

If equality holds, the square Vandermonde system and the known right radical
force

```text
roots(R_alpha)=S_beta\S_alpha.
```

Thus equality identifies every newly introduced error location with an
excess-recurrence root. In each of the three `w=0` packets, transversality is
universal and every locator-support pair satisfies
`|S_alpha union S_beta|>=rho`. The strict branch retains the exact weighted
moment system; no positivity is assumed. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_free_cubic_gap_one_two_slope_source_vandermonde_gate`.

## Cycle 114: column-farness kills the weak equality and pins the true boundary (2026-08-11, Codex)

The codeword line through two unique centers differs from the received
pencil on exactly `S_alpha union S_beta`. Column-farness therefore gives

```text
|S_alpha union S_beta|>=rho+1,
|S_beta\S_alpha|>=c_alpha+1.
```

Thus Cycle 113's `c_alpha`-source equality branch never occurs in a retained
packet. If the union has its true minimum `rho+1`, the source difference has
exactly `c_alpha+1` points. Its Vandermonde nullspace is one-dimensional,
and the first-jet radical forces

```text
mu_xR_alpha(x)=kappa/P_(alpha,beta)'(x),       kappa!=0.
```

Equivalently, the actual error values satisfy

```text
lambda_x e_beta(x)Q_min,alpha(x)Q_alpha(x)
P_(alpha,beta)'(x)=kappa(beta-alpha).
```

No difference point is then a root of `R_alpha`. Larger unions retain a
higher-dimensional cancellation space, so support cardinality alone is now
exhausted; the next useful inputs are these weights and higher coefficient
jets. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_free_cubic_gap_one_column_far_barycentric_gate`.

## Cycle 115: two-support union excess controls the complete coefficient rank (2026-08-11, Codex)

Expand the primitive kernel as `Q=sum_i z^iQ_i` after moving a supported
slope `alpha` to zero. Pairing the complete coefficient recurrence, including
the terminal equation `M_1q_e=0`, with the specialized left apolar kernel
gives a weighted Vandermonde annihilation on
`X=S_beta\S_alpha`. Therefore

```text
rank (Q_i(x))_(x in X,0<=i<=e)
 <=|S_alpha union S_beta|-rho.
```

This holds in all four cubic gap-one packets and does not require local Smith
transversality. On the minimum-union boundary `rho+1`, the rank is exactly
one, so all `c_alpha+1` nonzero row forms

```text
Q(-;x),       x in S_beta\S_alpha,
```

are proportional and have the same parameter zero divisor with
multiplicity. At union `rho+s`, their coefficient rank is at most `s`.
This reduces the next gate to point separation or a classification of
low-rank fibres of the coefficient map; neither is assumed here. The proved
node is
`rate_half_ca_hankel_a1_first_degree_core_free_cubic_gap_one_two_slope_coefficient_clone_rank_gate`.

## Cycle 116: symmetry raises every quadratic pair union to `rho+2` (2026-08-11, Codex)

For the symmetric core-one residual middle Hankel pencil, a slope of rank
loss `r_alpha` has `r_alpha+1` specialized left-kernel multiples. Applying
the complete coefficient chain to `S_beta\S_alpha` gives

```text
|S_alpha union S_beta|>=rho+2,

rank (Q_i(x))_(x in S_beta\S_alpha,0<=i<=e)
 <=|S_alpha union S_beta|-rho-1.
```

This holds in both quadratic `u=4` root patterns. At pair union `rho+2`,
all residual row forms on the difference are proportional. More importantly,
the joint support of any codeword line through two assigned centers now has
size at least `rho+2`. Therefore a line containing `h` assigned centers
satisfies

```text
2h<=rho+2-sum r_gamma.
```

For every fixed locator pair, at least

```text
ceil((rho+6+r_alpha+r_beta)/2)
```

other slopes have triple union at least `2rho+1`. This replaces the previous
constant lower bound `3+r_alpha+r_beta` by a linear-size bound. The Cycle-107
abstract cyclic design was tested only against the old condition and no
longer fences this route. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_two_slope_coefficient_rank_spread`.

## Cycle 117: the explicit cyclic quadratic design violates the spread (2026-08-11, Codex)

The Cycle-107 construction remains a valid realization of the raw locator
degree sequence, but it is not compatible with the coefficient-chain
constraints. For every `e>=14`, one adjacent deficient pair has exactly
`e+3` expanding third blocks. Cycle 116 requires at least

```text
ceil((3e+6)/2)>e+3.
```

Thus the explicit support-only countermodel is retired. This is not yet an
exclusion of every abstract design with the same degrees; global incidence
moments still leave slack. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_cyclic_design_spread_exclusion`.

## Cycle 118: sharp quadratic pairs are clone-barycentric (2026-08-11, Codex)

If a pair attains the sharp actual-support union `rho+2`, the Cycle-116
rank bound is one. Hence the `r_alpha+2` rows on
`S_beta\S_alpha` are nonzero proportional coefficient forms. They are light
rows, so they share the same squarefree set of `e` supported locator slopes.
The complete coefficient chain then fixes the endpoint errors up to scale:

```text
(f_beta-c_beta)(x)
 =kappa/((x-s_0)v_x lambda_x L_X'(x)).
```

The reverse orientation gives the corresponding clone class and formula on
`S_alpha\S_beta`. This is the field-valued interface needed to compare the
sharp boundary with the Forney numerator; it does not assert that a sharp
pair exists. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_minimum_pair_clone_barycentric_gate`.

## Cycle 120: the sharp quadratic pair boundary is empty (2026-08-11, Codex)

The Cycle-118 clone class cannot occur. Its `e` common supported locator
slopes, together with one endpoint, are forced onto one codeword pencil by
the full-locator triple-union bound and minimum distance. After removing the
fixed core point, every point in that pencil's joint support is light and
must miss exactly one of the `e+1` selected slopes. The resulting missing
incidence count forces deficit `e-2` on the pencil, contradicting the exact
packet-wide deficit `e-6` in both quadratic root patterns. Therefore

```text
|S_alpha union S_beta|>=rho+3,
3h<=rho+3-sum_(gamma in A)r_gamma.
```

Every pair has at least

```text
ceil((2rho+9+r_alpha+r_beta)/3)>=2e+3
```

expanding thirds. The next minimum pair boundary has coefficient-row rank
at most two. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_sharp_pair_exclusion`.

## Cycle 121: the new minimum boundary is one exact rank-two split pencil (2026-08-11, Codex)

At pair union `rho+3`, put `X=S_tau\S_sigma` in the orientation selected by
the padded-heavy ledger. The complete coefficient-chain nullspace is exactly
two-dimensional. Its barycentric basis gives independent degree-at-most-`e`
parameter forms `A,B` with

```text
eta_x L_X'(x)Qbar(-;x)=A+xB.
```

Rank one is impossible by the Cycle-120 center-line count, so the row
coordinate is injective. Every row form is squarefree and supported. If
`G=gcd(A,B)`, `g=deg G`, and `m=|X|=r_sigma+3`, their residual root sets are
pairwise disjoint and

```text
g+m(e-g)<=3e+3,
g>=max(1,ceil((r_sigma e-3)/(r_sigma+2))).
```

Every root of `G` is center-owned by the endpoint codeword pencil. The
positive-deficit cases therefore carry a forced linear-size common
parameter divisor; the zero-deficit three-row case remains the least
constrained. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_minimum_pair_rank_two_barycentric_normal_form`.

## Cycle 122: both orientations force a linear-size common gcd (2026-08-11, Codex)

The source slope lies outside the complete row-root union, sharpening the
positive-deficit root budget. At zero endpoint deficit the forward and
reverse gcd root sets exchange the endpoints and share all nonendpoint
roots. Their six residual row-root sets are pairwise disjoint: a shared
forward/reverse residual root would force its center onto the endpoint
pencil, where it must contain every point of both differences. Hence every
minimum pair has an oriented center-owned gcd satisfying

```text
max(r_alpha,r_beta)=0:  g>=ceil((3e-2)/5),
max(r_alpha,r_beta)=1:  g>=ceil((e-2)/3),
max(r_alpha,r_beta)=2:  g>=ceil((e-1)/2).
```

The zero-deficit official floor is `g>=109951162778`. The remaining task is
to compare this large divisor with the heavy-row cube/Forney factors. The
proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_minimum_pair_oriented_gcd_coupling`.

## Cycle 123: actual supports couple every deficit pattern (2026-08-11, Codex)

The difference rows are light and padded heavy rows are absent from actual
errors. Replacing full-locator estimates by actual-support unions removes
the orientation restriction: both minimum-pair row families have rank two
for every endpoint-deficit pattern. Their gcds exchange the endpoints and
share all other roots.

Every residual row root has deficit zero. Indeed, one difference point plus
the fixed core and one padded heavy deficit already force the third center
onto the endpoint codeword line, where it would be a common gcd root. The
same actual-support argument makes all forward and reverse residual root
sets pairwise disjoint. If `R=r_alpha+r_beta`, their common gcd degree `g`
leaves exact supported-slope slack

```text
s=(R+5)g-(R+3)e+2>=0.
```

All packet deficit `e-6` is localized to the common center line or this
slack. The line itself satisfies `3g+d_L<=3e-2`, yielding the stronger
arm-specific floors `(BHL8)--(BHL9)`. The remaining task is no longer a
generic gcd/heavy comparison: it is to show that the exact slack cannot
absorb the supported heavy divisor, or to exclude the resulting localized
intersection profile. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_minimum_pair_bidirectional_heavy_incidence_localization`.

## Cycle 124: the `rho+3` quadratic boundary is empty (2026-08-11, Codex)

For a hypothetical minimum pair, the common light intersection outside the
core has `3e-R-5` rows. No residual split-pencil slope can support one of
these rows, and a slack slope supports at most one, only at deficit zero.
Their global degree-`e` demand first forces the bidirectional gcd degree to
its maximum `g=e-1`.

At that maximum, the common center line has exactly `e` slopes. Its missing
incidences require

```text
3e-R-6+d_L
```

outside incidences on common rows, while the exact packet deficit leaves
only

```text
e-R+3+d_L
```

eligible zero-deficit slack slopes. The resulting `2e<=9` is impossible on
the official row. Hence

```text
|S_alpha union S_beta|>=rho+4,
4h+sum_(gamma in A)r_gamma<=rho+4
```

for every pair and every assigned-center line. This is a complete profile
removal; the next boundary is rank three at union `rho+4`. The proved node
is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_minimum_pair_exclusion`.

## Cycle 126: the quadratic pair floor jumps to `3rho/2-1` (2026-08-11, Codex)

For a pair with actual-support union `rho+j`, split the exact global
degree-`e` incidence on its light union between centers on and off the
endpoint codeword line. The line misses `j+r_gamma` points at slope
`gamma`; an off-line slope meets at most `j-r_gamma-2` noncore union
points. Eliminating the number of line centers gives the necessary concave
quadratic inequality `F_e(j)<=0`.

At both endpoints of

```text
4<=j<=rho/2-2
```

the polynomial is strictly positive, hence the complete interval is empty.
Therefore

```text
|S_alpha union S_beta|>=3rho/2-1=824633720831
```

on the official row. Every assigned-center line has at most three supported
slopes, and a three-center line has total deficit at most one. Thus every
pair has at least `rho+1` expanding thirds. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_macroscopic_pair_union_floor`.

## Cycle 127: the sole floor case yields at least `2e` minimum words (2026-08-11, Codex)

A pair above the floor, with union at least `3rho/2`, has only its two
endpoint centers on the corresponding codeword line. A pair attaining
`3rho/2-1` instead forces exactly one third line center and total line
deficit at most one.

For the `3e` off-line slopes in this equality case, let `a_delta` be the
actual triple-union excess over `d_min=2rho+1`. Exact global incidence and
the packet deficit give

```text
sum_(delta off line)a_delta=e.
```

At least `2e` slopes therefore have zero excess. For each, the affine second
difference of its assigned center with the endpoint centers is a nonzero RS
codeword supported on exactly `2rho+1` positions. Minimum distance makes it
an exact minimum word, whose `k-1` zero positions determine it up to scalar.
The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_extremal_three_center_minword_reduction`.
## Round-33 close addendum (2026-08-11, coordinator-audited): the four banks reconciled

**BANK 3 (rh_sat3_realizability) — ROUTE DECIDED: (SAT3) IS
REALIZABLE; the vacuity branch is DEAD.** Exhaustive at m = 1,
q = 17 (16 families, all carrying non-degenerate column-far Hankel
realizations, (SAT1)-(SAT5) exact), reproduced at five more fields.
THE COUNTING STACK IS SIMULTANEOUSLY TIGHT on the witness ((AO1) =
(MI2) = (ERC2) = (ERC4) = 5 = T, all equalities) — the 9/4 is a
route CEILING, not slack. CATCH-24C settled: both lanes count the
SAME T (PROVED, (HS3)) but LB1 does NOT transfer (corank-0: its
petal structure forces d_x = r > e). REGRESSION-TEST PRINCIPLE OF
RECORD: every proof of the strict target T <= rho+1 must be
m-dependent and must FAIL at m = 1; the witness is the test
((NEWCAP) passes — Lmin(0) = 0 there). TCAP-DIM posed (realizable
iff m <= 2; moduli excess -13, -1, +35, +95...), blind spot named;
THE DECISIVE EXPERIMENT: settle m = 2 (reduced to 40 parameters vs
39 rank conditions — the G2 system). e = m is the entire difficulty
(e < m is (ERC2)-closed; the e = 1 Kummer ladder stalls at 4).
[UPDATED (round 34): the G2 experiment RAN — fields-searched
NEGATIVE at m = 2 (not a theorem); the posed count omits the
automorphism quotient (dim >= 4, >= 6 generically) and the
corrected excess at m = 2 is +3..+5; TCAP-DIM re-posed with
boundary m <= 1. See the round-34 (SAT3) m=2 decision addendum.]

**BANK 1 (rh_psi_degree) — THE 8/5 IS ONE SLOPE.** (AO1) is exactly
the aggregate criterion "proved per-slope floor > forced mean
spend"; the shortfall rho*(mean_X - need_X_real) = 4m - def_in +
o_g + o_h for EVERY a (coordinator-verified): the 9/4/7/4/9/8/8/5
are four readings of ONE a-independent constant = rho+1 = one
slope's locator mass. The missing e = m lives in the NON-SPLIT part
of h_gamma: **(NS-m)** (every type-2 h_gamma carries >= m of its
degree in irreducible factors of degree >= 2) IMPLIES closure of
residual (ii); sub-goal #{j=0 type-2} <= 6. Symmetric moments
walled (the second moment is the exact Cauchy-Schwarz equality
case); (M2b) real but short by 7.5%.

**BANK 2 (rh_bivariate_system) — THE W-LAYER IS FENCED BY WITNESS.**
An explicit m = 2 configuration (T = rho+2, a = w* = a* = 7m-1,
every incidence axiom + the bivariate system, two fields) shows the
W-restricted system cannot exclude the failure configuration. Its
content is (BIV-CURVE) (type-2 classes = fibres of a
degree-(3m-3) dimension-m linear series; at m = 2 verbatim the xr
lane's pencil predicate — transport candidate); per-slope it is
banked (C2). LAYER A (the full-domain bidegree-(rho,m) Q(Z,x);
deficit 12m^2-4m) KILLS the exhibit — LAYER A IS THE INSTRUMENT,
and it is the same object as (NS-m): banks 1+2 converge. Lesson:
random-embedding censuses have q^{-Theta(m^2)} power —
construction or nothing. The m >= 3 (BIV-CURVE) feasibility is the
open fork (heuristic says infeasible for m >= ~16; the m = 2
witness says the heuristic fails at small m). [RESOLVED at m = 3
(round 34): REALIZABLE, explicit two-field witness — see the
round-34 (BIV-CURVE) addendum below; m = 4 remains open.]

**BANK 4 (rh_moving_kernel) — R-MOVING WITHDRAWN (see the FALSE
marker above).** What replaces it: the STACKED RANK h_r
(rho <= h_r <= 2rho; dim K_0 = r+1-h_r; moving increment
h_r - rho <= rho) [ANNOTATED (round 36): h_r = rho + deg(e_1/e_0)
on the forced common support when that ratio is a polynomial of
degree <= rho, and 2rho otherwise (210/210, 5 shapes, 5 fields);
h_r is INDEPENDENT of the support size and prices only the fibre
floor's decay rate ceil((r+1)/d), not the floor's existence —
see the round-36 R-HRLOW addendum]; the correct sufficient condition for a fixed
generator (p* + p_gen <= R — fails generically by 7/6); **the FG
stratum** (fixed squarefree generator P, rho < p <= 2rho) with a
genuinely new normal form — the pencil collapses to a rho x p
SCALED VANDERMONDE, the key equation C_gamma*sigma = h mod P, and
(MI1) RESTORED after reduction (78/78) while (MI2) PROVABLY cannot
follow (the reduced ring is a FIELD — no divisors to count); on FG
the measured T = q kills T <= rho, T <= p, T <= r+1 as candidate
bounds. NEW RESIDUALS: R-FG (the line-in-Lambda intersection
count); **R-PSTAR [RESOLVED YES, round 34 r34_pstar, coordinator-replayed
— and the parenthetical equivalence here was FALSE: FG requires
p* <= 2rho = R/32, a factor 16 stronger than p* <= R/2
(h_r <= min(p*, 2rho) unconditionally); an intermediate stratum
2rho < p* <= R/2 exists with a generically-fixed generator but
non-principal K_0 (five exhibited instances). FG IS NONEMPTY AT
RAZOR SHAPE: witness A (y_0 = e_{2rho-1}, y_1 = e_{rho-1};
K_0 = x^{2rho}F[x]; column-far unconditionally, any field, any D)
and witness B (P* = P_1 P_2, P_1 irreducible of degree 2^34;
SQUAREFREE, so FG3/FG4 apply verbatim). Column-farness is FREE on
the low-p* locus (excludes a 2^-1.15e12 fraction of P* choices).
R-KER is NOT the sole residual; R-FG is live with razor
coordinates. The codimension law codim{p* <= p} = 2R-3p calibrated
at 10 points (max dev 0.090); the FG3 descent widened to all
p* <= r with P* squarefree (1586/1586); LB1 is GENERIC
(p* = r+1 = ceil(2R/3), 3591/3591) [SCOPE-CORRECTED (round 35):
that measurement is at LB1's own k=2 small cell and does NOT
transfer — at razor-faithful shape (a > R+1, a-1 > r)
p*(LB1) = max(rho+1, floor((R+2)/2)) = floor(R/2)+1, 5/5 shapes;
see the round-35 R-FG-RAZOR addendum]; the round-33 "on FG measured
T = q" narrowed — the saturation tracks mu_1 = C(n,r)/q^rho, not FG
[NARROWING CORRECTED AGAIN (round 36): TOO GENEROUS — there is a
mu_1-FREE, field-size-independent excess on negation-closed D
(T = 95 vs r+1 = 9 at mu_1 = 1.26e-7, column-far razor-faithful;
mechanism = orbit-invariant even locators, count C(m-1,r/2-1)
exact; requires ceil(rho/M) = 1, dead at rho = 2^34 by 2^33-1
conditions — see the round-36 R-HRLOW addendum)]
membership (T <= r+1 survives at 2 of 4 cells; the three universal
bounds stay dead); q_crit ~ 2^64: below it the column-far locus is
measure-zero and every random model in this lane is void
[SCOPE-CORRECTED (round 35): a RAZOR-ROW constant —
theta_2 = n*H2(r/n)/(2rho) = 64*H2(63/128) = 63.988728 at
a = k+2^34 only; at the official candidate row's OWN shape the
same formula gives 1.6226; the key-equation threshold is
theta_1 = 2*theta_2 = 127.977457, and every admissible official
row (q > 2^128) is subcritical for BOTH]]**. R-DEEP/R-KER/R-LINEDEGREE
unchanged. Round 32's report is noted internally inconsistent (its
0/1700 (HK1) data contradicts its own forced-fixed claim) — the
audit cadence's sixth consecutive round of catching banked text.

**ROUND-33 STATE OF THE OPEN CONTENT:** the type-2 frontier = layer
A/(NS-m) (with the m = 1 regression test mandatory) + the G2 m = 2
decision; the far-CA frontier = R-KER + R-PSTAR (+ the FG key
equation as its coordinates); the located crossing itself. No
status flips; census unchanged 231 = 167/37/27.

## Cycle 143: the paired weld is a local cross-ratio certificate (2026-08-11, Codex)

For the two `A=1` quadratic pair boundaries, label every nonincidence edge
by

```text
c_(delta,x)=P_x(delta)/F_delta(x).
```

The sparse weld has nullity one exactly when these labels are a
multiplicative coboundary. Thus every nonincidence rectangle must satisfy one
explicit cross-ratio identity. In the extremal profile, any three selected
fiber neighborhoods share at least `6+d_A` rows, so the rectangle identities
alone certify every cycle. In the strict profile, rectangles plus explicit
fiber-transition triangles are complete.

A failed local identity gives full weld rank and excludes the boundary. If
all identities pass, they reconstruct the unique projective scalar vector
that must then pass the fixed-domain coefficient-MDS and retained
source/Hankel gates. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_paired_scalar_weld_cross_ratio_cycle_certificate`.
## Round-34 layer-A addendum (2026-08-11, coordinator-audited): (NS-m) refuted-and-restated; the factor-degree dichotomy PROVED

The r34_layer_a pilot (REPORT + FABLE_AUDIT in
notes/pilots_20260811/r34_layer_a/; coordinator replays: the m=1
exhaustive tables identical, the theorem's combinatorial core 0
violations over m = 1..40, the dichotomy algebra hand-verified):

- **(NS-m) AS STATED IS FALSE** — refuted exhaustively at m=1 on
  the 16 realized (SAT3) pencils (the round-33 regression test
  doing its job): at the realized a* = 6 the degree budget d = 0
  makes every h_gamma a nonzero constant (0/480 both stated forms);
  at the planted a = 7 the F_q-root-count form fails 4800/5280.
  The two stated forms (root count vs irreducible-factor gloss) are
  INEQUIVALENT (they agree only when deg h = d). Reach of the
  refutation LIMITED and declared: the m=1 counterexamples live in
  the a = 2rho stratum banked empty for m >= 2, and the m=1 killing
  mechanism (deg_Z G = m-1 = 0) has no m >= 2 analogue.
- **THE RESTATEMENT OF RECORD — (NS-W-m):** for every type-2 slope,
  under d = a-(4m+2) >= m: h_gamma has at most d-m roots IN W
  (with multiplicity). Still implies closure (X <= roots-in-W);
  strictly weaker than (NS-m); SURVIVES the regression 5280/5280;
  the d >= m hypothesis is free at the argmax for every m >= 2.
  (NS-m) is retired to a corollary of (NS-W-m) + a bound on Rout —
  and Rout is now THE deciding question (bank-1's measured
  Rout <= 3 in 648/648: theorem or sample? cheap and decisive).
  [RESOLVED (round 35): SAMPLE — and the premise was false as
  printed: bank 1's own banked cell d3_m2_q193.txt:70-71 records
  maxRout = 4. Rout is FREE (null-distributed; the trivial degree
  bound is attained) and it enters the exact closure criterion
  (CLO-m) with a POSITIVE sign, so bounding it was backwards.
  See the round-35 Rout/layer-A addendum.]
  Bank-1's falsifier F4: FIRED in the F_q reading at m=1 (4800
  instances), NOT fired in the W reading — the readings disagree.
- **THE WRONSKIAN INSTRUMENT IS WALLED, with the number:** a totally
  split fibre is reduced hence unramified — the rigidity spends
  NOTHING of either Pluecker budget (W-picture budget/demand ->
  5/12 exactly as pre-registered; A-picture slack ~3m).
  Ramification measures multiplicity; (NS-*) measures rationality;
  independent.
- **THE ROUND'S PROVED THEOREM (FACTOR-DEGREE DICHOTOMY)
  [ALREADY-PROVED IN-REPO (round-35 subtraction catch): this IS
  the PROVED node rate_half_ca_hankel_endpoint_rational_branch_
  exclusion, (CPR3)-(CPR5) — unique r = 4e-1 component, all
  others balanced, e_(i*) >= ceil((3m+1)/4), sum of the rest <=
  floor((m-1)/4), no splitting into m rational branches. The
  round-34 pilot's CATCH-24A missed it and so did my audit; the
  round-34 content stands as an independent re-derivation +
  exhaustive check, not a new theorem]:** in the
  layer-A variables, deg_x additivity + fibre disjointness force
  T*rho - O <= sum_j min(T*d_j, N*m_j) with sum_j d_j <= rho over
  the F_q(x)-irreducible factorisation of the kernel biform Q.
  Consequences (0 violations, every partition profile, m = 1..40):
  exactly ONE "small" factor; **Q cannot split into linear factors
  over F_q(x) for any m >= 2** (the m slope branches are never all
  rational functions of x); the surviving profiles carry an
  irreducible factor of Z-degree >= ceil((3m+1)/4) (EXACTLY
  attained); at m = 2,3,4 Q is IRREDUCIBLE over F_q(x); m=1 sits
  on the boundary realized (one branch, T*delta = 15 = N-1).
  Hypotheses all banked (the PROVED RNC node + the saturation
  rigidity's nonvanishing line). The (3m+1)/4 is the truth of the
  counting system; realizability of survivors untested.
- **STRUCTURE:** layer A and (BIV-CURVE) are ORTHOGONAL — 80/80
  fibre-constructor candidates killed at full span rank 8 (the
  W-layer's structured solutions land maximally far from layer A);
  the layer-A controls pass in the strong form (nullity exactly 1
  with the predicted kernel vector, 16/16; three builders agree
  320/320). The pilot's near-claim of the PROVED RNC node was
  caught by its own CATCH-24A (the "span <= m+1" reading IS
  rate_half_ca_hankel_endpoint_rational_normal_kernel_curve).
- **NEXT INSTRUMENTS OF RECORD:** (1) push the dichotomy into the
  RNC node's own named gate (the multiplicative-domain structure of
  D = mu_N — untouched by the cardinality-only count; survivors are
  few: 1 profile at m = 2,3,4); (2) decide Rout. No status flips.

## Round-34 (BIV-CURVE) addendum (2026-08-11, coordinator-audited): REALIZABLE at m = 3; the W-layer fence extends; the boundaries diverge

Pilot r34_bivcurve_m34 (round 34, bank 3; replay byte-identical,
two fields). Everything below is (SAT3)-conditional (T = rho+2) and
W-layer only.

- **(BIV-CURVE) IS REALIZABLE AT m = 3** — the round-33 open fork
  resolves POSITIVELY by explicit witness (F_97 and F_193;
  T = rho+2 = 13, a = w* = a* = 7m-1 = 20, every banked incidence
  axiom measured exactly, (BIV-CURVE) checked directly on the
  explicit G, bivariate system rank 39 / nullity 1 with an
  admissible kernel and the predicted mu). **The W-layer fence now
  covers m in {2,3}: no proof from the banked incidence axioms plus
  the W-restricted bivariate system can exclude w* = a* = 7m-1 at
  m = 3. The type-2 exclusion at m = 3 must come from layer A
  alone** — consistent with this round's orthogonality result
  (layer A ⊥ (BIV-CURVE), 80/80 above) and with round 33's "LAYER A
  IS THE INSTRUMENT".
- **THE MECHANISM ((SPLIT-m) + involution), new in this lane:**
  G(Z,x) = prod_{j=1}^{m-1}(u_j(x)Z - v_j(x)), deg u_j,v_j <= 3 —
  deg_Z = m-1 exact and deg_x <= 3(m-1) = 3m-3 meets the (BIV-G)
  budget with equality at EVERY m; the m = 2 exhibit is its
  one-factor case. The witness is its sigma-symmetric
  specialisation (sigma(x) = -x on mu_48, psi = phi o sigma): each
  sigma-orbit carries one shared slope pair, so 20 points cost 11
  slopes. Ramification is FREE in this class (every fibre splits by
  construction) — the heuristic's cost model does not see it. The
  first-moment heuristic (log2 E = +176.5 at m = 3, round 33) is
  CONFIRMED at m = 3; its failure mode is the inference step, not
  the small-m count.
- **m = 4 IS OPEN — searched-negative over ONE named ansatz class**
  ((SPLIT-4) with sigma(x) = -x and the forced 3+3+2 degree split;
  1600 draws, two fields, truncated DFS): NOT a theorem. The named
  obstruction is NOT the ramification budget — it is the (OV) pair
  cap 2rho-a = m-1 = 3 forcing the 12 shared slope-TRIPLES to form
  a linear (partial-Steiner) 3-uniform hypergraph (measured ceiling
  7 of 12), plus even m forcing a sigma-invariant factor that is
  Möbius in u = x^2, hence injective on orbits (one fresh slope per
  orbit; the cross-coincidence supply falls short by ~an order).
  CAUTION for m-uniform readings: at m >= 5 the cap m-1 >= 4
  re-admits tuple multiplicity 4, so the linearity constraint is
  SPECIFIC to m = 4; the odd/even parity prediction rests on two
  data points (falsifier: m = 5). PRIOR ART (coordinator catch):
  the repo already holds a PROVED linear-3-uniform-hypergraph
  compiler in the u1_x4 lane
  (background/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LINEAR_HYPERGRAPH_COMPILER.md
  — pair-uniqueness forcing linearity); transport candidate for any
  m = 4 decision attempt.
  [CORRECTED (round 35): the NAMED OBSTRUCTION IS MEASURED INERT —
  ablating the linearity constraint moves the ceiling by ZERO
  triples at both fields, and the abstract selection layer is
  DECIDED SATISFIABLE (Z_12 difference-set certificate {i,i+1,i+3}:
  12 triples, 3-regular, linear, 12 slopes, SDR); the binding
  constraint is the <= rho slope budget alone (arithmetic
  value-confinement). The ceiling 7 was SOFT (8 at matched budget,
  9 with value-prescribed pencils, two fields). The m=5 parity
  falsifier FIRED: (SPLIT-5)+sigma all-swapped — no invariant
  factor forced — reaches only 7/15 and 6/15, so the odd/even
  prediction is REFUTED as a realizability predictor (the
  invariant-factor mechanism is real but subdominant). Law of
  record: coincidence demand 3m^2-7m+2 (8, 22, 42 at m = 3,4,5)
  against a supply FLAT in m — m = 3 is where the curves cross.
  See the round-35 (BIV-CURVE) m=4 addendum.]
- **THE BOUNDARIES DIVERGE (registered prior 0.12, resolved NO):**
  TCAP-DIM (full Hankel realizability; posed boundary m <= 2,
  excess +35 at m = 3) and (BIV-CURVE) (W-layer incidence;
  realizable at m = 3) part company at m = 3. Every joule spent on
  the W-layer at m >= 3 is spent on the weaker layer; the
  exclusion instruments of record are layer A and realizability.
- **(OUT-m), POSED — the first LOWER bound on type-2 W-incidence
  in this lane, WITH COORDINATOR CORRECTIONS:** at a minimising
  pair union with (SAT1)-(SAT4), T = rho+2, a = 7m-1, writing
  X'_g = |S_gamma ^ (S_g D S_h)|, X''_g = |S_gamma ^ (S_g ^ S_h)|:
  **X'_gamma + 2 X''_gamma >= m-1 - eps_gamma**, where eps_gamma =
  total saturation deficiency on S_gamma, eps_gamma <= 1+O per
  slope. (Proof: place the (rho-X_gamma)(m-1) - eps outside
  block-pair incidences of S_gamma into the rho-1 other type-2
  blocks at pair capacity (m-1) - I_in each; audited.) CORRECTIONS
  to the pilot's statement: (i) the aggregate rider
  "sum_gamma eps_gamma <= 1+O" is FALSE — a deficient point outside
  W charges every type-2 block through it, so the correct aggregate
  is (m-1)(1+O); the pilot's own witness (deficient point = the
  outside pair) has sum eps = 2 > 1+O = 1. (ii) The corollary
  "X_gamma = 0 impossible" requires 1+O < m-1, i.e. O <= m-3 (at
  m = 3: O = 0 — satisfied by the witness and by the profile-target
  derivation, but NOT free in general). Checks: tight on the two
  degree-1 H-slopes of the m = 3 witness (X' = 2 = m-1); consistent
  with the m = 2 exhibit's min X = 1 (its deficient point is INSIDE
  W, so eps = 0 off that slope). It killed X = 0 slope-padding and
  two of the pilot's own designs; it is a constraint on the
  configuration space, not progress on residual (ii)'s direction.
- **DEAD SUB-ANSATZE (recorded so they are not retried):** the
  rank-2 pencil-of-quadratics G = N(Z)f(x) + M(Z)g(x) is DEAD at
  m >= 3 (fibres of size <= m-1 force >= 2(m+... distinct pairs
  > rho slopes at m = 3: 18 > 11); the explicit phi = x^4, psi =
  x^2 design dies on the per-side cap (a full mu_4-coset with a
  middle point forces |S_gamma ^ S_g| >= 3 > m-1).
- **SCOPE FENCES:** layer A was NOT run on the m = 3 witness (the
  banked expectation from the orthogonality result is that it dies
  there; unmeasured); the unsaturated exception was never exercised
  (O = 0, deficient point outside W); no random-embedding census
  was run; two fields is not q-uniformity; nothing here bears on
  (SAT3) itself.

## Round-34 (SAT3) m=2 decision addendum (2026-08-11, coordinator-audited): fields-searched negative; TCAP-DIM re-posed to m <= 1; the (L2) realization gate promoted

Pilot r34_m2_decision (round 34, bank 4; d1 replay byte-identical;
the pilot also replayed round 33's m=1 exhaustive + realization
scripts BYTE-IDENTICALLY, so the m=1 realization theorem now
carries independent replay evidence). **A fields-searched negative
is NOT a theorem** (q in {97,193,257}; the target stratum's
expected codimension ~13 makes sampling powerless either way).

- **THE VERDICT BY LAYER.** (L0) combinatorial: FREE — the simple
  design is unique up to isomorphism (420 labelled, 1 class,
  exactly K_9 - (P_3 + 3K_2)); multigraph designs abundant (capped
  enumeration). (L1) curve-from-design: NEVER OPENED — the 62x24
  system had rank 24 (full; need <= 23) in 400 random + 200
  structured draws, two fields. Forward search: 480,000 nets
  carrying three prescribed-split members reached max n7 = 4
  against the 8 the design forces — and the cost of the 4th split
  member (8.8e-6) matches the UNSTRUCTURED random-polynomial rate
  (q*C(32,7)/q^7 ~ 4e-6) to a factor 2: **the net structure buys
  nothing at m = 2**, against the 14% (10^4-fold) coherence the
  m=1 fibre structure buys. Exact witness detector (audited): the
  design forces >= 8 totally split members (62 endpoints on 9
  vertices of degree <= 7), so **n7 <= 7 certifies a net hosts no
  design** — no heuristic scoring enters.
- **THE SYMMETRY ESCAPE HATCH, CLASSIFIED AND CLOSED:** only
  cyclic orders k in {2,3} can host the design (slope-orbit +
  fixed-slope root-congruence u = 0,1 mod k + domain-cardinality
  arithmetic; coordinator-checked at k = 3,4,7) — maximum
  concentration factor 3, so a symmetric witness still needs >= 3
  independent ~1e-5 splitting events. **The m=1 coset mechanism is
  structurally dead at every m >= 2:** tau = id forces pairwise
  disjoint locator sets, i.e. d_x <= 1, i.e. T*rho <= N — which is
  EXACTLY the banked R4 fence (63 > 32 at m = 2). Agrees with (does
  not extend) the PROVED separated-pullback exclusion at the
  official endpoint. The k=4 family reached n7 = 8 = rho+1 at
  q=193 — the strict target attained at the LOCATOR layer — with
  (L2) nullity 0: symmetry concentrates split members and
  simultaneously sparsifies the parameter coefficients, and (L2)
  charges for sparsity.
- **THE (L2) GATE — the round's sharpest fact.** The syndrome
  realization layer M(Z)Q_Z = 0 is (m+2)(4m+1) equations on
  2R = 16m unknowns: **overdetermined by 4m^2-7m+2 = -1, +4, +17,
  +38, ... — m = 1 is the ONLY underdetermined case** (which is
  exactly why round 33's exhaustive m=1 scan realized all sixteen
  families). Measured: nullity 0 on 60/60 random curves per field
  at m=2; ZERO genuine e=m=2 objects in 2,800 structured + random
  curves over two fields — every apparent hit is one predicted
  degenerate family (shared domain root, weight-one error, generic
  rank 1, s != 0 — forbidden by (SAT1); rate (49/32)/q CONFIRMED:
  1.58%/1.43% at q=97, 0.79%/0.71% at q=193). The e=2 Kummer
  analogue is analytically dead (leading Z-coefficient constant
  forces y = 0; hand-checkable chain, 880 curves concur).
  **CONSEQUENCE OF RECORD: nobody — round 33, round 34, anywhere
  in this campaign — has ever exhibited a (SAT1)-profile pencil
  with e = m at any m >= 2.** Its nonemptiness is now an exactly
  stated linear-algebra question (a (4m+1) x 4m Hankel pencil,
  minimal index exactly m, generic rank 4m-1, s = 0). By the
  banked reduction ("e = m is the entire difficulty"), **proving
  that stratum empty for m >= 2 closes the strict endpoint
  outright**; exhibiting a member gives the campaign its first
  real m >= 2 object and finally exercises F1/(NEWCAP) (third
  round with zero power over them). This is the named
  "Hankel/apolar coefficient chain" gate of three endpoint
  claim-contracts, now with its exact count and sign change.
- **TCAP-DIM RE-POSED (boundary m <= 1).** The posed count omits
  the automorphism group acting freely (finite stabilisers — a
  positive-dimensional stabiliser would fix 9 slopes + 32 points)
  on every solution: orbit dim >= 4 (AGL_1 x AGL_1), >= 6
  generically (PGL_2 x PGL_2). Corrected excess at m=2: +3..+5
  (UNREALIZABLE-expected); both round-33 positive controls
  preserved (m=1 stays -9..-7; the e=1 ladder stays -8m-1 < 0 for
  every m); an independent locator-layer bookkeeping agrees in
  verdict (-5 at m=2, +7 at m=1). STATUS: heuristic with the
  pb_design_ceiling blind spot — the pilot's own MISS 2 (a
  degenerate 1.4%-rate family briefly misread as refuting the
  naive count) is a live instance inside the same report.
- **REGRESSION-TEST PRINCIPLE, SHARPENED:** a proof of the strict
  target T <= rho+1 must fail at m = 1 AND must fail there
  *because* e = 1 locator sets are pairwise disjoint (the coset
  mechanism) — any argument not turning on d_x <= e overlap is
  fighting the wrong object.
- **SCOPE FENCES:** the pilot WITHDREW its own P8(b) rationality
  argument (the design constrains the union of fibres, not each
  fibre — the hyperelliptic-invariance premise was false; C's
  rationality is UNDECIDED); the multigraph enumeration is capped,
  not complete; the k=8 monomial family's n7 = 0 (below random
  rate) is unexplained; no statement about q at scale.

## ROUND 34 CLOSE (2026-08-11): the four banks reconciled

**BANK 1 (r34_pstar):** R-PSTAR RESOLVED YES — FG nonempty at razor
shape (witnesses A and B), the coordinator's banked equivalence
corrected (FG needs p* <= 2rho = R/32, factor 16); R-FG-RAZOR and
R-KER are the far-CA residuals. **BANK 2 (r34_layer_a):** (NS-m)
refuted-and-restated (NS-W-m) (5280/5280); Wronskian walled at the
pre-registered 5/12; the FACTOR-DEGREE DICHOTOMY proved (Q never
splits over F_q(x) for m >= 2; forced factor Z-degree >=
ceil((3m+1)/4) tight); layer A orthogonal to (BIV-CURVE) 80/80.
**BANK 3 (r34_bivcurve_m34):** (BIV-CURVE) REALIZABLE at m = 3
(two-field witness, (SPLIT-m)+involution); W-layer fence covers
m in {2,3}; m = 4 open (named (OV)/linear-hypergraph obstruction);
(OUT-m) posed with coordinator corrections; boundaries diverge
from TCAP-DIM. **BANK 4 (r34_m2_decision):** (SAT3) fields-searched
negative at m = 2 with mechanism; TCAP-DIM re-posed to m <= 1; the
(L2) e=m realization gate promoted to the question of record.

**THE RECONCILED PICTURE.** The round pulled the frontier apart
into a clean two-front structure:

1. **The conditioning front (new, decisive if it lands):** every
   W-layer and layer-A object this campaign built at m >= 2 is
   (SAT3)-conditional — and bank 4 now expects the conditioning
   stratum EMPTY at m >= 2 (corrected ledger +3..+5; zero e=m >= 2
   objects ever exhibited; the (L2) count turns positive exactly at
   m = 2). **(R-L2): decide e=m stratum nonemptiness at m = 2.**
   Empty for m >= 2 => the strict endpoint closes outright and the
   entire W-layer/layer-A program at m >= 2 becomes moot. Nonempty
   => feed the witness to bank 4's machinery: the first real
   m >= 2 T-measurement, and F1/(NEWCAP) finally exercised.
   [RESOLVED (round 35): NONEMPTY, constructively — 12 certified
   objects over five fields, coordinator-independently verified;
   AND the "empty => closes outright" stake was over-priced: the
   PROVED residual_pole_interpolation_exclusion node already
   excludes strict A=3 e=m ENDPOINT PROFILES on even rows m >= 6
   including the official m = 2^37 row. See the round-35 R-L2
   addendum.]
2. **The instrument front (if the stratum is nonempty):** the
   W-layer CANNOT exclude at m = 2, 3 (witness fences, banks 3 +
   round 33); layer A is the sole instrument there (orthogonality
   + the dichotomy, bank 2); its standing rides on Rout and on the
   RNC multiplicative-domain gate (survivors: ONE profile at
   m = 2, 3, 4).

**OBSERVED IDENTITY (DEF-ID), mechanism unexplained:** the W-layer
(BIV-G) deficit (conditions minus unknowns, bank 3 / round 33:
7m^2-9m+2 - (3m^2-2m)) and the (L2) realization overdetermination
(bank 4: (m+2)(4m+1) - 16m) are the SAME quadratic **4m^2-7m+2**,
produced by mutually quarantined pilots counting ostensibly
different objects (the W-restricted locator curve vs the syndrome
coefficient chain). Both are negative only at m = 1. Candidate
structural link between the two layers; posed as a round-35
question, NOT claimed as a theorem.

**COMPLIANCE ROUND SUMMARY:** 4/4 pilots clean under the upgraded
compute-law clause (27 ramguard invocations, zero bare python3 —
the clause works); one sed -i write-path deviation (bank 3)
censured; round-35 CONSTRAINTS to name sed -i explicitly. The
audit cadence caught and corrected banked or pilot text in all
four banks (factor-16, (NS-m)'s two inequivalent forms, (OUT-m)'s
aggregate rider + corollary qualifier, TCAP-DIM's missing
quotient).

**ROUND-35 ANCHORS (priority order):** (1) R-L2 — construct or
refute an e=m=2 (SAT1)-profile pencil (the decisive question on
the board); (2) Rout — theorem-or-sample for bank 1's <= 3
measurement (decides (NS-W-m)'s reach); (3) layer A on the m=3
(BIV-CURVE) witness + the m=4 decision (non-split G, sigma = c/x,
(3,3,3); import the u1_x4 linear-hypergraph compiler); (4)
R-FG-RAZOR — the key-equation budget at witness B's coordinates;
(5) DEF-ID; (6) the m=5 parity falsifier; (7) q_crit on the
official candidate.

## Round-35 R-L2 addendum (2026-08-11, coordinator-audited): the e=m stratum is NONEMPTY at m=2 — constructively; the emptiness route is dead; the gate moves to (SAT3)-on-(L2)

Pilot r35_l2_gate (round 35, bank 1). The witness is
coordinator-independently verified: I re-checked the published
q=97 object with code written from scratch (E1/E2 identities, all
four blocks of M(Z)Q_Z = 0, degrees (7,7,7), s = 0, generic rank
7, single rank-drop z=10 to rank 6, full rank at infinity,
nullity(36x32) = 1, no degree-<=1 kernel so e = 2 exactly) — ALL
PASS. Existence is witness-checkable: this part is a THEOREM.

- **R-L2 RESOLVED: NONEMPTY.** Twelve certified (4m+1) x 4m
  syndrome Hankel pencils with minimal index exactly m = 2,
  generic rank 4m-1 = 7, s = 0, delta = m-1 = 1, independent
  Q_0,Q_1,Q_2, over five fields (q = 97, 193, 257, 641, 769).
  Route: the (D-B) congruence criterion (nullity(36x32) =
  10 - rank Phi for the 14x10 matrix (f,g) -> (Q_2f-Q_1g mod Q_0,
  Q_1f-Q_0g mod Q_2); verified 120/120 per field) + the (D-F)
  inversion (for fixed B = (f,g,h,k) the cleared system is a
  SQUARE 24x24 in the curve; existence = det M(B) = 0, ONE
  condition, hit rate ~1/q vs blind q^-5).
- **THE +4 WAS NEVER THE EXISTENCE COUNT (round-34 reading
  corrected).** The equation-count excess 4m^2-7m+2 is not an
  existence codimension. The honest count: determinantal codim
  (36-31)(32-31) = 5 in the 23-dim projective curve space —
  **expected dimension 11m-4 > 0 at EVERY m >= 1**. The round-34
  incidence count (19) is contaminated by an excess component of
  dimension 21 (the degenerate common-root family — round 34's
  rank-1/s!=0 family, now with a dimension; nullity 2 on 40/40
  planted curves per field); the good component has dimension
  EXACTLY 18 = 23-5 (the +4/codim-5 condition is transverse there;
  the B-fibre is a point). The TCAP ledger (+3..+5) prices the
  full (SAT3) object and is untouched. **The emptiness route to
  the strict endpoint is dead at m = 2 constructively and
  expected-dead at every m by the 11m-4 count.**
- **THE STRICT-ENDPOINT STAKE, RE-PRICED (coordinator forced
  correction of the round-34 close):** the PROVED background node
  rate_half_ca_hankel_endpoint_residual_pole_interpolation_exclusion
  (wave-57/58 strict-A=3 Picard-Forney chain) already excludes
  every strict A=3, e=m ENDPOINT PROFILE on even rows m >= 6 —
  including the official m = 2^37 row (pole-ideal interpolation +
  surface cohomology; scope fence: e>m strict profiles, A=1
  residuals, the complete crossing, the adjacent unsafe witness
  remain open). R-L2's emptiness branch was therefore never the
  decisive route to the OFFICIAL endpoint; its value was always
  the structural/small-m content, which the witness now delivers.
  (The witness — m=2, T=0 — is outside that node's hypotheses on
  both counts; no contradiction.)
- **THE DIFFICULTY MOVES, UNDIMINISHED, TO THE SPLITTING LAYER.**
  All witnesses have T = 0; not one locator splits completely over
  F_q; the root-count histogram is the Poisson(1) law of RANDOM
  degree-7 polynomials to within noise. Having a syndrome pencil
  buys NOTHING at the splitting layer — the same "no structural
  enhancement" round 34 measured on nets without pencils, now
  measured on nets with them. **The gate of record is now
  (SAT3)-ON-(L2): design B = (f,g,h,k) so the resulting locators
  split over mu_32 at T = rho+2 supported slopes.** The inversion
  leaves B entirely free — this is the named next instrument.
- **F1: first (weak) exercise in four rounds.** a* over ALL slope
  pairs = 13 = 7m-1 on 5 of 6 headline witnesses, and 12 on one —
  so a* is NOT forced to 7m-1 by the pencil alone. Not the
  endpoint functional (min over supported pairs needs supported
  slopes; none exist at T = 0). (NEWCAP) still at zero power.
- **DEF-ID RESOLVED: COINCIDENCE.** The identity
  (m+2)(4m+1) + m(3m-2) = (m-1)(7m-2) + 16m = 7m^2+7m+2 is exact,
  but the two systems' shapes are incompatible (quadratic/quadratic
  ratio -> 7/3 vs quadratic/linear -> infinity), the deficits have
  different provenance, and — decisively — the shared quantity
  governs NEITHER layer's existence ((L2) is nonempty at m=2
  despite +4; (BIV-G) realizable at m=3 despite +17). Closed as
  posed.
- **SCOPE FENCES:** the m >= 3 branch of R-L2 is untouched (the
  24x24 squareness is an m=2 accident: 80 equations on 48 for
  fixed B at m=3 — a new inversion is needed); five prime fields
  is not a lift to Z nor a q ~ 2^128 statement; the witnesses
  satisfy the pencil-intrinsic half of (SAT1) and NONE of
  (SAT2)-(SAT5) (vacuous at T=0, not verified); the designed-
  domain question is untested (the greedy instrument had zero
  input). Blind (L2) search is banned at every m (q^-5; use the
  inversion).

## Round-35 R-FG-RAZOR addendum (2026-08-11, coordinator-audited): walled AND downgraded; the type-2 ledger is vacuous on the open bracket; R-HRLOW is the new load-bearing residual

Pilot r35_fg_razor (round 35, bank 2; e3 exact-integer arithmetic
replayed — every committed razor integer E1-E22 exact, the banked
LB1-C constant 670,014,898,009 reproduced to the digit). No bound
on B_ca^far(k+2^34) either way.

- **THE TYPE-2 SPEND/LIST LEDGER IS VACUOUS ON THE WHOLE OPEN
  BRACKET — a SCOPE FENCE of record.** (C2)'s per-slope floor is
  (R+1) - w* with w* = |W| in [r, 2r]; it is positive for every
  admissible W iff 2r <= R iff a >= 3n/4 — exactly the top of the
  open bracket (the unique-decoding radius). At razor shape the
  adversary takes w* = 2r and the floor is -1,065,151,889,407:
  vacuous BY SIGN, not by slack (positive iff
  |S_g ^ S_h| >= 2r-R = 62r/63 = 98.41% of r — adversary-free).
  CONSEQUENCE: no transport of (C2)/(C3)/(C4)/X_gamma/layer-A
  instruments into [k+2^34, 3n/4) can bind — vacuous by sign
  before it is vacuous by counting. (No banked text connected the
  type-2 ledger to far-CA — zero grep hits — and now there is a
  proved reason not to.)
- **FG CARRIES NO STRUCTURAL BAD-SLOPE FLOOR; LB1 DOES.** At six
  razor-faithful rate-half cells across ten fields spanning
  mu_1 in [2.9e-5, 238]: LB1's type-1 count is EXACTLY r+1
  (field-size independent, 9/9 ledger rows; (C3) T_1 <= e+1
  ATTAINED at 0 bits with e = d_x = r); witness B's FG replica has
  T_1 in {2,3} and total T that tracks q*mu_1 and falls BELOW r+1
  in the subcritical regime (T = 1 at n=22, q=65537 vs r+1 = 10).
  Since every admissible official row is deeply subcritical, **the
  FG stratum is not where the extremal B_ca^far count can live**
  unless it beats its own first moment — and LB1 is the exhibit
  that beating it is possible: at q = 2^167 the first moment
  predicts E[T] = 2^{-6.704e11} against the PROVED floor r+1 =
  2^39.98. **The first moment is wrong by 6.70e11 bits in this
  lane** (LB1-C IS the subcriticality condition up to the exact
  residue log2 q + n(1-H2(r/n)) — verified to the digit at two q).
- **THE h_r DICTIONARY ORDERS THE RESIDUALS; PRIORITY INVERTED.**
  R-FG nests strictly inside R-KER (V_r = F[x]_{<=r}/K_0 of dim
  h_r; R-KER counts slopes where the (h_r-rho)-dim increment
  acquires a D_r(D) member; R-FG is the sub-stratum where V_r is
  a RING and U_gamma cyclic). Closing R-FG would NOT move
  B_ca^far. The extremal object sits at the SMALL end:
  **R-HRLOW (new residual of record): bound T for column-far
  razor pencils with h_r near rho** — LB1 is the h_r = rho+1
  extremal with p*(LB1) = floor(R/2)+1 = 2^39+1 (exactly ONE
  integer above the intermediate band's top), dim K_0 = r-rho,
  T_1 = r+1. Any upper bound in this lane must clear T = r+1 at
  h_r = rho+1 or exclude that configuration. Far-CA residual set
  after this round: {R-HRLOW > R-KER > R-FG-RAZOR (downgraded)};
  R-PSTAR-INTERMEDIATE carried no load as a stratum but its top
  edge floor(R/2) is LB1's sharp coordinate.
- **CRITERION CORRECTION (banked artifact, recorded here — the
  r34_pstar REPORT stays byte-original):** h_r = p* is NECESSARY
  but NOT SUFFICIENT for round-33 FG. FG needs K_0 = P*F[x]_{<=r-p}
  with p = deg P; h_r = p* only yields it with the WINDOW index
  p*, and deg P = d* can be strictly smaller (three exhibited
  counterexamples: LB1 at k=1 cells has p* = 4 = h_r, d* = 3,
  FG FALSE). The r34_pstar D1.2 table's "FG" label on the
  h_r = p* row is wrong as a criterion; witness B itself is
  unaffected (deg P = p verified 10/10).
- **q_crit PASSES on the official candidate** (secondary): by
  103.01 bits on the razor-shape threshold and 126.38 bits on the
  row's own threshold, at every admissible official row — the
  random model is not void there, and the key equation is
  subcritical too (theta_1 = 2*theta_2 exactly). The two inline
  SCOPE-CORRECTED markers above (LB1-generic; q_crit) are this
  bank's forced corrections.
- **SCOPE FENCES:** all machine numbers at q <= 65537, R <= 14 —
  zero razor-regime measurement; k=1 cells are non-faithful for
  p*(LB1) (they miss a > R+1 and a-1 > r — the pilot's own first
  design would have inverted the headline and was caught by hand);
  w* is reported under a 24-locator cap (direction favors the
  vacuity conclusion); the 2^128 numerology (theta_1 within 0.02
  bits of EPSILON_BITS) is a COINCIDENCE (n/rho vs the prize
  soundness parameter) and is recorded to prevent a future false
  link.

## Round-35 (BIV-CURVE) m=4 addendum (2026-08-11, coordinator-audited): the round-34 obstruction measured INERT; the parity prediction refuted; five classes searched-negative; (OUT-m) refined to an identity

Pilot r35_bivcurve_m4 (round 35, bank 3). m = 4 remains OPEN — no
witness, no theorem — but the obstruction is relocated, re-scoped,
and its ceiling raised. Coordinator hand-checks: the Z_12
certificate (differences of {0,1,3} are +-1,+-2,+-3 all distinct
=> linear; 3-regular; SDR), the route-(b) quotient-coordinate
derivation, the (OUT-m) aggregate identity, and the (DEG-m)
algebra all verified.

- **THE ABLATION (the round's main measurement):** with the
  linearity/(OV) constraint REMOVED from the m=4 selection search,
  the ceiling does not move at either field (7/7 at q=193, 8/8 at
  q=257; m=5 histograms BIT-IDENTICAL with and without the pair
  cap); with the <= rho SLOPE BUDGET removed instead, 12/12 in
  383/383 draws (15/15 in 500/500 at m=5). **The (OV)-forced
  linear hypergraph is real, proved, and INERT; the whole
  obstruction is arithmetic value-confinement (the slope
  budget).** The u1_x4 compiler transported and DECIDED the
  selection layer — positively, i.e. in the opposite direction to
  the transport's motivation.
- **FIVE CLASSES NOW SEARCHED-NEGATIVE (budgets 12000-30000 DFS
  nodes/draw, two fields each):** (1) (SPLIT-4)+sigma(-x) random,
  ceiling 8; (2) value-prescribed (SPLIT-4) (seven phi-values by a
  7x8 nullspace, targets from the Z_12 certificate), ceiling 9 —
  round 34's declared structured-pencil blind spot now measured,
  and its ceiling was SOFT (7 -> 9); (3) (SPLIT-4)+sigma(c/x),
  ceiling 7 — route (b) refuted at the DERIVATION level: for ANY
  involution the invariant subfield is F_q(w) (w = x^2 or
  x + c/x), so a deg_x <= 3 invariant factor is Möbius in w and
  INJECTIVE ON ORBITS (167/167, 177/177) — the fixed points never
  touch the cross-coincidence term (the round-35 brief's route-(b)
  hypothesis was WRONG; coordinator brief error, recorded);
  (4) un-symmetrised (3,3,3), ceiling 8 of 24 (demand 58 vs 21
  parameters — the worst route, now measured); (5) (QUAD-4), the
  first genuine non-split probe (G = Q(Z,u)L(Z,u), u = x^2, Q an
  irreducible sigma-invariant Z-quadratic; 14 parameters vs 10;
  disc-square rate 15.7/32 confirms non-splitness), ceiling 7 —
  the extra parameters are repaid by losing half the orbit pool.
  UNTOUCHED: general non-split G with no sigma-symmetry and no
  Q*L factorisation. DERIVED en route: at even m EVERY
  sigma-symmetric ansatz wastes one unit of the 3m-3 budget
  (invariant factors have even x-degree).
- **AUDIT QUALIFIER (coordinator):** the pilot's R2.3 parity
  argument ("no involution makes W sigma-stable at even m") is
  over-broad on the c in mu_32 branch — #Fix = 2 admits a
  sigma-stable odd set containing exactly one fixed point; the
  inference holds only when #Fix = 0. The route-(b) kill is
  carried entirely by the injectivity derivation, which is sound.
- **THE m=5 PARITY FALSIFIER FIRED.** (SPLIT-5)+sigma all-swapped
  (no invariant factor, budget 3+3+3+3 = 12 = 3m-3 exact — the
  configuration parity called easy) reaches 7/15 and 6/15: FURTHER
  from target than m=4. The law of record is parity-free:
  **coincidence demand D(m) = 3m(m-1)-(rho-1) = 8, 22, 42 at
  m = 3, 4, 5 against supply FLAT in m (best achieved 8, 12, 9) —
  m = 3 is the last m where supply meets demand, exactly** (which
  is why the m=3 witness cost 632/24939 trials).
  [CORRECTED (round 36): the demand row undercharges the middle
  tuples — with ceilings the 2-sharing values are 8, 25, 47 (exact
  only at m=3, where the two errors cancel); and the QUADRATIC is
  a 2-SHARING ARTEFACT: under maximal sharing k = m-1 (a Lüroth
  pullback through a degree-3 map — legal, budget met with
  EQUALITY, waste = 3(m-1) mod k) the demand is D_max(m) = 4m-8,
  LINEAR, for m >= 7 (11 at m=4). The crossing stays at m=3, but
  the m >= 5 fence is linear, not quadratic. See the round-36
  (SHARE3-4) addendum.] The pair-
  multiplicity cap generalises to floor((m-1)/2) (linearity = its
  m=4 face, as round 34's caution said — and it is inert there
  too). Positive control: the same engine reaches 9/9 at m=3 on
  both fields.
- **(OUT-m) SURVIVED ALL STRESS AND IS REFINED TO AN IDENTITY
  (adopted):** sum_gamma eps~_gamma = sum_x def(x)*t_x with t_x
  the number of type-2 blocks through x, charging m-1 / m-2 / m-3
  per unit of deficiency at outside / symmetric-difference /
  middle points respectively (coordinator-verified: trivial
  double-count once stated). The aggregate (m-1)(1+O) is attained
  ONLY by outside deficiency — the m=3 witness attains it exactly
  (sum = 2 = (m-1)(1+O), and the refuted original rider fails
  2 > 1, reproducing the round-34 catch); the m=2 exhibit (inside
  placement) charges 0. COROLLARY (DEG-m), inheriting POSED
  status: in sigma-designs X' = 2 deg_H, so deg_H(gamma) +
  X''_gamma >= ceil((m-1-eps~)/2) with the exact middle budget
  sum_gamma X''_gamma = (m-1)(m-2) — at m >= 4 a degree-1 slope
  REQUIRES middle support, a constraint round 34's DFS never
  imposed (its ceiling was measured on a relaxation); both
  selection certificates survive the tightening. SYMBOL COLLISION
  recorded: deg_H already names the bipartite non-incidence degree
  in the PROVED a1_core_one_active_partition_incidence_
  reconstruction node — two objects, one symbol, same rate_half
  family.
- **SCOPE FENCES:** every negative is a DFS ceiling under a named
  budget over a named class; no configuration this round was
  completed (no outside completion, no bivariate system, no
  per-side verification — selection-layer objects only; the k=9
  m=4 candidates are provably NOT completable as they stand: six
  degree-1 slopes against a completeness bound of four); layer A
  still unrun; (SAT3)-conditionality untouched; two fields is not
  q-uniformity; (DEG-m) inherits (OUT-m)'s POSED status. Pilot
  compliance: 9/9 ramguard clean (7th consecutive), zero
  write-discipline breaches; one recursive grep traversed dag.json
  as a filename (disclosed; round-36 CONSTRAINTS add
  --exclude=dag.json to the standard flags).

## Round-35 Rout/layer-A addendum (2026-08-11, coordinator-audited): Rout is FREE and the sign was backwards; layer A kills the m=3 witness COMPLETION-INDEPENDENTLY; the dichotomy was already proved

Pilot r35_rout_layer_a (round 35, bank 4). Coordinator
verifications: maxRout = 4 confirmed in bank 1's own banked file;
the rational_branch_exclusion node read (PROVED, (CPR3)-(CPR5) as
claimed); the pilot's one write-scope breach (an imported bank
script's output path overwrote r34_layer_a/d3b_replay_results.txt
at import time) left the repo CLEAN — git shows the regenerated
content byte-identical to the committed banked file (deterministic
seed), so the breach is procedural only; censured, and round-36
CONSTRAINTS add "audit imported scripts' output paths BEFORE
import".

- **ROUT DECIDED: FREE, AND THE QUESTION WAS POSED BACKWARDS.**
  Rout <= d-m is refuted IN CLASS at m=1 (4800/5280 on the
  realized (SAT3) stratum, replayed) and out of class at m=2,3
  inside the canonical band a >= 7m-1 (582 violations / 7275
  slopes, two fields at m=2); the banked "Rout <= 3" was false as
  printed (max 4 in its own file); Rout matches a uniform-random-
  polynomial null cell-by-cell (32700 slopes) and attains the
  trivial degree bound. THE SIGN: rearranging the banked (JDEC) +
  (DEGSUM) gives the EXACT closure criterion
  **(CLO-m): (d - Dh) + (n - ov) + Rout + nonsplit >= m**
  (equivalent to X <= d-m in 32700/32700) — Rout enters
  POSITIVELY; a bound on it could never buy closure.
  STATUS: (NS-m) RETIRED (strictly stronger than needed, false
  where closure holds); **(NS-W-m) is the target of record WITH
  HYPOTHESES STATED (canonical minimising W*, a >= 7m-1, d >= m)**
  — it holds 7275/7275 there and 5280/5280 in class, but FAILS at
  planted W (6686 times), so the hypotheses are load-bearing;
  (CLO-m) recorded as the exact target. The round-34 restatement
  was a REDIRECTION, not a correction. CLASS CAVEAT (both banks):
  every m >= 2 measurement is outside the T = rho+2 class (the
  constructor realizes max T = 3), and the class itself may be
  empty — see the gate below.
- **LAYER A KILLS THE m=3 (BIV-CURVE) WITNESS —
  COMPLETION-INDEPENDENTLY (round-34 MISS 7 discharged).** LA|_W
  (the 60 incidences INSIDE W only) already forces Q = 0 on both
  fields; no outside completion can rescue the witness (40 fresh
  completions: 40/40 killed; 4791/4845 resp. 4823/4845 of all
  16-subsets of W already bind — "any 16" is FALSE, caught by the
  pilot's own exhaustive scan). Span rank 12 = rho+1, maximal.
  MECHANISM **(LA-W COUNT), posed**: at a = 7m-1 with W saturated,
  the W-incidences impose (7m-1)m conditions on (rho+1)(m+1) =
  4m(m+1) biform coefficients — excess 3m^2-5m, NEGATIVE ONLY AT
  m=1. All three regressions fire (m=1: 16/16 witnesses survive
  with nullity exactly 2; m=2: bank 2's exhibit killed by its 26
  W-incidences alone — new; m=3: killed, both fields). The pilot's
  repaired positive control fires 6/6+6/6 (round-34's control
  never could — demand-splitting removed). **Proving (LA-W COUNT)
  as a rank theorem would make layer A an unconditional exclusion
  at every saturated a = 7m-1 configuration — the named
  instrument of record.**
- **THE MULTIPLICATIVE PUSH: THE SURVIVOR STANDS, AND THE
  DICHOTOMY WAS ALREADY PROVED.** Three of the round's D3 objects
  subtracted to PROVED nodes: the factor-degree dichotomy + its
  per-factor sharpening = rational_branch_exclusion (CPR3)-(CPR5)
  (the ALREADY-PROVED marker above); the norm identity = (ENF2)
  transposed; the coset obstruction = the quartic_coset_biform
  lift node's gcd(4m-1,16m) = 1. The m=2 survivor (Q irreducible,
  bidegree (2,7)) is exactly the (CPR3) profile — NOT emptied;
  survivor count closed form sum_{k <= floor((m-1)/4)} p(k).
  WHAT IS NEW — **the quantified gate**: the multiplicative domain
  enters only through C(16m, 4m-1) (q-INDEPENDENT count of
  degree-rho squarefree divisors of x^N-1) against ambient q^rho;
  the layer-A-consistency first moment is calibrated TWICE at m=1
  (+13.75 bits at q=17 where EXACTLY 16 configurations exist and
  they ARE the 16 realized (SAT3) families — two independent
  constructions; -0.94 at q=97 where none are realized) and is
  NEGATIVE for every m >= 2 at every field (~ -1952 m^2 bits at
  official scale; overestimates by 2^9.8 at its own calibration
  point, the safe direction). HEURISTIC — but it is the lane's
  first quantitative instrument for m >= 2, and it says the
  T = rho+2 class is likely EMPTY there (making the (NS-*) family
  vacuous and converging with round-34 bank 4's searched-negative
  and the corrected TCAP ledger from a third direction).
- **SCOPE FENCES:** the m=3 Rout census is single-field; the
  layer-A kill has power over the witness and its completions
  only (no m >= 2 layer-A-consistent candidate was sought);
  nullity 0 on structured objects is not non-existence; the first
  moment is negative, which proves nothing; all m >= 2
  measurements out of class; everything (SAT3)-conditional.

## ROUND 35 CLOSE (2026-08-11): the four banks reconciled — the board inverts

**BANK 1 (r35_l2_gate):** R-L2 NONEMPTY (theorem; 12 witnesses, 5
fields, coordinator-independent verification); the emptiness route
dead everywhere (11m-4 > 0); the strict-endpoint stake re-priced
(residual-pole node already excludes official-row strict A=3 e=m
profiles); gate of record (SAT3)-on-(L2); DEF-ID a coincidence.
**BANK 2 (r35_fg_razor):** R-FG-RAZOR walled and downgraded; the
type-2 ledger vacuous by sign on the whole open bracket; R-HRLOW
promoted (LB1 the h_r = rho+1 extremal; the first moment wrong by
6.7e11 bits against LB1's proved floor). **BANK 3
(r35_bivcurve_m4):** the round-34 m=4 obstruction measured INERT
(ablation; selection layer decided satisfiable by the Z_12
certificate); ceiling soft (7 -> 9); the m=5 parity falsifier
FIRED; law of record = demand 3m^2-7m+2 vs flat supply; (OUT-m)
refined to an identity. **BANK 4 (r35_rout_layer_a):** Rout free
and the sign backwards ((CLO-m) exact; (NS-m) retired, (NS-W-m)
of record with hypotheses); layer A kills the m=3 witness
completion-independently ((LA-W COUNT) 3m^2-5m); the dichotomy
was ALREADY PROVED in-repo; the C(16m,4m-1) first-moment gate
calibrated twice at m=1.

**THE RECONCILED PICTURE — the two fronts of round 34 have
INVERTED:**

1. **The conditioning front:** R-L2 answered NONEMPTY (the
   emptiness escape is gone), so the strict endpoint at small m
   rides entirely on (SAT3)-on-(L2): can the free B-parameters of
   bank 1's inversion make locators split over mu_32 at
   T = rho+2? THREE independent instruments now say that class is
   empty-expected at m >= 2 (round-34's searched-negative; the
   corrected TCAP ledger; bank 4's calibrated first-moment gate at
   ~ -1952 m^2 bits) — but none is a theorem, and bank 1's
   witnesses prove counting alone cannot be trusted in this lane
   (11m-4 vs the dead +4 reading; LB1 vs its first moment,
   bank 2). **The instrument face-off of record: design B to beat
   the moment (bank 1's route) vs prove the (LA-W COUNT) rank
   statement (bank 4's route — which would close every saturated
   a = 7m-1 configuration at once, unconditionally).**
2. **The instrument front:** layer A is CONFIRMED as the sole and
   sufficient W-layer exclusion instrument at m = 2, 3
   (completion-independent kills at both); the W-layer witness
   fences cost it nothing. The far-CA front is restructured
   around R-HRLOW (the type-2 ledger cannot reach the bracket;
   FG cannot carry the extremal count; LB1's mechanism — a fixed
   (r+1)-point set with r+1 locators — is the only known way to
   beat a first moment in this lane, and the question is whether
   any h_r > rho+1 stratum has an analogue).

**AUDIT LEDGER OF THE ROUND (9th consecutive round the cadence
caught real text):** banked text corrected — the round-34 m=4
obstruction attribution (inert), the round-34 close's R-L2 stake
(over-priced vs the residual-pole node), the round-33/34 "Rout <=
3" (false as printed, max 4 in its own file), the round-34
"PROVED THEOREM" dichotomy (already proved in-repo), q_crit and
LB1-generic (scope-corrected), the r34_pstar FG-criterion row
(h_r = p* not sufficient), + the round-35 brief's own route-(b)
hypothesis (refuted at derivation level) and pilot text (R2.3
over-broad; "any 16 points" false). COMPLIANCE: banks 1-3 clean
(5th-7th consecutive); bank 4 clean on compute (10/10 ramguard)
with ONE write-scope breach (imported script's output path;
repo left byte-identical; procedural censure; round-36 rule:
audit imported output paths BEFORE import, pre-list sibling
names, --exclude=dag.json standard).

**ROUND-36 ANCHORS (priority order):** (1) **(LA-W COUNT) -> rank
theorem** (closes all saturated a = 7m-1 configurations
unconditionally; squarely inside the RNC gate)
[RE-POSED (wave-59 integration, same day): the BARE form is
FALSE — Codex's PROVED rate_half_layer_a_saturation_count_route_
fence exhibits Q = Z^2-X^4 on W in mu_16 (13 points, all
saturated, excess +2) with nullity 4 (kernel = A(X)*Q, deg A <= 3;
coordinator hand-verified AND verifier-replayed). The rank theorem
MUST use the endpoint geometry (W = union of two degree-rho slope
supports, split-biform/support-intersection/Hankel-source
constraints) — exactly the fence's own scope note. The anchor
stands in re-posed form]
[RETIRED (round 36, bank 1): the unconditional rank target is
DEAD at every cheaply testable rung — (LA-EQ) shows the theorem
STRICTLY IMPLIES the strict-endpoint exclusion (any realized
endpoint's kernel biform restricted to 7m-1 of its >= 15m
saturated points gives nullity >= 1), H1 and H1+H2 are refuted
CONSTRUCTIVELY (closed-form nullity-1 families, both fields), and
the fence generalizes to Q_0 = Z^m - X^{2m} with nullity exactly
2m at every m >= 2. The surviving question — rank over
(SAT2)-completable configurations — IS the realizability
question. See the round-36 (LA-EQ) addendum]; (2)
**(SAT3)-on-(L2)** (bank 1's free-B design vs the first-moment
gate — either a witness that beats three instruments or evidence
the class is empty); (3) **R-HRLOW** (the h_r = rho+2..O(1) band:
does any stratum above LB1 carry an LB1-type mechanism?);
(4) the general non-split m=4 probe + (DEG-m)-tightened searches;
(5) the m=1 16=16 coincidence node (the lane's only calibrated
instrument); (6) retire Rout permanently (do not re-spend).
## Cycle 146 addendum: the live paired biform has an off-line norm factorization

The Round-34 `Rout` prompt above belongs to the strict `A=3`, `e=m`
endpoint, which Cycles 71--74 already close in this worktree. The surviving
`A=1` macroscopic pair boundaries instead carry the following exact norm.

For the extremal `(e-2,p-3)` split biform, multiply `G(delta,X)` over all
`3e` off-line supported slopes. Every classified row is a zero of exactly
`e-2` factors, so

```text
product_delta G(delta,X)=L_M(X)^(e-2) S_G(X),
deg S_G<=3e-9     (d_A=0),
deg S_G<=2e-7     (d_A=1).
```

Every selected padded-heavy root lies in `S_G`; at `d_A=1` these are
exactly the selected roots outside the classified row set. The strict
`(e-1,p-2)` carrier has the same row-power factorization with residual cap

```text
[3e^2-4e-7-2r_A(e-1)]/2.
```

In the extremal profile the residual degree is below the classified-row
count. Its value at a classified row is the product of every incident
`X`-derivative and every nonincident fiber value, divided by
`L_M'(x)^(e-2)`. These values uniquely reconstruct `S_G` by Lagrange
interpolation.

The residual degree is exact after fiber degree drops are charged:

```text
deg S_G=cap-sum_delta((p-3)-deg_X G(delta,X)).
```

The cap equals the complete sum of triple-union excess, padded-heavy degree,
and the possible exceptional-row incidences. Those incidence quantities
therefore cannot overfill the norm on their own.

The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_paired_split_biform_offline_norm_factorization`.
The next useful obstruction must evaluate those tangent products from the
retained Hankel/source equations or force a factor outside the exact slack
identity.

## Cycle 147 addendum: selected support roots are transverse, not tangent

The nonincidence Forney constant cannot be substituted at an actual-support
root. Writing the line-source value correctly as the minimum-word summand
plus the nonzero actual error gives, at every selected zero-excess support
root,

```text
G_t/Q_t-G_X/Q_X
 =(x-s_0)v_x L_U0'(x)e_delta(x)/Lambda(delta) !=0.
```

Thus the contracted locator and split-biform curves meet transversely at
all selected actual-support roots. A common component can meet a selected
fiber only through its padded-heavy roots. If its bidegree is `(a,b)`,

```text
(|Z_0|-b)a<=sum_(delta in Z_0)r_delta.
```

For the extremal carrier this forces `a=0`, and the classified row-root
dictionary excludes a nonconstant parameter-only factor. Hence `Q` and
`G` are coprime. For the first strict carrier, every nonconstant common
factor is forced into the single residual profile

```text
a=1,       b>=(e+15)/2+r_A,       r_A<=(e-17)/2,
```

with its selected-fiber roots all padded rather than actual support. The
putative linear factor would contribute at least
`b(2p+r_A-1)` classified row-slope pairs, while each of the `3e+1`
off-line slopes contributes at most one. This contradicts the displayed
lower bound on `b`, so the strict curves are coprime as well. The
proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_paired_zero_excess_first_jet_transversality`.
The next route is the coprime resultant/intersection ledger; the tangent-
product route must retain transversality rather than seek ramification at
the selected incidences.

## Cycle 148 addendum: the extremal coprime resultant has only four plus bad padding degrees

Since the extremal locator `Q` and split biform `G` are coprime, their
parameter resultant is nonzero. Removing the classified-row factor
`L_M^(e-2)` leaves degree at most `2e-5` for `d_A=0` and `e-3` for
`d_A=1`.

Every zero-excess padded-heavy factor divides this residual resultant. In
the `d_A=0` profile, the exceptional row contributes exactly `e-3`
additional off-line common points. If `r_bad` denotes total padding on
positive-excess slopes, removing all mandatory factors leaves one nonzero
polynomial `W_QG` with

```text
deg W_QG<=4+r_bad.
```

Every unclassified common point or excess local intersection multiplicity
must fit in this allowance; selected actual-support points are transverse
and add no excess. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_extremal_coprime_resultant_four_slack`.
The extremal route now needs either `r_bad` control or `5+r_bad` forced
additional intersection units.

## Cycle 149 addendum: every positive-excess fiber also contains all padding

For an arbitrary off-line slope, factor the center-difference codeword by
its `k-1-a_delta` forced zeros. The residual is a nonzero polynomial
`H_delta` of degree at most `a_delta`, and the split-biform fiber satisfies

```text
Qbar(delta,X)=chi A_delta B_delta R_delta,
G(delta,X)=zeta A_delta H_delta R_delta.
```

Thus every padded-heavy factor is present on the split-biform fiber,
including positive-excess slopes, and

```text
n-deg_X G(delta,X)=a_delta-deg H_delta.
```

The actual-error first-jet calculation also extends to every off-line
slope, so every actual-support common root is transverse. The proved node
is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_paired_all_excess_residual_fiber_factorization`.
In particular `r_bad` is now mandatory in the extremal resultant rather
than part of its unexplained allowance.

## Cycle 150 addendum: the extremal resultant residual is degree at most four

Insert every positive-excess padded factor from Cycle 149 into the nonzero
resultant of Cycle 148. In both `d_A` profiles,

```text
R_QG=L_M^(e-2) E_circ
     [product_(all off-line delta)R_delta] W_4,
deg W_4<=4,
```

where `E_circ=(X-x_circ)^(e-3)` for `d_A=0` and is one for `d_A=1`.
There are no additional vertical common factors:
`gcd(B_delta,H_delta)=1`, so every common root on an ordinary supported
off-line fiber is actual support or padding and is already accounted for.
Every excess mandatory-root multiplicity or common point over a center-
line, unsupported, or projective-infinity fiber uses the same four-degree
allowance; actual-support roots are transverse.

The projective statement is exact: Bezout gives total intersection
`(9e^2-23e+8)/2`, while the `n-a_delta` mandatory roots on the `3e`
off-line slopes sum to four fewer. After removing one copy of every actual-
support and padding point, the residual effective intersection cycle has
degree exactly four.

The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_extremal_coprime_resultant_exact_four_core`.
The extremal branch is now a constant-size problem outside ordinary
supported-fiber root supply: classify the four-core or force five excess
or nonordinary intersection units.

## Cycles 151--152 addendum: the four-core is the regular correction quartic

The contracted source moments have a canonical second-kind numerator
`P_F`. Its interpolation syzygy and normalized Hankel resultant are

```text
QB-Lambda G=L_U0 P_F,
Res_X(Q,P_F)=c a^(2d+1)D_1.
```

Thus `D_1` is the parameter pushforward of the Forney-contact divisor. The
regular quartic from Cycle 110 is now identified exactly:

```text
double root: E_4 proportional to S_B^2,
two simple:  E_4 proportional to S_1S_2.
```

Taking the `X`-resultant of the syzygy and inserting the exact row and
rank-loss factors gives

```text
Res_X(Q,G)
 =c E_4 product_(delta off line)ell_delta^(n-a_delta).
```

Every center factor cancels, including center-line rank loss. Hence the
parameter pushforward of the exact residual four-cycle is `div(E_4)`, with
no unlisted unsupported or infinity fiber. The proved nodes are
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_pade_regular_factor_identity`
and
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_extremal_resultant_regular_quartic_identification`.
The next live obstruction is local Hankel jet realizability of the forced
square or linear-times-cubic correction quartic.

## Cycle 153 addendum: marked multiplicity alone is fenced

The correction identities make the marked determinants exactly

```text
double root: g_*^3S_B^8,
two simple:  G_1^5G_2S_1^7S_2 and G_1G_2^5S_1S_2^7.
```

However, explicit symmetric affine Kronecker pencils with one primitive
minimal-index block realize isolated marked orders eight and seven. The
proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_correction_marked_jet_route_fence`.
Thus determinant multiplicity, symmetry, and generic corank one cannot
close the branch without a genuinely Hankel/source/split-fiber input.

## Cycle 154 addendum: ordinary supported rank loss is first-order transverse

The exact correction factorization now separates every ordinary supported
rank-loss slope from the constant-size correction locus. Away from
`S_B` in the double-root arm or `S_1S_2` in the two-simple arm,

```text
ord_gamma(D_1)=c_gamma.
```

The specialized symmetric Hankel kernel is
`Q_min F[X]_(<=c_gamma)`. Local Smith form therefore makes every positive
exponent one, and the derivative moment form

```text
B_gamma(A,B)=dot Phi(Q_min^2AB)
```

has rank `c_gamma` and radical exactly `span{R_gamma}`. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_supported_first_jet_perfect_pairing`.
Thus all extensive supported rank-loss mass is ordinary at first order;
only at most two double-root slopes or four two-simple slopes can carry the
higher local Smith behavior needed by the correction quartic.

## Cycle 155 addendum: the coefficient plane meets ordinary kernels sharply

The common coefficient plane `W_q` is totally isotropic for every local
Hankel derivative. Combining this with Cycle 154 gives

```text
dim((W_q intersect ker M_gamma)/span{Q_gamma})
 <=floor(c_gamma/2).
```

Hence at every correction-free rank-one loss slope the primitive locator
is the only coefficient-plane vector vanishing on the full actual support,
and the support evaluation matrix `(Q_i(x))` has exact rank `e`. At a
rank-two loss slope its rank is `e-1` or `e`. The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_supported_coefficient_plane_kernel_intersection`.
This is a genuine source/Hankel restriction absent from the abstract
Kronecker countermodel; it still requires an adapter to the split-biform
boundary before it can exclude a packet.

## Cycle 156 addendum: a separated double-root correction is cubic

In the double-root arm, assume `S_B` is squarefree and coprime to `g_*`,
and divide the primitive locator by the fixed heavy row:

```text
U(t,X)=[Q(t,X)-Q(t,x_*)]/(X-x_*).
```

The Pade contact divisor and the higher vertical contact prove

```text
P_F(t,x_*)=D_1(t)C_0(t),
M(t)U(t)=D_1(t)C(t),       deg_t C<=3,
C_(i+1)=x_*C_i-kappa S_Bh_i.
```

The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_heavy_quotient_cubic_residual`.
At each correction root, the quotient `U` is one primitive regular-kernel
direction carrying the full determinant valuation. Thus both separated
corrections have Smith type `[2]` rather than `[1,1]`. The separated locus
is one cubic source recurrence, not an unconstrained degree-`e` marked
determinant. Nonreduced corrections and roots shared with `g_*` remain
explicitly open.

## Cycle 157 addendum: the cubic residual is welded to the split biform

On the separated double-root extremal locus, put

```text
J=gcd(Lambda,g_*S_B^2),       j=deg J<=3.
```

The cubic Pade bracket and exact center cancellation give

```text
G(t,x_*)=[g_*(t)S_B(t)^2/J(t)]T_j(t),
deg T_j<=j.
```

The proved node is
`rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_heavy_row_center_overlap_factorization`.
All but at most three roots of the fixed heavy row are now prescribed. Its
coefficient vector augments the extremal coefficient-MDS system with at
most four scalar unknowns. The remaining separated double-root terminal is
the rank/nullity of this augmented system, not an untyped correction jet.

## Round-36 (LA-EQ) addendum (2026-08-11, coordinator-audited): the rank target retired; the layer-A and realizability lanes are ONE question

Pilot r36_lawcount_geom (round 36, bank 1). Coordinator
verifications: (LA-EQ)'s five-line derivation hand-checked against
the cited PROVED lines of saturation_rigidity and the RNC node;
the H1 closed form's algebra hand-checked (Q(g,.) = a(g-h)sigma_g,
Q(h,.) = b(g-h)sigma_h); the m=3 generalized-fence arithmetic
hand-checked; the (RIC3) and row-surplus nodes read (both PROVED,
exactly as subtracted).

- **(LA-EQ), the repricing reading:** for any hypothesis set H
  satisfied by the restriction of a strict A=3, e=m endpoint
  configuration to 7m-1 of its >= 15m parameter-saturated points,
  (LA-W COUNT | H) IMPLIES the endpoint is empty — the endpoint's
  own nonzero kernel biform lies in the layer-A kernel of the
  restriction. The rank theorem was never a route to the
  exclusion; it is a STRICT strengthening (strict because of the
  next bullet). Five lines from (SAT4)-(SAT5) + (RNC1)-(RNC2),
  both PROVED; a reading, not new mathematics — priced as such.
- **RUNGS H1 AND H1+H2 ARE CONSTRUCTIVELY FALSE.** The closed
  form Q = (Z-g)(Z-h)C(X) + a(Z-h)sigma_g(X) - b(Z-g)sigma_h(X)
  satisfies H1 by construction (two degree-rho supports split over
  mu_32, |S_g ^ S_h| = m-1); merging the induced second slopes is
  LINEAR in C: 4047/4047 (q=97) and 4426/4426 (q=193) admissible
  builds all have nullity 1. Forcing H2 (ALL pair intersections
  <= m-1, T = 9 exactly) leaves one scalar condition, solved:
  exhibits on both fields (supports [7,7,2,2,2,2,2,1,1], max
  pair-intersection 1, nullity 1), verified by two independent
  code paths; controls (unsolved shape, random saturated) give
  nullity 0 at 40-60/cell. NOT of invariant/subgroup type
  (P_1 != 0; slopes not a coset).
- **THE FENCE IS AN INFINITE FAMILY.** Q_0 = Z^m - X^{2m}, W
  inside 4 fibres of x -> x^{2m} on mu_{16m}, Gamma = the 4m
  m-th roots + one spare: saturated a = 7m-1, nullity EXACTLY 2m
  (measured m = 2,3,4,6 over five fields; = Codex's fence at
  m=2). The bare count is dead at EVERY m >= 2. Binomial
  subfamily classified (k = 2m admissible for all m <= 12; at
  m = 2 it is the UNIQUE admissible k — why the fence looked like
  an accident and is not).
- **THE EXACT FAILURE LOCUS ((LA-PADE)/(LA-DEG); mechanism =
  the PROVED (RIC3), found by subtraction after derivation):**
  nullity(E_I) = dim of the simultaneous Pade/Hankel kernel over
  the elementary-symmetric slope data E_j, with the reduced-basis
  degree formula dim K_j = max(0,4m-d_j) + max(0,4m-d'_j),
  d_j + d'_j = 7m-1 — agrees 9/9 with direct nullity including
  the fence (8-4 = 4) and the m=1 sign ((4-3)+(4-3) = 2, which
  (LA-EQ) also forces since the m=1 endpoint is realized).
  (RIC3)'s scope note ("one coefficient block") is exactly what
  the all-block form extends. CROSS-POINTERS of record: the
  saturation-count fence node, (RIC3), and the row-surplus fence
  (its m=1 instance) are three faces of one mechanism; neither
  fence node cites (RIC3) — recorded here.
- **THE LADDER TERMINATES AT THE OPEN PROBLEM.** The rung that
  kills every constructed counterexample is (SAT2)/global block
  completion (the exhibits sit at O in [34,37] against the cap
  m-1 = 1) — and a configuration PASSING that rung is a realized
  (SAT3) witness at m=2. **The layer-A lane and the realizability
  lane are the same question from two sides: a positive on either
  settles the other's negative.** Transportable to the
  realizability search: the closed form above is a starting
  variety that satisfies the pair-union + pair-cap geometry
  exactly, leaving all freedom for block completion.
- **STATUS AFTER THIS BANK:** layer A remains a per-witness
  instrument (round 35's completion-independent kills are
  untouched); the ambition of a standalone universal exclusion at
  a = 7m-1 is retired; the board's face-off collapses into ONE
  question — (SAT2)-completable saturated configurations, i.e.
  (SAT3) realizability at m >= 2 — attacked from the B-design
  side and now equipped with this bank's starting variety.
- **SCOPE FENCES:** H3/H4 untested (structural coverage via
  (LA-EQ) only); the H1+H2 refutation is m=2/two-field (enough to
  kill the m >= 2-quantified statement, no more); the O minima
  are sample minima over six exhibits; the generalized fence's
  2m is constructed-lower-bound + measured-equality (ten cells);
  no (SAT2)-satisfying configuration at m >= 2 was built or
  sought; everything hypothesis-class conditional.

## Round-36 (SAT3)-on-(L2) addendum (2026-08-11, coordinator-audited): T >= 1 achieved — the layer is non-vacuous; the (L2) stratum is rationally parametrized; the realizability ledger's m=2 cell flips

Pilot r36_sat3_on_l2 (round 36, bank 2). COORDINATOR HAND-CHECKS
(all pass): the elimination Q_2(f^2-kg) = Q_0(g^2+hf) from
E1*f + E2*g; both converse substitutions vanish IDENTICALLY; the
determinantal identity det([[f,k],[g,f]] + z[[g,f],[-h,g]]) =
(f^2-kg) + z(fg+hk) + z^2(g^2+hf) = L*Q_z expanded by hand; the
third ell-condition's implication (and its f(ell)=g(ell)=0
exception); the dimension 20+1-2-1 = 18; the +4-O arithmetic.

- **(PAR), THE PARAMETRIZATION OF RECORD:** L*Q_0 = f^2-kg,
  L*Q_1 = fg+hk, L*Q_2 = g^2+hf (deg f,g,h,k <= 4, L linear with
  root ell), subject to exactly TWO conditions at ell — a
  birational parametrization of the whole e=m=2 (L2) stratum, hit
  rate 1 (vs 1/q for the round-35 inversion, q^5 over blind);
  266,239 + 167,421 objects built in 95 s/field. Membership is a
  GCD: **(RES): det M(B) = 0 iff gcd(f^2-kg, fg+hk, g^2+hf) != 1**
  (1200/1200, two fields). Dimension 18 re-derived independently
  (= the round-35 measurement). m=2-SPECIFIC (the elimination
  uses deg(f^2-kg) <= deg Q_0 + 1).
- **(SAT3)-ON-(L2) IS NON-VACUOUS: T = 2 OVER mu_32** on
  certified e=m=2 objects (full certification table both fields;
  Möbius-normalised so both supported slopes are FINITE {0,1} and
  re-certified), by EXACT solve: prescribing Q_0 split is a
  square root mod g; prescribing Q_2 too is one proportionality
  in F_q[x]/(f), solved exhaustively over all C(32,7) subsets by
  meet-in-the-middle. T = 3 over a bespoke 32-set (126 instances,
  two fields; ZERO power for (SAT3) — the domain relaxation is
  never merged with the mu_32 column). CLASS SCOPING (the pilot's
  own first miss): banked T = 4 records are e = 1 — a class
  (ERC2) closes — so this is the first T >= 1 ever on e = m
  objects, the only class (SAT3) can inhabit. Round 34's
  designed-domain instrument now has input.
- **THE REALIZABILITY LEDGER'S m=2 CELL FLIPS (forced
  correction, second independent):** (ERC2) (PROVED) forces
  e = m for (SAT3), so the curve must lie on the 18-dim (L2)
  component, not the ambient 23-dim space the round-33 ledger
  used: excess -1-O -> **+4-O**. COORDINATOR STACKING NOTE: this
  correction (curve-side, 5 units) and round 34's automorphism
  quotient (solution-orbit side, +4..+6) are INDEPENDENT terms;
  stacked, the m=2 cell sits at ~ +8..+10 — the round-33
  conjecture "realizable iff m <= 2" is now doubly re-posed to
  m <= 1, consistent with the round-34 TCAP re-pose. The
  emptiness instruments now number FOUR (searched-negative;
  TCAP+quotient; the C(16m,4m-1) gate — sharpened here by
  2 log2 q to -61.3 bits at q=97 via the same dim-18 input; the
  flipped ledger) — still no mechanism, and the pilot's own
  positive half shows why counting stays untrustworthy (T=3 over
  mu_32 sits at +62.5 bits, q-INDEPENDENTLY — the 18-6T exponent
  vanishes at T=3 — yet no exact solve reaches it).
- **NO WALL WAS HIT — the finding.** The failure to reach T = 3
  over mu_32 is algorithmic (no third exact solve), not
  arithmetic. The predicted eventual obstruction is EIGENVALUE
  CONFINEMENT: the members' roots at x are the generalized
  eigenvalues of the 2x2 pencil P(x)+zR(x); (SAT3) needs all 32
  pencils rational-eigenvalued with all 63 slots in a 9-element
  alphabet; random (L2) objects deliver half the occupancy on 3x
  too many slopes. The m=1 coset fence does not FAIL at m=2 — it
  becomes INAPPLICABLE (d_x <= 1 cannot pose the doubling that
  T = 9 forces on 31 of 32 points).
- **HANDOFF OF RECORD: the third exact solve** (a third split
  member given Q_0, Q_2 — the analogue of the mod-f
  proportionality) is the single missing instrument between this
  round and T = 4; blind (L2) search is banned at rate-1
  parametrization. F1/(NEWCAP): still zero power (one supported
  pair; a* = 14 a single sample).
  [RE-POSED (round 37): NO third exact solve exists in (PAR)
  coordinates — the parametrization is a length-4 Hankel sequence
  (k,f,g,-h) whose TWO solvable slots (u_0, u_3) are consumed by
  the first two prescriptions; the third is an overdetermined
  type-(4,4) Cauchy interpolation (14 values, 9 dof, 2 scales —
  deficit 3, q^-3 per triple) with an exact O(1) test and no
  inverse; re-basing cannot create a slot (S_3 symmetry of the
  three minors). The open item of record is "an exact solve for a
  rank-deficient 14x10 Cauchy system" — Pade-lattice machinery
  (banked in the l1/xr lanes) is the pointer. See the round-37
  third-solve addendum.]
- **SCOPE FENCES:** two fields for all structure (five for
  ledger arithmetic); no T >= 4 built; (SAT2)/(SAT4)/(SAT5)
  inapplicable at T = 2 (reported: sum d_x = 14, no doubled
  point yet, vs the 31 doubles (SAT3) needs); m >= 3 untouched;
  the s != 0 degeneracy yield (42/46 rejected) has no predictive
  criterion yet. [RESOLVED (round 37): (SCRIT) — s = |S_0 ^ S_2|
  EXACTLY (four lines from (PAR); 251/251 two fields; hypothesis
  f(x)g(x) != 0 automatic on prescribed-split objects);
  restricting S_2 to mu_32 \ S_0 gives 100% s=0 yield at 1/7.00
  the cost. See the round-37 third-solve addendum.]

## Round-36 R-HRLOW addendum (2026-08-11, coordinator-audited): the band classified; h_r dissolved as the coordinate; STATEMENT U is the whole far-CA residual

Pilot r36_hrlow (round 36, bank 3). Coordinator hand-checks: the
common-support algebra (solving the 2x2 system for (y_0,y_1) in
terms of syn(u_1), syn(u_2)); the classification chain
(column-far => |W| >= r+1; one bad slope => f <= d; d=1 => f=1 =>
T_1 = r+1 FORCED); the razor over-determination ceil(rho/2)-1 =
2^33-1; the C(128,63)-vs-C(127,64) relation (ratio 128/65, ~0.98
bits — ONE binomial step, not equal; correspondence still to
check). All pass.

- **THE DICTIONARY: h_r = rho + deg(e_1/e_0)** on the common
  support (210/210 across 5 razor-faithful shapes x 5 fields;
  dim K_0 = r+1-rho-d likewise; 2rho when the ratio is not
  polynomial), INDEPENDENT of the support size s (12 degree pairs
  x 5 support sizes, 2 fields). [SCOPE-CORRECTED 2026-08-11 (mint
  wiring audit): the formula holds for d <= rho ONLY — the
  stacked matrix has 2rho rows, so polynomial ratios of degree
  d > rho saturate at h_r = 2rho exactly like non-polynomial
  ones (exhibited: rho=2, d=3, q=601 gives h_r = 4, not 5). All
  210 banked rows lie in scope; the wired node
  rate_half_far_ca_hr_dictionary_common_support carries the
  corrected form.] And **COMMON SUPPORT IS A
  THEOREM, not a family choice**: any column-far pencil with two
  bad slopes is generated by two errors on S_1 u S_2 (explicit
  reconstruction 12/12, two fields).
- **D1 ANSWERED YES: LB1 is the unique h_r = rho+1 structural
  family, and its T_1 = r+1 is FORCED** (d=1 => |W| = r+1 exactly
  => injective L => every value a slope). Exhaustive census: T =
  T_1 = r+1 with ZERO accidentals at q = 65537 AND q = 999983
  (mu_1 down to 1.26e-7). The p* CONVERSE is REFUTED (p* = 6 at
  both h_r = 3 and h_r = 4; p* is a coarser invariant and must
  not label strata — R-PSTAR-INTERMEDIATE retired as a stratum);
  the extended law p*(d) = max(rho+d, floor((R+1+d)/2)) holds
  205/210 with 5 NAMED failures (H2 symmetric-T quadratic, 5/5
  fields — p* is not a function of (R, rho, d)).
- **D2: THE h_r = rho+2 BAND IS NOT MOMENT-BOUND — the brief's
  antecedent is false.** The band carries a structural floor
  ceil((r+1)/d) that REACHES r+1 (injective quadratic ratio, 5
  shapes x 5 fields); even h_r = 2rho carries T_1 = r+1 (the
  cubic family at rho=3) — FG's floorlessness is a property of
  witness B's particular K_0, NOT of h_r (R-FG-RAZOR further
  downgraded). "LB1-limited" survives only as a VALUE (r+1),
  conditional on U below.
- **THE ROUND'S FIND: THE NEGATION-CLOSURE EXCESS.** On a
  negation-closed evaluation domain (which the official
  power-of-two multiplicative subgroup IS), column-far
  razor-faithful pencils exist with **T = 95-98 against r+1 = 9,
  field-size independent, at mu_1 down to 1.26e-7** — beating the
  first moment by 750x with zero saturation. Mechanism EXACT:
  even locators sigma(x) = Q(x^2) collapse the odd Hankel rows;
  count = C(m-1, r/2-1) (84/84 and 330/330, two fields); control
  decisive (same everything on non-closed {1..20}: T = 10). The
  carrier is the banked e22 orbit-invariant locator algebra
  L_B(X)G(X^M) — now deployed as a far-CA bad-slope mechanism.
  **KILLED AT THE RAZOR EXACTLY: ceil(rho/M) = 1 needs M >= rho =
  2^34; at M = 2 the surplus is 2^33-1 conditions.** A
  rho-threshold, not a field threshold. WARNING OF RECORD: any
  far-CA counting argument treating D as a generic point set is
  unsound at small rho. GAP: the symmetric-T variant is
  unmeasured at rho >= 3 (parity predicts survival at rho = 3,
  death at rho >= 4; 2^33 conditions of razor slack either way).
- **THE DICHOTOMY OF RECORD (R36-D):** T = T_fib + T_sym +
  T_rand; T_fib in [ceil((r+1)/d), r/f+1] with = r+1 iff f = 1
  and chi injective ((C3)-attainment is the SHADOW of f = 1, not
  the mechanism — and the fibre cap is a from-scratch pigeonhole,
  nothing imported through the vacuous type-2 ledger); T_sym
  needs an automorphism of order >= rho; T_rand is moment-priced
  (zero power). Falsifiers F-1/F-2/F-3 pre-registered in form.
- **STATEMENT U — the far-CA residual reduced to one sentence:**
  at razor shape, every bad slope of a column-far pencil admits a
  locator INSIDE W = S_1 u S_2. **U implies B_ca^far(k+2^34) =
  r+1 = 2^39.977280 EXACTLY** (floor: banked LB1; cap: the fibre
  pigeonhole). U = "T_sym = T_rand = 0"; U-sym is killed at razor
  rho by condition counting (modulo the rho=3 symmetric-T gap);
  U-rand is completely unpriced (the honest residual).
  [REFUTED AS A THEOREM (round 37): U-rand slopes are
  CONSTRUCTIBLE at fixed exchange rate rho conditions each —
  engineered column-far razor-faithful pencils on mu_n have
  T = (r+1)+j exactly for j up to the parameter cap
  (2(r+1)-1)/rho (exhaustive censuses at mu_20 and the full
  C(26,10) at mu_26). U survives only as the DEFINITION of the
  fibre stratum. THE PIN IS WITHDRAWN and replaced:
  B_ca^far(k+2^34) = r+1 + Theta(n/rho); constructive floor
  r+1+126 = 1,082,331,758,719 modulo one genericity lemma (kernel
  dim exactly 2 at j = 126); heuristic cap the same 126; in bits
  2^39.977280 unchanged to six decimals. Also corrected: the
  floor(rho/2) parity count is CEIL(rho/2) (symmetric-T dies at
  rho = 3, not 4 — the parity prediction refuted; the fused
  carrier's threshold is M >= 2rho-1, not M >= rho); "T_rand is
  moment-priced (zero power)" is false in the direction that
  matters (the mechanism needs NO automorphism). See the round-37
  U-rand addendum.]
  Residual
  map: R-HRLOW dissolved into R-U; carriers for U named (the
  split-pencil equivalence frame; the e22 locator algebra + the
  M >= rho threshold; the bivariate locator-extension node, which
  is scoped as exactly-the-missing-hypothesis). CHECK QUEUED: is
  the T_sym carrier at M = rho (C(128,63), ~2^124.15) the banked
  qcore plateau C(127,64) = 2^123.1714 (one binomial step)? If
  yes, T_sym inherits a proved cap. [CHECK DONE (round 37):
  DIFFERENT objects (orbit-invariant LOCATORS vs qcore CODEWORDS;
  ratio exactly 128/65, log2 = 0.977632 != 0.977280 — two
  different 0.977s); the Lam-Leung+nesting CAP does NOT transport;
  the DEDUP does (multi-scale T_sym families collapse to one
  scale).]
- **SHAPE FENCE (fourth flag, applied on the supplier node):**
  "B_ca^far(n-r) <= r+1" is PROVED only at the official row's own
  shape (r <= R/2); it is FALSE as a universal at r > R/2 on
  negation-closed D (T = 95 exhibit). One sentence added to
  split_pencil_equivalence.
- **SCOPE FENCES:** all machine numbers at q <= 999983, rho <= 4
  (widening from the registered 65537 disclosed); no exhaustive
  total-T census at rho >= 3 (the even-locator carrier IS swept
  completely there); char 2 unmeasured; T_rand unpriced;
  everything else per the pilot's 13 zero-power declarations.

## Round-36 (SHARE3-4) addendum (2026-08-11, coordinator-audited): the m=4 gap is ONE coincidence; the demand law corrected to linear; Lüroth identified

Pilot r36_m4_nonsplit (round 36, bank 4). Coordinator hand-checks:
the Lüroth degree arithmetic (deg_x = k*deg_w; k = m-1 gives
deg_w = 3 exactly; waste = 3(m-1) mod k, reproducing the even-m
lost unit at k=2); the demand calibration (D(2,2) = 8 at m=3;
D(3,3) = 11 at m=4; D_max = (8m-9)-(4m-1) = 4m-8); the m=4
3-sharing structure chain ((OV) equality => pair multiplicity 1;
per-side => d <= 2 => s = 13 forced); Lemma 1 (Möbius injectivity
6m > rho); the Cauchy-Schwarz bound. AUDIT NOTE: the closed-form
demand display is the divisible-case idealization — the ceiling
version (e.g. 25 = 36+4-15 at m=4, k=2) is operative.

- **ORDER-3 SHARING IS A LÜROTH PULLBACK, and the machinery is
  BANKED** (the pilot's own load-bearing subtraction, verified:
  f_weight2_inverse's GLOBAL PULLBACK Theorem 1 + payment_
  completeness's Lüroth-lattice unification — the repo already
  states the lattice subsumes multiplicative and affine-involution
  as one class; anchor 1's sigma and this w are members). New
  here: the identification of (BIV-CURVE) tuple-sharing as a
  lattice member + the x-degree arithmetic (maximal sharing is
  FREE in the budget — the exact opposite of the involution's
  wasted unit).
- **(SHARE3-4), the sixth m=4 class — full target REACHED, gap =
  ONE coincidence.** The line-in-P^3 reformulation (a 3-sharing
  pattern = a line through >= 8 of the 41664 mu_64-split cubics)
  gives the lane's first exhaustive-per-base non-DFS instrument.
  The pencils EXIST (12/9/9 complete fibres at q = 193/257/449)
  and are CONSTANT-NORM — the mu_N group structure supplies the
  sharing (fixed root-product costs 1/N, not 1/q), refuting the
  pilot's own registered q^-12 moment by 3400x (falsifier fired,
  threshold withdrawn — the third instrument-class this round
  where counting died on structured sets). |W| = 27 = 7m-1 lands
  exactly; the selection layer is FREE (13208 + 14594 of 40000
  structurally-verified legal draws); k = 8 of 8 reached — the
  first m=4 class ever to reach its full target; the shortfall is
  |slopes| = 14/15 vs 13 required (ONE/TWO coincidences, 40000
  ALLOC draws per field). m = 4 stays OPEN, six classes
  searched-negative, and this class is the live route.
- **THE GUARD AS THE FINDING:** the raw search reported a witness
  on the coincidence currency (C = 12 vs demand 11) that the
  structural verifier killed — one slope with hypergraph degree 8
  (a common root of Psi~) blowing the per-side cap by 8x. The
  registered quantity was satisfied while the configuration was
  infeasible; caught BEFORE being reported as a result.
- **(DEG-m): zero selection power, decisive at completion.** The
  tightened and relaxed 2-sharing ceilings are BIT-IDENTICAL
  (7/12, two fields) — it is a completion-level condition; but
  every ceiling configuration has n_1 = 9 against the
  completeness bound 4: **the 2-sharing m=4 negative upgrades
  from a ceiling to dead-objects-at-the-ceiling** (two fields).
- **THE FLAT-SUPPLY LAW, PART-PROVED:** unconditional for
  pencil-image classes — no degree-1 factor (Lemma 1) + AM-HM +
  Cauchy-Schwarz give required cross-coincidence >= ~m-5,
  VACUOUS for m <= 6, BINDING from m = 7; with the measured
  Weil-type supply the pencil classes die for q >~ 10^4 at every
  8 <= m <= 128 (CONDITIONAL). The o(m^2) supply bound is NOT
  delivered; m = 4 is untouched by the theorem (vacuous there,
  pre-declared).
- **SCOPE FENCES:** no G built, no completion, no bivariate
  system, nothing gated by bank 2's verifier; mu(x)-at-middles
  unchecked; sporadic (non-factoring) sharing unsearched (priced
  < 1e-4); base triples sampled (60-800 of 41664, exhaustive per
  base); the constant-norm censuses exhaustive over their named
  sub-families only; (OUT-m)/(DEG-m)-derived statements inherit
  POSED status. COMPLIANCE: ONE bare-python3 breach (empty
  heredoc no-op) — the first since the round-33 censures; the
  11-pilot clean streak ends; self-reported FIRST, censured.

## ROUND 36 CLOSE (2026-08-11): the four banks reconciled — construction is the only currency

**BANK 1 (r36_lawcount_geom):** the rank target RETIRED ((LA-EQ):
it strictly implies the endpoint exclusion; H1 and H1+H2 refuted
constructively; the fence an infinite family, nullity 2m; the
failure locus = the PROVED (RIC3) mechanism) — **the layer-A and
realizability lanes are ONE question**, with a closed-form
starting variety handed to the realizability side. **BANK 2
(r36_sat3_on_l2):** (SAT3)-on-(L2) NON-VACUOUS — T = 2 over mu_32
on certified e=m=2 objects via (PAR), a rational parametrization
of the whole stratum (rate 1; membership = a gcd); the
realizability ledger's m=2 cell flips (+4-O; doubly re-posed
m <= 1); the missing instrument is a THIRD EXACT SOLVE. **BANK 3
(r36_hrlow):** h_r dissolved (= rho + deg ratio; common support a
theorem; LB1 unique-and-forced; the rho+2 band floor-carrying);
the negation-closure excess found (T = 95 vs 9, mu_1-free) and
killed at razor rho; **STATEMENT U: every bad slope has a locator
inside W => B_ca^far(k+2^34) = r+1 EXACTLY** — U-sym
condition-killed, U-rand the unpriced residual. **BANK 4
(r36_m4_nonsplit):** the m=4 gap cut to ONE coincidence by the
Lüroth/constant-norm (SHARE3-4) class; the demand law corrected
(linear under maximal sharing); the flat-supply law part-proved.

**THE RECONCILED PICTURE.** The round's meta-result: **counting
died as a verdict-carrier, three more times** (the 11m-4-vs-+4
lesson repeated by the pilot's own q^-12 refutation on
constant-norm sets; the H1+H2 nullity-1 families against the
excess; the ledger flip that still cannot exclude). Every load-
bearing move this round was a CONSTRUCTION: the H1+H2 families,
the (PAR) parametrization + T = 2 objects, the T = 95 pencils,
the constant-norm 3-sharing pencils. The frontier after round 36:

1. **The converged small-m question** ((SAT3) realizability =
   layer-A rank over completable configurations): attacked from
   the B-side with rate-1 parametrization and T = 2 achieved;
   FOUR counting instruments say empty, ZERO mechanisms; **the
   third exact solve is the named instrument** — it decides
   whether T climbs to the q-invariant +62.5-bit T = 3 cell and
   beyond, or walls into the first genuine mechanism.
2. **Far-CA = STATEMENT U** (U-rand the only unpriced mode);
   proof carriers named; the C(128,63)-vs-C(127,64)
   correspondence queued.
3. **(BIV-CURVE) m = 4**: one coincidence short, on a class whose
   existence mechanism (constant-norm on mu_N) is exactly
   understood — more fields / finer constant-norm sub-families /
   exhaustive line censuses are cheap next probes.

**AUDIT LEDGER (11th consecutive catching round):** my round-35
"law of record" demand row corrected (middles undercharged; the
quadratic an artefact); my wave-59/round-35 anchor-1 pricing
retired by (LA-EQ); the round-34 narrowing corrected AGAIN
(mu_1-free excess); the round-33 realizability ledger's ambient
dimension corrected ((ERC2)-forced 18); h_r retired as a
coordinate; the round-34/35 h_r-floorlessness reading corrected
(witness-B's K_0, not h_r); p*-converse refuted. COMPLIANCE:
banks 1-3 clean (9th-11th consecutive); bank 4 ONE bare-python3
breach (self-reported first — the honesty machinery held; the
streak resets). ROUND-37 RULES: results files never through a
pipe; the helpers-duplicated-per-file anti-import pattern
recommended.

**ROUND-37 ANCHORS (priority order):** (1) THE THIRD EXACT SOLVE
(T >= 3 over mu_32 — the single named instrument of the converged
question); (2) U-rand (price or fence the codeword-mediated mode
— the last far-CA unknown); (3) the (SHARE3-4) one-coincidence
gap (constant-norm at more fields; exhaustive line censuses;
the split sub-case fence); (4) the rho = 3 symmetric-T gap +
the C(128,63) correspondence; (5) THE MINT WAVE (the queue now
holds ~30 items across rounds 34-36 — a consolidation round is
due); (6) m = 1 16=16 node + the eigenvalue-confinement shape.

## Round-37 U-rand addendum (2026-08-11, coordinator-audited): STATEMENT U REFUTED — the far-CA count is r+1 + Theta(n/rho); the coset-leader frame; U-sym closed

Pilot r37_urand (round 37, bank 1). Coordinator hand-checks (all
pass): the MDS identification (ker syn = degree-<= k-1
restrictions; d_min = R+1); FENCE-1's two-line contrapositive; the
rho-1 over-determination ((f+t)-(|W|+t-R)-1 = R-r-1, independent
of t and f); the razor kernel arithmetic (2(r+1) - 126*rho = 2
EXACTLY, so the cap is 126 with kernel dim 2 on the nose);
r+1+126 = 1,082,331,758,719; the ceil-vs-floor parity collapse
(rows 2s and 2s+1 fuse on the carrier).

- **THE COSET-LEADER FRAME (the round's instrument):** every bad
  slope decomposes as u = h_gamma + c with c in the [n,k] MDS
  code ker syn — the far-CA count is a coset-leader problem, and
  the adversary's currency is 2(r+1) field values of (e_0,e_1) on
  W at RHO CONDITIONS PER CODEWORD-MEDIATED SLOPE (three
  independent derivations; spend- and f-independent).
  **FENCE-1 (unconditional, the surviving fence):** |S_gamma u W|
  <= R forces c = 0 — no near-W slope is codeword-mediated
  (297/297 incidences, 14 rows, 2 shapes, 2 domain types; the
  inequality itself is the banked minimum-distance spend, here
  instantiated at the forced |W| = r+1 — cross-reference added so
  it is not re-derived again). MINIMAL-SPEND RIGIDITY: at t = rho
  the mediating codeword is minimum-weight with W inside its
  support (18/18; W in supp(c) at 297/297 — stronger than
  derived). The c-side analogue of chi is chi_Y : W -> P^2;
  U-rand at minimal spend = rho+1 collinear points of chi_Y(W).
- **STATEMENT U IS FALSE.** The adversary CHOOSES the
  collinearity: fixing j configurations and solving the LINEAR
  system (unknowns 2(r+1)+j, equations j(rho+1)) yields
  column-far razor-faithful pencils with **T = (r+1) + j EXACTLY**
  — verified by exhaustive census at mu_20 (j = 1,2,4,6,8 = the
  cap, three fields) and by the FULL C(26,10) = 5,311,735 census
  at mu_26 (T = 17 = r+1+6, T_fib = 11 = r+1, column-far, a
  factor 45,000 over the first moment). On the razor's own domain
  type; needs NO automorphism; works at rho = 3.
  **THE NEW PRICE: B_ca^far(k+2^34) = r+1 + Theta(n/rho).**
  Constructive floor r+1+126 (modulo R-GENERICITY: full rank +
  four open side-conditions, each held 60/60 at every reachable
  cell); heuristic cap the same 126; the prize question untouched
  (2^39.977280 to six decimals either way; log2(r+1+126)/2^39 =
  2^0.977279924).
- **U-SYM CLOSED, AND THE PARITY DERIVATION CORRECTED:** the
  symmetric-T carrier (X-x_0)P(X^2) fuses the two parity blocks —
  the count is CEIL(rho/2), not floor — so it DIES at rho = 3
  (measured: carrier = fibre exactly, excess 0, at rho = 3 and 4,
  2 fields x 2 shapes x 2 domain types; excess 318 at rho = 2).
  The round-36 T = 336 anomaly is decomposed exactly (5 fibre +
  323 carrier + 8 residual vs null 7.59; on mu_22 carrier explains
  330/330). Residual carrier-exhaustiveness question: is
  (X-x_0)P(X^2) the only parity-collapsing carrier at odd r?
- **T_rand ON GENERIC PENCILS IS NULL-COMPATIBLE (10/10 rows in
  the envelope, -> 0 at large fields)** — but the null is a MEAN
  and B_ca^far is a MAX: the engineered pencils beat it by 4.5e4.
  A clean generic null is not a fence — the lesson, again.
- **THE FAR-CA RESIDUAL MAP:** R-U retired (refuted). **R-URATE
  (new, load-bearing): is the exchange rate rho tight — prove
  T_rand <= 2(r+1)/rho** (a finite rank question on the
  j(rho+1) x (2(r+1)+j) incidence matrix). **R-GENERICITY (new):
  the full-rank + side-conditions lemma converting the +126 floor
  to unconditional.** R-USYM: close (carrier-exhaustiveness the
  only residue).
  [ROUND-38 UPDATE: R-URATE REFUTED as posed — the EXCHANGE LAW
  replaces it (T <= (r+1) - delta + floor((2(r+1)-1+delta)/rho);
  rank deficiency in Phi buys 1/rho slopes at the cost of one
  fibre slope; profitable at small rho: T = 19 > cap 18 at C3,
  FULL C(26,10) census, THREE fields; the banked T = 17 was
  search-limited — j = 7 gives 18. At the razor delta = 0 is
  optimal so 126 STANDS, but normal-form-conditionally with a
  17.17x PIGEONHOLE margin — not algebraic. R-GENERICITY's RANK
  HALF PROVED (the line-pencil decoupling rank M = j(rho+1) - L
  + rank Phi; multiplicity <= 2 => full rank; the razor j = 126
  exact-double-cover kernel in closed form, dim 2 exactly) + 2
  of 4 side-conditions PROVED (lambda_i != 0 fails on EXACTLY j
  of q+1 kernel points; gamma_i off-fibre by union bound);
  residue = chi-injectivity inside forced multi-edges (relaxable
  to <= 125 collisions) + column-farness Case B. R-USYM CLOSED
  (carrier completeness by degree parity at odd r; excess 0 both
  ways over ~560k locators, 2 shapes 2 fields). See the round-38
  URATE/genericity addendum.] Everything else unchanged. WARNING transported
  to the counting lanes: any far-CA upper bound pricing only the
  fibre stratum is off by an additive Theta(n/rho); T <= r+1 is
  unprovable at razor shape — do not spend on it.
- **SCOPE FENCES:** the +126 floor is constructive-MODULO-
  GENERICITY (never claimed proved); the integer-collinear
  minimal-spend family is a stand-in-domain artefact with ZERO
  razor power (three rational hits, declared, used for nothing);
  exhaustive censuses exist at C(20,8)/C(22,9)/C(24,10)/C(26,10)
  only (the rho = 4 construction is slope-verified but its total
  T unmeasured); q <= 999983, odd prime fields only; the type-2
  ledger was not imported (vacuous on the bracket). Pilot
  compliance: 5/5 ramguard clean (append-mode results files, no
  head pipes — both new rules held on first outing); the pilot's
  own blind constant log2(128/65) wrong in the 4th decimal,
  self-reported (miss 1).

## Round-37 mint-drafts addendum (2026-08-11, coordinator-audited): 10/10 packages drafted and verifier-passing; twelve discrepancies dispositioned; wiring deferred to the post-close mint session

Pilot r37_mint_drafts (round 37, bank 2 — a DRAFTING bank, not a
research bank). 10 of 10 mint packages complete (statement.md +
node.json + PASSING verify.py each; proof.md where status
warrants), drafted from the round-34..36 addenda with exact
sourcing and conservative statuses. Coordinator spot-replays:
packages 1, 2, 5 re-run PASS (the (PAR) verifier rebuilds the
banked T=2 witness from (f,g,h,k,L) alone and settles the
third-condition implication EXHAUSTIVELY over F_13^4 — exactly
(q-1)^2 exceptions, all f(ell)=g(ell)=0; the fence verifier
confirms the row-collapse on all 1158 covering locators and the
bad-set = covering-set identity). WIRING DEFERRED to a dedicated
session after the round closes (task #41): the exemplar format
needs 7 more files per node incl. the independent verify_audit.py
second code path; package 1 (statement_u) must be re-drafted
against the round-37 bank-1 REFUTATION; packages 8/10 blocked on
D11/D9 until now.

**DISCREPANCY DISPOSITIONS (the pilot's D1-D12, coordinator
rulings):**
- **D1 (a* convention) — ACCEPTED AS A GENUINE AMBIGUITY, ruling
  queued:** the round-35 a* = 13 reproduces only under the
  PROJECTIVE reading (roots at infinity counted); the affine
  reading gives 12 on the same witness. NO F1/(NEWCAP) pricing
  until the convention is ruled; flagged to the F1 ledger.
- **D2 ((RES) iff) — CORRECT SPLIT:** forward PROVED (one line),
  converse MEASURED (1200/1200). Package 2 carries it so; my
  round-36 addendum's bare "iff" is qualified by this record.
- **D3 (the covering count) — A GENUINE GENERALIZATION, ADOPTED:**
  C(m-1, r/2-1) is the off = 1 face of C(m-off, r/2-off),
  off = m-(r+1); the general law reproduces ALL SIX banked cells
  (165/715/3003/1365 at H4-H8 included) — verifier-confirmed.
  The round-36/37 fence texts are hereby read with the general
  law; the drafting pilot's own contribution.
- **D4 (locators vs slopes) — CONFIRMED:** 330 locators, 329
  slopes at H3; only slope counts enter T. Recorded.
- **D5 ("the official row's own shape") — CLARIFIED:** the phrase
  denotes the a = 3n/4+1 evaluation point (r = B*-1 <= R/2),
  OUTSIDE the open bracket; at the crossing offset a = k+2^34 the
  row has r = 63*2^34 > R/2. This is exactly why Statement U(')
  needs its own cap. Wording tightened here, not silently.
- **D6 (the 8/25/47 rule) — RESOLVED:** the ceiling table
  D = [(m-1) * ceil(6m/k)] + [(m-2) * ceil((m-1)/k')] - (4m-1)
  at k = k' = 2 generates 8, 25, 47 (the closed-form display was
  the divisible-case idealization — already noted at the bank-4
  audit; now stated once, here).
- **D7 (the "(11 at m=4)" parenthesis) — NOT A DEFECT:** 4m-8
  holds for m >= 7 (tD = 7 requires m >= 7); at m = 4 the true
  ceilinged value IS 11 = D(3,3). The text was correct; the
  reader-trap is now disarmed by this note.
- **D8 (the m <= 6 vacuity boundary) — CONFIRMED SOFT:** the
  crossover at m = 7 is the load-bearing claim; the ~(m-5)
  constant is soft. Round-36 bank-4's own MISS 4 already recorded
  the off-by-one; consistent.
- **D9 (the gate formula) — RESOLVED BY THE COORDINATOR:** the
  expression IS banked, at r35_rout_layer_a/REPORT.md:242
  (log2 E = [(m+1)(rho+1)-4] log2 q + log2 C(q+1,T) +
  T[log2 C(16m,4m-1) - rho log2 q]; the dim-18 sharpened variant
  in r36_sat3_on_l2's registrations) — the ADDENDA never
  reprinted it. Calibration re-verified by hand (+13.75 at m=1,
  q=17). Package 10 unblocked; pointer recorded here so the
  formula is never "lost" again.
- **D10 (sign conventions) — CONFIRMED:** the locator-layer and
  TCAP ledger rows use opposite conventions and agree in VERDICT
  only; never to be added. (Already flagged at the round-34
  bank-4 audit; now on the node.)
- **D11 (deg_H collision) — RULING: the (DEG-m) quantity is
  RENAMED deg_Sh** (sharing-hypergraph degree) **at wiring time**;
  the PROVED a1 node keeps deg_H. Package 8 unblocked.
- **D12 (fence duplication) — CONFIRMED:** package 6 cites the
  wave-59-node coordinator addendum rather than re-claiming the
  generalized fence; its contributions are the fresh m=3 replay
  (60x48, nullity 6 = 2m) and the explicit H1+H2 linear solve.
  The missing (RIC3) cross-citations go in at wiring.

**SCOPE:** drafts are PROPOSALS — no node is wired, no status is
assigned in the DAG by this bank; the verifiers replay statements
and banked constants, NOT the original experiments (the pilot's
own zero-power declaration, held). Pilot compliance: 25/25
ramguard clean; anti-import pattern; one parent-dir ls disclosed
(names already known from CONSTRAINTS). Anchor 1's Codex-cycle
window (L3967-4269) was NOT read by the pilot — the wiring
session must subtract packages against it.

## Round-37 (SHARE3-4) gap addendum (2026-08-11, coordinator-audited): the one-coincidence gap DERIVED (budget 8 vs demand 11); the constant-norm census exhaustive and the threshold corrected; THE SIDE DOOR IS LEGAL

Pilot r37_share3_gap (round 37, bank 3). Coordinator additions:
the (SAT4) side-door legality CHECKED (the pilot priced it and
left it unopened — see below); the round-36 decay/threshold
figures withdrawn on the strength of the exhaustive census.

- **THE GAP NOW HAS A DERIVATION.** An incidence is the rank-one
  tensor w(t) (x) v(gamma) (v on a rational normal cubic — the
  lane's own banked device, correctly subtracted); a merge edge's
  available directions form a SURFACE Sigma_ij = P(W_ij) x nu of
  dim 2 in P^15, so a span of dim d meets it only at d >= 14:
  **7 edges cost 2 each, the 8th costs 1, a 9th is impossible —
  the prescribable-merge budget is 8 against a demand of 11.**
  Measured BIT-IDENTICALLY at two fields (cost-2 in 700/700 draws
  at every dim 0..12, first cost-1 at dim exactly 14; 8 edges in
  690/700). The residual 3 merges must be free: measured mean
  0.096/0.079, maximum ever observed 2 (this round + round 36's
  80000 draws). Best legal |slopes| = 14/15 — the two-round
  ceiling is now EXPLAINED, not just reproduced. GRADING: a
  generic-position count (700/700, zero exceptions), NOT a
  theorem and NOT an exclusion — the 11-merge variety has
  expected dim 4 over F_qbar (two agreeing counts), and the
  UNRESOLVED TENSION is that it is cut out by 11 DETERMINANTAL
  conditions a myopic edge-scan cannot reach: the named open
  route is a simultaneous determinantal solve (Groebner-scale,
  beyond stdlib+ramguard).
- **THE EXHAUSTIVE CONSTANT-NORM CENSUS (the mu_64-orbit
  reduction):** gcd(3,64) = 1 makes u -> u^3 a bijection, the
  action is transitive on e_3, so the e_3 = 1 slice (651 = 41664/
  64 split cubics, predicted = measured at five fields) DECIDES
  the whole family. Result: pencils with >= 8 disjoint complete
  fibres = 5056/960/128/**0**/**0** at q = 193/257/449/577/641 —
  **exhaustively EMPTY at 577 and 641** (round 36's sampled null
  upgraded to non-existence; q = 641 never previously run).
  **WITHDRAWN: round 36's ~q^-7 decay and ~690 threshold** (the
  banked REPORT figures stay byte-original; the record of use is
  corrected here): the measured decay is ~q^-4.4 overall, NOT a
  power law (hard zero in (449, 577]), and the supply is MONOTONE
  DECREASING from q = 193 — the round-37 brief's "peaks at
  moderate q" premise was WRONG (coordinator brief error,
  recorded). FIELD-WINDOW CORRECTION of record: mu_64 <= F_q^*
  forces q = 1 mod 64 — exactly {193, 257, 449, 577, 641} in
  [97, 690]; "map densely" was impossible as briefed.
- **THE SIDE DOOR IS ARITHMETICALLY LEGAL (coordinator check —
  the round-38 headline anchor):** one fibre with a repeated
  slope drops the slot count 24 -> 23, so **10 merges suffice —
  which round 36 ALREADY ACHIEVED**. Cost: its three points have
  |A_x| = m-1, so sum_x(m-d_x) = 3 = 1+O with O = 2 — and
  (SAT2) allows O <= m-1 = 3, (SAT4) allows the sum <= m = 4:
  LEGAL, exactly at the identity. What remains to check (a
  pilot's job, cheap): the per-side caps and incidence
  bookkeeping at the three deficient points, and building the
  actual configuration from a 10-merge draw. If it survives, the
  full round-34 pipeline (G, completion, bivariate system) runs
  on an m = 4 witness candidate.
- **DERIVED FENCES (both parameter counts, consistent with all
  measurements):** the split sub-case is deficient by 5 (three
  Möbius maps mod PGL_2 = 6 continuous merges vs 11); group
  symmetry buys <= 4 of 11 (d_gamma = |orbit| vs the cap 2 —
  answering the brief's mu_2 question in the negative by
  derivation). The interpolation law f_j = sum_i lambda_ji f_i
  (row sums 1) verified at two fields — the A-side triples are
  free, the B-side determined, the residual system dim 1.
  Structure lemmas: a constant-norm line has AT MOST ONE repeated
  root (r_0 = -d_2/d_1); the 64 degenerate lines ({30:31, 31:33}
  at all five fields) are the one-per-r_0 family — an independent
  census correctness check.
- **SCOPE FENCES:** m = 4 stays OPEN (six classes searched-
  negative; nothing excluded); the census is exhaustive over the
  constant-norm family ONLY; sporadic non-factoring sharing
  remains unsearched (priced < 1e-4); no G, no completion, no
  bivariate system, nothing gated by bank 2's verifier; the
  pilot's ALLOC replication was dead (all round-36 comparisons
  are against reported numbers); the near-miss slope-value bias
  is an instrument artefact. COMPLIANCE: ONE bare-python3 breach
  (empty heredoc — the SAME tic as round 36, second consecutive
  round: a PROCESS failure; the round-38 CONSTRAINTS add the
  pre-Bash checklist rule "any command containing python3 MUST
  match 'tools/ramguard (tiny|local) -- python3'"); imported-
  script rule fired correctly for the first time (the round-36
  script's module-level "w"-mode write was caught by the
  pre-import audit and the import REFUSED); results files
  versioned per run (the new rules held).

## Round-37 third-solve addendum (2026-08-11, coordinator-audited): the ladder has exactly two rungs; (SCRIT), (CONIC)/(SLOT), (OV4); T = 4 bespoke

Pilot r37_third_solve (round 37, bank 4; resumed after an
output-overflow crash — clean run, 6/6 ramguard). COORDINATOR
HAND-CHECKS (all pass): the cross-product form (row_0 x row_1 of
[[k,f,g],[f,g,-h]] = -L*(Q_2,-Q_1,Q_0) — expanded by hand); the
(CONIC) identity (both sides = f^2g^2 - kg^3 - hkfg + hf^3 over
L); the (SCRIT) four-liner (k = f^2/g and h = -g^2/f at a shared
root force LQ_1 = fg - fg = 0); the slot-consumption argument;
the Cauchy deficit arithmetic (14 - 9 - 2 = 3).

- **THE LADDER IS EXHAUSTED — STRUCTURALLY.** (PAR) is the
  2x2-minor (cross-product) vector of the 2x3 Hankel matrix on
  (k, f, g, -h) (verified 58/58 + 59/59). Prescribing Q_0
  consumes slot u_0 = k; prescribing Q_2 consumes u_3 = -h
  UNIQUELY (200/200 injective, two fields); Q_1 is then the third
  minor of a determined sequence. The third prescription is an
  overdetermined type-(4,4) Cauchy interpolation — not a
  proportionality, not a norm condition; exact O(1) TEST (one
  extended Euclid / one 14x10 rank), NO solve; q^-3 per
  subset-triple; re-basing to {0,1,inf} exposes the S_3 symmetry
  and cannot create a slot. A general lesson banked: a
  length-(n+2) sequence admits exactly n free prescriptions.
- **(SCRIT) — the s != 0 criterion, exact:** s = |S_0 ^ S_2|
  (251/251, two fields, joint histogram perfectly diagonal;
  unrestricted draws have the f=g=0 exception, 1/58 + 1/59 — the
  same species as (RES)'s refinement). Operational: S_2 in
  mu_32 \ S_0 gives 100% s=0 at 1/7.00 the search cost —
  replacing round 36's empirical 4/46 mortality with a zero-cost
  combinatorial filter.
- **(CONIC)/(SLOT), new identities:** Q_0g^2 - Q_1fg + Q_2f^2 =
  L*Q_0*Q_2; pointwise, the SECOND root of the member-quadratic
  q_x at any x in S_0 u S_inf is -f(x)/g(x) — one formula for
  both prescribed supports.
- **(OV4) — the lane's first exact structural law at m=2:** for
  any three supported slopes, e(k,i) + e(k,j) <= 4 (= deg(f+zg);
  the m=1 unique-vote argument of the banked f_dim1 transported
  to the sequence's MIDDLE PAIR). Zero violations in 374 T>=3
  objects, two fields. Sharpenings: e(k,i) <= 3 always; e = 3
  forces e <= 1 elsewhere. HONESTLY GRADED: a NECESSARY condition
  — the banked 9-vertex (SAT3) design is simple and PASSES with
  slack 2; (OV4) excludes concentrated designs only, a filter
  never an exclusion.
- **T-RECORDS:** T = 4 over a bespoke 32-set on certified
  e = m = 2 objects (first in class; both records fully
  certified, two fields; |union| = 23/24), via the BESPOKE DOUBLE
  SOLVE (both members prescribed split with free roots — an exact
  instrument giving 101x/62x the T>=3 rate of round 36's single
  prescription; the recommended default for all bespoke pushes).
  T over mu_32 = 2 — a TIE with round 36, honestly reported; the
  quantified gap to T=3 over mu_32 is 8.9e3x/3.9e6x the built
  object counts (absence where none was sought at the required
  rate). [SUPERSEDED (round 38): T = 3 OVER mu_32 IS ACHIEVED —
  ten witnesses, two fields, via the scale-elimination algorithm;
  the shortfall figures were an INSTRUMENT artefact (round 37's
  own d4_results.txt:54 already contained the feasible per-pair
  count 912,673, three lines below the shortfall it published);
  round 37's per-object rate was (q-1)x too large. See the
  round-38 Cauchy-lattice addendum.] The counting instruments keep failing toward EXISTENCE
  through T = 4 (the pilot's own registered attempt to discount
  the +62.5-bit cell was refuted by its own arithmetic, ratio
  1.000000000000 at five fields).
- **SCOPE FENCES:** T = 4 bespoke has ZERO (SAT3) power (both
  records have T = 0 over mu_32; columns never merged); (SCRIT)
  is verified on the regenerable class (the f=g=0 exception
  hypothesis named); (OV4) fires on nothing currently believed;
  F1/(NEWCAP) still zero power; m >= 3 untouched ((PAR) is
  m=2-specific); no razor-scale claims. Round 36's published T=2
  vectors were NOT replayed (regenerated instead — declared).

## ROUND 37 CLOSE (2026-08-11): the four banks reconciled — the frontier hardens into named finite problems

**BANK 1 (r37_urand):** STATEMENT U REFUTED same-day; far-CA =
r+1 + Theta(n/rho) (constructive floor r+1+126 modulo
R-GENERICITY; bits unchanged); the coset-leader frame; FENCE-1;
U-sym closed (ceil(rho/2)); C(128,63) check done (dedup yes, cap
no). **BANK 2 (r37_mint_drafts):** the mint wave drafted 10/10
with passing verifiers; twelve discrepancies dispositioned (the
a* convention flagged for ruling; the covering-law generalization
adopted; D9 resolved — the gate formula was banked all along);
wiring queued (task #41). **BANK 3 (r37_share3_gap):** the m=4
one-coincidence gap DERIVED (prescribable budget 8 vs demand 11,
the Segre-surface count; two-round ceiling explained); the
constant-norm census EXHAUSTIVE (empty at 577 AND 641; the ~q^-7
/ ~690 figures withdrawn; five-field window); **THE SIDE DOOR IS
LEGAL (coordinator check: O = 2 fits (SAT2)/(SAT4) exactly — 10
merges suffice, which round 36 ACHIEVED)**. **BANK 4
(r37_third_solve):** the third exact solve does NOT exist
(structural: two slots on a length-4 sequence); (SCRIT), (CONIC)/
(SLOT), (OV4); T = 4 bespoke first-in-class; T = 2 over mu_32
(tie).

**THE RECONCILED FRONTIER — everything is now a NAMED FINITE
PROBLEM:** (1) **the m=4 SIDE DOOR** (build the degenerate-fibre
configuration from a 10-merge draw; per-side bookkeeping at the
three deficient points; if it survives — the full pipeline and an
m=4 witness candidate); (2) **R-URATE + R-GENERICITY** (two
self-contained rank/genericity lemmas that pin B_ca^far(k+2^34)
= r+1+126 unconditionally); (3) **the rank-deficient Cauchy
solve** (the re-posed third prescription; Pade-lattice machinery
banked in l1/xr); (4) **the determinantal 11-merge solve**
(Groebner-scale; a compute-request candidate); (5) **THE MINT
WIRING** (task #41, coordinator session, 10 packages + the
statement_u re-draft); (6) **the a* convention ruling** (gates
all F1/(NEWCAP) pricing). The counting instruments are dead as
verdict-carriers in BOTH lanes (five refutations across two
rounds); every live route is a construction or a finite algebra
question.

**AUDIT LEDGER (12th consecutive catching round):** Statement U
(mine, round 36) refuted; the round-36 narrowing, decay/threshold
figures, floor(rho/2) count, and "no predictive criterion" line
all corrected; my round-37 brief carried two wrong premises
(route-(b)... the share3 window/peak — both recorded); the
drafting pilot surfaced twelve discrepancies including the a*
convention. COMPLIANCE ROUND TALLY: banks 1, 2, 4 clean (the
resumed bank-4 pilot included); bank 3 ONE bare-python3 breach
(the same empty-heredoc tic as round 36 — a PROCESS failure);
ROUND-38 RULES: the pre-Bash checklist ("any command containing
python3 MUST match 'tools/ramguard (tiny|local) -- python3'";
no no-op interpreters, ever) goes in CONSTRAINTS and prompt;
results files append-or-version (held, and paid twice this
round); the imported-script audit (fired correctly, once).

**ROUND-38 ANCHORS (priority order):** (1) THE SIDE DOOR —
degenerate-fibre m=4 (the cheapest potentially-decisive item on
the board); (2) THE MINT WIRING (task #41, coordinator); (3)
R-URATE + R-GENERICITY; (4) the Cauchy-lattice solve attempt
(import the l1/xr machinery); (5) the a* ruling + F1 pricing;
(6) sporadic non-factoring sharing (the last untouched m=4
route); (7) the determinantal-solve compute request.

## Round-38 side-door addendum (2026-08-11, coordinator-audited): the ledger CLOSES but the door is BUDGET-NEUTRAL; DOOR B posed (deficit 2); the 9th-fibre completion fence; the pipeline gated at last

Pilot r38_side_door (round 38, bank 1; 7/7 ramguard clean — the
pre-Bash checklist held on its first outing; my brief's biv_core
warning CORRECTED by the pilot's own audit: biv_core.py has NO
module-level write (0 hits for open/write/flush, coordinator
re-verified) — the "w"-mode offender was share3_pencil.py; the
two are not to be conflated again).

- **THE LEDGER CLOSES — the side door is fully legal on paper.**
  Every axiom passes at O = 2: (SAT4) 3 <= 4, (SAT2) 2 <= 3,
  (SAT5) 61 >= 60 (margin 1 each); the (OUT-m) aggregate is
  3(m-2) = 6 <= (m-1)(1+O) = 9 (the deficient points are
  symmetric-difference points, charge m-2); the per-side cap, the
  (OV) pair multiplicity and the per-slope eps cap all hold AT
  EQUALITY. EXTENSION ADOPTED: (OUT-m)'s X = 0 corollary survives
  INSIDE deficiency even at O = 2 > m-3 (slopes disjoint from W
  have eps = 0), so s = 13 and n_2 = 10 are EXACT. CONDITIONAL:
  (SAT2)'s second clause (O <= sum c_gamma — Hankel-layer rank
  deficiency) is UNCHECKED at the W-layer; all legality is
  conditional on >= 2 units of M(gamma) rank deficiency.
- **THE DEMAND-MINIMALITY THEOREM (exhaustive):** within
  (SAT2)/(SAT4) at m = 4 the merge demand is >= 10; EXACTLY two
  placements attain 10 (DOOR A: one outer double-root fibre,
  slots 23; DOOR B: the middle fibre reserving ONE slope, slots
  24); 9 is unreachable (a second placement costs 6 > m).
- **BUT DOOR A IS BUDGET-NEUTRAL — the round's central result:**
  prescribing the tangency costs EXACTLY 2 dimensions (the
  available-direction variety w(t*) (x) span{v,v'} is a SURFACE,
  same dimension as Sigma_ij) — measured 2.000 in 1500/1500
  draws per field, obeying the round-37 cost table verbatim. The
  budget drops 8 -> 7 as the demand drops 11 -> 10: **deficit 3,
  INVARIANT** (four independent dimension counts all give the
  residual variety dim 4). Lesson banked: price a loophole in
  the same currency as the demand before calling it progress.
  Best legal: |slopes| = 14 at BOTH fields (the q=257 ceiling
  CORRECTED 15 -> 14 — the old 15 object is dead at completion);
  the first (SAT4)-legal Door-A object built (23 slots, 9
  merges, ONE short); 0 hits in 6600 draws.
- **DOOR B — POSED, UNDECIDED, AND BETTER (the new cheapest live
  item):** if a middle can carry TWO non-type-2 cubic roots, the
  demand is 10 with the OUTER structure unchanged at 24 slots —
  **deficit 2** — and the existing two-round stock of 14-slope
  objects become candidates. A bookkeeping question (the
  multiplicity of the middle's non-incident-root mechanism), not
  a search. Round-39 anchor #1.
- **THE 9TH-FIBRE COMPLETION FENCE (new):** the middle fibre's
  slope cubic must SPLIT over F_q with >= 2 roots off the outer
  slope set — 48.1/53.8% (q=193) and 75.5/82.0% (q=257) of
  structurally-legal objects CANNOT be completed to |W| = 27;
  heuristic P ~ 1-(5/6)^{F-8} matches shape and magnitude;
  stacks multiplicatively on the round-37 census (F = 9 at
  q = 257, 449 leaves ONE candidate middle). Two prior rounds
  never imposed it. Lesson: layers below the stuck one can be
  cheaper and more decisive.
- **THE PIPELINE IS GATED AT LAST:** the Door-A object ran W
  assembly (27 points), the 4/4 per-side split, the FIRST-EVER
  mu(x)-at-middles verification (and it BITES: exactly one
  middle-cubic root must be non-incident; on the object the
  mechanism FORCES mu = 24 — a falsifiable prediction for any
  full construction), and bank 2's deficiency-aware bivariate
  system (102 x 57 = 2a + Delta_W per the PROVED
  deficiency_clone node): rank 56 by biv_core AND by an
  independent solver, nullity 1, blockwise-nonzero kernel FOUND.
  **The (SHARE3-4) class SURVIVES the bivariate layer** (NOT a
  witness — the object has |Z| = 18 > T = 17; and the synthetic
  nullity-0 control excludes nothing, correctly read). The
  round-36/37 "nothing gated by bank 2" caveat is DISCHARGED.
- **SCOPE FENCES:** the invariance is a generic-position count
  (round-37 grading inherited); the demand theorem is
  conditional on the slot/reservation model; the fence rate is
  ensemble-relative; Door B undecided; layer A still unrun (5th
  round); the registered solve routes (kernel-of-Vandermonde,
  sequential scan) were NOT implemented — the determinantal solve
  remains the open route; (SAT2) c_gamma unchecked. COMPLIANCE:
  clean 7/7 (streak 1 under the checklist); the /dev/null
  stdout-discard judgment call RULED COMPLIANT by the
  coordinator (a discard is not a write in the rule's sense;
  codified henceforth).

## Round-38 Cauchy-lattice addendum (2026-08-11, coordinator-audited): T = 3 OVER mu_32 ACHIEVED — the scale-elimination algorithm; the two headline witnesses COORDINATOR-CERTIFIED e = m = 2

Pilot r38_cauchy_lattice (round 38, bank 2; 21/21 ramguard, the
pre-Bash checklist held — zero breaches). COORDINATOR
CERTIFICATION: the pilot honestly declined to claim e = m = 2
(its own registered rule, unmet — MISS 2); I certified BOTH
published witnesses from scratch with my round-35 apparatus
(solve the 36x32 for (y_0,y_1): nullity 1; generic rank 7;
single reduced rank-drop z=85/z=22 at rank 6; full rank at
infinity; degree-<=1 kernel 0 => e = 2 EXACTLY, both fields).
The T = 3 record is now CERTIFIED, not inherited.

- **THE ALGORITHM (the round's instrument):** the two scale
  ratios of the three-member prescription ELIMINATE EXACTLY —
  with G = (beta/gamma)g, H = (beta/alpha)f, the pointwise
  systems become linear and u = f+g is DETERMINED by
  (S_0, S_inf, S_1) alone as the 1-dim intersection of the
  kernels of two 2x5 HANKEL MOMENT MATRICES (m_j = sum
  P_inf(x)x^j/(P_1(x)P_0'(x)) etc.); the drop is then the single
  rank <= 2 condition **(TEST): u = c_1 G + c_2 H with
  c_1 c_2 != 0 and both parts of degree 4** — codimension
  (5-2)(3-2) = 3, reproducing the banked deficit from a route
  that never mentions a lattice; ~330 field ops per triple
  (57 us). THE DEGENERATE BRANCH MATTERS: G parallel H makes the
  raw rank test fire falsely, pair-dependently (3824 false vs 6
  true on one q=23 pair) — the corrected clause is mandatory
  (113/113 brute-force agreement; any reimplementation omitting
  c_1 c_2 != 0 reports ~400x too many hits). Sufficiency of the
  14 pointwise conditions PROVED constructive: (CONIC) makes L
  automatically polynomial, h and k follow — the inverse is a
  reconstruction, not a search, once the triple passes.
- **THE SWEEP AND THE RECORD:** one (S_0, S_inf) pair sweeps ALL
  C(32,7) = 3,365,856 subsets S_1 exhaustively in 192 s. Ten
  T = 3 witnesses: 9 at q=97 (11.97e6 triples; predicted 9.09 —
  ratio 0.99) and 1 at q=193 (37.54e6; predicted 3.62 — Poisson
  p ~ 0.12, honestly flagged; 6 of 16 pair-sweeps were partial
  at 78-80%, denominators printed). Every witness: (PAR)/(CONIC)
  identities exact, s = 0, the three member root sets exactly the
  prescribed subsets, (OV4) held 10/10, lattice first minimum 4
  with the remainder-degree window-skip {5..9} (the round-37
  characterization, confirmed 200/200 x2 + 120/120 constructed).
  ROUND-37 RATE CORRECTED: its P(T>=3 | T=2 object) was (q-1)x
  too large (their rate predicts 872/694 hits on the swept mass;
  observed 9/1); the 8.9e3x shortfall was the instrument's, and
  their own d4_results.txt:54 held the feasible count.
- **THE a* FORCING (adopted; the ruling's first dataset):** on
  EVERY s = 0 object with two supported slopes, (SCRIT) forces
  S_0 ^ S_inf = empty, so a* over supported pairs = 2rho = 14
  IDENTICALLY — round 36's single sample and round 37's 28+4
  objects all carry the forced value (regeneration adds
  nothing). On the ten T = 3 witnesses: per-pair {12:10, 13:10,
  14:10} exactly uniform and FORCED by the overlap combinatorics
  (a*(0,1) = 14 - |S_1 ^ S_0| etc.); per-object a* = 12 on 9/10,
  13 on one. THE PROJECTIVE RULING IS INERT ON SUPPORTED PAIRS
  (supported => 7 finite roots => no root at infinity; the two
  readings differ only at degree-drop slopes, never supported) —
  measured: exactly ONE all-slope pair moves per degree-drop
  pair. F1/(NEWCAP): still zero power (T = 3 vs the premise 9);
  the a* dataset is forced combinatorics, not family minima.
- **STATUS OF THE THIRD PRESCRIPTION: STILL SEARCH, NOW FINITE
  AND CHEAP** (912,673 triples = q^3 per hit at q=97; ~64 s).
  No solve exists (given a pair you cannot write down an
  admissible S_1); T = 4 over mu_32 needs ~q^3 pair-sweeps —
  out of enumeration reach; the rank-<=2 inverse is the named
  next question. An UNCLAIMED n=9 signal (hits concentrate at
  overlap sum >= 3, p ~ 0.034) is recorded as a candidate
  necessary condition to test at n ~ 15, nothing more.
- **SCOPE FENCES:** 4 + 12 pairs of ~1.6e12 — zero power for
  (SAT3)/emptiness/mu_32-in-general; the eight uncertified
  witnesses inherit class membership (the two published ones are
  coordinator-certified; the deg k = 3 witness q97-p0-w1 flagged
  for the wiring session); (TEST) verified both directions at
  q=23 only (forward-only at 97/193); no bespoke run this round
  (round 37's T_bespoke = 4 stands; columns never merged);
  (SAT2..5) inapplicable at T = 3. Compliance: one wall kill
  (sizing, results preserved by append mode — the rule paid a
  third time) and one self-caught IndexError; zero breaches.

## Round-38 URATE/genericity addendum (2026-08-11, coordinator-audited): the rank half PROVED; R-URATE refuted by the exchange law; R-USYM closed

Pilot r38_urate_genericity (round 38, bank 3; 5/5 ramguard, the
checklist held). Coordinator hand-checks: the line-pencil
decoupling (row (i,x) = the point (e_0(x),e_1(x)) on the line
X + gamma_i Y + lambda_i Z_{Y_i}(x) = 0; blocks interact only
through p_x); the per-point Vandermonde left-null argument
(d(x) <= 2 forces vanishing); the razor identity 126*rho = 2r
EXACTLY; the exchange law's derivative (1/rho - 1 < 0); the
degree-parity carrier completeness. All pass.

- **R-GENERICITY, RANK HALF PROVED:** rank M = j(rho+1) - L +
  rank Phi (L = sum max(d(x)-2, 0); Phi the explicit concurrency
  matrix with all-nonzero rows) — 0 violations in ~500 designs,
  16 rows, 2 domain types. COROLLARY (the clean sufficient
  condition): distinct gamma_i + every point of W in AT MOST TWO
  A_i => FULL RANK, lambda completely free. THE RAZOR DESIGN:
  j = 126 is EXACTLY the one-common-point exact double cover
  (126 rho = 2r on the nose); kernel dim 2 in closed form
  (lambda_i = -(u+gamma_i v)/Z_{Y_i}(x^*)) — reproducing round
  37's measured "kernel dim exactly 2". SIDE-CONDITIONS: 1 and 3
  PROVED (lambda_i != 0 fails on EXACTLY j of q+1 projective
  kernel points — 4/4 EXACT HITs; gamma_i off-fibre by the
  det = c_a c_b (gamma_a-gamma_b)^2 union bound); 2 relaxed
  (<= 125 collisions tolerable; the inside-block-pair residue
  named); 4 half-proved (Case |S u W| <= R by MDS; Case B open,
  zero-power). All four hold simultaneously on 99.87-99.95% of
  the projective kernel (EXACT counts, replacing 60/60 samples).
  **The +126 floor is now modulo TWO named residues, not four.**
- **R-URATE REFUTED — THE EXCHANGE LAW REPLACES IT:** a rank
  drop in Phi (the Z_{P_i}|_{A^*}-proportional mechanism) buys
  1/rho slopes per unit and costs ONE fibre slope
  (chi collapses on A^*): T <= (r+1) - delta +
  floor((2(r+1)-1+delta)/rho). At small rho the trade PROFITS:
  C3 (rho = 3) m=2 rank drop => j = 9 > cap 7 => **T = 19 >
  banked cap 18, FULL C(26,10) census, THREE fields, column-far,
  T_other = 0** (100% mechanism vs first moment 1.3e-4). BANKED
  CENSUS CORRECTED: the round-37 T = 17 at this cell was
  search-limited (j = 7 is reachable => T = 18; the anchor's own
  honest can't-tell is resolved: search-limited). At the razor
  delta = 0 is optimal (T_max - (r+1) = 125, 126, 125, 124 at
  m = 0..3) and 126 STANDS — but the cap is a theorem only
  within the shared-A^* normal form, and its safety margin is
  PIGEONHOLE (m_pig = 1.00e9 vs break-even m* = 1.72e10, margin
  17.17x) — not algebraic. Named breakers: an algebraic family
  with m > 1.7e10 (cosets EXCLUDED: the X^d - c^d identity
  forces m <= 2 — proved+measured), or a deficiency mechanism
  cheaper than one fibre slope per unit (unenumerated).
  TRANSPORT WARNING: any "c conditions per slope => <= 2(r+1)/c
  slopes" cap is FALSE in general — the joint rank of Phi is the
  correct object.
- **R-USYM CLOSED:** parity fusion <=> sigma^e, sigma^o linearly
  dependent <=> sigma = (X-x_0)P(X^2) (odd deg) or q(X^2) (even
  deg); at odd r only the first survives degree parity — THE
  CARRIER FAMILY IS EXHAUSTIVE. Excess 0 both ways over 31,824 +
  31,824 + 497,420 locators (2 shapes, 2 fields); counts match
  C(n/2,(r-1)/2)*(n-r+1) exactly. The round-36 carrier question
  is answered YES.
- **CROSS-REFERENCE OWED (recorded):** the engineering matrix is
  a CONCURRENCY problem — the banked f_concurrency_equiv node
  (F-lane, PROVED) is the same incidence type; one sentence at
  wiring stops the next re-derivation.
- **SCOPE FENCES:** the cap break is 3 fields ONE cell (C9's
  predicted break verified slope-by-slope but uncensused at
  C(36,14) = 5.6e9); the m >= 3 no-collision negative has NO
  power (counting predicts it); the rank-drop search covers the
  proportional normal form only; column-farness Case B and
  in-block chi-injectivity remain the +126's two residues; the
  m_pig margin is information-theoretic. Pilot self-catches: its
  own sharper cap (B-6/7/8) refuted by its first run; six of its
  own predictions broken and reported.

## Round-38 sporadic/determinantal addendum (2026-08-11, coordinator-audited): both remaining m=4 routes closed at reachable level; C38 posed; three banked figures corrected

Pilot r38_sporadic_det (round 38, bank 4; 9/9 ramguard clean —
ALL FOUR round-38 pilots clean under the checklist; the breach
era ends). Coordinator hand-checks: the deficit cancellation
(39 + 3t_D - 72 - (3t_D - delta - 13) = -20 + delta — the
t_D-dependence cancels exactly); the transitive-closure forcing
(component > deg Psi = 9 => Psi constant); the s >= 12 floor
(72 <= 6s); the forced-root degree correction (prescribed slopes
are automatic roots of downstream resultants). All pass.

- **SPORADIC (NON-FACTORING) SHARING: CLOSED BY DICHOTOMY, AND
  RE-PRICED 11 DEX WORSE.** Z (the coincidence scheme) is finite
  XOR contains a curve, and a curve forces Lüroth — NO
  correspondence case (a non-factoring symmetric (2,2) has
  transitive-closure components of mean size ~100 >> deg Psi =
  9, forcing constancy; the Bezoutian family has components of
  size EXACTLY 3, 60/60 both fields, and is a HYPERSURFACE in
  P^5 — Jacobian rank 5/6, 200/200). The sporadic cost ledger is
  FLAT: deficit = 20 - delta INDEPENDENT of the sharing pattern
  (0 mismatches over the whole band) — first moment 10^-15.3.
  **WITHDRAWN: the round-36 "< 1e-4" sporadic price** (optimistic
  by eleven orders; the "cheapest pattern" is a low-sharing
  re-labelling of already-searched classes). Priced-not-searched
  honestly declared (the joint system is a codim-33 determinantal
  question; sampling cannot see 10^-15).
- **THE DETERMINANTAL SOLVE WORKS — AND ANSWERS ROUND 37's
  UNRESOLVED TENSION: the dim-4 variety HAS F_q-points, and
  every reachable one is DEGENERATE.** 7-edge prescription
  (kernel dim 2 in 500,000/500,000) + iterated gcd on the four
  residual degree-<=6 resultants: 80 raw solutions in 700k
  draws, two fields, two arms (constant-norm vs random —
  statistically indistinguishable: the fence is GEOMETRIC), and
  **0 legal** — the kills are two NAMED degenerate components
  (identically-zero fibre cubic, 39; hypergraph-degree-8 slope —
  round 36's own artefact — 26). The hit rate scales q^-2.1
  (the codim-2 degenerate locus, not the codim-3 honest one).
  **ROUND-37 FREE-MERGE COUNT CORRECTED: 3 free merges occur at
  rate 1.19e-4 (80/674,393 states)** — its "never observed" was
  a 115-state sample artefact; its CONCLUSION stands (all 80
  illegal). Best legal |slopes| = 14 both fields both arms —
  **third round, third instrument, identical ceiling**.
  **CONJECTURE C38 (posed, with falsifiers):** the 11-merge
  variety has NO non-degenerate F_q-point at q = 193, 257 —
  equivalently the m=4 ceiling 14 is a property of V, not of
  instruments. Falsifiers: a verified 13-slope Psi; a full
  Groebner solve (compute-request candidate); a primary
  decomposition exhibiting a non-degenerate component; a
  degenerate-fibre (Door) route solution.
- **ROUND-36's R1.7 REPAIRED:** gcd(3,64) = 1 excludes
  multiplicative order-3 only; the complete statement is
  |Stab_PGL2(mu_64)| = 128 (dihedral 2-group, order histogram
  verified, zero order-3 elements) PLUS the exhaustive fact that
  no order-3 Möbius map carries more than 6 of the needed 8
  stable triples (all 83,328 candidates, two fields). The
  coincidence-curve + order-3-deck-map DEVICE is banked (the
  trigonal_subgroup_exclusion node + roadmap — the pilot's own
  load-bearing subtraction, verified); new = the transfer, the
  exhaustive finite version, and the stabiliser computation.
  ALSO: monomial-lattice mechanisms give 2-power multiplicities
  only (3 unreachable); the pattern-independent slope floor
  s >= 12 (the whole m=4 D-part lives in s in {12, 13}).
- **CROSS-BANK RECONCILIATION (coordinator):** C38's falsifier
  F4 and the pilot's thrice-asked (SAT4) question are ANSWERED
  BY THIS ROUND'S OWN BANK 1 (quarantine held — the pilots could
  not know): the door is LEGAL (O = 2 closes every axiom) but
  BUDGET-NEUTRAL, and DOOR B (deficit 2) is the surviving form
  of exactly this falsifier. The three-round ask is closed.
- **SCOPE FENCES:** C38 is a conjecture on a named-design 440k
  sample, NOT an exclusion; the deficit-20 count is a naive
  first moment of the class the campaign has repeatedly seen
  fail (F-R3 live: exhibit any sporadic family with deficit
  < 20); the order-3 exhaustion is at two fields; arm A is the
  complete constant-norm supply, not all pencils; nothing gated
  by bank 2's verifier this bank (bank 1 carries that flag this
  round); layer A still unrun. Pilot self-catches: the
  forced-root degree error (its registered rate 3-16x
  optimistic), the degeneracy-maximising design (11 of 12
  "solutions" manufactured, a full run burned), the wrong
  affine-chart guard corrected to the banked projective
  formulation.

## ROUND 38 CLOSE (2026-08-11): the four banks reconciled — the ceiling is intrinsic, the doors are B and the residues

**BANK 1 (r38_side_door):** the ledger CLOSES but the door is
BUDGET-NEUTRAL (tangency costs 2 = one merge; deficit invariant
at 3; demand-minimality: >= 10, two placements); **DOOR B posed
(deficit 2, existing objects as candidates)**; the 9th-fibre
completion fence (48-82% of legal objects non-completable); the
pipeline GATED at last (the Door-A object survives bank 2's
bivariate layer; first mu(x) verification — mu FORCED). **BANK 2
(r38_cauchy_lattice):** **T = 3 OVER mu_32 ACHIEVED** (ten
witnesses; the scale-elimination/(TEST) algorithm; 192-s
exhaustive pair-sweeps; the two published witnesses
COORDINATOR-CERTIFIED e = m = 2; the round-37 shortfall an
instrument artefact). **BANK 3 (r38_urate_genericity):**
R-GENERICITY's rank half PROVED (+126 now modulo TWO residues);
R-URATE REFUTED (the exchange law; T = 19 > cap at C3, three
fields; razor 126 stands normal-form-conditionally); R-USYM
CLOSED. **BANK 4 (r38_sporadic_det):** sporadic sharing closed
by dichotomy (re-priced 11 dex); the determinantal solve reaches
only degenerate points; C38 posed; R1.7 repaired.

**THE RECONCILED BOARD:**
1. **(BIV-CURVE) m = 4:** seven classes searched-negative; the
   14-ceiling is three-instrument-invariant and CONJECTURED
   INTRINSIC (C38). The live routes, in order: **DOOR B** (the
   bookkeeping decision — deficit 2 with the existing object
   stock); C38's Groebner falsifier (a compute-request
   candidate); the two- residue completion of the fences.
2. **The converged small-m question:** T = 3 over mu_32 achieved
   and certified; **T = 4 = the rank-<=2 inverse** (the named
   gate); the (SAT3) target T = 9 = the packing ceiling remains
   the far horizon with four instruments saying empty and
   constructions advancing one T per round.
3. **Far-CA:** the +126 floor modulo TWO residues (in-block
   chi-injectivity; column-far Case B); the cap
   normal-form-conditional with a pigeonhole margin; the razor
   count stable at r+1+126 = 2^39.977280 in bits.
4. **COMPLIANCE: 4/4 CLEAN — the pre-Bash checklist worked; the
   breach era (rounds 36-37) ends.** The results-file rules paid
   three more times; the imported-script audit corrected a
   coordinator brief error.

**AUDIT LEDGER (13th consecutive catching round):** the round-36
sporadic price (11 dex), the round-37 free-merge count, the
round-37 shortfall figures, the banked C3 census number
(T = 17 -> 18/19), R-URATE (a banked residual target refuted),
the q=257 ceiling (15 -> 14), round-36's R1.7, my own brief's
biv_core warning, and my round-37 a*-inertness expectation —
all corrected with sources. ROUND-39 ANCHORS: (1) DOOR B;
(2) the two +126 residues; (3) the rank-<=2 inverse; (4) C38's
Groebner falsifier (compute request); (5) THE MINT WIRING
(task #41 — now two rounds overdue, queue ~45 items);
(6) layer A on the Door-A object (six rounds unrun).

## Mint-wiring addendum (2026-08-11, coordinator session, task #41): the round-37 mint WIRED — ten background nodes, all pre-conditions discharged, three wiring-audit catches

The ten round-37 draft packages are wired as background nodes, each with
the full 11-file exemplar set including an independent verify_audit.py
second code path (every verifier and audit PASS from the wired location;
manifest refreshed; census UNCHANGED at 231 = 167/37/27 — all ten landed
off-orbit as predicted, no re-pin). The nodes:

- rate_half_type2_ledger_vacuous_by_sign_fence (PROVED)
- rate_half_far_ca_negation_closure_excess_fence (PROVED)
- rate_half_far_ca_hr_dictionary_common_support (PROVED; (PSTAR) POSED inside)
- rate_half_far_ca_crossing_offset_value_ledger (TARGET — the statement_u
  RE-DRAFT: U as refuted definition, r+1 + Theta(n/rho) pricing, the
  round-38 floor/cap state, the two residues; the recorded pre-condition)
- rate_half_l2_stratum_rational_parametrization (PROVED; (RES) split kept)
- rate_half_l2_stratum_nonempty_at_m_two (PROVED; D1 a*-PROJECTIVE ruling
  recorded as resolved)
- rate_half_layer_a_equivalence_and_geometry_counterexamples (PROVED;
  requires edge to the saturation fence; the (RIC3) wiring gap closed)
- rate_half_share3_luroth_template (CONJECTURE; round-37/38 updates carried
  — Door B, the 14-ceiling correction, the sporadic-price withdrawal)
- rate_half_bivcurve_out_m_identity_and_deg_m (CONJECTURE; **D11 APPLIED:
  (DEG-m)'s quantity is deg_Sh in all wired documents** — deg_H stays with
  the a1_core incidence-reconstruction node)
- rate_half_sat3_realizability_ledger_record (CONJECTURE; **D9 RESOLVED IN
  FULL: the gate formula from r35_rout_layer_a/REPORT.md D3.3 is printed on
  the node and its audit REPRODUCES both m=1 calibrations (+13.75 at q=17,
  -0.94 at q=97) to two decimals**)

PRE-CONDITIONS DISCHARGED: the statement_u re-draft; deg_Sh; the gate
formula; the (RIC3) cross-citations (both sides); and the SUBTRACTION
against the unread Codex-cycle window (L3967-4269 at draft pins) — that
window is entirely the a1 quadratic-gap-four split-biform lane (cycles
146-157), ZERO overlap with any package.

THREE WIRING-AUDIT CATCHES (the audits earned their keep before wiring
completed):
1. **(DICT) SCOPE-CORRECTED (marker applied above):** h_r = rho + d holds
   for d <= rho ONLY — the stacked matrix has 2rho rows, so polynomial
   ratios of degree d > rho saturate at 2rho (exhibits: rho=2 d=3 q=601
   gives h_r = 4; rho=3 d=4 q=1013 gives 6). All 210 banked rows in scope.
2. **The rho >= 3 negation-closure kill is GENERIC in q, not
   field-uniform:** the audit found the accidental covering solution at H4
   over q = 1009 (A = {6,9,11,12,13}, slope 291) at the predicted ~165/q
   rate; banked zero-counts live at q in {65537, 999983}. Recorded on the
   fence node's certificate; the razor kill (surplus 2^33 - 1) untouched.
3. **The banked six-decimal log2 figure is the ROUNDING, not the floor:**
   the float-free digit extractor pins log2(r+1) = 39.9772799..., so
   floor(10^6 log2) = 39977279; the banked 39.977280 is round-half-up.
   Both r+1 and r+1+126 agree to six decimals (in bits nothing moves).

Also banked by the audits: the first local replay of the m = 4 fence cell
(108 x 80, nullity 8 = 2m, fresh code, q = 193), a symbolic proof of
(DET)+(SYZ) over Z (characteristic-free), and a fresh-field (q = 577)
constant-norm line with 30 split members. Schema note: node-level POSED /
HEURISTIC map to the DAG bucket CONJECTURE (leaf rule enforced — ingredient
links carried textually). Graph: 2325 nodes / 6855 edges; full verify
chain PASS.

## Upstream-sweep addendum (2026-08-12, coordinator session, task #42)

Sweep of upstream PRs `#1153`-`#1163` (all scottdhughes; upstream `main`
unchanged since 2026-07-29; no maintainer comments on our six open PRs).

- **`#1160` (2w near-rational repair)**: already harvested by worker
  cycle 119 at `45b01e4e0`
  (`v13_2_near_rational_supportwise_two_anchor_payment` PROVED + the
  strengthened REFUTED sibling). Coordinator audit added this session:
  proof line-verified; independent second code path
  (`verify_audit.py`) with an EXHAUSTIVE `mu_16` badness census over
  all `C(16,10)=8008` supports (bad set exactly `{3,5}`), a
  fresh-field `F_29` falsifier replay, and the deployed charges
  (`2w = 134944` KoalaBear / `134896` Mersenne-31). The upstream
  packet read our DAG at `3edb8b31` (pre-repair) — its "strictly
  stronger" claim at the `GF(17)` seam is true of that head only.
- **`#1163` (common-core shortening staircase)**: NEW import node
  `rate_half_kb_common_core_shortening_adapter_staircase_import`
  (PROVED): the typed reversible cancellation adapter
  `(n,k,m) -> (n-c,k-c,m-c)` with two-directional noncontainment
  transport, plus four exact walls at the official row — the degree-18
  interface dies exactly at `c = 4131` (`32m - 17n = 61952 > 15c`),
  fixed-core cells fit only `s <= 2`, the direction-separated boundary
  is `J_13 < B_* < J_14`, and Jo's shortening transfer is blocked by an
  exact 3765-bit multiplier that telescopes. Both wired verifiers PASS;
  the audit path replays the adapter on a from-scratch `F_17` record
  (all 10 witness subsets, both rows). Route-cut RECORD: no
  chronology-correct whole-line selector; zero ledger movement.
- **External replay confirmations banked**: `#1153` (cell-5 `xi=3`
  six representatives, zero witnesses) and `#1157` (raw
  `433-1b -> O0a`, 25,200 signed systems, zero survivors) match our
  banked exclusions exactly; recorded on the two aggregate nodes'
  source evidence and as PARTIAL fulfilment on the
  `rate_half_kb_m2_r4_k3_independent_review` TARGET (which stays
  TARGET).
- **`#1154`/`#1155`** were reconciled by the worker on 2026-08-10 (our
  105-label cell-11 closure is strictly stronger; the guard
  non-transplant warning kept as provenance). **`#1158`/`#1159`**
  (carrier-fold cut; `d1 = 67473` dimension shift + `SEM-QBC`) are
  recorded on the K3 review node addendum; zero ledger movement each.

All changes off-orbit; census re-pin only if the compile says otherwise.

## Post-near error-rank ledger addendum (2026-08-13 evening, coordinator, task #45)

The first grand-challenge row's post-near stratification now has a
sourced ledger, banked node by node. All figures at the official
KoalaBear row, `B_* = 274980728111395087`; every payment lives in the
POST-NEAR STRATIFIED THEOREM, not the active-v4 first-match ledger
(each packet records zero v4 movement).

- **Near stratum: PAID**, `2w = 134944`
  (`v13_2_near_rational_supportwise_two_anchor_payment`, from `#1160`).
- **Error ranks <= 9: PAID**
  (`rate_half_mca_support_local_transversality_compiler`, the `#1166`
  theta-margin repair harvested after the `#1165`/Scott-`GF(257)`
  double refutation of the affine-span compiler).
- **Error rank 10: PAID, twice independently** — cycle 232
  (`rate_half_mca_rank10_margin_interleaving_split_payment`, 06:40
  UTC) and Scott's `#1167` (18:44 UTC): identical formula, optimum
  `T = 667`, total `61871313426765543`, slack `213109414684629544`
  (sum exactly `B_*`); `#1167` adds a `GF(11)` sharpness star.
- **Error rank 11: UNPAID — this is the frontier.** NEW evidence node
  `rate_half_mca_rank11_pair_core_route_cut_import` (from `#1168`,
  wall independently reproduced: `L(19737) = 808527428378681053`
  exact): the complete declared pair/core certificate class bottoms
  out at `813929118931913384`, over `B_*` by factor `> 2.9`; every
  over-budget rank-11 line forces a `delta <= 4` pair owning
  `>= 200632` slopes. Pre-registered escape: cross-pair same-line
  coupling, or a chronology-correct owner for dense parallel
  pair-cores.
- **Ranks >= 12**: behind the rank-11 wall (`#1166` exception ceilings
  `12, 387, 12049` at ranks 10-12 in the gauge frame; rank `>= 13`
  residual).
- **Full-lift support walls** (compatible branch, Codex waves 60-61 +
  the `#1164`/`#1165` thread): KoalaBear `e <= 96150`, Mersenne-31
  `e <= 130198` (recursive line-peeling; `e = 130199` is the method
  wall).

Queued imports: `#1164`'s empty-global-core content (all-LineRay
rank-three gate, degree-31/order-32 coherence fence, correction-ray
identity/cap) — bankable at printed scope per cycle 217, not yet
harvested. Consequence for THIS node: locating the crossing at the
official row now reduces, within the post-near stratification, to the
rank-11 coupling question plus the strata behind it.
