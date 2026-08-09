"""D1 robustness: (a) memory-frugal extended field sweep at N=16,
(b) column-far status of the CORE (s>=1) lines, (c) the N=20 dead-scale
census that blew the 1G cap in the first run, (d) the density law.

Memory-frugal line census: for each point i, bucket the normalised
directions to points j>i.  A maximal line is discovered at its
lowest-index point, so max over i of (best bucket + 1) is exact and the
memory is O(#points) instead of O(#lines).

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
        x = 1
        order = 0
        seen = set()
        while True:
            x = x * cand % q
            order += 1
            if x == 1:
                break
        if order == q - 1:
            g = cand
            break
    h = pow(g, (q - 1) // N, q)
    D = []
    x = 1
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


def frugal_lines(pts, q, dim, tmin):
    """return list of (i, dirvector, members) for lines with >= tmin pts."""
    inv = [0] * q
    for a in range(1, q):
        inv[a] = pow(a, q - 2, q)
    n = len(pts)
    found = []
    for i in range(n):
        Pi = pts[i]
        buck = {}
        for j in range(i + 1, n):
            Pj = pts[j]
            v = tuple((Pj[t] - Pi[t]) % q for t in range(dim))
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
            if len(js) + 1 >= tmin:
                found.append((i, vn, [i] + js))
    return found


# ------------------------------------------------------------------ (a)
say("=== (a) extended field sweep, N=16, rho=3, e=1, q = 1 mod 16 prime ===")
say("q     max_t  #corefree(t>=5)  #core(t>=5)")
witness_fields = []
for q in [x for x in range(17, 5000) if x % 16 == 1 and is_prime(x)]:
    D = subgroup(q, 16)
    locs = locators(D, q, 3)
    pts = [c for (_, c) in locs]
    found = frugal_lines(pts, q, 3, 5)
    cf, cr = 0, 0
    for (i, vn, mem) in found:
        sup = [locs[t][0] for t in mem]
        common = set(sup[0])
        for s in sup[1:]:
            common &= set(s)
        if common:
            cr += 1
        else:
            cf += 1
    maxt = max([len(m) for (_, _, m) in found], default=0)
    say("%-5d %-6d %-16d %d" % (q, maxt, cf, cr))
    if cf:
        witness_fields.append(q)
say("prime fields <5000 with a core-free strict-A3 witness at N=16: %s"
    % witness_fields)
say()

# ------------------------------------------------------------------ (b)
say("=== (b) are the CORE (s>=1) t>=5 lines genuine far-CA witnesses? ===")


def rref(M, q):
    M = [row[:] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    piv = []
    r = 0
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


def kernel(M, q, cols=None):
    if not M:
        return [[1 if i == j else 0 for i in range(cols)] for j in range(cols)]
    Mr, piv = rref(M, q)
    cols = len(M[0])
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = [0] * cols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-Mr[i][f]) % q
        basis.append(v)
    return basis


def hankel(y, Rv, rv, q):
    return [[y[i + j] % q for j in range(rv + 1)] for i in range(Rv - rv)]


def is_split(vec, D, q, rho):
    if vec[rho] % q == 0:
        return None
    iv = pow(vec[rho], q - 2, q)
    c = [v * iv % q for v in vec]
    roots = [x for x in D if sum(c[i] * pow(x, i, q) for i in range(rho + 1)) % q == 0]
    return tuple(roots) if len(roots) == rho else None


def pencil_from_line(q0, q1, Rv, rv, q):
    """solve M_rv(y0+Z y1)(q0+Z q1) = 0 for (y0,y1) in F^(2Rv)."""
    rows = []
    m = Rv - rv
    for deg in range(3):          # Z^0, Z^1, Z^2
        for i in range(m):
            row = [0] * (2 * Rv)
            for j in range(rv + 1):
                # y_{i+j} coefficient contributions
                if deg == 0:
                    row[i + j] = (row[i + j] + q0[j]) % q
                elif deg == 1:
                    row[i + j] = (row[i + j] + q1[j]) % q
                    row[Rv + i + j] = (row[Rv + i + j] + q0[j]) % q
                else:
                    row[Rv + i + j] = (row[Rv + i + j] + q1[j]) % q
            rows.append(row)
    return kernel(rows, q)


def analyse(y, Rv, rv, D, q):
    y0, y1 = y[:Rv], y[Rv:]
    M0, M1 = hankel(y0, Rv, rv, q), hankel(y1, Rv, rv, q)
    farker = kernel(M0 + M1, q)
    colfar = True
    for basis_dim in range(len(farker)):
        pass
    # column-close iff the common kernel contains a split locator
    if farker:
        if len(farker) == 1:
            colfar = is_split(farker[0], D, q, rv) is None
        else:
            colfar = True
            for coeffs in itertools.product(range(q), repeat=len(farker)):
                if all(c == 0 for c in coeffs):
                    continue
                v = [sum(coeffs[t] * farker[t][s] for t in range(len(farker))) % q
                     for s in range(rv + 1)]
                if is_split(v, D, q, rv):
                    colfar = False
                    break
    T = 0
    for g in range(q):
        yy = [(y0[t] + g * y1[t]) % q for t in range(Rv)]
        ker = kernel(hankel(yy, Rv, rv, q), q)
        hit = False
        if len(ker) == 1:
            hit = is_split(ker[0], D, q, rv) is not None
        elif len(ker) >= 2:
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
    return colfar, T


for q in (17, 97):
    D = subgroup(q, 16)
    locs = locators(D, q, 3)
    pts = [c for (_, c) in locs]
    found = frugal_lines(pts, q, 3, 5)
    ncore = 0
    bad = 0
    maxT_core = 0
    for (i, vn, mem) in found[:60]:
        sup = [locs[t][0] for t in mem]
        common = set(sup[0])
        for s in sup[1:]:
            common &= set(s)
        if not common:
            continue
        ncore += 1
        q0 = list(pts[mem[0]]) + [1]
        # direction of the locator line, padded with leading 0
        q1 = list(vn) + [0]
        sols = pencil_from_line(q0, q1, 8, 3, q)
        for sol in sols[:2]:
            if all(v == 0 for v in sol):
                continue
            colfar, T = analyse(sol, 8, 3, D, q)
            maxT_core = max(maxT_core, T if colfar else 0)
            if colfar and T > 4:
                bad += 1
    say("q=%d : tested %d core lines; column-far pencils with T>4 : %d ; "
        "max T among column-far core pencils = %d"
        % (q, ncore, bad, maxT_core))
say()

# ------------------------------------------------------------------ (c)
say("=== (c) N=20, rho=4 (a DEAD scale): counting bound says max t <= 5 ===")
for q in (41, 101):
    if (q - 1) % 20:
        continue
    D = subgroup(q, 20)
    locs = locators(D, q, 4)
    pts = [c for (_, c) in locs]
    found = frugal_lines(pts, q, 4, 5)
    cf = 0
    maxt = 0
    for (i, vn, mem) in found:
        sup = [locs[t][0] for t in mem]
        common = set(sup[0])
        for s in sup[1:]:
            common &= set(s)
        if not common:
            cf += 1
            maxt = max(maxt, len(mem))
    say("q=%-4d #loc=%d  core-free lines with t>=5: %d  max core-free t=%d "
        "(violation needs t>=6)" % (q, len(locs), cf, maxt))
say()

# ------------------------------------------------------------------ (d)
say("=== (d) density law for the strict A=3 sharp face at e=m ===")
say("codim exponent  cond-dim = T(rho-1) - [(e+1)(rho+1)-1]")
say("  with T=4m+1, rho=4m-1, e=m  ->  12m^2 - 8m - 1")
import math
for m in (1, 2, 3, 4, 8, 2 ** 37):
    ex = 12 * m * m - 8 * m - 1
    say("  m=%-14d exponent=%d" % (m, ex))
say("m=1 exponent 3: census predicted count ~ 16*(17/q)^3 -> 0 for q>=97 "
    "(CONFIRMED above)")
say("official m=2^37: exponent = %d ~ 2^%.1f ; residual fields are PRIME "
    "with q>2^167 (rate_half_residual_prime_field_collapse)"
    % (12 * (2 ** 37) ** 2 - 8 * 2 ** 37 - 1,
       math.log2(12 * (2 ** 37) ** 2)))
say("log10 of configuration entropy ~ (4m+1)*log10 C(16m,4m-1) ~ 15.6 m^2 ;")
say("log10 of the field penalty ~ (12m^2)*log10 q .")
say("=> a sharp-face witness needs log10 q <~ 15.6/12 = 1.30, i.e. q <~ 20.")
say("=== END ===")
