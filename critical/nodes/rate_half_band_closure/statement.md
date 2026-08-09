# rate_half_band_closure

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/flip_packets/rate_half_coverage_gap.md']

## Statement

Cover the 2,978,147-radius band at prize-max rate 1/2 (M_max = 2^33 vs sigma* = 8,592,912,738) by a new mechanism (quotient windows and integrality both fall short) — or the rate-1/2 determination lands bracket-grade there. Rates 1/4, 1/8, 1/16 need nothing (clean by margins < -121). THE rate-1/2 battlefield node.

## Attack surface

a third mechanism for the band: extended quotient scales, averaged conversion at giant M, or the B2b-style balance analysis

## Falsifier

a band radius provably uncoverable by any priced mechanism

## [LIST-SIDE RETIREMENT + MCA/CA RE-SCOPE (wave-8 audited, 2026-07-16)]

The GRAND-LIST-DECODING half of this obligation is RETIRED BY THEOREM:
`rate_half_cyclic_rotated_prefix_floor` (PROVED, imported; + background
`rate_half_fixed_tail_prefix_floor`) proves the entire residual band
2^33 < sigma <= sigma* list-unsafe at sigma* — the trigger count
> q/2^128 is exactly the prize's |Lambda(C^{==m})| <= 2^-128 |F| object
— for ordinary + every constant common-support arity, every admissible
q < 2^256 (margin 75.0796 bits at q=2^256; cap boundary 256.0366 > 256;
agreement = k+sigma* exact). With the banked safe side, the rate-1/2
LIST crossing is DETERMINED; list_adjacency_closing consumes the PROVED
node directly. REMAINING for this red: the support-wise MCA/CA crossing
only (trigger ~ q/k). GUARD (verbatim, audited): any MCA-side argument
must not reuse the list threshold q/2^128 as an MCA surrogate — the two
triggers are different objects (separation measured:
notes/rate_half_trigger_separation_modal.py).

## [CORRECTION to the wave-8 addendum above (2026-07-17, w9-C2 — our
## own overclaim, caught by the wave-9 audit via v4's scope audit)]

The sentence "With the banked safe side, the rate-1/2 LIST crossing is
DETERMINED" is WITHDRAWN. The "banked safe side above sigma*" was
planning prose, not an in-repo theorem (the Paper D pincer stops at
half distance; r2_clean_rates excludes rate 1/2), and the s = c-1
instantiation of the cyclic floor proves list-unsafety THROUGH
sigma_0 = 8,594,128,895 > sigma*. Corrected state: the LIST UNSAFE
side is proved through sigma_0 (the cyclic floor node, strengthened);
the LIST SAFE side is OPEN (field-dependent); the crossing is NOT
determined. The retirement claim narrows accordingly: what is retired
is the unsafety obligation on the band, not the crossing location.
This node's own open content remains the MCA/CA half — now re-posed by
the audited v4 work as (RH-ADJ): find field-dependent a_RH(q) >=
k + 8,594,128,896 with B_mca(a_RH) <= floor(q/2^128) < B_mca(a_RH - 1).

## FIXED-CROSSING REFUTATION + FIELD-DEPENDENT RE-POSE (wave-9 audited, 2026-07-17; pin statement body — master text above preserved per #104)


- **status:** TARGET
- **closure:** proof
- **current object:** rowwise support-wise MCA adjacent certificate
- **refs (legacy repo):** `experimental/notes/roadmaps/flip_packets/rate_half_coverage_gap.md`

## Statement

Let

```text
n=2^41,       k=2^40,       C=RS[F,D,k],
2^128<q=|F|<2^256,          n divides q-1,
B*(q)=floor(q/2^128),
```

where `D` is a multiplicative coset of order `n`. Produce an explicit
row-computable agreement `a_RH(q)` and prove the exact adjacent certificate

```text
B_mca(a_RH(q)) <= B*(q) < B_mca(a_RH(q)-1).              (RH-ADJ)
```

