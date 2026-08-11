# PREREG — r38_sporadic_det (round 38)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r36_m4_nonsplit/REPORT.md` (round 36)
2. `notes/pilots_20260811/r37_share3_gap/REPORT.md` (round 37)

## Mandate

THE LAST TWO m=4 ROUTES. (A) SPORADIC (non-factoring) 3-sharing:
Lueroth forces UNIFORM sharing to factor through a degree-3 w;
sporadic = non-uniform (8 shared triples WITHOUT a global
quotient map). Priced < 1e-4 by round 36, never searched, and
the pricing was a naive count in a lane where counting is dead
(five refutations in two rounds — including round 37's own
constant-norm mechanism beating its naive count by 3400x).
STRUCTURE FIRST: what does a non-factoring Psi with 8 shared
triples look like? The 8 shared-triple conditions are
Res_gamma(R(.,t_i), R(.,t_j))-type coincidences WITHOUT the
lattice structure — is there a WEAKER factoring (through a
correspondence rather than a map? a degree-3 rational curve
in P^1 x P^1?) that Lueroth does not forbid and that carries
sharing at sub-naive cost? Derive the taxonomy BEFORE searching.
(B) THE DETERMINANTAL 11-MERGE SOLVE: the 13-slope variety is
dim 4 over F_qbar (two agreeing counts) but unreachable by
incremental instruments (budget 8). Attack the simultaneous
system EXPLOITING ITS STRUCTURE: the merges are "the twisted
cubic C meets 11 named lines l_ij" — use the resultant/
elimination structure (each "meets l_ij" is one determinantal
condition on the 4-dim family; the family after 8 prescribed
merges is EXPLICIT with kernel dim 2 — parameterize it and solve
the REMAINING 3 conditions on ~3 parameters as a small
polynomial system: 3 resultants in 3 unknowns, NOT generic
Groebner). Even deciding solvability at q = 193 decides whether
the round-37 fence's "free-merge" reading was the whole truth.

## Deliverables

**D1 — THE SPORADIC TAXONOMY.** Non-uniform sharing patterns
compatible with the (OV)/per-side caps: which (n_3', n_2', n_1')
mixtures short of full uniformity survive round 36's exclusion
(it forced n_3 = 8 ASSUMING the demand ledger — recheck at the
degenerate-fibre slot count 23 too); the correspondence-sharing
question (Lueroth's scope: does a (3,3)-correspondence in
P^1 x P^1 carry 8 triples without factoring?); the cost ledger
for each surviving pattern. Then a TARGETED search of the
cheapest pattern only (two fields).

**D2 — THE 3-IN-3 SOLVE.** From a fixed 8-prescribed-merge state
(kernel dim 2 + the slope choices — derive the exact residual
parameter count), write the 3 remaining merge conditions as
polynomials in the residual parameters; solve by iterated
resultants/gcds (stdlib-feasible if degrees stay < ~50 — derive
the degrees FIRST). Sweep enough 8-merge states at q = 193 to
either find a 13-slope solution (=> hand to the pipeline: this
is the same witness event as the side door) or state the
solvability rate exactly on the swept sample.

**D3 — RECONCILIATION.** If D2 finds solutions the round-37
budget fence needs its scope tightened (it bounds INCREMENTAL
instruments only — confirm its own caveat); if D2 exhausts
negative on a large sample, the free-merge reading hardens
toward an exclusion CONJECTURE (state it with falsifiers).
Either way: the exact relationship between the dim-4 variety,
its F_q-points, and the budget-8 reachable locus.

**D4 — VERDICT.** The m=4 route map after this round; misses
first; cross-pilot flag (do NOT read siblings).

## Blind priors to register

P(a correspondence-sharing pattern exists legally), P(the 3-in-3
degrees are stdlib-feasible), P(a 13-slope solution from D2),
P(the dim-4 variety has F_q-points at q=193), expected outcome
(a phrase).
