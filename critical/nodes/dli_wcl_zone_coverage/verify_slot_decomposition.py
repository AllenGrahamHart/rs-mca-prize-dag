#!/usr/bin/env python3
"""Slot-decomposition completeness certificate for WCL-ZONE.

Mechanizes the finite-slot theorem: from the pinned primitives (schedule-r2
tower, extended window, Newton short-window bound, the proved weight floors,
the zero-event threshold), enumerate ALL (ell, w) cells that survive and
assert the result is EXACTLY the minted slot set — ten open + two closed.
Installed 2026-07-22 after the two-sided conventions/seam audit (independent
primitives derivation agreed with the bookkeeping derivation; ground-truth
cross-check vs the (2,5)/(2,6) certificates: no mismatch).

Mutation controls prove the enumeration is sensitive to every primitive,
including the historically dangerous level-INDEX-vs-DIMENSION conflation
(catch #205).
"""
from fractions import Fraction

T = 2 ** 33                                # schedule r2 (maintainer decision 4c)
N_LEVELS = 34
THRESHOLD = Fraction(1, 32)                # WCL-ZONE per-level bound
WINDOW_LO, WINDOW_HI = 1, 7                # extended raw ledger [L+1, L+7], L = DIMENSION (C1'-r3)
AMBIENT_EXCLUDED = {(1, 3), (1, 4)}        # weight-3/4 ambient census theorems (both ell=1 levels)
CENSUS_CLOSED = {(2, 5), (2, 6)}           # norm-gcd (168 Pocklington) / recursive-norm (404,740)

OPEN_SLOTS = {(1, 5), (1, 6), (1, 7), (1, 8),
              (2, 7), (2, 8), (2, 9),
              (4, 9), (4, 10), (4, 11)}


def tower_dims():
    return [-(-(T // 2 ** j) // 2) for j in range(N_LEVELS)]


def newton_floor(ell):
    """Newton short-window theorem: reduced vanishers need w >= 2*ell + 1."""
    return 2 * ell + 1


def one_orbit_mass(ell, w):
    return Fraction(2 * 256 * ell, 2 ** w)


def enumerate_cells(dims=None, window_hi=WINDOW_HI, newton=newton_floor,
                    ambient=AMBIENT_EXCLUDED, threshold=THRESHOLD):
    live, closed, weighted = set(), set(), set()
    for ell in set(dims if dims is not None else tower_dims()):
        for w in range(ell + WINDOW_LO, ell + window_hi + 1):
            if w < newton(ell):
                continue
            if (ell, w) in ambient:
                continue
            if one_orbit_mass(ell, w) <= threshold:
                weighted.add((ell, w))
                continue
            (closed if (ell, w) in CENSUS_CLOSED else live).add((ell, w))
    return live, closed, weighted


def main():
    dims = tower_dims()
    assert sum(dims) == T and len(dims) == N_LEVELS
    assert dims.count(1) == 2, "both ell=1 terminal levels share the (1,w) cells"

    live, closed, weighted = enumerate_cells()
    assert weighted == set(), f"non-zero-event cells inside a window: {weighted}"
    assert closed == CENSUS_CLOSED
    assert live == OPEN_SLOTS, f"DECOMPOSITION MISMATCH: {sorted(live ^ OPEN_SLOTS)}"
    for ell, w in sorted(live):
        assert one_orbit_mass(ell, w) >= 32 * THRESHOLD, "unexpected thin margin"

    # dag wiring: every open slot req-wired into this node; statuses sane
    import json
    from pathlib import Path
    root = Path(__file__).resolve().parents[3]
    dag = json.loads((root / "dag.json").read_text())
    nodes = {n["id"]: n for n in dag["nodes"]}
    edges = {(e["from"], e["to"], e.get("kind")) for e in dag["edges"]}
    for ell, w in sorted(OPEN_SLOTS):
        nid = f"dli_wcl_slot_{ell}_{w}_emptiness"
        assert nodes[nid]["status"] in ("TARGET", "PROVED"), nid
        assert (nid, "dli_wcl_zone_coverage", "req") in edges, nid

    # ---- mutation controls (each corruption must move the list) ----
    caught = 0
    # M1: heavier threshold admits "weighted" cells -> completeness breaks
    l1, _, w1 = enumerate_cells(threshold=Fraction(3, 1))
    if w1 or l1 != OPEN_SLOTS:
        caught += 1
    # M2: window end +1 mints three phantom cells
    l2, _, _ = enumerate_cells(window_hi=WINDOW_HI + 1)
    if l2 - OPEN_SLOTS == {(1, 9), (2, 10), (4, 12)}:
        caught += 1
    # M3: strengthened Newton bound silently deletes (4,9)
    l3, _, _ = enumerate_cells(newton=lambda ell: 2 * ell + 2)
    if (4, 9) not in l3 and l3 != OPEN_SLOTS:
        caught += 1
    # M4: dropping the ambient theorems resurrects (1,3),(1,4)
    l4, _, _ = enumerate_cells(ambient=set())
    if l4 - OPEN_SLOTS == {(1, 3), (1, 4)}:
        caught += 1
    # M5: the catch-#205 conflation — windows keyed to level INDEX j+1
    idx_cells = set()
    for j, ell in enumerate(tower_dims()):
        L = j + 1
        for w in range(L + WINDOW_LO, L + WINDOW_HI + 1):
            if w >= newton_floor(ell) and (ell, w) not in AMBIENT_EXCLUDED \
               and one_orbit_mass(ell, w) > THRESHOLD:
                idx_cells.add((ell, w))
    if idx_cells != OPEN_SLOTS | CENSUS_CLOSED:
        caught += 1
    assert caught == 5, f"mutation controls caught {caught}/5"

    print("WCL_SLOT_DECOMPOSITION_COMPLETENESS_PASS "
          f"open={len(live)} closed={len(closed)} weighted=0 "
          f"min_margin=32x mutations=5/5")


if __name__ == "__main__":
    main()
