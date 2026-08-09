# integer_code_distance_cert

- **status:** TARGET
- **closure:** open row certificate
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

For every row that a downstream prize certificate assigns to this lattice
route, pin the prime field, quotient order and root, class cell and its exact
cardinality, support bound `2l'`, explicit integer kernel matrix, and allowed
cyclotomic-relation basis. Then bank a machine-checkable certificate that no
non-cyclotomic ternary kernel vector of weight at most `2l'` remains and check
that the certified cell cardinality is greater than the row budget `B*`.

There is no hidden finite registry of official row primes. Closure must
therefore be either uniform over every admissible row assigned to this route,
or explicitly exhibit-scoped with every downstream claim narrowed to the same
field. Exact finite search proves procedure totality but does not prove that
its verdict is collision-free. The C-4 toy anchor is a format exemplar only.

The proved `integer_code_distance_high_field_folded_box_exclusion` pays the
complete order-128 folded cube whenever the row characteristic satisfies
`p>253^32`: every ternary kernel vector is then antipodal/cyclotomic. This is
an exact branch theorem, not a promotion. Lower characteristics, other
quotient orders, the universal row assignment, and the row's value-set budget
remain open.

## Attack surface

Before computation, bind the literal row payload and prove that its class count exceeds `B*`. Apply the high-field order-128 theorem where available. On a residual pinned row use: (1) pseudo-Boolean/SAT with proof logging (VeriPB-style); (2) MITM bands as baseline; or (3) LP/Delsarte. A collision verdict is a valid route outcome but does not close this no-vector target. E24's BKZ hunt is search evidence only.

## Falsifier

a non-cyclotomic ternary kernel vector inside the declared support bound, or a declared cell whose exact cardinality is at most `B*`

## Addendum (2026-08-07, round-21 closability probe — NOT closable via the transported distance laws)

Probe verdict (notes/pilots_20260807/red_closability_probes/): the
Z-1/Z-2 transport CANNOT close this node — hypotheses H1-H3 hold
and the shift-0 scope check PASSES, but the system supplies ell = 1
odd-power condition against the ell = 65 the threshold needs, and
ell = 1 is PERMANENT: multi_multiplier_reduction (REFUTED) proves
the k-multiplier residue matrix is a rank-1 outer product for every
k. Z-2 at ell = 1 yields only "weight >= 3", attained. The PROVED
high-field branch (p > 253^32) covers 5.02% of the e = 1 prime-row
log-window; the four pinned Proth exhibits sit 84.5-88.5 bits below
it. This node remains the genuine open content of the (re-posed)
mystery-5/kernel-lattice line.

## Round-22 addendum (2026-08-07, coordinator-applied on replay): exact fold-reduction thresholds — universal at toy scale; the residue is row-unboundedness, not per-row cost

