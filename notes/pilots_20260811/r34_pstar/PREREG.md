# PREREG — r34_pstar (round 34)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/rh_moving_kernel/REPORT.md` (round 33)
2. `background/nodes/rate_half_ca_hankel_split_pencil_equivalence/statement.md`

## Mandate

THE CHEAPEST DECISIVE FAR-CA QUESTION (round 33's R-PSTAR). The
far-CA deep stratum's structure now turns on one invariant: p*, the
minimal common apolar degree of the pencil space V = <Phi_0,Phi_1>.
Generically p* = floor((2R-1)/3)+1 ~ 2R/3. The FG stratum (where a
fixed generator exists, and where the scaled-Vandermonde normal
form + key equation live) requires p* <= 2rho; the honest
fixed-generator mechanism needs p* + p_gen <= R i.e. p* <= R/2
(misses generically by 7/6). THE QUESTION: does ANY column-far
pencil at razor-shaped parameters have p* <= R/2 (equivalently:
is FG nonempty among column-far pencils in the wide regime)? IF NO:
FG is empty at the razor, the whole fixed-generator branch closes
NEGATIVELY, and R-KER becomes the SOLE far-CA residual — a major
structural simplification. IF YES: the FG key equation gets its
first live instances and R-FG becomes a real budget question.

## Deliverables

**D1 — THE p*-vs-COLUMN-FARNESS STRUCTURE.** Low p* means V lies in
the inverse system of a degree-p* form: V ⊂ Ann(P*)^perp — i.e.
both syndromes are linear combinations of powers of P*'s roots
(generalized: the apolarity/Waring structure). Column-farness says
K_0 = Ann(V)_r contains no D-split element. Derive the exact
tension: for p* <= R/2, K_0 = P* · F[x]_{r-p*} (round 33's FG2:
column-far <=> P* not D-split-squarefree). So FG-membership at
p* <= R/2 just needs P* squarefree-non-D-split AND the syndromes
genuinely in the inverse system — CONSTRUCT directly (round 33's
FG pencils were constructed this way at small scale — quote and
extend). The REAL question is whether such pencils exist AT THE
RAZOR SHAPE (r/R = 1 - 2^-6, rho = R - r): check the dimension
arithmetic exactly — dim of the low-p* pencil locus vs the
column-far conditions.

**D2 — THE CENSUS.** At wide-regime cells (round 33's e1 cells +
razor-shaped ratios as feasible): the p* spectrum of column-far
pencils (exhaustive where cheap, constructed families otherwise).
Does p* <= R/2 occur? With what codimension?

**D3 — THE RAZOR VERDICT, exact arithmetic.** The locus
{p* <= R/2} has codimension ~(something)(p*-dependent) in pencil
space; column-farness is one condition per D-split candidate.
Derive whether the intersection is empty/nonempty at razor
parameters BY DIMENSION COUNT (with the naive-count caveat quoted —
round 33 bank 3's MISS 5 precedent), and if constructible, exhibit.

**D4 — VERDICT.** FG empty (R-KER sole residual) / FG nonempty
(R-FG live with witnesses) / undecided-with-named-gap. Misses
first; LB1-consistency check (LB1 pencils have dim K_0 = 0 — where
do they sit in the p* spectrum? predict then measure).

## Blind priors to register

P(FG nonempty at razor shape), P(p* <= R/2 occurs at any wide
census cell), expected codimension of the low-p* locus, P(the
dimension count is decisive either way).
