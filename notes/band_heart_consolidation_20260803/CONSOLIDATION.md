# Band-heart consolidation at the prize rows (coordinator, 2026-08-03)

Ratified analysis. Inputs: the four round-7/8 floors (kernel, 3-drop,
2V <= 3h trichotomy, LEMMA R), banked L2 (realised rank <= 2R-1),
per-ray accounting (definitions item 11), the ledger definitions
(items 7-9), and the six recorded rows
(`notes/pilots_20260802/support4_relation/stage5_escape.json`).
Arithmetic machine-checked: `verify.py` here (ramguard tiny, PASS).

## Verdict

**NOT closed by the floors — and provably not closable through the
ray/charge lens at all.** The consolidation's real output is (a) a
small new proved lemma, (b) a machine-checked negative finding that
retires the charge route as the primary attack, and (c) the exact
named open surface, with the recommended route now the CORE COUNT.

## 1. What the floors DO give (proved, per admissible live system)

Let the live-slope system at a row have V rays (item 7: one selected
support per live slope), core decomposition V = V_dead + V_0 + V_1 +
V_{2+} (by (3,k+1)-core membership and escape). LEMMA R + banked L2:
rank <= 2m - 1 <= 2R - 1. The 3-drop floor then bounds:

  V_dead <= (2R-1)/h        (307..959 across the six rows — negligible)
  V_1 + 2 V_{2+} <= 2R-1    (each escaping core ray pays its escape)

V_0 (zero-escape core rays) is bounded by NO current floor — this is
the Zfib11/pencil class, now known to be full-gate admissible.

## 2. CORE-DISJOINTNESS LEMMA (new, small, proved here)

Under (T), the depth-d cores (the joint agreement sets Z_P, |Z_P| =
k+d >= k+1) of DISTINCT pairs pairwise share <= k-1 points.
*Proof.* Two pairs sharing a ray: Z_ab ^ Z_ac <= S_a^S_b^S_c <= k-1
by (T). Disjoint pairs: Z_ab ^ Z_ce <= S_a^S_b^S_c, likewise. QED
Moreover each core of size >= k+1 forces the KEY-LEMMA
joint-explanation event A(Z) = B(Z) = 0 (banked
xr_band_key_lemma_pencil_mass: a shared agreement set of size > k
forces top-coefficient vanishing). So **N_d counts joint-explanation
(k+d)-sets of one received pair, pairwise <= k-1**.

## 3. The negative finding (machine-checked)

