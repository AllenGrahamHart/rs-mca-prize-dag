# PREREG — rh_bivariate_system (round 33)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/rh_fr_algebraic/REPORT.md` (round 32 —
   D2.4's bivariate paragraph)
2. `background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md`

## Mandate

THE OVERDETERMINED REALIZABILITY SYSTEM — round 32's unexploited
instrument. Under (SAT1)-(SAT4) with T = rho+2 at a = w* = a*, the
banked saturation rigidity forces every coordinate of the bivariate
Psi(Z) to factor as P_x(Z) = lambda_x * prod_{gamma in A_x}(Z - gamma)
* (Z - mu(x)) for x in W (A_x = the slopes through x, |A_x| = d_x;
mu(x) = the fibre slope) — (m+2)(4m+1) linear conditions on the
a = 7m-1 unknowns lambda_x: OVERDETERMINED BY A FACTOR ~O(m), and
nobody has computed its rank. YOUR JOB: exploit it. If the system's
rank exceeds a - 1 generically (projective lambda), the failure
configuration is KILLED outright; if consistency forces relations
on the incidence data (A_x, mu), those relations are new axioms
beyond the incidence fence — potentially the a/4 cap or the T-cap.

## Deliverables

**D1 — THE SYSTEM, DERIVED CLEANLY.** From the banked rigidity
(quote its exact statement + hypotheses file:line — note its
saturated-point scope >= 15N/16 and carry the unsaturated-point
exception honestly): write the linear system on (lambda_x)
explicitly. What are the equations indexed by? (The pilot text
says (m+2)(4m+1) conditions — re-derive that count; if it differs,
that is a finding.)

**D2 — RANK AND CONSISTENCY AT SMALL SCALE.** At m = 2, 3, 4 (two
fields each): build the system for (a) the K_7-star incidence
system (round 32's residual-(i) fence — does the bivariate layer
kill what incidence admits?), (b) the round-31 wave-57 fence's
m = 64 system restricted/scaled if feasible, (c) random admissible
incidence data. Compute exact ranks. THE DECISIVE QUESTION: does
the rank generically exceed the unknowns (=> the incidence-feasible
systems are algebraically infeasible)?

**D3 — THE CONSISTENCY RELATIONS.** Where the system IS consistent:
extract the relations on (A_x, mu) that consistency forces (kernel
dimensions, minor vanishing). Are they equivalent to / stronger
than the a/4 cap? POSE the resulting theorem with falsifiers.

**D4 — VERDICT.** The failure configuration killed / constrained /
untouched, with the exact algebra that remains. Cross-pilot note:
this instrument and the psi_gamma degree count are two views of one
layer — flag convergences for the coordinator, do NOT read the
sibling dir. Misses first.

## Blind priors to register

P(the condition count re-derives exactly), P(generic rank kills the
failure configuration), P(consistency relations imply X <= a/4),
expected rank deficit at m=2.
