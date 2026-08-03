# ESCAPE-1 GATE-CLEAN REALIZABILITY — channel (ii) of the band heart

(Persisted verbatim by the coordinator from the pilot's final message;
the pilot's REPORT.md write was harness-blocked. Pilot: Opus 5,
2026-08-03. Replay: tools/ramguard tiny -- python3
notes/pilots_20260803/escape1_realizability/verify.py -> 113 checks,
0 FAIL, 0 of 12 pre-registered falsifiers fired; PREREG.md timestamped
before the first run.)

## VERDICT — the two commissioned questions, answered separately

(1) REALIZABILITY: YES. Gate-clean ray systems whose (3,k+1)-core is
nonempty and contains a ray of escape EXACTLY 1 exist in abundance, in
three independent shapes; there is a family in which EVERY core ray
escapes exactly 1. Unification flag 5 resolved affirmatively.

(2) CHARGE: an escape-1 core ray CAN defeat per-ray charge 2 — but
only in the abstract gate-clean class, and every such fixture found is
non-realisable as a band system:
(2a) The abstract heart is FALSE: fixture E1 (k=19,h=4,V=12,n=30),
gate-clean, band-proper depths, core = all 12 rays, all escapes
exactly 1, rank = 22 < 24 = 2V for EVERY slope tuple (charge 1.833).
(2b) The sharp sub-case is PROTECTED by the new 3-DROP FLOOR (THEOREM
D): a single escape-1 core ray among escape->=2 rays can never defeat
charge 2; a failure needs >= 3h-2 low-escape core rays, and in the
all-escape-1 case V >= 3h (LEMMA ALL-1), saturated exactly by E1.
(2c) Band-admissibility kills every found counterexample: LEMMA R —
nontrivial realisers (u,v) exist iff rank < 2m; at rank = 2m every
realising pair is jointly explained on U, so no slope is exact-A live
and the system cannot be a selected-support system. E1 and its family
have rank = 2m exactly (820 tuples, 4 shapes, 3 fields: no deficit).

(3) CROSS-CHANNEL FLAG: channel (i) IS realised at FULL GATE.
Zfib11 (q=31, n=22, k=17, h=3, A=20; U = F_31^* split into the V=11
fibres of x^2, S_a = U\A_a, slopes = fibre parameters): gate-clean,
ZERO escape, below the Cor-3b threshold ((V-3)t+|A_0| = 16 = k-1),
rank = 9 < 2m = 10 (non-collapsing) and 9 < 2V = 22 — charge 0.818;
REALISED (dim nontrivial realisers = 1; nondegenerate draws give every
ray slope max agreement exactly A = 20); s4lib.gate_report: FULL_GATE
= True, ADMISSIBLE = True, live_slopes = 11. Fires the band TARGET's
channel-(i) falsifier and its V > m/2 falsifier verbatim. Per the
node's own wording this refutes the heart's ROUTE, not the column
bound (measured N_d = 55 = 0.11 n^2, far inside 0.68 n^2; sum L =
110, maxL = 2 = cap). Surfaced, not acted on.

## Structure lemmas (new, proved)

LEMMA A (h >= 3 forced): gate-clean with V >= 3 => h >= 3
(|S_a^S_b^S_c| >= 2(k+1)-(k+h) = k+2-h vs (T) <= k-1); h = 2
impossibility also verified exhaustively at k=2,3, n=8.
LEMMA B (|K| = 0 or >= 4): |K| <= 2 empty locus; |K| = 3 forces
T^inf_a <= a triple intersection of size <= k-1 < k+1.

## THEOREM D — the 3-drop kernel floor (new; strictly improves U3)

For (T)-clean systems with distinct slopes and nonempty core K, with
G3 := max over 3-subsets X of K of sum_{a in X}(h - esc_a):
  dim Rel <= sum_{a in K}(h - esc_a) - G3
  rank    >= sum_{a not in K} h + sum_{a in K} esc_a + G3.
Proof: Lemma 0 embeds Rel in (+)_{K} C_{T^inf_a}; for a 3-subset X
(|K| >= 4 by LEMMA B), a relation supported in X forces all three
supports inside a triple intersection of size <= k-1, killed by MDS
weight >= k+1; so Rel meets the X-block trivially. (The ray-support
Singleton bound: Rel has minimum ray-distance >= 4.) QED
TIGHT on the U-mechanism (3,5,1,4): predicts dim Rel <= 1, recorded
value 1, rank 19 — the first floor that PREDICTS the U-mechanism
deficit. COROLLARY D1: with n_0 = 0, charge 2 survives unless
n_1 >= 3h-2 (verified thresholds 7,10,13,16 at h = 3..6); ONE
escape-1 core ray can never defeat charge 2.

## Realizability fixtures

