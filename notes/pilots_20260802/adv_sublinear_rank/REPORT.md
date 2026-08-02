# Pilot report: adversarial attack on the sublinear-rank class (Opus 5, 2026-08-02)

Coordinator note: subagent's report, persisted by Fable (condensed;
full detail in the checkpoints). Audit: FABLE_AUDIT.md.

## VERDICT: K2 FIRES (re-pricing). K1 does not fire. K3 fails — the sunflower is NOT extremal.

**The structural correction (headline):** the banked cost theorem
charges per DATUM; it should charge per RAY. Core rows are IMPLIED by
ray rows (T2 + L1: the difference of two ray rows over a shared core
yields (0,c) hence (c,0)), so rank(family) = dim Sum G_{z_a}(C_{S_a})
<= V.h (h per RAY), and M <= C(V,2) (a datum IS a pair of rays). The
sunflower is the CYCLE (V rays, M = V, cost h); the extremal
configuration is the COMPLETE GRAPH K_V (V rays, M = C(V,2), cost
2h/(V-1)). Verified exactly (stage 6, 37 checks).

**The K_V "dual sunflower":** data at the C(V,2) intersection points
of V lines in general position in the (alpha,beta)-plane, one top-up
block per LINE (not per edge). The banked builder excluded this by
fiat (families.py:135 forbids repeated forced slopes = three collinear
points). 13 fixtures, 104/104, EVERY one admissible under the banked
occlib gates. Rank = V.h exactly in all 13; cost/datum -> 2(d+1),
independent of h (3.667 at h=11 vs sunflower h=11 — a 3.0x
improvement). Multi-cluster additivity 20/20.

**REFUTED (banked claims):** "cheapest admissible family = the
sunflower at exactly h; nothing below h"; SHARP-OCC's strong law
N_d <= floor((R+1)/(h-d)) (21 vs 4 = 5.25x violation, admissible);
the per-datum reading of the design ceiling — the banked 191/223/479
are the RAY counts; datum counts are their binomials.

**Exact re-pricing (48 checks, 2 deliberate negatives):** prize rows
V* = 192/224/480 -> N_1 = 18,336/24,976/114,960 (x95.5/x111.5/x239.5
over the old law); point budget binds; cost/datum drops h ~ 8.6e9 ->
~9.0e7. **SURVIVING: the ratified 0.68n^2 (margin >= 2.9e19); the
ledger column (<= 6.8e-20 n^3 vs 13n^3); SHARP-OCC's weak form
N_d <= n/2 at all six rows.** RowC 1/16 (h=3) degenerate: K_3 =
triangle = sunflower (the two deliberate FAILs).

**Failed adversaries (why K1 does not fire):** SPREAD-V
(combinatorially perfect to V=22/n=115, algebraically DEAD — rank
collapses, ray supports overshoot A, all pairs coincide); ray cliques
far above the K_V cap saturate rank at exactly 2m (total collapse);
growth-under-independence blocked in 14/14 fixtures at the cap
(slack V-2 every time). Empirical RAYCAP = (h+1)/(d+1)+1 (not proved;
does not bind at the prize rows — hence C(192,2), not larger).

**The induction — exact stopping point:** relations of support <= 2
PROVED zero (distinct slopes transverse); support 3 PROVED zero (the
k-packing kills the triple intersection — where the gate does real
work); **support 4 STOPS** (C_{S_3 ^ (S_1 u S_2)} has dim >= 2d+1 > 0;
support-4 relations occur in unconstrained random systems, absent in
every K_V fixture). **The residual named class RESTATES to: "an
admissible pairwise-intersecting ray system carrying a support-4
relation"** — four supports, two scalar equations.

**Why the restated gap is cheaper:** the sufficient per-ray floor is
rho >= 1.29-1.61 at the six rows — **a per-ray charge of 2 suffices
everywhere**; the proved per-ray charge is h (margin ~6e9 at prize
rows); and unlike the per-datum floor this survives arbitrary
ray-sharing.

**Caveats:** toy scale (gates to n=44); prize figures = the verified
builder's exact budget formulas at official parameters; RAYCAP
empirical; the upper bound N_d <= C(V,2) is conditional on ray
independence (= the support-4 gap); group-theoretic amplification
outside the P3 strip NOT attempted (open lane). Tally: 189 checks +
2 deliberate negatives (+ the hypothesis-test stages whose FAILs are
findings); files stage1-7 + spread + arith + advlib + checkpoints.
