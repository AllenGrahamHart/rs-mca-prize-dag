# WCL slot decomposition — fresh-context adversarial audit (AUDIT A + B)

Repo: /home/u2470931/smooth-read-solomin/prize @ master 8eb59e7c (read-only). Date: 2026-07-22.
Verdict summary: **slot decomposition is MATHEMATICALLY SOUND and COMPLETE (no missing, no
spurious slots); conventions match ground truth exactly; but the zone node's own pose,
conditional, and bookkeeping-of-record are STALE at the L+5/four-slot state** — a
documentation/assembly seam, not a math error. Details below.

---

## 1. Ledger definition of record (derived independently)

Chain: `C1PRIME_LEVEL_SCALED_POSE.md` (r2 conventions, kept verbatim by r3) -> banked M2
machine `critical/nodes/dli_prime_weighted_large_block_support/notes/m2_c1prime_level_scaled_modal.py`
(the RAW ledger of record per MAINTAINER RULING 4a) -> schedule r2 (RULING 4c) ->
`c1r3_program_20260719/c1r3_pose.md` (window L+5 -> L+7, everything else verbatim).

Machine facts (m2_c1prime_level_scaled_modal.py):
- omega = g^((q-1)/n'), g primitive root => omega EXACT order n' = 2N.
- Vanishings: L equations P(omega^(2j-1)) = 0, j = 1..L.
- Space: supports = w-subsets of base exponents [0, N) (`itertools.combinations(range(N), w)`),
  signs {+-1}^w, global sign quotient. Weight = # nonzero terms. Reduced = distinct base
  exponents = antipodal-free distinct root multiset in mu_n' (each element of mu_n' is uniquely
  +-omega^e, e in [0,N)).
- Primitive = no proper nonempty signed sub-support is itself a vanisher of ALL L equations
  (additive indecomposability at the same level). It is NOT an exponent-gcd/exact-order-support
  condition: even-exponent (lower-order lift) supports ARE enumerated and charged at this level
  — consistent with the raw-ledger ruling (lifts charged at their own level). Confirmed also in
  wz2_dedup_spec.md line 55.
- Orbit: signed shift e -> e+s mod 2N with sign flip past N (includes global negation at s=N);
  flat charge 2N*2^-w per orbit.

Schedule r2 (ruling 4c, recomputed exactly under ramguard): t = 2^33, ell_j =
ceil(floor(t/2^j)/2) => dims (2^32, 2^31, ..., 4, 2, 1, 1); sum = 2^33 exactly; ell=1 occurs
TWICE (j=32,33), ell=2,4,8,16,... once each. Per level: L = ell (DIMENSION), N = 256*ell,
n' = 2N = 512*ell, ell vanishing equations. Deepest level ell=2^32 has n' = 2^41 — the origin
of the official gate v_2(q-1) >= 41 (consistency PASS).

**General law (CONFIRMED):** at dimension ell — root of EXACT order 512*ell; ell odd-power
conjugate vanishings P(w), P(w^3), ..., P(w^(2ell-1)); reduced signed polys = w-subsets of
base exponents [0, 256*ell) with signs +-1 mod global sign.

"Any w of exact order n'" vs the fixed omega: equivalent (exact-order elements = omega^k, k odd;
P(omega^k)=0 <=> (k-dilated P)(omega)=0); odd-dilation (Galois) dedup in certificates is exactly
this identification. Sound.

**Exact-order vs order-dividing (the critical convention):** the correct reading is
"generator omega EXACT order n'; the w roots range over the FULL group mu_n' (order dividing)".
Lower-order relation content (e.g. a relation among mu_256 elements at the ell=1 level) embeds
as an even-base-support polynomial evaluated at the exact-order omega, so the full-support
sweep at the exact-order root CONTAINS every order-dividing configuration. An enumerator must
therefore sweep the FULL support space [0, N) with NO coprimality/gcd filter; a
"primitive-support-only" sweep would be UNSOUND (raw ledger charges lifts), while an extra
order-dividing sweep would be redundant but not wrong.

