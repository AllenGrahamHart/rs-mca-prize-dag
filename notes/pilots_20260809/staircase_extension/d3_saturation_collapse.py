"""D3: the saturation-collapse curve.

Measured functional (CATCH-19C):
    Tmax_cf(N, rho, q) = the maximum number of monic squarefree
    degree-rho polynomials, split over the order-N multiplicative
    subgroup D of F_q, that lie on ONE affine line in coefficient space
    AND have no common root (core-free, i.e. s = 0).

By the split-pencil equivalence this is exactly the maximal number of
far-CA supported slopes of a parameter-degree-1 (e=1) Hankel pencil of
generic rank rho, and it is capped by the proved incidence bound
    Tmax_cf <= floor((N e + rho - A e)/rho)  with e=1, A=R+1-2rho.
For the pure design cap ignoring A it is floor(N/rho).

The registered density law says a saturating configuration costs
q^(cond-dim) and is bought by combinatorial entropy, so saturation
should be a SMALL-FIELD phenomenon: at fixed (N,rho), Tmax_cf should
fall as q grows.

Stdlib only.  Run under tools/ramguard.
"""
import itertools


def say(s=""):
    print(str(s), flush=True)


def is_prime(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def subgroup(q, N):
    assert (q - 1) % N == 0
    for cand in range(2, q):
        x, order = 1, 0
        while True:
            x = x * cand % q
            order += 1
            if x == 1:
                break
        if order == q - 1:
            g = cand
            break
    h = pow(g, (q - 1) // N, q)
    D, x = [], 1
    for _ in range(N):
        D.append(x)
        x = x * h % q
    return sorted(D)


def locators(D, q, rho):
    out = []
    for S in itertools.combinations(D, rho):
        c = [1]
        for x in S:
            nc = [0] * (len(c) + 1)
            for i, ci in enumerate(c):
                nc[i] = (nc[i] - x * ci) % q
                nc[i + 1] = (nc[i + 1] + ci) % q
            c = nc
        out.append((S, tuple(c[:-1])))
    return out


def max_corefree(D, q, rho):
    """frugal: per base point, bucket normalised directions."""
    locs = locators(D, q, rho)
    pts = [c for (_, c) in locs]
    inv = [0] * q
    for a in range(1, q):
        inv[a] = pow(a, q - 2, q)
    n = len(pts)
    best = 1
    bestmem = None
    for i in range(n):
        Pi = pts[i]
        buck = {}
        for j in range(i + 1, n):
            Pj = pts[j]
            v = tuple((Pj[t] - Pi[t]) % q for t in range(rho))
            fi = 0
            while v[fi] == 0:
                fi += 1
            iv = inv[v[fi]]
            vn = tuple(vt * iv % q for vt in v)
            b = buck.get(vn)
            if b is None:
                buck[vn] = [j]
            else:
                b.append(j)
        for vn, js in buck.items():
            if len(js) + 1 <= best:
                continue
            mem = [i] + js
            sup = [locs[t][0] for t in mem]
            common = set(sup[0])
            for s in sup[1:]:
                common &= set(s)
            if common:
                continue                     # core line: s >= 1
            if len(mem) > best:
                best, bestmem = len(mem), sup
    return best, bestmem


say("=== saturation-collapse: Tmax_cf(N,rho,q) vs the incidence cap ===")
say("N   rho  q     #loc   floor(N/rho)  Tmax_cf  saturated?")
rows = []
# field axis at fixed (N,rho) = (16,3)
for q in [17, 97, 113, 193, 241, 337, 449, 577, 673, 769]:
    if (q - 1) % 16:
        continue
    D = subgroup(q, 16)
    t, mem = max_corefree(D, q, 3)
    rows.append((16, 3, q, t, 16 // 3))
    say("16  3    %-5d %-6d %-13d %-8d %s"
        % (q, 560, 16 // 3, t, t == 16 // 3))
# scale axis at rho=3, smallest admissible prime field each time
for N in (12, 20, 24, 28, 32, 36, 40):
    q = None
    for cand in range(N + 1, 4000):
        if (cand - 1) % N == 0 and is_prime(cand):
            q = cand
            break
    D = subgroup(q, N)
    import math
    nloc = math.comb(N, 3)
    t, mem = max_corefree(D, q, 3)
    say("%-3d 3    %-5d %-6d %-13d %-8d %s"
        % (N, q, nloc, N // 3, t, t == N // 3))
    if mem is not None and t >= 5:
        say("      witness supports: %s" % (mem,))
say()
say("=== rho=4 and rho=5 spot checks (smallest admissible prime field) ===")
for (N, rho) in ((16, 4), (20, 4), (24, 4), (16, 5), (20, 5)):
    q = None
    for cand in range(N + 1, 4000):
        if (cand - 1) % N == 0 and is_prime(cand):
            q = cand
            break
    D = subgroup(q, N)
    import math
    t, mem = max_corefree(D, q, rho)
    say("N=%-3d rho=%-2d q=%-5d #loc=%-7d floor(N/rho)=%-3d Tmax_cf=%-3d %s"
        % (N, rho, q, math.comb(N, rho), N // rho, t,
           "SATURATED" if t == N // rho else ""))
say("=== END ===")
