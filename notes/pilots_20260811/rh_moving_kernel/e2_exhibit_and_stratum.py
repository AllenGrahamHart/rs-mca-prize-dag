#!/usr/bin/env python3
"""e2_exhibit_and_stratum.py -- rh_moving_kernel (round 33), D1 + D2.

PART A (D1, refutation by exhibition).  One explicit column-far plane at
n=11,k=3,a=5 (r=6, R=8, rho=2, m_P=3 > rho): print the LOW apolar generator
P_gamma at every generic-rank slope and the gcd of K_0 = ker M_0 cap ker M_1.
If round 32's "at least one generator is forced fixed" held, the P_gamma
would all coincide and gcd(K_0) would be that P (degree p_gen).

PART B (D2, the fixed-generator stratum).  Build pencils that DO have a
fixed low generator: y_0, y_1 linear-recurrence sequences with a common
irreducible characteristic polynomial P of degree p.  Verify
  h_r = p, dim K_0 = r+1-p, gcd(K_0) = P, column-far,
and the (MI1)-RESTORATION claim: the residue space
  ker M(gamma) mod P  subset  Lambda = F[x]/(P)
is m_Q-dimensional and is the SHIFT FAMILY of a single u_gamma in Lambda.
Also count bad slopes T against rho.

Stdlib only.  Run under: tools/ramguard local -- python3 <this>
"""
import itertools
import random
import time

T0 = time.time()
OUT = "notes/pilots_20260811/rh_moving_kernel/e2_results.txt"
LINES = []


def emit(s):
    LINES.append(s)
    with open(OUT, "w") as fh:
        fh.write("\n".join(LINES) + "\n")


def inv(x, q):
    return pow(x, q - 2, q)


def build(n, k, q):
    R = n - k
    D = list(range(n))
    v = []
    for x in D:
        p = 1
        for y in D:
            if y != x:
                p = p * (x - y) % q
        v.append(inv(p, q))
    return R, D, v


def syn(f, D, v, R, q):
    return [sum(f[i] * v[i] % q * pow(D[i], m, q) for i in range(len(D))) % q
            for m in range(R)]


def rref(M, q):
    M = [row[:] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    piv = []
    rk = 0
    for c in range(cols):
        p = None
        for i in range(rk, rows):
            if M[i][c]:
                p = i
                break
        if p is None:
            continue
        M[rk], M[p] = M[p], M[rk]
        iv = inv(M[rk][c], q)
        M[rk] = [x * iv % q for x in M[rk]]
        for i in range(rows):
            if i != rk and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[rk][j]) % q for j in range(cols)]
        piv.append(c)
        rk += 1
    return M[:rk], piv


def nullspace(M, q):
    if not M:
        return []
    Rm, piv = rref(M, q)
    cols = len(M[0])
    free = [c for c in range(cols) if c not in piv]
    out = []
    for f in free:
        vv = [0] * cols
        vv[f] = 1
        for i, c in enumerate(piv):
            vv[c] = (-Rm[i][f]) % q
        out.append(vv)
    return out


def cat(y, R, i):
    return [[y[a + b] for b in range(i + 1)] for a in range(R - i)]


def rank(M, q):
    return len(rref(M, q)[0]) if M else 0


def norml(v, q):
    for x in v:
        if x:
            iv = inv(x, q)
            return tuple(t * iv % q for t in v)
    return tuple(v)


def trim(p):
    while p and p[-1] == 0:
        p.pop()
    return p


def polydiv(a, b, q):
    a = a[:]
    db = len(b) - 1
    ivb = inv(b[db], q)
    while len(a) - 1 >= db and any(a):
        da = len(a) - 1
        c = a[da] * ivb % q
        for i in range(db + 1):
            a[da - db + i] = (a[da - db + i] - c * b[i]) % q
        trim(a)
    return a


def polygcd(a, b, q):
    a = trim(a[:])
    b = trim(b[:])
    while b:
        a, b = b, polydiv(a, b, q)
    if a:
        iv = inv(a[-1], q)
        a = [x * iv % q for x in a]
    return a


def locators(n, r, D, q):
    out = []
    for X in itertools.combinations(range(n), r):
        c = [1]
        for j in X:
            c = [0] + c
            for i in range(len(c) - 1):
                c[i] = (c[i] - D[j] * c[i + 1]) % q
        out.append((X, c + [0] * (r + 1 - len(c))))
    return out


def in_span(vec, B, piv, q):
    w = vec[:]
    for i, p in enumerate(piv):
        if w[p]:
            f = w[p]
            w = [(w[j] - f * B[i][j]) % q for j in range(len(w))]
    return not any(w)


