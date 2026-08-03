# PRE-REGISTRATION — cross-lane cash-out (P-A1 |K|, P-B planting ceiling)

Pilot: Opus 5. Written **2026-08-03T15:25:23Z**, BEFORE any computation in
this directory (`verify.py` did not exist at this timestamp). Every
prediction below is stated with the falsifier that would kill it. A fired
falsifier is REPORTED as fired, never silently dropped.

Compute law: `tools/ramguard tiny|local -- python3 ...` from the repo root,
literal `--`. No Modal, no network.

Consumed, NOT re-derived (hard law 5 — subtraction sweep run in parallel):
Lemma 0 / the `(3,k+1)`-core operator `Phi`, U1-U5
(`k_escape_unification/REPORT.md`); THEOREM D 3-drop + LEMMA B + LEMMA R
(`escape1_realizability/REPORT.md`); v5 LEMMA 1 / THEOREM A,B,C,C',D
(`v5_occupancy/REPORT.md`); LEMMA O1/O2, THEOREM O3/O4 (Fisher)/O5
(`overlap_sliver/REPORT.md`); THEOREM F + LEMMA P + DICHOTOMY
(`lb_escape1_overagreement/REPORT.md`); D0-2/D0-3 and
`rank(F) = h|P| + rank(K)` (`exact_k_heart/REPORT.md`); pb_design_ceiling
THEOREM 1/3 and pb_block_dichotomy CLAIM 1-4 + SELECTOR CATCH.
Libraries `s4lib`, `tslib`, `occlib`, `stage5_escape`, `stage4_scan` are
IMPORTED read-only, never copied.

---

## PART A — the best unconditional `|K|` bound for P-A1

Notation: ray system `(z_a, S_a)_{a in K}` on union `U`, `|S_a| = A = k+h`,
`t := |U| - A` (complement size), gate **(T)** `|S_a^S_b^S_c| <= k-1`.
Target of record: `P-A1(d=0) <= (2R-1)/h + |K|`, so the consumer needs
`|K|` at the `(2R-1)/h` scale (`307/358/639` RowC, `383/447/959` prize).

**A-P1 (gate forces a complement floor).** Any (T)-clean system with
`>= 3` rays and all `|S_a| = A` has `2t >= h+1`.
*Mechanism (to be machine-checked, not assumed):*
`|S_a^S_b^S_c| >= 3A - 2|U|` and `(T)` give `2|U| >= 3A-k+1`, i.e.
`t >= (h+1)/2`.
**A-F1:** a (T)-clean system, `>= 3` rays, `2(|U|-A) <= h`.

**A-P2 (sunflower petal floor).** If the complements `A_a = U \ S_a` form a
sunflower — common core `Y`, `|Y| = lam`, pairwise-disjoint petals of size
`p = t - lam` — then (T) forces `2p >= h+1`.
**A-F2:** a (T)-clean sunflower system with `2p <= h`.

**A-P3 (the core-count ceiling).** Under A-P2, disjointness of the petals
inside `U \ Y` gives `|K| <= 1 + A/p <= 1 + 2A/(h+1)`.
**A-F3:** a (T)-clean sunflower ray system with `|K| > 1 + A/p`.

**A-P4 (row table — the cash-out).** At the six recorded rows
(`support4_relation/stage5_escape.json`, `criterion`), the derived
unconditional bound `1 + floor(2A/(h+1))` is STRICTLY BELOW the target
`floor((2R-1)/h)`. Predicted, before computing:
`88 / 45 / 34` (RowC 1/4, 1/8, 1/16) against `307 / 358 / 639`, and
`131 / 67 / 67` (prize) against `383 / 447 / 959`.
**A-F4:** any row where bound `>=` target, or where the recomputed integers
differ from the six predicted values.

**A-P5 (specialisation to the banked `Vmax`).** The record's clique model
is the `lam = 0` (disjoint) case with `p = h - d`, and the banked
`clique_Vmax` (`66/34/34` on BOTH triples) equals `floor(1 + A/(h-d))` with
`d := 2h - clique_m`.
**A-F5:** mismatch at any of the six rows.