Even granting BOTH candidate ray-side lemmas —
  L-A (pencil rigidity, e >= 2): zero-escape admissible sub-families
      are disjoint-block pencil systems, so V_0 <= n/2 (proved today
      only at e = 1, THEOREM C'; e >= 2 measured);
  L-B (escape-1 over-agreement): escape-1 core rays are never the
      selected exact-A ray, so V_1 = 0 (E1P evidence, 520 samples) —
the pair-graph bound N_d <= C(V,2) yields 0.78 n^2 (prize 1/4) to
2.12 n^2 (RowC 1/16): **ABOVE the 0.68 n^2 budget at every row**.
The charge/ray lens cannot close the occupancy lemma even with both
open lemmas granted. (This retires the ray route as primary — the
same conclusion the Zfib11 catch pointed to, now quantified.)

## 4. The recommended route: count CORES, not rays

The right object (section 2) is the set of depth-d joint-explanation
cores of the received pair (u,v): (k+d)-sets Z with A(Z) = B(Z) = 0 —
2d linear conditions in the top-coefficient space of the banked KEY
LEMMA — pairwise <= k-1, each carrying its banked member cap
L_P <= floor((n-J)/(A-J)). The occupancy lemma IS the statement that
one pencil admits <= 0.68 n^2 such cores per depth. Calibration: the
sharpest recorded adversary (U-mechanism, RowC 1/4) achieves
N_1 = 510 ~ n/2 — a factor > 1000 UNDER the budget (verify.py check
3). SHARP-OCC (conjectured, ~n/2) is the same object counted
optimally; the budget needs only n^2-level counting — the slack
between n/2 (measured) and 0.68 n^2 (needed) is the attack surface.

**L-D (the consolidated open statement):** for every admissible
received pair at the six rows and every band depth d, the number of
depth-d joint-explanation cores with L_P >= 2 selected is <= 0.68 n^2.
L-D subsumes L-A and L-B (they become irrelevant if it is proved
directly) and consumes only banked machinery (KEY LEMMA top
coefficients + core-disjointness + the L_P cap).

## 5. The open surface after consolidation (exactly three items)

1. **L-D** — the core count (primary; algebraic; dimension-count over
   pairwise-(<= k-1) (k+d)-sets with 2d vanishing conditions).
2. **L-A** — pencil rigidity at e >= 2 (fallback ray route,
   also independently valuable for the zero-escape story).
3. **L-B** — escape-1 over-agreement (fallback; sharp open question
   already flagged by the escape-1 pilot, with its named mechanism).

Everything else about the heart at the prize rows is PROVED: dead
rays, escaping core rays, the block class, the trichotomy, the
admissibility filter, and the refuted routes are all closed chapters.

## Flags

- The pair-graph negative finding assumes the worst-case pair density
  C(V,2); a finer per-depth pair count was NOT attempted (the
  core-count route makes it moot).
- L-D's 0.68 n^2 budget is the TARGET's recorded sufficient bound;
  SHARP-OCC would give ~n/2 but is NOT needed.
- No node status changed by this note; the TARGET's single open input
  is unchanged in substance — it is now NAMED (L-D) with two named
  fallbacks, and the primary lens is corrected from charge to cores.

## CORRECTION (2026-08-03, same day — L-D pilot, coordinator-accepted)

The L-D pilot REFUTED section 4's wording and terminated its route:
1. "(k+d)-sets Z with A(Z)=B(Z)=0" is FALSE as a <= 0.68n^2 claim
   (raw subsets of one deep joint agreement set explode: RAW_d =
   SUM_{e>=d} MAX_e C(k+e,k+d); machine-verified fixture 334 > 272;
   prize rows by 2^6.4e10). CORRECT object: codeword pairs whose
   joint agreement set has size EXACTLY k+d (maximal) — which IS the
   ledger's N_d.
2. Section 2's final sentence over-reached: pairwise <= k-1 holds for
   the MAXIMAL cores of DISTINCT pairs, not for raw subsets.
3. The "count CORES" route was ALREADY BANKED AND TERMINATED in
   notes/pilots_20260802/xr_band_occupancy/ (THEOREM 2: N_d <= min_z
   punctured-MDS list size at agreement k+d; THEOREM 4; PROPOSITION 5:
   the slope side CANNOT close — needs |Gamma_band| <= 1.32n^2). This
   note failed to subtract against it (fifth-surface rule).
4. The 0.68n^2 budget is VACUOUS at the three RowC rows; the
   obligation binds at the PRIZE rows only.
SURVIVES from this note: the negative finding (ray/pair lens
insufficient — sharpened by the pilot to V* = 1.166n, factor 1.072
above the granted-both-lemmas bound) and the L-A/L-B statements as
independent lemmas. THE OPEN SURFACE OF RECORD (corrected): the
banked xr_band_occupancy terminus — an RS list-size bound at
tau = k + ceil(h/2) for some pencil member (positive target #1
species) — with L-A/L-B as supporting, provably-insufficient-alone
lemmas.

## UPDATE 2 (2026-08-03, L-B pilot): L-A => L-B — the surface simplifies

L-B's conclusion (V_1 = 0) is PROVED on the group-fibre/pencil-block
class (THEOREM F pins realisers by any 3 fibre rays; the E1P
phenomenon is now a theorem); its MECHANISM is refuted as stated
(over-agreement is forced only for PRIVATE escaped points — LB-F2,
five fixtures); the general case is an exact DICHOTOMY (forced point
exists iff L-B holds at the ray), and the residual open configuration
is precisely L-A's subject. OPEN SURFACE OF RECORD (final form of
this note): the xr_band_occupancy RS list-size terminus (primary) +
L-A (pencil rigidity at e >= 2, which now also carries L-B).

## UPDATE 3 (2026-08-03, L-A pilot — FINAL surface of this note)

L-A as stated in section 5.2 is REFUTED (V = 4 non-pencil zero-escape
non-collapsing fixtures W1/W2 at e = 2, 3); repaired L-A' holds at
V >= 5 up to one block modulo the named residual (1 <= dim G < e,
Z != empty). The consumer V_0 <= n/2 is PROVED without the pencil at
V = 4 (disjointness forced), e <= 2 (matching bound), t = 2, and all
disjoint systems. FINAL OPEN SURFACE OF RECORD for the occupancy
heart: (1) the xr_band_occupancy RS list-size terminus at
tau = k + ceil(h/2) (primary; codeword-pair side; positive target #1
species); (2) the OVERLAP SLIVER — overlapping zero-escape block
systems at e >= 3, V >= 5 (carries the L-B residual via L-A => L-B).

## UPDATE 4 (2026-08-03, list-size pilot — ADJUDICATION CORRECTION)

UPDATE 3's item (1) named a terminus REFUTED the previous day
(list_bound_transfer R1+R2; the KEY LEMMA node's non-claim; the
xr_band_occupancy amendment) — the subtraction failure repeated.
CORRECTED FINAL SURFACE: (1) the un-reduced two-slope band occupancy
at band-proper high depths [ceil(h/2), h-2] — repair route SL-1
(windowed projection <= A-2, same species as L-B over-agreement,
toy-testable), Pro-brief candidate SL-2 (unstructured high-window
exclusion; structured half proved by BP(1)/BP(3), which protect the
lemma by exactly one depth and REQUIRE h odd); (2) the OVERLAP SLIVER
(unchanged). The min-over-members freedom is dead (SHADOW LEMMA: worth
256 bits against ~1e12); "positive target #1 species" struck.
