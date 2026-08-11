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

## Pilot registrations

Written after reading EXACTLY the two named anchors
(`rh_sat3_realizability/REPORT.md`,
`rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md`) and
BEFORE any other read, any grep, and any interpreter invocation.

**R0 — notation I will use.** `m=2, rho=7, N=32, R=16, A=3, e=2,
s=0, delta=m-1=1, T=rho+2=9`. `F(Z,x)=c_2(x)Z^2+c_1(x)Z+c_0(x)`,
`deg c_i<=7` (24 coefficients). `P_g(x):=F(g,x)=c_2g^2+c_1g+c_0`
is the locator of slope `g` (**linear in the 24 coefficients for
fixed `g,x`** — I will use this). `S_g` = root set of `P_g`,
`u_g=|S_g|`, `d_x=#{g: P_g(x)=0}<=e=2`, `O=sum_g (rho-u_g)<=delta=1`,
incidences `sum_x d_x = T*rho-O = 63-O`. Design graph `Gamma`:
vertices = the 9 slopes, one edge per domain point with `d_x=2`.
`Gamma` has 31 edges and degree sequence `7^8,6`.

**P1 — the headline.** P((SAT3) realizable at `m=2` over SOME
finite field) = **0.10**. P(I exhibit a witness this round, at
`q in {97,193}` or a designed domain) = **0.05**.

**P2 — the linear layer.** P(the 62x24 edge system has full rank
24 for random `(G,X)`) = **0.93**. P(some *structured* `(G,X)`
(subgroup slopes, geometric/arithmetic domains, Frobenius-stable
choices) drops the rank below 24 at `q<=200`) = **0.25**.
P(rank ever drops to <=23 *with a non-degenerate witness attached*,
i.e. the kernel vector actually realizes the design) = **0.05**.

**P3 — F1.** P(F1 fires | realizable) = **0.35** (`a* > 7m-1 = 13`).
At `m=2` the `w*` window is `[?, 2rho=14]` and `7m-1=13`, so the
window is a genuine two-point test, unlike `m=1`. If I get no
witness, F1 stays unexercised and this round has **zero power**
over it (pre-declared).

**P4 — m=3.** P((SAT3) realizable at `m=3`) = **0.02**.

**P5 — THE LOAD-BEARING PREDICTION (registered before computing).**
(TCAP-DIM) as posed counts `params = 23(curve) + (4m+1)(slopes) +
16m(domain)` against `conds = T*rho-O`, and **does not quotient by
the automorphism group that acts on every solution**: `x -> ax+b`
on the domain (2-dim) and `gamma -> alpha*gamma+beta` on the slope
line (2-dim), and, generically, the full `PGL_2 x PGL_2` (6-dim).
Every solution therefore sits in an orbit of dimension >= 4 (>= 6
generically) with finite stabiliser, so a naive expected dimension
below that is self-inconsistent. **I predict the corrected excess
is `excess'(m) = 12m^2-24m-1-O + G` with `G in {4,6}`, i.e.
`excess'(2) = +3..+5 > 0` (unrealizable-expected) while
`excess'(1) = -9..-7 < 0` and the `e=1` ladder stays `<0` at every
`m` — both of round 33's positive controls preserved and only
`m=2` flipping.** P(this correction is arithmetically right and
survives both positive controls) = **0.80**. P(it is already in
the repo somewhere, so not mine to claim) = **0.30**.

**P6 — the combinatorial layer.** P(the simple design is unique up
to isomorphism, `= K_9 - (P_3 + 3K_2)`) = **0.90**. P(genuine
multigraph designs — two blocks meeting twice — also exist and
must be searched) = **0.60**. P(the combinatorial layer is NOT the
binding constraint) = **0.92**.

**P7 — what the forward search will show.** Define `score(C)` =
max over 9-subsets `G` of the number of domain points whose BOTH
locator-roots lie in `G` (max 31). P(max score over all sampled
nets at `q<=200` is `<= 15`) = **0.75**; P(`<= 25`) = **0.95**.
P(the empirical decay is consistent with a `q^{-Theta(1)}` power
per extra edge, i.e. round 33's bank-2 lesson repeats) = **0.85**.

**P8 — structure predictions (falsifiable this round).**
(a) `F` is irreducible over `F_q(x)` in any realization — if
`F=c_2(Z-u)(Z-v)` with `u,v` rational of degrees `d_1+d_2=7`, the
saturated points are `<= 9*min(d_1,d_2) <= 27 < 31`. P(this
argument is correct) = **0.75**.
(b) the smooth model `C` of `F=0` (a bidegree-`(2,7)` curve, arithmetic
genus 6) cannot be rational. P = **0.55**.
(c) the necessary class condition `9K ~ 31h + p_0` on `C` costs
`genus(C)-1` conditions, so no genus stratum is free. P = **0.45**.

**MISS-2 GUARD (mean-vs-max, pre-registered).** Every number my
searches produce is a **max over a sample**, never a bound. I
commit in advance: (i) I will report the max score and the sample
size, and will NOT convert "the best of `n` draws scored 12/31"
into any statement about the max over all configurations; (ii) any
mean/typical statement (mean best-score, mean rank of the 62x24
layer, mean number of totally-split members of a net) is reported
only as a *calibration of the search*, and I will not let a mean
stand in for a max anywhere in the verdict; (iii) a negative from
sampled fields is NOT a theorem and will be labelled
"fields-searched negative" in the verdict line itself; (iv) if a
structured family beats the random mean I will report the family,
not the mean.

**ZERO-POWER DECLARATIONS, pre-committed.** (Z1) A negative at
`q in {97,193}` has zero power over `q = 2^37`-scale fields and
zero power over the existence question. (Z2) Any dimension ledger
(mine or (TCAP-DIM)) is a heuristic with the
`pb_design_ceiling/proof.md:125` blind spot and has no standing as
a bound. (Z3) If no witness, this round has zero power over F1 and
over `(NEWCAP)`'s content. (Z4) `m=3` work is calibration only.

**ROUTE ORDER (fixed now).** (1) design enumeration + positive
control replaying round 33's `m=1` result in MY code; (2) the
62x24 linear layer's rank as a function of `(G,X)`, random and
structured; (3) forward search: nets -> pair-graph -> best 9-set;
(4) targeted structured families (monomial/Kummer, Dickson,
group-invariant, elliptic/low-genus); (5) corrected ledger + m=3;
(6) verdict. I will not reorder to chase a positive.

**FALSIFIERS OF MY OWN VERDICT.** (F-a) any 9-set scoring 31; (F-b)
a rank-<=23 layer with a kernel vector realizing the design; (F-c)
a structured family with `>= 6` totally-split members in one net
(the bottleneck functional) — which would make P1 badly mispriced.
