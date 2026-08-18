# C2'' DLI reduced primitive-residue joint reserve

- **status:** see `dag.json`

For every official prize row `R`, use the generated evaluation field and the
packet's state-dependent nested tower. Put

```text
A(R)      = product_j E_U[rho_j],
X_prim(R) = q^(-t+H) W_cen^prim(R)
          = E_U[product_j rho_j]_reduced.
```

First remove every quotient/coset class owned by the structured staircase
column. Charge every primitive noncoset accident at its absolute weight, with
unique first ownership; do not absorb accident mass into an iid-relative
constant. The remaining primitive joint loss satisfies

```text
X_prim(R) <= 2^21 A(R).                             (C2'')
```

The aggregate 21-bit form is primary. No unreduced endpoint, uniform
per-junction bound, or factorization identity is asserted. This is the
successor to the refuted C2 node `dli_level_factorization`. The historical
three-part pose and its first survived adversarial round are recorded in
`../dli_prime_weighted_large_block_support/notes/C2PP_POSED_20260710.md` and
`../dli_prime_weighted_large_block_support/notes/M1_RESULT_AUDIT.md`.

The scope repair is forced by the PROVED node
`dli_unreduced_coset_endpoint_counterexample`: at an explicit admissible
Proth prime, the quotient-periodic central family alone gives
`X_unred>2^126`. It is separately owned and nonprimitive, so it is absent
from `X_prim`.


## Round-23 adjudication addendum (2026-08-07, coordinator-applied on replay: the c2pp_diag F-round 3)

Source: notes/pilots_20260807/c2pp_diag/ (four attack scripts +
results, all coordinator-replayed; REPOSE_C2PP_R3_DRAFT.md).

**THE EVIDENTIARY RESET (the symmetric not-evidence clause, now
binding).** Every banked C2'' number — M1's survival, round 2's
14.53%/85% margin, AND round 3's 482% F-d overflow reading — is a
shallow-tower (t <= 4, n = 32) single-junction measurement
transported to 33 junctions by the uniform x^33 convention. A
single-junction measurement multiplied by 33 is NOT evidence for
this conjecture and NOT evidence against it. This retires the
round-2 margin and the round-3 overflow TOGETHER. (Pro's 2026-08-01
adversarial audit reached the for-direction half independently: the
14.53% margin "is NOT evidence about the true joint ratio"; the
32-wise trap shows any instrument with reach k < 33 is defeatable
by construction at an admissible gate prime. That demotion is now
recorded HERE, on the node — it was previously only in the Pro
response notes.)

**THE THETA KILL (C-3 — fires under the packet's own rules, no new
transport needed).** The pose's insensitivity claim ("results
insensitive for theta in [2,4] at the 8 rows") is REFUTED on its
own 8 rows: F-b's own kill rule on F-b's own search set FIRES at
every theta in {2.5, 3.0, 4.0} (x_max jumps 1.0662 -> 2.2387; score
3.05 -> 38.37 bits = 182.71% of the 21-bit reserve; spread 35.3
bits across the declared-immaterial range). Mechanism: at
(t=2, q=8353) the theta=2 cut classifies two classes with ratios
2.2414 and 2.1429 as accidents (clearing the cut by 0.24 and 0.14);
any theta > 2.2414 returns them to bulk. The 85% margin was
produced by that classification, not by the tower. If any
three-part (coset/bulk/accident) form is ever re-adopted, theta
MUST become an operative pinned constant with a verdict-stability
requirement over its declared range.

**THE SELECTION-BIAS RECORD (C-2, C-4).** All three F-a/F-b/F-c
falsifiers exclude the high-loss cells by three different
mechanisms: F-b's scoring set drops bulk_ratio = 0 rows by
construction (c2r2_local.py:93 `if b > 0` — exactly the 4.25 and
8.40 rows); F-c's rare-window restriction lam_window <= 1/2
excludes the classes carrying lam = 40.72; F-a reads only the
coset-stripped object. Survival of those falsifiers therefore
never scored the high-loss cells.

