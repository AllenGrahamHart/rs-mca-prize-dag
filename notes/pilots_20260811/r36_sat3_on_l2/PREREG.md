# PREREG — r36_sat3_on_l2 (round 36)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r35_l2_gate/REPORT.md` (round 35)
2. `notes/pilots_20260811/r35_rout_layer_a/REPORT.md` (round 35)

## Mandate

(SAT3)-ON-(L2) — THE FACE-OFF ROUND. Round 35 proved the e=m=2
stratum NONEMPTY (twelve certified pencils, the D-B/D-F inversion:
for fixed B = (f,g,h,k), 20 free parameters projective-19, the
curve is pinned by det M(B) = 0 — ONE condition) but every witness
has T = 0: locators split at exactly the random rate. THREE
instruments say the T = rho+2 class is empty at m >= 2 (round-34's
searched negative; the corrected TCAP ledger +3..+5; anchor 2's
C(16m,4m-1) first-moment gate, calibrated twice at m=1 — the 16
realized (SAT3) families ARE the layer-A-consistent
configurations — and ~ -48 bits at m=2, q=97). ONE theorem warns
counting cannot be trusted in this lane (anchor 1's own witnesses
against the dead +4 reading; LB1 against its moment). YOUR JOB:
make the free B-parameters fight the moment. Either a witness —
which would be a REALIZED (SAT3) at m=2, moving the TCAP boundary
back, giving F1 its first real test and making the whole
W-layer/layer-A program non-vacuous — or a NAMED structural
obstruction, which upgrades three instruments to a mechanism.

## Deliverables

