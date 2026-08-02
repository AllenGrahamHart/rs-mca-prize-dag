# Band-lane definitions of record (ratified 2026-08-02)

Source: the band-adjudication pilot's definitions list
(`notes/pilots_20260802/band_adjudication/REPORT.md` section 4), extended
by the ratified Route T decisions and the occupancy/support-4 pilots.
These are the wordings standing hypothesis lists and new statements MUST
use; older wordings are corrected via dated node addenda, never silently.

1. **core(z,z')** := |S_z ^ S_z'| = |Z_P| (T2); **depth** d := core - k;
   symbol pinned: `k` (never `K`).
2. **band (proper)** := cores [k+1, A-2] = depths [1, h-2]; NEVER "band"
   for [k+1, A-1] without the word "column".
3. **cascade tier** := core A-1 = depth h-1 — the unique generic-branch
   cascade depth; under ratified Route T it is a NAMED tier of the band
   COLUMN [1, h-1] (`xr_graded_tangent_band_charge`).
4. **generic core ceiling** := all distinct-slope selected-support cores
   <= A-1 — the SOURCED unconditional property (genericity + strip
   forcing). This, not "cores <= k", is what standing hypothesis lists
   say for the raw generic branch; "cores <= k" holds only for the
   post-band-column remainder, by the R2 partition.
5. **below cascade** := the cascade tier is EMPTY (max joint pair
   agreement <= A-2) — STRICTLY STRONGER than genericity and NOT
   available in the generic branch. Band-ledger theorems use only
   k-packing + the tangent gate, so their hypothesis lines must cite
   item 4, not this. The KEY LEMMA's "cascade event" usage renames to
   "joint-explanation event".
6. **strip-free** := none of P0-P3 fires (incl. P2 single-slope
   over-agreement and P3 quotient-periodicity at any M > 1,
   M | gcd(n,k)). The MC pair is NOT strip-free (P3) — decisive; whether
   P3 formally fires depends on the quotient convention ("syndromes
   descend"), an open adjudication item.
7. **live slope** := exact-A max agreement, over ALL of P^1 including
   (0:1); selected support = the ONE first-match exact-A ray.
8. **L_P / N_d**: L_P counts SELECTED supports containing Z_P;
   N_d = #{depth-d pairs with L_P >= 2}. LOAD-BEARING non-example: under
   "any exact-A ray" (unselected), MC's N_{h-1} jumps n/2 -> 2^197.
   Selected-count measurements are LOWER than MC predictions because
   non-MC exact-A rays compete in first-match selection (safe direction;
   say so when comparing).
9. **Gamma_casc** = DISJOINT union of the Lambda_P (k-packing
   exclusivity): |Gamma_casc| = Sum L_P exactly — the ledger is TIGHT at
   the cascade tier.
10. **structured/coset family** := core complement a mu_M-coset union,
    M = 2^ceil(log2 d); THEOREM BP(1): structured => d is a power of two.
11. **per-ray accounting** (accounting of record, support-4/occupancy-v2
    pilots): condition-rank statements are FAMILY-RANK statements charged
    per ray (rank <= V*h, M <= C(V,2)); the per-datum/per-pair-additive
    reading mispredicts the sunflower by exactly 2x. State costs per ray.
12. **occupancy heart (escape form)**: "every ray support has >= 2 points
    lying in at most two supports" => the occupancy lemma is PROVED;
    open sub-items = the zero-escape collapse (rank = 2m exactly) and
    V <= m/2 for non-collapsing systems (m = |union S| - k).
