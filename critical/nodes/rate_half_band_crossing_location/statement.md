# BAND CHILD 2 (RH-AC): locate the adjacent crossing at the razor rows

- **status:** TARGET
- **parent:** `rate_half_band_closure` (req, gate all)
- **created:** 2026-08-09, the user-directed band decomposition
  (notes/band_decomposition_plan_20260809.md); pose adopted from the
  round-27 (RH-AC) draft with the decomposition ratification

## Statement (RH-AC, the pose of record; quantifier WIDENED 2026-08-10)

At every admissible row with n = 2^41, k = 2^40, **q prime,
q = 1 mod n, 2^167 < q < 2^256** — the entire undetermined range;
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