def gcd_of_space(basis, q):
    g = []
    for v in basis:
        g = polygcd(g, trim(v[:]), q) if g else trim(v[:])
    return g


# ------------------------------------------------------------------ PART A
def partA(n, k, a, q, tries=400, seed=11):
    random.seed(seed)
    R, D, v = build(n, k, q)
    r = n - a
    LOC = locators(n, r, D, q)
    emit("=== PART A: D1 refutation by exhibition ===")
    emit("cell n=%d k=%d a=%d -> r=%d R=%d rho_expected=%d  r+1-2rho=%d"
         % (n, k, a, r, R, R - r, r + 1 - 2 * (R - r)))
    for _ in range(tries):
        f0 = [random.randrange(q) for _ in range(n)]
        f1 = [random.randrange(q) for _ in range(n)]
        y0 = syn(f0, D, v, R, q)
        y1 = syn(f1, D, v, R, q)
        st = cat(y0, R, r) + cat(y1, R, r)
        K0 = nullspace(st, q)
        if len(K0) != r + 1 - 2 * (R - r):
            continue
        Kr, Kp = rref([w[:] for w in K0], q)
        if any(in_span(c, Kr, Kp, q) for (_, c) in LOC):
            continue                       # column-close
        rows = []
        ok = True
        for g in range(q):
            yg = [(y0[m] + g * y1[m]) % q for m in range(R)]
            if rank(cat(yg, R, r), q) != R - r:
                rows.append((g, None, None))
                continue
            for i in range(1, R + 1):
                ns = nullspace(cat(yg, R, i), q)
                if ns:
                    if len(ns) != 1:
                        ok = False
                    rows.append((g, i, norml(ns[0], q)))
                    break
        if not ok:
            continue
        emit("y_0 = %s" % y0)
        emit("y_1 = %s" % y1)
        emit("dim K_0 = %d ; gcd(K_0) = %s (degree %d)"
             % (len(K0), gcd_of_space(K0, q), len(gcd_of_space(K0, q)) - 1))
        emit("slope | p_gamma | low apolar generator P_gamma (normalised)")
        seen = {}
        for (g, i, P) in rows:
            if i is None:
                emit("%5d | rank-drop slope" % g)
            else:
                emit("%5d | %7d | %s" % (g, i, list(P)))
                seen.setdefault(i, set()).add(P)
        for i in sorted(seen):
            emit("degree %d: %d DISTINCT generators over %d slopes"
                 % (i, len(seen[i]), sum(1 for (_, j, _) in rows if j == i)))
        p_gen = min(seen)
        emit("p_gen = %d, m_P = r+1-p_gen = %d, rho = %d -> round 32 predicts "
             "P FIXED (m_P > rho: %s)"
             % (p_gen, r + 1 - p_gen, R - r, r + 1 - p_gen > R - r))
        emit("MEASURED: %d distinct low generators => P is NOT fixed."
             % len(seen[p_gen]))
        emit("")
        return
    emit("PART A: no witness found")


# ------------------------------------------------------------------ PART B
def irreducibles(p, q):
    """monic irreducible polys of degree p over F_q, coeff list low->high."""
    out = []
    for tail in itertools.product(range(q), repeat=p):
        c = list(tail) + [1]
        if any(sum(c[i] * pow(x, i, q) for i in range(p + 1)) % q == 0
               for x in range(q)):
            continue
        if p >= 4:
            # exclude products of two irreducible quadratics
            red = False
            for b0 in range(q):
                for b1 in range(q):
                    b = [b0, b1, 1]
                    if any(sum(b[i] * pow(x, i, q) for i in range(3)) % q == 0
                           for x in range(q)):
                        continue
                    if not trim(polydiv(c[:], b, q)):
                        red = True
                        break
                if red:
                    break
            if red:
                continue
        out.append(c)
    return out


def recurrence_space(P, R, q):
    """basis of {y in F^R : y satisfies the linear recurrence with char P}."""
    p = len(P) - 1
    basis = []
    for j in range(p):
        y = [0] * p
        y[j] = 1
        for m in range(p, R):
            y.append(-sum(P[i] * y[m - p + i] for i in range(p)) % q)
        basis.append(y[:R])
    return basis