**THE STATEMENT GAP (C-1).** The `_reduced` qualifier
distinguishing the twice-survived clause (ii) from this node's
wired unreduced claim exists in exactly one line of one script
(m4_assembly_verifier.py:112) and is dropped by the A5 step
(:827-828); it appears in no statement, node.json, or dag surface.
The wired claim X(R) <= 2^21 A(R) is strictly stronger than the
defended clause, and clause (i)'s "budget arithmetic, never
correlation" conflates internal-correlation-freedom (TRUE: the
coset class is internally uncorrelated, iota = 1.0000 at 6/6 rows)
with contribution-freedom (FALSE: conditioning shifts weight INTO
the coset class up to 21.8x; freezing internal means and moving
only weights gives 26-109 bits at the 33x convention). Clause
(iii)'s "counted once" is non-conservative at 2/8 banked rows
(the tower's own window law expects 1343.86 accidents at
(2,8353)).

**THE RE-POSE OF RECORD: C2''-r3 (aggregate, non-uniform,
transport-explicit).** For every official prize row, over the
actual 33 junctions of the official 34-level schedule:

    sum_{j=1}^{33} log2( E_U[rho_j | state_{<j} null] / E_U[rho_j] ) <= 21.

The unreduced consumer form as a genuine junction sum; no
per-junction bound; no clause licenses discarding a column before
the sum. Pre-registered falsifiers: (G-a) a measured junction sum
over >= 8 CONSECUTIVE junctions of a SINGLE tower, with a
separately justified J -> 33 transport, exceeding 21 bits; (G-b)
sum_j log2(omega_j) growing without bound in q over >= 8
consecutive junctions at >= 3 q-scales. Uniform stacking is
excluded on BOTH sides.

**STANDING:** C2'' is UNMEASURED AT ITS OWN QUANTIFIER DEPTH. No
instrument in the repo carries >= 8 consecutive junctions of one
tower; the 32-wise trap sets the bar. The next decisive test is
that instrument (Modal-scale, M1-census-shaped). The only banked
instruments with all-junction reach are the dli norm-gate family
(LN2/OS-2/OS-3 — kills |S_0| < 4 states uniformly; stops at its
own count-bound line). The risk register anticipated this
adjudication (05-risk-register.md: "c2pp reserve break ...
Decision 6 reversed; B-WEAK-direct re-pose from mechanism data") —
Decision 6's wiring is NOT reversed by this addendum (the
conditional route stands; what changed is the EVIDENCE ledger and
the pose of record).

## Round-24 addendum (2026-08-08, coordinator-applied on replay: c2pp_gb_probe — the falsifier set revised; the first non-stacked datapoint)

**G-b IS WITHDRAWN (vacuous in both directions, by theorem):**
omega_j <= 1/P_U[coset column] with a q-FREE denominator
(P_U[S_j empty] = 2^{h_{j+1}-n}, brute-verified), so the junction
sum is bounded uniformly in q by a SCHEDULE constant (2^46 + 256
bits at the official schedule — finite and q-free, so "growing
without bound in q" has no referent; and the official admissible q
set is FINITE anyway). Its silence also says nothing (the ceiling
exceeds the reserve by 3.35e12). **G-a's depth is UNREACHABLE:**
>= 8 consecutive junctions costs 2^203 census states (every extra
junction squares the census); a testable falsifier needs a
reachable depth or an analytic form — the falsifier clause of
C2''-r3 is OPEN for redesign (coordinator: next-round item).

