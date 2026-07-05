# Level-2 skew-tower falsifier -- results

Verifier: `nodes/b2b_primitive_core/notes/verify_level2_tower.py` (deterministic; recomputes every table). Single process, <1.5 GB.
Framework: `skew_tower_attack.md`; ground truth: the exhaustive mu_32
t-null censuses in `b2b_balance_concentration_scan.md`. Interpretation
for all three tests was fixed BEFORE the data (see the prompt / docstring).

## TEST 1 -- exact tower product-total vs ground-truth census (KILL-TEST)

For each n=32 row: tower total (sum over floor(t/2)-null m_1 of skewcount(G),
incl. empty set) minus 1  ==  my direct full-subset MITM census (excl. empty)
==  scan-published coset+noncoset.  ANY mismatch => the factorization leaks.

| t | q | scan c+nc | direct(excl e) | tower-1 | coset | noncoset | match |
|---|---|---|---|---|---|---|---|
| 2 | 97 | 455743 | 455743 | 455743 | 255 | 455488 | EXACT |
| 2 | 193 | 116511 | 116511 | 116511 | 255 | 116256 | EXACT |
| 2 | 8353 | 575 | 575 | 575 | 255 | 320 | EXACT |
| 2 | 32801 | 255 | 255 | 255 | 255 | 0 | EXACT |
| 3 | 97 | 6591 | 6591 | 6591 | 255 | 6336 | EXACT |
| 3 | 193 | 1023 | 1023 | 1023 | 255 | 768 | EXACT |
| 4 | 97 | 175 | 175 | 175 | 15 | 160 | EXACT |
| 4 | 193 | 15 | 15 | 15 | 15 | 0 | EXACT |

**TEST 1 verdict: PASS -- tower factorization reproduces every census exactly**

## TEST 2 -- profile-constancy of the skew count (the conjecture, incl. multiplicities)

Claim (skew_tower_attack.md pt.1 / conj. iii): #valid skews depends only on
m_1's multiplicity profile -- constant across states of a given singleton
count k (and, level-2, given (k, #doubled j)).  We tabulate, per profile,
the SET of skewcount values that actually occur among even-null m_1 states.
Constancy holds for a profile iff that set is a singleton.

**Level-1 baseline (n=16), where the program claims 'verified with zero exceptions':**

### L1 baseline: n=16, t=2, q=97  (tower total incl empty = 16)
  per-k skewcount value-sets: k0:[1]  k2:[0]  k4:[0]  k6:[0]  k8:[0]
  per-k constancy: HOLDS (each k a single skewcount value -- trivial/coset branching)
  scaling-orbit (cyclic-shift) invariance of skewcount: HOLDS

### L1 baseline: n=16, t=2, q=193  (tower total incl empty = 16)
  per-k skewcount value-sets: k0:[1]  k2:[0]  k4:[0]  k6:[0]  k8:[0]
  per-k constancy: HOLDS (each k a single skewcount value -- trivial/coset branching)
  scaling-orbit (cyclic-shift) invariance of skewcount: HOLDS

### L1 baseline: n=16, t=2, q=17  (tower total incl empty = 224)
  per-k skewcount value-sets: k0:[1]  k1:[0]  k2:[0]  k3:[0, 2]  k4:[0, 2]  k5:[0]  k6:[4]  k8:[16]
  **per-k CONSTANCY VIOLATED** at k in [3, 4] (distinct skewcount values coexist): {3: [0, 2], 4: [0, 2]}
  **per-(k,j) CONSTANCY ALSO VIOLATED** at [(3, 1), (3, 2), (3, 3), (3, 4), (4, 2)] (finer multiplicity profile does not repair it)
  scaling-orbit (cyclic-shift) invariance of skewcount: HOLDS

WITNESS (n=16,q=17,k=3): singleton set exps [0, 2, 3] has a weight-3 sign relation (skewcount 2) while exps [0, 1, 2] has none (skewcount 0) -- same profile k=3, different counts.

**Level-2 (n=32), the pre-registered level-2 experiment:**

### L2: n=32, t=2, q=97  (tower total incl empty = 455744)
  per-k skewcount value-sets: k0:[1]  k1:[0]  k2:[0]  k3:[0, 2]  k4:[0, 2]  k5:[0, 2]  k6:[0, 2, 4]  k7:[0, 2, 4, 6, 8]  k8:[0, 2, 4, 6, 8, 10]  k9:[0, 2, 4, 6, 8, 10, 12, 14]  k10:[4, 6, 8, 10, 12, 14, 16, 18, 20, 22]  k11:[10, 14, 16, 18, 20, 22, 24, 26, 28, 30]  k12:[32, 34, 36, 38, 44, 46, 52]  k14:[176]  k16:[672]
  **per-k CONSTANCY VIOLATED** at k in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12] (distinct skewcount values coexist): {3: [0, 2], 4: [0, 2], 5: [0, 2], 6: [0, 2, 4], 7: [0, 2, 4, 6, 8], 8: [0, 2, 4, 6, 8, 10], 9: [0, 2, 4, 6, 8, 10, 12, 14], 10: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22], 11: [10, 14, 16, 18, 20, 22, 24, 26, 28, 30], 12: [32, 34, 36, 38, 44, 46, 52]}
  **per-(k,j) CONSTANCY ALSO VIOLATED** at [(3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9)] ... (finer multiplicity profile does not repair it)
  scaling-orbit (cyclic-shift) invariance of skewcount: HOLDS