The round-22 ge_floor_falsifier pilot made the certification
threshold EXACT and UNIVERSAL via the fold reduction (K_p has a
non-cyclotomic ternary vector of support <= 2l' iff p | Norm(w) for
a nonzero w in the {-2..2}^h box with ||w||_1 <= 2l'):

- **THEOREM (toy, PROVED-exhaustive):** for every p = 1 mod 16
  above 463249 (full radius) or above 4049 (radius 6), K_p is
  empty of non-cyclotomic ternary vectors; both thresholds
  ATTAINED. For N' = 8: threshold 137. The norm-instrument family
  cannot reach the prize rows: MAXNORM's plausible sharpening
  (base 4(h-1), weakly supported and false at h = 2) gives
  2^255.27 at h = 64 vs the needed 2^250 (base 224.6), and
  TIGHTEMPTY sits within 0.41 bits of MAXNORM at h = 8 — no
  which-primes refinement rescues it. The smallest new theorem is
  a certified lambda1 lower bound on the folded kernel lattice,
  priced in the round-22 lattice_cone_certificate addendum
  (laptop-scale per row at N' = 128).
- This node's "no hidden finite registry of official row primes"
  clause is CONFIRMED as the binding residue: the bad primes run
  up to the threshold with no gap. Per-row certification is cheap;
  the universal form (this node) remains the open content — now
  the CONVERGENCE POINT of three lanes (mystery 5's GE-WEAK,
  round-21 PROBE 1's ell-condition system, and the crossing safe
  side's ternary relation-set weight enumerator, round-22
  bb_nu_transport).
Source: notes/pilots_20260807/ge_floor_falsifier/
(coordinator-replayed).

## Round-23 addendum (2026-08-07, coordinator-applied on replay: ge_lattice_cert + the cw_shared_target qualification)

**THE LITERAL-EXHIBIT HALF OF THE STATUS RULING IS NOW SUPPLIED:**
e1_folded_no_vector_certificate_128_payload is PROVED — a complete
enumeration certificate with a deterministic standalone checker at
the exact pinned field/root (2,061,127,954 nodes, EMPTY;
fail-closed planted control at the same dimension/determinant).
What this does NOT supply, per this node's own ruling: the
family-uniform theorem, the narrowing of consumers to the exhibit
field, or the value-set side. The four deployed Proth prize rows
(167-171 bits, below the 253^32 analytic threshold) now carry
radius-graded complete certificates to support <= 24 (12 swaps —
four times the archimedean-free radius L = 6); their full-radius
cells are priced at 2^60-2^63 (LLL) / 2^38-2^40 (BKZ-90) — the
laptop-scale reclassification holds only above ~242 bits (the
PRICE-CLIFF). The GS-FLOOR obstruction (round-23, proved) shows no
lambda_1-floor certificate exists for ANY basis at admissible
rows: the enumeration is irreducible, only its price moves.
Witness-count note: the round-22 toy thresholds remain ATTAINED;
the attaining sets are full 2h-orbits (16, not 2, at p = 463249 —
CATCH-23A).

**THE CONVERGENCE QUALIFIED (round-23 cw_shared_target):** this
node remains the convergence point of the GE-WEAK / PROBE-1 /
crossing-deep-stratum lanes at the OBJECT level (one functional:
the ternary theta / weight enumerator of K_p), but the round-23
pricing shows the crossing lane's LIVE crux (Acc_shallow +
aperiodic S) does NOT reduce to this object — its only bridge
loses >= 4.565e11 bits at the official row. One object, two
targets: closing this node serves mystery 5's per-row line and
mystery 2's terminal-adjacent form; it does NOT close the
crossing crux.

## Round-24 BOARD EVENT (2026-08-08, coordinator-replayed: kernel_window_hunt): THE FAMILY-UNIFORM EMPTINESS FORM IS FALSE

**Witness of record (REPRO PASS, coordinator-replayed):** at the
BLS-PROVEN 247-bit prime P = 18838259725604806405449165455743336372
0577825648201882790490986150665597569, P = 1 mod 128, P < 2^256:
Norm(w) = P exactly for a box vector with ||w||_1 = 127 <= 2l' =
128, whose ternary lift is a NON-CYCLOTOMIC kernel vector of K_P.
Plus 20,636 W_TOP hits (2,747 stored with all-distinct primes;
probable primes labelled as such). AND the mis-filing catch: the
repo has held EIGHT exhibited (w, p) pairs at N' = 256 (226-255
bits) since July 2026 — the e1_n256 campaign's own audit dismissed
a 248-bit prime as "below 2^250 and therefore harmless", filtering
by PRIZE-INTERVAL membership instead of admissibility; the uniform
form was already dead at N' = 256 on banked evidence.

**CONSEQUENCE:** per this node's own status ruling, the
"family-uniform theorem" branch is CLOSED OFF; the living branches
are (a) EXHIBIT-SCOPED closure with every consumer formally
narrowed, (b) an o(1)-SPARSITY re-pose (untouched — even
supported — by the measurements), or (c) a LARGE-v_2 RESTRICTION:
the generic witnesses have v_2(p-1) = 7 while EVERY pinned/deployed
row has v_2(p-1) in [92, 200] — the witness rows cannot support
the deployed 2^41+ smooth domains, making (c) a real and possibly
defensible narrowing. THE CHOICE AMONG (a)/(b)/(c) IS SURFACED TO
THE USER (genuine consumer-scope decision). Source:
notes/pilots_20260808/kernel_window_hunt/ (repro_witness_proven.py
REPRO PASS; calibration C1-C4 against the round-22 exhaustive
ground truth; coverage 2^22.0 of the box; the novelty subtraction
amended by the pilot itself — the N' = 128 exhibit and the stated
conclusion are new; the forward-direction method and N' = 256
exhibits are prior art).

