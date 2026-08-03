# The OVERLAP SLIVER — pilot report (2026-08-03, Opus 5)

(Coordinator-persisted; write harness-blocked. Replay: ramguard tiny
-> 33 checks, 0 FAIL; OS1-OS8/P1-P5 pre-registered.)

## VERDICT: V <= n/2 REFUTED for the sliver's shape class; the sliver
CLOSES at V <= |U| <= n (c = 1), and |U|/n <= 0.2588 at all six rows
recovers V <= 0.26n < n/2 at every actual row.

Proved chain: LEMMA O1 (triple corollary w_ab + w_ac <= e-1 —
subsumes banked D2 and D3 in one line); LEMMA O2 (at fixed band depth
every overlap equals lam = t-h+d: the complements form a constant-lam
design; t-lam = h-d >= 2); THEOREM O3 (zero escape empties the
sunflower branch); THEOREM O4 (FISHER: G = (t-lam)I + lam J
nonsingular => V <= |W| <= |U| <= n — needs only constant lam + the
depth gate; SHARP at PG(2,3), V = |U| = 13, and PG(2,5), V = 31);
THEOREM O5 (Deza 1974: V <= t^2-t+1 in the non-sunflower branch =>
V <= |U|/2 whenever k+h >= 2t^2-3t+2 — fires at the RowC rows, not
the prize rows).

REFUTATION witness (hard-coded, machine-audited): V = 6, |U| = 11,
t = 4, h = 4, k = 3, every gate tight, V > |U|/2. 47 overlapping
gate-clean systems found, 31 with V > |U|/2, all in the lam >= 1
non-sunflower branch.

CONJECTURE OV (open, strongly supported): overlapping gate-clean
zero-escape => Ann = 0 (collapse). Exhaustive pruned slope sweeps:
PG(2,3) 39.9M-2.96e12 tuples across q = 13/17/19, 5 small shapes
1.53M tuples — 0 non-collapsing. If OV holds, admissible => disjoint
=> V <= |U|/2 outright.

L-B residual: COVERED at V <= |U| unchanged (O4 needs no zero
escape); in the sunflower branch V <= |U|/2 anyway (H2); the
non-sunflower V <= |U|/2 gap is the same PG-type obstruction.

Rows: |U|/n = 0.2588/0.1338/0.0674 (RowC), 0.2578/0.1328/0.0664
(prize) — the n/2 consumer met at every recorded row.

FLAGS: F1 status change (UPDATE 3 item 2 as literally stated FALSE;
sharp bound V <= |U|); F2 Deza classical (optional sharpening only;
the close is self-contained); F3 uniform-depth hypothesis (varying
depth MEASURED to obey V <= |W|, 2 systems); F4 OV open (toy q <= 23);
F5 finite slopes; F6 one bare-python file-surgery slip self-reported
(no computation of record); F7 novelty subtraction done; F8 does not
touch the primary surface.
