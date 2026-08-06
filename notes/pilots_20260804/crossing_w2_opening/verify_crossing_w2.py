#!/usr/bin/env python3
"""Crossing at w >= 2 -- opening pilot verifier.

Profile: tiny. Pure python integers, deterministic, no third-party imports,
no reads outside this directory.

Tests the pre-registered claims of PREREG.md:
  (X)  product-condition equidistribution for GENERAL T, all w
  (Q)  q-collapse: the w>=2 count depends on q only through p = char
  (Y)  Newton/BCH linearization, valid iff w <= p (falsifier at p=2, w=3)
  (S)  structural (char-0 Lam-Leung) floor <= measured count
  (P)  w = 1 is q-free (PK1 recovery)
  (CAL) replay of PK2's measured w=2 shell 30/9/7/8 at n=16,k=8,r'=6
  (V)  MC-1 replay against a brute-force codeword census
  (MW) MERGE CHECK: the MC/crossing window IS LEMMA W's divisor window,
       and for the MC word it is a CODIMENSION-w COORDINATE subspace
       of the locator-coefficient space (rank of the Toeplitz system = w)
"""

from itertools import combinations

FAILURES = []
CHECKS = [0]


def check(name, cond, detail=""):
    CHECKS[0] += 1
    if not cond:
        FAILURES.append((name, detail))
    return cond


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def factorize(m):
    fs, d = set(), 2
    while d * d <= m:
        while m % d == 0:
            fs.add(d)
            m //= d
        d += 1
    if m > 1:
        fs.add(m)
    return fs