Here `B_mca(a)` is the maximum number of finite slopes carrying a failed
support-wise MCA witness with agreement at least `a`. Equivalently,
`B_mca(a)/q=epsilon_mca(C,1-a/n)` under the closed finite-slope convention.
The range `q<2^128` is the already-settled degenerate regime with grand
threshold zero; equality `q=2^128` cannot admit this order-`2^41`
multiplicative domain.

## Proved lower bracket and refutation

Put

```text
c=2^22,       d=2048,
sigma_0=dc+c-1=8,594,128,895.
```

The strengthened proved node `rate_half_cyclic_simple_pole_mca_floor` gives

```text
B_mca(k+sigma_0)>B*(q)                                    (RH-LOW)
```

for every field in scope. Consequently every valid adjacent certificate
must satisfy

```text
a_RH(q) >= k+sigma_0+1.                                  (RH-BRACKET)
```

This refutes the former fixed claim at

```text
k+8,592,912,738+1 <= k+sigma_0.
```

Thus `sigma*=8,592,912,738` is not the rate-half crossing, and the old
`(RH-SAFE)` statement must not be consumed downstream. The conjectural
corridor map that printed this point is also not an optimality certificate
for rate `1/2`.

## Exact safe-side reduction

For any proposed agreement `a`, the proved sparsification identity in
`rate_half_mca_sparse_layer_reduction` writes

```text
B_mca(a)=max(B_ca^far(a), S_sparse(a)).                   (RH-SPLIT)
```

Therefore the safe half of `(RH-ADJ)` is exactly the conjunction

```text
B_ca^far(a_RH(q)) <= B*(q),
S_sparse(a_RH(q)) <= B*(q).
```

The first term is the plain correlated-agreement upper problem for
column-far pairs. The second is the budget-restricted sparse mutual layer.
Neither is supplied by the deep or half-distance pincer at this
near-capacity radius.

The proved `rate_half_sparse_pinning_rigidity` theorem further reduces the
sparse term. At `a=k+tau`, every non-tangent bad slope requires support
`e>=tau+1`, a nonzero ambiguity polynomial with cofactor degree at most
`e-tau-1`, and at least `A-e+tau+1+u` active matches consistent with one
slope. For `q>=2^168`, all tangent slopes already fit `B*(q)`, so only this
coupled non-tangent system remains on the sparse side.

## Attack surface

Locate a candidate at or above `(RH-BRACKET)`, then prove both upper bounds in
`(RH-SPLIT)` and an adjacent lower witness. A complete first-match/profile
ledger may prove both upper terms; a stronger explicit lower family may move
the bracket farther before the upper work begins.

## Falsifier

For any proposed formula `A(q)`, either an admissible row with
`B_mca(A(q))>B*(q)` or failure to prove
`B_mca(A(q)-1)>B*(q)` falsifies that adjacent formula. The previously proposed
constant formula is already falsified by `(RH-LOW)`.

## QUADRATIC EXACT RANGE + SAFE BRACKETS + HANKEL SUITE + OPTIMIZED FLOOR (wave-10 audited, 2026-07-18 — the reconciled v4+v5 state; all previous poses preserved above)

**THE CROSSING IS DETERMINED for every admissible 2^128 < q < 2^167:** a_RH(q) = n - floor(q/2^128) + 1, unconditional. Composition: the quadratic staircase equality (mca_quadratic_prize_rows) covers B = floor(q/2^128) <= B_Q = 389,500,552,609 (~2^166.503); the (RQ4) equivalence reduces B_Q < B <= 2^39+1 to the single far-CA bound; the Hankel suite's unconditional layer B_ca^far(n-r) <= r+1 (every r <= 2^39-2) supplies it; the universal coordinate-tangent family (mca_full_agreement_endpoint, in-repo since wave-6) supplies the adjacent unsafe witness. The wave-9 PR4 q >= 2^168 caveat is bypassed below 2^167.