**Newton bound (re-derived):** p_1 = p_3 = ... = p_(2ell-1) = 0 and w <= 2ell kills all odd
elementary symmetric functions e_k (k <= w); odd w => e_w = +-prod r_i != 0 contradiction;
even w => char poly even => antipodal pairs => not reduced. So reduced vanishers need
w >= 2ell+1, uniformly in q (char 0 or char > w; official q > 2^41). Matches
`dli_wcl_newton_short_window_exclusion` exactly.

**Primitivity vs slot phrasing (subtlety, resolved):** slot statements say "NO reduced signed
weight-w polynomial vanishes" (no primitivity qualifier); the ledger needs only "no PRIMITIVE
orbit". Equivalent on the window GIVEN the proved floors: w=2 impossible unconditionally;
(1,3),(1,4) censuses + (2,3)/(2,4) Newton + (2,5),(2,6) certs + (4,<=8) Newton mean any
official-row vanisher in the window would have all proper sub-vanishers of weight >= 5 (ell=1),
>= 7 (ell=2), >= 9 (ell=4), so an imprimitive one needs weight >= 10/14/18 > 8/9/11. Hence
in-window vanisher = primitive vanisher at official rows: the slot form is sound and not
actually stronger. (This equivalence is itself conditional on the floor theorems — all PROVED.)

---

## 2. AUDIT A.1 — per-slot conventions table (stated vs derived)

Derived requirement for cell (ell,w): reduced signed weight-w poly, base exponents in
[0,256*ell), signs +-1 mod global sign; ell vanishings P(omega^(2j-1))=0, j=1..ell; omega exact
order 512*ell in F_q; official row q < 2^256, v_2(q-1) >= 41.

| slot | stated (statement.md / dag.json) | derived requirement | verdict |
|---|---|---|---|
| (1,5) | no reduced signed weight-5 poly vanishes at an order-512 root; official q | 1 vanishing, exact order 512, supports [0,256) | MATCH (wording: "order-512" should say "exact order"; benign — see sec. 1) |
| (1,6) | same, weight 6 | same | MATCH |
| (1,7) | dag: order-512 root, "extended window, w = L+6" | same, w=7; L+6=7 with L=1=dim | MATCH (L used as dimension, correct) |
| (1,8) | dag: order-512 root, "w = L+7" | same, w=8 | MATCH |
| (2,7) | P(w)=P(w^3)=0 at EXACT order 1024 | 2 vanishings, exact order 1024, supports [0,512) | MATCH (identical wording to closed (2,5)/(2,6) certs) |
| (2,8) | dag: P(w)=P(w^3)=0 exact order 1024 | same, w=8 | MATCH |
| (2,9) | dag: same | same, w=9 | MATCH |
| (4,9) | "four odd-power vanishings at order-2048 roots" | P(w^{1,3,5,7})=0, exact order 2048, supports [0,1024) | MATCH (descent node dli_wcl_ell4_weight9_quartic_divisor_descent pins exact order 2048, e in [0,1024), p_1=p_3=p_5=p_7=0) |
| (4,10) | dag: four odd-power vanishings, order-2048 | same, w=10 | MATCH |
| (4,11) | dag: same | same, w=11 | MATCH |

The order-(512*ell) and ell-conjugate law: CONFIRMED for every slot.

---

## 3. AUDIT A.2 — ground-truth cross-check against the CLOSED slots

### (2,5) `background/nodes/dli_wcl_ell2_weight5_norm_gcd_exclusion` (168 Pocklington primes)
Statement: official q<2^256, v_2(q-1)>=41, omega exact order 1024, NO reduced signed weight-5 P
with P(omega)=P(omega^3)=0. verify.py pins the exact space:
- `legal_pairs()`: x=zeta^i, y=zeta^j, i<j in [1,1023]\{512}, (j-i) mod 1024 != 512
  — i.e. ALL unordered pairs from mu_1024 \ {1,-1} with no antipodal collision against {1,x,y}.
  Subgroup (even-exponent) elements INCLUDED. 521,731-511 = 521,220 legal pairs.
- Dedup: odd dilation only (unit*pair mod 1024, unit odd) -> exactly 1,514 orbits, canonical
  min representative, ledger row order forced equal to `representatives()`.
- Router (dli_wcl_ell2_weight5_pair_quadratic_router, PROVED iff-form): any antipodal-free
  five-subset R of H=mu_1024 with sum r = sum r^3 = 0 normalizes (scale by e^-1) to a legal
  pair; final two roots = roots of T^2-vT+B in H; membership <=> B^M=1, D_M=2 (M=1024).
