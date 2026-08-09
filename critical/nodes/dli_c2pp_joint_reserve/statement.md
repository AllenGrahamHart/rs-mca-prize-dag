# C2'' DLI joint reserve

- **status:** see `dag.json`

For every official prize row `R`, use the generated evaluation field and the
packet's state-dependent nested tower. Put

```text
A(R) = product_j E_U[rho_j],
X(R) = q^(-t+H) W_cen(R).
```

Route every quotient/coset class through the exact staircase account. Charge
every noncoset accident at its absolute weight, with unique first ownership;
do not absorb accident mass into an iid-relative constant. The remaining
joint loss satisfies

```text
X(R) <= 2^21 A(R).                                  (C2'')
```

The aggregate 21-bit form is primary. No uniform per-junction bound and no
factorization identity are asserted. This is the successor to the refuted C2
node `dli_level_factorization`. The precise three-part pose and its first
survived adversarial round are recorded in
`../dli_prime_weighted_large_block_support/notes/C2PP_POSED_20260710.md` and
`../dli_prime_weighted_large_block_support/notes/M1_RESULT_AUDIT.md`.


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
