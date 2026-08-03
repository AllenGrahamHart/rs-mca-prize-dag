# F9 — PENCIL FORCING AT V >= 5 — pre-registration

Opus 5 proof pilot, 2026-08-03. WRITTEN BEFORE ANY COMPUTATION IN THIS
PILOT (no verify.py exists yet). Sibling machinery (zero_escape_collapse,
v5_occupancy, la_pencil_rigidity, unified_pencil_bound) is read-only.

## 0. ADJUDICATION OF THE STATEMENT (done first, from the banked reports)

v5_occupancy flag F9 as literally worded — "does 0 < dim Ann < e occur
off-pencil?" — is ALREADY ANSWERED **YES** by la_pencil_rigidity's W1
(e=2, dim Ann = 1, span{B_a} = 3) and W2 (e=3, dim Ann = 1, span = 4),
both gate-clean zero-escape non-pencil systems at V = 4. So the literal
F9 is CLOSED-YES and is NOT what the anchor consumes. Recorded as a
discrepancy for the coordinator (D1 below).

What the C = 1/2 anchor's pinning actually consumes (unified_pencil_bound
Q6/FABLE_AUDIT: "realisable family => every 3+3 subfamily realisable =>
C' forces one pencil at e=1 => M <= 1"): the pinning subfamily is the
union of two pencil-structured live families of size >= 3 each, and what
must be contradicted is that such a union can be non-collapsing. Hence

  **T0 (ANCHOR-EXACT).** For a gate-clean zero-escape system with V >= 5
  blocks and dim Ann >= 1, the blocks CANNOT be covered by two DISTINCT
  pencils carrying >= 3 blocks each.  [T0 <=> M <= 1 <=> C = 1/2.]

  **T1 (ANCHOR-SUFFICIENT).** Same hypotheses => at least V-1 of the V
  blocks are fibres of ONE pencil.   T1 => T0.
  (Proof of T1=>T0: a second pencil family of size >= 3 has <= 1 block
  off P, so >= 2 blocks in P; two distinct blocks of P span P; so the
  second pencil = P. V-1 is sharp: "V-2 in one pencil" does NOT imply
  T0.)

  **T2 (LITERAL FORCING, the task's proposed wording).** Same hypotheses
  => ALL V blocks are fibres of one pencil. T2 => T1 => T0.
  This is la_pencil_rigidity's residual F3 (1 <= dim G < e, Z non-empty,
  V >= 5).

I attack T2 first, then fall back T2 -> T1 -> T0. The anchor needs only
T0; anything weaker than T0 degrades C.

Two further prerequisites of the reduction, registered here because the
banked chain does not contain them:

  **P-SHARE.** Two DISTINCT pencil-structured live families share at most
  ONE live slope. (unified PREREG Q5 registers "<= 2 common fibres";
  if 2 were possible the pinning subfamily could be V = 4 — exactly the
  proved no-content regime where W1/W2 live, and the anchor's reduction
  would be void. So <= 1 is load-bearing.) PREDICTION: TRUE, with proof
  sketch: two shared slopes z,z' give A_z ^ A_z' = A_0 = A_0' (cores
  equal, since blocks inside a family are disjoint), then the two shared
  blocks are fibres of both pencils and a degree-s poly is determined up
  to scalar by its s distinct roots, so both pencils equal the span.
  FALSIFIER F9-FS: two distinct pencil-structured families sharing 2
  live slopes.

  **P-DISJ.** The pinning subfamily's complements are pairwise disjoint
  outside a common core (i.e. it is a BLOCK system in the sense of
  v5_occupancy/la). NOT automatic at V >= 5 (the gate only forces each
  point into <= V-3 blocks). Registered as an inherited gap (la's FC
  sweeps found no non-collapsing overlapping system, e = 2, V = 5, toy).
  I will test the anchor-relevant overlap shape, not close it.

## 1. Definitions of record

B(V,t,t_0,k) exactly as v5_occupancy: U = A_0 |_| A_1 |_| ... |_| A_V,
|A_0| = t_0, |A_a| = t, S_a = U \ A_a, distinct slopes z_a, sigma =
t_0+(V-3)t, e = k - sigma = 2t - h, m = t+h, gates t >= 2,
t+1 <= h <= 2t-1. B_a := prod_{x in A_a}(X - x). Ann as in zec.ann_dim.
"Pencil": all B_a in one 2-dimensional subspace of F[X]_{<=t}.

Normalisation at an ordered pair (i,j) (LEMMA 1 of v5, valid for ANY
pair since blocks are disjoint): w in F^{A_i u A_j}, w != 0, and
g_a in F[X]_{<e} for a not in {i,j} with

    (POINT)  w B_a = g'_a on A_i ,  w B_a = lambda_a g'_a on A_2 ,
    g'_a := g_a/(z_a - z_j) ,  lambda_a := (z_a - z_j)/(z_a - z_i).