**A-P6 (the rank route CANNOT bound `|K|`).** There are (T)-clean systems
with `|K| = V` growing and `rank(K)` constant `= 3h`, so no floor
`rank >= f(|K|)` with `f` unbounded exists; in particular THEOREM D's
`sum esc_a + G3` is bounded by `3h` on the zero-escape pencil family
however large `|K|` is. Concretely: the fibres of `x -> x^t` at
`V = 4,5,6,7,8` give `rank = 3h` at every `V`.
**A-F6:** `rank` grows with `V` on the pencil family (the rank route would
then survive and A's verdict changes).

**A-P7 (banked-fixture replay).** The U-mechanism `(k,h,d,V)=(3,5,1,4)`
(`dim 1`, `dimcap 4`, `rank 19`, `floor 16`), `K_V` `(3,7,1,5)` and
`(4,7,1,5)` (`dim 0`, `rank 35 = Vh`), and the clique rows replay exactly,
and none violates A-P3.
**A-F7:** any banked fixture failing replay or violating the derived bound.

---

## PART B — the P-B planting ceiling for REALISED families

Setting: `D = mu_n <= F_q^*`, `RS_K`, `A = K+h`, `r = n-K`; pencil model
`E(S) = (e_1(S),...,e_h(S))` on the affine line `L = {alpha + z beta}`
(`pb_block_dichotomy` Setting). THEOREM 3's exhibit: `n=20, q=41, K=4,
h=3, A=7`, `U = X^7`, `V = -X^6`, a spread realised `mu_20`-orbit of
`M = 20` supports, rank `31 = 2r-1` of `Mh = 60`.

**B-P1 (orbit-stabiliser replacement ceiling).** For a realised family that
is a single orbit of `H <= mu_n`, `M = |H|/|Stab(S_0)| <= |H| <= n`.
On THEOREM 3's fixture: `M = 20 = n`, `|Stab| = 1` — the ceiling is
ATTAINED, so it is sharp and cannot be improved for orbit families.
**B-F1:** THEOREM 3's orbit size `!= 20`, or any single-orbit family with
`M > n`.

**B-P2 (spread gives a stabiliser floor, vacuous here).** For `H = mu_n`,
`sum_{g in mu_n} |S_0 ^ g S_0| = A^2` exactly, hence spread forces
`|Stab| >= (A^2 - n(K-1))/(h+1)`. At THEOREM 3's shape
`A^2 - n(K-1) = 49 - 60 = -11 < 0`: VACUOUS — predicted consistent with
`M = n` being attained. Predicted vacuous at all six official rows too
(`A^2 < n(K-1)` at every row).
**B-F2:** the identity `sum_g |S_0 ^ gS_0| = A^2` fails, or a spread orbit
family with `|Stab|` below a POSITIVE value of the bound.

**B-P3 (invariant-line FORCING — the new structural claim).** If a realised
family on `D = mu_n` is `mu_n`-invariant and its moment vectors are not all
equal (`>= 2` distinct slopes = a live slope direction), then its moment
line `L` is a COORDINATE AXIS of `AG(h,q)`: `alpha, beta` are supported on a
single index `j_0`. Equivalently the pencil is forced MONOMIAL — THEOREM 3's
`U = X^A, V = -X^{A-1}` is not one example, it is the ONLY shape.
*Mechanism:* `e_j(gS) = g^j e_j(S)`, so `g.L = L`; a generator of `mu_n`
has `g^j != 1` for `1 <= j <= h < n`, forcing `beta` and `alpha` onto one
coordinate.
*Test (exhaustive at the fixture):* group all `C(20,7) = 77520` supports
into `mu_20`-orbits; for every orbit whose `E`-values are collinear with
`>= 2` distinct points, the affine hull is a coordinate axis.
**B-F3:** one orbit at the fixture that is collinear with `>= 2` distinct
moment points and whose line is NOT a coordinate axis; or THEOREM 3's
orbit members failing `e_2 = e_3 = 0`.

**B-P4 (what the replacement ceiling buys, and its honest limit).**
`M <= n` puts the ceiling's own refutation class strictly below the P-B
budget `8n^3` — by `2^23` (RowC) and `2^85` (prize). It does NOT cover
non-orbit realised spread families; that gap is stated, not closed.
**B-F4:** an arithmetic error in the six margins.

**B-P5 (SELECTOR catch vs L-B DICHOTOMY — species test).** PREDICTION:
GENUINELY DIFFERENT species, on two grounds, each decided by computation:
1. **Level.** L-B's forced over-agreement prunes at LIVENESS (a forced
   over-agreeing support is not an exact-`A` witness for ANY realiser, so it
   never enters the candidate set); the selector prunes at ATTRIBUTION
   (which of several live witnesses is charged). In the banked
   `stage4_scan.live_family` these are literally the `over` dict and the
   `tuple(sorted(S))` lex tie-break.
2. **Equivariance.** Relabel the domain by a permutation `sigma`. The
   over-agreement set is EQUIVARIANT (`LB(sigma F) = sigma(LB(F))`); the
   support-lex selector is NOT (`sel(sigma F) != sigma(sel(F))` on a
   positive fraction of relabelings).
**B-F5:** the over-agreement set fails equivariance, OR the lex selector's
choice IS equivariant under every relabeling — either outcome means SAME
species and must be reported as such.
**B-P5b (interaction).** Predicted INDEPENDENT: applying the L-B prune
first does not change the selector's surviving count. **B-F5b:** it does
(then the mechanisms interact and that must be reported).

---

## Scope limits fixed in advance

* Toy fields only (`q <= 6421` for part A ray work, `q = 41` for the P-B
  fixture); official-scale statements are EXACT INTEGER ARITHMETIC on the
  banked row pins only.
* No node is edited; no status is flipped; every claim that depends on an
  unproved input (CONJECTURE OV, Deza's dichotomy) is labelled CONDITIONAL
  in the report.
* Part A's bound is a statement about the CORE's covering design; it is
  NOT a claim that P-A1's live families are of that shape.

---

# ADDENDUM (registered 2026-08-03T17:43:02Z)

Written AFTER the hard-law-5 subtraction sweep and BEFORE any machine
computation in this directory (`verify.py` still does not exist at this
timestamp). Honest labelling: the statements below were derived BY HAND
during the sweep, so they are *not* blind predictions; what is
pre-registered is the FALSIFIER, i.e. the machine check that can kill
them. Reported as fired if fired.

## Subtraction result that forces a re-framing of PART A

The sweep found A-P1 and A-P3 ALREADY BANKED:
* the complement floor `2t >= h+1` is `e := 2t-h >= 1`
  (`v5_occupancy/REPORT.md:39-42`, 31,746 admissible tuples);
* the sunflower ceiling `|K| <= 1 + A/p` is `V <= (n_U-lam)/(t-lam)`
  (`overlap_sliver/PREREG.md:83-86`, `verify.py:546-556,841`) and, in the
  `lam=0` case, `clique_Vmax = u//(h-d)`
  (`support4_relation/stage5_escape.py:263-265`);
* A-P6 (rank cannot bound `|K|`) is banked twice
  (`v5_occupancy/REPORT.md:15-18`, rank `=3h` at `V=5,10,66`;
  THEOREM F "independent of V").
Therefore PART A is a TRANSFER, not a derivation, and the report must say
so. The only new content admissible in PART A is A-P8/A-P9 below.

## A-P8 (NEW — the escaping part of the core is unconditionally bounded)

Let `K` be a live `(T)`-clean core system (every ray in the core, distinct
slopes, `|K| >= 4` by LEMMA B), `t := |U_K| - A`, `m := h+t`,
`e := 2t-h`. Write `esc_1 <= ... <= esc_V` for the sorted escapes and
`K_+ := #{a : esc_a >= 1}`. THEOREM D (`escape1_realizability`) gives
`rank >= sum_a esc_a + G3` with `G3 = 3h - (esc_1+esc_2+esc_3)`; D0-3
(`exact_k_heart`, proved direction: equality kills the family) gives
`rank <= 2(|U|-k) - 1 = 2m-1`. Hence

```text
(i)   sum_{i>=4} esc_i  <=  2m-1-3h  =  2t-h-1  =  e-1
(ii)  |K_+|  <=  e+2  =  2t-h+2                (unconditional)
(iii) at the complement floor e = 1:  |K_+| <= 3
```

**A-F8:** any banked or constructed live `(T)`-clean core fixture with
`|K_+| > e+2`, or `rank > 2m-1`, or violating THEOREM D's inequality.

## A-P9 (NEW — the zero-escape counting threshold)

For a zero-escape core (every point of `U` covered `>= 3` times), the
triple gate `(T)` plus Jensen on `sum_x C(mult(x),3) <= C(V,3)(k-1)`
forces, with `beta := A/(A+t)`,

```text
A (beta V - 1)(beta V - 2)  <=  (V-1)(V-2)(k-1) ,
```

which bounds `V` iff `A beta^2 > k-1`, i.e. iff `(A+t)^2 < A^3/(k-1)`.
PREDICTION: at all six recorded rows this holds at the MINIMAL admissible
`t = ceil((h+1)/2)` and FAILS at `t+1` — the unconditional counting bound
exists in a one-integer window and dies immediately above it.
**A-F9:** the inequality is violated by a constructed zero-escape
gate-clean fixture (the derivation is then wrong), or the finite/infinite
threshold does not sit exactly at the minimal `t` at some row.

## B-P6 (NEW — rigidity pins the BASE, not the FIBRE)

THEOREM F's P-B transfer is: `3` witnesses pin the affine line `L` (hence
the pencil), because (STAR) has `2h` unknowns `(alpha,beta)` modulo the
`3`-parameter Mobius reparametrisation of `z` and each witness costs
`h-1` net conditions. Consequently rigidity bounds the number of DEGREES
OF FREEDOM of the family, **not** its size `M = |E^{-1}(L)|`, which is a
fibre count of the moment map. PREDICTION at THEOREM 3's fixture
(`n=20,q=41,K=4,h=3,A=7`): `|E^{-1}(e_1-axis)| = 40 = 2n`, a union of TWO
complete free `mu_20`-orbits — so `M <= n` is the SINGLE-ORBIT ceiling and
the full planted family is twice it.
**B-F6:** `|E^{-1}(L)| != 40`, or it is not a union of complete free
`mu_20`-orbits, or `3` witnesses fail to pin `L`.

## B-P7 (NEW — the orbit-size arithmetic is exact at every official row)

`Stab(S_0) <= mu_n` of order `s` forces `S_0` to be a union of `A/s`
cosets of `mu_s`, so `s | gcd(n,A)`, and orbit size `= n/s`. PREDICTION:
at all six official rows `n` is a `2`-power and `A = K+h` is ODD (`h` odd
at every row), so `gcd(n,A) = 1`, every `mu_n`-orbit is FREE, and a
single-orbit realised family has `M = n` EXACTLY (not merely `<= n`).
**B-F7:** `gcd(n,A) != 1` at any official row, or a stabiliser order not
dividing `gcd(n,A)` at the fixture.
