# xr_support4_structure

- **status:** PROVED (with the zero-escape COLLAPSE explicitly
  MEASURED-NOT-PROVED — it is recorded, never used as a theorem)
- **closure:** proof
- **scope:** the structure theorems are linear algebra over any prime
  field, valid at every scale; the U-mechanism's full-gate
  admissibility is toy-verified (`n <= 29`); official-scale figures are
  exact budget formulas at pinned parameters.
- **provenance:** support-4 pilot
  (`notes/pilots_20260802/support4_relation/{REPORT,FABLE_AUDIT}.md`,
  `s4lib.py`, stage JSONs; 301 checks + 4 measurements), on top of the
  adversarial pilot's support-`<= 3` transversality
  (`notes/pilots_20260802/adv_sublinear_rank/`), per-ray accounting of
  record (`notes/BAND_LANE_DEFINITIONS.md` items 11, 12).

## Setting

`RS_k` on `n` distinct points of `F_q`, `A = k + h`. A **ray system**
is `(z_a, S_a)`, `a = 1..V`, with `z_a in P^1(F_q)` pairwise distinct
and `|S_a| = A`; its condition row space is
`Row = sum_a G_{z_a}(C_{S_a})`, `G_z(W) = {(c, zc) : c in W}`,
`dim C_{S_a} = h`. The **relation space** is

```text
Rel = {(c_a) in (+)_a C_{S_a} : sum_a c_a = 0, sum_a z_a c_a = 0}
    = {(c_a) : sum_a e(z_a) (x) c_a = 0},   e(z) := (1, z),
```

so `rank(Row) = V h - dim Rel` (per-ray accounting, item 11).
Relations of ray-support `<= 2` are zero (distinct slopes are
transverse) and of support `3` are zero (the triple gate kills the
step) — the adv_sublinear_rank record, consumed. **Multiplicity** of a
point = number of supports containing it; **triple locus** = points of
multiplicity `>= 3`. Hypothesis (T), the triple gate:
`|S_a ^ S_b ^ S_c| <= k - 1` (follows from the banked pair-core
k-packing via the fibre identity when the pairwise intersections are
distinct pair cores). `m := |union_a S_a| - k`.

## Statement

1. **S4-1 (triple-locus localisation) — PROVED.** For every relation
   `(c_a)` and every point `x`: the number of rays with
   `c_a(x) != 0` is `0` or `>= 3` (pairwise independence of the
   `e(z_a)`). Hence `supp(c_a)` is contained in the set of points of
   `S_a` lying in at least two OTHER supports of the relation —
   every relation lives on the TRIPLE LOCUS.
2. **S4-2' (general-position kill; the K_V no-relation THEOREM) —
   PROVED.** If each `S_a` meets the triple locus in `<= k` points,
   the system carries NO relation (a nonzero dual word has weight
   `>= k + 1`, MDS). COROLLARY: the K_V family — supports
   `Y u (pair blocks) u (top-ups)`, triple locus exactly `Y`,
   `|Y| = k - 1` — provably carries no relation and has
   `rank = V h` EXACTLY: the banked K_V rank MEASUREMENT upgrades to
   a THEOREM.
3. **S4-3 (rank-2 rigidity) — PROVED.** In a support-exactly-4
   relation all four `c_a` lie in ONE 2-dimensional
   `L <= C^perp` (two of them solve for the other two through the
   invertible `2 x 2` slope system), and no two are proportional —
   two proportional members force all four proportional and
   `|S_1 ^ S_2 ^ S_3 ^ S_4| >= k + 1`, violating (T).
