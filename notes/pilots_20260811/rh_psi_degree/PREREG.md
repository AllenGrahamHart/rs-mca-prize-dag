# PREREG — rh_psi_degree (round 33)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/rh_fr_algebraic/REPORT.md` (round 32 —
   D2.4 is your launch point)
2. `notes/pilots_20260810/apolar_origin/PREREG.md` (round 28 — the
   (C2)/K' machinery definitions)

## Mandate

THE 8/5 ON THE TYPE-2 FRONTIER. Round 32 proved FR-canonical
(X <= 4rho-2a*-... at a minimising pair union) and priced the
residual at 7/4 with the missing step exactly 8/5 at the argmax
a = (20m-2)/3: needed X <= a/4, proved min(a-(4m+2), 4rho-2a).
Round 32's D2.4 identified THE live instrument: psi_gamma =
z_gamma * Q_gamma|_W is a polynomial h_gamma of degree
<= a-(4m+2) in the shortened apolar MDS code K'|_W, whose roots in
W are exactly F_gamma u (S_gamma ^ W). (C2) is "a polynomial has at
most its degree many roots"; the needed statement is "h_gamma has
<= ~a/4 + n_gamma roots although its degree allows more". The mean
weight of psi_gamma over the T slopes is ~5.25m against the 5m-1
that the threshold needs — ~5% headroom; the max-vs-mean step here
is NOT self-defeating (unlike the spend count — round 32's MISS 2
explains why). Wave 58's cycle 49 converged on the same object from
the fence side ("control its aggregate near-minimum-weight fibers
using the common pencil"). YOUR JOB: the aggregate weight attack on
the psi_gamma family.

## Deliverables

**D1 — THE AGGREGATE IDENTITY.** The T polynomials h_gamma live in
one MDS code and are coupled by the common pencil (z_gamma =
c_0 + gamma c_1 — the family is a PENCIL of codewords twisted by
the Q_gamma). Derive the exact aggregate: sum over gamma of
wt(psi_gamma) (or of root counts in W) as a function of the
incidence data — is there a second moment / product identity the
pencil forces? (The saturation identity gives the mean; you need
the instrument that caps the MAX — a Chebyshev-type step inside an
MDS code, or the pencil's Wronskian/resultant.)

**D2 — THE SUBCLASS THEOREM.** Prove X <= a/4 + O(1) (or any
c < 1/3 coefficient) on the largest stratum you can reach —
minimum-weight slopes first (j = 0: kappa = 1/sigma'_{WuS} makes
h_gamma explicit). Exact scope + falsifier per result.

**D3 — SMALL-SCALE MEASUREMENT.** Measure the true max root count
of h_gamma in W at the round-31/32 census scales (copy the banked
decoder from rh_type2_stratum/d3_census.py or
rh_fr_algebraic/d3_frcensus.py). Compare against a/4, the (C2)
degree cap, and the mean. Pre-register expectations. CAVEAT
CARRIED: T = 3 in every reachable pencil — (SAT3) untestable here;
say so wherever it binds.

**D4 — VERDICT.** The 8/5 closed, narrowed, or walled — with the
exact surviving obstruction named. Misses first.

## Blind priors to register

P(the aggregate identity exists and is new), P(X <= a/4 provable on
j=0 this round), expected true max/mean ratio at m=3,4.