## Round-25 narrowing decision support (2026-08-09, coordinator-applied on replay: large_v2_hunt)

**OPTION (c) LARGE-v_2 IS NOT VIABLE AS POSED — dead in all three
ways a narrowing can die — and option (b) o(1)-sparsity is
POSITIVELY supported by the same measurements. The (a)/(b)/(c)
choice REMAINS SURFACED to the user; the coordinator's prior
recommendation (c)+(b) is WITHDRAWN in favour of (b) primary,
(a) fallback.**

**(1) Dead by exhibition for every threshold <= 26:** witness
w in {-2..2}^64, |w|_1 = 125, p of 209 bits, p = 1 mod 128,
v_2(p-1) = 26, cofactor 197633, norm recomputed by Bareiss
determinant (independent of the tower recursion), kernel
certificate rho of exact order 128 with odd s = 99. Standalone
zero-import verifier repro_v2_r25.py: OVERALL PASS
(coordinator-replayed), negative controls fail closed on four
corruptions. Best witness within the c <= 2^12 criterion:
v_2 = 25.

**(2) Heuristically FALSE at the registered threshold:** at
v_2 >= 41 the measured bad-prime rate predicts ~2^98
counterexamples in the admissible window (~2^96 in the deployed
band). The h=64 suppression curve is EXACTLY the prime-density
law with K = 1 (the pooled K = 0.736 is an instrument artefact —
cofactor-1 acceptances are pinned by LAW 2 below); the
high-statistics independence test (14.7M incidences, chi^2 =
3.75/8 df, slope 0.3 sigma) bounds any structural per-level
factor to within 4% over levels 7..41. The rung-41 silence is
CALIBRATED UNINFORMATIVE (expected count 0.005) — registered in
advance as not evidence for (c).

**(3) Mechanism PROVED ABSENT:** NORMLAW (three lines, from
ideal-norm factorization: every odd box norm is a product of
p^f factors each = 1 mod N', so Norm = 1 mod N') subsumes the
conductor-128 local-reciprocity route, and the repo's own PROVED
local-norm EQUALITY (e1_n256_local_norm_cofactor_collapse
proof.md:17, Norm(O_K^*) = 1 + 256 Z_2, likewise at conductor
128) means the local norm map is ONTO — local reciprocity gives
v_2(Norm-1) >= 7 and provably forces nothing stronger. Measured:
box norms hit all 1024 classes mod 2^17. No 2-adic/archimedean
tension exists to build an obstruction on (conditioning on
v_2(Norm-1) >= g leaves LOGNORM flat for g = 7..14).