- Obstruction: q | gcd(|Norm F|,|Norm G|); all 1,514 gcds >= 1 (no double-zero pair occurred;
  verify rejects gcd<1); 507 distinct nontrivial gcds completely factored (product check);
  168 prime roots via 282-node recursive Pocklington graph; max v_2(p-1)=18 < 41.
  3/3 negative controls.

### (2,6) `background/nodes/dli_wcl_ell2_weight6_recursive_norm_exclusion` (404,740 orbits)
Statement: identical conventions, weight 6. proof.md + verify.py pin:
- Space: reduced antipodal-free six-set R of H=mu_1024, sum r = sum r^3 = 0; router selects
  {1,x,y} + d in H (ALL 1024 products): 1,514 pair orbits x 1024 = 1,550,336 presentations;
  quotient by triple rebasing (a,b,c)->(-a,b-a,c-3a) and odd dilation -> 404,740 candidate
  orbits (counts + histograms + representative digest enforced by verify.py; wave-9 independent
  reproduction).
- Branch 1: 404,230 nonzero saturated gcds (Norm(u)-saturation sound via the paid ell-2
  weight-3 exclusion), complete factorizations, 443 prime roots, 626-node Pocklington graph,
  max v_2(p-1)=18 < 41.
- Branch 2: 510 identically-zero pairs = exactly the structural family; power-of-two
  vanishing-sum lemma forces an antipodal pair => fails the reduced guard. Branches exhaust.

### Verdict
The certificates swept EXACTLY the space the open-slot conventions predict for (2,w):
same reduced/signed space (full mu_1024 root sets incl. subgroup-supported), same two
conjugate vanishings, same exact-order-1024 generator convention, dedup only by legitimate
symmetries (odd Galois dilation; rebasing; both preserve the defining property and norms).
**NO order-dividing/exact-order mismatch, NO signed/unsigned mismatch, NO orbit-dedup
mismatch, NO exponent-range mismatch.** Future (2,7)-(2,9) sweeps modeled on these
certificates target the RIGHT space. The one convention future sweeps must not drop:
the candidate space must keep subgroup-supported configurations (raw ledger).

Also cross-checked (1,3)/(1,4)/(2,3) censuses (the machinery named as attack for the six
extended slots): supports {0..255} (resp. {0..511}), signs mod global sign,
Res(X^256+1, P) resp. Res(X^512+1, P) — X^256+1 = Phi_512, X^512+1 = Phi_1024, i.e. evaluation
exactly at EXACT-order roots; affine-Galois dedup e -> a e + b (a odd) = signed shift + dilation,
both norm-invariant. Conventions identical to the ledger. MATCH.

---

## 4. AUDIT A.3 — weight-3/4 floor mapping (every sub-window cell, every ell)

Cells with w in {3,4} inside the r3 window [ell+1, ell+7] exist only at ell=1 ([2,8]) and
ell=2 ([3,9]). For ell >= 4 the window starts at ell+1 >= 5: no (ell,3)/(ell,4) obligation
exists. Exact per-cell exclusion map:

| cell | excluded by | scope/gate |
|---|---|---|
| (1,2) | Newton short-window (w<=2ell=2); also elementary (omega^{e1-e2} = +-1 impossible, e in [0,256)) | field-uniform |
| (1,3) | dli_wcl_weight3_ambient_exclusion — 11,054,080 supports, 254 affine-Galois classes, 439 primes, max v_2=18 | official rows (q<2^256, v_2>=41); explicitly "either terminal ell=1 level" (covers BOTH ell=1 levels j=32,33) |
| (1,4) | dli_wcl_weight4_ambient_exclusion — 1,398,341,120 supports, 24,979 classes, 44,599 primes, max v_2=29 | official rows; both ell=1 levels |
| (2,3) | Newton (w<=4) AND dli_wcl_ell2_weight3_ambient_exclusion (88,954,880 supports, 510 classes, 1,141 primes, max v_2=21) | Newton field-uniform; census official |
| (2,4) | dli_wcl_ell2_weight4_newton_exclusion AND Newton short-window (w<=4) | field-uniform (char not in {2,3}) |
| (2,5) | dli_wcl_ell2_weight5_norm_gcd_exclusion | official rows |
| (2,6) | dli_wcl_ell2_weight6_recursive_norm_exclusion | official rows |
| (4,5)..(4,8) | Newton short-window (w<=2ell=8) | field-uniform |
| ell>=8, whole window [ell+1,ell+7] | Newton short-window (ell+7 <= 2ell for ell>=7; scheduled ell>=8) | field-uniform |

