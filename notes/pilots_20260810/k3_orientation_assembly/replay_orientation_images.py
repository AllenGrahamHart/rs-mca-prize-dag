#!/usr/bin/env python3
"""Independent replay of the three declared orientation images of the
KoalaBear m2 r4 K3 arm.  Stdlib only; exact integer/combinatorial work.

Blocks:
  A. (KBDM-2)/(KBDM-3) diagonal facet-mixing orbit rows.
  B. (KBPRW-1)/(KBPRW-3)/(KBPRW-4) positive coordinate workboard.
  C. (KBCV-6)/(KBNL-2) negative coordinate workboard.

Nothing here is a new theorem; it is an audit that the printed censuses are
internally consistent with the printed equations, so that the routing-theorem
audit rests on replayed objects.
"""

from itertools import combinations, permutations, product

FAIL = []


def check(name, got, want):
    ok = got == want
    print(f"{'PASS' if ok else 'FAIL'} {name}: got {got!r} want {want!r}")
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------- block A
# Twelve source labels D = 0..11.  I = {0..5} invariant-coordinate six-set,
# K = {0..4} common five-set, xi = 5 the unique label of I \ K.
# tau = fixed-point-free involution on D.
# c = |I cap tau(J)| = |J cap tau(I)|
# a = number of tau two-cycles contained in K
# b = 1 iff tau(xi) in K
# (KBDM-1): tau(I) != I.

def fpf_involutions(labels):
    labels = tuple(labels)
    if not labels:
        yield {}
        return
    head, rest = labels[0], labels[1:]
    for i, partner in enumerate(rest):
        tail = rest[:i] + rest[i + 1:]
        for sub in fpf_involutions(tail):
            sub = dict(sub)
            sub[head] = partner
            sub[partner] = head
            yield sub


def block_a():
    D = list(range(12))
    I = set(range(6))
    J = set(range(6, 12))
    K = set(range(5))
    xi = 5
    rows = {}
    n_inv = 0
    n_preserving = 0
    for tau in fpf_involutions(D):
        n_inv += 1
        tauI = {tau[x] for x in I}
        tauJ = {tau[x] for x in J}
        if tauI == I:
            n_preserving += 1
            continue                      # (KBDM-1) deletes these
        c = len(I & tauJ)
        c2 = len(J & tauI)
        assert c == c2, "|I cap tau(J)| != |J cap tau(I)|"
        assert len(I & tauI) == 6 - c, "(KBDM-2) complement identity"
        a = sum(1 for k in K if tau[k] in K and tau[k] > k)
        b = 1 if tau[xi] in K else 0
        rows.setdefault((a, b, c), 0)
        rows[(a, b, c)] += 1
    check("A1 number of fixed-point-free involutions on 12 labels",
          n_inv, 10395)
    check("A2 c values realised", sorted({r[2] for r in rows}), [2, 4, 6])
    check("A3 (KBDM-3) orbit rows",
          sorted(rows),
          [(0, 0, 6), (0, 1, 4), (1, 0, 4), (1, 1, 2), (2, 0, 2)])
    print("     A3 multiplicities (labelled tau count per row):",
          {k: rows[k] for k in sorted(rows)})
    print("     A4 partition-preserving tau deleted by (KBDM-1):",
          n_preserving)
    return rows


# ---------------------------------------------------------------- block B/C
# Common / outside skeletons.  Vertices 0,1,2; l_i loops; m_ij internal
# edges.  Degree law deg_i = 2 l_i + sum_{j!=i} m_ij (verified against every
# printed row of (KBPRW-1) and (KBPRW-3)).
# Defect law reconstructed from the printed defect columns and verified on
# all sixteen printed rows:
#     defect = (number of loops) + sum_{i<j} 2*max(m_ij - 2, 0)

PAIRS = [(0, 1), (0, 2), (1, 2)]


