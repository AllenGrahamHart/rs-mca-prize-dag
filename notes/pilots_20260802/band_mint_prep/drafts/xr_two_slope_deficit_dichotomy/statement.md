# xr_two_slope_deficit_dichotomy

- **status:** PROVED
- **closure:** proof
- **scope:** both theorems are interpolation/counting arguments valid at
  every scale; every empirical figure quoted is toy-scale and labeled.
- **provenance:** occupancy-v2 pilot THEOREM 2 and THEOREM G
  (`notes/pilots_20260802/xr_occupancy_v2/{REPORT,FABLE_AUDIT}.md`,
  `hunt.py` stage E0: 371 cumulative witnessed sharing events, 0
  violations), under the per-ray accounting amendment
  (`notes/pilots_20260802/adv_sublinear_rank/`,
  `notes/BAND_LANE_DEFINITIONS.md` item 11).

## Setting

As in `xr_two_slope_cost_theorem`: `RS_k` on `n` distinct points of
`F_q`, `A = k + h`, `C_S` the shortened dual (L1 there), core/depth per
definitions item 1 (`core := |S_z ^ S_z'| = |Z_P|`, `d := core - k`,
symbol `k` never `K`), band (proper) = depths `[1, h-2]` (item 2).
**Live slope** = exact-`A` max agreement over ALL of `P^1(F_q)`
including `(0:1)`; selected support = the ONE first-match exact-`A` ray
(item 7).

Standing hypotheses (per definitions item 5 these theorems use ONLY the
following — the hypothesis line cites the generic core ceiling, item 4,
never "below cascade"):

- **(H1) k-packing:** distinct codeword pairs have
  `|Z_P ^ Z_P'| <= k-1` — BANKED, verbatim, at
  `background/nodes/xr_mismatch_chart_nongeneric_joint_support_equivalence/proof.md:19-22`;
  consumed here, not re-derived (hard law 5).
- **(H3) tangent gate, pencil-wide:** for every `z in P^1(F_q)`
  INCLUDING `(0:1)` and every codeword `c`, `agr(c, w_z) <= A`
  (`w_z = u + zv`, `w_{(0:1)} = v`).

## Statement (both PROVED)

1. **THEOREM 2 (low/high dichotomy).** Fix a band depth `d` with
   `2d >= h`. Under (H1) + (H3), for every received pair:
   (a) no two distinct depth-`d` codeword pairs have proportional
   differences (`f_1 - f_2 = -z (g_1 - g_2)` for some `z in P^1`), and
   (b) no ray of agreement `>= A` carries two distinct depth-`d` cores.
   Both fail through the same integer: two depth-`d` cores overlap in
   `<= k-1` points (H1), so their union has size
   `>= k + 2d + 1 >= k + h + 1 = A + 1`, which either (a) becomes the
   agreement of a single codeword against one pencil word — an over-`A`
   agreement, barred by (H3) — or (b) must fit inside one agreement set
   of size `A`. **Consequently the sunflower deficit mechanism (two
   same-depth data forced to share a slope through a `(k-1)`-overlap)
   exists ONLY at `d <= (h-1)/2`.**
2. **THEOREM G (sharing criterion — the structural core).** Let
   `(z_1, S_1) != (z_2, S_2)` be rays of agreement `>= A` (agreement
   sets `S_1, S_2`).
   (i) Their shortened duals share rank iff the supports overlap past
   `k`: `dim (C_{S_1} ^ C_{S_2}) = max(0, |S_1 ^ S_2| - k)` (L1).
   (ii) If `z_1 != z_2` and `|S_1 ^ S_2| >= k + 1`, then `S_1 ^ S_2`
   IS the joint agreement set of a codeword pair `P` — exactly, by the
   fibre identity — and both `z_1, z_2` are live for `P`: the overlap
   is itself a two-slope band pair at depth `e = |S_1 ^ S_2| - k`.
   (iii) **Complementary-depth bound:** if a ray of agreement `A`
   carries two distinct cores of depths `d` and `e`, then
   `d + e <= h - 1`.
   **Every unit of pairwise dual-rank sharing is witnessed by another
   band pair** — the deficit structure is self-referential and graded,
   one depth trading against another inside `h - 1`.
3. **Transversality floor (context for G).** Distinct cores are always
   transverse: `C_{Z} ^ C_{Z'} = 0` for distinct pair cores (H1 +
   L1), so the ONLY pairwise sharing channel between two-slope data is
   ray-support overlap, which is Theorem G.

## Explicitly NOT claimed (context)

- **No claim that pairwise sharing exhausts family rank deficits.**
  Relations of ray support 4 exist in admissible systems
  (`xr_support4_structure`); Theorem G prices the pairwise channel
  only. Support `<= 3` relations are zero (distinct-slope
  transversality + k-packing, the adv_sublinear_rank record).
- **No occupancy bound**; the band occupancy lemma stays open.
- **No extremality of the sunflower** (REFUTED by K_V — the sunflower
  is the cycle, not the cheapest admissible configuration).
- Theorem 2 does not empty the high band: depth-`d` band pairs with
  two live slopes exist at `2d >= h`; the theorem removes the SHARING
  mechanisms there, so each such pair pays its full rank (the
  `xr_two_slope_cost_theorem` `2h`).
- The "below cascade" hypothesis is NOT used anywhere in this node
  (definitions item 5): only (H1) and (H3).

## Falsifier

An admissible received pair with two distinct depth-`d` codeword pairs,
`2d >= h`, having proportional differences or sharing a live ray; or
two rays with `z_1 != z_2`, `|S_1 ^ S_2| >= k+1` whose overlap is NOT
the exact joint agreement set of a codeword pair with both slopes at
agreement `>= A`; or a ray carrying cores of depths `d, e` with
`d + e > h - 1`.

## Verifier

`verify.py` in this node (profile: `tiny`, pure python integers,
deterministic, no third-party imports, no reads outside this
directory). Checks: the dichotomy integer (`k + 2d + 1 > A` iff
`2d >= h`); a PLANTED proportional-difference pair at `2d = h` whose
forced ray over-agrees (`A + 1`), i.e. the gate fires exactly as
Theorem 2 predicts; realized admissible fixtures (single data at
`2d >= h`, a sunflower cycle at `d = (h-1)/2`, spread families) scanned
by a fresh exhaustive interpolation engine covering ALL of `P^1`
including `(0:1)`: 0 live-ray double-carries and 0 proportional
differences at `2d >= h`, Theorem G (i)-(iii) at every ray pair with
witnessed sharing events counted, core transversality, and the
mechanism's EXISTENCE at `d <= (h-1)/2` (the sunflower fixture's
shared slopes with proportional differences — the dichotomy is
two-sided).
