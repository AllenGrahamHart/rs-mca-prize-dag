#!/usr/bin/env python3
"""r35_fg_razor D1: faithful small-scale replicas of the razor witnesses.

Two families, same cells:
  FG  = witness-B replica  (P* = P_1 P_2, P_1 irreducible of degree rho,
        P_2 squarefree of degree rho, coprime; y_j = impulse responses)
  LB1 = the banked lower-bound family (e_1 = 1_T, e_0 = -lam.1_T on T,
        |T| = r+1, lam(t) = t)   [crossing_location:635-645]

Conventions (round 33/34):  v_x = 1/prod_{y!=x}(x-y) over D;
  y_m = sum_x e(x) v_x x^m ;  M_i(y) = (y_{s+j}), 0<=s<R-i, 0<=j<=i ;
  low-to-high coefficient order ; column-far  <=>  K_0 ^ D_r(D) = {}.
Cells all satisfy 4rho < R  (the separating regime, ZP-2).
Stdlib only.
"""
import sys
from itertools import combinations

OUT = []


def emit(s=""):
    OUT.append(str(s))
    print(s)
    sys.stdout.flush()


# ---------- F_p linear algebra ----------
def inv(a, p):
    return pow(a % p, p - 2, p)


def rref(M, p):
    """Return (rref matrix, pivot columns). M is a list of rows."""
    M = [row[:] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    piv = []
    r = 0
    for c in range(cols):
        pr = None
        for i in range(r, rows):
            if M[i][c] % p:
                pr = i
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        iv = inv(M[r][c], p)
        M[r] = [(x * iv) % p for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(cols)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return M, piv


def rank(M, p):
    if not M:
        return 0
    return len(rref(M, p)[1])


def nullspace(M, p, ncols=None):
    """Basis of {v : M v = 0} as list of vectors of length ncols."""
    if ncols is None:
        ncols = len(M[0])
    if not M:
        return [[1 if i == j else 0 for i in range(ncols)] for j in range(ncols)]
    Rm, piv = rref(M, p)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-Rm[i][f]) % p
        basis.append(v)
    return basis


# ---------- polynomials over F_p (low-to-high) ----------
def ptrim(a, p):
    a = [x % p for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b, p):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] = (out[i + j] + ai * bj) % p
    return ptrim(out, p)


def pmod(a, m, p):
    a = ptrim(a, p)
    m = ptrim(m, p)
    dm = len(m) - 1
    iv = inv(m[-1], p)
    while len(a) - 1 >= dm and a:
        f = (a[-1] * iv) % p
        sh = len(a) - 1 - dm
        for i in range(dm + 1):
            a[sh + i] = (a[sh + i] - f * m[i]) % p
        a = ptrim(a, p)
    return a


def pgcd(a, b, p):
    a, b = ptrim(a[:], p), ptrim(b[:], p)
    while b:
        a, b = b, pmod(a, b, p)
    if a:
        iv = inv(a[-1], p)
        a = [(x * iv) % p for x in a]
    return a


def pdiff(a, p):
    return ptrim([(i * a[i]) % p for i in range(1, len(a))], p)