def partB(n, k, a, q, p, ntrials=40, seed=5):
    random.seed(seed)
    R, D, v = build(n, k, q)
    r = n - a
    rho = R - r
    LOC = locators(n, r, D, q)
    irr = irreducibles(p, q)
    emit("=== PART B: the FIXED-GENERATOR stratum ===")
    emit("cell n=%d k=%d a=%d -> r=%d R=%d rho=%d ; P irreducible of degree "
         "p=%d (rho < p <= 2rho: %s) ; m_Q = r+p-R = %d"
         % (n, k, a, r, R, rho, p, rho < p <= 2 * rho, r + p - R))
    emit("monic irreducible degree-%d polys over F_%d: %d" % (p, q, len(irr)))
    m_Q = r + p - R
    tot = far = hr_ok = gcd_ok = shift_ok = 0
    Tmax = -1
    Tvals = {}
    PSTAR = []
    for _ in range(ntrials):
        P = random.choice(irr)
        B = recurrence_space(P, R, q)
        c0 = [random.randrange(q) for _ in range(p)]
        c1 = [random.randrange(q) for _ in range(p)]
        y0 = [sum(c0[j] * B[j][m] for j in range(p)) % q for m in range(R)]
        y1 = [sum(c1[j] * B[j][m] for j in range(p)) % q for m in range(R)]
        st = cat(y0, R, r) + cat(y1, R, r)
        if rank(st, q) != p:
            continue
        tot += 1
        hr_ok += 1
        K0 = nullspace(st, q)
        g = gcd_of_space(K0, q)
        if g == P:
            gcd_ok += 1
        Kr, Kp = rref([w[:] for w in K0], q)
        if any(in_span(c, Kr, Kp, q) for (_, c) in LOC):
            continue
        far += 1
        ps = next(i for i in range(1, R + 1)
                  if rank(cat(y0, R, i) + cat(y1, R, i), q) < i + 1)
        pgs = set()
        for gm in range(q):
            yg = [(y0[m] + gm * y1[m]) % q for m in range(R)]
            if rank(cat(yg, R, r), q) != rho:
                continue
            for i in range(1, R + 1):
                if nullspace(cat(yg, R, i), q):
                    pgs.add(i)
                    break
        PSTAR.append((ps, min(pgs) if pgs else None))
        # residue space of the kernel mod P, per slope; shift-family test
        allshift = True
        T = 0
        for gm in range(q):
            yg = [(y0[m] + gm * y1[m]) % q for m in range(R)]
            ns = nullspace(cat(yg, R, r), q)
            if not ns:
                continue
            res = []
            for w in ns:
                res.append(polydiv(trim(w[:]) or [0], P, q) + [0] * p)
            res = [t[:p] for t in res]
            Rr, Rp = rref([t[:] for t in res], q)
            if len(Rr) != m_Q:
                allshift = False
                continue
            # search the residue space for a generator u with
            # {u, x u, ..., x^{m_Q-1} u} = the whole space (shift family).
            found = False
            for co in itertools.product(range(q), repeat=m_Q):
                if not any(co):
                    continue
                u = [sum(co[i] * Rr[i][j] for i in range(m_Q)) % q
                     for j in range(p)]
                sh = []
                cur = u[:]
                for _j in range(m_Q):
                    sh.append(cur[:])
                    cur = (polydiv([0] + cur, P, q) + [0] * p)[:p]
                if rank(sh, q) == m_Q and all(
                        in_span(t, Rr, Rp, q) for t in sh):
                    found = True
                    break
            if not found:
                allshift = False
            Nr, Np = rref([w[:] for w in ns], q)
            for (_, c) in LOC:
                if in_span(c, Nr, Np, q):
                    T += 1
                    break
        if allshift:
            shift_ok += 1
        Tmax = max(Tmax, T)
        Tvals[T] = Tvals.get(T, 0) + 1
    emit("pencils with rank[M_0;M_1] = p : %d" % hr_ok)
    emit("gcd(K_0) = P                   : %d / %d" % (gcd_ok, tot))
    emit("column-far                     : %d / %d" % (far, tot))
    emit("kernel residues mod P are a SHIFT FAMILY of one u_gamma, "
         "dim m_Q=%d, at every generic slope : %d / %d"
         % (m_Q, shift_ok, far))
    emit("(p*, p_gen) observed: %s   [P is the low generator and is fixed "
         "iff p* = p_gen = p = %d]" % (sorted(set(PSTAR)), p))
    emit("bad-slope counts T: %s ; max T = %d ; rho = %d ; r+1 = %d ; "
         "T <= rho: %s ; T <= p: %s"
         % (sorted(Tvals.items()), Tmax, rho, r + 1, Tmax <= rho, Tmax <= p))
    emit("")


if __name__ == "__main__":
    partA(11, 3, 5, 13)
    partB(11, 3, 5, 13, 4)
    partB(11, 3, 5, 13, 3)
    partB(12, 3, 5, 13, 4)
    emit("wall %.1fs" % (time.time() - T0))
