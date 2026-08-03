# Coordinator audit — V >= 5 zero-escape occupancy pilot

**Auditor:** Fable, 2026-08-03. **Verdict: BANKED — channel (i) DECIDED
with the exact boundary 2V <= 3h; one more banked criterion refuted.**

## Replay + hand-verification

Replay: 67 checks, 0 FAIL (coordinator). PREREG confirmed (Q1-Q12
registered before computation, all as registered). Hand-verified line
by line: the class arithmetic (m = |U| - k = t + h, V-INDEPENDENT —
the pivotal identity; e = k - sigma = 2t - h; pairwise = k + (h-t);
gate <=> e >= 1; zero escape automatic at V >= 4); LEMMA 1's
normalisation (P, Q degree < k, uniqueness from |S_a| > k); THEOREM
B's embedding (nu determined by p_3; p_3 vanishes on the sigma points
of S_3\(A_1 u A_2); dim <= (k - sigma)^+ = e; hence rank >= 3h);
THEOREM A (rank <= 2m trivially, m V-independent, so charge >= 2
forces V <= m); the trichotomy's two unconditional regimes; Y1's full
arithmetic (V=5, rank 9 = 3h < 10 = 2V, charge 1.8); the RowC shape
identification (t = h - d: (5,1) gives t=4, t_0=1, m=9, e=3,
sigma=253 — matching the recorded misses-by-3). All correct.

## The refutation of k <= 2h^2 (F1) — ACCEPTED

The banked secondary criterion computed charge as 2m/Vmax, a CEILING;
an upper bound cannot certify charge >= 2. Y1 is the record's own
clique shape at (5,3,1) with k <= 2h^2 satisfied and true charge
1.8 < 2. The corrected criterion 2V <= 3h rests on the new proved
floor. At the PRIZE rows 2V <= 3h holds by ~1e8 — no prize-row number
moves; only the justification is replaced (and is now proved, where
the old one was a mislabeled heuristic). Addendum applied to the
support-4 node (addendum 3) and the definitions file.

## Flag adjudication

F1 applied as addenda (below). F2: task #33 RESOLVED as "cannot
succeed as posed" — the RowC toy-row kill is unrestorable by any
shape-only argument (Y5/Y6 share every recorded invariant and differ
in rank); the trail marker stays OPEN, and the PRIZE rows do not need
it (they rest on the 2V <= 3h floor). F3 scope honest (block systems;
the record's clique model provably forces disjoint blocks, so the
model of record IS covered; general V >= 6 overlap OPEN). F4/F9
measured-only items correctly labeled. F5 realisability inherited
(compute request stands). F6 novelty subtraction done by the pilot
itself (THEOREM A = concordance). F7/F8 clean.

## What this changes

- Channel (i) of the re-posed heart is DECIDED: charge >= 2 iff
  2V <= 3h (block systems; V=5 general bound m <= 3h-4 besides). At
  the prize rows the channel CLOSES (margin ~1e8, on a proved floor).
  At the RowC toy rows it genuinely FAILS (ceiling charge < 1) — the
  toy rows are dead for the arithmetic route, now provably.
- The collapse is dead at EVERY V >= 4 (exact locus: pencil fibres +
  Mobius equivalence, dim Ann = 2t - h).
- The heart's sole remaining open channel is ESCAPE-1 (pilot running).