**D1 — THE B -> SPLITTING MAP, STRUCTURED.** What does
prescribing split locators cost in B-space? The locators are the
roots of the Q_z = Q_0 + zQ_1 + z^2Q_2 pencil members at the
T = 9 supported slopes; splitting over a designed domain (mu_32
or a bespoke 32-set — round 34 bank 4's designed-domain question
had ZERO input; your witnesses give it input) is ~C(32,7)/q^6 per
member naively. Count exactly: conditions vs the 19 projective
B-dims + the field/domain choices. Derive BEFORE searching where
the supply must come from (the m=1 calibration says coherent
fibre structure — anchor 2's 16=16; what is the m=2 analogue?).

**D2 — THE DESIGNED SEARCH.** Not random draws. Structured B
families (self-reciprocal, subgroup-symmetric — the k in {2,3}
admissible symmetries survive round 34's classification), designed
domains, and INVERTED prescription: fix one or two split locators
FIRST (choose Q_0 with prescribed root set!) and solve D-B for
the rest — anchor 1's criterion is symmetric in Q_0/Q_2 and Q_0's
roots are free parameters of the construction. Track T (supported
slopes) as the objective; every T >= 1 configuration is the first
of its kind and gets the full measured table. Two fields minimum.

**D3 — THE OBSTRUCTION SIDE.** If the search walls: name it. Is
it arithmetic value-confinement again (the flat-supply law of the
(BIV-CURVE) lane)? Is there a FOURTH instrument (an exact
constraint linking det M(B) = 0 to non-splitting)? The m=1
mechanism (disjoint coset locators, the R4 fence) is banked-dead
at m >= 2 — where exactly does its failure bite the B-design?

**D4 — VERDICT.** The T-record of the round with its full
provenance; F1/(NEWCAP) status; the class-emptiness picture after
the round (how many instruments, any mechanism); misses first;
cross-pilot flag (do NOT read siblings).

## Blind priors to register

P(a T = rho+2 witness this round), P(T >= 1 achieved at all),
P(the designed-domain route beats mu_32), P(the wall, if hit, is
value-confinement), expected max T this round (a number).

---

## Pilot registrations

Written with the Edit tool after reading EXACTLY the two named
anchors (`r35_l2_gate/REPORT.md`, `r35_rout_layer_a/REPORT.md`)
and BEFORE any other read, any grep, any `ls`, and any interpreter
invocation. Everything below is derived from the two anchors and
from paper arithmetic only. No post-registration addenda: errors
here will be reported as misses, not edited away.

### R0 — notation fixed from the anchors

`m=2, rho=4m-1=7, N=16m=32, R=8m=16, A=R+1-2rho=3, e=m=2, s=0,
delta=m-1=1, T_target=rho+2=9`. `M(Z)=M_r(y_0)+Z M_r(y_1)`, `9x8`;
`Q_Z=Q_0+ZQ_1+Z^2Q_2`, `deg Q_j=7`. `B=(f,g,h,k)`, `deg<=4`, 20
coords, `P^19`. Anchor 1's `E1: Q_2f-Q_1g-Q_0h=0`,
`E2: Q_1f-Q_0g-Q_2k=0`; good component of the `(L2)` locus has
dimension 18; witnesses have `T=0`. Anchor 2's gate:
`log2 E = [(m+1)(rho+1)-4]log2 q + log2 C(q+1,T) + T[log2 C(16m,4m-1)
- rho log2 q]`, `= -48.14` at `m=2,q=97`.

### R1 — execution order (binding on me)

D1 (derive the exact B->splitting ledger and the parametrization)
-> D2 (designed search, two fields) -> D3 (obstruction) -> D4.
D3 is executed and reported even if D2 succeeds, and vice versa.

### R2 — falsifiable derivations, committed BEFORE any compute

**(X1) THE CLOSED-FORM PARAMETRIZATION (the round's bet).**
Eliminating between anchor 1's `E1`,`E2` gives
`Q_2(f^2-kg) = Q_0(g^2+hf)`... in the form I will use: there is a
linear `L` (root `ell`) with
```text
L*Q_0 = f^2 - kg ,   L*Q_1 = fg + hk ,   L*Q_2 = g^2 + hf
```
and the ONLY conditions are the two at `ell`:
`f(ell)^2 = k(ell)g(ell)` and `g(ell)^2 = -h(ell)f(ell)`
(the third, `f(ell)g(ell) = -h(ell)k(ell)`, is implied).
Equivalently `L*Q_z = det( [[f,k],[g,f]] + z[[g,f],[-h,g]] )`, a
`2x2` determinantal representation of the whole pencil member.
**Predicted consequence:** the `(L2)` stratum is RATIONALLY
PARAMETRIZED — every draw is a hit (rate 1), against anchor 1's
`det M(B)=0` rate `1/q`.
**FALSIFIER:** a draw satisfying the two `ell`-conditions whose
`(Q_0,Q_1,Q_2)` has `nullity(36x32) = 0`, or a certified anchor-1
witness not in the family.

**(X2) DIMENSION CHECK.** Parameters `B (19 proj) + ell (1) - 2
conditions = 18`, which must equal anchor 1's measured good
component dimension 18. **FALSIFIER:** any other number.

**(X3) PRESCRIPTION IS FREE ON THE `Q_0` SIDE.** Given any target
split `Q_0 = prod_{a in S_0}(x-a)` and any `g` of degree 4:
`f^2 == L Q_0 (mod g)` is solvable iff `L Q_0` is a square at each
root of `g`; then `k=(f^2-LQ_0)/g` has degree `<=4` automatically
and `f = f_0 + c*g` leaves `c` free. So **`T >= 1` over ANY
designed domain containing `S_0`, including `mu_32`, is achievable
BY CONSTRUCTION, not by search.** **FALSIFIER:** the degree of `k`
exceeds 4, or the resulting object fails certification.

**(X4) THE EXACT B->SPLITTING LEDGER (D1's answer).** On the
18-dimensional good component, "member `z` splits over a fixed
32-set" is codimension 7 (the split locus is `C(32,7)` points in
`P^7`), each supported slope carries `+1` (choice of `z in P^1`),
and the pencil-reparametrization `PGL_2` acting on `Z` removes 3.
Hence
```text
expected dim{T >= t} = (18-3) + t - 7t = 15 - 6t
```
`t=1: 9`, `t=2: 3`, `t=3: -3`, `t=9: -39`. **Predicted: the
designed-count threshold sits at `T = 2`, and `T >= 3` is already
expected-empty on dimension grounds** (before any arithmetic).

**(X5) THE FIRST-MOMENT LEDGER, B-SIDE (sharper than anchor 2).**
```text
log2 E(T=t) = 15 log2 q + log2 C(q+1,t) + t[log2 C(32,7) - 7 log2 q]
```
At `q=97` (`log2 97 = 6.600`, `log2 C(32,7) = 21.68`): per-member
term `-24.52`; `t=1: +81.1`, `t=2: +62.2`, `t=3: +42.7`,
`t=4: +22.7`, `t=5: +2.4`, `t=6: -18.1`, `t=9: -81.1` bits.
**Predicted: the B-side ledger is `33` bits MORE negative than
anchor 2's `-48.14` at `T=9`, the gap being exactly
`(20-15) log2 q`, because the `(L2)` good component modulo `PGL_2`
has 15 free dimensions, not the biform's 20.** **FALSIFIER:**
arithmetic recomputation giving a different gap or sign.

**(X6) (QPACK) — THE PACKING CEILING, DOMAIN-DESIGN-INDEPENDENT.**
For each `x`, `z |-> Q_z(x)` is a polynomial of degree `<= m = 2`
in `z`. With `s = 0` it is not identically zero, so
```text
d_x := #{supported z : Q_z(x) = 0}  <=  m = 2   for every x.
```
Summing over a domain `D` of size 32 against `T` fully split
members (`rho = 7` roots each):
```text
7T = sum_x d_x <= 2*32 = 64   =>   T <= 9 = rho+2.
```
**The (SAT3) target is EXACTLY the packing ceiling**, and `T = 9`
forces 31 of the 32 points to be roots of TWO supported members
and one point of exactly one — i.e. every `q_x(z) := Q_0(x) +
zQ_1(x) + z^2Q_2(x)` must split over `F_q` (cost `~2^-32`) AND
have both roots inside the 9-element supported set (cost
`~(C(9,2)/C(q+1,2))^31 = (36/4753)^31 = 2^-218` at `q=97`).
**PRE-DECLARED SUBTRACTION RISK: I expect `d_x <= m` to be BANKED
inside (SAT4) (anchor 2 cites `saturation_rigidity/statement.md:36-69`
for `d_x <= m` and `sum_x(m-d_x)=1+O<=m`).** I will grep before
claiming anything, and if banked I will report it as a
re-derivation, in MISSES, ahead of results.

**(X7) THE `7T > 32` THRESHOLD.** With every supported member fully
split over a 32-point domain, disjointness of root sets forces
`7T <= 32`, i.e. `T <= 4`. **So `T >= 5` REQUIRES member-pairs to
share domain roots** (a `q_x` with both roots supported), and `T=9`
requires near-perfect double packing. **FALSIFIER:** a `T >= 5`
object whose supported members have pairwise disjoint root sets.

**(X8) THE DESIGNED-DOMAIN GAIN, QUANTIFIED.** For `T >= 1`:
bespoke-32-set cost = "one member splits over `F_q`" `= 1/7! =
1/5040`; `mu_32` cost `= C(32,7)/q^7 = 3365856/6.4847e13 = 5.19e-8`.
Ratio `q^7/(7! C(32,7)) = 3.8e3` at `q=97`. Per curve, expected
number of `F_q`-split members `= (q+1)/5040 = 0.0194` at `q=97`.
**Anchor 1's 12 witnesses x ~98 parameters gave an expectation of
~0.23 split members and measured 0 — fully consistent with the
random law, so their `T=0` is NOT evidence of an obstruction.**
**FALSIFIER:** measured split rate off by >3x.

**(X9) THE `m=1` -> `m=2` SUPPLY ANALOGUE (D1's last clause).** At
`m=1` anchor 2's coherent fibre structure was "16 = 16": the
layer-A-consistent configurations ARE the realized families. My
`m=2` analogue prediction: the supply must come from the
**`ell`-fibre**, i.e. from the 2 conditions at a single point `ell`
being the ONLY obstruction, so that split prescription on ONE
member is free and every further member costs a full 7. **Predicted
shape of the answer: supply is coherent for `t=1` (free), partially
coherent for `t=2` (3 dims left), and INCOHERENT for `t>=3`.**

### R3 — blind priors (the five the brief demands, plus auxiliaries)

| id | statement | prior |
|---|---|---|
| P1 | a `T = rho+2 = 9` witness this round | **0.02** |
| P2 | `T >= 1` achieved at all (any domain) | **0.93** |
| P3 | the designed-domain route beats `mu_32` | **0.80** |
| P4 | the wall, if hit, is value-confinement (flat supply, (BIV-CURVE) lane) | **0.30** |
| P5 | **expected max `T` this round = 3** (number) | — |
| P5a | max `T` over `mu_32` specifically | **1** |
| P5b | max `T` over a bespoke 32-set | **3** |
| P6 | (X1) parametrization verifies with no correction | 0.70 |
| P7 | (X2) dimension comes out 18 | 0.75 |
| P8 | `T >= 1` over `mu_32` by construction (X3) | 0.85 |
| P9 | `T >= 2` over a bespoke 32-set | 0.60 |
| P10 | `T >= 2` over `mu_32` | 0.25 |
| P11 | `T >= 3` any domain | 0.15 |
| P12 | the wall is (QPACK)/packing-arithmetic rather than value-confinement | 0.45 |
| P13 | (X5)'s `33`-bit gap to anchor 2 verifies | 0.65 |
| P14 | `d_x <= m` is already banked (subtraction fires) | 0.80 |
| P15 | the `2x2` determinantal form is already banked (anchor 1 cites `a1_core_one_middle_adjugate_factorization` — an ADJUGATE factorization, which is `2x2`-shaped) | 0.55 |
| P16 | a FOURTH instrument (exact constraint linking `det M(B)=0` to non-splitting) is found | 0.35 |
| P17 | at least one ramguard run fails | 0.70 |

### R4 — MISS-2 GUARD (mean-vs-max), four clauses, binding

(i) **Any `T` I report is a SAMPLE MAXIMUM over the draws I made,
never a bound on `max T` over the stratum.** A greedy or designed
`T` is a LOWER bound on the best designable `T`; a search that
finds `T=0` is an upper bound on NOTHING.
(ii) **I will report the DISTRIBUTION of `T` (full histogram over
all draws and all `q+1` slopes), not only the record**, and the
record's provenance (which construction, which field, which
domain).
(iii) **Power is asymmetric and I declare the direction in
advance:** a witness has full power (existence is
witness-checkable); a negative has power only against the rate I
can actually sample, and (X8) says that rate is `0.0194` per curve
for `F_q`-splitting and `5e-6` per curve for `mu_32`-splitting.
**A null result at `<10^5` draws over `mu_32` has ZERO power and I
pre-declare it as such.**
(iv) **No counting excess is allowed to carry an emptiness verdict**
(anchor 1's own `pb_design_ceiling/proof.md:125` blind spot; anchor
2's R3(b)). (X4)'s `15-6t` and (X5)'s bits are heuristics; only
exhibited objects and measured ranks carry verdicts.

### R5 — zero-power pre-declarations

Z1. **A bespoke 32-set is NOT `mu_32`.** Any `T` measured over a
designed non-multiplicative domain has **zero power** for (SAT3),
for the strict endpoint, and for the official row, because the
endpoint's `D` is the multiplicative group `mu_N`. I will label
every `T` with its domain and will not merge the two columns.
Z2. **Failure to reach `T=9` proves nothing** — see R4(iii).
Z3. **Nothing here bears on `m >= 3`, on `q ~ 2^128`, on the `9/4`
or `7/4` ledgers, on FR-canonical, or on Rout.**
Z4. **The first-moment ledger (X5) is a heuristic and it is
NEGATIVE at `t>=6`, which is the direction that proves nothing.**
It cannot exclude; it can only price.
Z5. **If the `T=rho+2` class is empty, every statement quantified
over it is vacuous**, including any (SAT3)-conditional claim I
make (anchor 2's zero-power 2).
Z6. **Rank/nullity 0 on a structured object is evidence about that
object only, never evidence of non-existence.**
Z7. **Two fields minimum for every structural claim.** A one-field
number is declared single-field in the report, not glossed.
Z8. **`(SAT2),(SAT4),(SAT5)` remain vacuous unless `T>=1` is
achieved; `O`, `d_x`, `sum_x(m-d_x)` are undefined at `T=0`** and I
will say so rather than printing zeros.
Z9. **Whether the parameter `z = infinity` counts as a supported
slope is a framework question I cannot settle from the anchors.**
I will report `T` BOTH ways (`T_fin` counting only `z in F_q`, and
`T_P1` counting `z=infinity` i.e. `Q_2` as well) and will headline
the SMALLER.

### R6 — CATCH-24A subtraction plan (before any novelty claim)

Grep `background/`, `critical/`, `notes/` with
`--exclude-dir=r36_lawcount_geom --exclude-dir=r36_hrlow
--exclude-dir=r36_m4_nonsplit --exclude-dir=pilots_20260802
--exclude-dir='prize-codex-*' --exclude-dir=.git
--exclude-dir=__pycache__ --exclude=dag.json`, at the SEARCH level,
for: `d_x`, `saturat`, `packing`, `determinantal representation`,
`adjugate`, `2x2`/`2 x 2`, `Bezoutian`, `quadratic in Z`,
`designed domain`/`designed-domain`, `bespoke`, `split over D`,
`value confinement`/`value-confinement`/`flat supply`,
`rational parametrization`/`rational parametrisation`,
`f^2 - kg`, `first moment`/`first-moment`, `C(32,7)`/`C(16m`,
`T <= rho+2`/`T<=rho+2`/`rho + 2`, hyphenated and infixed variants
of each. Expected live subtractions: (X6)'s `d_x<=m` (P14=0.80),
the determinantal/adjugate form (P15=0.55), the `C(16m,4m-1)` gate
(anchor 2's, explicitly NOT mine).

### R7 — expected misses (registered so they are not surprises)

(a) The parametrization (X1) may miss a component (e.g. objects
with `L | f`, `deg L = 0`, or `Q_1` sharing factors) — I will test
coverage against fresh anchor-1-style `det M(B)=0` witnesses, not
assume it.
(b) `T` over `mu_32` beyond 1 will probably be out of reach at the
sampling rates in (X8), and I pre-declare that as zero power, not
as an obstruction.
(c) I expect at least one of (X4)/(X5)'s counts to be off by one
(the `PGL_2` quotient and the `z`-scaling interact); the two
independent derivations (`15-6t` vs the bit ledger) are the
cross-check, and a disagreement is a MISS, reported.
(d) I will probably over-claim novelty on the `2x2` determinantal
form; R6 is the check.
