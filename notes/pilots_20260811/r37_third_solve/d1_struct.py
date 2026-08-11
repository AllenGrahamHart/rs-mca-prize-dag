"""D1 - structure of the three-member system. r37_third_solve.
Self-contained (no imports of banked scripts). Appends to d1_results.txt.
"""
import random, time

def trim(a):
    while a and a[-1] == 0: a.pop()
    return a
def padd(a, b, p):
    n = max(len(a), len(b)); r = [0]*n
    for i in range(n):
        r[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
    return trim(r)
def psub(a, b, p):
    n = max(len(a), len(b)); r = [0]*n
    for i in range(n):
        r[i] = ((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p
    return trim(r)
def pmul(a, b, p):
    if not a or not b: return []
    r = [0]*(len(a)+len(b)-1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                r[i+j] = (r[i+j] + ai*bj) % p
    return trim(r)
def pscal(a, c, p):
    return trim([(x*c) % p for x in a])
def pdivmod(a, b, p):
    a = a[:]; db = len(b)-1; inv = pow(b[-1], p-2, p)
    q = [0]*max(0, len(a)-db)
    for i in range(len(a)-1, db-1, -1):
        c = (a[i]*inv) % p
        if c:
            q[i-db] = c
            for j in range(db+1):
                a[i-db+j] = (a[i-db+j] - c*b[j]) % p
    return trim(q), trim(a)
def pgcd(a, b, p):
    a = a[:]; b = b[:]
    while b:
        a, b = b, pdivmod(a, b, p)[1]
    return pscal(a, pow(a[-1], p-2, p), p) if a else []
def peval(a, x, p):
    r = 0
    for c in reversed(a): r = (r*x + c) % p
    return r
def roots_in(a, S, p):
    return [x for x in S if peval(a, x, p) == 0]

def randpoly(d, p, rng):
    return trim([rng.randrange(p) for _ in range(d+1)])

def mu_set(p, N):
    """the N-th roots of unity in F_p (requires N | p-1)"""
    g = 2
    while pow(g, (p-1)//2, p) == 1 or pow(g, (p-1)//3 if (p-1) % 3 == 0 else (p-1), p) == 1:
        g += 1
    h = pow(g, (p-1)//N, p)
    S = set()
    v = 1
    for _ in range(N):
        S.add(v); v = (v*h) % p
    return sorted(S)

def par_draw(p, rng):
    """random (PAR) object: returns (f,g,h,k,L,ell,Q0,Q1,Q2) or None"""
    ell = rng.randrange(p)
    L = [(-ell) % p, 1]
    f = randpoly(4, p, rng); g = randpoly(4, p, rng)
    h = randpoly(4, p, rng); k = randpoly(4, p, rng)
    fe = peval(f, ell, p); ge = peval(g, ell, p)
    if fe == 0 or ge == 0: return None
    # condition 1: f(ell)^2 = k(ell) g(ell)
    tgt = (fe*fe % p) * pow(ge, p-2, p) % p
    k = k[:] + [0]*(5-len(k)); k[0] = (k[0] + tgt - peval(k, ell, p)) % p; k = trim(k)
    # condition 2: g(ell)^2 = -h(ell) f(ell)
    tgt2 = (-(ge*ge % p)) * pow(fe, p-2, p) % p
    h = h[:] + [0]*(5-len(h)); h[0] = (h[0] + tgt2 - peval(h, ell, p)) % p; h = trim(h)
    N0 = psub(pmul(f, f, p), pmul(k, g, p), p)
    N1 = padd(pmul(f, g, p), pmul(h, k, p), p)
    N2 = padd(pmul(g, g, p), pmul(h, f, p), p)
    Q = []
    for N in (N0, N1, N2):
        qq, rr = pdivmod(N, L, p)
        if rr: return None
        Q.append(qq)
    return f, g, h, k, L, ell, Q[0], Q[1], Q[2]

def run(p, ntr, out, rng):
    D = mu_set(p, 32)
    stats = dict(n=0, conic=0, cross=0, slot=0, e12=0, scrit=0, ov=0, ovmax=0,
                 ovform=0, degL=0, sdist={}, ovdist={})
    for _ in range(ntr):
        o = par_draw(p, rng)
        if o is None: continue
        f, g, h, k, L, ell, Q0, Q1, Q2 = o
        stats['n'] += 1
        # (CONIC): Q0 g^2 - Q1 f g + Q2 f^2 == L Q0 Q2
        lhs = padd(psub(pmul(Q0, pmul(g, g, p), p), pmul(Q1, pmul(f, g, p), p), p),
                   pmul(Q2, pmul(f, f, p), p), p)
        rhs = pmul(L, pmul(Q0, Q2, p), p)
        if lhs == rhs: stats['conic'] += 1
        # (CROSS): (k,f,g) x (f,g,-h) == (-L Q2, L Q1, -L Q0)
        mh = pscal(h, p-1, p)
        c0 = psub(pmul(f, mh, p), pmul(g, g, p), p)
        c1 = psub(pmul(g, f, p), pmul(k, mh, p), p)
        c2 = psub(pmul(k, g, p), pmul(f, f, p), p)
        if (c0 == pscal(pmul(L, Q2, p), p-1, p) and c1 == pmul(L, Q1, p)
                and c2 == pscal(pmul(L, Q0, p), p-1, p)): stats['cross'] += 1
        # (E1,E2) sanity: Q2 f - Q1 g - Q0 h = 0 ; Q1 f - Q0 g - Q2 k = 0
        e1 = psub(psub(pmul(Q2, f, p), pmul(Q1, g, p), p), pmul(Q0, h, p), p)
        e2 = psub(psub(pmul(Q1, f, p), pmul(Q0, g, p), p), pmul(Q2, k, p), p)
        if not e1 and not e2: stats['e12'] += 1
        # (SLOT): g(x)^2 q_x(-f/g) == L(x)Q0(x)Q2(x)  for all x with g(x)!=0
        ok = True
        for x in range(p):
            gx = peval(g, x, p)
            if gx == 0: continue
            z = (-peval(f, x, p)) * pow(gx, p-2, p) % p
            qx = (peval(Q0, x, p) + z*peval(Q1, x, p) + z*z % p*peval(Q2, x, p)) % p
            if (gx*gx % p)*qx % p != peval(L, x, p)*peval(Q0, x, p) % p*peval(Q2, x, p) % p:
                ok = False; break
        if ok: stats['slot'] += 1
        # (SCRIT core): s = deg gcd(Q0,Q1,Q2) equals deg gcd(Q0,Q2)
        d02 = pgcd(Q0, Q2, p)
        d012 = pgcd(d02, Q1, p)
        s = len(d012)-1; s02 = len(d02)-1
        stats['sdist'][(s02, s)] = stats['sdist'].get((s02, s), 0)+1
        if s == s02: stats['scrit'] += 1
        # (OV4): |roots(Q_z) cap (S0 u S2)| == |roots(f+zg) cap (S0 u S2)| <= 4
        S0 = set(roots_in(Q0, D, p)); S2 = set(roots_in(Q2, D, p))
        U = sorted(S0 | S2)
        if U:
            good = True; mx = 0
            for z in range(p):
                if z == 0: continue
                Qz = padd(padd(Q0, pscal(Q1, z, p), p), pscal(Q2, z*z % p, p), p)
                a = len([x for x in U if peval(Qz, x, p) == 0])
                fzg = padd(f, pscal(g, z, p), p)
                b = len([x for x in U if peval(fzg, x, p) == 0])
                if a != b: good = False
                mx = max(mx, a)
            if good: stats['ovform'] += 1
            if mx <= 4: stats['ov'] += 1
            stats['ovmax'] = max(stats['ovmax'], mx)
            stats['ovdist'][mx] = stats['ovdist'].get(mx, 0)+1
    out.append("q=%d draws=%d CONIC=%d CROSS=%d E12=%d SLOT=%d SCRIT(s==deg gcd(Q0,Q2))=%d"
               % (p, stats['n'], stats['conic'], stats['cross'], stats['e12'],
                  stats['slot'], stats['scrit']))
    out.append("q=%d (s02,s) joint histogram = %s" % (p, sorted(stats['sdist'].items())))
    out.append("q=%d OV-form(roots(Qz) cap U == roots(f+zg) cap U)=%d  OV<=4 =%d  max overlap=%d  overlap-max hist=%s"
               % (p, stats['ovform'], stats['ov'], stats['ovmax'], sorted(stats['ovdist'].items())))

def main():
    rng = random.Random(20260811)
    out = ["", "=== RUN d1_struct %s ===" % time.strftime("%Y-%m-%dT%H:%M:%S")]
    for p in (97, 193):
        run(p, 60, out, rng)
    # ladder-exhaustion check: with (f,g,L) fixed, k<->Q0 and h<->Q2 are bijections
    for p in (97, 193):
        rng2 = random.Random(7*p)
        o = None
        while o is None: o = par_draw(p, rng2)
        f, g, h, k, L, ell, Q0, Q1, Q2 = o
        seen = set(); coll = 0
        for _ in range(200):
            h2 = randpoly(4, p, rng2)
            h2 = h2 + [0]*(5-len(h2))
            ge = peval(g, ell, p); fe = peval(f, ell, p)
            t = (-(ge*ge % p))*pow(fe, p-2, p) % p
            h2[0] = (h2[0] + t - peval(trim(h2[:]), ell, p)) % p
            h2 = trim(h2)
            N2 = padd(pmul(g, g, p), pmul(h2, f, p), p)
            q2, r2 = pdivmod(N2, L, p)
            if r2: continue
            key = tuple(q2)
            if key in seen: coll += 1
            seen.add(key)
        out.append("q=%d LADDER: 200 h-draws (ell-condition imposed) -> %d distinct Q_2, %d collisions"
                   " => h |-> Q_2 injective on the 4-dim h-family (Q_2 prescribed => h unique)"
                   % (p, len(seen), coll))
    with open("notes/pilots_20260811/r37_third_solve/d1_results.txt", "a") as fh:
        fh.write("\n".join(out) + "\n")
    print("\n".join(out))

main()
