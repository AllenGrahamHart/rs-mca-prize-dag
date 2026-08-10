# f2_z1_mass_knife_edge

- **status:** PROVED (the instruments; the open mass bound is a
  stated residual, NOT a claim)
- **minted:** 2026-08-06 (mint-4, round 18), coordinator-audited.
- **provenance:** notes/pilots_20260806/z1_ternary_mass/ (81/81) +
  notes/pilots_20260806/o1_generating_adversary/ (the blind-
  convergent D1), coordinator-replayed.

## Statement

THE F2 TERMINAL OF RECORD (SL-1b' pinned to the MASS form) AND ITS
PROVED CONSTRAINTS, on the admissible object (the [S, S-R, R+1]_p
negacyclic GRS code on the half-system of mu_{2^{e_p}},
S = 2^40/e, R/S = 1/log2 p, p >= 2^39; Z(L) = Z_1^C, C <= 4).

**THEOREM Z-FLOOR (pointwise first-moment floor).** For EVERY
F_p-subspace, Z(L) = sum_{eps in L^perp cap T} 2^{-wt(eps)} >=
2^m / p^{dim L}. One Cauchy-Schwarz from the banked collision
identity sum_s |F_s|^2 = 2^m Z(L)
(dli_c1_l1_block_owner_ledger:15,18) — the identity was banked, the
inequality never drawn. Tight within a factor 2 of the ensemble
mean (no subspace beats random by more than 2x). 696 configurations,
exact rationals, 0 violations.

**THEOREM Z-1 (the DLI transport; = the adversary's THEOREM D1,
blind convergence).** dli_wcl_newton_short_window_exclusion's
hypothesis char > w HOLDS on every admissible row (p > m always, by
the e_p case split — the tower verdict is REVERSED by the field
cap), so the min ternary weight is >= 2R+1 = 8,589,934,681, double
SL-1's characteristic-free R+1. SCOPE: shift-0 windows only — 43
shifted counterexamples exist; the transport is legitimate because
the official window starts at l = 1.

**THEOREM Z-2 (gift back to DLI).** The Newton short-window
exclusion holds for ALL integer coefficients with w read as the l1
weight — the {+1,-1} restriction is unnecessary. Licenses l1
sphere-packing between ternary codewords.

**THEOREM Z-NOGO.** Saturation pins R/S = 1/log2 p, so the entire
distance+counting family (M3 and all sharpenings: 39.2x -> 28.3x
with Z-1 -> 21.3x with l1 packing) discharges only if p <= 8 —
against an admissible floor of log2 p >= 39. NO bound in that
family can ever close the terminal.

**THE KNIFE EDGE.** At k = e the Z-FLOOR is silent by 46.02 bits
out of 2.75e11 under the banked R = ceil(t/2) reading — ONE Lambda
condition, worth log2 p = 64 bits — and FIRES at +17.98 bits under
the exact-balance reading (in which case ternary kernel vectors
provably exist at the witness row: Z_1 >= 2^{17.98}, the EXACT-ZERO
form of the terminal is dead, yet Z = 2^{o(n)} so the MASS form
survives). The two defensible t-readings straddle zero; the reading
belongs to the t-naming/ensemble maintainer stack.

**THE OPEN TERMINAL (residual, not claimed):** prove
Z_1 <= 2^{o(m)} at k = e. ROUTE (b) SIZING REFUTED (round-19
tern_route_b, forced correction 2026-08-06): the "factor-2 headroom"
dropped the degree factor — restored, Weil is VACUOUS by exactly
26.000 bits (deg·sqrt p = 2^65 vs |H| = 2^39), and the executable
substitute (AM-GM + Z-2 moments, THEOREM 7: Z_1 <= 2^{0.8908·S}
unconditional) closes only at p <= 8.30 — Z-NOGO's own threshold.
NO NAMED ROUTE REMAINS. What survives of (b): the exact 1+cos
character form (the object is a sum of p^R NON-NEGATIVE terms — no
cancellation exists in principle; the true criterion is the
TAIL-COUNT |{u : P(u) >= 2^{cS}}| <= 2^{(1-c)S+46+o(S)} for all c);
two favourable reductions (oddness => COMPLETE subgroup sums, no
partial-sum loss; AM-GM => first moment in V_1 only, no L2->Linf
loss). THE PROP-10 LEAD IS RETIRED (round-20 tail_count CATCH-T1,
third forced correction 2026-08-06): the doubling/log-sine
functional TELESCOPES to the elementary cost form log2 P(u) = S -
sum_s d(c_s(u)) — no Dedekind content, nothing to bound. THE OPEN
FORM OF RECORD (normalized): Pr_u[P(u) >= 2^{cS}] <= 2^{-cS+o(S)}
(the +46.02 was exactly the saturation constant Delta; the knife
edge = the c = 1 slack, re-identified from the tail side); the tail
IS a small-values/box count for the MDS value code (structure
theorem); THE BINDING LAYER is c* = 1/ln 2 - 1 = 0.4427, where the
flat model saturates with ZERO margin — no per-coordinate-loss
argument can survive there. Proved: U_c = {0} for
c > 1 - 2^{-124.19} (an endpoint, honestly, not bulk progress).
Both standard supplies killed with computed thresholds (Z-2
moments: p <= 8.30 = Corollary 8; interpolation: no p at all,
position entropy H(1/L) > 1/L); the common cause: every supplied
input is R-LOCAL, short by the factor log2 p / log2(e log2 p) =
8.60; the Fourier escape is circular. The measured genuine tail
obeys the criterion at every reachable row with the binding layer
measured at 0.45 (= c* to grid resolution). Remaining leads: a
non-R-local instrument (nothing named), and the constant-weight
Z-FLOOR cell (crossing-side). Route (a)
(norm sandwich) is DEAD quantified (yields w >= 4.0000 — constant corrected per round-19 CATCH-T3, the sharp ceiling being w^{n/4} — dominated
by 4.3e9); route (c) (class structure) localises but cannot narrow.

**Calibration (honest):** on all valid miniatures (2-power 2N ONLY —
composite 2N carries p-independent cyclotomic ternary relations the
official object structurally cannot have, CATCH-Z6; a standing grid
rule) the deployed code sits at or below the random-ensemble median;
the deficit is exactly the excluded low-weight mass; "better than
random" is NOT established. No toy is evidence about Z_1 at the
official row.

## Falsifier

A subspace violating Z-FLOOR; an admissible row violating Z-1's
transported floor; a distance+counting discharge at p > 8
(contradicting Z-NOGO); an exact-balance-reading row where the floor
fails to fire as computed.

## NOT claimed

Z_1 <= 2^{o(m)} at k = e (THE open terminal); the t-reading; a
shifted 2R+1 law at 2-power 2N (open, thin sample); the route-(b)
sizing as a theorem.

## Round-22 forced corrections (2026-08-07, coordinator-applied on replay: CATCH-RL1 + CATCH-RL2 of f2_rlocality; 47/0 verifier suite)

**CATCH-RL1 — the 8.60 is attached to the wrong layer.** The
constant log2 p / log2(e log2 p) = 8.5990 (lines 82-84) is correct
arithmetic, but it is the instrument deficit AT LAYER c = 1
(DEF_INSTR(1)), where in fact R-locality costs NOTHING (proved by
exact LP: OPT_k(1) = p^{-k} exactly, measured 17^{-2}, 17^{-3};
tail_count THEOREM 12 already proves the c = 1 layer purely
R-locally with the knife-edge constant as the entire margin). The
BINDING-LAYER deficit is DEF_INSTR(c*) = 6.3130 (the quoted
sentence's own two numbers 0.443/0.116 = 3.8068 mix the two layers:
0.116 = I_INSTR(1), while the requirement 0.443 is at c*; the true
I_INSTR(c*) = 0.070124). Four-factor decomposition at c*:
THETA 1.0000 (zero margin) x AMGM 2.2990 x GAUSS 1.0348 x
LOCALITY-CAP 2.6536 = 6.3130 — at the binding layer the lossiest
single step is the locality cap, and at c = 1 the dominant loss in
the 8.60 was Chebyshev-at-an-endpoint (GAUSS = 44.36), not
locality. Numbers of record: 6.3130 (binding layer), floors below.

**CATCH-RL2 — the position-entropy diagnosis is an artifact.** The
clause "interpolation: no p at all, position entropy H(1/L) > 1/L"
(lines 81-82; tail_count THEOREM 10) rests on the union bound
|U_c| <= C(S,R) m^R, which is not the right R-local instrument:
the exact binomial moment Pr[N_A >= m] <= E[C(N_A,R)]/C(m,R) =
C(S,R) rho^R / C(m,R) CANCELS the position entropy, turning the
exponent positive (-0.0947 -> +0.0017 at c*) with a threshold at
every log2 p >= 3.06. The route still dies NUMERICALLY (deficit
258.9) — the ledger is unchanged; the DIAGNOSIS changes: the wall
is locality, not position entropy. "Dies at every p / no threshold
in p" is withdrawn as a diagnosis.

**THE CONCLUSION SURVIVES AND IS NOW A FLOOR.** The deficit is
STRUCTURAL for the formalized class (k-LOCAL: valid against every
k-wise-uniform law): exact toy floor FLOOR_R(c*) = 1.5889 at G1
(full 12870-state LP; second row p = 41: 2.7651); lifted
official-row floors (asymptotic evidence) FLOOR_R = 6.2063,
FLOOR_2R = 3.4848. The banked instrument (6.3130) sits +1.7% above
the k = R floor — essentially OPTIMAL for what R-wise independence
allows; the at-most-1.81x remaining headroom requires turning
Z-2's 2R-order l1-restricted information into a genuine 2R-wise
tail bound, and the licensed-radius analysis shows that attempt
collapses back onto V_1. The k <= R moment cap is SHARP (N_{R+1}
fails on all three toy rows, banked G2 value reproduced).

**MYSTERY 2'S REQUIRED INPUT, named:** a NON-LOCAL statement — "no
codeword of the GRS value code C* is unusually smooth" (a
box/smoothness count at exponential scale, quantifying over
Theta(S) coordinates at once). Nearest banked object: the
constant-weight Z-FLOOR cell on the crossing side (the same
constant-weight population shape as the round-22 crossing crux —
a FOURTH lane convergence). Sharpening: under the finite target
Z(L) <= 1 + N^3 the window is 4.77 bits absolute, so the non-local
input must be essentially EXACT, not merely 2^{o(S)}.
Source: notes/pilots_20260807/f2_rlocality/ (PROOFS.md THEOREMS
RL-1..RL-5; four verifier logs, coordinator-replayed).