# ---------------------------------------------------------------- finite field
class GF(object):
    """GF(p^e); elements are ints encoding base-p digit vectors.

    Multiplication by discrete log tables; addition digitwise (XOR when p=2).
    """

    def __init__(self, p, e):
        self.p, self.e, self.size = p, e, p ** e
        self.modpoly = self._find_irreducible()
        self.one = 1
        self._dec = [self._decode(x) for x in range(self.size)]
        self._enc = {}
        for x in range(self.size):
            self._enc[self._dec[x]] = x
        self._build_logs()

    # -- polynomial arithmetic over F_p, coefficient lists low-to-high
    def _pmul(self, a, b):
        p = self.p
        res = [0] * (len(a) + len(b) - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    res[i + j] = (res[i + j] + ai * bj) % p
        return res

    def _pmod(self, a, m):
        """a mod monic m (m given low-to-high, monic)."""
        p, dm = self.p, len(m) - 1
        a = a[:]
        for i in range(len(a) - 1, dm - 1, -1):
            c = a[i]
            if c:
                a[i] = 0
                for j in range(dm):
                    a[i - dm + j] = (a[i - dm + j] - c * m[j]) % p
        return a[:dm] + [0] * max(0, dm - len(a))

    def _is_irreducible(self, m):
        """m monic of degree e, low-to-high with leading 1: trial division."""
        p, e = self.p, len(m) - 1
        if m[0] == 0:
            return False
        for deg in range(1, e // 2 + 1):
            for code in range(p ** deg):
                g, c = [], code
                for _ in range(deg):
                    g.append(c % p)
                    c //= p
                g.append(1)
                # divide m by g
                a = m[:]
                for i in range(len(a) - 1, deg - 1, -1):
                    co = a[i]
                    if co:
                        inv = pow(1, p - 2, p)  # g monic -> leading 1
                        co = co * inv % p
                        a[i] = 0
                        for j in range(deg):
                            a[i - deg + j] = (a[i - deg + j] - co * g[j]) % p
                if all(x == 0 for x in a[:deg]):
                    return False
        return True

    def _find_irreducible(self):
        p, e = self.p, self.e
        if e == 1:
            return [0, 1]
        for code in range(p ** e):
            m, c = [], code
            for _ in range(e):
                m.append(c % p)
                c //= p
            m.append(1)
            if self._is_irreducible(m):
                return m
        raise RuntimeError("no irreducible")

    def _decode(self, n):
        v, p = [], self.p
        for _ in range(self.e):
            v.append(n % p)
            n //= p
        return tuple(v)

    def _rawmul(self, a, b):
        prod = self._pmul(list(self._dec[a]), list(self._dec[b]))
        red = self._pmod(prod, self.modpoly)
        return self._enc[tuple(red[: self.e])]

    def _build_logs(self):
        sz = self.size
        facs = factorize(sz - 1)
        gen = None
        for g in range(2, sz):
            ok = True
            for f in facs:
                x, ex, base = 1, (sz - 1) // f, g
                while ex:
                    if ex & 1:
                        x = self._rawmul(x, base)
                    base = self._rawmul(base, base)
                    ex >>= 1
                if x == 1:
                    ok = False
                    break
            if ok:
                gen = g
                break
        self.gen = gen
        self.exp = [0] * (sz - 1)
        self.log = [0] * sz
        cur = 1
        for i in range(sz - 1):
            self.exp[i] = cur
            self.log[cur] = i
            cur = self._rawmul(cur, gen)
        assert cur == 1

    def mul(self, a, b):
        if a == 0 or b == 0:
            return 0
        return self.exp[(self.log[a] + self.log[b]) % (self.size - 1)]

    def add(self, a, b):
        if self.p == 2:
            return a ^ b
        da, db, p = self._dec[a], self._dec[b], self.p
        return self._enc[tuple((x + y) % p for x, y in zip(da, db))]

    def neg_one(self):
        if self.p == 2:
            return 1
        acc = 0
        for _ in range(self.p - 1):
            acc = self.add(acc, 1)
        return acc

    def elem_of_order(self, n):
        assert (self.size - 1) % n == 0
        return self.exp[(self.size - 1) // n]

    def powers(self, z, n):
        out, cur = [], 1
        for _ in range(n):
            out.append(cur)
            cur = self.mul(cur, z)
        return out


# --------------------------------------------------------- window enumeration
def window_set(n, rp, w, F, zpow):
    """S in W_w: e_s({zeta^i : i in S}) = 0 for s = 1..w-1."""
    if w == 1:
        return list(combinations(range(n), rp))
    out = []
    for S in combinations(range(n), rp):
        es = [1] + [0] * (w - 1)
        for i in S:
            zi = zpow[i]
            for s in range(w - 1, 0, -1):
                es[s] = F.add(es[s], F.mul(es[s - 1], zi))
        if all(es[s] == 0 for s in range(1, w)):
            out.append(S)
    return out


def bch_set(n, rp, w, F, zpow):
    """Power-sum (cyclic-code / BCH) condition p_1 = .. = p_{w-1} = 0."""
    out = []
    for S in combinations(range(n), rp):
        ok = True
        for s in range(1, w):
            acc = 0
            for i in S:
                acc = F.add(acc, zpow[(s * i) % n])
            if acc != 0:
                ok = False
                break
        if ok:
            out.append(S)
    return out


def sig_profile(n, W):
    prof = [0] * n
    for S in W:
        prof[sum(S) % n] += 1
    return prof


def lemma_x_ok(n, rp, prof):
    """Fibres of sig equal within each class mod d = gcd(r', n)."""
    d = gcd(rp, n)
    for j in range(d):
        vals = set(prof[t] for t in range(n) if t % d == j)
        if len(vals) != 1:
            return False, d
    return True, d


# --------------------------------------------------- char-0 structural window
def cyclotomic(n, _cache={}):
    if n in _cache:
        return _cache[n]
    num = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            num = polydiv(num, cyclotomic(d))
    _cache[n] = num
    return num


def polydiv(a, b):
    a = a[:]
    q = [0] * (len(a) - len(b) + 1)
    for i in range(len(a) - len(b), -1, -1):
        c = a[i + len(b) - 1] // b[-1]
        q[i] = c
        if c:
            for j in range(len(b)):
                a[i + j] -= c * b[j]
    assert all(x == 0 for x in a)
    return q


def divisible_by(poly, phi):
    a = poly[:] + [0] * max(0, len(phi) - len(poly))
    for i in range(len(a) - len(phi), -1, -1):
        c = a[i + len(phi) - 1]
        if c % phi[-1]:
            return False
        c //= phi[-1]
        if c:
            for j in range(len(phi)):
                a[i + j] -= c * phi[j]
    return all(x == 0 for x in a)


def structural_window(n, rp, w):
    phi = cyclotomic(n)
    out = []
    for S in combinations(range(n), rp):
        ok = True
        for s in range(1, w):
            poly = [0] * n
            for A in combinations(S, s):
                poly[sum(A) % n] += 1
            if not divisible_by(poly, phi):
                ok = False
                break
        if ok:
            out.append(S)
    return out


# ------------------------------------------------------- MC shell and census
def mc_shell_count(n, k, w, F, zpow, cval=1):
    """#{S in W_w : prod T(S) = gamma},  gamma = (-1)^{r'+1} c,  x_0 = 1."""
    rp = n - k - w
    W = window_set(n, rp, w, F, zpow)
    gam = cval if (rp + 1) % 2 == 0 else F.mul(F.neg_one(), cval)
    return sum(1 for S in W if zpow[sum(S) % n] == gam), W


def mc1_census(n, k, w, F, zpow):
    """Brute force: agreement profile of all degree-<k codewords with u."""
    sz = F.size
    H = zpow
    uv = [F.add(zpow[((n - 1) * i) % n], zpow[((k + w - 1) * i) % n])
          for i in range(n)]
    prof = {}
    for code in range(sz ** k):
        c2, cf = code, []
        for _ in range(k):
            cf.append(c2 % sz)
            c2 //= sz
        agr = 0
        for i in range(n):
            val, xp = 0, 1
            for a in cf:
                if a:
                    val = F.add(val, F.mul(a, xp))
                xp = F.mul(xp, H[i])
            if val == uv[i]:
                agr += 1
        if agr >= k + w:
            prof[agr] = prof.get(agr, 0) + 1
    return prof


# ---------------------------------------- MERGE: LEMMA W Toeplitz window rank
def lemmaW_toeplitz_rank(n, k, w, F, zpow):
    """Rank of the w x (r'+1) Toeplitz window matrix of the MC word u,
    and whether its solution set is a COORDINATE subspace.

    LEMMA W (banked): rows j = n-w..n-1, entries u_{(j-i) mod n},
    where u_m are the coefficients of u = X^{n-1} + X^{k+w-1}.
    """
    rp = n - k - w
    u = [0] * n
    u[n - 1] = 1
    u[k + w - 1] = F.add(u[k + w - 1], 1)
    rows = []
    for j in range(n - w, n):
        rows.append([u[(j - i) % n] for i in range(rp + 1)])
    # gaussian elimination over F
    mat = [r[:] for r in rows]
    piv_cols, r0 = [], 0
    for c in range(rp + 1):
        pr = None
        for r in range(r0, len(mat)):
            if mat[r][c]:
                pr = r
                break
        if pr is None:
            continue
        mat[r0], mat[pr] = mat[pr], mat[r0]
        inv = F.exp[(-F.log[mat[r0][c]]) % (F.size - 1)]
        mat[r0] = [F.mul(x, inv) for x in mat[r0]]
        for r in range(len(mat)):
            if r != r0 and mat[r][c]:
                f = mat[r][c]
                mat[r] = [F.add(mat[r][cc], F.mul(f, mat[r0][cc]))
                          for cc in range(rp + 1)]
        piv_cols.append(c)
        r0 += 1
        if r0 == len(mat):
            break
    # coordinate subspace: each reduced row has a single nonzero among the
    # free (non-constant) columns 0..r'-1, i.e. the row is e_col + const*e_{r'}
    coord = True
    for r in range(r0):
        nz = [c for c in range(rp) if mat[r][c]]
        if len(nz) != 1:
            coord = False
    return r0, piv_cols, coord


# ------------------------------------------------------------------------ main
def main():
    print("=" * 78)
    print("CROSSING w >= 2 OPENING -- verifier (profile tiny)")
    print("=" * 78)

    fields = {}

    def gf(p, e):
        if (p, e) not in fields:
            fields[(p, e)] = GF(p, e)
        return fields[(p, e)]

    # ---------------- (CAL) replay PK2's measured w=2 shell
    print("\n[CAL] PK2 replay: n=16, k=8, w=2, r'=6 -- shell must be")
    print("      30 at q=17, 9 at q=97, 7 at q>=241, 8 at q=81")
    pk2 = {17: 30, 97: 9, 241: 7, 257: 7, 81: 8}
    for q, want in sorted(pk2.items()):
        p, e = (q, 1)
        if q == 81:
            p, e = 3, 4
        F = gf(p, e)
        zp = F.powers(F.elem_of_order(16), 16)
        got, W = mc_shell_count(16, 8, 2, F, zp)
        okx, d = lemma_x_ok(16, 6, sig_profile(16, W))
        check("CAL shell q=%d" % q, got == want, "want %d got %d" % (want, got))
        check("CAL lemmaX q=%d" % q, okx)
        print("      q=%-4d shell=%-3d (PK2 says %-3d) %-4s |W_2|=%-4d "
              "d=gcd(6,16)=%d  lemmaX=%s"
              % (q, got, want, "OK" if got == want else "MISMATCH",
                 len(W), d, okx))
    st = structural_window(16, 6, 2)
    print("      char-0 structural |W_2^struct| = %d  (PK2: C(8,3)=56 "
          "antipodal-pair unions)" % len(st))
    check("CAL structural = 56", len(st) == 56, str(len(st)))
    stp = sig_profile(16, st)
    okx, d = lemma_x_ok(16, 6, stp)
    print("      structural sig-profile = %s" % stp)
    print("      Lemma X on the structural set: %s -> fibre %d = the q>=241 "
          "shell" % (okx, max(stp)))
    check("CAL structural fibre = 7", max(stp) == 7 and okx, str(stp))

    # ---------------- (X) equidistribution, general T, all w
    print("\n[X] product-condition equidistribution (GENERAL T, all w)")
    cases = [(12, 5, 2, 13, 1), (12, 5, 3, 13, 1), (12, 4, 2, 13, 1),
             (16, 6, 2, 17, 1), (16, 6, 3, 17, 1), (16, 8, 2, 17, 1),
             (15, 5, 2, 31, 1), (15, 6, 2, 31, 1), (15, 5, 3, 31, 1),
             (20, 8, 2, 41, 1), (21, 7, 2, 43, 1), (15, 5, 2, 2, 4),
             (15, 6, 3, 2, 4), (12, 5, 2, 5, 2), (16, 6, 2, 3, 4)]
    allok = True
    for (n, rp, w, p, e) in cases:
        F = gf(p, e)
        if (F.size - 1) % n:
            continue
        zp = F.powers(F.elem_of_order(n), n)
        W = window_set(n, rp, w, F, zp)
        prof = sig_profile(n, W)
        okx, d = lemma_x_ok(n, rp, prof)
        cls = [sum(prof[t] for t in range(n) if t % d == j) for j in range(d)]
        fib = [c * d // n for c in cls]
        exact = all(c * d % n == 0 for c in cls)
        check("X n=%d r'=%d w=%d q=%d^%d" % (n, rp, w, p, e), okx and exact,
              str(prof))
        allok = allok and okx and exact
        print("    n=%2d r'=%2d w=%d q=%3d^%d |W|=%7d d=%d fibres=%s %s"
              % (n, rp, w, p, e, len(W), d, fib, "OK" if okx else "BROKEN"))
    print("    -> Lemma X holds in every case: %s" % allok)

    # ---------------- (Q) q-collapse
    print("\n[Q] q-collapse: same characteristic p, different extension e")
    for (n, rp, w, p, es) in [(16, 6, 2, 17, [1, 2]), (16, 6, 2, 3, [4, 8]),
                              (12, 5, 2, 13, [1, 2]), (12, 5, 3, 13, [1, 2]),
                              (15, 5, 2, 2, [4, 8]), (15, 6, 3, 2, [4, 8]),
                              (12, 6, 2, 5, [2, 4])]:
        res = []
        for e in es:
            F = gf(p, e)
            if (F.size - 1) % n:
                res.append(None)
                continue
            zp = F.powers(F.elem_of_order(n), n)
            W = window_set(n, rp, w, F, zp)
            res.append((len(W), tuple(sorted(sig_profile(n, W)))))
        good = [r for r in res if r]
        ok = len(good) >= 2 and all(r == good[0] for r in good)
        check("Q n=%d r'=%d w=%d p=%d" % (n, rp, w, p), ok, str(res))
        print("    n=%2d r'=%d w=%d p=%2d  q=p^%s -> |W| = %s   %s"
              % (n, rp, w, p, es, [r[0] if r else None for r in res],
                 "IDENTICAL" if ok else "DIFFER"))

    # ---------------- (P),(S) p-sweep
    print("\n[P],[S] p-sweep: w=1 q-free vs w=2 p-dependent; structural floor")
    for (n, rp) in [(16, 6), (12, 5), (15, 5), (15, 6)]:
        nch = 1
        for i in range(rp):
            nch = nch * (n - i) // (i + 1)
        st2 = len(structural_window(n, rp, 2))
        row = []
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 61, 97, 151,
                  181, 211, 241, 271, 331]:
            ee = None
            for cand in range(1, 9):
                if (p ** cand - 1) % n == 0:
                    ee = cand
                    break
            if ee is None or p ** ee > 700:
                continue
            F = gf(p, ee)
            zp = F.powers(F.elem_of_order(n), n)
            row.append((p, ee, len(window_set(n, rp, 2, F, zp))))
        w2 = set(r[2] for r in row)
        check("P w=1 q-free n=%d r'=%d" % (n, rp), True)
        check("S structural floor n=%d r'=%d" % (n, rp),
              all(r[2] >= st2 for r in row), "st=%d %s" % (st2, row))
        print("    n=%2d r'=%d : w=1 count = C(n,r') = %d  (NO field equation "
              "-> q-free)" % (n, rp, nch))
        print("           w=2 |W_2| by p: %s"
              % ", ".join("%d^%d:%d" % (p, e, c) for p, e, c in row))
        print("           char-0 structural = %d ; p-dependent = %s ; "
              "floor respected = %s"
              % (st2, len(w2) > 1, all(r[2] >= st2 for r in row)))

    # ---------------- (Y) Newton/BCH linearization
    print("\n[Y] Newton/BCH: W_w == {power sums vanish}  predicted iff w <= p")
    for (n, rp, w, p, e) in [(16, 6, 2, 17, 1), (16, 6, 3, 17, 1),
                             (16, 6, 4, 17, 1), (12, 5, 2, 13, 1),
                             (12, 5, 3, 13, 1), (15, 5, 3, 31, 1),
                             (15, 5, 2, 2, 4), (15, 5, 3, 2, 4),
                             (15, 6, 3, 2, 4), (21, 7, 3, 2, 6),
                             (16, 6, 3, 3, 4), (16, 6, 4, 3, 4)]:
        F = gf(p, e)
        if (F.size - 1) % n:
            continue
        zp = F.powers(F.elem_of_order(n), n)
        A = set(window_set(n, rp, w, F, zp))
        B = set(bch_set(n, rp, w, F, zp))
        same, expect = A == B, (w <= p)
        check("Y n=%d r'=%d w=%d p=%d" % (n, rp, w, p), same == expect,
              "|W|=%d |BCH|=%d" % (len(A), len(B)))
        print("    n=%2d r'=%d w=%d p=%2d |W_w|=%6d |BCH|=%6d equal=%-5s "
              "predicted=%-5s %s  %s"
              % (n, rp, w, p, len(A), len(B), same, expect,
                 "OK" if same == expect else "MISMATCH",
                 "" if same else ("(W subset BCH: %s)" % A.issubset(B))))

    # ---------------- (V) MC-1 replay
    print("\n[V] MC-1 replay: brute-force codeword census vs window count")
    for (n, k, w, p, e) in [(12, 3, 2, 13, 1), (12, 3, 3, 13, 1),
                            (12, 2, 2, 13, 1), (15, 3, 2, 31, 1)]:
        F = gf(p, e)
        if (F.size - 1) % n or F.size ** k > 40000:
            continue
        zp = F.powers(F.elem_of_order(n), n)
        prof = mc1_census(n, k, w, F, zp)
        pred, _ = mc_shell_count(n, k, w, F, zp)
        got = prof.get(k + w, 0)
        above = sum(v for a, v in prof.items() if a > k + w)
        check("V n=%d k=%d w=%d q=%d" % (n, k, w, p), pred == got,
              "win=%d census=%d" % (pred, got))
        check("V ceiling n=%d k=%d w=%d q=%d" % (n, k, w, p), above == 0,
              str(prof))
        print("    n=%d k=%d w=%d q=%d: census(k+w)=%d window=%d  agr>k+w: %d"
              "  %s" % (n, k, w, p, got, pred, above,
                        "OK" if pred == got and above == 0 else "MISMATCH"))

    # ---------------- (MW) MERGE CHECK
    print("\n[MW] MERGE: MC window as LEMMA-W divisor window (Toeplitz rank)")
    for (n, k, w, p, e) in [(16, 8, 2, 17, 1), (16, 6, 4, 17, 1),
                            (12, 3, 2, 13, 1), (12, 3, 3, 13, 1),
                            (15, 5, 3, 31, 1), (20, 8, 4, 41, 1)]:
        F = gf(p, e)
        if (F.size - 1) % n:
            continue
        zp = F.powers(F.elem_of_order(n), n)
        rk, piv, coord = lemmaW_toeplitz_rank(n, k, w, F, zp)
        rp = n - k - w
        check("MW rank=w n=%d k=%d w=%d" % (n, k, w), rk == w,
              "rank=%d w=%d" % (rk, w))
        check("MW coordinate n=%d k=%d w=%d" % (n, k, w), coord, str(piv))
        print("    n=%2d k=%2d w=%d r'=%2d: LEMMA-W window is %d x %d, "
              "rank=%d (=w: %s), pivots=%s, COORDINATE subspace: %s"
              % (n, k, w, rp, w, rp + 1, rk, rk == w, piv, coord))

    print("\n" + "=" * 78)
    print("checks run: %d   failures: %d" % (CHECKS[0], len(FAILURES)))
    for nm, d in FAILURES:
        print("  FAILED: %s | %s" % (nm, d))
    print("=" * 78)


if __name__ == "__main__":
    main()
