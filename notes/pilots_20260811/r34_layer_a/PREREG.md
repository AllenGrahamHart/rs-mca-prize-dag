# PREREG — r34_layer_a (round 34)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/rh_psi_degree/REPORT.md` (round 33)
2. `notes/pilots_20260811/rh_bivariate_system/REPORT.md` (round 33)

## Mandate

THE CONVERGED TYPE-2 INSTRUMENT. Round 33's banks 1+2 converged
from opposite directions on the FULL-DOMAIN layer: one bivariate
Q(Z,x) of bidegree (rho, m) on all of D (deficit 12m^2 - 4m, ~3x
the W-layer), which killed bank 2's own m=2 exhibit. Bank 1 named
its statement form: **(NS-m)** — every type-2 h_gamma carries >= m
of its degree in irreducible factors of degree >= 2 — which IMPLIES
closure of residual (ii); and its geometric form: all a fibres of
H(Z,x) are totally split over F_q (the rigidity), so (NS-m) asks
whether the TRANSVERSE family (h_gamma, one per curve point) can
also split — a Wronskian/ramification question on a g^{m+1}_d on
P^1. THE REGRESSION TEST IS MANDATORY (round 33 bank 3): (SAT3) is
REALIZED at m = 1, so any (NS-m)-type theorem must either hold on
the m=1 witnesses or be m-dependent and fail there — CALIBRATE
FIRST. YOUR JOB: the layer-A attack on (NS-m).

## Deliverables

**D1 — THE m=1 CALIBRATION (first, mandatory).** On the 16 realized
m=1 configurations (banked in rh_sat3_realizability/): compute the
h_gamma family and measure (NS-m) directly (does every type-2
h_gamma at m=1 carry >= 1 of its degree non-split?). If VIOLATED,
(NS-m) as stated is FALSE and needs restatement (m-dependence or a
stratum hypothesis) — that changes everything downstream, so it
comes first. Also run layer A's rank system on a realized witness
(it MUST be consistent there — nullity >= 1; if not, the layer-A
builder is wrong: a built-in control).

**D2 — THE WRONSKIAN ATTACK.** The rigidity forces every fibre
P_x(Z) totally split; the Wronskian of the g^{m+1}_d counts total
ramification (2(d + (m+1)(g... on P^1: deg W = (m+2)(d - m-1) +
...) — derive the exact ramification budget and what total
fibre-splitness costs against it. Does the budget FORCE >= m
non-split degree in the transverse direction (= (NS-m))? This is
the round's theorem attempt. POSE with falsifiers what you cannot
prove; the m=1 calibration bounds what the theorem may claim.

**D3 — LAYER-A RANK AT SCALE.** Using bank 2's biv_core.py (banked,
copy first): the layer-A system's rank/nullity on (a) the m=1
witnesses (control: consistent), (b) bank 2's m=2 W-layer exhibit
(known: killed — reproduce), (c) structured m=2/m=3 candidates
from the (BIV-CURVE) fibre method. Where layer A kills, extract
WHICH equations bind (the consistency relations = candidate (NS-m)
mechanisms).

**D4 — VERDICT.** (NS-m) proved / restated / walled, with the m=1
regression status explicit. Misses first.

## Blind priors to register

P((NS-m) survives the m=1 calibration as stated), P(the Wronskian
budget yields the theorem this round), P(layer A consistent on all
16 m=1 witnesses).