4. **S4-4 (Mobius / cross-ratio criterion) — PROVED.** With
   `zeta_a := [c_a] in P(L) = P^1` (the forced direction of ray `a`
   in `L`), a support-4 relation exists iff the four points
   `([1 : z_a], zeta_a)` of `P^1 x P^1` lie on a `(1,1)`-divisor,
   i.e. iff

   ```text
   CR(z_1, z_2, z_3, z_4) = CR(zeta_1, zeta_2, zeta_3, zeta_4),
   ```

   and the relation is then unique up to scalar (Segre `4 x 4`
   kernel condition). Slope codimension 1: at fixed supports, the
   relation exists on a codimension-1 slope locus. Minimal case
   (`|U| = k + 2`, `L = C_U`): the weight-`(k+1)` words are
   `e_y = lam^U (x - x_y)|_U`, `zeta_y = x_y` — the slopes must
   replicate the HOLES' evaluation points:
   `CR(z_1..z_4) = CR(x_{y_1}..x_{y_4})`.
5. **S4-14 (connectivity floor) — PROVED.** MDS sum lemma:
   `|X ^ S| >= k` implies `C_X + C_S = C_{X u S}`. For a
   PAIRWISE-INTERSECTING ray system (every `|S_a ^ S_b| >= k`; a
   fortiori when every pair is a datum) with finite slopes,
   `pi_1(Row) = sum_a C_{S_a} = C_{union S_a}`, so

   ```text
   rank >= m = |union_a S_a| - k,
   ```

   and `Row <= C_union x C_union` gives `rank <= 2m`. Charge per ray
   lies in `[m/V, 2m/V]`; **the occupancy floor `2` holds
   AUTOMATICALLY whenever `V <= m/2`** (definitions item 12).
6. **Escape floor / peeling (proved half of the dichotomy).** Peel
   `S_a^{(i+1)} = S_a^{(i)} ^ (triple locus of the current system)`;
   by S4-1 every relation survives peeling, so with limit `S_a^inf`:
   `dim Rel <= sum_a (|S_a^inf| - k)^+` and
   `rank >= sum_a min(h, |S_a \ S_a^inf|)` (the ESCAPE floor — the
   `min(h, .)` cap is load-bearing: the uncapped sum is FALSE on the
   K_V fixture, 40 vs rank 35). In particular: **"every ray support
   has `>= 2` points lying in at most two supports" implies
   `rank >= 2V` (`h >= 2`), i.e. the occupancy lemma's per-ray
   charge `2`** — the purely combinatorial escape form of the heart
   (item 12). *(Honesty note kept from the record: a mis-coded first
   version of this floor was caught and fixed in the pilot; the
   verifier here recomputes it freshly.)*
7. **Zero-escape COLLAPSE — MEASURED, NOT PROVED.** Zero-escape
   cliques (every point of every support in the stable triple locus)
   were measured at `rank = 2m` EXACTLY — the T3-type collapse: the
   row space saturates `C_union x C_union` and every realisation is
   a single joint explanation on the union, not a family — across
   exhaustive slope sweeps (3,876 + 8,855 tuples at two fixtures,
   never `2m - 1`). This is one of the two NAMED OPEN SUB-ITEMS
   (prove the collapse; prove `V <= m/2` for non-collapsing
   systems). Nothing in this node's PROVED claims depends on it.
8. **The U-MECHANISM (standing calibration adversary #3, joining K_V
   and MC).** Builder: `|U| = k + 2` (`dim C_U = 2`), distinct holes
   `y_a in U`, `S_a = (U \ {y_a}) u (pair blocks, |B_ab| = d) u
   (private)`; every pair is a depth-`d` datum; every triple
   intersection is EXACTLY `k - 1` — the gate is SATURATED, not
   violated; the four duals are the minimum-weight `e_{y_a}` (weight
   exactly `k + 1`); with Mobius-matched slopes `dim Rel = 1`
   (deficit exactly 1; no stacking — deficit `<= 1` per ray, S4-10);
   full-gate admissible at 6/6 toy fixtures. Toy pins re-verified
   here: `(k,h,d,V) = (3,5,1,4)`: `rank = Vh - 1 = 19`. Re-pricing
   pins (consistency-checked, budget formula NOT re-derived — see
   AUDIT_CHECKLIST): RowC 1/4, `d = 1`: `U_N = 510` vs K_V `384`
   (ratio `1.328125`) against `n/2 = 512` — SHARP-OCC's weak form
   survives by a MARGIN OF 2, the tightest calibration in the
   program; prize rows UNCHANGED (`18,336/24,976/114,960`, the point
   budget binds first, deficit relative `~1e-10`).

