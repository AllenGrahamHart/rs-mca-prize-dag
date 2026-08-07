# FABLE_AUDIT — ge_floor_falsifier (round 22, agent 2 of 4 to report)

**Auditor:** Fable, 2026-08-07. **Verdict: BANKED, MAINTAINER-LEVEL —
the falsifier search did its job in the strongest possible way:
FLOOR-GE survives AS STATED (its own registered falsifier exhausted
empty at N' = 8, 16, independent implementation), while the
ROUTE-BLOCKING use of it is killed by an exhaustive witness
(L_2(8) = 17 = 2N'+1 > N'+1, two odd prime ideals above 3, witness
{0} u {+-1}^4) — and the replacement floor PRICE-GE is measured AT
the prize cell rather than extrapolated: 1.83 falling to 0.84
centers per odd prime ideal at N' = 128, cost quadratic in orbit
count, an 82-163-bit ceiling against poly(N') that no longer
depends on the norm-class restriction. Mystery 5's (a)-route is
now dead norm-class-free. AND the (b)-route repricing is a genuine
strategy event: per-row GE-WEAK certification at N' = 128 is a
dim-64 radius-16 lattice enumeration at 2^27.4 nodes — ~20 orders
below the pricing of record.**

Replay: selftest.py SELFTEST PASS (tower norm vs independent
Bareiss determinant, full box h = 2, 4 + 300 random h = 8);
d1_small.py 4 5 — the escape curve 9/9/17/17/17/17 EXACT;
d3_kernel.py — the threshold tables and split-model crossover
exact; d4_cone.py — the C-4 anchor replay (0 witnesses at radius
6), the full-radius 6 witnesses at the SAME prime, the TIGHTEMPTY
boundary witnesses (Norm = p exactly), and both certified-empty
cells reproduced. REPORT.md persisted verbatim (task
aa5edfd7cba37294d).

ADOPTED (four node addenda + one superseded note, all
merge-safety-checked against the staged wave-48 tree — the four
files are byte-identical between master and v12, so my addenda are
the only diverging side):
- generator_economy: the two-verdict split + PRICE-GE (with its
  pre-registered falsifier) + the prize-cell price.
- kernel_lattice_reframing: CATCH-1 forced correction — the
  ~2^-50 expected-hits figure is multiplicity-inflated by 54.3
  bits (existence heuristic 2^-101.4; distinct folded classes
  5^64); same defect class as round-21's collision catch; SAFER
  direction.
- lattice_cone_certificate: the C-4 anchor generalized from a
  pinned prime to the congruence class p = 1 mod 16 above 4049
  (radius 6) / 463249 (full radius, attained); the SCOPE CATCH
  (the same anchor prime has 6 witnesses at full radius —
  consumers must respect the radius scope); the ~20-order per-row
  pricing correction with the fplll production spec; the N' = 256
  "do not attempt" CONFIRMED (R/lambda1 = 2.135).
- integer_code_distance_cert: the universal toy thresholds; the
  norm-instrument family ruled out of reach of prize rows for a
  structural reason; the node confirmed as the convergence point
  of THREE lanes.
- gen_economy_diag/REPOSE_DRAFT.md D4 section marked superseded
  (coordinator note in that dir).

SUBTRACTION DISCIPLINE — the round's model: the pilot arrived at
lambda1 > 16 independently, then FOUND THE PRIOR ART ITSELF
(PRO_W3, banked) and claimed only the pricing; it also caught that
PRO_W3's "do not attempt" is about N' = 256/dim 128 (where it is
right) not the prize cell N' = 128/dim 64 (where enumeration is
cheap) — a scope distinction that unlocks real work.

HONEST LEDGER accepted: H3, H4, H5 all FALSIFIED as registered and
reported plainly (one odd ideal buys nothing — a STRONGER floor
than predicted; the norm base pattern fails at h = 2 and is
unconfirmed at h = 16; TIGHTEMPTY hugs MAXNORM). Two runs died on
the ramguard wall with NO verdict and are reported as such
(L_1(16) exhaustive only over top-3 ideals; L_2(16) unmeasured).
The pilot's first cost functional was 5x loose, published, then
CAUGHT BY ITS OWN cross-check and superseded with headers — the
correction chain is in the artifacts. Rule brush (two environment
probes) disclosed in the PREREG. Quarantine held absolutely; no
subagents dispatched.

BOARD EFFECT (mystery 5): the (a)-construction route is dead
without the norm-class caveat; the (b)-route is repriced from
Modal-scale to laptop-scale PER ROW; the mystery's hard core is
now cleanly "universality over an unbounded row set" — exactly
integer_code_distance_cert, the three-lane convergence instrument.
NEXT-MOVE CANDIDATE (queued for the round-22 wrap): implement the
dim-64 enumeration per the fplll spec (or a checkpointed stdlib
Fincke-Pohst under ramguard) and CERTIFY the pinned prize rows —
the first executable positive step mystery 5 has ever had.
