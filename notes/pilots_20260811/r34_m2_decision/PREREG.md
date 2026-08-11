# PREREG — r34_m2_decision (round 34)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/rh_sat3_realizability/REPORT.md` (round 33)
2. `background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md`

## Mandate

THE DECISIVE EXPERIMENT (round 33's G2): settle whether (SAT3) is
realizable at m = 2. Round 33 proved it realizable at m = 1
(exhaustive; the counting stack tight) and posed TCAP-DIM
(realizable iff m <= 2; moduli excess -13 at m=1, -1 at m=2, +35
at m=3). m = 2 sits at excess -1 — the boundary. Round 33 reduced
it: the locator curve is F(Z,x) = c_2(x)Z^2 + c_1(x)Z + c_0(x)
with deg c_i <= rho = 7 on N = 32 domain points; (SAT4) demands a
9-vertex 31-edge multigraph of slope-pair incidences with degree
sequence 7^8,6 (the design EXISTS: K_9 minus a 2-path and 3
disjoint edges); each edge {a,b} needs a domain point x with
c_1(x) = -(a+b)c_2(x), c_0(x) = ab*c_2(x) — 62 equations LINEAR in
the 24 curve coefficients once the 9 slopes and 31 points are
chosen: ~40 free parameters vs 39 rank conditions. A realization
exists iff that system has a rational point (then verify the
resulting pencil column-far at generic rank rho with T = rho+2 =
9). YOUR JOB: decide it.

## Deliverables

**D1 — THE SEARCH, PROPERLY STRUCTURED.** Not random draws (the
round-33 bank-2 lesson: q^-Theta(m^2) power). Structure the search:
fix the multigraph design (enumerate the few isomorphism classes if
cheap); the slopes G and points X enter algebraically — eliminate
the linear c-layer first (the 62x24 system's rank as a function of
(G, X) assignments), then search the combinatorial layer with the
rank condition as the filter. Two fields (32 | q-1: q = 97, 193;
also designed domains at larger q per round 33's D3 method).

**D2 — EITHER OUTCOME, CERTIFIED.** If realizable: the explicit
witness (pencil, verified column-far, generic rank rho, T = 9,
(SAT1)-(SAT5) measured exactly — the full round-33 D2 table) +
what it does to F1/(NEWCAP) (at m=2 the w* window is NOT degenerate
— measure a* vs 7m-1 = 13: THIS IS THE FIRST REAL F1 TEST). If
not realizable at the searched fields: state exactly what was
exhausted vs sampled (a fields-searched negative is NOT a theorem —
say so) and what obstruction pattern emerged.

**D3 — THE TCAP BOUNDARY.** Whichever way D2 lands: update
TCAP-DIM's status (boundary confirmed at 2 / moved to 1 /
undecided-with-named-gap). If realizable, attempt m = 3 with the
same structured method (excess +35 — expected infeasible; a
negative there with the structure visible is worth more than the
m=2 positive).

**D4 — VERDICT.** Misses first; the m-boundary of record.

## Blind priors to register

P((SAT3) realizable at m=2), P(the linear layer generically full
rank), P(F1 fires if realizable — a* > 13), P(m=3 realizable).