def degrees(l, m):
    mm = {p: m[i] for i, p in enumerate(PAIRS)}
    out = []
    for i in range(3):
        d = 2 * l[i]
        for j in range(3):
            if j != i:
                d += mm[tuple(sorted((i, j)))]
        out.append(d)
    return tuple(out)


def defect(l, m):
    return sum(l) + sum(2 * max(x - 2, 0) for x in m)


def relabel(l, m, p):
    """Apply the vertex permutation p (new position i holds old vertex
    p[i]) to (l, m)."""
    mm = {tuple(sorted(pp)): m[i] for i, pp in enumerate(PAIRS)}
    lp = tuple(l[p[i]] for i in range(3))
    mp = tuple(mm[tuple(sorted((p[i], p[j])))] for (i, j) in PAIRS)
    return lp, mp


def canon(l, m):
    """Orbit representative under the subgroup that preserves the ORDERED
    degree profile: (4,4,2) admits only the A<->B swap, (4,3,3) only the
    B<->C swap.  A skeleton whose ordered degrees are neither is first
    rotated into the profile-normal order."""
    d = degrees(l, m)
    sd = sorted(d, reverse=True)
    # rotate into normal order: 442 -> (4,4,2), 433 -> (4,3,3)
    order = sorted(range(3), key=lambda i: (-d[i], i))
    l, m = relabel(l, m, tuple(order))
    if sd == [4, 4, 2]:
        group = [(0, 1, 2), (1, 0, 2)]
    else:
        group = [(0, 1, 2), (0, 2, 1)]
    best = None
    for p in group:
        cand = relabel(l, m, p)
        if best is None or cand < best:
            best = cand
    return best


def enumerate_skeletons():
    """All (l;m) with at most one loop per vertex, total edge count 5, and
    degree multiset (4,4,2) or (4,3,3).  Returns dict orbit-representative
    -> [profile, orbit size, defect, loops]."""
    out = {}
    for l in product(range(2), repeat=3):
        for m in product(range(6), repeat=3):
            if sum(l) + sum(m) != 5:
                continue
            d = sorted(degrees(l, m), reverse=True)
            if d not in ([4, 4, 2], [4, 3, 3]):
                continue
            rep = canon(l, m)
            prof = "442" if d == [4, 4, 2] else "433"
            out.setdefault(rep, [prof, 0, defect(l, m), sum(l)])
            out[rep][1] += 1
    # orbit sizes were counted over ALL labellings of the three vertices;
    # divide out the profile-normalising rotation (3 for 442 since the
    # degree-2 vertex can sit in any slot, 3 for 433 likewise).
    for rep in out:
        out[rep][1] //= 3
    return out


