"""k3_chain_seams attack A5b: adversarial reproduction of (KBPRW-2/3/4),
the PROVED workboard that supplies the 13-route positive partition the
whole K3 chain is built on.

Source under test:
  background/nodes/rate_half_kb_m2_r4_coordinate_positive_residual_loop_workboard/
  statement.md:16-62  (status PROVED)

Two independent kill conditions:
  K1 — the six outside orbits (KBPRW-3) are NOT the complete solution set of
       (KBPRW-2) up to permuting D,E,F with sum l_i <= 1.
  K2 — the route table (KBPRW-4) is NOT reproduced by the stated rule
       "total defect <= 3, and a common loop forbids an outside loop".

If either fires, the 13-route count that complete_payment, the ledger, and
structural_surplus all quote is wrong at its root. Stdlib only, exhaustive.
"""

from itertools import product

# (KBPRW-1) live common skeletons: name -> ((l_A,l_B,l_C),(m_AB,m_AC,m_BC), defect)
COMMON_LIVE = {
    "442-0a": ((0, 0, 0), (3, 1, 1), 2),
    "442-1b": ((0, 1, 0), (2, 2, 0), 1),
    "433-0":  ((0, 0, 0), (2, 2, 1), 0),
    "433-1a": ((0, 0, 1), (3, 1, 0), 3),
    "433-1b": ((1, 0, 0), (1, 1, 2), 1),
}

# (KBPRW-3) claimed outside orbits: name -> ((r_D,r_E,r_F),(l_D,l_E,l_F),(m_DE,m_DF,m_EF), orbit, defect)
OUTSIDE_CLAIMED = {
    "O0a": ((0, 0, 2), (0, 0, 0), (3, 1, 1), 3, 2),
    "O0b": ((0, 1, 1), (0, 0, 0), (2, 2, 1), 3, 0),
    "O1a": ((0, 0, 2), (0, 0, 1), (4, 0, 0), 3, 5),
    "O1b": ((0, 0, 2), (0, 1, 0), (2, 2, 0), 6, 1),
    "O1c": ((0, 1, 1), (0, 0, 1), (3, 1, 0), 6, 3),
    "O1d": ((0, 1, 1), (1, 0, 0), (1, 1, 2), 3, 1),
}

# (KBPRW-4) claimed route table
ROUTES_CLAIMED = {
    "442-0a": {"O0b", "O1b", "O1d"},
    "442-1b": {"O0a", "O0b"},
    "433-0":  {"O0a", "O0b", "O1b", "O1c", "O1d"},
    "433-1a": {"O0b"},
    "433-1b": {"O0a", "O0b"},
}

PERMS = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]


def m_index(i, j):
    """m is indexed (DE, DF, EF) = pairs (0,1),(0,2),(1,2)"""
    a, b = min(i, j), max(i, j)
    return {(0, 1): 0, (0, 2): 1, (1, 2): 2}[(a, b)]


def canonical(r, l, m):
    """canonical form of (r,l,m) under permuting D,E,F"""
    best = None
    for p in PERMS:
        rr = tuple(r[p[i]] for i in range(3))
        ll = tuple(l[p[i]] for i in range(3))
        mm = []
        for (a, b) in [(0, 1), (0, 2), (1, 2)]:
            mm.append(m[m_index(p[a], p[b])])
        cand = (rr, ll, tuple(mm))
        if best is None or cand < best:
            best = cand
    return best


def solves(r, l, m):
    if sum(r) != 2:
        return False
    if sum(l) + sum(m) != 5:
        return False
    if sum(l) > 1:
        return False
    for i in range(3):
        deg = r[i] + 2 * l[i] + sum(m[m_index(i, j)] for j in range(3) if j != i)
        if deg != 4:
            return False
    return True


def main():
    # ---------- K1: exhaustive solution set of (KBPRW-2) ----------
    found = {}
    R = range(0, 5)
    for r in product(R, repeat=3):
        if sum(r) != 2:
            continue
        for l in product(range(0, 3), repeat=3):
            if sum(l) > 1:
                continue
            for m in product(range(0, 6), repeat=3):
                if solves(r, l, m):
                    found[canonical(r, l, m)] = found.get(canonical(r, l, m), 0) + 1
    print("K1 exhaustive scan of (KBPRW-2), sum l_i <= 1")
    print("   distinct orbits found:", len(found), "  claimed: 6")
    claimed_canon = {canonical(v[0], v[1], v[2]): k for k, v in OUTSIDE_CLAIMED.items()}
    print("   claimed orbits distinct:", len(claimed_canon))
    missing = set(found) - set(claimed_canon)
    extra = set(claimed_canon) - set(found)
    print("   orbits found but NOT claimed (KILL if nonempty):", len(missing))
    for x in sorted(missing):
        print("      ", x)
    print("   orbits claimed but NOT solutions (KILL if nonempty):", len(extra))
    for x in sorted(extra):
        print("      ", x, claimed_canon[x])
    print("   K1 verdict:", "NO KILL" if not missing and not extra else "KILL")

    # cross-check the printed orbit sizes (number of labeled tuples per orbit)
    print()
    print("   printed orbit sizes vs recomputed:")
    ok_sizes = True
    for name, v in OUTSIDE_CLAIMED.items():
        c = canonical(v[0], v[1], v[2])
        rec = found.get(c, 0)
        print("      %-4s printed %d  recomputed %d  %s"
              % (name, v[3], rec, "ok" if rec == v[3] else "MISMATCH"))
        ok_sizes &= (rec == v[3])
    print("   orbit-size check:", "consistent" if ok_sizes else "MISMATCH")

    # ---------- K2: reproduce (KBPRW-4) ----------
    print()
    print("K2 reproduction of (KBPRW-4) from 'defect <= 3' + 'common loop forbids outside loop'")
    derived = {}
    for cname, (cl, cm, cdef) in COMMON_LIVE.items():
        c_has_loop = sum(cl) > 0
        keep = set()
        for oname, (r, l, m, orb, odef) in OUTSIDE_CLAIMED.items():
            o_has_loop = sum(l) > 0
            if cdef + odef > 3:
                continue
            if c_has_loop and o_has_loop:
                continue
            keep.add(oname)
        derived[cname] = keep
    kill = False
    for cname in sorted(COMMON_LIVE):
        d, c = derived[cname], ROUTES_CLAIMED[cname]
        same = (d == c)
        kill |= not same
        print("   %-8s derived %-32s claimed %-32s %s"
              % (cname, ",".join(sorted(d)), ",".join(sorted(c)), "ok" if same else "MISMATCH"))
    total = sum(len(v) for v in derived.values())
    print("   derived total routes:", total, " claimed: 13 ->",
          "CONSISTENT" if total == 13 else "MISMATCH")
    print("   K2 verdict:", "KILL" if kill or total != 13 else "NO KILL")

    # ---------- KBPRW-1 bookkeeping ----------
    print()
    print("KBPRW-1 bookkeeping: 'five live orbits and seven labeled skeletons'")
    live_orbit_sizes = {"442-0a": 1, "442-1b": 2, "433-0": 1, "433-1a": 2, "433-1b": 1}
    print("   live orbit rows:", len(live_orbit_sizes),
          " sum of orbit column:", sum(live_orbit_sizes.values()))
    print("   -> reading 'orbit' column as labeled-skeleton count:",
          "CONSISTENT (5 orbits / 7 skeletons)"
          if len(live_orbit_sizes) == 5 and sum(live_orbit_sizes.values()) == 7
          else "MISMATCH")


if __name__ == "__main__":
    main()
