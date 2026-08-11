# PREREG — r38_cauchy_lattice (round 38)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r37_third_solve/REPORT.md` (round 37)
2. `background/nodes/l1_exact_shell_balanced_shifted_lattice_reduction/statement.md`

## Mandate

THE CAUCHY-LATTICE ATTEMPT. Round 37 proved the third split
prescription is not an exact solve in (PAR) coordinates: it is
the condition that the FIRST MINIMUM of an explicit rank-2
F_q[x]-lattice ({(f,g) : f == R g mod P_0 P_inf}, deg P_0 P_inf
= 14) DROPS from its generic 7 to <= 4 — an overdetermined
type-(4,4) Cauchy interpolation, deficit 3, with an exact O(1)
test (one extended Euclid) and no known inverse. The banked
lattice-reduction machinery lives in the l1 lane (anchor 2) and
the xr syzygy router. YOUR JOB: attack the inverse. Either (a) an
ALGORITHM: exploit structure (the values t(x) are not arbitrary —
they come from (PAR) objects; S_0, S_inf are split subsets of
mu_32; the lattice varies ALGEBRAICALLY as the subsets move) to
find minimum-dropping triples faster than the q^3-blind rate —
any factor turns T=3-over-mu_32 from unreachable (8.9e3x short)
to reachable; or (b) a CHARACTERIZATION: which (S_0, S_inf, S_1)
triples admit the drop (an exact criterion in the (SCRIT) mold —
even a necessary condition prunes the search); or (c) a WALL: a
proof that the drop locus has no exploitable structure (state
what "no structure" means precisely). ALSO: the a* CONVENTION IS
RULED (coordinator, this launch): a* is PROJECTIVE — members are
degree-rho forms on P^1, roots at infinity counted (it reproduces
the banked 13 and preserves PGL_2-covariance of (PAR)). Under the
ruling, measure a* on every T >= 2 object you or prior rounds
built (regenerate as needed) — the first real F1 dataset.

## Deliverables

**D1 — THE LATTICE, STRUCTURED.** The Euclid trajectory of
(R, P_0 P_inf): the drop <=> a quotient-degree pattern (the
minimum's degree profile = the gap structure of the continued
fraction). Derive: how does the trajectory vary as ONE point of
S_1 moves? As S_1 is swapped wholesale? Is there a
divide-and-conquer (half-gcd) incremental update making a sweep
over all C(25,7) admissible S_1 cost near-linear amortized? (The
exact test is O(1) each; the question is beating enumeration by
structure, or organizing enumeration so it IS feasible:
C(25,7) = 480,700 tests/pair at q=97 — ALREADY within a ramguard
window if each test is microseconds. DERIVE THE REAL COSTS FIRST;
the blind-rate pessimism may be wrong about exhaustive-per-pair.)

**D2 — THE PUSH.** Execute the best instrument from D1 at
q = 97 and 193: sweep (S_0, S_inf) pairs (100%-s=0 via (SCRIT)'s
restriction; the bespoke double solve supplies the pairs), test
all admissible S_1 per pair. ANY T = 3 over mu_32 is the first
of its kind — full certification + a* under the ruling + push
toward T = 4 (the negative-exponent cell). If the sweep
exhausts without a hit, that is the first EXHAUSTIVE statement
about T = 3 over mu_32 on the reachable sub-locus — state its
scope exactly.

**D3 — F1 UNDER THE RULING.** a* (projective) on every T >= 2
object available; the distribution vs 7m-1 = 13; the supported-
pair overlap structure. Zero-power declared where the sample is
what it is — but this is the first F1 data with a fixed
convention.

**D4 — VERDICT.** Solve/characterization/wall status; the T
record; misses first; cross-pilot flag (do NOT read siblings).

## Blind priors to register

P(an exhaustive-per-pair sweep is feasible), P(T = 3 over mu_32
this round), P(a criterion in the (SCRIT) mold lands), P(the
Euclid trajectory admits incremental update), expected max T
over mu_32 (a number), P(a* = 13 dominates under the ruling).