def block_b():
    sk = enumerate_skeletons()
    check("B1 common orbit count (parent's ten)", len(sk), 10)
    printed = {
        ((0, 0, 0), (3, 1, 1)): ("442-0a", 1, 2),
        ((0, 0, 1), (4, 0, 0)): ("442-1a", 1, 5),
        ((0, 1, 0), (2, 2, 0)): ("442-1b", 2, 1),
        ((1, 1, 0), (1, 1, 1)): ("442-2", 1, 2),
        ((1, 1, 1), (2, 0, 0)): ("442-3", 1, 3),
        ((0, 0, 0), (2, 2, 1)): ("433-0", 1, 0),
        ((0, 0, 1), (3, 1, 0)): ("433-1a", 2, 3),
        ((1, 0, 0), (1, 1, 2)): ("433-1b", 1, 1),
        ((1, 0, 1), (2, 0, 1)): ("433-2", 2, 2),
        ((1, 1, 1), (1, 1, 0)): ("433-3", 1, 3),
    }
    by_canon = {}
    for (l, m), (name, orb, dfc) in printed.items():
        by_canon[canon(l, m)] = (name, orb, dfc)
    check("B2 printed rows are ten distinct orbits", len(by_canon), 10)
    check("B3 printed orbit set equals enumerated orbit set",
          sorted(by_canon) == sorted(sk), True)
    bad = []
    for rep, (name, orb, dfc) in by_canon.items():
        prof, size, mydfc, loops = sk[rep]
        if size != orb or mydfc != dfc:
            bad.append((name, (size, mydfc), (orb, dfc)))
    check("B4 orbit sizes and defects match (KBPRW-1)", bad, [])

    live = {}
    for rep, (name, orb, dfc) in by_canon.items():
        prof, size, mydfc, loops = sk[rep]
        if loops <= 1 and mydfc <= 3:
            live[name] = (mydfc, loops, size)
    check("B5 live common orbits (loop cap 1, defect cap 3)",
          sorted(live), ["433-0", "433-1a", "433-1b", "442-0a", "442-1b"])
    check("B6 labelled live skeletons",
          sum(v[2] for v in live.values()), 7)

    # (KBPRW-2)/(KBPRW-3): outside orbits.
    outside = {}
    for r in product(range(5), repeat=3):
        if sum(r) != 2:
            continue
        for l in product(range(3), repeat=3):
            if sum(l) > 1:
                continue
            for m in product(range(6), repeat=3):
                if sum(l) + sum(m) != 5:
                    continue
                ok = True
                mm = {p: m[i] for i, p in enumerate(PAIRS)}
                for i in range(3):
                    d = r[i] + 2 * l[i]
                    for j in range(3):
                        if j != i:
                            d += mm[tuple(sorted((i, j)))]
                    if d != 4:
                        ok = False
                        break
                if not ok:
                    continue
                # orbit under permuting D,E,F (acts on r, l and m together)
                best = None
                for p in permutations(range(3)):
                    rp = tuple(r[p.index(i)] for i in range(3))
                    lp = tuple(l[p.index(i)] for i in range(3))
                    mp = tuple(mm[tuple(sorted((p.index(i), p.index(j))))]
                               for (i, j) in PAIRS)
                    cand = (rp, lp, mp)
                    if best is None or cand < best:
                        best = cand
                outside.setdefault(best, [0, sum(l) + sum(2 * max(x - 2, 0)
                                                          for x in m)])
                outside[best][0] += 1
    check("B7 outside orbit count", len(outside), 6)
    printed_out = {
        ((0, 0, 2), (0, 0, 0), (3, 1, 1)): ("O0a", 3, 2),
        ((0, 1, 1), (0, 0, 0), (2, 2, 1)): ("O0b", 3, 0),
        ((0, 0, 2), (0, 0, 1), (4, 0, 0)): ("O1a", 3, 5),
        ((0, 0, 2), (0, 1, 0), (2, 2, 0)): ("O1b", 6, 1),
        ((0, 1, 1), (0, 0, 1), (3, 1, 0)): ("O1c", 6, 3),
        ((0, 1, 1), (1, 0, 0), (1, 1, 2)): ("O1d", 3, 1),
    }
    mismatch = []
    named = {}
    for key, (name, orb, dfc) in printed_out.items():
        r, l, m = key
        mm = {p: m[i] for i, p in enumerate(PAIRS)}
        best = None
        for p in permutations(range(3)):
            rp = tuple(r[p.index(i)] for i in range(3))
            lp = tuple(l[p.index(i)] for i in range(3))
            mp = tuple(mm[tuple(sorted((p.index(i), p.index(j))))]
                       for (i, j) in PAIRS)
            cand = (rp, lp, mp)
            if best is None or cand < best:
                best = cand
        if best not in outside:
            mismatch.append((name, "orbit absent"))
            continue
        size, dd = outside[best]
        named[name] = (dd, sum(l))
        if size != orb or dd != dfc:
            mismatch.append((name, (size, dd), (orb, dfc)))
    check("B8 outside orbit sizes and defects match (KBPRW-3)",
          mismatch, [])

    # (KBPRW-4): total defect <= 3, and a common loop forbids an outside loop.
    routes = []
    for cname in sorted(live):
        cdfc, cloops, _ = live[cname]
        for oname in sorted(named):
            odfc, oloops = named[oname]
            if cdfc + odfc > 3:
                continue
            if cloops > 0 and oloops > 0:
                continue
            routes.append((cname, oname))
    check("B9 total necessary route records", len(routes), 13)
    printed_routes = sorted([
        ("442-0a", "O0b"), ("442-0a", "O1b"), ("442-0a", "O1d"),
        ("442-1b", "O0a"), ("442-1b", "O0b"),
        ("433-0", "O0a"), ("433-0", "O0b"), ("433-0", "O1b"),
        ("433-0", "O1c"), ("433-0", "O1d"),
        ("433-1a", "O0b"),
        ("433-1b", "O0a"), ("433-1b", "O0b"),
    ])
    check("B10 route table equals (KBPRW-4)", sorted(routes), printed_routes)
    return sk


