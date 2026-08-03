# xr_two_slope_cost_theorem

- **status:** PROVED
- **closure:** proof
- **scope:** toy-verified rank laws proved for every admissible datum at
  every shape (the proofs are scale-free interpolation/linear algebra);
  the six-row ceiling table is exact integer arithmetic at the pinned
  official parameters.
- **provenance:** occupancy-v2 pilot THEOREM 1 + corollary
  (`notes/pilots_20260802/xr_occupancy_v2/{REPORT,FABLE_AUDIT}.md`,
  engine `tslib.py`, checks `cost.py` 59/59), CORRECTED to the per-ray
  accounting of record by the same-day adversarial pilot
  (`notes/pilots_20260802/adv_sublinear_rank/{REPORT,FABLE_AUDIT}.md`,
  K2) and `notes/BAND_LANE_DEFINITIONS.md` item 11.

## Setting

`RS_k` on a domain of `n` distinct points of `F_q`, `A = k + h` the
selected support size, band depths `d in [1, h-2]`. Symbol pinned: `k`
(never `K`). For `S` a point set with `|S| >= k`,
`C_S = {c : supp(c) inside S, c _|_ RS_k}` (shortened dual), and

- **(L1)** `dim C_S = |S| - k` and
  `dim (C_S ^ C_T) = max(0, |S ^ T| - k)` (MDS shortening; proved in
  `proof.md`).

A received pair is `(u,v) in F_q^n x F_q^n`. A codeword pair
`P = (f,g)` has joint agreement `Z_P = {i : f(x_i) = u_i, g(x_i) = v_i}`;
**core** of two selected supports `:= |S_z ^ S_z'| = |Z_P|`, **depth**
`d := core - k`. A **live slope** is an exact-`A` max-agreement direction,
over ALL of `P^1(F_q)` including `(0:1)`; **selected support** = the ONE
first-match exact-`A` ray (definitions items 1, 7).

A **depth-`d` two-slope datum** is `(Z; z_1, S_1; z_2, S_2)` with
`|Z| = k + d`, `|S_j| = A`, `Z = S_1 ^ S_2`, `z_1 != z_2` in
`P^1(F_q)`. It imposes on `(u,v)` the linear conditions

```text
(C0)  <c,u> = <c,v> = 0            for all c in C_Z
(Cj)  <c,u> + z_j <c,v> = 0        for all c in C_{S_j}   (j = 1, 2;
                                    z = (0:1) means <c,v> = 0)
```

with row space `R(P) = (C_Z x C_Z) + G_{z_1}(C_{S_1}) + G_{z_2}(C_{S_2})`,
`G_z(W) = {(c, zc) : c in W}`, inside `F_q^n x F_q^n`.

**Lemma 0 (fibre identity; graded-band-ledger pilot THEOREM 2, proved
inline in `proof.md`).** If live slopes `z_1 != z_2` have
`|S_{z_1} ^ S_{z_2}| >= k`, the forced pair `P` satisfies
`S_{z_1} ^ S_{z_2} = Z_P` EXACTLY. So the datum shape above (core =
support intersection, on the nose) is what realized two-live-slope band
pairs actually produce; it is not an assumption.

## Statement (all PROVED)

1. **THEOREM (exact per-datum cost).** For every admissible depth-`d`
   two-slope datum, at every `d in [1, h-2]` and every slope pair
   including `z in {0, (0:1)}`:

   ```text
   dim R(P) = 2d + (h-d) + (h-d) = 2h,   independent of d.
   ```

   Moreover the core rows are IMPLIED by the ray rows
   (`(c, z_1 c) - (c, z_2 c) = (0, (z_1-z_2) c)` for `c in C_Z`, and
   `C_Z <= C_{S_1} ^ C_{S_2}`), so
   `R(P) = G_{z_1}(C_{S_1}) + G_{z_2}(C_{S_2})` — the accounting object
   is the RAY SYSTEM (definitions item 11).
2. **THEOREM (free-slope codimension).** With the two slopes free, the
   realisation locus (union over the ~`q^2` slope pairs of the
   `2h`-codimensional prescribed-slope kernels) has codimension `2h - 2`:
   every prescribed pair has rank exactly `2h`, and distinct slope pairs
   have distinct kernels (strictly larger joint rank).
3. **COROLLARY (two-slope design ceiling — per-ray accounting of
   record).** `RS_k x RS_k` lies in every kernel, so a family is
   realisable by a NON-degenerate received pair only if its total rank
   is `<= 2(n-k) - 1`. Hence, per-RAY: a realisable family carried by
   `V` rays has `rank <= V h`, so `V <= (2(n-k)-1)/h`, and datum counts
   are BINOMIAL in the ray count: `M <= C(V,2)`. Per-DATUM (the weaker,
   historic form): a prescribed-slope family of `M` data with total rank
   `2hM - delta` has `N_d = M <= (2(n-k)-1+delta)/(2h)`; with slopes
   free, `/(2h-2)`.
   Exact six-row values (verifier-recomputed):
   per-datum prescribed `floor((2(n-k)-1)/(2h))` = 153/179/319 (RowC)
   and 191/223/479 (prize); free `floor((2(n-k)-1)/(2h-2))` =
   191/223/479 on both triples; per-ray `floor((2(n-k)-1)/h)` =
   307/358/639 (RowC), 383/447/959 (prize); at the prize rows the
   `d = 1` point budget caps `V* = floor((n-k+1)/(h-1)) = 192/224/480`
   and the corresponding datum counts are `C(V*,2)` =
   **18,336 / 24,976 / 114,960** (the K_V re-pricing; ~`10^22` inside
   the ratified `0.68 n^2` requirement, margin `>= 2.9e19`).

