"""f4_close.py  (r36_hrlow)

Closes the round.

The f3 histogram identified the h_r=rho+2 excess exactly: with D closed
under x -> -x and L = x^2 (so e_1 = x^2 e_0), the EVEN split locators
sigma(x) = Q(x^2) (root set S = A u (-A)) make the ODD-index Hankel rows
of the pencil vanish identically.  Reason: v_{-x} = (-1)^{n-1} v_x on a
negation-closed D, and sum_{x in D} v_x g(x) = 0 for deg g <= n-2, so
for odd i the whole row collapses to the orbits NOT met by T.  Killing
those orbits (S contains them) leaves only the EVEN-index rows as
genuine conditions on gamma: ceil(rho/2) conditions, one unknown.

  rho = 2 -> 1 condition, 1 unknown  -> one slope per even locator: a
             field-size-independent excess of ~C(n/2-1, r/2-1).
  rho >= 3 -> >= 2 conditions, 1 unknown -> generically NOTHING.

A. even-locator scan at rho=2 (H1,H3) and rho=3 (H4,H5), two fields.
B. control: the SAME d=2 family on a NON-negation-closed D, exact census.
C. razor-scale closed forms.

Writes: notes/pilots_20260811/r36_hrlow/f4_results.txt   (own dir)
"""
import sys
from itertools import combinations
from math import log2, lgamma

OUT = "notes/pilots_20260811/r36_hrlow/f4_results.txt"


def inv(a, q):
    return pow(a % q, q - 2, q)


def make_v(D, q):
    v = {}
    for x in D:
        pr = 1
        for y in D:
            if y != x:
                pr = (pr * (x - y)) % q
        v[x] = inv(pr, q)
    return v


def polyeval(p, x, q):
    s = 0
    for c in reversed(p):
        s = (s * x + c) % q
    return s


def syn_of(ev, D, v, q, R):
    y = [0] * R
    for x in D:
        e = ev.get(x, 0) % q
        if not e:
            continue
        c = (e * v[x]) % q
        xp = 1
        for m in range(R):
            y[m] = (y[m] + c * xp) % q
            xp = (xp * x) % q
    return y


def hank(y, rho, r, q):
    return [[y[i + j] % q for j in range(r + 1)] for i in range(rho)]


def poly_from_roots(roots, q):
    p = [1]
    for al in roots:
        np_ = [0] * (len(p) + 1)
        for i, c in enumerate(p):
            np_[i + 1] = (np_[i + 1] + c) % q
            np_[i] = (np_[i] - c * al) % q
        p = np_
    return p


def slope_of(M0, M1, sig, rho, r, q):
    """the unique gamma with (M0+gamma M1)sig = 0, or None; 'COMMON' if
    sig is a common kernel vector."""
    U = []
    W = []
    for i in range(rho):
        su = 0
        sw = 0
        for j in range(r + 1):
            sj = sig[j]
            if sj:
                su += M0[i][j] * sj
                sw += M1[i][j] * sj
        U.append(su % q)
        W.append(sw % q)
    if all(x == 0 for x in W):
        return "COMMON" if all(x == 0 for x in U) else None
    j = next(i for i in range(rho) if W[i])
    g = (-U[j] * inv(W[j], q)) % q
    if all((U[i] + g * W[i]) % q == 0 for i in range(rho)):
        return g
    return None


