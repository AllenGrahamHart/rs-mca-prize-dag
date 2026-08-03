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