**WHAT THE PROBE ESTABLISHED (J = 4, the deepest exact depth;
positive control 8/8 bit-exact against the banked kernel):**
(1) THE FREEZE LAW: every census freezes integer-identically once
log2 q >= n/t (closed form verified; the constant states carry the
saturated census). The official row has n/t = 256 and log2 q in
[41, 256] — it lives ENTIRELY in the pre-saturation regime,
terminating exactly at the freeze point: any q-growth argument
about the official family lives only there. (2) THE SHAPE:
middle-peaked (the deepest junction is the SMALLEST term at every
depth cell); per-junction charge grows with n (2.66 -> 5.64 ->
6.75 bits at n = 32/64/128; toy scope, no transport). (3) **THE
FIRST NON-STACKED DATAPOINT on the r3 object (GB-5):** R3_W =
11.34 bits over 4 consecutive junctions at (n=32, t=16) vs the
window-scaled reserve 21*4/33 = 2.545 bits — a factor 4.5, with
NO J -> 33 transport licensed and the U-induced skew law declared
(divergence D-10). Not a G-a firing; not comfortable; the object
worth escalating. Source: notes/pilots_20260808/c2pp_gb_probe/
(verify_law ALL CHECKS PASS; analyze criterion scoring;
coordinator-replayed).

## Round-25 addendum (2026-08-09, coordinator-applied on replay: c2pp_falsifier_redesign — C2''-r3 has a POWERED falsifier and it is SILENT; GB-5's 4.5x repriced)

**(1) THE TELESCOPING LEMMA (C25-1, the enabler):**
N_{>j-1} = E_j AND N_{>j}, so the window quantity R3_W is EXACTLY
a difference of two level censuses plus per-level block censuses —
round 24's wall (each junction squares the census) applies to the
WINDOW, not to the LEVELS. Verified by independent brute-force
enumeration of all 2^16 states at four configs (coordinator replay:
PR-A PASS, positive control 8/8).

**(2) THE FALSIFIER OF RECORD (G-c, level-decay exponent) — the
first POWERED registered falsifier this conjecture has had.**
Power-controlled on synthetic true/false worlds BEFORE proposal
(the round-23 lesson executed): detects floor inflation at
kappa >= 1/32 and decay excess at delta >= 0.10; against the
official reserve this makes G-c powered for rows with log2 q <=
247 (F1) / <= 232 (F2) and BLIND at the knife edge (107/2^33 ~
1.2e-8 is unresolvable by any toy — registered in advance).
Coordinator replay: power_results.json IDENTICAL. **VERDICT:
SILENT** — deep-band alpha/T = 0.9953, 0.9969, 1.0097, 1.0668 at
the four well-determined cells (tolerance +-10%). Under the
symmetric not-evidence clause this is a SURVIVED POWERED TEST on
toy families, not uniform-stacking evidence for the official row.

**(3) GB-5's 4.5x IS A SATURATION ARTEFACT (C25-4).** The banked
GB-5 cell (n=32, t=16, R3_W = 11.3367) reproduces bit-exactly AND
is the FULL tower (4 of 4 junctions, not 4 of 33) — but its shape
n/t = 2 is saturated at every admissible q. At the two cells
nearest the official shape (n/t = 16 and 8, deep pre-saturation):
**R3_W = -0.0030 and +0.0004.** The saturated ratio grows ~
linearly in n (4.6e10 at the official shape) and can show nothing
else. The round-24 "first non-stacked datapoint, factor 4.5"
above STANDS AS A MEASUREMENT but its interpretive weight moves
to the saturated regime, which the official row does not occupy.

**(4) THE ANALYTIC FORM LANDS ON THE OFFICIAL LEDGER (C25-2).**
The frozen stratum is exactly the e-periodic stratum (e = n/(2t),
by cyclotomic factorization): Zinf = sigma(u,2T)^e, closed forms
98/98 exact at n in {16..128}, ALL e in {1,2,4,8} (86/98
re-verified independently by the coordinator, 0 mismatches,
timeout-truncated). This stratum IS official_scale.json's coset
stratum: cells 128, size 2^128, probability 2^-2199023255424, and
the coset-term formula all rebuilt from toy censuses (5/5,
coordinator-replayed), and the packet's magic constant is
explained: **107 = e - 21 = 128 - 21 exactly** (C25-6).

