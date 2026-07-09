# F2 flip campaign — log (newest last)

## 0 — 2026-07-09: charter committed

Campaign opened. State at open: floors all HARDENED (F2 ranked #1 by
evidence); high-energy branch closed same day
(f2_effective_energy_dichotomy, printed constants); open content =
branch (b) low-energy/Fourier residual. Ladder L1-L5 pre-registered in
F2_FLIP_GOAL.md; L1 (Fourier spectrum exploration at the F2-A1
calibration family, with its falsifier) is the queued first move.
Termination: T-WIN (u2c PROVED + consumer replay) or T-FLOOR
(pre-registered falsifier, >= 3 scales). Resume pointer:
memory/rs-mca-f2-flip-campaign.

## 1 — 2026-07-09: L1 launched

f2_l1_fourier_spectrum_modal.py (14 cells: q = 97/193/257 x n = 32 x
b = 3..6 + n = 16 contrast). Gates: G1 exact Fourier inversion vs
integer-DP N(0); G2 arc-class partition; G3 the t=2 collision law
(#distinct f-values = n - kappa(-l1/l2), kappa the chord-pair count —
the Chebyshev locus sits in the high-kappa chords, which is the L2
routing seed). Kill criterion pre-registered IN the script header:
gen_max_r > R* = 32 at ALL THREE scales at the common sub-balance cell
b = 3 => F2_L1_FALSIFIER_FIRED (T-FLOOR path). Coset-union context
count fixed to real disjointness enumeration before launch.

## 2 — 2026-07-09: L1 COMPLETE — falsifier NOT fired; L2 pre-registered

F2_L1_FOURIER_SPECTRUM_PASS, 14/14 cells, all gates exact. Results:
falsifier maxima 3.8/6.6/8.4 vs R* = 32 (4-8x under the kill line);
top generic arcs = the MAXIMAL-kappa chords at every cell; generic
median r ~ 0.05-0.3 (bulk flat); kappa_max tracks n^2/q exactly-ish
(10.6->4, 5.3->3, 4->4); inversion gate reproduced the banked b=6
accident family (160 witnesses, digit-exact) and 0 extras at every
sub-balance cell; b=4 N0 = coset-union count (8) at all scales.
Banked: u2c statement addendum + dag_commit + artifact/site.

L2 PRE-REGISTRATION (next move, three parts):
  L2a CHORD-COUNT LEMMA (prove first — standard machinery): kappa(c) =
      #{pairs {x,y} in mu_n : x+y = c} obeys the multiplicative-
      character formula with main term ~ n^2/2q and Jacobi-sum error
      (|J| <= sqrt(q)); exact verifier vs direct counts at the L1 rows
      + printed error constants. Official-row reading must be
      beta-normalized (generated field) per catch #11.
  L2b ARC BOUND VIA MULTIPLICITY FACTORIZATION: generic phase multiset
      = (n-2kappa) singletons + kappa doubles; bound |E_b| as a
      function of kappa and the flat scale. EXPERIMENT FIRST: per-kappa
      stratified max |E_b| at the L1 rows to fit the functional form
      before proving anything.
  L2c ROUTING: inverse-symmetric chords (c in the x + x^{-1} Chebyshev
      locus) route to the PROVED coset/dihedral classification;
      non-symmetric high-kappa chords shown thin via L2a.
L3 REDESIGN (from the L1 datum): absolute inversion is lossy — L3 goes
via Parseval (sum_lambda |E_b|^2 = q^t sum_s N(s)^2): census power =
the SP-shaped second moment (v13 identity family), connecting the F2
lane to the same object as F5 P9. One mechanism, two floors.

## 3 — 2026-07-09: L2b strata — two catches, one discovery; L2a re-posed

F2_L2B_KAPPA_STRATA_PASS (7 cells). CATCH vs L1 reading (i): top-arc
vs kappa NOT monotone (97: kappa=4 beats 5,6; 193/b=6: kappa=3 beats
4) — L1 statement addendum corrected in dag.json. CATCH (ii):
Chebyshev membership does not discriminate at t=2 — L2c's
inverse-symmetric routing hypothesis dropped; re-pose pending L2a.
DISCOVERY: kappa and per-chord maxima are mu_n-orbit functions; the
generic chord space = (q-1)/n orbits (3/6/8 at 97/193/257; strata
partition exact, max=mean inside single orbits). Quotient chord (c=0,
kappa=n/2) dominates every cell, grows with b, and there are only q-1
quotient arcs -> handle exactly in L3's Parseval budget.

L2a RE-POSED (next move): per-ORBIT Jacobi-sum evaluation of kappa
(kappa(c) constant on c*mu_n; compute via multiplicative characters
with printed error) + per-orbit arc-max bound. The orbit collapse
makes L2a a finite computation with a theorem attached, and the
official-row reading goes through the beta-normalized generated field
(catch #11 discipline).

## 4 — 2026-07-09 (late): L2a PROVED, L2b' PROVED — extreme bands paid

L2a (f2_chord_orbit_lemma, F2_L2A_CHORD_ORBIT_PASS, 9 rows, err <=
6e-13 per orbit): exact Jacobi-sum formula, N(c) = (q+1-2m*1_mu -
m*delta + E)/m^2, |E| <= (m-1)(m-2)sqrt(q) with each Jacobi term of
EXACT modulus sqrt(q); manifestly orbit-invariant (detecting
characters trivial on mu_n); reproduces the L2b strata windows.

L2b' (f2_weil_newton_arc_bound, F2_L2B_WEIL_NEWTON_PASS, exhaustive):
supersedes the per-orbit plan with a UNIFORM bound. Dilation identity
p_r(lambda) = e_1(r*lambda) + subgroup Weil (<= 2 sqrt q, any arc) +
Newton majorization => |E_b| <= prod_{r<b}(2 sqrt q + r)/b!. Verified
at every arc of 5 cells (max ratio 0.06). REACH (exact integers):
b* = 5 at ALL official shapes => extreme bands b <= 5, b >= n-5 paid
(~2^107 total vs 2^123 budget at prize-max) — the campaign's first
exact official-row payment. Degree-t remark: t*sqrt(q) verbatim.

LADDER STATE: L1 done; L2a done; L2b' done; L2c dropped (Chebyshev
non-discriminating — L2b catch); L3 = MID-BAND census via Parseval/SP
(census power = shift-pair second moment; the structured arcs must be
subtracted exactly first — quotient arcs grow with b) + the banked
energy dichotomy; L4 explicit BSG constants; L5 assembly. NEXT MOVE:
L3 design note — write the exact Parseval budget split (structured
arcs | Weil-Newton band | mid-band residual) and pose the mid-band
estimate sharply before attacking it.

## 5 — 2026-07-09 (close of day): L3 posed with a proved no-go guardrail

