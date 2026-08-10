"""D1/D3: strict-A=3 residual census on band-analogue rows.

Scaled band-analogue row: N = 2k, R = k, D = order-N multiplicative
subgroup of F_q (N | q-1).  Strict residual radius r = R/2 - 1 = rho,
A = R+1-2rho = 3.  A failure of the staircase-shaped formula at that
radius is exactly a column-far pencil with T >= rho+2 supported slopes.

For parameter degree e=1 the supported locators lie on an AFFINE LINE in
monic-locator coefficient space, so the whole e=1 question is the exact
census run here.  (For N=16 the counting bound forces e<=floor(rho/3)=1,
so this census is COMPLETE for that scale.)

Sections:
  S1  liveness table over scales R (P5)
  S2  the m=1 route-fence witness replay over F_17 (validation)
  S3  line census over fields q = 1 mod 16 at N=16, rho=3 (P4,P6,P7)
  S4  line census at N=20, rho=4 (counting bound says max <= 5)

Stdlib only.  Run under tools/ramguard.
"""
import itertools
import sys

OUT = []


def say(s=""):
    OUT.append(str(s))
    print(str(s), flush=True)


# ----------------------------------------------------------------- S1
def liveness(Rv):
    """strict A=3 budget at scale R: rho=R/2-1, need T>=rho+2,
    counting cap T <= floor(((N-s)e + rho-3e)/rho) with s=0, e<=rho//3."""
    N = 2 * Rv
    rho = Rv // 2 - 1
    if rho < 1:
        return None
    emax = rho // 3
    best = 0
    beste = 0
    for e in range(0, emax + 1):
        cap = (N * e + rho - 3 * e) // rho
        if cap > best:
            best, beste = cap, e
    return dict(R=Rv, N=N, rho=rho, emax=emax, need=rho + 2, cap=best,
                arge=beste, live=best >= rho + 2)


say("=== S1: liveness of the strict A=3 residual budget by scale ===")
say("R    N    rho  e<=  need  cap(max over e)  argmax e  LIVE?")
dead = []
for Rv in range(4, 42, 2):
    d = liveness(Rv)
    if d is None:
        continue
    say("%-4d %-4d %-4d %-4d %-5d %-16d %-9d %s"
        % (d["R"], d["N"], d["rho"], d["emax"], d["need"], d["cap"],
           d["arge"], d["live"]))
    if not d["live"]:
        dead.append(d["R"])
say("DEAD set in R in [4,40]: %s" % dead)
# official row
Rv = 2 ** 40
rho = Rv // 2 - 1
N = 2 * Rv
emax = rho // 3
say("official R=2^40: rho=%d  need T>=%d  e window [m,floor(rho/3)] = [%d,%d]"
    % (rho, rho + 2, 2 ** 37, emax))