**(4) Not repairable by raising the threshold:** VSTAR ~ 136-139
(the threshold above which zero counterexamples are heuristically
expected; the estimator over-predicts the h=8 toy by 2^2.8,
haircut applied and stated). Any threshold retaining the four
deployed Proth rows (v_2 = 92, 93, 95, 97 per status_ruling
lines 17-19) leaves ~2^45-2^49 predicted counterexamples; the
threshold that works excludes every deployed row and retains only
the E1-128 pinned field (v_2 = 200), which is already certified
per-row. The toy analogue is exact: at h=8 (exhaustive), option
(c) is false at every threshold <= MAXV2BAD8 = 12 — attained by
the Kyber NTT prime 12289 = 3*2^12+1 — and the threshold law
VSTAR = m + log2(#bad * K) = 12.74 matches.

**Support for (b):** bad-prime density in the top window is
~2^-112 — the o(1)-sparsity form is exactly what the measured
suppression law asserts, at every v_2 uniformly (the h=8 census
shows the suppression is prime-density and nothing else: pooled
BADFRAC 0.1115, flat across v_2, chi^2 p = 0.07 stratified).

**NEW PROVED LAW banked (LAW 2, the load-bearing refinement
round 24 flagged):** for h a power of two,
Norm(1 + 2v) = 1 + 2h*v_{h/2} (mod 4h), by Newton's identities
(proved for w = 1 + 2v; general w is a NAMED OPEN GAP).
Machine-checked as an identity with 0 violations at h = 2..64
(coordinator-replayed). Corollaries verified: FAM-B is pinned at
v_2(Norm-1) = 7 identically (3000/3000 + 0 rung-8 events in 7e6
samples); a FAM-B hit with v_2(p-1) >= 8 forces cofactor = 129
mod 256 (360/360 on the banked round-24 witnesses).

**Honest limits:** coverage 2^-124 of the box (silence bounds
only the sampled region); the counterexample counts are heuristic
expectations calibrated at h=8 but extrapolated across the
R/lambda_1 = 1 threshold; box realization of 2-adic classes is
measured only to depth 2^17 (second NAMED GAP). Nothing here
exhibits a v_2 >= 41 witness — it predicts ~2^98 exist. Pilot
self-corrections: 6, all disclosed, incl. its registered
structural fact R0 being false (repaired via residue degrees —
the 536 of the round-22 ground truth are exactly the f=1
stratum of 554). Source: notes/pilots_20260809/large_v2_hunt/
(REPORT.md, FABLE_AUDIT.md; repro PASS, LAW 1/2 identity suite,
and the exhaustive h=8 census coordinator-replayed).

## NARROWING RATIFIED (2026-08-09, user): (b) primary, (a) fallback, (c) withdrawn

**The user ratified the round-25 recommendation: the family-uniform
emptiness statement (FALSE as posed, by the N'=128 witness) is
narrowed to (b) o(1)-SPARSITY as the primary form — bad primes have
density o(1) in every admissible window, uniformly in v_2, as the
measured suppression law asserts (W_TOP density ~2^-112; BADFRAC
flat across v_2) — with (a) EXHIBIT-SCOPED as the fallback (the
per-row certificates: E1-128 pinned field + the four deployed
Proth rows, each certified individually). Option (c) large-v_2 is
WITHDRAWN per the round-25 kill (dead by exhibition, by count, and
by proved mechanism-absence).** The round-26 task of record: pose
(b) in weakest usable form with pre-registered falsifiers (the
b_sparsity_pose pilot). Decision of record for mystery 5's
family-uniform arm; the per-row lane (kernel-lattice certification)
is unaffected.

## Round-26 addendum (2026-08-09, coordinator-applied on replay: b_sparsity_pose — the ratified (b) is a THEOREM at the prize cell, with three teeth)

**THEOREM B1 (PROVED, coordinator-replayed end to end):** at N'=128,
bad primes (rows whose kernel carries a non-cyclotomic ternary
vector, ANY support bound 2l' <= N' via the fold reduction) number
<= 2^135.6034 in W_ADM = (2^128, 253^32], hence density
**<= 2^-93.93 (fully elementary) / <= 2^-106.93 (with the exact
Burnside orbit count over the 8192-element norm-preserving group)**,
uniformly on every v_2-stratum up to **VSPARSE(128) = 113.93**.
Proof = four banked ingredients + one pigeonhole: fold reduction
(kernel_lattice_reframing) + the DLI lane's energy ceiling
(dli_norm_gate_energy_ceiling LN4 — a cross-lane reuse) + pigeonhole
(two prime factors > 2^128 would force Norm > 2^256 = 256^32 —
ZERO-margin but airtight by strictness; the pilot's registered
0.2-0.4-bit margin was WRONG, disclosed) + PNT in AP at fixed
modulus 128. The union-bound ROUTE is prior art in our own repo
(e1_folded_no_vector_certificate_256_payload/retired_proof.md — no
novelty claimed for it); new: the height bound, the exact orbit
count (13.00 bits), the v_2-grading, and a runnable script — which
RESTORES the standing catch-#61 item ("cited script NOT ON DISK").
Consistency: round-25's measured log2 BADCOUNT = 132.0 sits under
the proved ceiling 135.60 with 3.60 bits headroom (a check that
could have failed and did not). Deployed Proth rows (v_2 = 92-97)
are inside the graded theorem with 16.9 bits to spare; the E1-128
field (v_2 = 200) is outside and covered by its per-row certificate.

**THE THREE TEETH (all measured, none hidden):**
**(i) "o(1)" has NO valid asymptotic parameter.** Under the prize's
fixed |F| < 2^256 the bound collapses: 2^-216 (N'=32), 2^-180 (64),
2^-106.9 (128), **2^+42.7 VACUOUS (256)** — and the retired proof's
own heuristic (reproduced: E S_p = 2^63.6 collisions per prime)
says essentially EVERY admissible prime is bad at N'=256. "o(1) as
N' -> infinity" is heuristically FALSE in the fixed window; the
surviving asymptotic reading uses a window growing to MAXNORM.
**SURFACED RE-SCOPE: pose (b) as a NUMERIC PER-CELL bound, not an
asymptotic** (awaits user).
**(ii) (a) and (b) are COMPLEMENTARY, not primary/fallback.** On
the stratum the deployment actually uses (W_DEP AND v_2 >= 92, or
Proth k*2^92+1) the proved bound is VACUOUS by ~62 bits (PI =
2^74.1 vs count ceiling 2^135.6); heuristic density there ~2^-29,
unproved. The deployed rows are exactly where (a)'s per-row
certificates do the work and (b)'s theorem cannot.
**(iii) Governance gap.** status_ruling.md:11-15 admits return to
PROVED only via family-uniform theorem (dead) or exhibit-scoped
certificate; a density theorem has NO SLOT. Banking (b) as the
node's route requires AMENDING THE RULING (precedent one lane
over: e1_official_typicality_or_certificate). SURFACED (awaits
user).

**What (b) buys (consumer bars named per CATCH-24C):** the
row-SELECTION reading — good rows are a 1-eps fraction of every
octave, found in O(1) expected draws, then certified per-row. It
serves generator_economy's universal-closure clause
(statement.md:100-102), NOT lattice_cone_certificate's
per-assigned-row clause (conditional.md:41-45), which only (a)
closes for adversarial rows.

**Falsifier record:** F1 (h=8 exhaustive, full power): 0 LEM
violations; measured toy density 0.00776 vs proved toy bound
0.3385 — non-vacuous at the toy, 43.6x over truth. F2
(Cochran-Armitage trend on BADFRAC8(v)): Z = -0.472 pooled /
-1.336 stratified, NOT falsified; MDE 10.0%/15.6% per v-step at
80% power — resolves round-25's chi^2 p=0.07 as omnibus noise,
not a trend. F4 registered standing: any collision at a deployed
Proth row (heuristic probability <= 4*2^-29) is a >= 2^27
surprise. GUESS-G (a closed form for the LAW-2 bit) REFUTED.

**LAW 2 GENERAL-w: CLOSED (named gap 1 discharged), two ways.**
P1: s(w) = ((Norm(w)-1)/2h) mod 2 is a homomorphism (two lines).
P2 (proved + 0 violations to h=64):
**Norm(w) = 1 + 2h*[sigma(u) + (u^{-1} z)_{h/2}] (mod 4h)** with
u = w mod 2, z = ((w - lift(u))/2) mod 2 — round-25's LAW 2 is the
u=1 case; the whole z-dependence is exactly linear. P2': s(w)
depends only on w mod 4. The residual function sigma has NO
low-degree closed form (exact ANF degrees 2/3/5 at h=4/8/16) but
IS linear in the canonical (zeta-1)-adic digit coordinates:
s(w) = sum eps_k c_k with computed constant tables (0/200
violations at h = 4..32; c_k = 1 for all k >= h-1 at every h
tested). Coordinator-replayed: all zero-violation suites + the
digit tables.

**Box depth (named gap 2): 2^17 -> 2^40, NO structure.** 2^20
samples, tower-recursion norm mod 2^48 validated 0/60 against
exact: full class realization PROVED BY EXHIBITION to depth 2^23
(all 65536 classes hit); realized/available = 1.000-1.014 through
2^40 (a factor-2 gap excluded > 5 sigma at D=40); LAW-1 replay
1048576/1048576. Resolution honestly ends at D~44 (2 sigma).
v_2-uniformity has no hidden 2-adic obstruction to depth 2^40.

Scope: no status flip (the ruling amendment is the surfaced
gateway). Pilot disclosures: registered pigeonhole margin wrong
(0.0000 exact); first Burnside justification wrong (replaced by
exact count); one out-of-dir write (a deterministic escape test
rewrote a banked state file BYTE-IDENTICALLY — coordinator
verified git-clean); GUESS-G refuted; F3 superseded by proof.
Source: notes/pilots_20260809/b_sparsity_pose/ (REPORT.md,
FABLE_AUDIT.md; d1_burnside/d1_prize/d1_toy/d2_law2/d2_digits/
d3-analyse/d4_checks all coordinator-replayed).