**(5) FIRST ESTIMATE OF THE OFFICIAL JUNCTION SUM [law]:**
R3_full ~ -0.0066 bits for every admissible q with log2 q <=
255.9, crossing 21 bits at exactly log2 q = 256 - 107/2^33
(replayed: reserve-break scale 255.999999987544). Labelled [law]
throughout: the closed form extrapolated, anchored by the 5/5
ledger rebuild; the reachable data licenses it for log2 q <= 232;
on (232, 256] it cannot decide; within 107/2^33 of 256 the law
itself says the reserve is BROKEN — precisely where the packet's
two 256-bit rows sit ("exceeds_2^21": true).

**(6) NEW LAWS:** (i) S_inf = 1/ln 2 to full double precision,
hence R3inf_full(n, n/2) -> 0.4427 n (C25-7); (ii) the freeze law
is PER-LEVEL, LamStar(lev) ~ (n/t)c_lev — round 24's log2 q >=
n/t is the lev=0 case; official crossovers 256.0 (lev 0,1) to
2218 (lev 33), so the official row is pre-saturation at every
level (STRENGTHENS GB-3) (C25-3).

**(7) NAMED RESIDUAL OBSTRUCTION:** the freeze-tail cutoff law —
the second census term is not a pure q^{-T} power law; it steepens
near freeze and terminates in an exact integer cutoff (measured
freeze scales 14.5..67 vs naive n/T). Unfitted; the next
theorem-shaped target on this node.

**(8) CATCH C25-5 (constant, sidecar-corrected):**
notes/pilots_20260802/c2pp_nullity_structure/results/
official_scale.json line 83 prints "107/2^33 = 1.24556e-05"; the
true value is 1.245644e-08 (10^3 too large; the FRACTION is
correct, every formula uses the fraction). Sidecar correction
filed next to the file; the banked artifact itself left verbatim.

Scope: no status flip; census evidence is evidence, never proof;
toy-to-official transport of numbers not licensed. Pilot
self-corrections: 7, all disclosed (incl. two spurious-failure
episodes caught by its own registered cautions and an invalid
registered cell dropped as never-measurable, not filtered post
hoc). Source: notes/pilots_20260809/c2pp_falsifier_redesign/
(REPORT.md, FABLE_AUDIT.md; PR-A, power control, analytic anchor,
and 86/98 closed forms coordinator-replayed).

## Round-26 addendum (2026-08-09, coordinator-applied on replay: freeze_tail_law — the named obstruction CLOSED AS A THEOREM; S_inf PROVED; the licensed range extended)

**(1) THE FREEZE-TAIL CUTOFF THEOREM (C26-1, the round-25 named
obstruction, closed).** For n, t powers of two, u = 2^lev,
h = n/2^lev, T = t/2^lev, e = n/2t, prime q = 1 mod n: if
log2 q > B(n,t,lev) = max_v (m_v/g_v)(lev + v + 0.5 log2 m_v)
then Zlev(q) = Zinf EXACTLY. Proof mechanism: a non-frozen state
has Phi_{d_v} not dividing C for some v, so Res(Phi_{d_v}, C) is a
NONZERO bounded integer that q^{g_v} divides (distinct Hensel
roots); Hadamard bounds it. The tail is therefore NOT a steepened
power law — it is a SHORT-VECTOR CENSUS of a rank-e lattice in a
box, terminating at an exact integer. Verified: 419/419 rows (275
banked + 144 new), zero rows frozen-side violations; five exact
integer cutoffs certified predictively (8,279 primes between Q*
and 2^B all frozen, 0 violations). Coordinator replays: the
419-row theorem check (PASS from scratch), and the (32,2,1)
cutoff Q* = 273857 INDEPENDENTLY re-derived by full-box Bareiss
determinant sweep (also reproducing the 1450-norm census).

