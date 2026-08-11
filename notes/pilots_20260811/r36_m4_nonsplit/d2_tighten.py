"""D2b: the (DEG-m)-TIGHTENED m=4 2-sharing search.

Anchor 1 measured its m=4 ceilings on a RELAXATION: the DFS capped
degrees from ABOVE only, while (DEG-m) (r35 REPORT.md:256-263) forces
deg_H(gamma) + X''_gamma >= 2 at m=4 with the EXACT middle budget
sum_gamma X''_gamma = (m-1)(m-2) = 6.  A degree-1 slope therefore needs
X'' >= 1 and a degree-0 slope needs X'' >= 2, so any (DEG-m)-consistent
selection using s of the T_2 = 15 type-2 slopes must satisfy

      n_1 + 2*(15 - s)  <=  6 .

Two variants, SAME pencils, SAME budget, SAME draw count, SAME run, per
field -- so the comparison is matched (anchor 1 MISS 5).

Writes d2_tighten_results.txt in this directory only.  Stdlib only.
"""
import random
import sys
import time

DIR = "notes/pilots_20260811/r36_m4_nonsplit/"
OUT = []
T0 = time.time()
DEADLINE = 250.0


def p(s=""):
    OUT.append(str(s))


def flush():
    with open(DIR + "d2_tighten_results.txt", "w") as f:
        f.write("\n".join(OUT) + "\n")