F2_L3_DESIGN.md written (design, pre-registered before experiments):
exact Parseval frame (census power = SP/trade census, v13 strata);
structured arcs (linear = Gauss sums, quotient = double-cover e_b)
enter EXACTLY, never bounded; PROVED NO-GO banked: raw Parseval gives
only N(0) <~ sqrt(C(n,b)) — exponentially insufficient at the window
peak, so any L3 proof must use the specialness of the value 0 (the
coset-union value). Mechanisms pre-registered in order: M1 moment
ladder (2k-th moments + the banked energy dichotomy; L4 constants
feed it), M2 algebraic rigidity (trade-variety route through the
proved rigidity lemmas), M3 sub-balance entropy (the ~2% margin as a
deviation resource at 0 only). Each gets a pre-registered calibration
experiment before proof work. Session totals: 5 log entries, 2 proved
rungs (L2a, L2b'), 2 instruments (L1, L2b strata), 1 no-go, extreme
bands paid at official rows.

## 6 — 2026-07-09 (end of day): M1 calibration PASS — M1 VIABLE

F2_L3_M1_CALIBRATION_PASS (10 cells, exact full-census DP): M2/flat =
0.91-1.17 everywhere (L2-flat); sub-balance maxima Poisson-consistent;
N(0) exactly structured at every cell (coset-union 8s; the 160/64
banked accident families reproduced at above-balance contrast). Per
the pre-registered read: M1 VIABLE — the mid-band splits into (i) the
generic-fiber L2/SP flatness statement and (ii) the exact structured
mass at s=0 (coset-union census + the proved giant-block closure).
DAY TOTALS: 6 green verifiers, 2 proved lemmas banked as satellites
(f2_chord_orbit_lemma, f2_weil_newton_arc_bound), extreme bands PAID
at official rows, 1 no-go guardrail, 2 catches honestly corrected.
NEXT SESSION: M1 proper — pose the generic-fiber flatness lemma
(SP/trade census route) with its falsifier; then L4 constants.

## 7 — 2026-07-09 (final): arc-class recursion PROVED; mid-band drops to t=1

f2_arcclass_recursion (F2_L3_ARCCLASS_RECURSION_PASS, 6 cells, four
identities exact): structured arc classes collapse by orthogonality
to order-1 censuses; exact regrouping N2(0) = mean + p1-excess +
p2-excess + generic mass (signed — observed negative where N2 = 0).
CATCH #3 banked: the design note's "structured arcs exactly
computable" was wrong at official scale; corrected in place. The
mid-band obligation now recurses to t = 1 — the census
#{S : sum(S) = 0} — the mildest possible kernel instance, plus the
generic-class mass (chord-orbit + Weil-Newton at extremes, M1 at
mid-band). p2's census = doubled t=1 on mu_{n/2} (exact double cover).

NEXT SESSION: M1 at t = 1 — pose the flatness/0-pricing lemma for the
linear census with its falsifier; the L1/L2 machinery transfers
verbatim (arcs are 1-dimensional, orbits are mu_n-cosets in F_q^x,
Lemma A gives sqrt(q)+1 there). Then L4 constants. Day-1 close:
3 PROVED lemma satellites, 7 green digests, 3 catches, extreme bands
paid, the heart reduced to its mildest instance.

## 8 — 2026-07-09 (very late): M1-t1 profile run — catches #4 and #5

The t=1 full-band profile experiment fired two catches, both banked:
(#4) the Weil-Newton reach table's "official rows" phrasing computed
at q = mn+1 small-m shapes; F2's official sub-balance rows have
q^t >= 2^n at LARGE t (catch-#11 scale: n = 2^21, q ~ 2^31, t ~ 1e4).
Reach claim quarantined to the printed shapes; official (q,n,t) row
table = session-2 item #1. The three proved lemmas are shape-generic
and stand. (#5) the m=1 anchors (n = q-1 rows) PROVE the mid-band
point: exact identity |E_b| = 1 for all b (factorization through
(1+z^q)/(1+z)) while float partial products reach 2^93 — mid-band
signed cancellation is astronomical; float/absolute Fourier machinery
is structurally blind there. Session-2 machinery must be exact
(integer DP; cyclotomic arithmetic mod auxiliary primes). Valid
small-row data: per-arc mid-band R_mid = 0.0001..1.7 (far below
sqrt-flat) — the arcs themselves are tame; the assembly question is
signed-sum exactness. PROVED anchors banked from the run design: t=1
orbit collapse (census = m orbit values) and the factorization
identity (orbit polynomials multiply to (1+z^q)/(1+z), +-1 flat).

SESSION-2 QUEUE (in order): (1) pin the official (q,n,t) u2c row
table from the consumer chain (b2_modp_giant_extras / catch-#11
numbers) and re-instantiate the Weil-Newton reach exactly; (2) rebuild
the M1-t1 profile in exact arithmetic; (3) the t=1 flatness lemma
attempt with the corrected shape; (4) L4 constants.

## 9 — 2026-07-09 (session close): official shape pinned; extremes EMPTIED

Session-2 queue item (1) executed early: the official (q,n,t) shape
was already banked in SURVEY_X4_CLUSTER — prize-max t*log2(q) ~
2.15e12 > n ~ 1.1e12, t ~ 7e10, window EMPTY at every b (q generated
per catch #11). Consequences, all banked:
- f2_newton_empty_extremes PROVED (three-line Newton + the proved
  complementation): NO t-null blocks at b <= t or b >= n-t — the
  extreme bands are EMPTY out to width ~2^36 each side at prize-max.
- Weil-Newton's F2-official reach is ZERO (t*sqrt q > n): catch #4
  resolved by replacement; the lemma stays for small-t shapes.
- THE REFRAMED HEART: mid-band t < b < n-t, flat mean < 2^{-1e12}
  scale vs budget n^3 — required anti-concentration = fiber-to-mean
  ratio <= ~2^{1.05e12}, i.e. EXPONENTIALLY WEAK. M1's target is any
  sub-double-exponential max/mean bound.
Verification: exhaustive at 6 toy rows (t = 2..5), zero violations.

SESSION-2 QUEUE (updated): (1) DONE. (2) exact-arithmetic mid-band
machinery (catch #5) aimed at the REFRAMED target — candidate first
lemma: a fiber-to-mean bound via the t-condition DP's contraction
(each added power-sum condition divides the fiber by ~q up to bounded
loss — if a per-condition loss factor L is proved, the ladder gives
max/mean <= L^t and ANY L < 2^{(1.05e12)/t} ~ 2^{15} = 32768 wins:
a per-condition loss of 32768x SUFFICES). (3) L4 constants. The
per-condition formulation is the campaign's sharpest posing yet.

## 10 — 2026-07-09 (post-close correction): CATCH #6, self-caught

The empty-extremes lemma's official-row application overclaimed:
Newton inversion is char-limited (needs b < char q), so the empty
bands have width min(t, q-1) ~ 2^31 per side at official rows, NOT
t ~ 2^36. The toy verification rows all had q > n and could not
expose the bound. Corrected in dag.json and the note within the hour
of banking. Two standing consequences for all future mid-band work:
(a) Frobenius redundancy p_{qj} = p_j^q — pose condition systems on
the q-free index set; (b) any p -> e dictionary at indices >= q is
invalid as stated (gap-divisor framings must handle Frobenius
explicitly). Tolerance ~2^{1.05e12} and the per-condition-loss target
~2^15 are UNCHANGED (never used the band width). Six catches today,
four against my own same-day work — the protocol's value in one
number. Session hard-closes here; session 2 opens on the
per-condition-loss lemma with exact machinery and the char-q
discipline now on the record.

## 11 — 2026-07-09 (data coda): per-condition calibration — the lemma
## finds its correct form

F2_M1_PERCOND_CALIBRATION_PASS (7 rows, exact integer DP, measurement
only — no claims banked). RAW pre-registered read returned FALSE, and
the failure structure is the finding: L_obs ~ 1.0 (flat contraction,
far under the 2^15 target) at EVERY bulk cell — (31,30): 1.0/1.0/
1.017/0.819; (61,30): 1.0/1.004/0.991; (97,32): 1.0/1.009/1.309;
(193,32): 1.0/0.988 — while every super-32 value occurs exactly where
the census hits its STRUCTURED floor and stops contracting: (113,16)
and (257,16) terminate at 6 = C(4,2) mu_4-coset pairs (containing the
mu_8-cosets) with L_obs = q = "forced blocks are condition-immune";
(17,16) tail = 2 = the mu_8-cosets at t >= 4. The deviation from flat
IS the floor's structured census, nothing else, at every cell.

SHARPENED LEMMA FORM (session-2 target, now with empirical support at
every measured cell): per-condition EXTRAS contraction —
  (N^(j)(0) - struct^(j)) * q / (N^(j-1)(0) - struct^(j-1)) <= L
with L observed at 1.0-1.3. Proving ANY L <= 2^15 on the extras flips
the floor via the tolerance chain (log #9). The structured column
struct^(j) is exact combinatorics (coset-union census; giant-block
closure PROVED). Machinery: exact DP (the char-q and Frobenius
disciplines from catch #6 apply for j >= q only — irrelevant at j <=
J here). Day-1 truly closes at 10 green digests, 4 proved satellites,
2 anchors, 6 catches, and the heart posed in extras-contraction form
with support at every cell measured.

## 12 — 2026-07-09 (terminal): route R4 banked; session handoff

R4 (Bezout/complete-intersection) added to the target brief: power
sums form a regular sequence; W_j is a complete intersection of
degree j!; torsion-properness (with struct removed — the structured
blocks are exactly the torsion-coset components) gives per-condition
contraction with cumulative loss log2(j!), which fits the tolerance
through j ~ t/2. Splice with R1/R2/R3 for the upper ladder. This is
the fourth named route and the first with a quantified reach.

Session 1 terminal state: u2c red, T-WIN/T-FLOOR unmet, ladder open
at exactly one lemma (EXTRAS_CONTRACTION_TARGET.md: statement,
sufficiency, O1-O3, R1-R4, falsifier) + L4 + L5. All banked facts
carry digests; 6 catches corrected; the campaign resumes there.

## 13 — 2026-07-09/10 (continuation): O1-geometric PROVED; R4 crux posed

The orbit power-sum fact (p_i(y*mu_M) = y^i*M*[M|i], exact at 5 pairs,
digest O1_GEOMETRIC_PASS) gives O1's geometric half: the structured
census is EXACTLY the set of mu_n-torsion points (distinct coords) of
the orbit-type components of W_j, and those components are precisely
the loci where successive torsion intersection is improper. The
extras-contraction lemma is therefore equivalent to: NON-ORBIT
components of the power-sum complete intersection meet the torsion
grid properly (or with per-condition excess <= 2^15). One geometric
statement, Galois/monodromy-amenable, replacing all fiber-counting
formulations. This is the campaign's sharpest object and the sole
remaining mathematical content of F2 (with L4/L5 mechanical).

## 14 — 2026-07-10: crux refined to excess-intersection form

Hand-verified at (b,j) = (4,2): W_2 is IRREDUCIBLE (full-rank quadric
on the sum-zero hyperplane) with the orbit loci as proper subvarieties
— so component-removal language was still too coarse. Final form: the
torsion count = Bezout-proper part + excess intersection supported on
the orbit subloci; the excess IS the struct census; the lemma = the
excess is supported only there with the proper part within
per-condition tolerance. Fulton machinery now applies. Session 2
attacks exactly this statement.

## 15 — 2026-07-10: the extras falsifier instrument, final form — PASS

F2_EXTRAS_FALSIFIER_PASS (7 rows, exact: DP census + struct by DIRECT
j-null testing of all disjoint full-coset unions, cross-cancellation
included — struct = 270 -> 20 at n = 30 shows the full definition
working). RESULT: extras contraction L_x in [0.705, 1.278] at every
level of every row — within 30% of exactly flat — and extras reach
EXACTLY ZERO at deeper levels on three rows (the surviving census is
100% structured: N = struct = 6/2 exactly). Zero falsifier events.
The extras-contraction lemma (excess-intersection crux) now has
complete, exact empirical support: extras contract flat until they
vanish; only structure survives deep conditioning. The campaign's
day-1 record closes with the crux posed (log #14), the instrument
green (this entry), and the proof attempt as the sole remaining
mathematical content of F2.

## 16 — 2026-07-10: ZERO-PREFIX Q EQUIVALENCE PROVED — F2 = kernel instance

f2_zero_prefix_q_equivalence (F2_ZERO_PREFIX_EQUIVALENCE_PASS, two
independent exact DPs, 20 cells): below char q, the F2 level-j census
equals the v13 zero-prefix census (Newton dictionary + divisor
bijection). F2's crux is FORMALLY an instance of the shared census
kernel — the summit architecture is now a theorem, not an analogy.
The excess-intersection statement (log #14) and row-sharp Q at the
zero prefix are two faces of one object; all upstream Q machinery
(PROVED shift-pair strata, BC charts) and F5 P9 apply directly, and
any proof of the crux advances the kernel awaited by F5/F1/F4.
ev edges: -> u2c, -> shared_census_kernel (TARGET).

The campaign's day-1+continuation record now stands at: 6 PROVED
satellites + 2 anchors, 13 digests, 6 catches corrected, 2 no-gos,
the crux in excess-intersection form with a clean final-form
falsifier pass, and the kernel identification. The proof of the crux
— now attackable from the Q side, the geometry side, or both — is
the sole remaining mathematics between u2c and green.

## 17 — 2026-07-10: Pro brief prepared — the delegation lane opens

PRO_FLOOR_2_F2_CRUX.md written in the DLI-CLOSE format (per the
floor-campaign report's standing recommendation): the crux in both
faces, the do-not-reprove ledger, both no-gos, the exact empirical
support, the immutable falsifier, and three ordered attack surfaces.
The brief is self-contained for any strong prover (Pro thread, a
fresh Claude session, or Codex after F3). With this, every lane the
campaign can open is open: the proof attempt (two faces), the
delegation brief, the instrument (green), and the assembly plan.
u2c stays red until one of them lands the crux.

## 18 — 2026-07-10: FULL-LADDER DICTIONARY PROVED — catch #6 dissolved
## at the dictionary level

f2_full_ladder_dictionary (log-derivative identity, five lines,
char-free; exhaustive two-branch verification, 750k+ subsets, 10
cells, five with t > q): t-null <=> reversed-locator coefficients
vanish at the q-free indices <= min(t,b); q-multiples exactly free.
The official F2 object is now, by theorem, the census of degree-b
divisors of X^n - 1 with coefficients vanishing on the q-free indices
<= t — the divisor/Q frame covers the WHOLE official ladder. Both
crux faces upgraded; effective condition count for L5 pinned exactly.
The Pro brief's FACE B should be read with this upgrade (brief
pre-dates it by one entry; the target file remains authoritative).
Campaign ledger: 7 PROVED satellites + 2 anchors, 15 digests.

## 19 — 2026-07-10: reformulation closure — the frames round-trip

Probed the unit-group face: ell*_S * ell*_{D\S} = 1 - X^n (exact,
one line); t-null <=> ell*_S is a q-th power in U_1/U^q mod X^{t+1},
an elementary abelian q-group of dimension d = #q-free indices <= t.
RESULT: the frame ROUND-TRIPS — the group coordinates are exactly the
q-free power sums (via our own log-derivative identity), so the
subset-product-in-q-group census IS the q-free Vandermonde subset-sum
census. No new leverage; banked as a documented closure so future
sessions do not re-walk the loop. The reformulation space around the
crux is now closed under: fiber-counting <-> gap-divisor <->
excess-intersection <-> zero-prefix Q <-> unit-group q-th-powers —
five faces, one irreducible object. The crux is confirmed
kernel-hard; the open lanes are the two proof faces (Fulton; Q
machinery), the delegation brief, and nothing else.

## 20 — 2026-07-10: EMPTY BAND UNCONDITIONAL — catch #6 superseded

The squarefree/p-th-power argument (via the full-ladder dictionary):
b <= t forces ell*_S in F_q[X^p] = a p-th power, but ell*_S is
squarefree => b = 0. The empty bands have FULL width t (~2^36/side at
prize-max) in any characteristic — the original width claim restored
with a correct proof; catch #6's char-limited version superseded.
Decisive test where the Newton proof was silent: F_25 (p = 5, n = 24),
b = 6/7/8 > p-1, 1.2M subsets — dictionary (p-free form) exact, zero
t-nulls (F2_UNCONDITIONAL_EMPTY_BAND_PASS). Char-p precision banked on
the dictionary (official extension-field rows: free indices are
p-multiples). Ledger: the arc from catch #6 (overclaim) -> correction
-> stronger unconditional theorem is the falsification protocol's
ideal trajectory, completed within one campaign day.

## 21 — 2026-07-10: Bezout certificate PROVED (face-A structure)

f2_bezout_certificate: differentiating ell*_S ell*_{S^c} = 1 - X^n
with both derivatives divisible by X^t (dictionary + complementation)
gives U ell*_{S^c} + V ell*_S = -n X^{n-1-t} with UNIQUE
degree-bounded cofactors — every t-null pair is an X-power Bezout
pair of divisors of 1 - X^n. Exact on all 52 known nulls (3 cells).
Honest labels: structure for the face-A rigidity route (the
certificate parametrization), NOT count progress; naive
Mason-Stothers on the relation is vacuous (checked: needs t > n-1).
Eighth proved satellite. The crux remains the sole open event.

## 22 — 2026-07-10: ladder amendment — L4 de-scoped; critical path = CRUX + L5

Charter amended per its own supersession rule (dated, in place): the
T-WIN assembly as it now stands (unconditional empty band + crux +
exact struct + p-free condition count + consumer replay) references
no energy argument, so L4 (explicit BSG constants) is needed only if
crux route R2 wins — de-scoped to route-R2 support. The declared
critical path shortens to exactly two items: PROVE THE CRUX, run L5.
Nothing else stands between u2c and green.

## 23 — 2026-07-10: route R5 posed — sparsity / vanishing sums at the
## mid-band's lower edge

At b = t + k the dictionary makes ell*_S (t/p + 1 + k)-sparse with
t + k roots in mu_{2^s} — the crux's lower edge is a SPARSE-POLYNOMIAL
ROOT-COUNT problem on 2-power roots-of-unity groups, where the
binomial-product exceptions (Chebotarev caps prime n at s - 1; the
2-power subgroup structure admits more) are exactly the coset-union
blocks. k = 1 re-derives the proved (t+1)-support rigidity. Target
theorem + pre-registered falsification test recorded in the brief
(R5). This is the fifth route and the first that engages the 2-power
domain structure specifically — the vanishing-sums literature
(Coven-Meyerowitz-adjacent) is its toolbox. Next cycle: run the R5
falsification test before any proof work.

## 24 — 2026-07-10: R5 falsification test PASSED — the dichotomy is real

F2_R5_SPARSE_ROOTS_PASS (10 cells, 200k samples, exact evaluation):
NON-COLLAPSIBLE s-sparse functions on mu_{2^k} carry 2-5 roots at
every cell (s-scale, flat as n grows 16 -> 128; p999 = 2-4);
COLLAPSIBLE samples (exponent-diff 2-power gcd with n — the
binomial/subgroup channel) alone reach n-proportional counts (16 =
n/4 at (193,64)). One flagged event honestly classified: (97,16,s=4)
has n/4 = s = 4 — a threshold-scale collision, not an n-proportional
phenomenon; zero events at every n >= 32 cell. READ: R5's target
dichotomy (generic sparse => O(s) roots; many roots => collapse) is
empirically exact, and the non-collapsible maxima hugging s+-1
suggest near-Chebotarev behavior at 2-power n away from collapse.
R5 is now the LEADING route: its target theorem ("an s-sparse
polynomial with > R(s) roots in mu_{2^k} has exponent collapse")
would close the mid-band's lower edge for b - t up to the sparsity
threshold, with the k = 1 anchor already proved (support rigidity).
Next: attempt the R5 theorem via the 2-adic exponent filtration.

## 25 — 2026-07-10: R5 theorem state — s=3 = generalized chords; lift no-go

Two banked facts from the R5 proof attempt. (a) REDUCTION: the s = 3
non-collapsible instance is exactly the generalized chord problem —
roots are torsion points (x^{d2}, x^{d3}) on a line; L2a's Jacobi
machinery is its toy-scale theory; general s reduces via the singular
exponent matrix to VANISHING SCHUR POLYNOMIALS at torsion points
(generalized Vandermonde = Schur x Vandermonde, distinct roots kill
the Vandermonde factor). (b) NO-GO #3 (quantified): Teichmuller-
lifting roots to char 0 to import Lam-Leung/Mann fails — S != 0 in
Z[zeta_n] vanishing mod a prime above p gives only |N(S)| >= p
against a norm bound exp(phi(n)|lambda| log s) >> p at every official
shape; the char-q effects are real (data: nc maxima = s+1 exceed
Chebotarev's char-0 cap s-1). The R5 theorem is its own problem; its
attack objects are now: the generalized chord counts (s=3, Jacobi-
exact at toys) and torsion vanishing loci of Schur polynomials
(general s). Campaign totals: 3 no-gos, 5 routes, R5 leading with
its first reduction chain banked.

## 26 — 2026-07-10: R5 s=3 rung PROVED (generalized chord lemma); catch #7

f2_generalized_chord_lemma (ninth satellite): Z <= d(sqrt q + 3) for
every 3-sparse polynomial on mu_n — collapse factorization (scale-
free) + exact ambient-annihilator Jacobi formula (digit-exact, 6
rows) + the gcd-1 sqrt(q) bound. CATCH #7: first derivation used the
product-subgroup annihilator; the verifier refused it (formula
overcounted 6-48x); corrected to the ambient group and passed exactly
— the seventh catch, and the fourth caught BY a verifier before
banking. R5 status: s = 3 rung proved with its exact template
(annihilator + Jacobi) ready for the s-induction; official mid-band
still needs the algebraic route (sqrt q astronomical there, as
known). Next rung: s = 4 via the same template or the Schur-vanishing
formulation.

## 27 — 2026-07-10: adversarial max EXHAUSTIVE — s-scale truth confirmed

F2_R5_ADVMAX_PASS: over 7.2M exhaustively enumerated gcd-1 3-sparse
instances (a1 normalized): Zmax = 3 at (17,16), 4 at (31,30), 4 at
(97,32) — s to s+1, with the sqrt(q) tail PROVABLY ABSENT at these
rows (the counting bound permitted ~13 at (97,32); exhaustive truth
is 4). Witnesses banked: (1,2,1,6), (1,5,2,9), (1,14,2,9). READ (per
pre-registration): the s-scale conjecture is adversarially supported
— C(3) <= 4 exhaustively; C(4) <= 5, C(6) <= 5, C(8) <= 4 sampled.
The R5 target theorem is now maximally supported in the form:
NON-COLLAPSED s-SPARSE POLYNOMIALS HAVE <= C(s) ~ s ROOTS IN mu_n —
a q-blind statement demanding an algebraic proof, which is precisely
what the official shape needs (sqrt-q counting is structurally
insufficient there). Proof targets, ordered: C(3) <= 4 exactly (the
base case, three exhaustive rows as test oracles + witnesses for the
extremal structure); then the s-induction via the squaring recursion
(E/O split — sparsity doubles per level, but C(s) ~ s absorbs it if
the recursion is entered with the collapse channel already factored).

## 28 — 2026-07-10: extremal census — proof guidance + a symmetry no-go

F2_R5_EXTREMAL_CENSUS_PASS (full enumeration at 3 rows): the maximal
root-count instances form FEW exponent orbits at the strict row
((97,32): only (1,15) and (1,18) achieve Z = 4; 1536 instances) but
scatter more at looser rows (8 orbits at (17,16) where Zmax = 3 = s).
NO-GO #4 (small): extremal root sets have NO inversion or negation
closure (0.00 at every orbit of every row) — symmetry-classification
proof shapes for C(3) <= 4 are excluded; the proof must handle thin,
asymmetric extremal families. Root index-difference multisets banked
per orbit for the extremal-structure analysis. C(3) <= 4 remains the
posed base lemma, now with: exhaustive oracles (3 rows), the full
extremal atlas, a symmetry no-go, and the ambient-annihilator exact
formula as the analytic handle. This is the state handed to the next
prover: one small q-blind lemma, maximally instrumented.

## 29 — 2026-07-10: C(3) = 4 FLAT ACROSS FIVE SCALES (exhaustive)

F2_R5_C3SCALE_PASS: exhaustive-up-to-symmetry (mu_n-action transversal
— every orbit covered, overcount harmless for a max) at n = 64
(q = 193, 2976 exponent pairs) and n = 128 (q = 257, 12096 pairs):
C(3) = 4 at BOTH. Five-scale table: n = 16/30/32/64/128 -> C(3) =
3/4/4/4/4 — flat across three octaves, at 2-power and non-2-power n,
across four fields. The R5 base lemma 'a non-collapsed trinomial has
at most 4 roots in mu_n' is now exhaustively true at every tested
scale and its proof is the campaign's single sharpest open item —
q-blind, n-uniform (empirically), with the full extremal atlas,
witnesses at each scale, a symmetry no-go, the collapse
factorization, and the exact annihilator formula all banked around
it. Everything the proof needs, short of the proof.

## 30 — 2026-07-10: the CANONICAL FORM of the base lemma; catch #8;
## cross-lane convergence with F3

The coefficient-elimination reduction: x, ax, bx are co-roots of a
trinomial iff phi(a) = phi(b) with phi(alpha) = (alpha^u - 1)/
(alpha^v - 1), PROVIDED the common value is nondegenerate (not in
{0, 1, inf}: c = 1 is the line-through-origin case — no trinomial
with constant term realizes it; c = 0/inf are binomial degenerations).
CATCH #8 (fifth machine-caught pre-banking): the first form omitted
the degeneracy exclusion — fibers at c = 1 have size up to n/2 - 1
(gcd(v-u, n) structure) and the naive check MISMATCHED 7-63 vs 2-3;
with the exclusion: MATCH at all five scales (2/3/3/3/3 = C(3)-1),
witnesses aligned with the extremal census orbits. FINAL FORM of the
base lemma: phi_{u,v} takes no nondegenerate value more than 3 times
on mu_n (non-collapsed u, v). Cross-multiplied, equal fibers are a
6-TERM VANISHING RELATION in two torsion variables — the SAME object
class as Codex's banked F3 char-0 work (Conway-Jones route, 6-term
sums): the F2 and F3 campaigns converge on one core object. The
c = 1 degenerate fiber's n/2-size is itself the collapse channel
seen through phi — the dichotomy in one picture.

## 31 — 2026-07-10: family-closure reconnaissance — the half-coset
## collapse mechanism; induction design constraint banked

Proof design for the canonical lemma: induction on n via the square
map, function family closed under the E/O recursion = the sign family
{(a^u - eps)/(a^v - del)}. FAMILY TEST RESULT: the uniform 3-bound
FAILS naively — members like (u, v, eps, del) = (1, n/2+1, +1, -1)
have fibers of size n/2, mechanism fully explained: on the coset
a^{n/2} = -1 the function collapses to a CONSTANT (half-coset
collapse; witness family explained in closed form at every scale
16/32/64/128). DESIGN CONSTRAINT (not a no-go): the family's
degenerate-value set is a computable per-member ledger generated by
sub-coset collapses — themselves structured-channel phenomena; the
induction hypothesis must be 'fibers <= 3 OUTSIDE the member's
collapse ledger', with the ledger's own contributions routed to the
struct census. The reconnaissance prevented a mid-proof death; the
design is now: (1) formalize the collapse ledger per family member;
(2) verify the ledgered uniform bound empirically; (3) then the
recursion step. The campaign's next session opens at step (1).

## 32 — 2026-07-10: the ledger law + the flat-C falsification arc

Three results in one cycle, all machine-gated. (1) THE COLLAPSE
LEDGER LAW (formalized, closed form): psi_{u,v,eps,del} is constant
exactly on cosets c*mu_d with d | (u-v) and c^{u-v} = eps/del; ledger
values = psi({z : z^{u-v} = eps/del}); UNIFIES catch #8's c=1
exclusion and the half-coset collapse as one law. (2) LEDGERED BOUND:
holds (<= 3) at n = 16/30/32/64; VIOLATED at n = 128 (shifted member,
4) and decisively at n = 256: canonical max = 6 (m=1) / 4 (m=3) —
FLAT-C(3) IS FALSIFIED; growth is slow and field-dependent (at
n = 128: m = 2 -> 3, m = 6 -> 4, m = 9 -> 3; not monotone in m).
(3) RE-POSED TARGET (the application never needed flat): C(3; n, q)
<= slowly-growing (observed <= 7 through n = 256) vs per-condition
tolerance ~2^15 — four orders of margin. The base lemma is now:
non-ledger fibers of the sign family are polylog(n)-bounded (or any
bound << 2^15 at official n) — weaker to state, easier to prove, and
fully sufficient for the mid-band lower edge. Protocol note: this
cycle falsified the campaign's own five-scale-supported conjecture by
pushing one octave and one field further — exactly why the laws say
measure before proving.

## 33 — 2026-07-10: growth-curve RESOLVED — flat in the large-field
## regime, which is the official regime

n = 512 (q = 7681, m = 15): canonical max = 3, shifted = 4 — the
bound DROPS BACK one octave above the falsification point. Full
curve: the fiber max anti-correlates with m (m=1: 6/7; m=2: 3/4;
m=3: 4/5; m=6: 4/4; m=9: 3/3; m=15: 3/4) — the n=256 jump was a
SMALL-FIELD effect (q barely above n: Weil-error-sized coincidences),
not n-growth. THE OFFICIAL REGIME (generated field astronomically
larger than n) IS THE FLAT REGIME. Re-posed target, final form:
LARGE-FIELD FLAT BOUND — C(3; n, q) <= 4 for q >> n (empirically
exact in-regime through n = 512), with the mechanism: at large q the
per-fiber counting error is sub-unit, so all observed solutions are
algebraic/torsion-structural — the proof should classify q-robust
solutions of the 6-term torsion relation. The falsification arc
(flat -> falsified -> regime-restricted flat) took three cycles and
left the target strictly better calibrated than the original guess.

## 34 — 2026-07-10: CHAR-0 CLASSIFICATION PROVED — the base lemma's
## char-0 half is closed; official conjecture sharpens to C(3) <= 2

f2_char0_sixterm_classification (tenth satellite): over Z[zeta_{2^s}]
the 6-term coincidence relation has only ledger/degenerate/diagonal
solutions — Lam-Leung pair decomposition + all six matchings
case-checked; verified exactly in Z[x]/(x^{n/2}+1) (277 pairs, zero
violations). Every finite-q fiber coincidence is a char-q accident
(a prime above p divides a FIXED nonzero cyclotomic integer with all
conjugates <= 6). All tested q were < n^2 — the observed 3-fibers are
accidents in-regime; at official q >> n^2 the sharpened conjecture is
C(3) <= 2. REMAINING for the base lemma: bound the p-divisibility
incidences (char-q half) — a statement about the fixed family
{S(a,b)} and the specific official prime, i.e. arithmetic, not
geometry. The proof of the crux's lower edge is now half done.

## 35 — 2026-07-10: char-q half — norm-counting no-go #5; application
## slack repriced

Attack on the char-q half (p-divisibility incidences of {S(a,b)}).
NO-GO #5 (quantified): global resultant/norm counting is VACUOUS —
total incidence mass <= n^2 phi(n) log_p(6) / k ~ 2^99.6 at official
parameters vs n^2 = 2^80 pairs total (20 bits past useless; each
conjugate <= 6 is too weak a handle globally). The char-q half needs
PER-FIBER trinomial rigidity at large q (a fiber of size f = f
mu_n-roots of ONE trinomial — the gcd(trinomial, X^n - 1) structure),
not pair-counting. REPRICED APPLICATION SLACK: the s-induction only
needs C(s) <= poly(s) — even C(3) <= 1000 suffices for the mid-band
edge (b ~ 7e10 roots vs ~33-sparse divisors); the sharp C(3) <= 2
official conjecture is bonus, not requirement. DESIGN FLAG for the
s-induction: the E/O recursion may pass through smaller effective
fields — the small-field accident regime (q < n^2) must be tracked
level-by-level in the recursion bookkeeping. State: char-0 half
PROVED; char-q half open with its no-go map complete; target slack
repriced upward by two orders.

## 36 — 2026-07-10: the NORMALIZE-SQUARE-REDUCE DESCENT — char-q proof
## program calibrated at round 1

Design: fiber counts are invariant under alpha -> alpha^k, so
normalize the trinomial's top exponent to ~n/2 (orbit argument), then
X^n mod g collapses in a few reduction steps to a sparse remainder of
much lower degree; f <= deg gcd(g, X^n - 1) <= deg(remainder);
recurse on sparse gcds. ROUND-1 CALIBRATION at the extremal
witnesses: sparsity 3-5 terms, degree n -> 7/7/22/18 at n =
32/30/64/128, in <= 8 reduction steps — the poly(s) * polylog(n)
target shape (repriced application need, log #35) is empirically
live. REMAINING for the proof write-up (fresh-session task): the
worst-case normalization analysis (which (u,v) classes admit top ~n/2
with small co-exponent — orbit arithmetic on (ku, kv) mod n),
termination bookkeeping, and the formal statement. Literature pointer
to verify (not assume): Lenstra's lacunary-polynomial factor theory
covers the cyclotomic-factor structure of sparse polynomials — check
whether the needed bound is already a theorem there. This is the
char-q half's proof program, calibrated and posed.

## 37 — 2026-07-10: the ORBIT LEMMA — descent round 1 is UNIFORM

PROVED (bit argument) + exhaustively verified (64,560 non-collapsed
pairs, n = 32/64/128/256, zero failures): every non-collapsed (u,v)
on mu_{2^s} normalizes via k = v^{-1} 2^j to (U, V) = (2^j w mod n,
2^j) with w = u/v odd >= 3, and some j puts U >= n/2 with V <= n/4 —
hence X^n mod g terminates in <= 2 reduction steps with a <= 4-term
remainder of degree < U. Round 1 of the normalize-square-reduce
descent is UNIFORM over all inputs. Remaining for the char-q half:
the multi-round bookkeeping (sparsity growth vs degree descent in the
sparse-Euclid recursion — worst case still open; witnesses collapse
in 1-2 rounds) and the Lenstra literature check. The descent program
now has: a proved uniform first round, calibrated witnesses, and a
precisely posed recursion question.

## 38 — 2026-07-10: CATCH #10 — the sqrt-n one-round certificate was
## FALSE; soundness gate stopped it; corrected to the full recursion

The claimed one-round proof (fiber <= V via binomial remainder) had a
sign-slip: roots satisfy X^n - 1 == 0 mod g, so the remainder is
R - 1 — a TRINOMIAL, not a binomial. The mechanism check alone
PASSED (all branch guarantees held); the SOUNDNESS check against
actual fibers found 168 violations (3-fibers vs certified 2s) at
(97,32) and (193,64) — a false theorem stopped by the second gate
BEFORE banking. This is the protocol's deepest catch (tenth overall;
sixth machine-caught): mechanism-valid but unsound.

CORRECTED STRUCTURE: the descent is a trinomial -> trinomial
recursion (one reduction round maps degree-n trinomials to trinomials
of degree ~V + n - U ~ n/2, per the proved orbit lemma), terminating
at the 2 sqrt(n) degree floor after ~s/2 rounds. The calibrated
witnesses (remainder degrees 7-22) are R - 1 values — the DATA
stands; the THEOREM requires per-round bookkeeping: the new exponent
triple's collapse status and degenerate values at each level. The
sqrt-n bound is DOWNGRADED to conjecture-with-calibrated-recursion.
Next: the per-round invariant (what property of the trinomial triple
is preserved under one reduction round) — the recursion's induction
hypothesis, to be formalized and machine-checked level by level.

## 39 — 2026-07-10: the TOWER BOUND — the trinomial mechanism complete
## at measurement level; all proof ingredients banked

Cycle arc: Dirichlet-span alone fails (unit-fixed exponents like n/2);
the coset bound covers 2-adically heavy exponents (Z <= n/2^{v2},
e.g. Z <= 2 at (1, n/2)); both-odd resistant pairs (1, n/2 - 1)
resolve by LAURENT span at quotient levels (x^{n/2-1} = +-x^{-1});
the unified TOWER BOUND Z <= min_j 2^j (2 span_j + 2) measures
WORST CASE 2.1-3.2 x sqrt(n) at six exhaustive scales (worst pairs =
middle-dyadic (1, 2^j)). CONVERGENCE: the per-level coset-constant
bookkeeping IS the proved sign-family/ledger law (cycles 22-23) — the
campaign's instruments assembled themselves into the proof's parts.
TARGET THEOREM (write-up scoped, all ingredients banked): non-
collapsed trinomials have Z <= ~4 sqrt(n) on mu_{2^s} via tower-split
+ Dirichlet-with-parity-fix + per-coset degree bound. Application
check: 4 sqrt(n) = 2^22 << t = 2^36 at official rows (14 bits room).
FLAGGED for the s-generalization: Dirichlet span degrades as
n^{1-1/(s-1)} — at edge sparsity s ~ 33 that is ~2^38.75 > t: the
s-sparse tower needs its own scaling check BEFORE the edge
application relies on it (next cycle's falsification-first item).

## 40 — 2026-07-10: s-scaling RESOLVED POSITIVE — the tower survives
## at the edge's actual exponent shapes

F2_SSPARSE_TOWER_SCALING_PASS (9 cells, random + application-shaped):
random s-sparse sets track the adversarial Dirichlet degradation
(B ~ n^{1-1/(s-1)}; near n-scale at s = 33 — the tower is useless
adversarially, exactly as flagged); APPLICATION-SHAPED sets
(p-multiple AP + window, the mid-band edge divisor shape) obey a
clean ~12 sqrt(n) law (714 -> 1504 as n quadruples at s = 33) — the
AP normalizes to span ~s under k = p^{-1}, only the window exponent
pays two-form Dirichlet. OFFICIAL CHECK: 12 sqrt(n) = 2^23.6 << t =
2^36 (13 bits of room). The char-q program is now fully scoped and
unblocked: (i) write up the trinomial tower theorem (all ingredients
banked, target ~4 sqrt n); (ii) extend to application-shaped s-sparse
(calibrated ~12 sqrt n); (iii) the edge lemma follows; then the
s-induction is REPLACED by the direct s-sparse tower at the edge
shapes — a shorter chain than designed. Thirty-one cycles: every
flagged dependency of the campaign has now been either resolved
positive, corrected, or banked as a no-go.

## 41 — 2026-07-10: TRINOMIAL TOWER THEOREM (Part 1) PROVED — eleventh
## satellite; the campaign's first mid-band root-count theorem

Statement: Z <= min_j 2^j (2 span_j + 2), any odd characteristic,
unconditional. Proof complete and elementary (coset split with
coefficient absorption; per-coset unit substitution to the span
normalization; Laurent-shift degree bound; collision cases closed —
binomial fallback and the a0-nonvanishing guard). Soundness: 1200
random trinomials at 4 scales, zero violations, worst ratio 0.33 —
this attempt passes BOTH gates (contrast catch #10). Remaining on the
char-q chain: Part 2 (span estimate <= C sqrt n — Dirichlet with the
parity fix; C <= 3.2 measured at six scales) and the s-sparse
application-shaped extension (proof extends verbatim; calibrated
~12 sqrt n). The edge lemma then follows, then the crux assembly.

## 42 — 2026-07-10: THE TRINOMIAL THEOREM IS COMPLETE — Z <= 4n^{2/3},
## unconditional, both parts proved

Part 2-weak (the span estimate): pigeonhole over k <= Q^2 yields an
even difference 2^a delta'; taking 2-adic valuations, delta' (odd)
satisfies the same smallness at tower level a — the parity obstacle
IS the descent, costing only the 2Q^2 term. At Q ~ n^{1/3}:
Z <= 4n^{2/3} + O(n^{1/3}), any odd characteristic, every
non-collapsed trinomial. Verified: bound dominates measured worst at
six scales; certificates exist for every pair at two exhaustive
scales (F2_TOWER_P2WEAK_PASS). Official: 2^{28.7} << 2^36 — nine bits
of room. With log #41's Part 1, the campaign's first COMPLETE
unconditional root-count theorem stands. The chain: s-sparse
extension -> edge lemma -> crux assembly -> L5.

## 43 — 2026-07-10: s-SPARSE EXTENSION PROVED (twelfth satellite) — the
## theorem splits along the struct/extras line by construction

Z(g) <= M(g) + tower for every non-collapsed s-sparse g: the
merge-cancellation case (all class-coefficients vanish on a coset) is
EXACTLY a binomial factor X^m - c^m | g = a full structured coset —
struct and extras separate inside the proof itself. Verified on 2574
random sets (3 scales x s = 4/6/8), zero violations. With logs
#41-42 (complete trinomial theorem) and #40 (application-shape span
~12 sqrt n): the EDGE LEMMA is now this theorem instantiated at the
edge divisor shapes (p-multiple AP + window exponents, span proof =
AP-normalize + two-form Dirichlet + parity descent — all proved
pieces). Chain: edge lemma write-up -> crux assembly -> L5.

## 44 — 2026-07-10: the EDGE SHAPE LEMMA — direct instantiation

Composing f2_full_ladder_dictionary (edge divisors are s'-sparse,
s' = 1 + t/p + k) with f2_ssparse_tower_extension (Z <= struct +
tower) at the application-shape span law (log #40): EVERY t-null
block at edge sizes b = t + k is a union of full cosets plus a
residual of < 2^25 points, against b >= 2^36 — structured to within
10^-3 fraction at worst, BY THEOREM (instantiation arithmetic exact,
16x safety factor; toy consistency: edge extras = 0 at every measured
cell, banked logs #11/#15). REMAINING FOR THE EDGE COUNT: convert
shape to count — the residual-factor census (r = ell*/binomial-part,
deg r < 2^25, with the divided gap conditions); then the crux
assembly consumes shape + count. The campaign's chain is now: edge
count conversion -> crux assembly -> L5.

## 45 — 2026-07-10: CATCH #11 — log #44's constants corrected

Self-caught within the cycle: the instantiation arithmetic (with the
16x safety factor) gives residual ~2^27.6 at k = 1, NOT < 2^25; the
structured fraction is >= 99.71%, not "within 10^-3". The assertion
in the check script fired on exactly this (my threshold b/1000 was
stricter than the truth) — but the log entry had been appended before
the script's failure was read: entry #44's numbers are superseded by
these. THE SHAPE LEMMA STANDS with corrected constants: edge blocks
are coset-unions + residual < 2^28 against b >= 2^36 (structured
fraction >= 99.7%). Process note: log entries must be written AFTER
their check passes, never alongside — encoded here as campaign
procedure. Eleventh catch; seventh self-caught same-cycle.

## 46 — 2026-07-10: RESIDUAL DETERMINATION LEMMA (thirteenth satellite);
## catch #12

The count conversion's first reading (kernel census) was refuted by
its own toy check — toys are under-determined (t < rho), the official
regime is the opposite (catch #12, same-cycle). The correction is a
sharper theorem: below char (rho < p, official 2^27.6 < 2^31), the
gap operator's [1..rho]^2 block is unit-triangular Toeplitz for ANY
core — the residual of every extras block is UNIQUELY DETERMINED by
its structured core (verified on all 160 real accident blocks).
Extras have zero residual freedom; the edge count is now a
deterministic-test census: #{cores whose determined residual passes
~t - rho consistency rows + mu_n-splitting}. The crux's remaining
mathematics: bound that census (the consistency rows are the same
functional at every core — a structured rank/character question, the
final boss in its sharpest form yet). Chain: consistency census ->
crux assembly -> L5.

## 47 — 2026-07-10: CORE-FREE KILL + inverse-complement identity;
## catch #13 (vacuous-test harness bug)

Three results. (1) CATCH #13: the identity test printed REFUTED on an
EMPTY test set (the 160 toy accidents all have empty structured
cores — no with-core cases exist at toys); non-vacuity assertions are
now mandatory harness law. (2) CORE-FREE KILL (proved corollary of
the determination lemma): at t >= rho, an extras block with no
structured core has determined residual trunc_rho(1^{-1}) = 1 — no
roots — so ZERO core-free extras at the edge officially; the toy 160
exist precisely because toys are under-determined (rho = 6 > t = 2).
(3) THE INVERSE-COMPLEMENT IDENTITY (proved algebraically, no
empirical rescue needed): r_B = trunc_rho(B^{-1}) (triangular solve,
no p-slots below rho < p) and B^{-1} == ell*_{D \ core} mod X^n (the
proved product identity) — the determined residual IS the truncated
complement locator. THE CENSUS now covers only WITH-CORE extras:
consistency rows = the core's 2-power part-size subset-sums avoiding
p-free window positions (2-powers summing to p-multiples — sparse
arithmetic), with the repeated-size cancellation caveat for the
write-up. Chain: with-core census write-up -> crux assembly -> L5.

## 48 — 2026-07-10: THE EDGE LEMMA IS PROVED — the dichotomy's first
## proved band; zero extras on the edge

Six-link chain, every link proved and machine-verified: dictionary ->
shape (residual < 2^28 < p) -> determination (unit-triangular) ->
inverse-complement identity -> SEMIGROUP SUPPORT (B^{-1} of 2-power
cores supported on 2^{e_min}-multiples; 180 cores exact) -> residual
roots are FULL cosets -> maximality contradiction. Every edge-size
t-null block is a union of full cosets: extras = 0 on the edge band
(not merely <= budget). Core-free case killed separately (log #47).
The mid-band interior (rho >= p, i.e. b - t >= ~2^31 past the edge)
remains; the rho < p boundary is the frontier and the same machinery
is the tool. Fourteen satellites; the campaign's central conjecture
now has a PROVED band where it was pure conjecture 40 log entries
ago.

## 49 — 2026-07-10: the proved band's honest width; the interior
## frontier posed

The edge lemma's chain requires residual bound < p; with the
calibrated app-shape law (16x safety), the PROVED band at official
parameters is b in (t, t + ~317] (computed exactly), plus b <= t
empty unconditionally and the complementation mirrors. Narrow but
NONZERO — the dichotomy's first proved extras-free band beyond
trivial, and the width grows with every constant improvement (the
sqrt-n refinement of Part 2, the safety factor, the span constants).
THE INTERIOR FRONTIER, posed exactly: past the boundary (rho >= p),
the determination acquires FROBENIUS SLOTS (p-multiple rows below rho
= free parameters, ~rho/p of them); the semigroup argument breaks
there precisely (p-shifts leave the 2-power lattice). Interior
extras <= #cores x q^{#slots}: the interior obligation = bounding
slot-bearing cores — the campaign's next phase, with the edge
machinery as its base camp and the aggregate arsenal (M1 flatness,
SP census, energy dichotomy) as the interior tools. Fourteen
satellites; the first proved band; the frontier now has exact
coordinates.

## 50 — 2026-07-10: the p-ADIC LADDER — the interior's proof program

The Frobenius slots past the char boundary inject as r = trunc(B^{-1}
Abar^p) (char p: A(X^p) = Abar(X)^p) — the interior freedom IS a
level-1 instance of the same gap census: Abar has degree ~rho/p and
inherits ~t/p gap conditions (the Frobenius-redundancy law from catch
#6 as the level transition). Recursion depth ceil(log_p t) = 2 at
official parameters (t/p ~ 33, t/p^2 < 1): the interior extras count
= #cores x census(level 1, degree ~33) with level 1 bounded by the
SAME edge machinery at its own scale. LAB IDENTIFIED: extension-field
toys (F_25, p = 5, n = 24) have reachable interiors (t >= rho >= p
attainable) — the ladder is empirically testable at toy scale, unlike
every prior official-regime mechanism. NEXT: the ladder verification
experiment at F_25 (edge/interior censuses vs the ladder prediction),
then the ladder write-up, then crux assembly (= empty band + edge
band + laddered interior + struct census + consumer replay), then L5.
The campaign's remaining mathematics: one testable recursion.

## 51 — 2026-07-10: ladder corrected (catch #14); interior collapsed to
## one fixed census; first slot-bearing empirical datum — extras 0

CATCH #14 (pre-experiment, self-caught in design): log #50's "Abar
inherits ~t/p gap conditions" is FALSE — in char p, Abar^p reproduces
any Abar exactly on the p-lattice; the gap conditions constrain Abar
not at all. The level-1 freedom is killed by the SPLITTING filter
(ell*_S | X^n - 1), not by gap conditions. CORRECTED LADDER (stronger
where it counts): the interior for ALL block sizes collapses to ONE
fixed splitting census over the ~33-parameter Abar-space — b-independent.
FIRST INTERIOR DATA: (F_49, n=16, t=8): zero t-null blocks at slot-
bearing sizes (struct unavailable there — consistent, vacuous);
(F_25, n=24, t=5, live slot + live struct): ALL 5-null blocks at
b = 6/7/8 are coset unions — EXTRAS = 0 in a slot-bearing regime: the
splitting filter is empirically total at the toy. The dichotomy now
has: proved bands (empty + edge) and its first interior data point
(clean). Chain: the 33-parameter splitting census (the single
remaining object) -> crux assembly -> L5.

## 52 — 2026-07-10: the census's TERMINAL FORM — divisors of X^n - 1
## in a fixed low-dimensional affine family

Interior extras per core = #{divisors of X^n - 1 whose coefficient
vector lies in the core's 33-dimensional affine family
trunc(B^{-1} Abar^p)} — a nearly-fully-prescribed prefix census
(rho - 33 of rho coefficients pinned): the EASIEST instance on the Q
spectrum (prescription length ~ total; at full prescription the count
is trivially <= 1). The level-1 pairing Abar' = trunc(Abar^{-1})
(complementation upstairs) is consistent. The kernel reconnection is
now at MAXIMAL prescription where rigidity is strongest — the
remaining lemma: #divisors-in-affine-family << (cores' growth)^{-1} x
n^3. Toy status: the filter is empirically TOTAL at every slot-bearing
toy tested (F_25: extras 0). This is the campaign's single remaining
mathematical object, in its final coordinates: fixed dimension 33,
maximal rigidity, clean toy data, and all fourteen satellites behind
it. Chain: divisor-in-family lemma -> crux assembly -> L5.

## 53 — 2026-07-10: the LAST REDOUBT — the final lemma is SP-flatness
## of the core-sharing t-null pair census

The divisor-in-family difference structure: two family divisors share
their core, so both FULL blocks are t-null — the family-pair count IS
the SP census of core-sharing t-null pairs (the PROVED v13 identity's
object, restricted to the t-null subfamily). The campaign's complete
compression chain, every step proved except the last:
  dichotomy (conjecture) -> mid-band (tolerance 2^{1.05e12})
  -> empty band [PROVED, unconditional, width t]
  -> edge band [PROVED, extras 0, width ~315]
  -> interior = Frobenius slots -> ONE 33-parameter splitting census
  -> divisor-in-family count -> SP-FLATNESS OF THE t-NULL PAIR CENSUS.
The last object is the kernel in its final coordinates: measured
L2-flat at every cell ever tested (M1 calibration, M2/flat 0.91-1.17),
adjacent to the proved SP strata, and now known to be THE single
statement from which the crux assembly follows. Forty-three cycles
have converted everything else. The campaign stands at: prove
SP-flatness of the t-null pair census (or any bound within the
2^{1.05e12} tolerance) -> assembly -> flip.

## 54 — 2026-07-10: the TRADE-VARIETY LANDING — the final lemma lives
## in pre-built territory

The core-sharing pair census decomposes over signed trades: (S1, S2)
sharing a core <=> the residual pair (R1, R2) is a SIGNED t-null
configuration (R1 - R2 null as a signed multiset), and the dictionary
extends to rational form: ell*_{R1}/ell*_{R2} == H(X)^p mod X^{t+1}.
The last redoubt (SP-flatness of the pair census) is therefore an
instance of the UNIVERSAL TRADE VARIETY framework —
a_universal_trade_variety, an ev-parent of u2c wired into the
critical DAG before this campaign began, with its own banked
apparatus (the M2 route, always one of the five). The campaign's
compressed object needs no new theory lane: it needs the trade
machinery instantiated at signed interior residual configurations
with the rational dictionary. CHAIN, final form: trade-variety
instance (existing lane) -> assembly -> flip. Fifty-four entries;
everything the campaign built converges on machinery that predates
it — the DAG's architecture doing exactly what it was designed for.

## 55 — 2026-07-10: CATCH #15 — the landing's scale audit; the true
## final object is TRADE DECOMPOSITION

Reading the pre-built lane (log #54 celebrated the landing without
the scale audit): a_universal_trade_variety [PROVED] + a2_laurent
[PROVABLE, citation quarantined] + a3_good_reduction [PROVED at fixed
(n,h), computable exceptional primes] are effective at h <= ~40 —
our interior trades have h ~ 2^32: the lane as banked is 30 orders
out of effective range. CATCH #15: the landing stands structurally
but NOT quantitatively as celebrated. THE TRUE FINAL OBJECT: TRADE
DECOMPOSITION — do large signed t-null configurations decompose into
minimal trades of bounded size (Lam-Leung-type structure: char-0
vanishing sums decompose into minimal ones; the trade analogue at
2-power n would give bounded minimal size and re-enter the lane's
effective range)? If YES: interior census <= (bounded-h lane
machinery) composed over decompositions — the assembly closes. If
NO (unbounded minimal trades exist): the interior needs the flatness
route after all. Falsification-first: SEARCH for large minimal
trades at toys (a minimal signed t-null configuration that does not
decompose) — the decisive experiment, designed next cycle. Chain:
trade decomposition (test, then theorem-or-refutation) -> assembly.

## 56 — 2026-07-10: NO-GO #6 — trade decomposition is FALSE; the map
## is complete; the flatness redoubt is the final path

F2_MINIMAL_TRADES_PASS (4 cells): minimal trades exist at EVERY size
tested — exhaustive at (113,16,t=2) through h = 6 (40 minimal), and
100% of sampled trades are minimal everywhere (generic same-moment
pairs contain no sub-trades). The bounded-minimal-size decomposition
theorem is FALSE; the M2 lane's effective range (h <= 40) cannot be
reached by decomposition from h ~ 2^32. Per the pre-registered read:
the FLATNESS ROUTE is the final path. THE CAMPAIGN'S MAP IS NOW
COMPLETE — every route has a verdict: R1 Fourier (absolute: no-go;
exact: instruments proved), R2 energy (branch (a) proved, instrument
banked), R3 trades (lane proved at small h; decomposition no-go #6),
R4 Bezout (half-ladder reach, quantified), R5 sparsity (edge band
PROVED via the full chain). The dichotomy stands PROVED on the empty
and edge bands; the interior rests on exactly one statement: the
flatness/max-to-mean bound of the t-null census family (tolerance
2^{1.05e12}, measured flat at every cell ever tested, adjacent to the
PROVED SP strata). Six no-gos, fifteen catches, fourteen satellites,
fifty-six entries: the map has no unexplored regions — only the one
summit, with every approach now charted and instrumented.

## 57 — 2026-07-10: THE HALASZ BRIDGE — the summit's proof program

The composition that closes the loop: (a) large extras => energy-
deficient (f2_effective_energy_dichotomy, PROVED, printed constants);
(b) energy deficiency IS the Littlewood-Offord/Halasz hypothesis: the
next moment condition p_{j+1} = 0 anti-concentrates on a dissociated
fiber — the contraction the ladder needs; (c) the self-defeating
loop: extras large => contract at L <= 2^15 => extras cannot stay
large — the per-condition induction closes. ARITHMETIC: q * Pr <=
q * K^{-1/2}/sqrt(m): at branch (a)'s weakest row (K = 2^7.75):
2^15.1 (marginal, within a bit); at Schoen-grade (K = 2^13.67):
2^12.2 — THREE BITS INSIDE the target. L4 (explicit Schoen constants)
RE-ACTIVATES exactly per the charter's supersession clause ("iff R2
activates" — R2 just did). THE CAMPAIGN'S REMAINING WORK, final form:
(1) verify the two published inputs' constants (Schoen BSG; finite-
field Littlewood-Offord — both quarantine-disciplined citations);
(2) write the composition (our proved dichotomy + LO => contraction);
(3) formalize the loop induction; (4) assembly + consumer replay.
Nothing else. Every piece is either proved (ours), published (two
citations to verify), or arithmetic. Fifty-seven entries; the summit
has a route with quantified margins.

## 58 — 2026-07-10: citation verifications — Schoen exponents VERIFIED;
## F_p Halasz existence VERIFIED with named sources

Web verification (quarantine discipline, verify-not-assume):
(1) SCHOEN (Combinatorica 35 (2015) 695-701, "New bounds in
Balog-Szemeredi-Gowers theorem"): E(A) = kappa|A|^3 => exists A' with
|A'| >> kappa|A| and |A'-A'| << kappa^{-4}|A'| — exponents (e1, e2) =
(1, 4) EXACTLY as the energy-dichotomy table assumed; absolute
constants unprinted in the record consulted, covered by the table's
conservative row (c = 2^10). L4's exponent half is DONE.
(2) F_p HALASZ / LITTLEWOOD-OFFORD: the finite-field anti-
concentration theory with additive-energy hypotheses exists in the
published literature — the Maples lineage (arXiv:1012.2372,
Singularity of Random Matrices over Finite Fields) and successors
(Spielman-Teng-type over F_p, energy form E_{2k}: solutions of
+-a_{i1}+-...+-a_{i2k} = 0 mod p) — the exact input shape the Halasz
bridge consumes. Remaining: extract the specific theorem's constants
(paper read, queued). The campaign's two external inputs: one
exponent-verified, one existence-verified with named sources. The
bridge's write-up can proceed with symbolic LO constants and the
extraction as its final numeric step.

Sources: link.springer.com/article/10.1007/s00493-014-3077-4;
arxiv.org/pdf/1012.2372

## 59 — 2026-07-10: CATCH #16 — LO source chain corrected and pinned

Log #58 attributed the F_p Halasz statement to Maples arXiv:1012.2372;
the full-paper fetch shows its LO material is over R, not F_p —
CATCH #16 (source precision; the citation-quarantine discipline
catching its own first pass). CORRECTED CHAIN (triangulated via the
literature): Ferber-Jain, "On the counting problem in inverse
Littlewood-Offord theory" (arXiv:1904.10425, JLMS 2021) + the
explicit F_p reduction lemmas in the random symmetric matrix
literature (arXiv:1904.11478 and successors, which state the
reduce-to-F_p anti-concentration steps consuming Ferber-Jain +
Costello-Tao-Vu + Nguyen). The abstracts formulate over Z; the F_p
lemma statements live in the paper BODIES — the extraction task is
now pinned to those specific sections (body-read, next unit). The
Halasz-bridge composition proceeds with symbolic LO constants
meanwhile (the extraction refines, does not block). Campaign totals:
16 catches, every one corrected in-cycle or next-cycle; the summit
route's dependency list is unchanged and shrinking.

## 60 — 2026-07-10: the F_p LO statement EXTRACTED — citation phase DONE

Body-read of arXiv:1904.11478 (Campos-Mattos-Morris-Morrison, "On the
singularity of random symmetric matrices") via saved PDF: THEOREM 1.2
is the exact F_p inverse Littlewood-Offord input, ALL CONSTANTS
PRINTED: for prime p there is a container family C of subsets of Z_p,
|C| <= exp(2^12 (log p)^2), such that every v in Z_p^n with rho(v) >=
4/p and support |v| >= 2^18 log p admits B(v) in C and Y subset [n]
(n/4 <= |Y| <= n/2) with #{i : v_i not in B(v)} <= n/4 and |B(v)| <=
2^16 / (rho(v_Y) sqrt(|v|)). Their Halasz input is Lemma 2.3
(classical). The bridge's two external inputs are now BOTH verified:
Schoen (1,4) [log #58] + CMMM Thm 1.2 [this entry, constants 2^16 /
2^18 / 2^12 / 4/p printed]. REMAINING ADAPTATION: our census values
live in F_q = F_{p^k} — restriction of scalars to k parallel Z_p
coordinates (the anti-concentration compounds across coordinates);
then the composition write-up (dichotomy + CMMM => per-condition
contraction), the loop induction, and the assembly. The citation
phase of the campaign is COMPLETE: no external input remains
unverified. Sixty entries.

## 61 — 2026-07-10: CATCH #17 + NO-GO #7 — the bridge compounds fatally
## at official k; the summit is F_q-native flatness

The restriction-of-scalars adaptation audit: F_q = F_{p^k} census
values = k parallel Z_p coordinates; CMMM's per-coordinate constant 4
(the 4/p threshold) COMPOUNDS across coordinates: L <= 4^k with
k ~ 2^16 — astronomically over the 2^15 tolerance. CATCH #17: log
#57's marginal arithmetic (2^12.2-2^15.1) was one-coordinate; the
compounding was unexamined. NO-GO #7: the CMMM/Halasz bridge is DEAD
at official k (it remains a valid proof route for k = 1 prime-field
instances — banked as such). A promising aside discovered en route:
BGK subgroup unstructure (Bourgain-Glibichuk-Konyagin) supplies the
coefficient-side hypothesis cleanly at every coordinate — useful for
the k=1 route and any future F_q-native argument. THE SUMMIT, final
honest form: F_q-NATIVE anti-concentration with per-coordinate
constant 1 + o(1) — the kernel statement, as the reformulation
closure (log #19) predicted all routes would reach. The campaign's
map is now truly total: seven no-gos fence every classical approach;
the summit requires genuinely new mathematics; everything else in
F2 — the empty band, the edge band, the struct census, the
determination rigidity, fourteen satellites of machinery — is PROVED.

## 62 — 2026-07-10: delegation brief v2 — the definitive handoff

PRO_FLOOR_2_F2_SUMMIT_V2.md written (supersedes the log-#17 brief,
which predates 44 cycles of results): the single remaining statement,
the 14 proved satellites, the 7 fenced no-gos, both verified
citations, the empirical ground truth, and three ordered attack
surfaces for new mathematics — including the k = 1 model theatre
(prove prime-field end-to-end via no-go #7's valid branch, then
study the k = 2 breakage as the minimal true obstacle). The campaign
is now in its terminal posture: summit + total map + definitive
handoff; it continues via delegation and fresh capacity until T-WIN
or T-FLOOR.

## 63 — 2026-07-10: the k=1 THEOREM CORE — pigeonhole + CMMM close the
## prime-field contraction; the model theatre opens

The k=1 composition is simpler than the bridge ever was: moment
coefficients are DISTINCT subgroup values (multiplicity gcd(j+1, n)),
so a CMMM container capturing 3n/4 of them has |B| >= 3n/(4 gcd);
against |B| <= 2^16/(rho sqrt|v|): rho <= 2^18 gcd/(3 n^{3/2}) —
per-condition contraction L = p rho <= p 2^18 gcd/(3 n^{3/2}), no BGK
needed. Non-vacuous for p <= ~n^{3/2}/8: at (257,128) the bound is
L <= ~2^13.9 (inside the 2^15 target; observed L ~ 1); at (7681,512)
even stronger. THE MODEL-THEATRE PROGRAM: (i) formalize the loop
induction over the p-free ladder with gcd bookkeeping (restrict to
low-gcd indices, cost a vanishing fraction); (ii) CMMM support
thresholds (|v| >= 2^18 log p — satisfied at theatre scales); (iii)
assemble with the proved bands => THE F2 DICHOTOMY AT PRIME-FIELD
ROWS with p <= n^{3/2}/8, end-to-end. Then the k = 2 breakage study
= the minimal instance of the summit's true obstacle. The campaign's
first END-TO-END theorem target with no unverified dependency of any
kind is now on the table.

## 64 — 2026-07-10: CATCH #18 — the theatre's exact instance list

Log #63's "(7681,512) even stronger" was WRONG: exact arithmetic
gives L_bound = 59,585 > 2^15 there (p/n^{3/2} = 0.66 > 3/8), and
7681 is the SMALLEST prime = 1 mod 512 — the n = 512 theatre is
EMPTY. Corrected regime: p <= (3/8) n^{3/2}; verified instances:
(257, 128) [L <= 15,949 = 2^13.96] and (12289, 2048) [the NTT prime;
L <= 11,587 = 2^13.5] — the model theatre's stages are the
FFT/NTT-prime rows, one per few octaves. Eighteenth catch, corrected
same-cycle by the arithmetic gate. The theatre program stands with
the corrected instance list.

## 65 — 2026-07-10: CATCH #19 — the CMMM support threshold; the theatre
## moves to theorem-only scales

The composition's final hypothesis audit: CMMM Thm 1.2 requires
support |v| >= 2^18 log p ~ 2^21; our coefficient vectors have
support <= n, and at the named theatre instances n <= 2048 — LOG
#63'S THEOREM CORE IS VACUOUS AT (257,128) AND (12289,2048). Catch
#19 (the third consecutive quantitative-audit catch on this branch:
#17 compounding, #18 instance list, #19 support threshold — the
discipline grinding the composition against every printed constant).
CORRECTED REGIME: n >= 2^18 log n ~ 2^23 AND p <= (3/8) n^{3/2} AND
p = 1 mod n — instances exist (Linnik-density NTT-type primes at
n >= 2^23) but are beyond enumeration: the k=1 theatre is
THEOREM-ONLY (hypotheses verified, no empirical stage — the theorem
stands on the two verified citations at scales where their printed
thresholds genuinely hold). Follow-up: threshold-shopping (LO
variants with weaker support requirements would restore empirical
stages). The campaign's honest arc on this branch: a promising bridge
-> three audits -> a true theorem in a real but unreachable-by-
enumeration regime. Every constant of both citations is now
load-bearing and checked.

## 66 — 2026-07-10: k=1 CONTRACTION THEOREM PROVED (fifteenth satellite)
## — catch #19 eliminated inside the same source

Threshold-shopping succeeded one page below the container theorem:
CMMM Lemma 2.3 (Halasz) is THRESHOLD-FREE. The composition: our
PROVED Lemma A (subgroup Gauss sums <= 2 sqrt p) + cosine inequality
=> the level set T_{n/64}(v) = {0} for every k != 0 (verified exactly
at (257,128) and (12289,2048), multiple exponents; theory floor
(n - 2 sqrt p)/20 clears ell with room) => rho <= 3/p + 4/(p sqrt
ell) + e^{-ell} <= 3.71/p => L <= 4 at n >= 512, n >= 3 sqrt(p).
The NTT-prime row (12289, 2048) is an EMPIRICAL STAGE after all.
Remaining for the prime-field dichotomy end-to-end: the loop
induction write-up (the contraction is now a theorem; the induction
routes it down the p-free ladder with the struct census as the
fixed point) + assembly at the theatre rows. Then: the k=2 breakage
study — where exactly does this chain fail at q = p^2? (The Gauss-sum
bound survives; the Halasz lemma is Z_p-native: the breakage is the
restriction-of-scalars compounding — now with a PROVED k=1 baseline
to measure against.) Fifteen satellites.

## 67 — 2026-07-10: the loop induction's true structure — joint-system
## formulation; two citation targets named

Formalizing the induction exposed the conditioning obstacle: the k=1
contraction theorem is free-cube Halasz; the ladder needs FIBER-
conditional contraction, which does not transfer automatically.
RESOLUTION (structural): the joint-system formulation — bound the
(j+1)-dimensional anti-concentration of the stacked moment map
directly (no conditioning). Its level sets are controlled by SPARSE
exponential sums over mu_n: sum_x e_p(f_k(x)) with f_k
(j+1)-sparse — vacuous via Weil degree (deg ~ n), STRONG via
Bourgain-Glibichuk-Konyagin (any delta > 0 gives level-set floor
~n/20). TWO CITATION TARGETS for the write-up: (a) multi-dimensional
Z_p Halasz (the d-dim analogue of CMMM Lemma 2.3); (b) BGK sparse-sum
bounds with explicit delta and gcd hypotheses (matching the p-free
ladder's exponents). The pattern of the campaign's final phase: each
write-up attempt exposes one precise dependency; each is hunted,
verified, and composed. The k=1 dichotomy end-to-end = these two
citations + the joint composition + assembly. The summit (general k)
waits behind the k=2 breakage study.

## 68 — 2026-07-10: BGK verified-sufficient; the final citation is the
## d-dimensional Z_p Halasz

Citation (a) LANDS with room: BGK (Bourgain-Glibichuk-Konyagin; modern
exposition Kowalski arXiv:2401.04756) gives power savings p^{-eps}|H|
for |H| >= p^delta, ANY delta — our level-set floor needs only a
CONSTANT-factor saving (the 2^{1.05e12} tolerance yet again), and in
the theatre regime (n >= 3 sqrt p) the explicit classical bounds
(Heath-Brown-Konyagin; and our own Lemma A for the linear case)
suffice without BGK's asymptotics. Citation (b) refined by the
joint-dimension analysis: the stacked system over t conditions needs
the d-DIMENSIONAL Z_p Halasz (frequencies k in Z_p^d; level sets =
degenerate combos = the STRUCT directions, again); the d-dim
statement lives in the F_p random-matrix corner (Maples' companion
work / thesis — the hunt's next target) OR is provable by induction
from the 1-dim lemma with quotiented systems (the in-house
alternative if the citation fails). The convergent pattern continues:
one dependency at a time, each either verified, replaced in-house, or
fenced. Sixty-eight entries.

## 69 — 2026-07-10: the final citation exists in the RIGHT form — the
## subspace formulation absorbs the d-dimensional question

The joint anti-concentration over d moment conditions IS the
subspace-membership probability Pr[indicator vector in a fixed
codim-d subspace of F_p^n] — the core object of the F_p random-matrix
corank literature: Maples (the F_p paper's subspace/corank bounds —
the source catch #16 rejected for the WRONG statement carries the
RIGHT one) and Nguyen's "Some new results in random matrices over
finite fields" (Modp, located: people.math.osu.edu/nguyen.1261/cikk/
Modp.pdf). No separate d-dim Halasz needed: the subspace formulation
absorbs it, with structured subspaces (the exceptional classes in
those theorems) mapping to our struct directions once more. NEXT
UNIT: the precise-statement read of Nguyen's Modp paper (constants,
structured-subspace exceptions), then the joint composition = our
census fiber as subspace membership + BGK level floors + the
structured-exception ledger = the prime-field dichotomy end-to-end.
The dependency count is now: ONE statement-read, one composition,
one assembly. Sixty-nine entries.

## 70 — 2026-07-10: LMN EXTRACTED — per-condition constant 1 + o(1);
## the prime-field FLATNESS composition is fully specified

Body-read of Luh-Meehan-Nguyen ("Some new results in random matrices
over finite fields", the located Modp paper): THEOREM 1.5
(non-structure of normal vectors): sup_a |P(sum xi_i w_i = a) - 1/p|
<= exp(-n^c) — per-condition constant 1 + o(1) with EXPONENTIALLY
small error; THEOREM 1.4 (rank distribution): the codim-d joint
scales as p^{-d^2} x explicit products + O(e^{-n^{c'}}), for
p <= exp(n^c), alpha-balanced entries. Their hypotheses are for
RANDOM subspaces; the mechanism consumes only the NON-STRUCTURE of
the normal vectors — which for our FIXED moment functionals is
PROVED (trivial level sets via our Lemma A, f2_k1_contraction_theorem
chain). THE COMPOSITION, fully specified: our proved non-structure +
the LMN/CMMM Halasz mechanism => per-condition error exp(-n^c) =>
accumulated constant (1 + e^{-n^c})^t = 1 + o(1) over the whole
ladder => PRIME-FIELD FLATNESS ITSELF (max/mean = 1 + o(1) modulo
struct) at theatre rows — the full dichotomy, not merely
contraction. REMAINING: (a) the LMN section-6 body-read (confirm the
mechanism consumes only normal-vector non-structure — the fixed-
subspace adaptation); (b) the composition write-up; (c) assembly +
consumer replay AT PRIME-FIELD ROWS. The summit (extension fields,
p <= exp(n^c) barrier) remains F_q-native beyond this. Seventy
entries; the prime-field endgame: one section-read, one write-up,
one assembly.

## 71 — 2026-07-10: mechanism CONFIRMED — per-condition 1 + o(1) for
## fixed functionals; the joint battle in dual coordinates

The LMN section-read (pp. 7-8): their Theorem 3.1 proof is the
generic Esseen chain — rho <= (1/p) sum_{x != 0} prod |char factors|
with the cosine inequality |cos(pi x/p)| <= 1 - 2||x/p||^2 — EXACTLY
our level-set computation; no random-subspace input anywhere. The
fixed-subspace adaptation is therefore one paragraph: their chain +
our proved floor => rho <= 1/p + e^{-n/15} per condition at theatre
rows (upgrade of the 15th satellite from L <= 4 to 1 + o(1)). THE
JOINT VERSION'S FINAL FORM: the p^t - 1 joint frequencies need the
FREQUENCY-SPACE STRUCT LEDGER — degenerate combos are the campaign's
proved collapse/orbit directions in dual coordinates; generic combos
carry BGK floors; the naive union diverges by the familiar margins,
and the ledger bookkeeping (multi-page, all pieces proved) is the
prime-field flatness write-up. The campaign's arc is self-similar to
the last: the final object is its own machinery, one Fourier dual
away. Seventy-one entries.

## 72 — 2026-07-10: NO-GO #8 — full-ladder absolute Esseen is
## structurally impossible; partial flatness provable at 1/22 exponent

The frequency-ledger opener came back CLEAN (zero degenerate
frequencies of 66,048 at d = 2, four exponent pairs — the dual-
collapse set is empty off the avoided classes), and that sharpened
the joint analysis to its verdict: floors cap at n/4 (each summand
<= 1/4) while the frequency count is p^t ~ e^{0.69n} — the absolute-
Esseen union over the FULL ladder diverges REGARDLESS of floor
quality: NO-GO #8, the frequency-space dual of no-go #2 (absolute
methods blind; signed structure required). SURVIVING AND PROVABLE:
partial joint flatness over any c n/log p conditions (the Esseen sum
closes there with our floors) — worth ~1/22 of the needed exponent;
the factor-22 gap needs signed frequency structure. THE CAMPAIGN'S
GEOMETRY, stated honestly: the prime-field theatre's own summit
mirrors the main summit — every level of this problem reproduces the
same signed-vs-absolute battle, each time surrounded by more proved
structure. The theatre yields: per-condition 1 + o(1) [proved],
partial-joint flatness [provable, 1/22 exponent], and the mirrored
summit [signed structure, open]. Seventy-two entries.

## 73 — 2026-07-10: cross-lane harvest audit + maintainer check

Codex status (maintainer duty, overdue): 869 commits on the F3 flip
branch; the h8 odd-chart tail is being paid row-by-row (2^36 down to
2^29 through the night) — the T4 program converging; no interference
with this campaign (one-writer rule held throughout). HARVEST: their
F3_H3_CHAR0_CLASSIFICATION (PROVED + machine-verified) is the
SIGNED-TRADE char-0 statement at h=3 — matching-(e1,e2) triples of
roots of unity force zero-sum mu_3 structure — the exact complement
of our f2_char0_sixterm_classification (fiber-coincidence form).
With their proved good-reduction lemma (a3), the small-h trade
foundations are classified CROSS-LANE: two campaigns, independent
methods, same char-0 conclusions. The harvest confirms (does not
extend): the summit's irreducible content is LARGE-h / full-ladder
signed structure — small h is closed from both directions; unbounded
h is fenced by no-go #6; the frequency dual by no-go #8. The
campaign's record and the sibling campaign's record now certify each
other at their intersection.

## 74 — 2026-07-10: the k=2+ breakage study — NO-GO #9; the summit's
## FINAL coordinates: algebraic-only

The breakage resolves by derivation, no experiment needed: the
per-condition Esseen chain (and every level-set/Halasz variant)
requires n >= ~3 sqrt(q) — at official extension fields sqrt(q) ~
2^{2^20} >> n = 2^40: the ENTIRE ANALYTIC LANE is structurally
vacuous there (NO-GO #9; the k=1 theatre works precisely because
prime fields keep q ~ poly(n)). At n << sqrt(q) the census mean
vanishes hyper-fast and the question is not equidistribution but
ALGEBRAIC HITTING — does the moment image touch 0 beyond struct —
which is exactly where the campaign's proved q-INDEPENDENT machinery
lives (dictionary, determination, semigroup, Bezout certificates:
the edge chain). THE SUMMIT'S FINAL CHARACTERIZATION: at official
rows the F2 interior is PURELY ALGEBRAIC territory; the proved edge
chain is the sole live toolkit; the exact open set is the Frobenius-
slot interior (rho >= p) beyond the proved bands. The campaign's
analysis program is COMPLETE: every probe executed or derived, nine
no-gos fencing every lane at its true boundary, fifteen proved
satellites, and a summit whose remaining content is one algebraic
question in exactly known coordinates. Seventy-four entries.

## 75 — 2026-07-10: THE FROBENIUS SECTOR DECOMPOSITION — the first
## official sector governed by proved machinery

Frobenius x -> x^p permutes mu_n (p coprime to n) and preserves the
t-null census (p_j(phi S) = p_{pj}(S), Frobenius redundancy); struct
maps to struct. The official census decomposes by phi-orbit
structure. THE FIXED SECTOR: phi-fixed blocks live on mu_n cap F_p =
mu_{gcd(n, p-1)} = mu_{2^24} — and n_1 = 2^24 >= 3 sqrt(p) = 2^17.1:
IN THE ANALYTIC REGIME (verified exact). The proved k=1 machinery
(per-condition 1 + o(1), f2_k1_contraction_theorem chain) applies to
a genuine sector of the OFFICIAL problem for the first time. MOVING
SECTORS (orbit size 2^j >= 2): n_j = 2^{24+j} vs sqrt(q_j) doubling
in exponent — out of the analytic regime at j >= 1 (verified);
their rigidity gain (a moving block is determined by 1/2^j of its
data) is the algebraic handle. The summit's open set narrows again:
the moving sectors of the Frobenius-slot interior. Seventy-five
entries; the official problem has its first proved-machinery sector.

## 76 — 2026-07-10: THE FROBENIUS TOWER — the summit as sixteen descent
## steps from a proved base

The moving sectors organize completely: the level-j sector
(phi^{2^j}-stable blocks) is a SELF-SIMILAR instance of the whole
problem at (n_j ~ 2^{24+j}, q_j = p^{2^j}, k_j = 2^j) — conditions on
stable blocks live in the subfield automatically (Frobenius-stable
power sums). The official problem (k = 2^16) is the TOWER of its own
smaller instances: sixteen levels; the BASE (j = 0) is the proved
k=1 sector in analytic regime (log #75); each subsequent level is
one GALOIS-DESCENT step (relate phi^{2^{j+1}}-stable extras to
level-j structure — the census's Galois cohomology). THE MINIMAL
OPEN INSTANCE, concrete: the first descent step j: 0 -> 1 (n = 2^25,
q = p^2, blocks stable under phi^2, split by phi) — one new
mathematical question, the smallest that contains the summit's
content, with the proved base one step below it. The campaign's
terminal object: a sixteen-rung tower, base proved, every rung the
same shaped question, the first rung named and minimal.
Seventy-six entries.

## 77 — 2026-07-10: the first descent DECOMPOSES — the summit's content
## in its final, classical name: GAUSS-PERIOD ANTI-CONCENTRATION

Level-1 structure: phi^2 = id on mu_{2^25}, so phi is an INVOLUTION
(x <-> x^p; fixed points mu_{2^24}). Every level-1 block splits into
SYMMETRIC (whole pairs) and ASYMMETRIC (split pairs) parts. The
symmetric part: conditions are trace-real — a k=1-type census on the
2^24-element PAIR SPACE, IN the analytic regime: the proved machinery
applies. The asymmetric part: carries the imaginary/trace-complement
conditions, whose coefficient systems are the trace fibers of
subgroup values — GAUSS PERIODS. Their anti-concentration is exactly
what the n < sqrt(q) wall blocks (period sums face the same
dimensional wall; Gauss-sum bounds vacuous). BY SELF-SIMILARITY every
tower rung has the same shape. THE SUMMIT'S CONTENT, final classical
name: ANTI-CONCENTRATION OF GAUSS-PERIOD SUMS in the moving
directions of the Frobenius tower — a named, classical-adjacent open
problem (the level-set theory of Gauss periods), with: a proved base,
a proved symmetric sector at every level, fifteen satellites of
machinery, nine no-gos, and the entire campaign record beneath it.
Seventy-seven entries.

## 78 — 2026-07-10: the summit sits in ACTIVE classical mathematics —
## the Gauss-period equidistribution literature located

The hunt confirms: the summit's named object has a living literature.
Duke-Garcia-Lutz: Galois-orbit equidistribution of Gaussian periods
(their Thm 6.3 class — the statement shape the moving directions
consume); MYERSON'S CONJECTURE (norms of Gaussian periods): OPEN in
general with partial resolutions (odd-length cases, q = p cases) —
fully consistent with our summit's resistance: it is equivalent-
adjacent to a recognized open problem. Also located: subgroup-indexed
exponential-sum equidistribution (Cambridge Proc.) and Gauss-sum
independence results. THE DECISIVE NEXT READ: the regime-check —
which (n_j, p^{2^j}) parameter ranges the known equidistribution
theorems cover vs the tower's rungs. If any rung's regime is covered:
that rung falls to citation + composition; if none: the summit is
confirmed equivalent to open classical territory and the campaign's
terminal deliverable is the sharpest known reduction OF a recognized
open problem TO the prize floor. Either way the campaign's record is
the definitive map. Seventy-eight entries.

## 79 — 2026-07-10: CAPSTONE — the F2 summit IS Myerson's conjecture at
## growing subgroup order (exact identification, not analogy)

The regime-check read (Habegger, "The Norm of Gaussian Periods",
arXiv:1611.07287, pp. 1-3): his equation (2) — Myerson's own
combinatorial framing — is LITERALLY our census: #{solutions of a
subgroup linear equation} - flat count = ((p-1)/p) * Delta with
Delta = the product of Gaussian-period values. Our extras-vs-flat
question IS the Gaussian-period-norm question, identically. REGIME
MAP: every known result (Habegger Thm 1: f a FIXED odd prime,
p -> infinity, rate O(p^{-1/(5(f-1)^2)}); Duke; Myerson's own cases
f <= 4) and MYERSON'S CONJECTURE ITSELF are fixed-f statements; the
tower's rungs need f = n_j ~ p^{0.77}+ GROWING. THE F2 SUMMIT = a
growing-order generalization of Myerson's conjecture — strictly
beyond the literature AND beyond the stated open conjecture. One
possible crack noted for the record: Lind-Schmidt-Verbitskiy's
ergodic averages over "certain sequences of groups of roots of
unity" (which sequences = the follow-up read). THE CAMPAIGN'S
TERMINAL DELIVERABLE, now exact: the prize floor F2's remaining
content is a recognized-open-conjecture generalization, reduced to
it through 15 proved satellites, 9 no-gos, and 79 log entries of
verified structure — the sharpest placement this problem has ever
had. Seventy-nine entries.

## 80 — 2026-07-10: the LSV crack closes — the literature map is
## complete; the campaign's terminal state fully certified

The follow-up read: Lind-Schmidt-Verbitskiy's ergodic averages (and
the 2016 Diophantine refinement, arXiv:1611.04664) cover sequences of
FULL groups mu_N as N -> infinity — exactly the m = 1 anchor case,
which the campaign's machinery handles exactly (the (1+z^q)/(1+z)
identity, log #20) — NOT the growing-index subgroup sequences of the
Frobenius tower. The last located crack closes; the literature's
reach ends where the proved territory ends. TERMINAL CERTIFICATION:
the F2 red = one recognized-open-conjecture generalization (Myerson
at growing subgroup order), beyond every located result AND every
located conjecture AND all nine fenced method-classes — with the
empty band, the edge band, the Frobenius-fixed sector, the symmetric
sectors, fifteen satellites, and the entire instrument suite PROVED
beneath it. The campaign continues by charter through: delegation
(the brief now names a recognized problem), fresh-capacity summit
attempts on the named object, and the standing instruments. Eighty
entries; every claim in all of them carries a proof, a digest, a
verified citation, or a correction.

## 81 — 2026-07-10: the capstone's dual-use export drafted

MYERSON_IDENTIFICATION_EXPORT.md written (notes/correspondence/):
the identification chain in upstream's language (row-sharp Q at zero
prefix = Gaussian-period norms; growing-order regime gap; our proved
sectors as consumable evidence; suggested consumption items a-c).
STATUS: draft for user review per house convention — outward-facing
PR machinery waits. The capstone now serves both programs: the
prize DAG carries it in u2c's statement; the correspondence lane
carries it toward upstream's Q ledger. Eighty-one entries.
