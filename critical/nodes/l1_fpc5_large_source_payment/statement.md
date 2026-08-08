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

## Round-23 diagnosis addendum (2026-08-07, coordinator-applied on replay: fpc5_diag)

**CLASSIFICATION: MYSTERY-HARD, and the LEAST DEFENDED of the three
FPC5 reds** (the registered exposure test FIRED as pre-registered —
an exposure, not a witness; the partition stands). Same wall (MF)
plus two missing pieces the m4 reds already have: (i) NO mu-basis /
overlap-cap theorem exists for t >= 4 (the three-petal theorems do
not generalize as stated; even the Johnson functional J is
undefined there); (ii) NO background-guard analogue at M >= 5.
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
