# The V >= 5 zero-escape occupancy question — pilot report (2026-08-03)

(Persisted verbatim by the coordinator from the pilot's final message;
the pilot's REPORT.md write was harness-blocked. Pilot: Opus 5.
Replay: tools/ramguard tiny -- python3 notes/pilots_20260803/v5_occupancy/verify.py
-> 67 checks, 0 FAIL. Q1-Q12 pre-registered with falsifiers BEFORE any
computation; all twelve came out as pre-registered.)

## THREE SEPARATE VERDICTS

1. Collapse at V >= 5 below the Cor-3b threshold: FALSE. The V=4
   pencil family extends to every V >= 4, with exact formula
   dim Ann = e := 2t - h on a Mobius locus in the slopes, 0 off it.
   Gate-clean witnesses at V = 5, 6, 10, 66.
2. rank >= 2V at V >= 5: FALSE — exact boundary 2V <= 3h. Floor
   rank >= 3h PROVED and TIGHT; ceiling rank <= 2m = 2(t+h)
   independent of V. Smallest counterexample V = 5: rank = 9 < 10 =
   2V, charge 1.8.
3. RowC 1/4: kill NOT restored, and unrestorable by any shape-only
   argument. Fixture Y5 reproduces the recorded shape exactly
   (|U|=265, k=256, |A_a|=4, V=66, triples 253) with rank = 15 = 3h
   < 18 = 2m — the collapse is false at RowC's own shape.

BONUS CATCH: the banked secondary criterion k <= 2h^2 is REFUTED;
correct replacement 2V <= 3h. The three prize rows survive by ~1e8,
now on a proved floor.

NET EFFECT: channel (i) does not close as posed, but closes where the
program needs it — at the prize rows 2V <= 3h holds by ~1e8, so
rank >= 3h gives escape-0 charge >= 3.9e8 >> 2.

## 1. The class

B(V,t,t_0,k): U = A_0 |_| A_1 |_| ... |_| A_V, |A_0| = t_0,
|A_a| = t, S_a = U \ A_a. Then |U| = t_0+Vt, A = t_0+(V-1)t,
h = A-k, m = |U|-k, sigma = |S_a^S_b^S_c| = t_0+(V-3)t, e = k-sigma.
Machine-swept over 31,746 admissible tuples:

    m = t + h ,  e = 2t - h ,  2m - 3h = e
    zero escape automatic for V >= 4
    pairwise = k + (h-t) >= k+1  <=>  h >= t+1
    gate (T) sigma = k - e <= k-1  <=>  h <= 2t-1  <=>  e >= 1

Admissible: t >= 2, t+1 <= h <= 2t-1, t_0 >= 0, V unconstrained,
k = t_0+(V-1)t-h. Band-proper depth d = h-t in [1,h-2] throughout.

## 2. LEMMA 1 (normalisation / nu-parametrisation) — PROVED

With A_1 ^ A_2 = empty, every class of Ann has a unique representative
with p_1 = p_2 = 0, and then (i) lambda = mu = 0 on U\(A_1 u A_2);
(ii) lambda = -z_2 mu on A_1, -z_1 mu on A_2; (iii) with
nu := mu|_{A_1 u A_2}, for a >= 3: p_a = 0 on S_a\(A_1 u A_2),
p_a = (z_a-z_2)nu on A_1, (z_a-z_1)nu on A_2 — and conversely.
Proof: subtract P + z_a Q with P = (z_2p_1-z_1p_2)/(z_2-z_1),
Q = (p_2-p_1)/(z_2-z_1); uniqueness since p_1,p_2 determined on
|S_a| > k points. QED

## 3. THEOREM A (ceiling, independent of V) — PROVED

m = t+h <= 3t-1, so rank <= 2m = 2(t+h) for every V; charge >= 2
forces V <= m. (Mechanism NOT new — the record's own 2m/Vmax
arithmetic; see F6.)

## 4. THEOREM B (floor; TIGHT) — PROVED

dim Ann <= e = k - sigma = 2t - h, hence rank >= 2m - e = 3h.
Generally: a disjoint block pair + any third ray c gives
dim Ann <= (k - |S_a^S_b^S_c|)^+.
Proof: by LEMMA 1 the class is determined by nu, and nu by p_3 alone;
Ann embeds in {p in F[X]_{<k} : p = 0 on S_3\(A_1 u A_2)}, a set of
sigma points, dimension (k-sigma)^+. QED
At V=4 this CONTAINS the banked (*) and PROP 6, and explains the
banked deficits: X1/X2/X3 have e = 1,1,2 and rank = 3h = 9,21,12.

## 5. THEOREM C (V >= 4 pencil-fibre classification) — PROVED

For V full fibres of a base-point-free degree-t pencil <w,w'>
(parameters c_a), any disjoint A_0, and sigma <= k-1:
dim Ann = e iff (c_a) and (z_a) are Mobius-equivalent in P^1; else 0.
(Construction p_a := kappa_a D (prod_{j>=3,j!=a} B_j) g for
deg g < e; degree fits under k EXACTLY because sigma+e-1 = k-1;
converse forces the Mobius equation.) At V=4 this is the banked
THEOREM 4(c); X1's CR = 11 reproduced.

THEOREM C' (pencil FORCED at e=1) — PROVED: if e=1 and Ann != 0, all
V blocks are fibres of <B_1,B_2>. At e >= 2 MEASURED only (F4).