say("  cap at e=m: %d  (need %d, deficit %d)"
    % ((N * 2 ** 37 + rho - 3 * 2 ** 37) // rho, rho + 2,
       rho + 2 - (N * 2 ** 37 + rho - 3 * 2 ** 37) // rho))
say("  window size = %d" % (emax - 2 ** 37 + 1))
say()


# ------------------------------------------------------- field helpers
def subgroup(q, N):
    """the unique order-N subgroup of F_q^*, as a sorted list."""
    assert (q - 1) % N == 0
    g = None
    for cand in range(2, q):
        seen = set()
        x = 1
        for _ in range(q - 1):
            x = x * cand % q
            seen.add(x)
        if len(seen) == q - 1:
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
    """all monic squarefree degree-rho polys split over D.

    returns list of (support tuple, ascending coeff tuple length rho)."""
    out = []
    for S in itertools.combinations(D, rho):
        # poly = prod (X - x)
        c = [1]
        for x in S:
            nc = [0] * (len(c) + 1)
            for i, ci in enumerate(c):
                nc[i] = (nc[i] - x * ci) % q
                nc[i + 1] = (nc[i + 1] + ci) % q
            c = nc
        assert c[-1] == 1
        out.append((S, tuple(c[:-1])))
    return out


def line_census(pts, q, dim):
    """count affine lines through >=2 of pts; return dict key->set(idx)."""
    inv = [0] * q
    for a in range(1, q):
        inv[a] = pow(a, q - 2, q)
    lines = {}
    n = len(pts)
    for i in range(n):
        Pi = pts[i]
        for j in range(i + 1, n):
            Pj = pts[j]
            v = tuple((Pj[t] - Pi[t]) % q for t in range(dim))
            # normalise direction: first nonzero -> 1
            fi = 0
            while v[fi] == 0:
                fi += 1
            iv = inv[v[fi]]
            vn = tuple(vt * iv % q for vt in v)
            # base point: kill coordinate fi
            lam = Pi[fi]
            base = tuple((Pi[t] - lam * vn[t]) % q for t in range(dim))
            key = (vn, base)
            s = lines.get(key)
            if s is None:
                lines[key] = {i, j}
            else:
                s.add(i)
                s.add(j)
    return lines


def census_scale(q, N, rho, verbose=False):
    D = subgroup(q, N)
    locs = locators(D, q, rho)
    pts = [c for (_, c) in locs]
    lines = line_census(pts, q, rho)
    hist = {}
    big = []
    for key, idxs in lines.items():
        t = len(idxs)
        hist[t] = hist.get(t, 0) + 1
        if t >= rho + 2:
            sup = [locs[i][0] for i in sorted(idxs)]
            common = set(sup[0])
            for s in sup[1:]:
                common &= set(s)
            big.append((key, sorted(idxs), sup, sorted(common)))
    return D, locs, hist, big


# ----------------------------------------------------------------- S2
say("=== S2: replay of the m=1 route-fence witness over F_17 ===")
q = 17
D17 = subgroup(q, 16)
say("D = order-16 subgroup of F_17^* = %s" % D17)
y0 = [1, 10, 16, 2, 14, 0, 3, 11]
y1 = [0, 14, 9, 7, 13, 12, 15, 0]
Rr, rr = 8, 3


def hankel(y, Rv, rv, q):
    return [[y[i + j] % q for j in range(rv + 1)] for i in range(Rv - rv)]


def rref(M, q):
    M = [row[:] for row in M]
    rows, cols = len(M), len(M[0])
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


def kernel(M, q):
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


def is_split_locator(vec, D, q, rho):
    """vec = ascending coeffs length rho+1; monic-normalise, need rho
    distinct roots all in D."""
    if vec[rho] % q == 0:
        return None
    iv = pow(vec[rho], q - 2, q)
    c = [v * iv % q for v in vec]
    roots = [x for x in D if sum(c[i] * pow(x, i, q) for i in range(rho + 1)) % q == 0]
    if len(roots) == rho:
        return tuple(sorted(roots))
    return None


def supported_slopes(y0, y1, Rv, rv, D, q):
    res = {}
    for g in range(q):
        y = [(y0[t] + g * y1[t]) % q for t in range(Rv)]
        M = hankel(y, Rv, rv, q)
        ker = kernel(M, q)
        found = None
        if len(ker) == 1:
            found = is_split_locator(ker[0], D, q, rv)
        elif len(ker) >= 2:
            # search the projective kernel space (small dims only)
            import itertools as it
            for coeffs in it.product(range(q), repeat=len(ker)):
                if all(c == 0 for c in coeffs):
                    continue
                v = [sum(coeffs[i] * ker[i][t] for i in range(len(ker))) % q
                     for t in range(rv + 1)]
                f = is_split_locator(v, D, q, rv)
                if f:
                    found = f
                    break
        if found:
            res[g] = found
    return res


ranks = {}
for g in range(q):
    y = [(y0[t] + g * y1[t]) % q for t in range(8)]
    M = hankel(y, 8, 3, q)
    _, piv = rref(M, q)
    ranks[g] = len(piv)
say("rank of M_3(y0+g y1) over finite slopes: %s" % sorted(set(ranks.values())))
sup = supported_slopes(y0, y1, 8, 3, D17, q)
say("supported finite slopes (T=%d): %s" % (len(sup), sorted(sup.items())))
say("expected T=5 with triples {1,2,5},{3,7,11},{9,12,13},{4,6,16},{8,10,15}")
allpts = set()
for g, tri in sup.items():
    allpts |= set(tri)
say("union of supports = %d points; omitted from D: %s"
    % (len(allpts), sorted(set(D17) - allpts)))
# column-far test: common kernel of M(y0), M(y1) contains a split locator?
M0 = hankel(y0, 8, 3, q)
M1 = hankel(y1, 8, 3, q)
ker_both = kernel(M0 + M1, q)
say("dim of common kernel of M_3(y0),M_3(y1) = %d -> column-far = %s"
    % (len(ker_both), len(ker_both) == 0))
say("T=%d vs rho+1=%d : staircase-shaped bound %s at r=3"
    % (len(sup), rr + 1, "VIOLATED" if len(sup) > rr + 1 else "holds"))
say()

# ----------------------------------------------------------------- S3
say("=== S3: field axis. N=16, rho=r=3, e=1 line census, q = 1 mod 16 ===")


def is_prime(x):
    if x < 2:
        return False
    for p in range(2, int(x ** 0.5) + 1):
        if x % p == 0:
            return False
    return True


qs = [x for x in range(17, 1000) if x % 16 == 1 and is_prime(x)]
say("fields: %s" % qs)
say("q    #loc  max_t  #lines(t=4)  #lines(t>=5)  core-free witnesses")
tot5 = 0
witness_records = []
for q in qs:
    D, locs, hist, big = census_scale(q, 16, 3)
    maxt = max(hist) if hist else 0
    corefree = [b for b in big if not b[3]]
    tot5 += len(corefree)
    say("%-4d %-5d %-6d %-12d %-13d %d"
        % (q, len(locs), maxt, hist.get(4, 0), sum(v for t, v in hist.items() if t >= 5),
           len(corefree)))
    if corefree:
        witness_records.append((q, corefree))
say("TOTAL core-free t>=5 lines over q in [97,1000]: %d"
    % sum(len(c) for (qq, c) in witness_records if qq >= 97))
for q, cf in witness_records:
    say("  q=%d : %d core-free 5-lines; first omits %s"
        % (q, len(cf), sorted(set(subgroup(q, 16)) -
                              set().union(*[set(s) for s in cf[0][2]]))))
say()

# ----------------------------------------------------------------- S4
say("=== S4: N=20, rho=r=4, e=1 census (counting bound says max t <= 5) ===")
for q in [41, 101]:
    if (q - 1) % 20:
        continue
    D, locs, hist, big = census_scale(q, 20, 4)
    say("q=%d  #loc=%d  max_t=%d  need t>=%d for a violation -> %s"
        % (q, len(locs), max(hist), 4 + 2,
           "no violation" if max(hist) < 6 else "VIOLATION"))
    say("     histogram: %s" % sorted(hist.items()))

say("=== END ===")