### L2: n=32, t=2, q=8353  (tower total incl empty = 576)
  per-k skewcount value-sets: k0:[1]  k1:[0]  k2:[0]  k3:[0]  k4:[0]  k5:[0]  k6:[0]  k7:[0, 2]  k8:[0]  k9:[0]  k10:[0]  k12:[0, 4]  k14:[4]  k16:[0]
  **per-k CONSTANCY VIOLATED** at k in [7, 12] (distinct skewcount values coexist): {7: [0, 2], 12: [0, 4]}
  **per-(k,j) CONSTANCY ALSO VIOLATED** at [(7, 3), (7, 4), (7, 5), (7, 6), (12, 0), (12, 2), (12, 4)] (finer multiplicity profile does not repair it)
  scaling-orbit (cyclic-shift) invariance of skewcount: HOLDS

### L2: n=32, t=2, q=32801  (tower total incl empty = 256)
  per-k skewcount value-sets: k0:[1]  k2:[0]  k3:[0]  k4:[0]  k5:[0]  k6:[0]  k7:[0]  k8:[0]  k10:[0]  k12:[0]  k14:[0]  k16:[0]
  per-k constancy: HOLDS (each k a single skewcount value -- trivial/coset branching)
  scaling-orbit (cyclic-shift) invariance of skewcount: HOLDS

### L2: n=32, t=3, q=97  (tower total incl empty = 6592)
  per-k skewcount value-sets: k0:[1]  k1:[0]  k2:[0]  k3:[0]  k4:[0]  k5:[0, 2]  k6:[0, 2]  k7:[0, 2]  k8:[0, 2]  k9:[0, 2]  k10:[0, 2, 4]  k11:[0, 2, 4]  k12:[0, 4]  k14:[0]  k16:[32]
  **per-k CONSTANCY VIOLATED** at k in [5, 6, 7, 8, 9, 10, 11, 12] (distinct skewcount values coexist): {5: [0, 2], 6: [0, 2], 7: [0, 2], 8: [0, 2], 9: [0, 2], 10: [0, 2, 4], 11: [0, 2, 4], 12: [0, 4]}
  **per-(k,j) CONSTANCY ALSO VIOLATED** at [(5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9)] ... (finer multiplicity profile does not repair it)
  scaling-orbit (cyclic-shift) invariance of skewcount: HOLDS

### L2: n=32, t=4, q=97  (tower total incl empty = 176)
  per-k skewcount value-sets: k0:[1]  k2:[0]  k3:[0]  k4:[0]  k5:[0, 2]  k6:[0]  k7:[0]  k8:[0]  k9:[0]  k10:[0]  k12:[0]  k16:[32]
  **per-k CONSTANCY VIOLATED** at k in [5] (distinct skewcount values coexist): {5: [0, 2]}
  **per-(k,j) CONSTANCY ALSO VIOLATED** at [(5, 4), (5, 5), (5, 6), (5, 7)] (finer multiplicity profile does not repair it)
  scaling-orbit (cyclic-shift) invariance of skewcount: HOLDS