## 6. THEOREM D (trichotomy — the answer) — PROVED

3h <= rank <= 2m = 2(t+h), both attained.

    2V <= 3h        charge >= 2 holds for EVERY such system (PROVED)
    2V > 2m         charge >= 2 fails for EVERY such system (PROVED)
    3h < 2V <= 2m   holds generically, FAILS on the pencil family

Answer: NO, with exact boundary 2V <= 3h.

## 7. Fixtures (all machine-verified)

Reformulation lemma: the GRS isomorphism C_U ~ F[X]_{<m} carries
C_{S_a} onto B_a F[X]_{<h}, so rank = dim span{(B_aX^i, z_aB_aX^i)}.

    Y1  q=11  V=5  t=2 t_0=0 k=5  |U|=10 h=3 m=5 e=1 dimAnn=1 rank=9  charge 1.80
    Y2/Y2b (non-pencil / off-Mobius): rank=10, charge 2.00
    Y3  q=13  V=6: rank=10 (COLLAPSED) yet charge 1.67
    Y3' q=13  V=6 pencil: rank=9, charge 1.50
    Y4  q=41  V=10 t=4 t_0=1 k=32: rank=15=3h, charge 1.50
    Y5  q=269 V=66 t=4 t_0=1 k=256 (RowC replica): rank=15=3h < 18=2m, charge 0.227
    Y6  q=269 V=66 same supports off-Mobius: rank=18=2m, charge 0.273

All gate-clean; band-proper d = 1. Section E: exhaustive sweep, 3,024
slope tuples modulo affine over 6 pairings of F_11^* — dim Ann > 0
EXACTLY on the Mobius orbit; only 6 of 945 pairings are pencils.
Section J (exploratory): at e=2 the pencil fixture breaks the collapse
while keeping charge 2 — the two conclusions are separable.

## 8. RowC 1/4 (task #33)

The record's clique model (stage5_escape.py section D: u = k+2h-d,
Vmax = u//(h-d), m = 2h-d) IS B(V,t,t_0,k) with t = h-d —
machine-verified against stage5_escape.json for all six rows. RowC 1/4
is (h,d) = (5,1) => t=4, t_0=1, m=9, e=3, sigma=253.

Verdict: NOT restored; stays OPEN; cannot be closed by a shape-only
argument. The kill consumes the collapse as structural uniqueness
(rank = 2m => joint explanation); Y5 reproduces the recorded shape
exactly with rank = 15 < 18 (deficit exactly e = 3 — the same slack
by which THEOREM 3 misses, 256-253); Y6 shares every recorded
invariant and collapses. The shape decides nothing; the support-pencil
and the slopes do. Charge route definitively dead at RowC (ceiling
0.273, floor 0.227). Honest limit: RowC's supports are code-determined
and its field unpinned; whether the actual blocks are degree-4 pencil
fibres is undecided here.

## 9. The catch: k <= 2h^2 is REFUTED

proof.md:140-145 / support4_relation/REPORT.md:63-66 /
stage5_escape.py:16-17: "the zero-escape channel can reach per-ray
charge < 2 only when k > 2h^2". Its computation is charge := 2m/Vmax —
the CEILING divided by V; an upper bound cannot certify a lower bound.
Refuted at the smallest fixture: Y1 IS the record's own clique at
(k,h,d) = (5,3,1) with V = Vmax = 5; k = 5 <= 2h^2 = 18 holds, true
charge 1.8 < 2. Corrected criterion: 2V <= 3h. Row table: RowC
1/4 / 1/8 / 1/16 all FAIL both criteria (ceiling charges 0.273 /
0.529 / 0.294); prize 1/4 / 1/8 / 1/16 PASS with 3h/2 ~ 1.3e10 vs
Vmax <= 66. Prize rows survive on the proved floor; no prize-row
number moves.

## 10. Beyond block systems

For V = 5, zero escape forces empty triple-block intersections, so
inclusion-exclusion gives, for ANY gate-clean V=5 zero-escape system,
m <= 3h - 4 (PROVED). The record's model (m = 2h-d) forces disjoint
blocks exactly (|A_a ^ A_b| = m - 2h + d_ab).

## 11. FLAGS

F1 banked criterion k <= 2h^2 refuted in three locations + JSON field;
surfaced, not applied. F2 task #33 cannot succeed as posed. F3 scope:
block systems (forced in the record's model); general V >= 6
overlapping blocks not covered; V=5 general bound only. F4 pencil
converse at e >= 2 measured only. F5 realisability inherited: gates
combinatorial, no band-gate (u,v), toy fields q <= 269; full-gate
realisation = COMPUTE REQUEST. F6 novelty subtraction: THEOREM A =
record's own arithmetic (concordance); new = tight 3h floor, V >= 5
construction, dim Ann = 2t-h, trichotomy, F1 catch. F7 Y5 is a
replica over F_269. F8 compute law kept (tiny 4.2 s; one local sweep
2.4 s). F9 whether 0 < dim Ann < e occurs off-pencil is OPEN.

## 12. What this leaves for the heart

Channel (i) is DECIDED: charge >= 2 iff 2V <= 3h, proved both ways;
at the prize rows it holds by ~1e8, so the channel is closed THERE —
which is what the band TARGET consumes. The collapse is dead at every
V >= 4; every consumer needing rank = 2m must be re-derived from a
THEOREM 2/3 certificate. Remaining open channel: escape-1 core rays.
