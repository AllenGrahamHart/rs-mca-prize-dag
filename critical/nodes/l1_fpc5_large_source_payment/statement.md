# L1 FPC5 large-source payment

- **status:** TARGET
- **consumer:** `l1_full_petal_fpc5_payment`

After the official small-source sieve, the remaining large source scales are

```text
rate 1/2:   M>=5,
rate 1/4:   M>=5,
rate 1/8:   M>=7,
rate 1/16:  M>=15.
```

Every cell satisfies

```text
2<=t<2M-4,       d<ell(M-2),
max(0,2d+1-t ell)->infinity.
```

The target is one disjoint polynomial/profile allocation across first-owned
sources, touched-petal sets, defects, and exact owners. Raw enumeration of
sources or touched subsets is not an admissible payment.

## Exact proved prefilter

The proved node `l1_fpc5_large_source_exact_prefilter` now separates the
bookkeeping reductions from the aggregate target. For every fixed source,
touched set, and defect degree, put

```text
h=t ell,       r=2d-h,       u=d-(t-1)ell.
```

The cell is empty if `u>b`, is a singleton if `r<0` or
`2d>N+(t-2)ell+b`, and is polynomially paid whenever either the ordinary or
joint-background Johnson denominator is positive. Hence the only live fixed
cells satisfy the exact residual `(PF6)` in that supplier. This reduction is
uniform over every official `ell`; the sampled EMPTY/SINGLETON percentages
below remain evidence and are not used as theorem premises.

The proved node `l1_fpc5_tpetal_saturated_slice_dimension` also removes the
general-`t` linearization gap. Every nonempty survivor has

```text
e=2d+1-t ell=r+1>=1,       t ell>d,
```

so its guarded pair slice projects isomorphically to a locator space of
dimension `e+1`, with a monic affine `e`-flat. Thus every surviving fixed
cell is a correctly typed split-locator max-to-mean instance. The open
content is the uniform split-point and aggregate owner/profile payment, not
the existence or dimension of the flat.

The proved node `l1_fpc5_tpetal_anchor_coordinate` removes the remaining
fixed-pair multiplicity. Relative to one exact anchor `(F,W)`,

```text
H=(FB-GW)/Lambda,       deg H<=e-1,
```

is an affine coordinate on the complete monic pair chart, and every exact
member obeys

```text
gcd(H,F)=gcd(G,F).
```

Thus all fixed common-defect owners are gcd strata of one coordinate body at
every `t`. The target must count the coordinates whose reconstructed locator
splits and passes the exact guards, aggregated without summing independent
owner pencils.

The proved node `l1_fpc5_tpetal_anchor_pade_chart` makes that reconstruction
explicit. If `I=W^(-1) mod F`, then

```text
G_H=F+rem_F(-Lambda H I),
B_H=(G_H W+Lambda H)/F.
```

The primitive condition is an exact root-local nonvanishing test in `H` and
`H'`. Hence the remaining fixed-cell object is a typed primitive
split-remainder maximum; it is not an implicit coefficient or pair-counting
problem.

The proved node `l1_fpc5_tpetal_joint_anchor_owner` also incorporates the
background guard. If `R_0` is the anchor's background zero set, then

```text
gcd(H,F L_(R_0))
```

simultaneously recovers the candidate's common defect roots and common
background roots with the anchor. Every other background root is one printed
affine equation in `H`. Thus fixed defect and background owners must be
treated as one coordinate stratum, not independently summed ledgers.

The proved node `l1_fpc5_tpetal_joint_owner_packing` pays every fixed joint
owner by

```text
binom(N+b-q,r-q+1) / binom(d+max(0,u)-q,r-q+1).
```

In particular, every bounded co-deficiency owner `q=r-O(1)` is polynomial
per owner. The exact small-cell owner probe shows that realized owner groups
are usually singletons, so a bounded-owner coalescence theorem is not a
credible aggregate route.

The proved node `l1_fpc5_tpetal_joint_owner_ambient_mds_census` makes that
route cut exact in the complete monic chart. If

```text
P_0=F L_(R_0),       p=deg P_0,
```

