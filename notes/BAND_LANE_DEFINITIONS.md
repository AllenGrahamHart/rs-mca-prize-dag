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

## Addendum (2026-08-03): item 12', the iterated (kernel) escape form

The round-7 unification pilot (audited; `notes/pilots_20260803/
k_escape_unification/REPORT.md` U1-U5) proves item 12's one-step peel is
the FIRST ITERATE of the full `(3, k+1)`-core operator (delete points
covered `< 3` times AND rays holding `<= k` surviving points, to the
greatest fixed point). Item 12' (PROVED, Corollary U5): if `h >= 2` and
every ray of the core escapes `>= 2` points relative to `W_infinity`,
then `rank >= 2V`. This hypothesis is implied by and strictly weaker
than item 12's (an explicit `(T)`-clean fixture fails item 12's
hypothesis while the conclusion holds through the core). The only
channels that can defeat per-ray charge 2 are core rays of escape 0
(the zero-escape collapse, the named open sub-item) and escape 1 (named
by the pilot; whether it reaches the gate-clean admissible class is
OPEN — flag 5 of the report).

## Addendum 2 (2026-08-03, later same day): item 12' channel status update

The collapse pilot settles the escape-0 channel AT `V = 4` positively
(per-ray charge >= 2 holds there unconditionally, Prop 6 of
`notes/pilots_20260803/zero_escape_collapse/REPORT.md`) while REFUTING
the zero-escape collapse itself and `V <= m/2` as general statements.
The occupancy heart's remaining open channels are exactly: (i) V >= 5
zero-escape systems with `(V-3)t + |A_0| <= k - 1` (below the
Corollary-3b kill threshold), and (ii) escape-1 core rays (gate-clean
realizability OPEN, unification flag 5). Wherever this file or item 12'
says "the zero-escape collapse, the named open sub-item", read: struck
as a conjecture; survives only as fixture theorems.

## Addendum 3 (2026-08-03, ratified): item 12' is the heart's form of record

The re-pose was ratified and applied: item 12' (the iterated-core
escape form) is now the occupancy heart's hypothesis OF RECORD in
`critical/nodes/xr_graded_tangent_band_charge` (statement + dag text
synced). Item 12's one-step form survives as a sufficient special
case. Open channels of record: V >= 5 zero-escape below the Cor-3b
threshold; escape-1 core rays.

## Addendum 4 (2026-08-03): channel (i) DECIDED

For the block class of record (the clique model forces disjoint
blocks): charge >= 2 holds iff 2V <= 3h (proved both directions;
floor rank >= 3h tight, ceiling 2m V-independent). At the prize rows
this holds by ~1e8 — channel (i) of item 12' is CLOSED at the prize
rows. The banked k <= 2h^2 criterion is refuted (see support-4
addendum 3). Remaining open channel of item 12': escape-1 only
(V >= 6 overlapping-block generality also open, but outside the model
of record).

## Addendum 5 (2026-08-03): channel (ii) resolved; the charge route re-scoped

Escape-1 gate-clean core rays EXIST (unification flag 5 affirmative;
E1 family, all-escape-1, V >= 3h forced). Protections proved: the
3-DROP FLOOR (rank >= sum_{a not in K} h + sum_K esc_a + G3, G3 the
best 3-subset drop — dominates the kernel floor, tight on the
U-mechanism); charge defeat needs n_1 >= 3h-2 low-escape core rays;
LEMMA R: rank <= 2m-1 is NECESSARY for band admissibility (rank = 2m
kills exact-A liveness); every escape-1 counterexample found is
band-inadmissible. CROSS-CHANNEL CATCH: the zero-escape pencil family
at V=11 (Zfib11) passes the FULL band gate, realises with exact-A
agreements, and has charge 0.818 — the per-ray-charge-2 route is
FALSE for full-gate admissible systems in general; it survives at
prize-row parameters because every known defeat class needs 2V > 3h
or n_1 >= 3h-2, both astronomically false there. The occupancy
lemma's conclusion and the column bound are untouched (Zfib11's own
ledger: N_d = 0.11 n^2). Heart status: route through admissibility +
row arithmetic; open = consolidating the general-V admissible case at
prize rows.

## Addendum 6 (2026-08-03): exact Route-T budget interface

The campaign phrase "the `13n^3` headroom" denotes the floored lower
bound on the free third-column budget. It is not an upper bound. The
critical-DAG interface is

```text
H_band(C) := s_lo(C)-16n^3,
|Gamma_band| <= H_band(C),
```

so the band column and the `16n^3` post-band remainder total at most
`s_lo(C)` exactly. At the three prize rows `H_band/n^3` is about
`13.857`; replacing it by either `4n^3` or a literal upper bound of
`13n^3` breaks the ratified `17/25` occupancy arithmetic. The exact
integer check lives in `critical/nodes/xr_graded_tangent_band_charge/
verify.py` and includes the separately capped cascade tier.

## Addendum 7 (2026-08-03): window locators use maximal selected currency

