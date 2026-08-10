"""Transport arithmetic for the 433-1b -> O0b split-BC outside-label quotients.

NOT a census and NOT an elimination: this only counts orbits of record
permutations acting on the 7*15 = 105 (missing-record, residual-matching)
labels.  Two of the four cases reproduce numbers already banked in the DAG
(57 orbits for the d -> -d involution, 36 orbits for the O0a universal
quotient); those two are the validation of the label model itself.

stdlib only.
"""

from itertools import combinations


def matchings(items):
    """All perfect matchings of an even-size tuple into unordered pairs."""
    if not items:
        return [frozenset()]
    first = items[0]
    out = []
    for k in range(1, len(items)):
        pair = frozenset((first, items[k]))
        rest = items[1:k] + items[k + 1:]
        for m in matchings(rest):
            out.append(m | {pair})
    return out


def labels():
    """(xi, matching-of-the-other-six) for xi in 0..6."""
    out = []
    for xi in range(7):
        rest = tuple(r for r in range(7) if r != xi)
        for m in matchings(rest):
            out.append((xi, frozenset(m)))
    return out


def act(perm, label):
    xi, m = label
    return (perm[xi], frozenset(frozenset(perm[i] for i in p) for p in m))


def perm_from_cycles(cycles):
    p = list(range(7))
    for cyc in cycles:
        for i in range(len(cyc)):
            p[cyc[i]] = cyc[(i + 1) % len(cyc)]
    return p


def orbits(gens, universe):
    seen = set()
    prof = {}
    n = 0
    for lab in universe:
        if lab in seen:
            continue
        comp = {lab}
        stack = [lab]
        while stack:
            cur = stack.pop()
            for g in gens:
                nxt = act(g, cur)
                if nxt not in comp:
                    comp.add(nxt)
                    stack.append(nxt)
        seen |= comp
        prof[len(comp)] = prof.get(len(comp), 0) + 1
        n += 1
    return n, dict(sorted(prof.items()))


U = labels()
assert len(U) == 105, len(U)
assert len(set(U)) == 105

CASES = [
    # name, generator cycle-lists, banked expectation (or None)
    ("VALIDATE O0b SBC / d -> -d      (2 3)(4 5)",
     [[(2, 3), (4, 5)]], "banked 57 orbits, profile 1:9,2:48"),
    ("VALIDATE O0a universal          (0 1) and (3 4)",
     [[(0, 1)], [(3, 4)]], "banked 36 orbits, profile 1:3,2:15,4:18"),
    ("NEW  O0b SDE/SDF identical pair (2 3)",
     [[(2, 3)]], None),
    ("NEW  O0b S0 B<->C,E<->F         (0 1)(2 4)(3 5)",
     [[(0, 1), (2, 4), (3, 5)]], None),
    ("NEW  O0b S0 both generators",
     [[(0, 1), (2, 4), (3, 5)], [(2, 3), (4, 5)]], None),
]

for name, cyclesets, note in CASES:
    gens = [perm_from_cycles(cs) for cs in cyclesets]
    n, prof = orbits(gens, U)
    total = sum(k * v for k, v in prof.items())
    print("%-46s orbits=%3d profile=%s total=%d %s"
          % (name, n, prof, total, note or ""))
    assert total == 105