**EXACT RESIDUAL of (RH-ADJ):** budgets 2^39 (strict A=3, s=0, e in [2^37, floor((2^39-1)/3)]) and 2^39+1 (A=3 e >= 2^37+1, plus A=1 rows) — recorded per w10-H1 as the explicit open-budget set {2^39, 2^39+1}; beyond 2^167, brackets only: a_RH in [k+2^34, 3n/4] for q >= 2^169, [k+2^34, n] otherwise. The k+2^34 floor (v5's optimized re-instantiation, c=2^33, d=1, field-independent list 2^242.65) SUPERSEDES the former k+8,594,128,896 bracket lines and sigma_0 as the forward-facing constant (sigma_0 retained as history — forced-corrections authority, proved constant improvement).

**Hankel suite note (w10-H5):** the seven strict-endpoint nodes rigidify the residual profile at strict budget e=m only — they are NOT q-axis coverage progress. The five wave-9 guidance lines and the three pre-suite 'Remaining proof' lines are superseded, not deleted (w10-H2).

**LIST side (v5, audited):** the safe side is now OWNED by the TARGET pose rate_half_list_adjacent_crossing (the w9-C3 repair vehicle); the exact-integer Johnson anchor is PROVED; the list crossing is DETERMINED for budgets B* in {1,2} at a_L = 3n/4; the proved unsafe reach doubles to excess 2^34-1.

## Round-27 FORCED CORRECTION (2026-08-09, coordinator-applied on replay: pincer_formalization — FLOOR v2's OWN FALSIFIER FIRED; D0 = BROKEN)

**The FLOOR v2 pose is SUPERSEDED BY ITS OWN PRE-REGISTERED
FALSIFIER, which fires in the structural-surplus direction BY
THEOREM.** The round-27 foundation audit (deliverable order binding:
audit before formalization) returned BROKEN on the "safe side above
sigma*" machinery, with the failure verified by the coordinator from
this node's own text:

**(1) sigma* = 8,592,912,738 is NOT a pincer constant.** It is
t*(255.9) - 1, the RANDOM-WORD first-moment corridor edge computed
in xr_radius_arithmetic/proof.md §2 (mean over received words). No
safe-side theorem at or near it exists (exhaustive own-repo sweep:
the only rate-half MCA safe upper bounds are RQ1/RQ2 (q < 2^166.5),
HD1 (a = 3n/4), and the lossless sparse-layer identity). The
"generic pincer" provenance line was a mis-attribution; the genuine
half-distance pincer safe point is HD1's excess 2^39 — 63.978x
above sigma*.

**(2) The claimed-safe point is strictly INSIDE the proved-unsafe
region — and this node's own statement has recorded that fact since
wave 9 without reconciling it:** sigma_0 = 8,594,128,895 > sigma*
is unsafe by the PROVED simple-pole floor (the wave-9 text above);
2^34 - 1 is unsafe by the wave-10 optimized floor (1.999x sigma*).
The type error: B_mca is a MAX over received words; the FM corridor
is a MEAN — the repo's own moment-ledger caveat ("the fixed-word
worst-case conversion remains with the KMS/globalness branch")
flagged exactly this.

**(3) The falsifier firing, quantified:** on the DETERMINED rows
(RQ1, 2^129 <= q < 2^166.503, 38 scales), the proved worst-word
crossing exceeds the random-word FM crossing by rho in
[53.77, 79.88] — sustained, one-directional, on the official row
shape, by theorem. At the razor rows it fires directly via (2).

**(4) Survivals +1..+4 are RE-CLASSIFIED as zero-power for this
claim:** every banked window-law/crossing-fidelity cell has
q < 2^128, hence B* = 0 (the degenerate regime), and every one
measures the random-word MEAN object — invisible to the
max-vs-mean gap. F3 of the successor pose pre-declares all further
q < 2^128 random-word count checks as zero-power (the guard that
would have prevented the mis-banking).

**(5) The "band (2^33, sigma*]" is the wrong band.** The proved
bracket at razor rows is sigma_RH in [2^34, 2^39] (width
532,575,944,704 — 178,828x wider), and sigma* < 2^34 lies outside
it entirely.

**(6) CATCH-24A: the "unformalized worst-word crossing" HAS BEEN
FORMALIZED IN THIS NODE SINCE WAVE 9** — it is (RH-ADJ)/a_RH with
the (RH-SPLIT) decomposition and the RQ1 exact range. The WP5 flag
(2026-07-10) was true when written and went stale on 2026-07-17;
the wave-9 import plan's supersession banners for
P6_RATEHALF_SIBLING.md and pro_brief_razor.md NEVER LANDED (custody
miss) — they are landed NOW, with this correction.

**SUCCESSOR POSE (RH-AC), DRAFT — recorded, NOT adopted (the pose
of record awaits the round-27 bank + user view per the
decomposition plan):** at every admissible razor row, locate
a_RH(q); the binding term is S_sparse alone (B_ca^far is free at
razor rows since B* ~ 2^128 >> n, discharged by the Hankel layer);
open content = min{a : S_sparse(a) <= floor(q/2^128)} within the
PROVED bracket [k+2^34, 3n/4]. Named endpoints (RH-AC-lo) k+2^34
tight vs (RH-AC-hi) 3n/4 tight — NO discriminating evidence held;
the determined-region rho extrapolation (~2^38.9, near -hi) is a
heuristic across a mechanism change, labelled as such. Falsifiers:
F1 push the quotient floor past 2^34-1 (high power, fires unsafe);
F2 exhibit S_sparse(k+2^34) > B* at one row (fires safe); F3 the
zero-power declaration above. Consumer bars (CATCH-24C):
adjacency_closing needs the LOCATED crossing (full RH-ADJ);
mca_safe needs ONLY the safe half — **FLAGGED UNVERIFIED LEAD: HD1
may already discharge mca_safe's rate-1/2 bar at razor rows
(q >= 2^169); needs a dedicated read of whether the consumer's
a_safe is free or pinned**; list_adjacency_closing no longer
consumes this node's MCA content (owner moved at wave 10).

Coordinator replays: d0d2.py + esc.py exact (rho window, the two
gap integers, 6/6 escape suite); HD1/sigma_0/mca_safe-bar/banner
absence all verified from primary text. Pilot self-corrections: 6,
disclosed (incl. a wrong registered constant landing inside its
window "by luck, not correctness" — reported as such; and the
lgamma re-implementation of the Modal-dependent verifiers, named
as a substitution). No status flip (the node stays TARGET; the
POSE changes). Source:
notes/pilots_20260809/pincer_formalization/ (REPORT.md,
FABLE_AUDIT.md).

## Round-27 addendum (2026-08-09, coordinator-applied on replay: cancellation_recon — the barrier mapped exactly; BLIND CONVERGENCE with the round-27 forced correction)

**Run under quarantine from the pincer_formalization pilot, this
recon independently derived three of the same conclusions** — the
live gap is sigma in [2^34, 2^39] (not the nominal band, which the
proved reach already covers entirely); a PROVED theorem exhibits a
structural surplus of EXACTLY 2.0000x over the random-word
first-moment line (CATCH-E: the proved reach 2^34-1 = 2 x
n/log2 q, the surplus being the +c from the maximal prefix); and
mca_safe consumes the upper half only. Blind convergence noted as
corroboration of the forced correction above.

**THE Z-FLOOR TRANSPORT SELF-SUBTRACTS (hard law 5, the pilot's
own registered 0.55 prediction):** Z-FLOOR's mechanism (mass by
pigeonhole + second-moment ceiling + Cauchy-Schwarz) IS the PROVED
rate_half_cyclic_simple_pole_mca_floor — coordinator-verified
verbatim at its proof.md:42-56. The transport exists, is banked,
and buys zero new reach.

