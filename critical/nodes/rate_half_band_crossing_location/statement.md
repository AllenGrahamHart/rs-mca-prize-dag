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
stratum), R-MOVING (the 2-generated-truncation budget — one
generator is FORCED FIXED by multiplicity arithmetic, column-
farness forbids it D-split; bounding the other's slopes is the
open problem), R-KER (the >= r+1-2rho ~ 2^40-dim common kernel
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