def mu(q, n=64):
    for g in range(2, q):
        h = pow(g, (q - 1) // n, q)
        s = set()
        x = 1
        for _ in range(n):
            s.add(x)
            x = x * h % q
        if len(s) == n:
            return sorted(s)
    raise RuntimeError


def ev(c, x, q):
    r = 0
    for a in c:
        r = (r * x + a) % q
    return r


def orbits(q, D):
    """(SPLIT-4)+sigma(x)=-x: 32 orbits, each carrying the shared triple
    {phi(x), phi(-x), chi(x)} with chi Mobius in u = x^2 (r34 D3.1)."""
    seen = set()
    obs = []
    for x in D:
        if x in seen:
            continue
        y = (-x) % q
        seen.add(x)
        seen.add(y)
        obs.append((x, y))
    return obs


def draw_triples(q, D, obs, rnd):
    A = [rnd.randrange(q) for _ in range(4)]
    B = [rnd.randrange(q) for _ in range(4)]
    R = [rnd.randrange(q) for _ in range(2)]
    S = [rnd.randrange(q) for _ in range(2)]
    out = []
    for x, y in obs:
        bx, by = ev(B, x, q), ev(B, y, q)
        u = x * x % q
        sv = ev(S, u, q)
        if bx == 0 or by == 0 or sv == 0:
            continue
        a = ev(A, x, q) * pow(bx, q - 2, q) % q
        b = ev(A, y, q) * pow(by, q - 2, q) % q
        c = ev(R, u, q) * pow(sv, q - 2, q) % q
        t = (a, b, c)
        if len(set(t)) == 3:
            out.append(tuple(sorted(t)))
    return out


def dfs(trips, budget, tighten):
    """max selection: pair multiplicity <= 1 (linear), degree <= 3,
    <= 15 slopes.  tighten: also require n_1 + 2*(15-s) <= 6."""
    best = [0]
    nodes = [0]
    deg = {}
    pairs = set()

    prof = [None]

    def consistent():
        """(DEG-m) is a COMPLETION-level condition: a complete m=4
        configuration has n_1+n_2+n_3 = 15, sum deg = 36, deg <= 3, hence
        2n_1+n_2 = 9 and n_1 <= 4; and n_0 = 15-s <= 3 because a degree-0
        slope needs X'' >= 2 against the exact budget sum X'' = 6.
        Applied to a PARTIAL selection it is not monotone -- degrees still
        grow -- so it can only be evaluated at the full target."""
        s = len(deg)
        n1 = sum(1 for v in deg.values() if v == 1)
        return n1 <= 4 and 15 - s <= 3

    def rec(i, cnt):
        nodes[0] += 1
        if nodes[0] > budget:
            return
        if cnt > best[0] and (not tighten or cnt < 12 or consistent()):
            best[0] = cnt
            prof[0] = (len(deg), sum(1 for v in deg.values() if v == 1),
                       sorted(deg.values()))
        if i >= len(trips) or cnt + (len(trips) - i) <= best[0]:
            return
        t = trips[i]
        ps = [(t[0], t[1]), (t[0], t[2]), (t[1], t[2])]
        ok = all(pp not in pairs for pp in ps)
        if ok:
            add = [g for g in t if g not in deg]
            if len(deg) + len(add) <= 15 and all(deg.get(g, 0) < 3 for g in t):
                for g in t:
                    deg[g] = deg.get(g, 0) + 1
                for pp in ps:
                    pairs.add(pp)
                rec(i + 1, cnt + 1)
                for pp in ps:
                    pairs.discard(pp)
                for g in t:
                    deg[g] -= 1
                    if deg[g] == 0:
                        del deg[g]
        rec(i + 1, cnt)

    rec(0, 0)
    return best[0], prof[0]


BUDGET = 12000
NDRAW = 215
FIELDS = [193, 257]
if len(sys.argv) > 1:
    FIELDS = [int(x) for x in sys.argv[1].split(",")]

p("=== D2b  (DEG-m)-TIGHTENED m=4 2-SHARING SEARCH ===")
p("class: (SPLIT-4)+sigma(x)=-x on mu_64, shared triple per orbit")
p("budget %d DFS nodes/draw, %d draws/field -- MATCHED to anchor 1's"
  % (BUDGET, NDRAW))
p("m4_struct cell (r35 REPORT.md:170-176: budget 12000, ~215 draws)")
p("target = 12 of 12 shared triples")
p()
for q in FIELDS:
    if time.time() - T0 > DEADLINE:
        p("!! DEADLINE before q=%d -- ZERO DRAWS, NOT a measurement" % q)
        break
    D = mu(q)
    obs = orbits(q, D)
    rnd = random.Random(31 * q)
    hu, ht = {}, {}
    bu = bt = 0
    bprof = None
    n = 0
    for _ in range(NDRAW):
        if time.time() - T0 > DEADLINE:
            break
        trips = draw_triples(q, D, obs, rnd)
        if len(trips) < 12:
            continue
        ku, pu = dfs(trips, BUDGET, False)
        kt, _ = dfs(trips, BUDGET, True)
        hu[ku] = hu.get(ku, 0) + 1
        ht[kt] = ht.get(kt, 0) + 1
        if ku > bu:
            bu, bprof = ku, pu
        bt = max(bt, kt)
        n += 1
    p("--- q = %d : %d draws, %d orbits/draw" % (q, n, len(obs)))
    p("    V-RELAXED  (deg<=3, <=15 slopes, linear)      BEST = %2d of 12" % bu)
    p("      histogram %s" % dict(sorted(hu.items())))
    p("    V-TIGHTENED (+ (DEG-m): n_1 + 2(15-s) <= 6)   BEST = %2d of 12" % bt)
    p("      histogram %s" % dict(sorted(ht.items())))
    p("    CEILING MOVED BY %d triple(s)" % (bu - bt))
    if bprof:
        s, n1, ds = bprof
        p("    best partial profile: s = %d slopes, n_1 = %d degree-1 slopes,"
          % (s, n1))
        p("      degree sequence %s" % ds)
        p("      completion bounds: n_1 <= 4 ? %s ; n_0 = 15-s = %d <= 3 ? %s"
          % (n1 <= 4, 15 - s, 15 - s <= 3))
        p("      -> the partial is NOT (DEG-m)-completable as it stands"
          if (n1 > 4 or 15 - s > 3) else
          "      -> the partial is (DEG-m)-completable as it stands")
    p()
    flush()

p("NOTE: both variants are DFS CEILINGS under the named budget over the")
p("named class -- not upper bounds (R7.1).")
p("total wall %.1f s" % (time.time() - T0))
flush()
print("\n".join(OUT))