def block_c(sk):
    # (KBCV-6) injective pair-multiplicity skeletons = all m_ij <= 2.
    injective = {}
    for rep, (prof, size, dfc, loops) in sk.items():
        l, m = rep
        if max(m) <= 2:
            injective[rep] = (prof, size, dfc, loops)
    check("C1 injective skeleton orbits (parent's seven)",
          len(injective), 7)
    # (KBNL-1) ell_K <= 2, ell_K = number of loop orbits.
    negative = {rep: v for rep, v in injective.items() if v[3] <= 2}
    check("C2 negative skeletons after ell_K<=2 (KBNL-2)",
          len(negative), 5)
    printed_neg = [
        ((0, 1, 0), (2, 2, 0)),
        ((1, 1, 0), (1, 1, 1)),
        ((0, 0, 0), (2, 2, 1)),
        ((1, 0, 0), (1, 1, 2)),
        ((1, 0, 1), (2, 0, 1)),
    ]
    check("C3 negative skeleton set equals printed (KBNL-2)",
          sorted(canon(l, m) for (l, m) in printed_neg),
          sorted(negative))
    # The two sets of five differ: this is a real structural fact.
    pos_live = {"433-0", "433-1a", "433-1b", "442-0a", "442-1b"}
    name_of = {
        canon((0, 0, 0), (3, 1, 1)): "442-0a",
        canon((0, 0, 1), (4, 0, 0)): "442-1a",
        canon((0, 1, 0), (2, 2, 0)): "442-1b",
        canon((1, 1, 0), (1, 1, 1)): "442-2",
        canon((1, 1, 1), (2, 0, 0)): "442-3",
        canon((0, 0, 0), (2, 2, 1)): "433-0",
        canon((0, 0, 1), (3, 1, 0)): "433-1a",
        canon((1, 0, 0), (1, 1, 2)): "433-1b",
        canon((1, 0, 1), (2, 0, 1)): "433-2",
        canon((1, 1, 1), (1, 1, 0)): "433-3",
    }
    neg_names = sorted(name_of[r] for r in negative)
    check("C4 negative live names",
          neg_names, ["433-0", "433-1b", "433-2", "442-1b", "442-2"])
    print("     C5 positive-only live skeletons:",
          sorted(pos_live - set(neg_names)))
    print("     C6 negative-only live skeletons:",
          sorted(set(neg_names) - pos_live))
    print("     C7 shared skeletons:",
          sorted(pos_live & set(neg_names)))


def main():
    print("== block A: diagonal facet-mixing orbit rows (KBDM-2/3) ==")
    block_a()
    print()
    print("== block B: positive coordinate workboard (KBPRW-1/3/4) ==")
    sk = block_b()
    print()
    print("== block C: negative coordinate workboard (KBCV-6/KBNL-2) ==")
    block_c(sk)
    print()
    print("FAILURES:", FAIL if FAIL else "none")


if __name__ == "__main__":
    main()