## Explicitly NOT claimed (context)

- **The collapse (claim 7) is not a theorem here** — it is measured;
  and `V <= m/2` for non-collapsing systems is a CONJECTURE (all 9
  observed families conform; Fisher-type bounds give only
  `V <= k + m`).
- **No occupancy bound.** The residual heart, restated two levels
  down, is: "an admissible, non-collapsing, pairwise-intersecting
  ray system with `V > m/2`" — equivalently the escape statement of
  claim 6 fails somewhere. This node supplies the floors and the
  structure theory, not the lemma.
- Double-hole generalisation (`|U| = k + 2l`, `l >= 2`: relations
  for EVERY slope tuple, dimension `Vl - 2(D+1)`) is pilot record,
  not minted here; `D >= 2` pencils argued-not-swept optimal at
  `D = 1`.
- The official-scale `U_N` cluster-packing formula is
  consistency-checked against the persisted JSON, not re-derived.
- Support-`<= 3` transversality is consumed from the
  adv_sublinear_rank record (k-packing does the support-3 kill), not
  re-proved.

## Falsifier

A relation with some point carried by exactly 1 or 2 rays; a
relation on a system whose supports meet the triple locus in `<= k`
points (e.g. any K_V fixture); a support-4 relation with cross-ratios
unequal, or none with them equal (fixed generic supports); a
pairwise-intersecting finite-slope system with `rank < m`; a system
with every ray escaping `>= 2` points and `rank < 2V`; or (would
upgrade claim 7, not falsify this node) a zero-escape clique with
`rank != 2m`.

## Verifier

`verify.py` in this node (profile: `tiny`, pure python integers,
deterministic, no third-party imports, no reads outside this
directory). Checks: the U-mechanism build at `(3,5,1,4)`, `n = 16`,
`q = 97` — combinatorial gates (pairwise `k+d`, triples exactly
`k-1`), `dim Rel = 1`, `rank = Vh - 1`, S4-1 pointwise localisation
(`0` or `>= 3` everywhere), S4-3 (four duals in one 2-dim `L`, no
two proportional, `supp(c_a) = U \ {y_a}`, weight `k+1`), S4-4
(cross-ratio equality on the matched build; a 24-value `z_4` sweep:
`dim Rel = 1` EXACTLY at cross-ratio matches, else `0`); the K_V
no-relation THEOREM at `(3,7,1,5)`, `n = 22` (`triple locus = Y`,
`dim Rel = 0`, `rank = Vh` exactly); S4-14 (MDS sum lemma on
samples; `dim pi_1 = m`; `m <= rank <= 2m`; the `V <= m/2 => charge
>= 2` arithmetic on both fixtures); the peeling/escape floor on both
fixtures (`rank >= sum min(h, |S_a \ S_a^inf|)`, `dim Rel <= sum
(|S_a^inf| - k)^+`; pilot values reproduced: U-mechanism floor
16/cap 4, K_V floor 35 = rank with `S^inf` sizes 2 — and the
UNCAPPED sum 40 shown false); the zero-escape
clique at `(3,5,3,5)`, `n = 10` — `rank = 2m = 14` over 60
deterministic slope tuples, labeled MEASURED; and the re-pricing
consistency pins (`510 = 51 x 10`, ratio `1.328125`, margin
`512 - 510 = 2`).

## Addendum (2026-08-03, round-7 audit): the peel is ONE pass; the kernel floor

Two facts from the audited round-7 unification pilot
(`notes/pilots_20260803/k_escape_unification/REPORT.md`, Theorems U1-U4,
coordinator-replayed 18/18):

1. **Claim 6's peel terminates after one pass** (definitional, no defect):
   with no ray-death rule, a point leaves every support simultaneously or
   none, so `S_a^inf = S_a ^ W_0` always. All recorded floor and fixture
   values are unchanged.
