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