Z := {x in A_i u A_j : w(x) = 0} = common zero set of all g_a there;
Z_i := Z ^ A_i, Z_j := Z ^ A_j; d_{ij} := dim span{g'_a}; the lambda_a
are DISTINCT (Moebius image of distinct slopes) and every g'_a != 0
(else w = 0).

## 2. Pre-registered claims, predictions, falsifiers

**Q1 (r-formula).** For blocks with distinct lambda_a and g'_a != 0:
dim span{B_a : a not in {i,j}} = 2 <=> d_{ij} = 1, whenever there are
>= 3 such blocks (i.e. V >= 5). PREDICTION: TRUE (proof: the vectors
(g'_a, lambda_a g'_a) in G+G; if two g' are independent any third
non-zero g' produces a third independent vector).
FALSIFIER F9-F1: a fixture with 3 blocks off the pair, non-proportional
g's, and span 2 (or proportional g's and span >= 3).

**Q2 (all-lambda dichotomy).** If >= 2 blocks off the pair share a
g-direction g, then X_lambda := {f in F[X]_{<=t} : w f = c g on A_i,
w f = c lambda g on A_j} is non-zero for EVERY lambda, and every block
with that direction is a fibre of the single pencil <f_0, f_1>,
f_0 = B_j^Z s_0 (deg s_0 <= |Z_j|), f_1 = B_i^Z s_1 (deg s_1 <= |Z_i|),
where B_i^Z := prod_{x in A_i \ Z_i}(X - x).
PREDICTION: TRUE (the admissibility conditions are affine in lambda; two
roots kill both coefficients).
FALSIFIER F9-F2: a fixture where exactly 2 <= #{admissible lambda} < q.

**Q3 (T2 at V >= 5) — THE HEADLINE.** PREDICTION: **FALSE**. I predict I
can CONSTRUCT a gate-clean zero-escape NON-PENCIL system with V >= 5 and
dim Ann >= 1, from Q2's normal form, namely (registered in full BEFORE
running so the fixture cannot be retro-fitted):

    t = 3, e = 2, h = 4, |Z| = 1: pick A_1, A_2 disjoint 3-sets,
    x_0 in A_1, y outside A_1 u A_2; set f_0 := B_2,
    f_1 := (B_1/(X-x_0))(X-y), g := X - x_0,
    w := g/f_0 on A_1\{x_0}, 0 at x_0, g/f_1 on A_2;
    take the blocks A_3, A_4, A_5 (, A_6) to be root sets of SPLIT
    members f_0 + lambda f_1 (lambda avoiding 0, -1, infinity and the
    root of f_0(x_0) + lambda f_1(x_0)); slopes z_a from lambda_a.
    B_1 is NOT in <f_0,f_1> iff y != x_0, so span{B_a} = 3.

  Why this evades la_pencil_rigidity's 700 + 310 partition sweeps
  (pre-registered): the sweeps draw RANDOM partitions and then sweep all
  slope tuples; "4 of the 5 blocks lie in one pencil" is a codimension-4
  condition on the partition, so the expected number of hits in 700
  random partitions over F_19 is ~ 700/19^4 ~ 5e-3. Their D-route
  (extend a V=4 hit) is exhaustive but was run at q = 13,17,19 (t=3)
  and 23,29 (t=4) where 4 blocks already use 12 resp. 16 of the q
  points, so a 5th disjoint block usually cannot fit. I therefore run
  at q >= 31 (t=3) and q >= 41 (t=4).
  PREDICTION: fixtures found at (t,e) = (3,2) and (4,3), V = 5 and 6.
FALSIFIER F9-F3: if the construction yields NO gate-clean non-pencil
V >= 5 system after an exhaustive scan of the registered families over
q in {31,37,41,43,53,61,71,101}, T2 stands and I report it PROVED-BY-
EXHAUSTION-plus-argument (and must then prove it, not assert it).

**Q4 (T1 at V >= 5).** PREDICTION: TRUE. In the Q2 normal form B_j is a
fibre of <f_0,f_1> iff Z_j = empty, so with Z concentrated in one block
exactly ONE block (B_i) escapes and V-1 lie in one pencil.
FALSIFIER F9-F4 (the "2-rogue" fixture): a gate-clean V >= 5 system with
dim Ann >= 1 in which only V-2 blocks lie in one pencil. Registered
search: e >= 3 (needs |Z| >= 2), |Z_1| = |Z_2| = 1, t = 4,5, q <= 151.
PREDICTION: 2-rogue systems EXIST combinatorially (the construction has
free parameters s_0, s_1) — so I expect F9-F4 to FIRE and T1 to be
FALSE. I register this expectation now, and with it that the verdict
will then rest on T0.

