"""D3: the DEAD scales.  At R=10 (N=20, rho=4) and R=12 (N=24, rho=5)
the counting layer already closes the strict residual budget, so the
design functional Tmax_cf must stay below rho+2.  Exact check.

Tmax_cf(N,rho,q) = max number of core-free collinear split monic
degree-rho locators over the order-N subgroup of F_q.

Stdlib only.  Run under tools/ramguard.
"""
import itertools
import math


def say(s=""):
    print(str(s), flush=True)


def subgroup(q, N):
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
    locs = locators(D, q, rho)
    pts = [c for (_, c) in locs]
    inv = [0] * q
    for a in range(1, q):
        inv[a] = pow(a, q - 2, q)
    n = len(pts)
    best, bestmem = 1, None
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
                continue
            best, bestmem = len(mem), sup
    return best, bestmem


say("=== dead scales: the counting layer already closes B = R/2 ===")
say("R    N    rho  q     #loc     rho+2(need)  ERC2 cap  Tmax_cf  verdict")
for (Rv, q) in ((10, 41), (12, 73), (12, 97)):
    N = 2 * Rv
    rho = Rv // 2 - 1
    if (q - 1) % N:
        continue
    A = Rv + 1 - 2 * rho
    emax = rho // 3
    cap = max((N * e + rho - A * e) // rho for e in range(0, emax + 1))
    D = subgroup(q, N)
    t, mem = max_corefree(D, q, rho)
    say("%-4d %-4d %-4d %-5d %-8d %-12d %-9d %-8d %s"
        % (Rv, N, rho, q, math.comb(N, rho), rho + 2, cap, t,
           "closed (Tmax_cf < rho+2)" if t < rho + 2 else "VIOLATION"))
    if mem:
        say("     extremal core-free line supports: %s" % (mem,))
say("=== END ===")