**TEST 2 verdict: FALSIFIED** -- profile-constancy (constant skewcount per
multiplicity profile) is FALSE at every prime with nontrivial branching:
already at LEVEL 1 (n=16, exceptional q=17) and pervasively at LEVEL 2
(n=32, q=97). It holds only VACUOUSLY at non-exceptional primes (all
skewcounts 0 except the empty profile). skewcount is invariant on cyclic
scaling orbits but NOT constant across a multiplicity profile, so the
sketched 'product of per-profile constants' (conj. iii) does not hold as
stated; the exact total (Test 1) is a SUM over non-constant profiles.

## TEST 3 -- bounded-coefficient relation counts (explosion test)

R(D,k,C,q) = #{k-subset S of domain D, c in ({-C..C}\{0})^k : sum c_i s_i
= 0 mod q}.  E = C(|D|,k)(2C)^k/q is the random-chance floor.  rho=R/E:
rho~1 => relations are just the random floor (no structure); rho>>1 =>
STRUCTURED (exceptional-prime) relations.  Pre-registered: norm-gate
generalizes iff structure (rho>>1) is confined to the exceptional prime and
generic primes stay rho~1 for all C; an explosion of rho>>1 at a GENERIC
prime once C>=2 falsifies per-level rigidity.

### domain: mu16-transversal {z16^0..7} (the genuine level-1 skew domain, 8 classes, NOT closed under negation -- the clean exceptionality probe)
  -- coefficient bound C=1 (nonzero coeffs in +-[1..1]) --
  |  q  | k=1 | k=2 | k=3 | k=4 | k=5 | k=6 | k=7 | k=8 |
  |---|---|---|---|---|---|---|---|---|
  |     17 | 0(rho0.0) | 0(rho0.0) | 32(rho1.2) | 80(rho1.2) | 96(rho0.9) | 96(rho0.9) | 64(rho1.1) | 16(rho1.1) |
  |     97 | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 16(rho1.4) | 16(rho0.9) | 16(rho0.9) | 16(rho1.5) | 0(rho0.0) |
  |    193 | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 16(rho1.7) | 16(rho1.7) | 0(rho0.0) | 0(rho0.0) |
  |   3329 | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) |
  |  40961 | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) |
  | 786433 | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) |

  -- coefficient bound C=2 (nonzero coeffs in +-[1..2]) --
  |  q  | k=1 | k=2 | k=3 | k=4 | k=5 | k=6 | k=7 | k=8 |
  |---|---|---|---|---|---|---|---|---|
  |     17 | 0(rho0.0) | 16(rho0.6) | 240(rho1.1) | 1056(rho1.0) | 3312(rho1.0) | 6800(rho1.0) | 7696(rho1.0) | 3856(rho1.0) |
  |     97 | 0(rho0.0) | 0(rho0.0) | 16(rho0.4) | 240(rho1.3) | 592(rho1.0) | 1168(rho1.0) | 1312(rho1.0) | 672(rho1.0) |
  |    193 | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 96(rho1.0) | 400(rho1.3) | 528(rho0.9) | 576(rho0.8) | 448(rho1.3) |
  |   3329 | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 48(rho1.4) | 48(rho1.2) | 48(rho2.4) |
  |  40961 | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) |
  | 786433 | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) |

  -- coefficient bound C=4 (nonzero coeffs in +-[1..4]) --
  |  q  | k=1 | k=2 | k=3 | k=4 | k=5 | k=6 | k=7 | k=8 |
  |---|---|---|---|---|---|---|---|---|
  |     17 | 0(rho0.0) | 96(rho0.9) | 1760(rho1.0) | 16720(rho1.0) | 108064(rho1.0) | 431728(rho1.0) | 986896(rho1.0) | 986896(rho1.0) |
  |     97 | 0(rho0.0) | 16(rho0.9) | 256(rho0.9) | 3136(rho1.1) | 18608(rho1.0) | 75936(rho1.0) | 172864(rho1.0) | 172960(rho1.0) |
  |    193 | 0(rho0.0) | 16(rho1.7) | 112(rho0.8) | 1392(rho0.9) | 9920(rho1.0) | 37632(rho1.0) | 87008(rho1.0) | 86960(rho1.0) |
  |   3329 | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 144(rho1.7) | 448(rho0.8) | 2160(rho1.0) | 5120(rho1.0) | 5008(rho1.0) |
  |  40961 | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 16(rho2.3) | 64(rho1.4) | 112(rho0.6) | 368(rho0.9) | 464(rho1.1) |
  | 786433 | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 0(rho0.0) | 16(rho1.7) | 32(rho1.5) | 16(rho0.8) |

