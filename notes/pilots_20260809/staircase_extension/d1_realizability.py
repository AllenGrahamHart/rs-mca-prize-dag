"""D1: the Hankel origin is what cuts the design cap down.

The design functional Tmax_cf (max core-free collinear split locators)
saturates its incidence cap at several rows.  This script tests whether
those saturating LINES are Hankel-realizable, i.e. whether the linear
system

    M_r(y_0 + Z y_1) . (q_0 + Z q_1) = 0   in F[Z]

has a nonzero solution (y_0,y_1) in F^(2R), and if so whether the
resulting pencil is column-far with the advertised supported-slope
count.

Rows tested:
  (a) N=16, R=8,  r=rho=3, q=17  : the PROVED m=1 fence 5-line  -> expect realizable
  (b) N=28, R=14, r=rho=3, q=29  : the saturating 9-line        -> (ERC2) caps a
      realizable A=9 pencil at T<=7, so a realizable 9-line would contradict a
      PROVED node; expect NOT realizable
  (c) N=12, R=6,  r=rho=3, q=13  : the cyclotomic family X^3-c  -> A=1 profile

Stdlib only.  Run under tools/ramguard.
"""
import itertools


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


def poly_from_roots(S, q):
    c = [1]
    for x in S:
        nc = [0] * (len(c) + 1)
        for i, ci in enumerate(c):
            nc[i] = (nc[i] - x * ci) % q
            nc[i + 1] = (nc[i + 1] + ci) % q
        c = nc
    return c                      # ascending, monic, length rho+1


def rref(M, q):
    M = [row[:] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    piv, r = [], 0
    for c in range(cols):
        p = None
        for i in range(r, rows):
            if M[i][c] % q:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        iv = pow(M[r][c], q - 2, q)
        M[r] = [v * iv % q for v in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % q:
                f = M[i][c]
                M[i] = [(M[i][t] - f * M[r][t]) % q for t in range(cols)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return M, piv


def kernel(M, q, cols):
    if not M:
        return [[1 if t == j else 0 for t in range(cols)] for j in range(cols)]
    Mr, piv = rref(M, q)
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = [0] * cols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-Mr[i][f]) % q
        basis.append(v)
    return basis


def realizability(q0, q1, Rv, rv, q):
    """nullity of the (3(R-r)) x (2R) system, and a basis."""
    rows = []
    m = Rv - rv
    for deg in range(3):
        for i in range(m):
            row = [0] * (2 * Rv)
            for j in range(rv + 1):
                if deg == 0:
                    row[i + j] = (row[i + j] + q0[j]) % q
                elif deg == 1:
                    row[i + j] = (row[i + j] + q1[j]) % q
                    row[Rv + i + j] = (row[Rv + i + j] + q0[j]) % q
                else:
                    row[Rv + i + j] = (row[Rv + i + j] + q1[j]) % q
            rows.append(row)
    return kernel(rows, q, 2 * Rv)


def hankel(y, Rv, rv, q):
    return [[y[i + j] % q for j in range(rv + 1)] for i in range(Rv - rv)]


def is_split(vec, D, q, rho):
    if vec[rho] % q == 0:
        return None
    iv = pow(vec[rho], q - 2, q)
    c = [v * iv % q for v in vec]
    roots = [x for x in D if sum(c[i] * pow(x, i, q) for i in range(rho + 1)) % q == 0]
    return tuple(roots) if len(roots) == rho else None


def report(name, sups, q, N, Rv, rv):
    D = subgroup(q, N)
    polys = [poly_from_roots(S, q) for S in sups]
    # the line through the first two; verify all lie on it
    p0, p1 = polys[0], polys[1]
    direction = [(p1[i] - p0[i]) % q for i in range(rv + 1)]
    onit = True
    params = []
    for p in polys:
        # p = p0 + t*direction ?
        t = None
        for i in range(rv + 1):
            if direction[i] % q:
                t = (p[i] - p0[i]) * pow(direction[i], q - 2, q) % q
                break
        if any((p0[i] + t * direction[i] - p[i]) % q for i in range(rv + 1)):
            onit = False
        params.append(t)
    say("%s: N=%d R=%d r=rho=%d q=%d  #locators=%d  collinear=%s"
        % (name, N, Rv, rv, q, len(sups), onit))
    say("   line parameters (slopes up to affine change): %s" % params)
    A = Rv + 1 - 2 * rv
    erc2 = (N * 1 + rv - A * 1) // rv
    say("   A = R+1-2rho = %d ; (ERC2) cap at e=1,s=0 : T <= %d ; "
        "design count = %d" % (A, erc2, len(sups)))
    sols = realizability(p0, direction, Rv, rv, q)
    say("   Hankel realizability: nullity of the %dx%d system = %d"
        % (3 * (Rv - rv), 2 * Rv, len(sols)))
    if not sols:
        say("   => NOT Hankel-realizable: the design line is not a syndrome "
            "pencil.  The counting cap is attained by a NON-Hankel object.")
        return
    for idx, sol in enumerate(sols[:3]):
        y0, y1 = sol[:Rv], sol[Rv:]
        if all(v == 0 for v in sol):
            continue
        common = kernel(hankel(y0, Rv, rv, q) + hankel(y1, Rv, rv, q), q, rv + 1)
        colfar = True
        for coeffs in itertools.product(range(q), repeat=len(common)):
            if all(c == 0 for c in coeffs):
                continue
            v = [sum(coeffs[t] * common[t][s] for t in range(len(common))) % q
                 for s in range(rv + 1)]
            if is_split(v, D, q, rv):
                colfar = False
                break
        T = 0
        for g in range(q):
            yy = [(y0[t] + g * y1[t]) % q for t in range(Rv)]
            ker = kernel(hankel(yy, Rv, rv, q), q, rv + 1)
            hit = False
            for coeffs in itertools.product(range(q), repeat=len(ker)):
                if all(c == 0 for c in coeffs):
                    continue
                v = [sum(coeffs[t] * ker[t][s] for t in range(len(ker))) % q
                     for s in range(rv + 1)]
                if is_split(v, D, q, rv):
                    hit = True
                    break
            if hit:
                T += 1
        say("   solution %d: column-far=%s  supported finite slopes T=%d "
            "(target T<=rho+1=%d)" % (idx, colfar, T, rv + 1))


say("=== (a) N=16 q=17 : the PROVED fence 5-line ===")
report("fence 5-line", [(1, 2, 5), (3, 7, 11), (9, 12, 13), (4, 6, 16),
                        (8, 10, 15)], 17, 16, 8, 3)
say()
say("=== (b) N=28 q=29 : the saturating design 9-line ===")
report("design 9-line", [(1, 2, 5), (3, 6, 7), (4, 16, 21), (9, 17, 23),
                         (10, 19, 26), (11, 18, 27), (12, 13, 22),
                         (14, 20, 28), (15, 24, 25)], 29, 28, 14, 3)
say()
say("=== (c) N=12 q=13 : the cyclotomic family X^3 - c ===")
D12 = subgroup(13, 12)
cubes = sorted({pow(x, 3, 13) for x in D12})
sups = []
for c in cubes:
    S = tuple(sorted(x for x in D12 if pow(x, 3, 13) == c))
    sups.append(S)
say("cube classes: %s" % (sups,))
report("cyclotomic 4-line", sups, 13, 12, 6, 3)
say("=== END ===")
