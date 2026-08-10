"""D3 corrected: structured vs sporadic collinearity of the
reciprocal-locator point set (registrations A2', A3', A4).

structured line: for a (rho+1)-subset U of D\\W the rho+1 points
   P_{U\\{u}} = [A - u B]  are collinear over EVERY field.
sporadic triple: collinear {P_S1,P_S2,P_S3} whose union has > rho+1 points.

Stdlib only.  Run under tools/ramguard.
"""
import itertools
import random


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


def sigma_prime_W(W, q):
    out = {}
    for x in W:
        p = 1
        for y in W:
            if y != x:
                p = p * (x - y) % q
        out[x] = p
    return out


def point(S, W, spw, q):
    v = []
    for x in W:
        s = 1
        for y in S:
            s = s * (x - y) % q
        v.append(pow(spw[x] * s % q, q - 2, q))
    for c in v:
        if c:
            iv = pow(c, q - 2, q)
            return tuple(t * iv % q for t in v)
    return None


def on_line(p, u, w, q):
    n = len(u)
    i0 = -1
    det = 0
    for i in range(n):
        for j in range(i + 1, n):
            d = (u[i] * w[j] - u[j] * w[i]) % q
            if d:
                i0, j0, det = i, j, d
                break
        if i0 >= 0:
            break
    if i0 < 0:
        return False
    inv = pow(det, q - 2, q)
    al = (p[i0] * w[j0] - p[j0] * w[i0]) % q * inv % q
    be = (u[i0] * p[j0] - u[j0] * p[i0]) % q * inv % q
    for t in range(n):
        if (al * u[t] + be * w[t] - p[t]) % q:
            return False
    return True


def census(q, N, rho, a, W, label):
    D = subgroup(q, N)
    if W is None:
        W = sorted(random.sample(D, a))
    rest = [x for x in D if x not in W]
    spw = sigma_prime_W(W, q)
    subs = list(itertools.combinations(rest, rho))
    P = [point(S, W, spw, q) for S in subs]
    M = len(P)
    struct = spor = 0
    sporex = []
    for i in range(M):
        for j in range(i + 1, M):
            for k in range(j + 1, M):
                if on_line(P[k], P[i], P[j], q):
                    un = set(subs[i]) | set(subs[j]) | set(subs[k])
                    if len(un) <= rho + 1:
                        struct += 1
                    else:
                        spor += 1
                        if len(sporex) < 4:
                            sporex.append((subs[i], subs[j], subs[k]))
    say("  %-22s q=%-4d M=%-4d structured=%-6d sporadic=%-4d"
        % (label, q, M, struct, spor))
    for e in sporex:
        say("        sporadic: %s %s %s" % e)
    return struct, spor


say("=== A2' : structured lines are field-independent and counting-dead ===")
for (q, N, rho, a) in [(17, 16, 3, 6), (97, 32, 7, 10)]:
    D = subgroup(q, N)
    random.seed(7)
    W = sorted(random.sample(D, a))
    rest = [x for x in D if x not in W]
    spw = sigma_prime_W(W, q)
    U = tuple(rest[:rho + 1])
    pts = [point(tuple(u for u in U if u != x), W, spw, q) for x in U]
    allon = all(on_line(pts[t], pts[0], pts[1], q) for t in range(2, len(pts)))
    say("  q=%d N=%d rho=%d a=%d : U of size rho+1=%d -> %d points, all"
        " collinear : %s" % (q, N, rho, a, rho + 1, len(pts), allon))
    say("      their supports give d_x = rho = %d for x in U ; counting layer"
        " needs d_x <= e = m = %d  ->  %s"
        % (rho, (rho + 1) // 4, "EXCLUDED" if rho > (rho + 1) // 4 else "allowed"))
say()

say("=== A4 : the m=1 fence's own W vs random W, at q=17 ===")
census(17, 16, 3, 6, [1, 2, 3, 5, 7, 11], "FENCE W")
random.seed(20260810)
for t in range(4):
    census(17, 16, 3, 6, None, "random W #%d" % t)
say()

say("=== A3' : sporadic census across prime fields (m=1, N=16, rho=3, a=6) ===")
say("   q     #W   mean structured  mean sporadic   heuristic 280000/q^4")
random.seed(20260810)
for q in [17, 97, 113, 193, 241]:
    if (q - 1) % 16:
        continue
    ss = sp = 0
    nW = 6
    for _ in range(nW):
        a1, b1 = census(q, 16, 3, 6, None, "  scan")
        ss += a1
        sp += b1
    say("  %-5d %-4d %-16.2f %-15.3f %.4f"
        % (q, nW, ss / nW, sp / nW, 280000 / q ** 4))
say("=== END part 5 ===")
