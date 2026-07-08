# F5 skeleton — formal statements and first proved pieces (P1, 2026-07-07)

## Conventions (pinned against verify_xr_smallcore_rungs_2a_2b.py)

Row: domain D ⊂ F_q^×, |D| = n; codewords = deg<k polynomials; pair
(u, v) ∈ F_q^n × F_q^n; pencil word at slope z: u + z·v. A SUPPORT is the
exact agreement set of a codeword with u + z·v at size A = k + σ (σ = the
excess; the floor's core threshold is k + t − 1). ALIGNMENT CONDITION for
(S, z): the values of u + z·v on S extend to a deg<k codeword, i.e. the σ
top interpolation coefficients vanish:

>  Π_S(u + z·v) = 0 ∈ F_q^σ,   Π_S linear in the word.

**Structure Fact 1 (linearity + slope split).** Π_S(u + z v) =
Π_S(u) + z·Π_S(v). Hence each (S, z) contributes σ linear functionals on
(u, v)-space of the RIGID FORM (a_S, z·a_S), where a_S = the top-coeff
interpolation functional row(s) of S, depending on S ONLY.

**Structure Fact 2 (full support, nonzero weights).** Each scalar
component of a_S is supported exactly on S with ALL coordinates nonzero
(Lagrange top-coefficient weights 1/Π_{l≠j}(x_j − x_l) ≠ 0).

## L1 (classification — assembly of proved rung identities)

Every z-aligned support of (u,v) is exactly one of:
(i) SAME-SLOPE (rung 2a: the exact-list object of u + zv) — stripped;
(ii) TANGENT-CHARGED (rung 2b: a distinct-slope pair with core r ≥ k+1
forces (u,v)|core to a codeword pair; depth d = r − k) — stripped;
(iii) LIVE: distinct slopes, all pairwise cores ≤ k + t − 2.
The post-strip remainder consists of class-(iii) families. [Assembly of
proved identities; formal write-up with the verifier's conventions.]

## L2 (alignment ledger — definitional)

A live family {(S_i, z_i)} imposes the condition set
{(a_{S_i}, z_i a_{S_i})}. If the conditions are INDEPENDENT, the family
size is ≤ 2n/σ (solution space nonempty demands #conditions ≤ 2n). So
the theorem reduces to bounding DEPENDENT (syzygetic) families — L3.

## L3a (per-coordinate collapse — PROVED, the first mined obstruction)

**Lemma.** Let Σ_i λ_i (a_{S_i}, z_i a_{S_i}) = 0 be a dependence
(λ ≠ 0). Then per coordinate x, with μ_i(x) := λ_i a_{S_i}(x) over the
participating supports containing x:
   Σ_i μ_i(x) = 0   and   Σ_i z_i μ_i(x) = 0.
If some x is contained in EXACTLY TWO participating supports with
DISTINCT slopes, then (z_i − z_j)μ_i(x) = 0 forces μ_i(x) = 0, and by
Structure Fact 2 (a_{S_i}(x) ≠ 0) λ_i = 0 — contradiction on that
support's participation.
**Corollary (covering rigidity).** In any live dependence, EVERY point of
EVERY participating support is covered by ≥ 3 participating supports (or
≥ 2 sharing a slope — excluded in a live family by class (i) stripping...
[boundary detail: same-slope pairs within a live family are re-classified
to (i); pin in the write-up]). Combined with pairwise cores ≤ k + t − 2,
a participating support of size A needs ≥ ⌈2A/(k+t−2)⌉ partners — live
syzygies require RICH COVERING DESIGNS, not generic families. ∎ (proof
as above; verifier to instantiate at toys)

## L3 (live-syzygy lemma — the remaining core, now sharpened)

**Candidate statement.** A live family admitting a dependence whose
covering design satisfies the L3a rigidity must, on its solution locus,
force Π_{S_i}(v) = 0 for some participant (invalid alignment) or a
class-(i)/(ii) structure. Equivalently: rich-covering live syzygies are
arithmetically unrealizable with all alignments valid.
**Status:** open; held adversarially (Pro window-5: all found dependencies
collapsed to Π_S(v) = 0). P2 attacks EXACTLY the L3a-rigid configurations
(triple-covering designs with pairwise-small cores) — the only place a
counterexample can now live.

## L4 (composition — arithmetic once L3 lands)

Independent families ≤ 2n/σ (L2); dependent families need L3a-rigid
designs, which L3 kills (or bounds); totals ≤ 2n/σ + O(design bound)
≪ 16n³ at every official candidate (slack ~2^100). Toy calibration:
measured engineered maximum 0.55n; measured natural families = q
(slope-limited).

## P1/P2 run 1 (2026-07-07) — HONEST STATUS

- **L3a PROVED on paper** (the proof does NOT depend on the checker):
  dependence Σ λ_i (a_{S_i}, z_i a_{S_i}) = 0 splits into u-block
  Σ λ_i a_{S_i} = 0 and v-block Σ λ_i z_i a_{S_i} = 0. Restrict to the
  LEADING top-coefficient functional a_S^lead(x) = 1/Π_{l≠x}(x−x_l),
  which is nonzero at every x ∈ S (Structure Fact 2, leading row only —
  the lower rows can vanish, but one nonzero functional per point
  suffices). At x: Σ_{i∋x} μ_i = 0 and Σ_{i∋x} z_i μ_i = 0 with
  μ_i = λ_i a_{S_i}^lead(x). A point in exactly one participant forces
  λ_i = 0; in exactly two distinct-slope participants forces
  (z_i−z_j)μ_i = 0 ⟹ μ_i = 0 ⟹ λ_i = 0. So every participant point is
  triple-covered or shares a slope. ∎
- **CHECKER BUG (not banked as verification):** the Modal L3a covering
  flag is over-conservative (flags min-multiplicity < 3 without the
  shared-slope exception), so its "L3a holds: False" is a FALSE flag —
  it does not refute the paper lemma. Also the greedy live-family
  extraction is degenerate on random words (live = 1354 at q = 47 from
  noise, not a structured family). Both need repair before the checker
  validates L3a.
- **P2 decisive signal (partial run):** rigid VALID live syzygies found
  = 0 across all COMPLETED trials (the object whose existence would
  refute L3). Several shards timed out; the run is INCONCLUSIVE, not a
  survival credit. Next: fix the checker (shared-slope exception + a
  real live-family definition scoped to STRUCTURED words), shard the
  larger rows, and run the engineered triple-cover construction that L3a
  says is the only remaining home for a counterexample.

STATUS: L3a is a PROVED obstruction (first mined lemma of the program);
the counterexample surface for L3 is now provably confined to
triple-covering designs with pairwise cores ≤ k+t−2 and all valid
alignments — that confinement is the program's first real progress.

## P2 v2 + realization decision (2026-07-07) — the loop closes on L3's true form

- CHECKER FIXED (one support per slope; shared-slope exception): the
  natural/adversarial-word runs are clean.
- ENGINEERED HUNT (f5_p2_v2_modal.py): ~387 rigid triple-cover designs x
  8 embeddings x 3 scales = ~3000 dependent-configuration tests. ONE hit
  passed the hunt's (incomplete) validity screen: q = 47, the MINIMAL
  3-regular design (8 points, 6 supports, cores <= 2, distinct slopes),
  condition rank 11/12 — a genuine linear-algebra syzygy.
- EXACT REALIZATION DECISION (f5_p2_realize_modal.py): the hit is an
  **ARTIFACT — exactness is FORCED to fail**: coincidence functionals
  cf_i(y) − (u_y + z_i v_y) for union points y outside S_i are
  IDENTICALLY ZERO on the solution space — every solution makes some
  codeword agree beyond its design support, inflating the true agreement
  sets and re-classifying the family OUT of the live class (into
  tangent/big-core territory). The syzygy exists linearly but cannot
  manifest as a spread-family object. L3 STANDS on this hit.

## L3 REFINED (the mined dichotomy — now the precise proof target)

**L3 (refined).** Any dependence among the alignment conditions of a live
family forces, IDENTICALLY on its solution locus, at least one of:
  (a) Π_S(v) = 0 for a participant (invalid alignment — Pro's observed
      collapse mode), or
  (b) an agreement-spillover coincidence (a participant's codeword
      forced to agree outside its support — re-classifying the family
      out of class (iii)).
Evidence: every dependence ever produced (Pro's greedy adversary + our
~3000 engineered rigid configs) died by (a) or (b); the q=47 minimal
design died by (b) via identically-vanishing coincidence functionals.

## L4 ROBUSTNESS (the theorem survives even a weakened L3)

Independent of L3's final form: by L3a + the design-cost combinatorics,
every independent syzygy consumes >= m_min participants (m_min = 6 at
A = 4; general m_min(A) from C(m,2)(A−2) >= 3P >= ... — a finite
combinatorial lemma). Hence rank >= sigma·N_f − N_f/m_min, so
N_f <= 2n/(sigma − 1/m_min) = THETA(n) even if valid syzygies existed.
The 16n^3 theorem is therefore TWO-WALLED: L3 (dichotomy) OR the design
cost — either suffices for L4.

## CORRECTION (same day, self-caught): the "two-walled" claim overstates wall 2

The design-cost route ("every syzygy costs >= m_min participants ⟹
rank >= sigma·N − N/m_min") is NOT a proof as sketched: matroid girth
does not bound nullity in general (R generic vectors in a (c−1)-dim
space have girth c and nullity R−c+1). The route survives only if the
SPECIAL structure of the functionals (full-support a_S on S, pairwise
cores <= k+t−2, the (a_S, z·a_S) slope form) fights nullity growth —
i.e. wall 2 needs L3a-type per-coordinate arguments applied to the whole
dependence SPACE, not just minimal circuits. Status: wall 2 = CANDIDATE
route with this named gap; wall 1 (the L3 dichotomy) remains the primary
proof target, now precisely stated with both collapse modes evidenced.

## P3 (2026-07-07): the dichotomy — formal reductions proved, the engine identified

**P3.1 (reduction to a per-configuration containment — PROVED).** Let R =
the row space of the family's alignment functionals (on the union
coordinates), V = R^⊥ the solution locus. Exactness fails identically iff
some coincidence functional χ_{i,y} ∈ R (y a union point outside S_i;
outside-union points are NEVER forced since R does not touch their
coordinates — matches the q=47 data). Validity fails identically iff some
support's full Π_{S_i}(v)-block of functionals ⊂ R. Conversely if NO
χ ∈ R and no Π(v)-block ⊂ R, then since a linear space over F_q is not a
union of fewer than q proper subspaces, a point of V avoiding all (≤
m(U−A) + m ≪ q) bad hyperplanes exists — a valid exact realization.
Hence: **L3-point ⟺ "every dependent live configuration has χ ∈ R or a
Π(v)-block ⊂ R" — a per-configuration, linear-algebra-decidable
statement.** (This is exactly what f5_p2_realize_modal.py decides.)

**P3.2 (pencil identity — PROVED).** On V, for all i, j:
Π_{S_j}(u + z_i v) = (z_i − z_j)·Π_{S_j}(v). (From linearity and
Π_{S_j}(u + z_j v) = 0.) In divided-difference language (σ = 1): the
alignment functional of S_j evaluated on any pencil word is (z − z_j)
times its v-evaluation.

**P3.3 (first-order no-go — PROVED).** The dependence relations
Σλ_iΠ_{S_i} = 0 and Σλ_i z_iΠ_{S_i} = 0, paired with any pencil word via
P3.2, yield identities that vanish automatically (the coefficients are
again the two dependence relations applied to v). NO first-order pairing
of the dependence with the pencil can produce the dichotomy: the
obstruction is second-order — it lives in the EXACTNESS geometry (the
containment of P3.1), not in formal syndrome algebra. This kills a
family of tempting proof attempts and steers P3 to the containment.

**P3.4 (the engine — Schwartz–Zippel class certificates).** The
containment "χ ∈ R" is a determinantal (Zariski-closed) condition in the
embedding coordinates of the design. Strategy: enumerate the ISOMORPHISM
CLASSES of rigid designs (per L3a) at each size; for each class, test the
containment at random embeddings over a ~61-bit prime. By
Schwartz–Zippel, containment at a random embedding certifies the generic
identity with error ≤ deg/p (quantifiable, repeatable, upgradeable to
symbolic). Outcome per class: (i) generically NOT dependent (class
irrelevant), or (ii) generically dependent AND containment holds →
**L3 PROVED generically for the class**, with the non-generic embedding
locus Zariski-closed of bounded degree (a bounded exceptional family —
absorbable in L4's ledger); or (iii) containment FAILS at some embedding
→ decide realizability exactly (the P2 procedure); a realizable case =
honest L3 counterexample → pivot to nullity-structure bounds.

## P3 run (2026-07-07): stratum certificates + the mechanism isolated

**Part A — the ENTIRE minimal stratum certified at M61.** All 1,485 raw
shapes of the minimal rigid design space (P = 8, m = 6, 3-regular, cores
<= 2; complete enumeration wlog containing the lex-min block) x 8 random
embeddings over p = 2^61 − 1: **all 11,880 embedded systems are
INDEPENDENT.** By Schwartz–Zippel (coordinates sampled from a 10^9 box;
per-shape error <= (deg/10^9)^8), **generic embeddings of every minimal
design are independent** — the q=47 dependence was a small-field accident
(a point ON the proper Zariski-closed dependence locus). SURPRISE
UPGRADE: on the minimal stratum, generic independence holds outright; the
dichotomy is only ever needed ON the dependence locus.

**Part B — exact-decision sweep, no sampling verdicts:** 1,290 dependent
embedded configurations across q in {47, 97, 193, 389} (random rigid
designs, P up to 14): **every single one resolves to forced_coincidence
(mode (b), agreement spillover); zero forced_invalid; zero GENUINE.**
The operative collapse mode of the dichotomy is (b) universally in this
regime; mode (a) (Pi(v) = 0) appears only in non-rigid greedy families
(Pro's window-5 data), consistent with L3a: those dependences were not
covering-rigid.

**The reformulation that exposes the core (proved, definitional):** the
coincidence functional chi_{i,y} IS the extra alignment row of the
extended support S_i ∪ {y} (aligning on A+1 points = aligning on A +
coinciding at y). So R_ext(i,y) = R + span(chi_{i,y}), and:
  L3(b) ⟺ **"rank R < sigma·m implies some one-point extension does not
  increase rank"** — dependent live families ABSORB one of their
  one-point extensions.
This is an exchange-type statement about the interpolation matroid of
the configuration — the theorem's remaining core, now in its sharpest
form. Contrapositive: if every one-point extension strictly increases
rank, the family's conditions are independent (and L2 caps it at 2n/sigma).

**Remaining gap (named, honest):** prove the absorption statement on the
dependence locus (all components, all strata), or equivalently the
exchange lemma. Everything else in L1-L4 is proved or certified. Evidence:
1,290/1,290 dependent configs absorb; 11,880/11,880 generic minimal
configs are independent; zero counterexamples in ~16,000 exact decisions
across the program.

## P3.5 (proved): the P0-quotient reduction of absorption

Every spillover functional vanishes on the pencil-degenerate plane
P0 = {(p|_U, r|_U) : deg p, deg r < k} (on P0 the pencil word is globally
deg<k, so c_i = w and c_i(y) − w(y) = 0), and every Π_{S_i}(v)-functional
vanishes there too (v deg<k). Also P0 ⊆ V always, giving the a-priori
bound rank ≤ 2(U − k) — which the minimal stratum saturates generically
(12 = 2(8−2): the generic independence of Part A is the SATURATION of
this bound). Hence with V = P0 ⊕ F (F = the fresh directions,
dim F = 2(U−k) − rank):

>  **Absorption ⟺ some spillover χ_{i,y} or some Π_{S_i}(v)-block
>  vanishes identically on F.** In the rank-deficit-1 case (dim F = 1,
>  fresh direction (u*, v*)): absorption ⟺ some scalar χ_{i,y}(u*,v*) = 0
>  or some Π_{S_i}(v*) = 0.

Triple-alignment language (k = 2): a nondegenerate pencil aligns each
triple of U at EXACTLY ONE slope (the collinearity determinant is linear
in z). The configuration demands 24 designated triple-alignments; a
spillover = 6 extra triples aligning at a designated slope. Absorption
says the dependence forces the fresh pencil to over-align. [Both proved /
elementary; the triple-slope map ζ(τ) is the right coordinate system for
the exchange argument.]

## P3c (2026-07-07): ABSORPTION AS STATED IS FALSE — self-refutation, banked

The volume harvest on the TRUE minimal stratum (not the denser random
designs of the earlier sweep) found the dependence locus at codim 1
(density ~ q^-1 at q = 97..769) and 127 NOT-absorbed on-locus points.
One verified END-TO-END with independent code: **q = 97, supports
{22,26,76,60},{22,60,63,92},{22,63,51,19},{26,76,92,19},{26,60,51,19},
{76,63,92,51}, slopes {50,48,3,89,68,6}, rank 11/12, explicit full-domain
(u,v)** with all six supports EXACT agreement sets, all Pi(v) != 0,
pairwise cores <= 2, distinct slopes (certificate:
f5_absorption_counterexample.json). Dependent live families EXIST.
- Why earlier evidence missed it: the P3 Part-B sweep used denser random
  designs (dimension-crowded, spillover-forced); Pro's greedy families
  were not covering-rigid; the single P2 minimal hit at q=47 landed on a
  deeper forced sub-locus. The minimal stratum's codim-1 locus is where
  the lemma dies. Classification lesson: the earlier "mode-(b) universal"
  claim was a STRATUM artifact.
- THE FLOOR IS UNAFFECTED: a deficit-1 six-support cluster is size 6,
  not 16n^3. What died is the candidate proof lemma.

## RE-AIM: L3'' (the rank lower bound — all the theorem needs)

The theorem does not need independence. It needs: **rank >= sigma*N / x
for ANY x up to ~n^2** (then N <= 2n*x/sigma <= 16n^3 with room). The
new target is a nullity upper bound: how many independent syzygies can a
live N-support family carry? Each syzygy is confined by L3a (proved) to
a rigid >= 6-support subconfiguration sitting on a codim-1 embedding
condition. Disjoint clusters give nullity <= N/6 (fine); the open
question is STACKING: can overlapping clusters pile nullity to
sigma*N - o(N)? Next experiment: engineered stacking of dependent
clusters sharing supports; measure max nullity vs N. Next lemma
candidate: nullity <= N/m_min via the per-point L3a collapse applied to
the whole dependence SPACE.

## P4 partial (2026-07-07): Pro's rank bound VERIFIED — toy-window theorem
## COMPLETE; two scope catches; official-scale gap named

**Pro's rank theorem (VERIFIED, absorbed).** For N supports of size A on
<= n points with pairwise cores <= A−2: rank(R) >= sigma*N(A−1)/(A*C(n−1,
A−2)). Proof: (1) point-degree bound deg(p) <= C(n−1,A−2)/(A−1) by
double counting residual (A−2)-subsets (two residuals sharing one would
make the originals share A−1 points); (2) greedy matching M >= N/(A*Delta);
(3) disjoint supports contribute sigma rank each (interpolation
isomorphism; u-projection; disjoint coordinates add). Uses ONLY the
pairwise-core condition. Our verification: logic sound; q=97 certificate
rank replayed (11); 300-family random stress at q=193: bound holds
everywhere.

**TOY-WINDOW THEOREM (COMPLETE).** Composing with rank <= 2(n−k) (P0
containment): N <= 2(n−k)*x/sigma with x = (2/3)(n−1)(n−2) at A=4:
**N = O(n^3) < 16n^3 for every live family in the k=2, t=2 scaled
window.** The floor's statement is now a THEOREM at toy scale.

**Catch #9 (Pro's q=11 example, verified: rank 7/8 with four 1-covered
points): L3a's covering conclusion is FALSE for sigma >= 2** — my proof
treated lambda_i as scalars (valid only at sigma = 1); for vector blocks,
a point in one support imposes one scalar condition per moment row, not
lambda_i = 0. L3a re-scoped: sigma = 1 ONLY. The m_min >= 6 syzygy-cost
combinatorics dies with it (q=11: a 4-support dependence). Pro's rank
bound replaces all of it, cleanly.

**Catch #10 (scope): Pro's bound is VACUOUS at official parameters** —
x_A(n) = A/(A−1)*C(n−1, A−2) explodes at A = k+t with k = rho*n
(C(n−1, k) ~ 2^{nH(rho)}). The toy window is where set-combinatorics
suffices. THE REMAINING CORE of the F5 program: the rank/count bound at
OFFICIAL scale (A = k+t, k = Theta(n)), where the matching argument
collapses (at rho = 1/2 only ~2 disjoint supports fit). The official
bound must use the coding structure: per-slope exact-list sizes (the
same-slope column is charged for exactly this reason), cross-slope
aggregation, tangent-strip geometry — the set-combinatorial abstraction
provably cannot reach 16n^3 there (a sunflower of N supports through a
common k-core is core-legal but matching-free). NEXT PHASE: pose the
official-scale statement precisely; check what the consumer needs at the
six candidates; attack with the list machinery.

## P5 (2026-07-07, program resumed): the OFFICIAL-SCALE statement posed;
## the SUNFLOWER PENCIL LEMMA (catch-#10's obstruction shape PRICED)

**Consumer extraction (weakest sufficient form).** xr_clean_residual_any_gate
consumes exactly: R_post(u,v;A) <= 16 n^3 per pair, post quotient/tangent
strips, dihedral + extension inside, with sufficiency = exact integer
arithmetic at the SIX CANDIDATES (the per-rate crossing evaluations). So:

>  **F5-OS (the official-scale target):** at A = k+t, k = rho*n, for every
>  received pair (u,v) after the quotient/tangent strips: the number of
>  LIVE SLOPES (slopes z carrying an exact, valid, aperiodic alignment on
>  a support of size A; one support per slope by L1) with pairwise cores
>  <= A-2 is at most 16 n^3, in the exact form the six candidate
>  evaluations consume.

**Reformulation (proved, definitional):** live families are counted by
SLOPES. For a fixed pair (u,v), a candidate codeword c and a point x with
v(x) != 0 determine the unique coincidence slope zeta_c(x) =
(c(x) - u(x))/v(x); a support S is live at z with codeword c iff
zeta_c(x) = z for ALL x in S (v-vanishing points carry z-independent
coincidence and are charged separately). So each (c, S) pair carries AT
MOST ONE slope, and live slopes at c = values z whose zeta_c-fiber has
size >= A.

**SUNFLOWER PENCIL LEMMA (PROVED — the new obstruction).** Fix a k-set
W. Codewords agreeing with u + z*v on W form the pencil c_z = P_W +
z*Q_W (P_W, Q_W = the deg<k interpolants of u|_W, v|_W; linearity of
interpolation). For x outside W:
 (a) if v(x) != Q_W(x): exactly ONE slope zeta_W(x) = (P_W(x) - u(x)) /
     (v(x) - Q_W(x)) makes c_z coincide at x;
 (b) if v(x) = Q_W(x) and u(x) = P_W(x): EVERY slope coincides at x —
     but then the codeword PAIR (P_W, Q_W) agrees with (u,v) at W ∪ {x};
     >= t such points give pair-agreement >= k+t = a TANGENT event,
     charged to the tangent strip;
 (c) if v(x) = Q_W(x), u(x) != P_W(x): NO slope coincides.
Hence POST-TANGENT-STRIP (< t degenerate points per W, say d): every
live support containing W needs >= t - d >= 1 points from its own slope's
zeta_W-class, classes are disjoint, so
    #live slopes with a support containing W  <=  (n-k)/(t-d)  <=  n-k.
COROLLARY: any live family whose supports share a common k-core has
N <= n-k (LINEAR) — catch #10's "core-legal but matching-free" sunflower
is priced by the pencil + the tangent strip, exactly the predicted shape
(the set-combinatorial abstraction cannot see this; the coding structure
kills it in three lines).

**Stratification plan for F5-OS:**
 (i)  HIGH-CORE stratum (some pair of supports shares >= k points, i.e.
      cores in [k, A-2]): both slopes live through a common W — per-W
      pencil counts apply; need the W-multiplicity aggregation.
 (ii) LOW-CORE stratum (all pairwise cores <= k-1): at official scale
      supports of size ~n/2 overlap in ~n/4 >> k is IMPOSSIBLE for
      k = rho*n... (cores <= k-1 ~ n/2 - 1 is not restrictive there);
      the instrument is the per-slope exact-list cap + the (c,S)->unique-z
      accounting; open.
 (iii) v-vanishing and pencil-degenerate escapes: charged to their strips
      (validity, tangent) — the ledger already carries both columns.

**P5-E1 (next, Modal):** exhaustive live-slope censuses at official-SHAPED
toys (k = n/2, t = 2, A = n/2 + 2): the per-W pencil scan enumerates ALL
live (z, S) completely (every size-A support contains a k-set); measure
max/median live-slope counts N(u,v) post-strip vs n; random + engineered
pairs; record core geometry of the found families. Falsifier shape: N
growing super-polynomially (vs the toy-window O(n^3)) or engineered
stacking beating the pencil-lemma strata.

## P5-E1 (2026-07-07, run): mean-regime censuses + program catch #11 (row shape)

Exhaustive live-slope censuses at (n, q) = (12,97), (16,97), (16,193),
t = 2 (n = 24 job timed out; defer). FINDINGS:
1. FIRST-MOMENT-PINNED: N_post medians 5 / 36 / 53 vs mean predictions
   C(n,k+2)/q = 5.1 / 41.5 / 82.6 (slope-collapse explains the gap at
   the last row). No super-mean stacking in 100 random pairs.
2. ENGINEERED STACKING FAILED: pencil-perturbed pairs fired the tangent
   strip (84 / 1287 tangent-W events) and landed BELOW random
   (N_eng <= N_rand at every row). The strip absorbs the attack, as the
   pencil lemma predicts.
3. PROGRAM CATCH #11 (against my row design): t = 2 toys sit at the
   MEAN-SCALE window. The official window has t = A - k ~ 67471 (the
   crossing depth): first moment C(n,A) q^{1-t} is astronomically
   negative, so F5-OS is a WORST-PAIR ANTI-CONCENTRATION claim in the
   deep sub-mean regime (the F2-sub-balance shape). Consequences:
   (a) the sunflower pencil lemma at official t is strong: the
       common-k-core stratum has N <= (n-k)/t ~ 14.5 at the KB shape;
   (b) the honest toy scales t: sub-mean windows C(n,k+t)/q^{t-1} << 1
       (e.g. t = 4 at (16,97): mean ~ 0.002) — P5-E2 hunts whether ANY
       pair (random or engineered) carries live slopes there at all.

## P5-E2 (2026-07-07, run): SUB-MEAN windows — the anti-concentration hunt

Same scanner, t scaled to reach sub-mean windows (f5_p5e2_submean_modal.py):

    (n,q,t)     mean C(n,k+t)/q^(t-1)   random N_post   engineered N_post
    (12,97,3)   0.023                   0 (max)         3 (max)
    (16,97,3)   0.46                    1               4  (165 tangent-W stripped)
    (16,97,4)   0.002                   0               1
    (16,193,4)  0.0005                  0               1
    ((20,193,5) timed out; defer — needs sharding)

FINDINGS:
1. Random pairs: ZERO live slopes in every deep sub-mean window — the
   mean arithmetic is honest there.
2. Engineered near-pencil pairs buy O(1) live slopes, DECREASING with
   window depth (3-4 at t=3, 0-1 at t=4) — nowhere near n^3 = 1728-4096,
   and the diagnostic maxcore = A-1 events among the greedy picks mean
   the LEGAL (core-capped) family is smaller still.
3. NEXT LEMMA CANDIDATE (mined from the engineered channel): NEAR-PENCIL
   BUDGET — for an r-perturbed pencil pair, post-strip live slopes are
   confined to k-sets W absorbing nearly all unperturbed points (else
   the degenerate count d >= t fires the tangent strip), a thin W-family;
   conjectured bound f(r,t) independent of n. E2 data consistent with
   small f. This + the sunflower pencil lemma + the (c,S)-unique-slope
   accounting are the emerging skeleton of F5-OS's high-core side.

PROGRAM STATE: F5-OS posed (consumer-exact); sunflower stratum PROVED
<= (n-k)/t (~14.5 at the KB shape); mean + sub-mean toy windows both
clean under random AND engineered attack; the strip verified live as the
absorbing mechanism twice. OPEN: the near-pencil budget lemma (pose +
prove or refute), the low-core stratum instrument, and the W-multiplicity
aggregation for the high-core stratum.

## P6 (2026-07-07): the NEAR-PENCIL BUDGET posed; two sub-lemmas PROVED;
## the Z-mining danger channel identified and priced by window arithmetic

Setting: (u,v) = r-perturbed pencil pair: u = c0 + z0*w0 + du, v = w0 + dv
with c0, w0 codewords (deg < k) and du, dv supported on R_u, R_v,
R = R_u ∪ R_v, |R| <= 2r. For a candidate live triple (z, c, S) write
c' = c − (c0 + (z0+z) w0) (a codeword).

**NP-SUPPORT LEMMA (PROVED).** At any unperturbed x, the coincidence
c(x) = u(x) + z v(x) reads c'(x) = 0. If c' = 0 the alignment is the
pencil codeword itself, with agreement >= n − |R| — at the consumer
window that exceeds A, so it is TANGENT-column mass (charged). If
c' != 0 it has <= k−1 zeros, so |S ∩ unperturbed| <= k−1, i.e.

    every post-tangent live support satisfies  |S ∩ R| >= A − k + 1 = t+1.

**NP-VALIDITY LEMMA (PROVED).** If S ∩ R_v = ∅ then v|_S = w0|_S is a
deg<k codeword restriction, so the top coefficients of v's interpolant
on S vanish: the alignment is INVALID. Hence every valid live support
contains at least one v-perturbed point. (This kills the v-unperturbed
channel where the T-equations become z-free and every slope would go
live simultaneously — validity is load-bearing exactly here.)

**The Z-mining channel (the real attack surface).** Fix T ⊆ R with
|T| = s >= t+1 and a zero-set Z ⊆ unperturbed with |Z| = A − s; then
c' = ell_Z * g with deg g <= s − t − 1, and the T-coincidences read

    ell_Z(x) g(x) = du(x) + z dv(x),   x in T

— s equations, (s − t) + 1 unknowns (g, z): overdetermined by t − 1.
At s = t+1 (g = const): z is pinned by one Möbius relation per point
pair and must satisfy t − 1 further checks, each ~1/q: a random Z
solves with probability ~ q^-(t-1). The adversary mines Z-space:

    E[#live (z, Z) hits per T]  ~  C(n − |R|, A − t − 1) * q^-(t-1),

the SAME mean arithmetic as everything in the lane. Slope count also
caps at q − 1.

**NPB (the posed conjecture, window form).** At consumer-window rows
(the six candidates: C(n,A) q^{1-t} astronomically << 1), for every pair
within joint distance 2r of a pencil pair:

    N_post(u,v) <= C(2r, t+1)  +  o(1)-mining remainder,

i.e. the only live slopes are the finitely many the adversary can
hard-wire through T-subsets of the perturbed set; the Z-mining channel
is dead by the window arithmetic (its density q^-(t-1) times a binomial
that the window caps). Falsifier: a construction at a sub-mean row with
N_post > C(2r, t+1) sustained across scales.

**P6-E3 (next): calibrate the mining-density model** — enumerate the
FULL Z-space at a boundary row (n=24, q=73, t=3, r=4: predict ~31 hits
over <= 72 slopes) and a q-ladder control (q = 193, 577, 1153: predicted
hits 4.5 / 0.5 / 0.13 — the q^-(t-1) law measured directly); verify
every found support against the two lemmas end-to-end.

## P6-E3 (2026-07-07, run): the mining-density model CALIBRATED — the
## q^-(t-1) law measured directly

Full Z-space enumeration (167,960 sets/trial, 5 trials/row, exact
arithmetic, every hit verified end-to-end incl. both NP lemmas):

    (n,q)      predicted C(20,11)/q^2   measured hits        slopes
    (24,73)    31.5                     27,25,29,33,37       23-29
    (24,193)   4.51                     2,4,5,4,7            2-7
    (24,577)   0.50                     0,0,0,0,2            0-2
    (24,1153)  0.13                     0,0,0,1,0            0-1

FINDINGS:
1. The Z-mining channel obeys the mean arithmetic EXACTLY (q^-(t-1)
   density over the Z-binomial, 16x q-ladder) — at the six candidates
   this is astronomically << 1: the channel is dead at consumer windows.
2. Zero lemma violations: every found support had >= t+1 perturbed
   points and >= 1 v-perturbed point; every validity check behaved.
3. Everything far below the NPB budget C(2r,t+1) = 70 even at the
   mean-scale row.
4. Uniform-overdetermination observation (banked for the proof): at
   every stratum s = |S∩R| >= t+1, the T-system has s equations and
   s-t+1 unknowns — overdetermination t-1 INDEPENDENT of s. So the
   full mining mass is sum_s C(2r,s) C(n-2r, A-s) q^-(t-1) ~
   C(n,A) q^-(t-1) x (small): ONE window condition kills all strata
   simultaneously. NPB window form now rests on: NP-SUPPORT +
   NP-VALIDITY (proved) + this counting shape (to be made a lemma).

F5-OS LEDGER AFTER P6: sunflower stratum PROVED <= (n-k)/t; near-pencil
stratum: NPB posed + calibrated (proof needs the sub-mean counting lemma
for achievable ell_Z-tuples); REMAINING: the far-from-pencil generic
stratum (the F2-shaped worst-pair anti-concentration heart) + the
W-multiplicity aggregation + low-core instrument.

## P7 (2026-07-07): the counting lemma — REDUCTION PROVED; the sharp form
## identified AS the shared census kernel; conditional discharge wired

Attempting the mean-sharp counting lemma resolved into three proved
pieces and one honest barrier statement.

**P7.1 REDUCTION LEMMA (PROVED).** Fix the r-perturbed pencil pair,
T ⊆ R with |T| = s ≥ t+1, D' = D \ R, and the line
L(z) = [δ_u|_T + z·δ_v|_T] ⊂ P(F^T). Mining hits at stratum s biject
(up to the measure-zero degeneracies excluded in P6) with polynomials

    c' ≠ 0, deg ≤ k−1, with ≥ A−s distinct roots in D',
    and [c'|_T] ∈ L,

via c' = c − (c0 + (z0+z)w0) = ell_Z · g, deg g ≤ s−t−1. At the base
stratum s = t+1 (deg g = 0) this reads: hits ↔ COMPLETELY-SPLIT-over-D'
polynomials of degree k−1 lying in the explicit codimension-(t−1)
subspace V_T = eval_T^{-1}(span(δ_u|_T, δ_v|_T)). Higher strata are the
partially-split members of the same subspace family. Proof: the c'
computation of P6 in both directions; root-set ↔ monic-polynomial
bijection; the slope is read off [c'|_T] ∈ L (injective in z since
δ_v ≢ 0 on T and the δ-tuples are non-proportional). □

CONSEQUENCE: **the NPB mining remainder IS a base-field split-in-subspace
census** — the same object family as upstream's split-pencil census
(prob:capg-active-BC: split members of low-dimensional polynomial
pencils/subspaces) and the coefficient-side sibling of our F2 t-null
extras (additive/root-side). The F5 near-pencil stratum does not carry a
new hard object; it lands on the SHARED KERNEL both programs already
name as their frontier.

**P7.2 WHY THE SHARP FORM IS NOT PROVED HERE (barrier, stated honestly).**
The mean-sharp count (≈ C(n', k−1)·q^-(t-1)) is a worst-instance
anti-concentration statement for subset-product/coefficient maps — the
Q/BC class. Character/moment routes hit upstream's PROVED moment-order
floor (orders ~ w·beta/Delta needed); elementary exchange recursions
(P7.4 below) lose the window factor entirely. A two-page proof here
would breach the program-wide cancellation barrier; we do not claim it.

**P7.3 CONDITIONAL DISCHARGE (PROVED reduction of NPB).** If the row
carries a split-in-subspace census bound of the shared-kernel form —
count ≤ max(1, mean)·poly(n) for codim-(t−1) subspaces over the
generated field (upstream's BC input at the row, or the F2-class
sub-balance instance at the six candidates, where the corrected window
|B0|^t ≥ 2^n holds by ~2%) — then

    N_post(near-pencil pair) ≤ C(2r, t+1) + poly(n) · (sub-mean o(1)),

i.e. NPB holds with the budget the high-core stratum needs. So F5-OS's
near-pencil stratum is DISCHARGED MODULO THE EXISTING KERNEL: no new
red, no new object — an ev-level weld from F5 to the F2/Q/BC frontier.

**P7.4 UNCONDITIONAL EXCHANGE BOUND (proved, weak, recorded).** For
W ⊆ P_{≤m} of codim c, N(m, W) := #{Z ⊆ D', |Z| = m, ell_Z ∈ W}
satisfies m·N(m,W) ≤ C(n',m−1) + n'·N(m−1, W₂) with W₂ = {h : Λ(h) =
Λ(Xh) = 0 ∀Λ ⊥ W} (each non-degenerate Z₀ admits ≤ 1 completing root,
by linearity of Λ((X−ζ)h) in ζ; degenerate Z₀ have ell ∈ W₂). Unrolled,
this is C(n',m−1)·exponential-in-depth — poly-below-total only; it
cannot see the window. Recorded as the honest measure of what
elementary exchange buys; termination depth ≤ (m+1)/(t−1) under
Vandermonde independence of {Λ∘X^a}.

**P7-V (verification, next): the reduction bijection is machine-checked
at (24,73): #split-in-V_T counted directly on the c'-side must equal
the E3 hit counts.**

## P7-V (2026-07-07, run): the REDUCTION BIJECTION MACHINE-CHECKED

f5_p7v_reduction_check_modal.py recounts the E3 trials on the c'-side of
P7.1 (split polynomials in V_T, rank test only — no slope solving, no
gamma): counts match E3's hits DIGIT-FOR-DIGIT at both rows, all 10
trials ((24,73): 27,25,29,33,37; (24,193): 2,4,5,4,7). The validity
filter did not remove any in-V member in these trials (valid == in-V),
consistent with E3. The P7.1 reduction is verified end-to-end.

P7 CLOSES the counting-lemma question with: REDUCTION PROVED +
MACHINE-CHECKED; sharp form = the shared BC/Q census kernel (barrier
honestly cited); NPB discharged conditionally on that kernel with the
C(2r,t+1) budget. F5-OS ledger: sunflower stratum PROVED; near-pencil
stratum DISCHARGED-MODULO-KERNEL; remaining genuinely open: the
far-from-pencil anti-concentration heart + W-aggregation + low-core.

## P8 (2026-07-08): the W-MULTIPLICITY AGGREGATION INSTRUMENT — imported
## from upstream, proof-read, and machine-replayed (import, not new math)

Upstream's grande_finale.tex proves an exact saturation identity
(thm:saturation): for any word U, the size-m agreement-support census
factors EXACTLY through codeword rays,

    Cen(U; m) = sum_c C(s_c(U), m),

with the forgetful fiber above ray c exactly C(s_c, m); and the line
version (prop:line-ray-saturation): sum_z Cen(U_z; m) = sum over line
rays (z,c) of C(s_{z,c}, m), whence

    N_live_slopes <= #rays <= sum_z Cen(U_z; m).

PROOF READ (correct; elementary (T,c)-double-count: W = ell_{D\T} monic
of degree n-m pins T; N/W = c pins the codeword; W(x) != 0 on T forces
U|_T = c|_T; converse trivial). MACHINE REPLAY
(f5_p8_lineray_saturation_modal.py, 14 pairs, full enumeration, exact):
per-word identity, line identity, AND the W-scan corollary F5 actually
consumes,

    sum_{|W|=k} #{rays through W} = sum_rays C(s_{z,c}, k),

both sides counted independently — all EXACT on every pair (random +
near-pencil, n = 12/16, q = 97). Instructive datum at the n=16
near-pencil pairs: 8442 raw (W,z) pairs -> 160 rays -> 97 slopes; the
mean per-ray W-fiber 45-53 vs the guaranteed minimum C(A,k).

WHAT THE INSTRUMENT SETTLES: per-W pencil budgets (P5's sunflower
lemma) now aggregate by RAYS with an exact, known fiber factor — never
by raw (W,z) pairs; the C(n,k) naive aggregation factor was never real.
In upstream language: MCA counts a bad slope once; the support census
overcounts by exactly the saturation factor.

WHAT REMAINS OPEN IN STRATUM (i), NOW POSED SHARPLY: the high-core
stratum needs a bound on W-COLLISIONS — the number of k-cores W
carrying >= 2 live slopes (each high-core pair of family members
donates one), with per-W multiplicity already capped at (n-k)/(t-d) by
the sunflower lemma. This is a second-moment-shaped count, adjacent to
the PROVED shift-pair second-moment identity
(v13_second_moment_shift_pair_identity) — the natural next tennis ball.
F5-OS ledger after P8: sunflower PROVED; near-pencil
DISCHARGED-MODULO-KERNEL; W-aggregation INSTRUMENTED (exact bookkeeping
imported + replayed, collision count posed); remaining genuinely open:
far-from-pencil anti-concentration heart, W-collision moment, low-core
instrument.
