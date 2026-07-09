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
