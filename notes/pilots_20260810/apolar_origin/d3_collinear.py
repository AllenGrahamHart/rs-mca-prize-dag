"""D3: the extremal normal form (AO2) and the q=17 field artifact.

Measured functional: for a joint support W (|W|=a) and a rho-subset S of
D\\W, the reciprocal-locator point

    P_S = [ 1/(sigma'_W(x) sigma_S(x)) ]_{x in W}  in  P^(a-1).

collin(W) = max over lines L of P^(a-1) of #{S : P_S in L}.
trip(W)   = number of collinear triples {P_S}.

A1 : the m=1 fence's three type-2 supports must be collinear.
A2 : mean trip(W) across prime fields q = 1 mod 16.
A3 : m=2 (N=32, rho=7, a=10, q=97) sampled search.

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
    """P_S, normalised so the first nonzero coordinate is 1."""
    v = []
    for x in W:
        s = 1
        for y in S:
            s = s * (x - y) % q
        if s == 0:
            return None
        v.append(pow(spw[x] * s % q, q - 2, q))
    for c in v:
        if c:
            iv = pow(c, q - 2, q)
            return tuple(t * iv % q for t in v)
    return None


def on_line(p, u, w, q):
    """is p in span(u,w)?  rank([u;w;p]) == 2 test."""
    n = len(u)
    i0 = j0 = -1
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


say("=== A1 : the m=1 fence, extremal normal form ===")
q = 17
D = subgroup(q, 16)
W = [1, 2, 3, 5, 7, 11]
spw = sigma_prime_W(W, q)
T2 = [(9, 12, 13), (4, 6, 16), (8, 10, 15)]
pts = [point(S, W, spw, q) for S in T2]
for S, p in zip(T2, pts):
    say("  S=%s -> P_S = %s" % (S, p))
say("  P_3 on line(P_1,P_2) : %s" % on_line(pts[2], pts[0], pts[1], q))
# the two type-1 slopes give z with 3 zero coordinates each
say("  (type-1 slopes contribute the two points of L with 3 vanishing"
    " coordinates; they are the S_0,S_1 halves of W)")
say()

say("=== A2 : field census of collinearity at m=1 (N=16, rho=3, a=6) ===")
say("   q     #W sampled  mean trip(W)  max collin(W)  heuristic C(120,3)/q^4")
random.seed(20260810)
for q in [17, 97, 113, 193, 241]:
    if (q - 1) % 16:
        continue
    D = subgroup(q, 16)
    nW = 6
    tots, best = 0, 0
    for _ in range(nW):
        W = sorted(random.sample(D, 6))
        rest = [x for x in D if x not in W]
        spw = sigma_prime_W(W, q)
        P = []
        for S in itertools.combinations(rest, 3):
            p = point(S, W, spw, q)
            if p:
                P.append(p)
        M = len(P)
        cnt = 0
        bb = 0
        for i in range(M):
            for j in range(i + 1, M):
                c = 2
                for k in range(j + 1, M):
                    if on_line(P[k], P[i], P[j], q):
                        cnt += 1
                        c += 1
                bb = max(bb, c)
        tots += cnt
        best = max(best, bb)
    say("  %-5d %-11d %-13.3f %-14d %.4f"
        % (q, nW, tots / nW, best, 280840 / q ** 4))
say()

say("=== A3 : m=2 sampled search (N=32, rho=7, a=10, q=97) ===")
q = 97
D = subgroup(q, 32)
random.seed(20260810)
nW, nlines = 3, 120
for _ in range(nW):
    W = sorted(random.sample(D, 10))
    rest = [x for x in D if x not in W]
    spw = sigma_prime_W(W, q)
    P = []
    for S in itertools.combinations(rest, 7):
        p = point(S, W, spw, q)
        if p:
            P.append(p)
    M = len(P)
    best = 2
    for _ in range(nlines):
        i, j = random.sample(range(M), 2)
        c = 2
        for k in range(M):
            if k != i and k != j and on_line(P[k], P[i], P[j], q):
                c += 1
        best = max(best, c)
    say("  W sample: M = %d points in P^9 ; %d random lines ; max collinear"
        " count = %d  (need 6)" % (M, nlines, best))
say("=== END part 3 ===")
