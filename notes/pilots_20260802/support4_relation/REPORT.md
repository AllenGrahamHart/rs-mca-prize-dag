# Pilot report: the support-4 relation (Opus 5, 2026-08-02)

Coordinator note: condensed persistence (full detail in the stage
JSONs); audit in FABLE_AUDIT.md. stage3 (30/30) + stage6 replayed
(the one FAIL = the reported RowC 1/4 finding, N_1 = 510 vs 384).

## VERDICT: K3 REFUTED — admissible support-4 relations EXIST; K2
FIRES quantified — the mechanism is completely classified, deficit
<= 1/ray, and the prize-row ceilings are UNCHANGED (bit-exact).

**THE U-MECHANISM (the construction, 6/6 full-gate fixtures, deficit
exactly 1)**: |U| = k+2 (dim C_U = 2), distinct holes y_a in U,
S_a = (U \ {y_a}) u P_a with (h-1)-paddings pairwise meeting in d and
no triple point. Every pair is a depth-d datum; every triple
intersection is EXACTLY k-1 — the k-packing gate is SATURATED, not
violated; the relation's four duals are the minimum-weight e_{y_a}
(weight exactly k+1). An extremal object sitting exactly ON the gate
— which is why the banked builders never hit it.

**COMPLETE STRUCTURE THEORY (proved + verified)**: S4-1 localisation
(every relation lives on the TRIPLE LOCUS); S4-2 general position
kills (empty triples => no relation; COROLLARY: the banked K_V family
provably carries NO relation — upgrading the banked measurement to a
theorem: its triple locus is Y, size k-1 < k+1); S4-3 rank-2 rigidity
(all four duals in ONE 2-dim L; proportional pairs => k-packing
break); **S4-4 THE MOBIUS CRITERION — a complete characterisation:
the relation exists iff CR(z_1..z_4) = CR(zeta_1..zeta_4)** (cross-
ratio of slopes = cross-ratio of the four dual classes in P(L);
unique up to scalar); S4-5/6 the pencil picture (minimal case:
zeta_y = x_y — slopes must match the HOLES' evaluation points);
S4-13 depth budget (uniform depth needs h >= 3d+1; ray cap
min(k+2, (h-1)/d + 1)); S4-10 no stacking (deficit <= 1/ray);
**S4-14 CONNECTIVITY FLOOR (new, unconditional): rank >= m :=
|union S| - k, so charge/ray in [m/V, (2m-1)/V] — occupancy holds
AUTOMATICALLY whenever V <= m/2**; S4-15 iterated
localisation/escape floor (rank >= sum min(h, |S_a \ S_a^inf|);
a mis-coded first version produced a false floor, caught and fixed).

**Gate-failure taxonomy (1800 random systems)**: the banked
"unconstrained relations" are overwhelmingly k-packing breaks
(support-3 in disguise); 1/600 came through gate-clean — the class
is designable, not accidental. The double-hole generalisation
(|U| = k+2l, l >= 2): relations exist for EVERY slope tuple (no
cross-ratio condition), dimension exactly Vl - 2(D+1), charge
>= V(h-l) — measured 7.3-10.6/ray.

**AMPLIFICATION — capped**: cluster deficit = V-3 exactly (rank =
V(h-1)+3, charge/ray -> h-1); the mechanism BEATS K_V per datum at
toy scale (up to 1.82x) where the ray cap binds; **the escape/
collapse dichotomy caps everything: zero-escape families have rank =
2m EXACTLY (the T3 collapse — a single band pair, no family;
exhaustive over 3876 + 8855 slope tuples, never 2m-1); escape >= 2
=> charge >= 2**. Every non-collapsing family observed satisfies
V <= m/2.

**RE-PRICING — prize rows UNCHANGED**: N_1 = 18,336/24,976/114,960
IDENTICAL to the banked K_V numbers (ratio 1.000000 — the point
budget binds first; the deficit V-3 is a relative 1e-10). The
ratified 0.68n^2, the 13n^3 column, SHARP-OCC weak form ALL survive.
**Toy-row finding: at RowC 1/4 the U-mechanism beats K_V by 1.33x
(N_1 = 510 vs 384) — against n/2 = 512, SHARP-OCC's weak form
survives by A MARGIN OF 2, the tightest that law has ever been
measured.** Secondary: the zero-escape channel can only reach charge
< 2 when k > 2h^2 — margins 2.7e8-5.4e8 at the prize rows; at the
RowC toy rows k > 2h^2 holds and THE COLLAPSE THEOREM is the
load-bearing kill there (honest limitation of the arithmetic route).

**THE RESIDUAL, RESTATED TWO LEVELS DOWN**: was "support-4 relations
exist?" (SETTLED: yes); now — **"an admissible, non-collapsing,
pairwise-intersecting ray system with V > m/2"** (= per-ray charge
< 2 = the occupancy lemma's failure). Equivalently, in pure
combinatorics with NO algebra left: **"every ray support has >= 2
points lying in at most two supports" => the occupancy lemma is
PROVED.** Open sub-items: prove the zero-escape collapse (rank = 2m
always — the toy rows' load-bearing kill), prove V <= m/2 for
non-collapsing systems (conjecture; all 9 families conform; Fisher
gives only V <= k+m).

**Caveats**: toy scale n <= 29 for full-gate fixtures (prize figures
= exact budget formulas); collapse measured not proved; V <= m/2
conjectural; non-minimal pencils D >= 2 argued-not-swept optimal at
D = 1; the double-hole family's realised gates untested at priv = 0
(it collapses) and above scan budget otherwise; support-<=3 lemmas
relied on as banked. Tally: 301 checks + 4 measurements; 9 FAIL
lines all deliberate/findings.