E1 (all escapes exactly 1): U = A_0 u B_1..B_V u Y with a perfect
matching; S_a = A_0 u (all B_b, b != a) u {y_{i(a)}}; gates read
ceil(h/2) <= s <= h-2 (so h >= 4). Pin h=4,s=2,p=6,k=19: A=23, n=30,
m=11; pairwise 20/21 = k+1/k+2 (band-proper depths 1,2); triples 18 =
k-1 saturated; 4-wise 16; core = all 12; one-step escapes 1 too;
rank = 22 = 2m < 24 = 2V. X1p (V=4): the collapse pilot's x^4-fibre
system perturbed by one point swap — escapes (1,1,1,0), gate-clean.
E1P (V=10, q=31, ten fibres of x^3, k=22, h=5): escapes (1,0,...,0).

## Charge

E1deep (p=10,V=20,k=35): rank 30 < 40, charge 1.5. Mechanism: m < V
with the banked rank <= 2m — slope-INDEPENDENT (unlike X1-X3's
cross-ratio locus). CONTRAST E1safe (p=3,V=6,k=19, m=8 >= V): charge
2.667 — escape 1 alone is harmless.
LEMMA ALL-1: gate-clean, core = all rays, every escape exactly 1,
m < V forces |E| >= V/2, 2|E| <= 2t+2-h, t >= 2h-1, V >= 3h —
E1 saturates all three at h=4. Family scan (99 members): V = 12
minimal. The interval n_1 in {10,11} at h=4 between D1's 3h-2 and
ALL-1's 3h is an honest gap.
LEMMA R (realisability): dim{nontrivial realisers} = 2m - rank; at
rank = 2m no exact-A live slope once |U| > A — rank <= 2m-1 is
NECESSARY for band admissibility. (The banked T3-type consequence
turned into an admissibility test.) E1/E1deep/Z1/Z1big all have
rank = 2m exactly => none band-admissible. Sharp open question:
an all-escape-1 gate-clean system with dim Ann = 1 (THEOREM D allows
exactly 1 at the E1 pin; 820 tuples found 0). E1P has a genuine
deficit (rank 16, 2 nontrivial dims) BUT in 520 sampled nondegenerate
realisers the escape-1 ray's max agreement is always A+1, never A
(exact counts: 2h > m => any A-agreement carries the S_a interpolant)
— EVIDENCE, not proof (FLAG 4). Structural hardness: escape-1 block
families force m >= 9 vs zero-escape's m >= 5, so charge-defeat needs
V >= 10 vs 6.

## Implications (conservative, no status flips)

1. The gate-clean hypothesis list is INSUFFICIENT for the heart:
   charge 2 is false for gate-clean systems in both channels (0.818
   realised zero-escape; 1.5 abstract escape-1). The heart must be
   stated for BAND-ADMISSIBLE systems; sharpest missing ingredient =
   LEMMA R's rank <= 2m-1.
2. Necessary condition now explicit: charge 2 forces V <= m; any
   future route must get V <= m from admissibility, not the gates.
3. THEOREM D is a new floor of record (dominates the kernel floor by
   up to 3h; tight on the U-mechanism; proved from banked ingredients).
4. Channel (ii) is not the danger; channel (i) is: every pure
   escape-1 counterexample has rank = 2m (non-realisable); the
   realised full-gate counterexample is zero-escape. If zero-escape
   admissible systems are ruled out, D1 closes escape 1 for
   n_1 < 3h-2.
5. Survives untouched: the node's PROVED claims, the column bound
   |Gamma_band| <= 4n^3, and the occupancy lemma's conclusion.

## FLAGS

1. CROSS-CHANNEL/UPSTREAM: Zfib11 fires two of the band TARGET's own
   pre-registered falsifiers at FULL GATE (sibling channel, not my
   anchor; no node edited; dated addendum owed). 2. Scope: the
   heart's ROUTE refuted, not the column bound. 3. Toy scale (q <=
   127 gate work; full-gate fixture is a rate-17/22 toy row). 4. E1P
   negative result is evidence (520 samples), not proof. 5. Open gap
   n_1 in {10,11} at h=4; ALL-1 covers only the m < V mechanism.
   6. The E1-family deficit question is open and sharp. 7. Consumed
   not re-derived: Lemma 0/Phi, S4-1, MDS kill, per-ray accounting,
   occlib gate semantics. 8. Compute law kept (tiny 20 s; local
   sweeps); COMPUTE REQUEST: the occlib full-gate oracle is C(n,k) —
   deciding the full gate for an escape-1 fixture (m >= 9) needs the
   complement-enumeration test or larger budget. 9. Banked replays
   clean (U-mech 19/16/4; K_V 35; S1 10).

## Falsifiers: 0 of 12 fired (E-F1..E-F12, all as pre-registered).