**LOAD-BEARING correction (kept from the record).** The cost theorem is
a FAMILY-RANK statement charged per ray, NEVER a per-datum-additive
charge: the per-pair-additive reading mispredicts the sunflower family
(cycle: `V` rays, `M = V` data, rank `Vh`, cost `h` per datum) by
exactly `2x`, and the admissible `K_V` family (`V` rays,
`M = C(V,2)` data, rank `Vh`, cost `-> 2(d+1)` per datum) by an
unbounded factor. The banked six-row values 191/223/479 are RAY-count
ceilings; datum counts are their binomials.

## Explicitly NOT claimed (context)

- **No occupancy bound.** Nothing here bounds `N_d` for admissible
  families; the band occupancy lemma stays open (the red TARGET
  `xr_graded_tangent_band_charge` names it). The ceiling binds only
  through the realisability rank inequality, and the datum-count bound
  `M <= C(V,2)` is an identity of the accounting, not a cap on
  admissible `V` beyond `V <= (2(n-k)-1)/h` and the point budget.
- **SHARP-OCC's strong law is REFUTED** (`N_d <= floor((n-k+1)/(h-d))`
  fails by `5.25x` against the admissible `K_V` construction); only the
  weak form `N_d <= n/2` survived at all six rows, and it is a
  CONJECTURE, not claimed here.
- **"Cheapest admissible family = the sunflower at `h`" is REFUTED**
  (K_V reaches `2(d+1)` per datum); no extremality claim is made.
- **Core independence is NOT a law** (dims short by 1-4 at `d >= 2`,
  worst-of-60 in the pilot record); route (i) rank arguments must not
  assume it.
- The upper bound `N_d <= C(V,2)` as a bound on ADMISSIBLE families is
  conditional on ray independence — exactly the support-4 gap
  (`xr_support4_structure`); rank `= Vh` can fail by the classified
  relation mechanisms.
- Nothing is claimed about official-scale admissibility of any family
  (toy-verified gates only; the prize figures are exact budget formulas
  at the pinned parameters).

## Falsifier

An admissible depth-`d` two-slope datum with `dim R(P) != 2h`; a
prescribed slope pair whose kernel coincides with a different slope
pair's kernel; a realisable family whose rank exceeds `V h`; or an
exact-integer failure of the six-row ceiling table.

## Verifier

`verify.py` in this node (profile: `tiny`, pure python integers,
deterministic, no third-party imports, no reads outside this
directory). Checks: L1 dims and intersection dims; `dim R(P) = 2h` at
five shapes, every band depth, slope pairs including `0` and `(0:1)`;
core rows implied by ray rows (rays-only rank = full rank = `2h`);
tiny-shape all-slope-pairs sweep (rank `2h` for all `C(12,2)` pairs at
`(n,k,h,q) = (9,2,3,11)`) plus distinct-kernel witnesses; family-rank
law `rank <= Vh` with equality on spread (`2hM`), pairwise-core
(`3h < 6h`), and sunflower-cycle (`mh` vs per-datum `2hm` — the exact
`2x`) families; the six-row exact integer ceiling table incl.
`C(V*,2) = 18336/24976/114960`; and an end-to-end realisation at
`(16,4,4,97)`, `d = 1`, confirmed by a fresh exhaustive interpolation
scan (intended core at depth 1, both prescribed slopes live).

## Addendum (2026-08-03, mint-2 audit): the corollary's independence hypothesis, explicit

The corollary sentence "a realisable family carried by `V` rays has
`rank <= Vh`, so `V <= (2(n-k)-1)/h`" is a chain only when
`rank = Vh`, i.e. under RAY INDEPENDENCE — as this node's own
NOT-claimed section already records. The gap is now WITNESSED: a
realised, spread, zero-self-collision `mu_20`-orbit family (n=20,
q=41, K=4, h=3; 20 supports, 20 distinct slopes, condition rank 31 of
60 rows) has `V = 20 > (2r-1)/h = 10`, exceeding the ceiling
(`background/nodes/pb_design_ceiling/`, Theorem 3, machine-verified).
The ceiling bounds INDEPENDENTLY-IMPOSABLE families, never realised
families as such; "rank deficit forces self-collision" is FALSE.
Consumers must read the corollary with the independence hypothesis
explicit.