def is_irreducible(f, p):
    """f monic, deg d >= 1: Rabin-style via x^(p^i) mod f."""
    d = len(f) - 1
    if d <= 0:
        return False
    if d == 1:
        return True
    # x^(p^d) == x  and  gcd(x^(p^(d/l)) - x, f) == 1 for prime l | d
    def xpow_frob(k):
        # returns x^(p^k) mod f
        cur = [0, 1]
        for _ in range(k):
            # raise to p-th power by repeated squaring on exponent p
            e = p
            res = [1]
            base = cur[:]
            while e:
                if e & 1:
                    res = pmod(pmul(res, base, p), f, p)
                base = pmod(pmul(base, base, p), f, p)
                e >>= 1
            cur = res
        return cur
    xd = xpow_frob(d)
    if ptrim([(xd[i] if i < len(xd) else 0) - (1 if i == 1 else 0)
              for i in range(max(len(xd), 2))], p):
        return False
    dd = d
    primes = set()
    m = d
    f2 = 2
    while f2 * f2 <= m:
        while m % f2 == 0:
            primes.add(f2)
            m //= f2
        f2 += 1
    if m > 1:
        primes.add(m)
    for l in primes:
        xk = xpow_frob(dd // l)
        g = pgcd(ptrim([(xk[i] if i < len(xk) else 0) - (1 if i == 1 else 0)
                        for i in range(max(len(xk), 2))], p), f, p)
        if len(g) - 1 != 0:
            return False
    return True


def find_irreducible(deg, p):
    """Smallest monic irreducible of given degree, lexicographic on coeffs."""
    total = p ** deg
    for code in range(total):
        c = []
        t = code
        for _ in range(deg):
            c.append(t % p)
            t //= p
        f = c + [1]
        if is_irreducible(f, p):
            return f
    return None


# ---------- cell machinery ----------
def dual_mults(D, p):
    v = []
    for x in D:
        pr = 1
        for y in D:
            if y != x:
                pr = (pr * (x - y)) % p
        v.append(inv(pr, p))
    return v


def syn_from_error(err, D, v, R, p):
    """err: dict x -> value. y_m = sum_x err(x) v_x x^m."""
    y = []
    for m in range(R):
        s = 0
        for idx, x in enumerate(D):
            e = err.get(x, 0)
            if e:
                s = (s + e * v[idx] * pow(x, m, p)) % p
        y.append(s % p)
    return y


def hankel(y, i, R, p):
    return [[y[s + j] % p for j in range(i + 1)] for s in range(R - i)]


def stacked(y0, y1, i, R, p):
    return hankel(y0, i, R, p) + hankel(y1, i, R, p)


def ann_dim(y0, y1, i, R, p):
    M = stacked(y0, y1, i, R, p)
    return (i + 1) - rank(M, p)


def pstar(y0, y1, R, p, hi):
    for i in range(1, hi + 1):
        if ann_dim(y0, y1, i, R, p) > 0:
            return i
    return None


def poly_from_roots(rs, p):
    f = [1]
    for a in rs:
        f = pmul(f, [(-a) % p, 1], p)
    return f


def gcd_of_space(basis, p):
    g = []
    for v in basis:
        g = pgcd(g, ptrim(v[:], p), p) if g else ptrim(v[:], p)
        if len(g) - 1 == 0:
            break
    return g


def is_D_split_squarefree(f, D, p):
    """f (monic, deg d) splits into distinct linear factors over D."""
    d = len(f) - 1
    if d == 0:
        return True
    roots = [x for x in D if not ptrim(pmod(f[:], [(-x) % p, 1], p), p)]
    if len(roots) != d:
        return False
    return len(set(roots)) == d


def column_far(K0basis, D, r, p):
    """True iff no monic squarefree degree-r D-split poly lies in span(K0)."""
    if not K0basis:
        return True
    Rm, piv = rref([b[:] for b in K0basis], p)
    ncols = len(K0basis[0])
    for S in combinations(D, r):
        sig = poly_from_roots(S, p)
        vec = sig + [0] * (ncols - len(sig))
        # reduce vec against Rm
        w = vec[:]
        for i, c in enumerate(piv):
            if w[c] % p:
                f = w[c]
                w = [(w[j] - f * Rm[i][j]) % p for j in range(ncols)]
        if not any(x % p for x in w):
            return False
    return True


def impulse(P, R, p):
    """Impulse response of monic P (deg d): u_0..u_{d-2}=0, u_{d-1}=1."""
    d = len(P) - 1
    u = [0] * (d - 1) + [1]
    while len(u) < R:
        m = len(u)
        s = 0
        for j in range(d):
            s = (s + P[j] * u[m - d + j]) % p
        u.append((-s) % p)
    return u[:R]


# ---------- experiments ----------
CELLS = [
    # (q, n, k, r)  with D = {0..n-1};  R = n-k, rho = R-r, need 4rho < R
    (11, 11, 1, 8),
    (13, 13, 1, 10),
    (17, 17, 1, 13),
    (19, 19, 1, 15),
    (23, 23, 1, 19),
]


def analyse(tag, y0, y1, cell, p, D, v, R, r, rho, extra=None):
    q, n, k, _ = cell
    hr = rank(stacked(y0, y1, r, R, p), p)
    K0 = nullspace(stacked(y0, y1, r, R, p), p, ncols=r + 1)
    dimK0 = len(K0)
    ps = pstar(y0, y1, R, p, r)
    g = gcd_of_space(K0, p) if K0 else []
    degg = len(g) - 1 if g else -1
    principal = (dimK0 == r + 1 - degg) and degg >= 0 and dimK0 > 0
    # verify principality honestly: K0 == g * F[x]_{<= r-degg}
    if degg >= 0 and dimK0 > 0:
        shifts = []
        for s in range(r - degg + 1):
            vec = [0] * s + g[:]
            vec = vec + [0] * (r + 1 - len(vec))
            shifts.append(vec)
        principal = (rank(shifts, p) == dimK0 and
                     rank(shifts + [b[:] for b in K0], p) == dimK0)
    else:
        principal = False
    isFG = principal and ps is not None and ps <= 2 * rho and hr == ps
    cf = column_far(K0, D, r, p)
    emit("  [%s] q=%d n=%d k=%d r=%d R=%d rho=%d  4rho<R:%s" %
         (tag, q, n, k, r, R, rho, 4 * rho < R))
    emit("      p*=%s  h_r=%d  dimK0=%d (generic r+1-2rho=%d)  deg gcd(K0)=%d"
         "  principal=%s  FG=%s  column-far=%s" %
         (ps, hr, dimK0, r + 1 - 2 * rho, degg, principal, isFG, cf))
    if extra:
        emit("      " + extra)
    return dict(tag=tag, q=q, r=r, R=R, rho=rho, pstar=ps, hr=hr,
                dimK0=dimK0, degg=degg, principal=principal, FG=isFG, cf=cf,
                K0=K0, g=g)


def key_equation_probe(y0, y1, cell, p, D, v, R, r, rho, Pstar):
    """D-1 (DOF) and D-2 (codim U_gamma = rho) and FG5 shift family."""
    pdeg = len(Pstar) - 1
    mQ = pdeg - rho
    rows = []
    dofs = []
    codims = []
    shiftok = 0
    shifttot = 0
    for gam in range(p):
        yg = [(y0[m] + gam * y1[m]) % p for m in range(R)]
        M = hankel(yg, r, R, p)
        rk = rank(M, p)
        Kg = nullspace(M, p, ncols=r + 1)
        dof = len(Kg)
        dofs.append((gam, rk, dof))
        # U_gamma = Kg mod P*  inside Lambda = F[x]/(P*)
        red = []
        for b in Kg:
            red.append(pmod(b[:], Pstar, p) + [0] * pdeg)
            red[-1] = red[-1][:pdeg]
        du = rank(red, p)
        codims.append(pdeg - du)
        # FG5: is U_gamma a shift family u*Lambda_{<mQ} for some u in U_gamma?
        if du == mQ and mQ >= 1:
            Ub, Upiv = rref([x[:] for x in red], p)
            Ub = Ub[:du]
            shifttot += 1
            found = False
            # search over the space (round 33 miss 6: not an arbitrary basis vector)
            for code in range(1, p ** du):
                co = []
                t = code
                for _ in range(du):
                    co.append(t % p)
                    t //= p
                u = [0] * pdeg
                for i, c in enumerate(co):
                    if c:
                        for j in range(pdeg):
                            u[j] = (u[j] + c * Ub[i][j]) % p
                fam = []
                for s in range(mQ):
                    w = pmod(pmul(u, [0] * s + [1], p), Pstar, p)
                    w = w + [0] * pdeg
                    fam.append(w[:pdeg])
                if rank(fam, p) == mQ and rank(fam + [x[:] for x in red], p) == mQ:
                    found = True
                    break
            if found:
                shiftok += 1
    ranks = sorted(set(x[1] for x in dofs))
    dofset = sorted(set(x[2] for x in dofs))
    emit("      key-eq: rank M(gamma) in %s (rho=%d); dim ker in %s"
         "  [predicted (r+1)+m_Q-p = r+1-rho = %d]" %
         (ranks, rho, dofset, r + 1 - rho))
    emit("      codim U_gamma in Lambda: %s   [D-2 predicts rho=%d];"
         "  m_Q = p-rho = %d ; FG5 shift family %d/%d" %
         (sorted(set(codims)), rho, mQ, shiftok, shifttot))
    return dofs, codims, (shiftok, shifttot)


def main():
    emit("=== r35_fg_razor  e1_replica  (D1 structure) ===")
    emit("")
    results = []
    for cell in CELLS:
        q, n, k, r = cell
        p = q
        D = list(range(n))
        R = n - k
        rho = R - r
        a = n - r
        v = dual_mults(D, p)
        emit("CELL q=%d n=%d k=%d a=%d r=%d R=%d rho=%d  (4rho=%d < R=%d : %s)"
             % (q, n, k, a, r, R, rho, 4 * rho, R, 4 * rho < R))
        # ---- FG replica of witness B ----
        P1 = find_irreducible(rho, p)
        # P2: rho distinct linear factors over D, coprime to P1
        P2 = poly_from_roots(list(range(rho)), p)
        Pstar = pmul(P1, P2, p)
        y0 = impulse(P1, R, p)
        y1 = impulse(P2, R, p)
        sq = (len(pgcd(Pstar, pdiff(Pstar, p), p)) - 1 == 0)
        info = ("P_1 = %s (irred deg %d, irreducible=%s); P_2 = %s;"
                " P* squarefree=%s; deg P* = %d = 2rho" %
                (P1, rho, is_irreducible(P1, p), P2, sq, len(Pstar) - 1))
        rFG = analyse("FG(witness B)", y0, y1, cell, p, D, v, R, r, rho, info)
        rFG["Pstar"] = Pstar
        if rFG["FG"]:
            key_equation_probe(y0, y1, cell, p, D, v, R, r, rho, Pstar)
        # negative control B': P_1 replaced by a D-split squarefree factor
        P1b = poly_from_roots(list(range(rho, 2 * rho)), p)
        Pb = pmul(P1b, P2, p)
        y0b = impulse(P1b, R, p)
        rB = analyse("B' control (D-split)", y0b, y1, cell, p, D, v, R, r, rho,
                     "P_1' = %s (D-split squarefree)" % (P1b,))
        # ---- LB1 replica ----
        T = list(range(r + 1))
        err1 = {t: 1 for t in T}
        err0 = {t: (-t) % p for t in T}
        z1 = syn_from_error(err1, D, v, R, p)
        z0 = syn_from_error(err0, D, v, R, p)
        rLB = analyse("LB1", z0, z1, cell, p, D, v, R, r, rho,
                      "T = %s (|T| = r+1 = %d), lam(t) = t" % (T, r + 1))
        emit("      LB1 predictions: h_r = rho+1 = %d ; dim K_0 = r-rho = %d ;"
             " p* = ceil((R+2)/2) = %d ; p_gen = floor((R+1)/2) = %d ;"
             " 2rho = %d ; floor(R/2) = %d" %
             (rho + 1, r - rho, (R + 2 + 1) // 2, (R + 1) // 2, 2 * rho, R // 2))
        results.append((cell, rFG, rB, rLB))
        emit("")
    emit("=== SUMMARY TABLE ===")
    emit("cell(q,n,k,r) | family | p* | h_r | dimK0 | deggcd | princ | FG | colfar")
    for cell, rFG, rB, rLB in results:
        for rr in (rFG, rB, rLB):
            emit("%-14s | %-20s | %s | %s | %s | %s | %s | %s | %s" %
                 (str(cell), rr["tag"], rr["pstar"], rr["hr"], rr["dimK0"],
                  rr["degg"], rr["principal"], rr["FG"], rr["cf"]))
    with open("notes/pilots_20260811/r35_fg_razor/e1_results.txt", "w") as fh:
        fh.write("\n".join(OUT) + "\n")


main()