- The ell=1 floor at w=5 is sound: (1,2) Newton/elementary + (1,3),(1,4) censuses. It is
  OFFICIAL-ROW-only at w=3,4 (weight-3 relations exist at non-ambient primes — scope
  guardrail); fine, WCL-ZONE is an official-row statement.
- The (4,w) floor at 9 comes from NEWTON (w >= 2ell+1 = 9), NOT from the weight-3/4 theorems.
  CONFIRMED.
- Display lag (non-blocking): `dli_wcl_newton_short_window_exclusion/statement.md`'s
  "consequently" table prints the L+5-era windows (2..6 / 3..7 / 5..9 / ell+1..ell+5) and the
  historical six-slot list. The THEOREM (w <= 2ell) is window-free and covers the r3 windows;
  the ell>=8 r3 consequence (ell+7 <= 2ell) is asserted in c1r3_pose.md, not in the node.

---

## 5. AUDIT B — window seam vs C1'-r3

### B.1 What is L in W_ext?
In C1'-r3 (dli_c1r3_gated_envelope_bound/statement.md + c1r3_pose.md), L is the ROW parameter
of (q, n'=2N, L) with 2^N >= q^L, N >= 16L — at production this is the level DIMENSION
ell_j (N_j = 256*ell_j, r_j = q^{ell_j}/2^{256 ell_j}; pose text explicitly uses
"for every scheduled level ell >= 8, L+7 <= 2L"; ruling 4c). NOT the level index j=0..33.
Induced per-dimension windows: ell=1 -> w in [2,8] (two levels, j=32,33); ell=2 -> [3,9];
ell=4 -> [5,11]; ell>=8 -> [ell+1, ell+7], entirely Newton-empty.

### B.2 Slot ends vs induced window; missing/spurious
Upper ends: (1,8),(2,9),(4,11) = ell+7 EXACTLY. Lower ends: window start ell+1 formally
(2/3/5), but the BINDING floor is: ell=1 — censuses (Newton only reaches w=2); ell=2 —
certs (Newton reaches 4 = 2ell, certs close 5,6); ell=4 — Newton (2ell = 8 binds, so slots
start at 2ell+1 = 9 > ell+1 = 5). Exact enumeration (recomputed under ramguard):

  ell=1 [2,8]: 2 Newton | 3,4 censuses | 5,6,7,8 SLOTS
  ell=2 [3,9]: 3,4 Newton | 5,6 certs | 7,8,9 SLOTS
  ell=4 [5,11]: 5-8 Newton | 9,10,11 SLOTS
  ell>=8: all Newton

Predicted slot list = {(1,5),(1,6),(1,7),(1,8),(2,7),(2,8),(2,9),(4,9),(4,10),(4,11)} =
exactly the ten minted TARGET nodes, all ten req-wired to dli_wcl_zone_coverage in dag.json.
**NO MISSING SLOT. NO SPURIOUS SLOT.**

### B.3 Which window does each seam consume? Residual L+5 text
CONSISTENT (operative, r3/ten-slot): dli_c1r3_gated_envelope_bound (statement, W_ext L+1..L+7);
c1r3_pose.md; dli_marginal_baseline100_coverage/conditional.md 2026-07-21 addendum ("W_ext <=
1/32 via the EXTENDED slot set... window extension L+5 -> L+7 on both sides keeps the 41/8
arithmetic verbatim"); the ten slot statements; dag.json req wiring (10 edges).

STALE (still L+5-era) — the seam findings:
- **[S1]** `critical/nodes/dli_wcl_zone_coverage/statement.md` line ~16: the zone node's OWN
  operative formula is still `sum_(primitive O, L+1<=w(O)<=L+5) 2N_L*2^-w(O), N_L=256L` (both
  the old window AND the superseded N_L=256L display at the top; r2 correction only appended
  below). The node claimed by the baseline as supplying W_ext <= 1/32 nowhere defines W_ext.
- **[S2]** `critical/nodes/dli_wcl_zone_coverage/conditional.md`: the assembly proves
  "WCL-ZONE holds iff the FOUR slots (1,5),(1,6),(2,7),(4,9) are empty" (the L+5 equivalence).
  The ten-slot equivalence needed for WCL-ZONE-ext is wired in dag.json but NOT assembled in
  the conditional. If a census closed only the four old slots, the baseline premise would still
  be unproved — the conditional must be re-issued as: WCL-ZONE-ext holds iff ALL TEN slots
  empty (every component of that equivalence is already PROVED: Newton + censuses + 2 certs).
- **[S3]** `critical/nodes/dli_wcl_zone_coverage/official_terminal_attack.md` — the file every
  one of the ten slot statements names as "bookkeeping of record" — ends at the wave-9
  FOUR-slot residual (2026-07-17) and never mentions (1,7),(1,8),(2,8),(2,9),(4,10),(4,11) or
  the L+7 window. The bookkeeping of record does not know about six of its ten slots.
- **[S4]** `background/nodes/dli_wcl_raw_ledger_interface_guardrail/statement.md` line 12:
  W_raw displayed with L+1..L+5 (the guardrail's content — raw vs dedup — is window-agnostic,
  but the display is L+5-era).
- **[S5]** `dli_wcl_newton_short_window_exclusion/statement.md` consequence table: L+5 windows
  + six-slot list (see sec. 4).
- **[S6]** dag.json `dli_wcl_zone_coverage.statement` text: old L+5 formula + "first-owner
  de-duplication" phrase (struck by ruling 4a) still leads the field; corrections live only in
  appended history. dag.json `dli_marginal_baseline100_coverage.statement` narrative ends at
  "ROUTE BROKEN -> TARGET (2026-07-13)" while status field = CONDITIONAL (the 07-21 re-arm is
  only in conditional.md).
Historical packets (wz/wz2 falsifier docs, M3/M4, C1PRIME pose, QUALITY.md) legitimately
retain L+5 as history — not defects.

### B.4 Threshold arithmetic / mass margins (exact, ramguard)
Single-orbit mass = 2N*2^-w = 512*ell*2^-w; threshold 1/32.

| slot | one-orbit mass | x threshold |
|---|---|---|
| (1,5) | 16 | 512x |
| (1,6) | 8 | 256x |
| (1,7) | 4 | 128x |
| (1,8) | 2 | 64x |
| (2,7) | 8 | 256x |
| (2,8) | 4 | 128x |
| (2,9) | 2 | 64x |
| (4,9) | 4 | 128x |
| (4,10) | 2 | 64x |
| (4,11) | 1 | 32x |

- NO cell in any ell in {1,2,4} window is excluded by mass alone; every slot cell's SINGLE
  orbit already breaches 1/32 by >= 32x. **No slot is a spurious (mass-safe) obligation — all
  ten are load-bearing zero-event cells.** Equivalently W_ext <= 1/32 <=> all ten slots empty.
- No near-threshold cell: minimum overshoot is 32x at (4,11); nothing within 1% (no w8-C9
  analogue). The only exact saturation in the tower is ell=16, w=18 (mass exactly 1/32) —
  Newton-empty, no obligation.
- ell=8: min in-window mass 1/8 > 1/32 (would be zero-event even without Newton); ell>=16:
  weighted regime begins but the whole window is Newton-empty. So the ten-slot reduction is
  robust to the window extension at every level.
- Baseline arithmetic re-verified exactly: 41^34 < 2^202, slack 19.8432 bits; headroom claim
  verified: allowance 6 passes ((1+6*33/32)^34 < 2^100), 7 fails.

---

## 6. PRIMITIVES BLOCK (pinned, for the completeness enumerator)

```
TOWER      t = 2^33; levels j = 0..33; ell_j = ceil(floor(t/2^j)/2)
           = (2^32, 2^31, ..., 4, 2, 1, 1); sum_j ell_j = t; ell=1 twice (j=32,33).
PER LEVEL  dim ell; N = 256*ell; n' = 2N = 512*ell; q official: prime, q < 2^256,
           v_2(q-1) >= 41 (=> q ≡ 1 mod n' at every scheduled level, since n' | 2^41
           for ell <= 2^32).
ROOT       omega in F_q of EXACT order n' = 512*ell (any exact-order choice; all are
           odd-dilation conjugate — enumerators may quotient by odd Galois dilation
           e -> a*e, a odd mod n', and by signed shift e -> e+b; both preserve the cell).
SPACE      reduced signed weight-w polynomial: support = w-subset of base exponents
           [0, N), signs s_i in {+1,-1}, global sign quotient allowed. NO gcd/coprimality
           filter on exponents (raw ledger charges lower-order lifts at this level;
           subgroup-supported configurations MUST be swept).
           Equivalent root form: w-subset of mu_n' (elements +-omega^e), pairwise
           distinct AND antipodal-free (r_i != +- r_j).
VANISHING  cell (ell,w) nonempty iff exists such P with P(omega^(2j-1)) = 0 in F_q for
           ALL j = 1..ell  (powers 1,3,...,2ell-1).
PRIMITIVE  no proper nonempty signed sub-support satisfies all ell equations. For the
           ten slot cells, at official rows, in-window vanisher <=> primitive vanisher
           (floor exclusions make parts of weight < 5/7/9 impossible), so emptiness may
           be swept WITHOUT the primitivity filter.
NEWTON     reduced vanishers require w >= 2*ell + 1 (char 0 or char > w; official q ok).
FLOORS     (1,2) Newton/elementary; (1,3),(1,4) ambient censuses (official-gated);
           (2,3),(2,4) Newton (+ ell2 census at w=3); (2,5),(2,6) closed certificates
           (norm-gcd / recursive-norm, official-gated); (4,5..8) Newton.
WINDOW     C1'-r3 / WCL-ZONE-ext: L+1 <= w <= L+7 with L = ell (DIMENSION, never the
           level index j). Induced: ell=1: [2,8]; ell=2: [3,9]; ell=4: [5,11];
           ell >= 8: [ell+1, ell+7] entirely Newton-empty (ell+7 <= 2ell iff ell >= 7).
MASS       per primitive orbit: 2N * 2^-w = 512*ell*2^-w, flat. THRESHOLD: W <= 1/32
           per level. At ell in {1,2,4} every in-window orbit mass >= 1 > 1/32
           => zone bound <=> slot EMPTINESS (zero-event); no mass-safe cell.
COMPLETE   predicted open cell list (window minus Newton minus floors):
CELL LIST  (1,5) (1,6) (1,7) (1,8)   [1 vanishing, exact order 512,  e in [0,256)]
           (2,7) (2,8) (2,9)         [2 vanishings, exact order 1024, e in [0,512)]
           (4,9) (4,10) (4,11)       [4 vanishings, exact order 2048, e in [0,1024)]
           = exactly the ten minted TARGET slots. Both ell=1 levels share the (1,w) cells.
```

Sizing note for sweeps: raw spaces C(N,w)*2^(w-1); the fenced Burnside counts
(weight5_orbit_route_fence.md) are 2,296,920 affine-Galois norm classes at (1,5) and
185,569,028 at (1,6) — the router/moment-system route (as in (2,5)/(2,6)) is the recorded
viable path, not blind norm censuses.

---

## 7. Recommended pre-census fixes (forced, correction-authority class)

1. Re-pose `dli_wcl_zone_coverage/statement.md` header: W_ext with window [L+1, L+7],
   N = 256*ell, dims per r2 (delete/supersede the leading L+5 + N_L=256L display).
2. Re-issue `conditional.md` as the TEN-slot equivalence (WCL-ZONE-ext <=> ten slots empty);
   all components PROVED, purely an assembly re-statement.
3. Append the ten-slot/L+7 section to `official_terminal_attack.md` (it is the named
   bookkeeping of record for all ten slots and currently ends at the four-slot residual).
4. Cosmetic: raw-ledger guardrail window display; Newton node consequence table (add the
   ell+7 <= 2ell line); dag.json statement fields for zone + baseline.
None of these change any mathematics; they close the #198-class two-object risk (a census
run against the four-slot conditional would silently under-prove the baseline premise).
```