### domain: mu8 FULL group {z8^0..7} (8 classes, closed under negation -> carries char-0 antipodal relations)
  -- coefficient bound C=1 (nonzero coeffs in +-[1..1]) --
  |  q  | k=1 | k=2 | k=3 | k=4 | k=5 | k=6 | k=7 | k=8 |
  |---|---|---|---|---|---|---|---|---|
  |     17 | 0(rho0.0) | 8(rho1.2) | 16(rho0.6) | 56(rho0.9) | 128(rho1.2) | 128(rho1.2) | 64(rho1.1) | 16(rho1.1) |
  |     97 | 0(rho0.0) | 8(rho6.9) | 0(rho0.0) | 24(rho2.1) | 0(rho0.0) | 32(rho1.7) | 0(rho0.0) | 16(rho6.1) |
  |    193 | 0(rho0.0) | 8(rho13.8) | 0(rho0.0) | 24(rho4.1) | 0(rho0.0) | 32(rho3.4) | 0(rho0.0) | 16(rho12.1) |
  |   3329 | 0(rho0.0) | 8(rho237.8) | 0(rho0.0) | 24(rho71.3) | 0(rho0.0) | 32(rho59.4) | 0(rho0.0) | 16(rho208.1) |
  |  40961 | 0(rho0.0) | 8(rho2925.8) | 0(rho0.0) | 24(rho877.7) | 0(rho0.0) | 32(rho731.4) | 0(rho0.0) | 16(rho2560.1) |
  | 786433 | 0(rho0.0) | 8(rho56173.8) | 0(rho0.0) | 24(rho16852.1) | 0(rho0.0) | 32(rho14043.4) | 0(rho0.0) | 16(rho49152.1) |

  -- coefficient bound C=2 (nonzero coeffs in +-[1..2]) --
  |  q  | k=1 | k=2 | k=3 | k=4 | k=5 | k=6 | k=7 | k=8 |
  |---|---|---|---|---|---|---|---|---|
  |     17 | 0(rho0.0) | 48(rho1.8) | 144(rho0.7) | 1096(rho1.0) | 3360(rho1.0) | 6808(rho1.0) | 7696(rho1.0) | 3856(rho1.0) |
  |     97 | 0(rho0.0) | 16(rho3.5) | 32(rho0.9) | 176(rho1.0) | 480(rho0.8) | 1200(rho1.0) | 1440(rho1.1) | 880(rho1.3) |
  |    193 | 0(rho0.0) | 16(rho6.9) | 0(rho0.0) | 96(rho1.0) | 224(rho0.8) | 752(rho1.3) | 576(rho0.8) | 448(rho1.3) |
  |   3329 | 0(rho0.0) | 16(rho118.9) | 0(rho0.0) | 96(rho17.8) | 0(rho0.0) | 256(rho7.4) | 0(rho0.0) | 256(rho13.0) |
  |  40961 | 0(rho0.0) | 16(rho1462.9) | 0(rho0.0) | 96(rho219.4) | 0(rho0.0) | 256(rho91.4) | 0(rho0.0) | 256(rho160.0) |
  | 786433 | 0(rho0.0) | 16(rho28086.9) | 0(rho0.0) | 96(rho4213.0) | 0(rho0.0) | 256(rho1755.4) | 0(rho0.0) | 256(rho3072.0) |

  -- coefficient bound C=4 (nonzero coeffs in +-[1..4]) --
  |  q  | k=1 | k=2 | k=3 | k=4 | k=5 | k=6 | k=7 | k=8 |
  |---|---|---|---|---|---|---|---|---|
  |     17 | 0(rho0.0) | 128(rho1.2) | 1600(rho0.9) | 17016(rho1.0) | 107824(rho1.0) | 431800(rho1.0) | 986896(rho1.0) | 986896(rho1.0) |
  |     97 | 0(rho0.0) | 64(rho3.5) | 320(rho1.1) | 2984(rho1.0) | 18320(rho1.0) | 76320(rho1.0) | 172848(rho1.0) | 173128(rho1.0) |
  |    193 | 0(rho0.0) | 32(rho3.4) | 64(rho0.4) | 1632(rho1.1) | 9152(rho1.0) | 38824(rho1.0) | 86112(rho1.0) | 87224(rho1.0) |
  |   3329 | 0(rho0.0) | 32(rho59.4) | 0(rho0.0) | 384(rho4.5) | 256(rho0.5) | 3456(rho1.6) | 2848(rho0.6) | 6464(rho1.3) |
  |  40961 | 0(rho0.0) | 32(rho731.4) | 0(rho0.0) | 384(rho54.9) | 0(rho0.0) | 2048(rho11.4) | 0(rho0.0) | 4096(rho10.0) |
  | 786433 | 0(rho0.0) | 32(rho14043.4) | 0(rho0.0) | 384(rho1053.3) | 0(rho0.0) | 2048(rho219.4) | 0(rho0.0) | 4096(rho192.0) |