**(2) L3 NEGACYCLIC REDUCTION (C26-2):** a T=1 level census IS a
skew census on e coordinates (the same mitm_null_count the
junctions use) — 181/181 banked rows bit-exact; state counts drop
(u+1)^{h/2} -> (2u+1)^{e/2} (e.g. 7.0e9 -> 1.19e6), unlocking
cells direct MITM cannot reach. Sharp max-norm law (C26-4):
max |Res(X^e+1, A)| over [-u,u]^e = (e-1)^{e/2} u^e for
e in {4,8} (e=2 exception 2u^2) — reproduces all five cutoff
cells exactly; conjectured beyond e=8.

**(3) FORCED CORRECTION of the round-25 addendum item (7)
(C26-5):** the "measured freeze scales 14.5..67" were NOT
cutoffs — the excess is NON-MONOTONE in q ((64,4,2) is frozen at
2^21 yet non-frozen at 2^21.5 and 2^22; true cutoff 2^27.222, a
6.2-bit understatement; the 34/67 figures were sparse grid points
far above their true cutoffs 2^18.96/2^23.05). "Smallest frozen
scale" was never a cutoff estimator.

**(4) S_inf = 1/ln 2 PROVED (C26-6)** — the summand telescopes
against the factorial: S_K = K - 2^-K log2((2^K)!), then Stirling.
Coordinator-verified (identity to 1e-15, algebra by hand). Mint
of record with the constant explicit:
R3inf_full(n, n/2) = (log2 e - 1) n - (1/2) log2(pi n) + 1/2
+ O(1/n); cross-check at n=16: 4.7575 vs exact 4.74986 (which is
bit-identical to the measured saturated R3 at (16,8,W=[0,1,2])).

**(5) THE LICENSED RANGE MOVES: 232.7 -> 251.1 [law, with a named
caveat].** The 10% tolerance capping G-c's F2 power was
fit-scatter now IDENTIFIED as freeze-tail contamination reaching
3-5 bits BELOW LamStar (C26-9 — also why round-25's alpha fits
scattered). Depth-windowed refits (x <= -5; five cells, two
distinct T, incl. three cells only L3 makes reachable):
eps = 0.0195, licensed log2 q <= 251.1. The G-c undecidable band
shrinks (232, 256] -> (251.1, 256] — ~80% closed. CAVEAT: this
converts fit-scatter into a detection threshold reusing round-25's
delta_det calibration; a clean claim needs power.py re-run on
synthetic worlds at the new tolerance — THE NAMED NEXT JOB, not
done.

**(6) The (232, 256] band by census: UNREACHABLE** (cheapest
official level census 2^4224 states, 2^2176 even under L3; and the
band is DEEP BAND, not tail — the freeze tail occupies only the
last 1.49e-8 of log2 q, exactly the knife edge). C26-7 flag: the
ledger's coset term is a LINEAR model of tail depth and the toys
show true depth EXCEEDS it once positive — precisely the window
where the break constant 107 is defined; flag on the model, no
transport licensed.

Pilot misses disclosed first in its report: PR-6 (registered
refit window wrong by 0.7 — itself the C26-9 finding), PR-6b
(tail slope 2/e refuted; the tail is a censored sample), PR-5
5/7. Deviations: one pre-registration ckpt key-peek disclosed;
three new deep cells rest on L3's 181/181 + two guards each (no
independent MITM — the point of L3), declared. Scope: the theorem
and the identity are unconditional at every scale; the decay
constants and licensed-range numbers are [law]. No status flip.
Source: notes/pilots_20260809/freeze_tail_law/ (REPORT.md,
FABLE_AUDIT.md; P2 419/419, Q* independent, S_inf identity all
coordinator-replayed).

## Round-27 scope correction (2026-08-18, Codex: exact counterexample and ownership repair)

The unreduced reading is REFUTED. At the Proth-certified admissible prime in
`dli_unreduced_coset_endpoint_counterexample`, more than `2^127` central
`t`-null supports are quotient-periodic and their normalized unreduced mass
is greater than `2^126`. Thus neither `X_unred<=2^121` nor the statement
gap's `X_unred<=2^21 A` can be a live prize premise.