def main():
    lines = []

    def w(t):
        lines.append(t)
        print(t)
        sys.stdout.flush()

    w("# f4_close.py — r36_hrlow")

    # ---------- A: even-locator scan ----------
    w("")
    w("== A. EVEN-locator scan (D negation-closed, L = x^2, s = r+1)")
    w("#  m = n/2 orbits {+-1..+-m}; T = {1..r+1} meets orbits 1..r+1 "
      "one-sidedly; even locator S = A u (-A), |A| = r/2.")
    w("#  PREDICTION: #bad even locators ~ C(m-1, r/2-1) when rho=2 "
      "(1 residual condition) and ~0 when rho>=3 (>=2 residual "
      "conditions).")
    for tag, n, k, rho in (("H1", 20, 10, 2), ("H3", 24, 12, 2),
                           ("H4", 26, 13, 3), ("H6", 30, 15, 3),
                           ("H7", 34, 17, 3), ("H8", 36, 18, 4)):
        R = n - k
        r = R - rho
        a = n - r
        if r % 2:
            w("  %s r=%d odd — even locators of degree r do not exist; "
              "skipped" % (tag, r))
            continue
        m = n // 2
        w("  -- %s n=%d k=%d R=%d rho=%d r=%d a=%d | FAITHFUL 4rho<R %s "
          "a>R+1 %s a-1>r %s | C(m,r/2)=%d  C(m-1,r/2-1)=%d" %
          (tag, n, k, R, rho, r, a, 4 * rho < R, a > R + 1, a - 1 > r,
           len(list(combinations(range(m), r // 2))),
           len(list(combinations(range(m - 1), r // 2 - 1)))))
        for q in (65537, 999983):
            D = []
            for i in range(1, m + 1):
                D.append(i % q)
                D.append((-i) % q)
            v = make_v(D, q)
            T = [i % q for i in range(1, r + 2)]
            e0 = {x: 1 for x in T}
            e1 = {x: polyeval([0, 0, 1], x, q) for x in T}
            y0 = syn_of(e0, D, v, q, R)
            y1 = syn_of(e1, D, v, q, R)
            M0 = hank(y0, rho, r, q)
            M1 = hank(y1, rho, r, q)
            offT = set(range(r + 2, m + 1))
            good = 0
            common = 0
            gam = set()
            withorb = 0
            nfull = 0
            for A in combinations(range(1, m + 1), r // 2):
                sA = set(A)
                if offT <= sA:
                    nfull += 1
                S = [x % q for x in A] + [(-x) % q for x in A]
                sig = poly_from_roots(S, q)
                g = slope_of(M0, M1, sig, rho, r, q)
                if g == "COMMON":
                    common += 1
                elif g is not None:
                    good += 1
                    gam.add(g)
                    if offT <= sA:
                        withorb += 1
            w("     q=%-7d |orbits off T|=%d  #A covering them=%d | bad "
              "EVEN locators=%4d (distinct slopes=%4d, covering=%4d) "
              "| common=%d | r+1=%d" %
              (q, len(offT), nfull, good, len(gam), withorb, common,
               r + 1))

    # ---------- B: control on a NON-negation-closed D ----------
    w("")
    w("== B. CONTROL — same d=2 family, D NOT negation-closed "
      "(D = {1,...,n}), exact census over all C(n,r) locators")
    n, k, rho, q = 20, 10, 2, 65537
    R = n - k
    r = R - rho
    D = [i % q for i in range(1, n + 1)]
    assert len(set(D)) == n
    v = make_v(D, q)
    T = [i % q for i in range(1, r + 2)]
    objs = []
    for tag, Lc in (("d1-x", [0, 1]), ("d2-inj", [0, 0, 1])):
        e0 = {x: 1 for x in T}
        e1 = {x: polyeval(Lc, x, q) for x in T}
        y0 = syn_of(e0, D, v, q, R)
        y1 = syn_of(e1, D, v, q, R)
        groups = {}
        for x in T:
            groups.setdefault((-inv(e1[x], q)) % q, []).append(x)
        objs.append(dict(tag=tag, M0=hank(y0, rho, r, q),
                         M1=hank(y1, rho, r, q), gam=set(), common=0,
                         struct=set(g for g, Z in groups.items()
                                    if len(T) - len(Z) <= r)))
    nD = len(D)
    sys.setrecursionlimit(10000)

    def rec(start, depth, sig):
        if depth == r:
            for ob in objs:
                g = slope_of(ob['M0'], ob['M1'], sig, rho, r, q)
                if g == "COMMON":
                    ob['common'] += 1
                elif g is not None:
                    ob['gam'].add(g)
            return
        for idx in range(start, nD - (r - depth) + 1):
            x = D[idx]
            ns = [0] * (r + 1)
            for j in range(depth + 1):
                c = sig[j]
                if c:
                    ns[j + 1] = (ns[j + 1] + c) % q
                    ns[j] = (ns[j] - c * x) % q
            rec(idx + 1, depth + 1, ns)

    s0 = [0] * (r + 1)
    s0[0] = 1
    rec(0, 0, s0)
    for ob in objs:
        G = ob['gam']
        w("   q=%d D={1..20} %-8s | column-%s | T=%d T_struct=%d "
          "T_acc=%d | r+1=%d   (negation-closed D gave T=98, T_acc=89)" %
          (q, ob['tag'], "CLOSE" if ob['common'] else "far", len(G),
           len(G & ob['struct']), len(G - ob['struct']), r + 1))

    # ---------- C: razor closed forms ----------
    w("")
    w("== C. razor closed forms  (R=k=2^40, rho=2^34, r=R-rho, n=2^41)")
    R = 2 ** 40
    rho = 2 ** 34
    r = R - rho
    n = 2 ** 41
    kk = R
    aa = kk + rho
    w("   R=%d rho=%d r=%d n=%d a=k+rho=%d" % (R, rho, r, n, aa))
    w("   FAITHFUL at the razor: 4rho<R %s ; a>R+1 %s ; a-1>r %s" %
      (4 * rho < R, aa > R + 1, aa - 1 > r))
    w("   r+1 = %d = 2^%.6f   (banked LB1 floor)" % (r + 1, log2(r + 1)))
    for d in (1, 2, 3, rho // 2, rho):
        ps = max(rho + d, (R + 1 + d) // 2)
        fl = -((-(r + 1)) // d)
        w("   d=%-12d h_r=rho+d=%-12d p*=%-14d p*-floor(R/2)=%-3d "
          "fibre floor ceil((r+1)/d)=%d" % (d, rho + d, ps,
                                            ps - R // 2, fl))
    w("   => over the WHOLE band d=1..rho: p* in [2^39+1, 2^39+2^33], "
      "every value STRICTLY above floor(R/2)=%d" % (R // 2))
    w("   => the fibre floor decays from r+1=2^%.4f (d=1) to %d (d=rho)"
      % (log2(r + 1), -((-(r + 1)) // rho)))
    lgc = (lgamma(n + 1) - lgamma(r + 1) - lgamma(n - r + 1)) / log2(2.718281828459045 ** 1) / 1.0
    log2C = (lgamma(n + 1) - lgamma(r + 1) - lgamma(n - r + 1)) / 0.6931471805599453
    w("   log2 C(n,r) = %.4f  (mu_1 = C(n,r)/q^rho)" % log2C)
    for lq in (128, 167, 256):
        w("      log2 mu_1 at q=2^%-4d = %.6e" % (lq, log2C - rho * lq))
    # the even-locator mechanism at razor scale
    m = n // 2
    half = r // 2
    log2Ceven = (lgamma(m + 1) - lgamma(half + 1) - lgamma(m - half + 1)) / 0.6931471805599453
    w("   even-locator carrier at razor (D a multiplicative subgroup of "
      "even order is negation-closed):")
    w("      #even locators = C(n/2, r/2) = 2^%.4f ; residual conditions "
      "on the single unknown gamma = ceil(rho/2) = %d" %
      (log2Ceven, (rho + 1) // 2))
    w("      over-determination = ceil(rho/2) - 1 = %d  => the rho=2 "
      "excess mechanism is DEAD at the razor by %d conditions" %
      ((rho + 1) // 2 - 1, (rho + 1) // 2 - 1))
    w("   B*(q)=floor(q/2^128) on the residual interval = 2^39 or 2^39+1;"
      " (r+1)/2^39 = %.6f" % ((r + 1) / 2.0 ** 39))

    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print("wrote", OUT)


main()
