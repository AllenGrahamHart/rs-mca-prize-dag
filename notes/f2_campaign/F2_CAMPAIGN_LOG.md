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