### domain: mu16 FULL group {z16^0..15} (16 classes, closed under negation -> char-0 antipodal/coset baseline)
  -- coefficient bound C=1 (nonzero coeffs in +-[1..1]) --
  |  q  | k=1 | k=2 | k=3 | k=4 | k=5 | k=6 | k=7 | k=8 |
  |---|---|---|---|---|---|---|---|---|
  |     17 | 0(rho0.0) | 16(rho0.6) | 288(rho1.1) | 1776(rho1.0) | 8096(rho1.0) | 29984(rho1.0) | 86464(rho1.0) | 194032(rho1.0) |
  |     97 | 0(rho0.0) | 16(rho3.2) | 0(rho0.0) | 368(rho1.2) | 1312(rho0.9) | 5376(rho1.0) | 15488(rho1.0) | 33392(rho1.0) |
  |    193 | 0(rho0.0) | 16(rho6.4) | 0(rho0.0) | 112(rho0.7) | 768(rho1.1) | 2624(rho1.0) | 7744(rho1.0) | 17184(rho1.0) |
  |   3329 | 0(rho0.0) | 16(rho111.0) | 0(rho0.0) | 112(rho12.8) | 0(rho0.0) | 448(rho2.9) | 512(rho1.2) | 1120(rho1.1) |
  |  40961 | 0(rho0.0) | 16(rho1365.4) | 0(rho0.0) | 112(rho157.5) | 0(rho0.0) | 448(rho35.8) | 0(rho0.0) | 1120(rho13.9) |
  | 786433 | 0(rho0.0) | 16(rho26214.4) | 0(rho0.0) | 112(rho3024.7) | 0(rho0.0) | 448(rho687.4) | 0(rho0.0) | 1120(rho267.3) |

  -- coefficient bound C=2 (nonzero coeffs in +-[1..2]) --
  |  q  | k=1 | k=2 | k=3 | k=4 | k=5 | k=6 | k=7 | k=8 |
  |---|---|---|---|---|---|---|---|---|
  |     17 | 0(rho0.0) | 96(rho0.8) | 2208(rho1.0) | 27408(rho1.0) | 262336(rho1.0) | 1930672(rho1.0) | 11026688(rho1.0) | 49609696(rho1.0) |
  |     97 | 0(rho0.0) | 32(rho1.6) | 192(rho0.5) | 5280(rho1.1) | 45664(rho1.0) | 339216(rho1.0) | 1930304(rho1.0) | 8695120(rho1.0) |
  |    193 | 0(rho0.0) | 32(rho3.2) | 64(rho0.3) | 2304(rho1.0) | 23648(rho1.0) | 172256(rho1.0) | 965824(rho1.0) | 4367264(rho1.0) |
  |   3329 | 0(rho0.0) | 32(rho55.5) | 0(rho0.0) | 448(rho3.2) | 512(rho0.4) | 10240(rho1.0) | 50656(rho0.9) | 258464(rho1.0) |
  |  40961 | 0(rho0.0) | 32(rho682.7) | 0(rho0.0) | 448(rho39.4) | 0(rho0.0) | 3712(rho4.6) | 1920(rho0.4) | 30240(rho1.5) |
  | 786433 | 0(rho0.0) | 32(rho13107.2) | 0(rho0.0) | 448(rho756.2) | 0(rho0.0) | 3584(rho85.9) | 0(rho0.0) | 17920(rho16.7) |

  -- coefficient bound C=4 (nonzero coeffs in +-[1..4]) --
  |  q  | k=1 | k=2 | k=3 | k=4 | k=5 | k=6 | k=7 | k=8 |
  |---|---|---|---|---|---|---|---|---|
  |     17 | 0(rho0.0) | 448(rho1.0) | 17088(rho1.0) | 437728(rho1.0) | 8419392(rho1.0) | 123492832(rho1.0) | 1411235040(rho1.0) | 12701381872(rho1.0) |
  |     97 | 0(rho0.0) | 128(rho1.6) | 2464(rho0.8) | 78640(rho1.0) | 1473056(rho1.0) | 21643552(rho1.0) | 247315680(rho1.0) | 2226105408(rho1.0) |
  |    193 | 0(rho0.0) | 128(rho3.2) | 1376(rho0.9) | 37200(rho1.0) | 739168(rho1.0) | 10901328(rho1.0) | 124319104(rho1.0) | 1118609328(rho1.0) |
  |   3329 | 0(rho0.0) | 64(rho27.7) | 0(rho0.0) | 4288(rho1.9) | 45312(rho1.1) | 653504(rho1.0) | 7156768(rho1.0) | 64851888(rho1.0) |
  |  40961 | 0(rho0.0) | 64(rho341.3) | 0(rho0.0) | 2048(rho11.3) | 4608(rho1.3) | 85696(rho1.7) | 602112(rho1.0) | 5520784(rho1.0) |
  | 786433 | 0(rho0.0) | 64(rho6553.6) | 0(rho0.0) | 1792(rho189.0) | 0(rho0.0) | 30208(rho11.3) | 25088(rho0.8) | 543744(rho2.0) |