2. **The escape floor is dominated by the KERNEL FLOOR**
   `rank >= sum_a min(h, |S_a \ T*_a|)` where `T*` is the stable limit of
   the full `(3, k+1)`-core operator (support-shrink AND ray-death,
   iterated): proved, strictly better on explicit `(T)`-clean fixtures
   (escape floor 8 vs kernel floor 10 = rank at `k = h = 2`), and equal to
   the escape floor on both banked fixtures here (which is why the two
   residuals looked identical). P-A1's un-peelable core `|K|` is the ray
   side of the SAME operator's greatest fixed point — the two lanes'
   residuals are one covering condition read twice.

## Addendum 2 (2026-08-03, same day, round-7 collapse pilot): claim 7 REFUTED as a general statement

The zero-escape collapse conjecture (`rank = 2m` for zero-escape
cliques) is **FALSE in general**: gate-clean counterexamples X1/X2/X3
(`notes/pilots_20260803/zero_escape_collapse/REPORT.md`, coordinator-
replayed 26/26, falsifiers pre-registered) — zero-escape,
pairwise-intersecting `>= k+1`, k-packing-SATURATED `V = 4` systems
built from four fibres of a polynomial pencil plus one cross-ratio
equation, with `rank = 2m - 1` (X1, X2) and `2m - 2` (X3). The banked
measurement is NOT contradicted: slope sweeps at fixed supports cannot
see a support-locus obstruction; on the measured fixtures the collapse
is now a THEOREM (MDS-chain / triple-cover criteria; the `(3,5,3,5)`
fixture by Corollary 3c). Consequences of record:

1. Claim 7's label was MEASURED and stays accurate for its fixtures;
   the GENERAL conjecture is struck. PROVED claims 1-6 and 8 are
   untouched (none consumed claim 7).
2. The T3-type consequence needs a collapse CERTIFICATE (Theorem 2/3
   hypotheses), not zero escape alone.
3. The secondary criterion's RowC use ("k > 2h^2 holds and the
   collapse is the load-bearing kill there") is now OPEN: Theorem 3
   misses the RowC clique by 3 (triples >= 253 vs k = 256); that kill
   awaits a V >= 5 support-condition argument.
4. "Non-collapsing => V <= m/2" is FALSE (X1, X3) and is struck;
   replaced by the proved V = 4 occupancy floor (Prop 6:
   rank >= min(3t+3, 4t+2) > 2V) and the OPEN V >= 5 question.
5. New proved tools: the duality criterion (collapse <=> Ann = 0), the
   V = 4 cross-ratio classification (exact dual of S4-4), and the
   improved unconditional floor `rank >= m + dim Sum C_{I_ab}`.

## Addendum 3 (2026-08-03, V >= 5 pilot): the secondary criterion is refuted; the exact boundary

The claim-7 secondary criterion ("the zero-escape channel can reach
per-ray charge < 2 only when k > 2h^2") is REFUTED: its computation
was the ceiling 2m/Vmax, an upper bound that cannot certify a lower
bound; the record's own clique shape at (k,h,d) = (5,3,1), V = 5 has
k <= 2h^2 and true charge 1.8 < 2
(`notes/pilots_20260803/v5_occupancy/REPORT.md`, coordinator-replayed
67/67). CORRECTED CRITERION (proved, tight): for the block class of
record, 3h <= rank <= 2m = 2(t+h) with dim Ann <= 2t-h, so charge
>= 2 holds iff 2V <= 3h. The pencil-fibre family extends to every
V >= 4 (dim Ann = 2t-h on the Mobius locus) — the collapse is dead at
every V. At the PRIZE rows 2V <= 3h holds by ~1e8 (no number moves;
the justification is now a proved floor); at the RowC toy rows the
channel provably fails (ceiling charge < 1), and the claim-7 "RowC
load-bearing kill" is unrestorable by any shape-only argument.