**CATCH-B (live-number correction):** the campaign's quoted band
deficit ("x28.4, 4.73-4.83 bits, flat across all 2,978,146 band
cells", witness-hunt 2026-07-12, still quoted in this node's
statement blob) is the deficit of the fixed-tail N=128 d=0 rung —
whose reach only TIES the current proved 2^34-1. Closing it buys
ZERO. **The live deficit at the first reach-improving rung
(rotated N=128, d=1, reach 2^35-1) is 11.8737 bits (x3750).**
CATCH-C: the difference is exactly log2(128) + log2(65/63) = 7.045
bits, and the 7 is UNRECOVERABLE — the pigeonhole normalizer is
exactly tight (class-profile DP at the real rung parameters:
largest class = C(N-1,m)/N to 9 decimal places).

**THE NEXT-RUNG FLOOR IS DEAD TWICE OVER at the real parameters:**
(i) the 11.87-bit supply deficit with a provably tight normalizer;
(ii) the second registered repair route (sharpen the simple-pole
conversion) dies the OPPOSITE way — the conversion becomes
LOSSLESS as q grows (measured 8.006 -> 1.120 over the banked
9-point ladder; Cauchy-Schwarz tight at 1.00-1.25), so an
infinitely sharp conversion buys nothing at razor q.