then the owner zeros are the zero support of the degree-at-most-`r`
Reed-Solomon evaluation word `H|Z(P_0)`, up to nonzero diagonal scaling.
Every degree-`r` divisor `Q|P_0` occurs as a top owner with exactly
`|mathbb F|-1` ambient chart points, for a total of

```text
binom(p,r)(|mathbb F|-1).
```

These ambient pairs need not have split locators or pass the guards. The
theorem therefore forbids owner-only and unguarded-linear coalescence; the
simultaneous split-and-guard predicate must supply the full saving.

The proved node `l1_fpc5_tpetal_owner_free_cauchy_divisor_chart` now prints
that simultaneous predicate without choosing an anchor. If `chi` is the
CRT multiplier equal to `c_i` modulo `L_i`, every core-split locator `G`
reconstructs as

```text
B_G=rem_Lambda(chi G).
```

The condition `deg B_G<=d` is exactly a block of `h-d-1` weighted moments
on the petal roots. Primitivity is nonvanishing of the punctured zeroth
moment at each root of `G`, and every background agreement is one explicit
Cauchy-transform zero. Equivalently, with `A=L_Core/G`, the complete cell
is one weighted reciprocal-divisor census over `A|L_Core`. This formulation
retains the predicates omitted by the ambient MDS theorem and does not sum
owners independently.

The proved node `l1_fpc5_tpetal_cauchy_hankel_kernel` identifies the linear
part of that census more sharply. If

```text
mu_s=sum_(z in T)c(z)z^s/Lambda'(z),
```

then the coefficient vector of `G=sum g_a X^a` lies in the full-row-rank
Hankel kernel

```text
sum_a mu_(j+a)g_a=0,       0<=j<h-d-1.
```

The moment generating function is `chi/Lambda` at infinity and obeys the
exact `Lambda` recurrence. Thus the remaining flat is not arbitrary: it is
a rational Pade-Hankel kernel intersected with the core divisors, with
punctured first-row primitive tests and background Cauchy guards.

For `u=d-(t-1)ell>=0`, the proved node
`l1_fpc5_tpetal_fixed_background_hankel_codimension` moves any fixed
required `u`-set `R` of background zeros into the same CRT/Hankel system by
giving it label zero. The augmented block has exactly

```text
t ell+u-d-1=ell-1
```

full-rank rows, locator dimension `d-ell+2`, and monic codimension
`ell-1`, independently of `t` and `u`. The exact incidence sum weights a
candidate by `binom(|R_H|,u)`; a first-`R` rule is disjoint but no longer a
complete linear chart. Thus the background threshold is now normalized,
but its aggregate payment remains open.

The proved node `l1_fpc5_tpetal_hankel_support_determinantal_system`
imports Przemek's generalized-Vandermonde criterion and makes the support
geometry explicit. Each Hankel row is one determinant equation on the
selected core roots and moment column. If `w_i` is the corresponding Cramer
amplitude, then

```text
M_0(G/(X-x_i))=w_i G'(x_i),
```

so the primitive puncture is exactly `w_i!=0`. The fixed-background local
target is therefore a printed quasi-affine determinantal point count modulo
support permutations, with the remaining background and chronology filters
still visible.

The proved node `l1_fpc5_tpetal_hankel_grs_syndrome_shell` imports the exact
upstream syndrome-locator bijection. For locator degree `d` and `c` Hankel
rows, put `D=d+c`. Primitive split locators are exactly the weight-`d`
vectors in one syndrome coset of the `D`-row weighted Vandermonde check on
the `N` core points. If `D<N`, this is the exact radius-`d` shell of

```text
RS[F,Core,N-D];
```

if `D>=N`, each fixed chart contains at most one primitive locator. In the
fixed-background branch `c=ell-1`, so `D=d+ell-1`, and the MDS distance
recovers the sharp support-overlap cap `d-ell`. This identifies the
noninjective local wall with an ordinary GRS exact-list shell rather than a
new Hankel-only object. It does not coalesce the required background sets or
pay the guarded/chronology aggregate.

The proved node `l1_fpc5_tpetal_joint_owner_split_pencil` gives the
replacement terminal. Factor the exact owner as `Q=DE`, remove `D` from the
two core locators and `E` from the two background numerators, and write
`H=DEK`. Then

