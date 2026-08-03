# L-A (pencil rigidity at e >= 2) — pilot report (2026-08-03)

(Persisted by the coordinator; REPORT.md write harness-blocked.
Pilot: Opus 5. Replay: ramguard tiny -> 30 checks, 0 FAIL; PREREG
falsifiers FA-FE + dimension prediction P pre-dated.)

## VERDICT: REFUTED as stated; PARTIAL (repaired); consumer PROVED without it

FA fired: THEOREM C' does NOT extend verbatim — gate-clean zero-escape
non-collapsing NON-PENCIL systems exist at V = 4 for every e >= 2.
Repair: rigidity holds at V >= 5 up to one block. And the consumer
(V_0 <= n/2) needs NO pencil at all at e <= 2.

## Proved content

LEMMA R (reduction): dim Ann = dim {w : T_a w in E for all a >= 3}
(the nu-parametrisation as a rank formula; 7/7 cross-checked against
banked ann_dim/rank_row). THEOREM 1: every g_a != 0. THEOREM 2 (the
e >= 2 resultant trick): B_b g_a in M := B_1 F[X]_{<e} + B_2 F[X]_{<e}
for all pairs. THEOREM 3 (spanning => pencil): dim G_b = e forces
B_b in <B_1, B_2> (iterated X-shift argument). COROLLARY: C' in one
line at e = 1 (constants: dim G_b = 1 = e automatically) — isolating
the exact breakage: at e >= 2, G_b may be proper. THEOREM 5
(dim G = 1 branch): all blocks b >= 3 are fibres of ONE pencil; A_1,
A_2 join iff their zero-sets Z_i of g are empty (automatic at e = 1).
The ONLY escapes from the pencil: Z != empty, or 1 < dim G < e.

## Counterexamples (audited by banked code, independent of the reduction)

W1 (e=2, q=13, k=5, V=4, t=3, h=4): dim Ann = 1, rank = 13 = 2m-1,
span{B_a} = 3 (NOT a pencil); the Z-escape (g = 2X+4, Z = {11}).
W2 (e=3, q=23, k=7, V=4, t=4, h=5): dim Ann = 1, rank = 2m-1,
span = 4; dim G = 2 escape (refuting the pilot's own pre-registered
fallback — recorded, not retro-fitted). 34 + 20 audited non-pencil
witnesses. V = 4 is exactly the no-content regime for THEOREM 3.

## V >= 5 (L-A', proposed)

At V >= 5, dim G = e forces >= V-1 blocks into <B_1,B_2> (THEOREM 3);
dim G = 1 puts A_3..A_V on one pencil (THEOREM 5). No V >= 5
counterexample in any search (700 + 310 partitions, all slope tuples
mod affine; exhaustive extension route positively controlled 3/3).
RESIDUAL OPEN: 1 <= dim G < e with Z != empty at V >= 5.

## The consumer V_0 <= n/2 survives WITHOUT the pencil

LEMMA D1: at V = 4 zero escape forces DISJOINT complements (each
point in <= V-3 = 1). LEMMA D2: overlaps <= min(e-1, t-2) — e = 1 or
t = 2 forces disjointness outright. LEMMA D3: at e = 2 the overlap
graph is a matching, V <= |U|/(t - 1/2) < |U|/2. So V_0 <= n/2 is
PROVED at V = 4, at e <= 2, at t = 2, and for all disjoint systems
(point count). OPEN sliver: overlapping systems at e >= 3, V >= 5
(F5; RowC has e = 3 but is budget-vacuous per the L-D pilot; the
prize-row block shapes have e = h-2d — large — so the sliver is the
genuine remaining ray-side obligation).

## Flags

F1 L-A as in CONSOLIDATION.md 5.2 FALSE (W1/W2); consumer unaffected;
nothing edited outside the pilot dir. F2 pre-registration honesty
(second branch found; both tested separately). F3 V >= 5 residual not
closed; searches thin at (4,3). F4 prediction P's converse refuted at
(5,3,4) — THEOREM 3 is the right predictor, not the naive dimension
count. F5 e >= 3 overlap count OPEN. F6 toy fields q <= 41,
combinatorial gates only. F7 novelty subtraction done (THEOREM 2 = C'
trick generalized; LEMMA R = v5 nu-parametrisation as formula; NEW =
THEOREMS 3/5, W1/W2, D1-D3). F8 compute law kept (tiny, 15.6 s).