**THE BARRIER, NAMED AND QUANTIFIED:** above sigma = n/log2 q the
AVERAGE ball occupancy falls below the budget, so no counting
argument can produce witnesses — only atypically-clustered
algebraic configurations can. Both in-repo LB mechanisms die at
the same line for different reasons: M1 (tangent construction,
payload <= 2^40 < B* for q >= 2^168) and M2 (counting, capped at
2 x n/log2 q by ball-volume exhaustion). Same barrier as WP7's
clean-rate instance — but the rate-1/2 shortfall is 11.87 bits vs
212 there: BY FAR the closest instance to closing. Sharpest
bracket of record: sigma_true in [2^34, 2^39] for q >= 2^169.

**Consumer-bar map sharpened (CATCH-24C, per-consumer):** ONLY
adjacency_closing has an open band lower-bound clause, and it is a
MOVING bar (sigma_LB must meet the safe side minus one — no fixed
lower bound discharges it alone). mca_safe: upper half only.
list_adjacency_closing: lower half ALREADY DISCHARGED by the
PROVED rate_half_cyclic_rotated_prefix_floor; its open piece is
the list safe side (owned elsewhere). **K5 AS MINTED IS
DISCHARGED-STALE:** its coverage interval (R(lq), sigma*] was
superseded 8 days after minting by the wave-10 optimized floor;
the live kernel need is (2^34 - 1, a_RH - k - 1].

Pilot record: 9 predictions HIT (incl. the exact 2.0000 ratio and
the self-subtraction), 1 MISS + 1 half-MISS (the repair route
died the opposite way from its framing — reported as such), 3
registered small-scale tests NOT RUN (superseded by exact
computation at the real parameters — a declared deviation,
strictly stronger, misses left unresolved and named). Coordinator
replays: all four scripts byte-identical; the simple-pole proof
mechanism verified verbatim. No status flip. Source:
notes/pilots_20260809/cancellation_recon/ (REPORT.md,
FABLE_AUDIT.md).

## Round-27 addendum (2026-08-09, coordinator-applied on replay: nonpoly_flank_census — the flank censused; THEOREM CAP scope-limited; the falsifier does NOT fire)