For depth `d`, the two top-coefficient window systems parametrize raw
`(k+d)` interpolation sets, not automatically the maximal pairs counted
by `N_d`. If `MAX_e` counts full joint cores of depth `e`, then

```text
RAW_d = sum_{e>=d} MAX_e binom(k+e,k+d).
```

Therefore every window-divisor count consumed by the band lane must
require: (i) the reconstructed pair's full core is exactly `H\T`, and
(ii) that pair has `L_P>=2` under the support-wise first-match selector.
Single-word Toeplitz rank `d` also does not imply stacked joint
codimension `2d`. The corrected residual of record is
`xr_band_maximal_window_divisor_count`.

13. **official row** is AMBIGUOUS in-repo and must never be used bare
    in a new statement. Write either "admissible row" (the descriptor
    family — q = p^e, n = 2^s, k = rho*n under q < 2^256, k <= 2^40,
    n | q-1; s free) or "maximal row" (s pinned; state the pin).
    Existing bare uses are read at their node-local pin; the dli_wcl_*
    family's parenthetical "(q < 2^256, v_2(q-1) >= 41)" IS an s = 41
    pin and does not cover s < 41. Two maximal-row conventions coexist
    (Convention A: N = 2^41, K = rho*N; Convention B: n = 2^41..2^44,
    k = 2^40) — they agree only at rate 1/2. **ADJUDICATED 2026-08-10
    (user-delegated coordinator ruling): "maximal row" = CONVENTION B**,
    the cap-saturating rows, per the primary source: the ABF26 page-5
    grand-challenge box fixes rate rho in {1/2, 1/4, 1/8, 1/16} with
    k <= 2^40, so the maximal admissible row per rate is k = 2^40,
    n = 2^40/rho in {2^41..2^44} — exactly Convention B, and exactly
    the cp-packet/petal_g3 usage. Convention A's rows at rates < 1/2
    (K = rho*2^41, i.e. k = 2^37..2^39) are ADMISSIBLE BUT NOT MAXIMAL
    and must be called "rate-scaled N=2^41 rows"; the three A-statements
    (x4_primitive_star_u1_coverage, b2b_near_tail_bound,
    u2c_exact_slice_extras_budget) keep their content under the
    node-local-pin reading rule — their claims are about the rows they
    define — but their row vocabulary is read per this ruling. Nothing
    at rate 1/2 changes.

14. **The ABF26 "sufficiently large |F|" proviso is RESOLVED NEGATIVE**
    (2026-08-10, primary source read): abf26 = Arnon-Boneh-Fenzi,
    "Open Problems in List Decoding and Correlated Agreement"
    (2026-04-08). The page-5 box reads "assuming |F| is sufficiently
    large so that such a delta*_C exists" — a FIELD-SIZE
    well-definedness clause (epsilon_mca has 1/|F| scaling, so
    epsilon* = 2^-128 needs a large field), NOT a row-size exclusion.
    Small-k rows make the clause EASIER, not excluded. With "for every
    choice of F, L, and k" and "mostly interested in ... k <= 2^40,
    and |F| < 2^256" (a cap over the family), the k_extremal HOLE
    STANDS: the rate-half grand-challenge family is the 41 row sizes,
    and no Przemek/rules question is needed. Version note: the
    vendored rs-mca open-proximity.pdf read for this ruling hashes
    e543ec6a...81de3, while official_row_primes_reframe.json pins
    426a979c...caa5 — version drift; all four pinned fragments were
    re-verified VERBATIM on page 5 of the version read.

15. **POSE 3 ADOPTED (2026-08-10, user-delegated coordinator ruling):
    the rate-half lane's official pose is the PER-S FOUR-BAND FAMILY**
    (n = 2^s, k = 2^(s-1), s = 1..41), with s = 41 the flagship
    instance. All existing s = 41 results keep their pins unchanged;
    POSE 1's elementary corridor covers the list side at s <= 7 above
    its per-s thresholds (pending referee); the s = 8..40 interior is
    open family territory and every new band statement must declare
    its s-scope explicitly. Node-level retrofit of the four
    crossing/floor nodes rides the next mint wave; until then this
    item plus the node-local scope flags (k_extremal FLAGs A-D) are
    the reading of record.

16. **The e-axis (2026-08-10, F4 RULING EXECUTED: WIDEN).** The
    RH-AC pose is q = p^e, e in {1..6} exactly (the stratum lemma on
    rate_half_residual_prime_field_collapse's round-31 addendum);
    "q prime" was PROVED only on the residual-budget sliver
    [2^167, 2^167+2^129) (RPFC) and was an unstated assumption
    elsewhere. The RPFC contrapositive keeps every extension row out
    of the prime-field machinery's territory. Standing rules: any
    future far-CA UPPER bound must not assume "no proper subfield"
    (O6); the prime-only evidence base is flagged for extension
    re-runs (O7). Full grounds: the rh_e_axis_audit REPORT +
    the e-axis widening block on the crossing pose.