**Q5 (T0 — the anchor).** PREDICTION: TRUE, with this proof route: in
the Q2 normal form, a SECOND pencil family of size >= 3 forces a third
block B in <B_i,B_j>; writing B = alpha B_i + beta B_j and pushing it
through (POINT) gives alpha * prod_{Z_i}(X-x) * s_0 = c * lambda *
prod_{Z_j}(X-x) * s_1, which forces s_1 ~ prod_{Z_i}(X-x) (i.e. B_i in
the first pencil, so the two pencils coincide) or alpha = 0 (i.e. B is
not a new block). Hence M <= 1 and C = 1/2 SURVIVE even when T2/T1 fail.
FALSIFIER F9-F5 (kills the anchor): a gate-clean zero-escape V >= 5
system with dim Ann >= 1 whose blocks are covered by two DISTINCT
pencils with >= 3 blocks each. Registered search: exhaustive over the
Q2 normal form at (t,e) = (3,2),(4,3),(5,4) and a direct two-pencil
sweep (pick P, P', 3 fibres each, test the gate and zec.ann_dim).

**Q6 (degradation).** If F9-F5 fires, C degrades to M_0/2 with M_0 the
observed pencil count; I will report the largest M_0 realised and the
best C I can PROVE, never the best C I hope for.

**Q7 (replay).** Every claimed theorem is replayed against the banked
fixtures W1, W2 (la), X1-X3 (zec), Y1-Y6 (v5) and against the la V >= 5
sweeps: any theorem that contradicts a banked fixture is retracted.
FALSIFIER F9-F7: disagreement between my reduction and zec.ann_dim /
zec.rank_row on ANY fixture.

**Q8 (honesty about the la record).** I additionally register two
suspected LOOSENESSES in la_pencil_rigidity's REPORT, to be confirmed or
withdrawn: (a) "at V >= 5, dim G = e forces >= V-1 blocks into
<B_1,B_2>" — the count of blocks b with dim G_b = e is (V-2) - #essential
and #essential can be as large as e, so the correct statement is
>= V-2-e blocks (only e <= 1 gives V-1); (b) the V >= 5 non-existence
evidence (700 + 310 partitions) is a random-partition search over a
codimension-4 locus and is therefore not evidence of absence.

## 3. Compute law
tools/ramguard tiny|local -- python3 ... from the repo root, literal --.
No Modal, no network. All sibling machinery imported READ-ONLY.

## 4. Honesty rules
In-run amendments are appended below with a timestamp and reason, never
by editing the text above. Fixture-level surprises are reported even
when no registered falsifier fires. Every fixture is audited by BANKED
code (zec.ann_dim, zec.rank_row) independently of my reduction.

## IN-RUN AMENDMENT 1 (2026-08-03, after the first full run)

Check E2 as first written FAILED (12 of 18 fixtures) and the CHECK, not the
lemma, was wrong. E2 asserted "the escape pencil P' and P = <B_1,B_2> meet
only in 0". That is the conclusion of LEMMA 5 only under the hypothesis
B_1, B_2 not in P' — which is exactly the hypothesis T0's proof arranges by
choosing the normalising pair inside F \ F'. My constructed fixtures are
1-rogue systems, where B_2 IS a fibre of P' (Z_2 empty => s_0 ~ zeta_2), so
they violate that hypothesis and a 1-dimensional intersection <B_2> is the
PREDICTED behaviour. Corrected statement, checked from here on:

  LEMMA 5. P' ^ <B_i,B_j> is 0 unless s_0 ~ zeta_j (then it is <B_j>) or
  s_1 ~ zeta_i (then it is <B_i>); in every case it contains NO third
  block. [Proof: h = c_0 f_0 + c_1 f_1 = alpha B_i + beta B_j gives
  B_j^Z (c_0 s_0 - beta zeta_j) = B_i^Z (alpha zeta_i - c_1 s_1), and
  gcd(B_i^Z, B_j^Z) = 1 with deg <= |Z_j| < t - |Z_i| = deg B_i^Z forces
  c_0 s_0 = beta zeta_j and c_1 s_1 = alpha zeta_i.]

The failed run is kept in the record; the original E2 wording is preserved
above. New checks E2a/E2b/E2c test the corrected form, and section H is
ADDED (not registered in advance, and reported as such): an adversarial
two-pencil realisability sweep that tests F9-F5 directly, independently of
my normal form, and covers the (t,e) = (5,4) regime where T0's case (b)
argument has its degree residual.