```text
A V-C U=Lambda K,       deg K<=r-deg Q.
```

The two reduced columns are primitive, the locator entries remain
squarefree and split, and all petal congruences survive explicitly. Within
one fixed owner chamber and relative to one member,

```text
K_0(C,V)=K(C_0,V_0)+T(A,U),       deg K,deg T<=r-deg Q.
```

At top ownership this is an ordinary affine pencil of locators split on the
core, coupled to a scalar determinant of the disjoint touched-petal locator.
Bounded co-deficiency gives a bounded-degree rational pencil. The unresolved
issue is therefore a uniform dual-domain simultaneous split-and-guard census and
chronology-valid aggregation across many distinct owners, not a missing
owner coordinate or an expected small number of realized owners.

## Round-23 diagnosis addendum (2026-08-07, coordinator-applied on replay: fpc5_diag)

**CLASSIFICATION: MYSTERY-HARD, and the LEAST DEFENDED of the three
FPC5 reds** (the registered exposure test FIRED as pre-registered —
an exposure, not a witness; the partition stands). Same wall (MF)
plus two missing pieces the m4 reds already have: (i) NO mu-basis /
overlap-cap theorem exists for t >= 4 (the three-petal theorems do
not generalize as stated; even the Johnson functional J is
undefined there); (ii) NO background-guard analogue at M >= 5.
**[Claim (ii) is FALSE — round-25 forced correction below, the
same mechanism that felled claim (i) in round 24.]**
Exact facts established: t <= M always (so the rate-quarter
uniqueness template applies exactly on the t = M, b <= 1 stratum
and nowhere else); touched-subset multiplicity is FREE
(binom(M,t) <= n^{1/c_0} by the layout-domination cutoff — the
attack note's first line aims at a non-obstruction); the exact
Johnson sieve at k = 2^40 leaves **408 residual rows** across the
four rates (all t at M >= 10), with e reaching n/3 — e.g. rate
1/2, M = 5, t = 2: a residual d-window of width 3.48e11.

**THE NAMED GATE (cheapest decisive probe):** prove the t-petal
overlap-cap lemma — for distinct primitive members of the t-petal
slice, |Z(F) cap Z(F')| <= e - 1 (the cofactor/syzygy determinant
argument, PROVED verbatim at t = 2 and t = 3). The moment it
lands, the entire J-sieve becomes legal and removes every
t < M, J > 0 cell at a stroke; the sieve table is already computed
and waiting (fpc5_exact.py). Second: port the m4_t2
background-guard collapse to general M — the codim = sigma
identity predicts the answer in advance.
Source: notes/pilots_20260807/fpc5_diag/.

## Round-23b adjudication note (2026-08-07, coordinator-applied on replay: mf_wall_adversary)

The round-23 one-wall evidence is REPRICED under adversarial attack:
the statement-level (MF) shape-pun test FAILED its power control
(the PROVED rate-quarter sibling satisfies every (MF) clause with
better margins; the separating clause — over-determination
t*ell > N — is not part of (MF)), and the two quantitative handles
are WITHDRAWN as classification evidence (the cap-4 is
structure-specific — a random flat with identical parameters
reaches 5; the trivial-owner concentration is 92x its parametric
reference). Both remain valid node-level findings, and the cap-4
data is STRENGTHENED (exact, not sampled, at ell = 4, 5, 6 over
329 configs and three primes; the sharpened overlap cap ell-3
achieved tightly at every ell; the cap is soft — budget elasticity
+1..+4 core points — and stiffens with ell; the mechanism at
ell >= 5 is UNIDENTIFIED). The REPAIRED test (round-19 three
gates, METHOD = the-missing-theorem-is-the-same; passed all three
power controls incl. the PROVED-sibling hard control): the m4_t2
and m4_t3 reds SHARE ONE WALL at METHOD level — a
dimension-uniform max-to-mean bound for split locators in a
growing-dimensional flat (the anticode bound's exponent grows with
flat dimension). The same METHOD wall matches the PROVED
l1_rootfree_rational_q_projective_packing at its own open
d = Theta(n) regime and f_global_packing_step (identical formula,
identically named failure). The large-source red is UNDECIDED:
only 142/408 residual rows are even posable as flats; the other
266 await the t-petal overlap-cap lemma. Upstream
prob:capfr1-master-flatness has ZERO discriminating power as a
wall test (PROVED nodes are instances of it; (MF) is an instance,
not the same statement; a |B|^{-s} vs q^{-sigma} normalization
mismatch is unresolved). Source:
notes/pilots_20260807/mf_wall_adversary/ (coordinator-replayed).

## Round-24 FORCED CORRECTION (2026-08-08, coordinator-applied on replay: t_petal_lemma)

**Claim (i) of the round-23 addendum is FALSE in both clauses.** The
t-petal overlap-cap theorem EXISTS at arbitrary support size: it is
clause (JB3) of the PROVED background node
l1_fixed_support_defect_johnson_bound (r_J = 2d - h; put h = t*ell
and (JB3) reads |Z(F) cap Z(F')| <= e-1 verbatim), and the Johnson
functional J is exactly (JB4)'s denominator d^2 - N*r_J. The gap was
BOOKKEEPING (the argument existed under six names while three
round-23 artifacts recorded it as missing). Verified: the node's
verifier replayed; a self-contained general-t proof (5 elementary
steps, degree-counting — the mu-basis/syzygy budget is never
needed) at notes/pilots_20260808/t_petal_lemma/
LEMMA_TPETAL_OVERLAP_CAP.md, coordinator-read; refutation search 0
violations with MIN_SLACK = 0 (the cap ATTAINED at t = 4, 5, 6 —
the search has resolution) and the power control fired on 2/3
broken arms. CONSEQUENCES, executed and replayed: the J-sieve is
LEGAL at every t (all 674 grid rows have a defined functional; the
156 t >= 4 rows previously paid ILLEGALLY are now legally paid;
residual = 408 exactly as computed). Claim (ii) may ALSO be
mis-stated: (CJ2)/(CJ3) of l1_joint_core_background_johnson_bound
is proved at arbitrary h and would rescue 71 residual rows — its
chart hypotheses at M >= 5 are UNAUDITED (the named next probe).
NEW THEOREM (draft for minting, machine-checked at 391 cells +
proved): dim V = e+1 at EVERY t (the slice-dimension theorem via
the cross-determinant map E(G,B) = (FB-GW)/Lambda — kernel exactly
the line K(F,W)) — the t >= 4 rows are now POSABLE AS FLATS, so
red 3's mystery-7 membership is DECIDABLE. Bonus (proved +
machine-checked): the core/petal disjointness hypothesis is FREE
for primitive members.

## Round-25 forced correction (2026-08-09, coordinator-applied on replay: m7_complement_repose)

**Claim (ii) of the round-23 diagnosis is FALSE — the named next
probe is DONE and DECIDED: the (CJ2)/(CJ3) chart hypotheses of
l1_joint_core_background_johnson_bound TRANSFER at M >= 5**, by
the same bookkeeping mechanism that made claim (i) false in round
24. Hypothesis ledger over all 408 residual rows: background
capacity 0 <= b < ell — 0 failures (the sieve's b IS the node's
background capacity; measured b in [0, 5.13e11] against ell in
[6.47e10, 5.31e11]); g = ell-b >= 1 — 0; r = 2d-h >= 0 — 0;
core/petal/background pairwise disjoint — 0, verified
ARITHMETICALLY at every rate ((k-1)+S = rate·k and S = M·ell+b
hold identically, so core and source partition the ambient);
N = k-1 — 0. The only binding condition is the list threshold
h >= d+g, which is ALGEBRAICALLY the round-24 u <= b correction
under another name (u = d-(t-1)ell <= b iff t·ell >= d+ell-b).
Replay MATCHED exactly in two independent paths: **71 of 408
residual rows rescued, 3,972,788,690,368 d-values = 1.97% of
residual d-mass** (coordinator replay byte-identical).

**Honest scope:** the rescue is PARTIAL on every row (max 74.2% of
any one row's d-window; 0 rows fully rescued; the residual row
count stays 408). Coverage: t = 2..5, M = 5..18, rates 1/2 (24
rows), 1/4 (39), 1/8 (8); **rate 1/16 gets nothing.** (CJ4) gives
m <= 97 on the leading sampled row and m up to 2.33e13 across the
71, all <= n^3 — a defined finite payment exists, not a cheap one.
With both (i) and (ii) of the round-23 diagnosis now false, this
red's "least defended of the three" classification rests solely on
the MF wall itself. Source:
notes/pilots_20260809/m7_complement_repose/ (d4_cj3_audit.py,
replayed byte-identical by the coordinator).

## Round-26 addendum (2026-08-09, coordinator-applied on replay: m7_falsifier_hunt — the sharp cap, the EMPTY charge, red 3 undecided)

**(1) THE SHARP OVERLAP CAP (a corollary of this chain's own
(CJ2), un-summed — NOT new mathematics, never before drawn):**
guarded overlap max = r_J - |R_1 cap R_2| <= r_J - max(0, 2u-b),
and EXACTLY d - ell at u = b. Verified 0 violations in 8336 exact
configs across 25 cells (rates 1/2..1/16, M = 5..120, t in {2,3}),
ATTAINED at every cell with m>=2. Consequence: THE PENCIL STRATUM
IS DELETED — split-only members reach r_J = d-1 in quantity (up to
52% of pairs) while guarded contributors reach it 0/8336, and
PENCIL_MAX = 1 everywhere; round-25's config-18 sunflower deletion
is systematic at M >= 5 and now explained. The registered
codimension identity (dim V = d-ell+2; the round-24
slice-dimension theorem = its u=0 case) held 28/28.

**(2) THE EMPTY CHARGE (the third instance of the bookkeeping
mechanism that felled claims (i) and (ii) — REPLAYED, NOT YET
ADOPTED):** the sieve of record (p7_large_source_sieve) caps d at
min(ell(M-2)-1, N) only, and never charges this node's own list
threshold. Charging it (u = d-(t-1)ell > b means the forced
background agreements exceed |B| — no contributor can exist;
coordinator-verified logic): **71.380% of the residual d-mass is
EMPTY** (143,981,892,664,856 of 201,710,563,424,605 d-values; 35
of 408 rows entirely empty) **plus 0.679% SINGLETON by the PROVED
l1_background_overlap_singleton_payment (BO2)** (disjoint from
EMPTY by construction; 39 rows entirely paid) — versus the 1.97%
CJ3 rescue banked in round 25, on the identical denominator.
Residual after EMPTY + SINGLETON: 27.94%. Rate 1/16 has NO
residual rows at all (why the CJ rescue "got nothing" there). The
pilot's own (SING) derivation was caught by its CATCH-24A grep as
a re-derivation of (BO2) and is credited as such. CAVEATS
(binding before adoption): the denominator is the banked 3-point
ell-sample, counts (row,d) cells not distinct d (a d killed at
small t may live at larger t), and the CJ3/SINGLETON band overlap
is UNCOMPUTED — the full-grid distinct-d computation is THE
HIGHEST-VALUE NAMED FOLLOW-UP before any residual repricing.
Coordinator replay: d4_bo_sieve.py byte-identical (incl. the CJ3
baseline 0.01969549 byte-match).

**(3) RED 3's MYSTERY-7 MEMBERSHIP STAYS UNDECIDED — honest
refusal of record:** t >= 4 exact enumeration priced at ~17
min/config (~2.3 h for a grid of 8) and NOT spent; and the 23b
repaired max-to-mean functional FAILS ITS POWER CONTROL at every
accessible t <= 3 cell (guarded flats statistically
indistinguishable from matched-random on the discriminating
functional: 3.96 vs 4.43 at dim 3). Membership must not be
flipped on this evidence. The falsifier-firing story for this
node is recorded on l1_rootfree_rational_q_projective_packing
(round-26 correction): 156/408 rows pass sigma < 2a and ALL are
~10^11 bits short of the polynomial target — 17 of the 156 are
already (BO2) singletons. Source:
notes/pilots_20260809/m7_falsifier_hunt/ (REPORT.md,
FABLE_AUDIT.md).