This does not refute the primitive route. The consumer packet assigns the
periodic family to the structured quotient column and asks DLI to bound the
remaining primitive core. The pose of record is therefore the reduced
inequality at the head of this file. Rounds 23--26 measured and modelled the
unreduced telescoping object; their exact telescoping, periodic-stratum, and
freeze-tail theorems remain valid decomposition tools, but their survival
and fitted ranges are not evidence for the repaired primitive target.

The next closure action is analytic: express first-owner deletion inside the
telescoping identity and bound the resulting primitive endpoint census. A
new numerical fit to the unreduced level law is out of scope.

## Round-28 exact primitive subtraction (2026-08-18, Codex)

`dli_primitive_first_owner_antipodal_subtraction` closes the first-owner
operation exactly. For a weight interval `I`, let `X_I(n,t)` denote the
normalized `t`-null count before primitive deletion and put
`I/2={c:2c in I}`. At the official even `t`,

```text
X_I^prim(n,t)
  = X_I(n,t) - (q^(t/2)/2^(n/2)) X_(I/2)(n/2,t/2).       (P-SUB)
```

There is no inclusion-exclusion tail: every nontrivial stabilizer in the
cyclic `2`-group contains the antipodal shift. Thus the live C2'' target is
the signed two-scale inequality

```text
X_I(n,t) - (q^(t/2)/2^(n/2)) X_(I/2)(n/2,t/2) <= 2^21 A(R).
```

This is a strict narrowing, not a close. The two unreduced terms can both be
large, so separate upper bounds lose the cancellation. The next theorem must
couple the telescoping censuses at `(n,t)` and `(n/2,t/2)`, or produce an
equivalent positive primitive-residual expansion.

## Round-29 primitive ratio telescoping (2026-08-18, Codex)

`dli_primitive_joint_ratio_telescoping` supplies the positive residual
expansion. Put `t=2^m`; let `Z_j` be the exact `U`-weighted level census,
`B_j` the unconditional junction block census, and `C_1` the first
saturated/coset census. Then

```text
C_1 = Z_0(q,n/2,t/2),
J_prim = 2^(nm)(Z_0-C_1)/(Z_m product_(j=0)^(m-1) B_j).        (PRIM-TEL)
```

The central primitive numerator is no larger than this all-weight primitive
numerator. Thus the remaining C2'' target is the single positive integer
inequality

```text
2^(nm)(Z_0-C_1) <= 2^21 Z_m product_(j=0)^(m-1) B_j.          (C2-INT)
```

Equivalently, when `Z_0>C_1`, its logarithm is the old full-tower `R3` plus
`log2(1-C_1/Z_0)`. This is the required cancellation, made before taking
logs. On the frozen exact bank, 29 of 45 full-tower rows have zero primitive
numerator and the maximum surviving ratio is `1.4166572071` bits. That scan
is stress evidence only; `(C2-INT)` remains open on official rows.

## Round-30 square-root falsifier (2026-08-18, Codex)

The scale-free candidate

```text
J_prim <= sqrt(2n)                                           (SQRT)
```

would specialize to exactly `2^21` at the official `n=2^41`. It was tested
only as a preregistered falsification target, not adopted as a premise.
`notes/pilots_20260818/c2_primitive_sqrt_falsifier/` computes 13 exact
`t=2` towers through `n=256` by arbitrary-precision dynamic programming.
All rows survive. The old `(32,2,5857)` row remains the maximum at
`14680064/5498847` (`1.4166572071` bits); every new `n>=64` ratio is strictly
below one by exact integer comparison.

This identifies a plausible closing scale but proves no `t=2 -> t=2^33`
transport. A proof would need primitive prefix/support-pattern collision
flatness across the complete tower. Failure of that collision estimate, or
one deeper exact row with `J_prim>sqrt(2n)`, kills this route without changing
`(C2-INT)`.