**The named residual hunt space is now parameterized, censused, and
NON-EMPTY — but the node's pre-registered falsifier does NOT fire.**
The first-moment law held EXACTLY in 58/58 exhaustive cells
(delta-independence proved: every term of the stratum total carries
q^{k-i}, so the FM model transfers to the flank with ZERO
correction), F_MAX <= B_pois in every exhaustive cell, and the
sporadic ladder is empty in every starved row to q ~ 2^40. What IS
new: **THEOREM CAP is scope-limited to slack 0.** Off that stratum
the exact maximum exceeds the plateau — char-0 (q-stable), two
independent fields, two scales: n=8 +0.737 bits (4 fields); n=16
delta=1 F_SUBSET = 46 vs plateau 35 (exact max over all 1.036e8
word classes, IDENTICAL at q=10177 and q=10193 —
coordinator-verified in both maxscan files), achieved F_LIST 39;
maximal slack (= ARBITRARY received words) 67 two-field. The
explicit maximizer is clean: the ANTIPODAL-PAIR LOCATOR
W = L_{{x,-x}}. The surplus is a max/supply phenomenon at 2 scales
— not the falsifier's 3-scale mean deviation.

**The flank, parameterized exactly:** every received word is a
polynomial; the escape class is POSITIVE SLACK delta = deg Y - a in
[1, n-1-a]; the planted-hybrid family is the SUPPORT SUB-CLASS, not
the whole class; giant slack saturates at the arbitrary-word set —
the banked census measured one stratum of a family whose top
stratum is the prize's own list-side object. **The useful reduction
(proved):** in complement coordinates the flank is the SAME width-t
window SHIFTED by delta ([delta+1, delta+t] vs [1, t]). Also
proved: the dedup law (subset counts = list counts x C(j,a),
tolerance 0); and the PRESCRIBED-SUM THEOREM P4 (h-subset sum
multiplicities peak at v=0 ONLY; exhaustive char-0 at N=8/16, exact
probes at N=32 q~2^40) — the prescribed-nonzero-sum escape
generalization is CLOSED at three scales.

**THE NAMED RESIDUAL (sharpened, honestly conflicted):** the
delta=1 mechanism's analytic model matches at n=8/16 then COLLAPSES
(2^-500 at prize scale — it cannot reach the 4.83-bit need), but
the maximal-slack surplus GREW over the two measured scales
(+0.74 -> +0.94/1.25 bits). Two points, both lower bounds,
different mechanisms: **the scaling of the arbitrary-word maximum
is UNDETERMINED.** The deciding computation is named: the exact
n=32, t=1 whole-word-space maxscan (C(32,15) = 5.7e8 per word —
Modal-class, out of stdlib reach).

**The 2^-5.2 price: verified and explained.** lg C(255,128) =
250.67284 (coordinator-recomputed); the banked 2^-5.2 and 2^-5.3
are THE SAME QUANTITY at the two ends of the razor slice (255.900
vs 256.000). The flank does not multiply the trial count (the
sporadic event depends on (q,N,h) only); the hatch sits 133.3 bits
from mattering; the banked R1c kill line stands. The 4.7286-4.8286
bit deficit vs C(127,64) = 2^123.1714 reproduced exactly
(coordinator-recomputed) — NOTE per the cancellation_recon
addendum above: that figure is the WITNESS-SUPPLY gap; the
LB-floor rung deficit is the separate 11.87-bit figure — two
different objects on this node, now both priced.

Pilot record: 6 registered predictions HIT (incl. the price within
0.002 bits), its OWN registered reduction REFUTED by its own
census (reported first; obstruction named exactly: the flank's
admissible set is a delta-dimensional affine subspace, not a
point); 5 self-corrections disclosed (incl. a subset-vs-list
near-miss and an invalid cross-field RNG comparison caught and
excluded). Coordinator replays: the 31-cell n=8 exhaustive census
BYTE-IDENTICAL; the price/deficit arithmetic re-derived; the
two-field argmax verified in both banked maxscan files. No status
flip. Source: notes/pilots_20260809/nonpoly_flank_census/
(REPORT.md, FABLE_AUDIT.md; data/ 12 result files).