## Round-23 addendum (2026-08-07, coordinator-applied on replay: the cw_shared_target pricing)

**THE NORMALIZATION PIN (pilot's catch, adopted).** The banked
factor-2 calibration ("no subspace beats random by more than 2x,
696 configurations") covers the RATIO normalization
CRATIO = Z/(1 + (2^m - 1)/p^dim L) — measured max 1.2610 over
7,000+ exhaustively swept 2-power cells across BOTH the f2 and
crossing families, 0 violations. It does NOT cover the EXCESS
normalization (Z - 1) * p^dim L / (2^m - 1), which exceeds 2 inside
this node's own family: EXCESS = 2.3463 at (S,R,p) = (16,2,3137)
(32 weight-11 ternary kernel vectors against a heuristic mass of
2^-7.23; grows along SIGMA -> -infinity: 2.13 at p=1409, 1.70 at
1889, 2.35 at 3137). Consumers at SIGMA < 0 need the EXCESS form —
do not quote the factor-2 calibration there.

**CONJECTURE Z-CEILING (candidate route for the open terminal —
proposed by the coordinator on the pilot's draft; adversarially
tested BEFORE proposal).** There is an absolute constant C such
that for every admissible F_p-subspace L on the 2-POWER grid:
Z(L) <= C * (1 + 2^m / p^{dim L}). Status: conjecture; the sharper
EXCESS form is already FALSIFIED (above) and must not be stated;
the ratio form survives 7,000+ cells at C <= 1.2610. IF true with
C < 2^4.77, it closes THIS node's open terminal with 4.44 bits of
headroom at the toy-measured constant (Z_1 <= 2^18.31 vs the
finite target 2^22.75) — under the exact-balance reading; under
the R = ceil(t/2) reading the terminal is trivially met (SIGMA =
-46.02), so the terminal is open ONLY under exact balance.
LOAD-BEARING HYPOTHESIS: the 2-power grid — at composite 2L the
p-free cyclotomic relations drive EXCESS to 178.51 (L=6, p=19993),
growing linearly in p. Registered falsifier: any admissible 2-power
cell with CRATIO > C.

**THE CONVERGENCE RESTATED HONESTLY (qualifies the round-22
"fourth lane convergence" above).** The convergence is real on the
OBJECT (one functional: TMASS(D) = sum_{eps in D cap T} 2^{-wt} —
mystery 4's deep-stratum population is EXACTLY this functional via
the LEMMA TC bijection, weight-distorted by only GDEV in
[1, Theta(sqrt L)], verified 20/20 + 12/12 against banked counts)
and on the missing DIRECTION (both consumers need the UPPER
companion of the proved floors). It is NOT a convergence on the
BOTTLENECK: mystery 2's terminal IS the functional (0-bit bridge),
while mystery 4's LIVE crux (Acc_shallow + aperiodic S) sits
exactly OFF the periodic strata where the TC fold is a bijection,
and the only remaining bridge (collision/Cauchy-Schwarz) loses a
measured 0.31-0.50 of kappa*log2 p — >= 4.565e11 bits at the
official row against a 54.45-bit tolerance. ONE OBJECT, TWO
TARGETS. First official-row datum on the shared functional: THEOREM
BB's 2^199.575 floor composed with the TC identity puts the
official-object ternary theta 11.84 bits BELOW its volume
heuristic — consistent with Z-CEILING, not refuting it.
Source: notes/pilots_20260807/cw_shared_target/
(coordinator-replayed, 130/29 with every FAIL an itemized
registered-prediction miss).

## Round-24 update (2026-08-08, coordinator-applied on replay: z_ceiling_assault — the conjecture SURVIVES, repriced and sharpened)

**Z-CEILING survives 59,203 exact-rational cells; the CONSTANT OF
RECORD RISES: C >= 1.7681** (record cell: the I2/RSET family,
N = 16, kappa = 1, p = 161761, TMASS = 159/64 EXACT, verified by
three independent algorithms to 6.5e-14). Headroom arithmetic
updated: Z_1 <= 2^18.80, headroom 4.44 -> 3.95 bits. The sigma ->
-inf direction is PROVABLY SAFE for the ratio form (CRATIO =
(1 + EXCESS*H)/(1+H): as H -> 0, CRATIO -> 1 regardless of
EXCESS); the danger band is sigma ~ 0 at small N.

**THEOREM RC (new, PROVED, 20/0 replayed):** for eps ternary of
weight U in the kernel, p | Res(Phi_2N, f) with 1 <= |Res| <=
U^{N/2} <= N^{N/2}. Hence UMIN >= p^{2/N}; TMASS = 1 identically
for every admissible p > N^{N/2}; and each N-line's sup CRATIO is
a maximum over FINITELY many primes. The sharp form of the
2-power gate: a nonzero ternary f (deg < N) with Res(Phi_2N, f)
= 0 exists IFF 2N is not a 2-power; at 2N = 2^a*3, PFMASS =
(5/4)^{L/3} exactly, reproducing the banked composite blowup
178.51 from a closed form, and a composite exhibit crosses 2
(CRATIO = 2.4314 at n = 24, p = 1000033, TMASS = 625/256 exact).

**SCOPE PIN (load-bearing):** "admissible" must be pinned to the
negacyclic-GRS parity row / I2 RSET specialization — for a GENERAL
subspace the ratio form is FALSE (all-ones line: CRATIO = 25.23 at
N = 8, p = 257; saturating at C(2N,N)/2^N, unbounded in N).

**THE HONEST STRUCTURAL FINDING (S2, proved):** via TMASS =
(2^N/p^kappa) sum_u prod_j cos^2(pi<u,c_j>/p), Z-CEILING(C) is
EQUIVALENT to bounding the non-trivial smoothness mass SMOOTH <=
(C-1) + C(p^kappa-1)/2^N — i.e. Z-CEILING is a FAITHFUL
RESTATEMENT of this node's named non-local input, not a weaker
stepping stone. E[SMOOTH] = (p^kappa-1)/2^N exactly (the ensemble
form is proved and inert). The named decisive computation:
N = 32 at sigma in [-2, 2] (needs a new algorithm — the MITM
state count 3^16 exceeds the local wall; a Modal/algorithmic
candidate). CATCH on a sibling node applied separately
(tern_master_threshold CZ-M count formula). Source:
notes/pilots_20260808/z_ceiling_assault/ (coordinator-replayed:
RC 20/0; the addendum suite reproduces the record cell and the
count refutation).

## Round-25 addendum (2026-08-09, coordinator-applied on replay: z_n32_band — the named decisive computation EXECUTED)

**The N=32 wall is BROKEN and the ladder verdict is measured: no
cell beats the record (C >= 1.7681 stands), but the reason to
believe C is absolute is WEAKER after this round, because the
census's own growth law missed the N=32 max by 10x and the
matched decay is not statistically significant.**

**The algorithm (BBM, bucket-bisect MITM, new this round):**
buckets are contiguous residue intervals, so for a fixed
first-half partial sum the matching second-half partials are at
most two contiguous ranges of the sorted table, found by bisect —
all R bucket passes cost ONE enumeration, memory drops by an
arbitrary factor, no disk. Measured: 117.5 s and ~50 MB RSS per
N=32 cell (registered bound: < 20 min, < 400 MB). Round 24's
blocker ("3^16 = 43M states — out of reach at 1G by any kappa")
is REPRICED: the wall was memory layout, not arithmetic. Bonus
finding: the unbucketed 18/14 MITM at the SAME op count is ~12x
slower (a 575 MB dict thrashes cache) — bucketing buys speed,
not just memory.

**The grid:** 72 N=32 cells (47 kappa=1 sampled from ~2.1e7
admissible primes; 18 kappa=2; kappa=3,4 EXHAUSTIVE) + the
EXHAUSTIVE 1305-cell N=16 in-band line + 19-cell N=8 line.
Max CRATIO at N=32: 1.4210954721 (TMASS = 22852627/2^23,
p=4683696257, sigma=-0.125). Z-FLOOR: 0 violations anywhere.
Verification: 15/15 escape tests (incl. the round-24 record
replayed exactly: TMASS=159/64, CRATIO=1.7680688810, NKER=289);
33/72 N=32 cells re-derived by a disjoint-internals variant with
0 disagreements, covering ALL top-12 cells; the record cell is
THREE-WAY derived (identity/256, even-odd/181, and the
coordinator's reversed/101 replay — AGREE). Honest tail: 39/72
cells are single-algorithm; the independent unbucketed MITM
completed zero N=32 cells under contention.

**The ladder verdict (all numbers coordinator-replayed from the
seeded analysis):** raw max decays 1.7681 -> 1.4211, BUT (i)
sigma-stratified + M-matched against the exhaustive N=16 line,
the N=32 max sits at quantile 0.2278 — mild decay, NOT
significant at 5%; (ii) the M-normalised N-exponent is -0.026,
OUTSIDE round-24's registered window [-0.30, -0.12] on the
less-decay side; (iii) the sd(CRATIO) decay IS significant
(quantile 0.0000) while the max decay is not — THE BODY SHRINKS,
THE TAIL DOES NOT; (iv) round-24's SD-based extreme-value law
predicted MAXCR-1 = 0.041 at M=47, measured 0.421 — 10x under.
**Round-24's P4d extrapolation ("C = 1 + o(1) with grotesque
room") is NOT SUPPORTED at N=32.** (v) The heuristic band
extrapolation EVX(47 -> 2.1e7) puts the N=32 band max at ~1.88,
ABOVE the N=16 record — an extrapolation, not a measurement, and
exactly the direction that reopens the death question.

**Mechanism (weight enumerators, AU exact to U<=12):** the
kappa=1 distribution is a tight body (46/47 cells in [0.95,
1.11]) plus rare spikes set by low-weight arithmetic accidents:
record cells have UMIN=9 vs typical 11, and weights <= 12 supply
48% of the record's excess mass. Every exact AU[U] is a multiple
of 64 — the mu_64 negacyclic-orbit invariant (an independent
structural check). The correct UMIN threshold is
C(32,U)2^U >= 64p (orbits, not vectors) — which lands exactly at
the measured 11 and explains the registered miss. The max is set
by a non-Gaussian spike process the SD-based law cannot see.

**Hedged lead (kappa direction):** RC's low-weight protection
UMIN >= 2^{2(N-sigma)/(kappa N)} DECAYS in kappa (4.0, 2.0, 1.56,
1.39 for kappa=1..4); kappa=2 produced 1.3887 from only 18 cells
vs kappa=1's 1.4211 from 47. The official row has kappa = R >> 1.
Confounded by tiny cell counts at kappa>=3 — a lead, not a
result.

**Named follow-on (replaces "wider ladder"):** UMIN-TARGETED
SPIKE SEARCH — enumerate N=32 cells by weight-9/10 orbit count
via the weight enumerator (~3x a cell) instead of waiting for a
47-cell sample to hit a spike; plus the declared post-hoc
exhaustive kappa=2 band (266 cells, never run). Pilot
prediction record: 9 registered predictions HIT (incl. the
Tier-2/3 prime bands EXACTLY), 6 MISSED — including its own
headline (P-Z1 predicted max 1.041, measured 1.4211) — all
reported plainly. Scope: every number is about the FORM of
Z-CEILING on toy families; the f2 calibration clause binds; no
status change. Source: notes/pilots_20260809/z_n32_band/
(REPORT.md, FABLE_AUDIT.md; ez 15/15, seeded analysis, and the
record cell replayed by the coordinator).

## Round-26 addendum (2026-08-09, coordinator-applied on replay: umin_spike_hunt — CONJECTURE Z-CEILING's ratio form FALSIFIED on its own pinned family)

**BOTH registered kill outcomes FIRED. The record: CRATIO =
5.8131644651 exact at the M4/I2-RSET cell N=32, kappa=1,
p=4337074369, sigma=-0.0141 (TNUM=49692303616, NKER=551489) —
FOUR-WAY derived** (the pilot's identity/256, even-odd/181,
reversed/101, plus the coordinator's stride-5/113 — all
exact-integer identical) **and the weight-5 kernel witness
(support {0,1,3,12,25}) verified DIRECTLY by coordinator code
independent of the sieve. 119 of 124 exactly-computed kappa=1
cells exceed 2; the N=16 record 1.7681 is beaten 3.3x; round-25's
sample max 1.4211 by 4.1x. Z-FLOOR holds at every one of 292
cells — the FLOOR stands, the CEILING falls.**

**THEOREM RS (new, the converse of THEOREM RC — an IFF, giving
the sweep recall 1.000 BY PROOF):** for 2N a 2-power and
2N | p-1, the cell carries a ternary kernel vector of weight U
iff some ternary f (deg < N, weight U) has p | Res(Phi_2N, f).
((<=): Res = prod_{k odd} f(theta^k), so some f(theta^k) = 0;
g(x) = f(x^k) mod (x^N+1) is ternary of the SAME weight for odd
k, and g(theta) = 0 — coordinator-verified argument.) The sweep
is over f, NOT over p: one enumeration decides every prime in
the band. Measured recall control: the N=16 whole-band census
(1305 cells, U <= 12) agrees with the reference weight
enumerator with 0 mismatches; the N=8 band likewise; the power
control hit exactly the banked AU profiles (64/32/0/0). Cost:
4.4 microseconds per admissible prime vs ~200 s/prime by direct
enumeration (~4e7 speedup).

**THE CENSUS (a census, not a sample — all 2.12e7 admissible
kappa=1 primes in [2^30, 2^34] decided):** UMIN <= 3 empty BY
PROOF (Res <= 3^16 < 2^30); UMIN = 4: 0; UMIN = 5: 90 (the
whole stratum computed exactly by BBM — min 1.3369, median
3.6476, max 5.8132); UMIN = 6: 2,395; UMIN = 7: 25,105; total
0.130% of the band. kappa=2: exactly ONE in-band prime (p=33409)
carries weight <= 7; the exhaustive 266-cell sweep (declared
post-hoc in round 25, never run) was 168/266 at pilot report
time and was COMPLETED BY THE COORDINATOR from the pilot's
resume machinery — [completion recorded in FABLE_AUDIT.md].

**THE MECHANISM — why no absolute constant can exist:** the
ternary kernel is the ternary part of an IDEAL (ker = P
intersect T), so one weight-U element drags in its ternary
multiples: TMASS >= ~(1 + 2^{1-U})^N. THEOREM RC pins
U_min -> 5 on the band while N grows, so the guaranteed mass
grows GEOMETRICALLY in N against a bounded normaliser. Measured
ladder (minimal-weight strata exhaustive): band max 0.944 (N=8)
-> 1.7681 (N=16) -> >= 5.8132 (N=32) — factor >= 3.3 per
doubling, vs the law's 2.64. **The absolute-constant (ratio)
form of Z-CEILING is dead on the pinned family: C(N) grows
without bound.** (The N=32 value 2^2.54 has not itself crossed
the round-23 finite-target line 2^4.77 — it does not need to:
the application required the bound at the official row's N, and
N-uniformity is what the mechanism kills. Extrapolation beyond
N=32 is a two-point law + mechanism, labelled as such.)

**ROUND-25 VERDICT SUPERSEDED, and its tension resolved:** the
round-25 ladder verdict ("matched decay not significant"; EVX
extrapolation ~1.88) was reading the BODY, and the round-25
report itself flagged that the SD-based law cannot see the
spike process. Correct: 0.130% of the band carries the mass
(4e-6 at U=5); a 47-cell sample had expectation 2e-4 of hitting
the U=5 stratum. The tail is ARITHMETIC, not statistical. The
round-24 repricing "C >= 1.7681 with 3.95 bits headroom" is
superseded by C >= 5.8132 at N=32 and no absolute C.

**WHAT SURVIVES:** THEOREM Z-FLOOR (0 violations, 292 cells);
THEOREM RC; THEOREM RS (new); the negacyclic object and its
dictionaries. **WHAT THIS MEANS FOR THE F2 TERMINAL
[SURFACED]:** round-23's S2 identified Z-CEILING with the
non-local smoothness input; with the ceiling dead on the pinned
family, the terminal's smoothness input again has NO NAMED ROUTE
(strengthening the round-19 verdict). The mass form's 46-bit
knife edge and the tail-count criterion are unchanged. Scope:
every number is toy-family FORM; the f2 calibration clause
binds; nothing here is about Z_1 at the official row.

Pilot record: 7 predictions HIT / 5 MISSED, misses first —
including its own headline (registered max window [1.75, 3.05];
measured 5.8132: direction right, magnitude missed because the
registered additive predictor was structurally wrong; the
multiplicative ideal mechanism was found in the data and is
declared unregistered). Its escape replays initially resumed
from checkpoints (a checkpoint sum, not a derivation) — caught
by the pilot itself and re-derived from scratch. Coordinator
replays: the record four-way + direct witness; the kappa=2
completion. Source: notes/pilots_20260809/umin_spike_hunt/
(REPORT.md, FABLE_AUDIT.md; HITS/CANDS/CELLS26 tsv data;
N16_CENSUS.json).