READING (the discriminator is large-q PERSISTENCE, not raw rho -- at small
primes the random floor E is inflated, so rho~1 there is ambiguous):
- The genuine skew domain (mu16-transversal) has NO prime-independent
  relations: at the large control prime 786433 (floor<<1) R=0 for C=1,2 at
  every k<=8, and only a handful (rho~1, floor-level) at C=4.  So bounded
  coefficients up to C=4 do NOT manufacture STRUCTURED relations that
  survive to a generic large prime -- per-level rigidity HOLDS.
- At generic small primes 97/193 the counts that appear as C grows all
  TRACK the random floor (R~E, rho~1) and vanish as q grows: no rho>>1
  spike at a generic prime is created by C>=2.  The field-specific relations
  that DO occur (e.g. the exceptional prime 17 has weight-3 +-1 relations
  absent at 97/193/large q) are exactly the sporadic norm-gate hits (p |
  Norm(sum c_i xi_i)), sparse and prime-dependent -- not an explosion.
- The mu8 and mu16 FULL groups (closed under negation) instead carry
  PRIME-INDEPENDENT relations (R converges to a fixed baseline as q->inf:
  8/24/32/16 for mu8 C=1 at k=2/4/6/8): these are the char-0 antipodal/
  coset relations, present at every prime by construction -- expected, and
  NOT a counterexample to generic-prime rigidity.

**TEST 3 verdict: PASS (bounded-coefficient relations track the random floor / char-0 baseline; no structured explosion at generic primes -- per-level rigidity survives, consistent with a norm-gate generalization)**

## OVERALL
- TEST 1 (product-total == census): **PASS**
- TEST 2 (profile-constancy conjecture): **FALSIFIED**
- TEST 3 (bounded-coefficient explosion): **PASS**

### What this means for the skew-tower program
- The DESCENT + CONSTRAINT SPLIT (L2/L3/L5) is quantitatively exact: the
  tower reproduces every exhaustive mu_32 census to the unit (Test 1).
  The factorization t-null <-> (floor(t/2)-null m_1, valid skew) is real.
- The PER-PROFILE-CONSTANT PRODUCT (conjecture iii -- the step that would
  turn the exact SUM into a clean product of per-level constants) is
  FALSE (Test 2): skewcount is invariant only on cyclic scaling ORBITS,
  and a multiplicity profile (fixed k, or fixed (k,j)) contains many
  orbits with DIFFERENT skewcounts -- already at the level-1 exceptional
  prime, and pervasively at level 2.  The 'orbit acts transitively within
  profiles' assumption underlying (iii) is contradicted by explicit
  witnesses.  #{t-null} remains an exact SUM over non-constant profiles,
  not a product; the counting must be closed some other way.
- The BOUNDED-COEFFICIENT RIGIDITY that such an alternative closure would
  rely on SURVIVES (Test 3): coefficients up to C=4 do not create
  structured (large-q-persistent) relations at generic primes; the
  norm-gate picture generalizes.  So the program is not dead, but its
  advertised route to a product formula is: the win, if any, must come
  from bounding the SUM via norm-gate sparsity, not from profile-constancy.