## Round-27 addendum (2026-08-09, coordinator-applied on replay: staircase_extension — the residual diagnosed to the unit; the razor is a NEW THEOREM; the cyclotomic threat killed)

**The {2^39, 2^39+1} residual is NOT closed and is NOT a
proof-budget artifact: the counting layer is EXACTLY ONE SLOPE
short at its limit** (cap T <= 4e+1 = rho+2 vs target rho+1 at the
first live degree), and the m=1 fence (PROVED, explicit F_17
witness) says no incidence/core-freeness/split-fiber/Hankel
argument closes the endpoint uniformly. Sized exactly:
687,194,767,358 ~ 2^39.32 open (A,s,e) strata; per-stratum
deficits 1 / 4 / 3-4 slopes; at e=m every failure is forced onto
the sharp face h=0, T=rho+2.

**But the TRUTH-vs-PROOF question is closed on the officially
relevant axis:** at the exact scaled analogue of the strict
residual (N=16, complete line census), the violating configuration
exists at THE SMALLEST FIELD ONLY (q=17) and dies at every prime
field 97 <= q < 5000 — and rate_half_residual_prime_field_collapse
(PROVED) forces both residual budgets onto prime fields q > 2^167.
The staircase-shaped formula HOLDS at scale on the prime-field
axis. The residual is (evidence-grade) TRUE with the proof needing
the apolar origin the incidence family provably lacks.

**Boundary diagnosis per layer (D2):** staircase equality —
STRUCTURAL (proved counterexample at the first post-quadratic
radius); (RQ4) — STRUCTURAL, it IS the half-distance barrier
verbatim (r_sp = min(floor((n-k)/2), B*), PR5); far-CA Hankel —
method wall with a proved no-go for the whole incidence family
(the counting cap is ATTAINED by non-Hankel objects: 9 collinear
disjoint split cubics at N=28 with Hankel nullity 0 — exact
certificate, coordinator-replayed byte-identical). **Consequence:
the razor determination is a NEW THEOREM, not a computation** —
at razor rows B* ~ 2^128 >> n and a = n-B+1 is not even well
posed.

**THE CYCLOTOMIC THREAT — the one field-independent threat to
budget 2^39+1 — TESTED AND KILLED at every accessible analogue:**
the family Q = X^rho U^e - (c_0 U + c_1 V)^e saturates the design
cap whenever rho = e*r_0 with r_0 | N — and at the official A=1
profile rho = 2^39 DOES divide N = 2^41 with e inside the window.
Measured (coordinator-replayed byte-identical): every over-target
instance has Hankel nullity 0; the only realizable instances are
at or below target. Clean law: **realizable exactly when it does
not exceed the target.**

**D4 CROSS-LINK (new leverage):** the q >= 2^169 condition on the
bracket top a_RH <= 3n/4 is imposed by the far-CA term ALONE, and
the imposing term IS residual budget 2^39+1 itself. Closing it
extends the proved bracket top to ALL q > 2^167 — a 2-bit window,
materially larger than the residual's own 2^-38 q-axis payoff.
This re-prices the residual from "smallest open piece" to "the
gate on the bracket top."

Pilot record: 9/10 registered predictions HIT (P8's A=1 e in
[2,4] census NOT RUN — out of reach, only the cyclotomic
sub-family tested — disclosed); one COMPUTE-LAW BREACH disclosed
(a single un-ramguarded patch heredoc; 12/13 invocations
compliant); a RAM-cap hit handled by redesign; an out-of-domain
(ERC2) evaluation caught by absurdity and corrected. The pilot
read this statement's mid-session round-27 growth as primary text
(legitimate; sibling dirs never read). Coordinator replays:
d1_realizability + d1_cyclotomic byte-identical; escape anchors +
the 2^39.32 stratum count exact. No status flip. Source:
notes/pilots_20260809/staircase_extension/ (REPORT.md,
FABLE_AUDIT.md).
