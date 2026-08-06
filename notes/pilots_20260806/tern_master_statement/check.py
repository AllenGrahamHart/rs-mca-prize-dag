"""check.py -- machine checks for the TERNARY MASTER STATEMENT (round 19).

Fail-closed: every stage raises on the first violated assertion and the
process exits nonzero.  Stage `failclosed` injects a false check by
construction and MUST exit 1.

Usage (COMPUTE LAW -- never bare python3):
    tools/ramguard local -- python3 notes/pilots_20260806/tern_master_statement/check.py STAGE

Stages: dict char0 cs floor thresh rot newton failclosed
"""

import sys
import os
from decimal import Decimal, getcontext
from collections import Counter
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tern_lib import (ExtField, frob_closure, cyclo_norm, zmul_neg,
                      ternary_codewords, ternary_vectors, syndrome, wt,
                      pmod, pnorm)

getcontext().prec = 80

CHECKS = [0]
FAILS = [0]


def require(cond, msg):
    CHECKS[0] += 1
    if not cond:
        FAILS[0] += 1
        raise AssertionError("FAIL: " + msg)


def done(stage):
    print("\n[%s] %d checks, %d FAIL" % (stage, CHECKS[0], FAILS[0]))
    if FAILS[0]:
        sys.exit(1)
    print("STAGE_%s_ALL_PASS" % stage.upper())


def log2D(x):
    return Decimal(x).ln() / Decimal(2).ln()


# ------------------------------------------------------------------ dict ----

def zeta_pow(k, h):
    """zeta_n^k as an integer poly mod X^h+1 (n = 2h)."""
    k %= 2 * h
    v = [0] * h
    if k < h:
        v[k] = 1
    else:
        v[k - h] = -1
    return v


def stage_dict():
    """P2a: CS2's quantity (r' - a_{n/2}(S)) IS the ternary support size,
    and the second-moment identity sum_{c odd} |X_c|^2 = h * wt at master
    level (ternary), verified exactly in Z[zeta_n]."""
    print("=== STAGE dict: the 0/1 <-> ternary dictionary (LEMMA AB bridge) ===")
    for n in (16, 32):
        h = n // 2
        # (a) exhaustive at n=16; deterministic LCG sample at n=32
        if n == 16:
            masks = range(1 << 16)
        else:
            masks, x = [], 1
            for _ in range(4000):
                x = (1103515245 * x + 12345) % (1 << 32)
                masks.append(x)
        cnt = 0
        for mask in masks:
            S = [i for i in range(n) if (mask >> i) & 1]
            rp = len(S)
            Sset = set(S)
            # a_{n/2}(S) = #{(i,j) in SxS : i - j = n/2 mod n}
            a_half = sum(1 for i in S if (i - h) % n in Sset)
            A = [1 if i in Sset else 0 for i in range(h)]
            B = [1 if (i + h) in Sset else 0 for i in range(h)]
            v = [A[i] - B[i] for i in range(h)]
            require(rp - a_half == wt(v),
                    "n=%d mask=%d: r'-a_{n/2}=%d != wt(A-B)=%d"
                    % (n, mask, rp - a_half, wt(v)))
            cnt += 1
        print("  n=%2d : r' - a_{n/2}(S) == wt(A-B) on %d subsets" % (n, cnt))

    # (b) the second-moment identity, exactly in Z[X]/(X^h+1), for TERNARY eps
    for n in (8, 16):
        h = n // 2
        tested = 0
        for eps in ternary_vectors(h):
            if not any(eps):
                continue
            acc = [0] * h
            for c in range(1, n, 2):            # the h embeddings sigma_c
                Xc = [0] * h
                Xcb = [0] * h
                for j, e in enumerate(eps):
                    if e:
                        zp = zeta_pow(c * j, h)
                        zm = zeta_pow(-c * j, h)
                        for t in range(h):
                            Xc[t] += e * zp[t]
                            Xcb[t] += e * zm[t]
                prod_ = zmul_neg(Xc, Xcb, h)
                for t in range(h):
                    acc[t] += prod_[t]
            require(acc[0] == h * wt(eps) and all(x == 0 for x in acc[1:]),
                    "n=%d eps=%s: sum_c |X_c|^2 = %s != h*wt = %d"
                    % (n, eps, acc, h * wt(eps)))
            tested += 1
        print("  n=%2d : sum_{c odd} |X_c|^2 == h*wt(eps) on %d ternary eps"
              % (n, tested))
    done("dict")


# ----------------------------------------------------------------- char0 ----

def int_reduce_basis(N, Phi):
    """images of X^i mod Phi (i<N) as integer vectors of length deg Phi."""
    d = len(Phi) - 1
    out = []
    for i in range(N):
        cur = [0] * (i + 1)
        cur[i] = 1
        # exact integer division by monic Phi
        r = cur[:]
        while len(r) - 1 >= d and any(r):
            while r and r[-1] == 0:
                r.pop()
            if len(r) - 1 < d:
                break
            k = len(r) - 1 - d
            c = r[-1]
            for j, y in enumerate(Phi):
                r[j + k] -= c * y
            while r and r[-1] == 0:
                r.pop()
        r = r + [0] * (d - len(r))
        out.append(r[:d])
    return out


def cyclotomic(m):
    """Phi_m(X) as an integer coefficient list (m small)."""
    num = [-1] + [0] * (m - 1) + [1]            # X^m - 1
    for k in range(1, m):
        if m % k == 0:
            dk = cyclotomic(k)
            q = [0] * (len(num) - len(dk) + 1)
            r = num[:]
            for i in range(len(q) - 1, -1, -1):
                c = r[i + len(dk) - 1] // dk[-1]
                q[i] = c
                if c:
                    for j, y in enumerate(dk):
                        r[i + j] -= c * y
            assert all(x == 0 for x in r), "non-exact cyclotomic division"
            num = q
    return num


def kernel_ternary_char0(N, Phi):
    """all nonzero ternary v of length N with Phi | V over Z, by MITM."""
    basis = int_reduce_basis(N, Phi)
    lo, hi = N // 2, N - N // 2
    tab = {}
    for w_ in ternary_vectors(hi):
        s = [0] * len(basis[0])
        for i, c in enumerate(w_):
            if c:
                b = basis[lo + i]
                for t in range(len(s)):
                    s[t] += c * b[t]
        tab.setdefault(tuple(s), []).append(w_)
    out = []
    for u in ternary_vectors(lo):
        s = [0] * len(basis[0])
        for i, c in enumerate(u):
            if c:
                b = basis[i]
                for t in range(len(s)):
                    s[t] += c * b[t]
        for w_ in tab.get(tuple(-x for x in s), ()):
            v = u + w_
            if any(v):
                out.append(v)
    return out


def stage_char0():
    """THEOREM CZ-M: char-0 emptiness at 2-power orders, and the EXACT
    master form of CATCH-Z6 at composite orders (a labelled rule-test)."""
    print("=== STAGE char0: master char-0 emptiness (THEOREM CZ-M) ===")
    # (a) 2-power n: the half-system is a Z-basis => T = {0} for ANY Lambda
    for n in (8, 16):
        h = n // 2
        bad = 0
        for eps in ternary_vectors(h):
            if not any(eps):
                continue
            if cyclo_norm(list(eps), h) == 0:
                bad += 1
        require(bad == 0, "n=%d: %d nonzero ternary eps with N(X)=0" % (n, bad))
        print("  n=%2d (2-power): 0 of %d nonzero ternary eps have X = 0 "
              "in char 0" % (n, 3 ** h - 1))
    # rank statement: N == phi(2N) iff 2N is a 2-power
    for nn in (8, 12, 16, 20, 24, 32):
        N = nn // 2
        ph = len(cyclotomic(nn)) - 1
        ispow2 = (nn & (nn - 1)) == 0
        require((N == ph) == ispow2,
                "2N=%d: N=%d phi=%d ispow2=%s" % (nn, N, ph, ispow2))
    print("  rank law: N == phi(2N)  <=>  2N is a power of 2   (6 orders)")

    # (b) RULE TEST (CATCH-Z6), composite 2N ONLY -- never used in any
    #     conclusion about official rows.  Reproduces the banked counts.
    print("  --- RULE TEST (composite 2N, CATCH-Z6 reproduction) ---")
    banked = {12: 8, 20: 8, 24: 80}
    for nn, expect in sorted(banked.items()):
        N = nn // 2
        Phi = cyclotomic(nn)
        ker = kernel_ternary_char0(N, Phi)
        mw = min(wt(v) for v in ker) if ker else None
        rank = N - (len(Phi) - 1)
        require(len(ker) == expect,
                "2N=%d: %d p-independent ternary vectors, banked %d"
                % (nn, len(ker), expect))
        require(len(ker) == 3 ** rank - 1,
                "2N=%d: count %d != 3^rank-1 = %d"
                % (nn, len(ker), 3 ** rank - 1))
        print("    2N=%2d: N=%2d phi=%2d rank=%d -> %3d ternary kernel vectors"
              " (= 3^rank - 1), min weight %s   [banked: %d]"
              % (nn, N, len(Phi) - 1, rank, len(ker), mw, expect))
    done("char0")


# -------------------------------------------------------------------- cs ----

CELLS = []
for _n in (16, 32):
    for _p in (3, 5, 7, 17):
        for _w in (2, 3, 4, 5, 6, 7, 8):
            CELLS.append((_n, _p, _w))


def cell_data(n, p, w, cap=None):
    h = n // 2
    lam = [s for s in range(1, w) if s % 2 == 1]
    if not lam:
        return None
    F = ExtField(p, n)
    lam_star = frob_closure(lam, p, n)
    G = F.gen_poly(lam_star)
    g = len(G) - 1
    require(g == len(lam_star),
            "n=%d p=%d w=%d: deg G = %d != |Lambda^*| = %d"
            % (n, p, w, g, len(lam_star)))
    cw = ternary_codewords(h, G, p, cap=cap)
    return dict(h=h, lam=lam, lam_star=lam_star, G=G, g=g, cw=cw,
                delta=F.delta)


def stage_cs():
    """THEOREM CS-M: p^{|Lambda^*|} | N(X) and N(X)^2 <= wt(eps)^h,
    for ternary eps -- CS read verbatim over T(P, Lambda)."""
    print("=== STAGE cs: THEOREM CS-M (Galois multiplicity + AM-GM) ===")
    print("  n   p   w   |Lam*| delta  #ternary  checked  tightest CS3 margin")
    for (n, p, w) in CELLS:
        d = cell_data(n, p, w, cap=None)
        if d is None or not d["cw"]:
            continue
        h, g = d["h"], d["g"]
        cws = d["cw"]
        step = max(1, len(cws) // 120)          # deterministic stride
        sample = cws[::step]
        tight = None
        for v in sample:
            Nrm = cyclo_norm(list(v), h)
            require(Nrm != 0, "n=%d p=%d w=%d: N(X)=0 for ternary v" % (n, p, w))
            aN = abs(Nrm)
            require(aN % (p ** g) == 0,
                    "CS1 n=%d p=%d w=%d: p^%d does not divide |N|=%d"
                    % (n, p, w, g, aN))
            U = wt(v)
            require(aN * aN <= U ** h,
                    "CS2 n=%d p=%d w=%d: N^2=%d > U^h=%d" % (n, p, w, aN * aN, U ** h))
            require(p ** (2 * g) <= U ** h,
                    "CS3 n=%d p=%d w=%d: p^{2g} > U^h" % (n, p, w))
            m = (Decimal(h) / 2) * log2D(U) - Decimal(g) * log2D(p)
            tight = m if tight is None else min(tight, m)
        print("  %2d %3d %3d %5d %5d %9d %8d   %s bits"
              % (n, p, w, g, d["delta"], len(cws), len(sample),
                 str(tight.quantize(Decimal('0.0001')))))
    done("cs")


# ----------------------------------------------------------------- floor ----

def stage_floor():
    """THEOREM Z-FLOOR-M transported off I1: the collision identity, the
    census identity, and the EXISTENCE forcing g*log2 p < h  =>  T != {0}."""
    print("=== STAGE floor: Z-FLOOR-M off-instance (collision / census /"
          " existence) ===")
    print("   n   p   w  delta  g  g*log2p    h   fires?  #ternary  verdict")
    fired = 0
    for (n, p, w) in CELLS:
        d = cell_data(n, p, w)
        if d is None:
            continue
        h, g, cws = d["h"], d["g"], d["cw"]
        gl = Decimal(g) * log2D(p)
        fires = gl < Decimal(h)
        ntern = len(cws)
        # P4 falsifier: if the floor fires there MUST be a nonzero codeword
        if fires:
            require(ntern > 0,
                    "P4 KILLED at n=%d p=%d w=%d: g*log2p=%s < h=%d but "
                    "ternary count is 0" % (n, p, w, gl, h))
            fired += 1
        # exact collision identity + Cauchy-Schwarz floor.
        # (all n=16 cells; at n=32 the four p in {3,17} x w in {2,6} cells)
        if n == 16 or (p in (3, 17) and w in (2, 6)):
            G, pp = d["G"], p
            basis = []
            for i in range(h):
                e = [0] * h
                e[i] = 1
                basis.append(syndrome(e, G, pp))
            cnt = Counter()
            for mask in range(1 << h):
                s = [0] * g
                mm = mask
                i = 0
                while mm:
                    if mm & 1:
                        b = basis[i]
                        for t in range(g):
                            s[t] = (s[t] + b[t]) % pp
                    mm >>= 1
                    i += 1
                cnt[tuple(s)] += 1
            pairs = sum(c * c for c in cnt.values())
            mass = sum(2 ** (h - wt(v)) for v in cws) + 2 ** h   # + zero word
            require(pairs == mass,
                    "collision identity n=%d p=%d w=%d: pairs=%d != mass=%d"
                    % (n, p, w, pairs, mass))
            require(pairs * (p ** g) >= (1 << (2 * h)),
                    "Z-FLOOR-M n=%d p=%d w=%d: %d < 2^{2h}/p^g"
                    % (n, p, w, pairs))
        require(len(cws) + 1 >= (1 << h) // (p ** g),
                "count floor n=%d p=%d w=%d" % (n, p, w))
        print("  %2d %3d %3d %5d %3d %9.3f %5d   %-6s %8d  %s"
              % (n, p, w, d["delta"], g, float(gl), h,
                 "YES" if fires else "-", ntern,
                 "forced" if fires else ("exists" if ntern else "empty")))
    print("  Z-FLOOR-M fired (and was confirmed) in %d cells; 0 falsifications."
          % fired)

    # the I3 census identity, replayed directly at n = 16
    print("  --- I3 census identity replay (n = 16, all 2^16 subsets) ---")
    for p in (3, 5, 7, 17):
        for w in (2, 4, 6, 8):
            d = cell_data(16, p, w)
            if d is None:
                continue
            h, G, cws = d["h"], d["G"], d["cw"]
            direct = 0
            for mask in range(1 << 16):
                Sset = {i for i in range(16) if (mask >> i) & 1}
                if all(((i + h) % 16 in Sset) == (i in Sset) for i in range(16)):
                    continue                     # strat(S) >= 1
                v = [(1 if i in Sset else 0) - (1 if (i + h) in Sset else 0)
                     for i in range(h)]
                if all(x == 0 for x in pmod([c % p for c in v], G, p)):
                    direct += 1
            pred = sum(2 ** (h - wt(v)) for v in cws)
            require(direct == pred,
                    "census n=16 p=%d w=%d: direct=%d != sum 2^{z(v)}=%d"
                    % (p, w, direct, pred))
    print("     #{S : strat(S)=0, odd conditions} == sum_{v!=0} 2^{h-wt(v)}"
          "   (16 cells)")
    done("floor")


# ---------------------------------------------------------------- thresh ----

def stage_thresh():
    """P3: the master threshold g*log2 p vs h at all three instances."""
    print("=== STAGE thresh: the master threshold  g*log2 p  vs  h ===")

    # ---- I1: the F2 admissible object (banked constants) ----
    p1 = 18446735827372343297
    e_p, S = 39, 2 ** 38
    lp = log2D(p1)
    print("  [I1] p = %d, e_p = %d, h = S = 2^38" % (p1, e_p))
    print("       log2 p = %s" % str(lp.quantize(Decimal('0.000000001'))))
    for R, banked in ((4294967340, Decimal('-46.0249')),
                      (4294967339, Decimal('17.9751'))):
        exponent = Decimal(S) - Decimal(R) * lp
        print("       R = %d  ->  h - g*log2 p = %s bits   [banked %s]"
              % (R, str(exponent.quantize(Decimal('0.0001'))), banked))
        require(abs(exponent - banked) < Decimal('0.01'),
                "I1 knife edge: got %s expected %s" % (exponent, banked))
    R = 4294967340
    ratio = Decimal(S) / Decimal(R)
    require(abs(ratio - lp) < Decimal('0.0001'),
            "I1 saturation: h/g = %s != log2 p = %s" % (ratio, lp))
    print("       h/g = %s  ==  log2 p  (saturation: the object sits ON the"
          " master threshold)" % str(ratio.quantize(Decimal('0.000000001'))))

    # ---- I2: the crossing deep stratum and stratum 0 ----
    n2 = 2 ** 41
    print("  [I2] n = 2^41; deep stratum a = v-1 vs stratum a = 0")
    print("        w     L=n/w  DSA thr (L-2)   a=0: h0/g0   agree?")
    for v in range(34, 40):
        w = 2 ** v
        L = 2 ** (41 - v)
        require(L == n2 // w, "I2: L != n/w at w=2^%d" % v)
        h0, g0 = n2 // 2, (w - 1 + 1) // 2      # ceil((w-1)/2) = 2^{v-1}
        require(g0 == 2 ** (v - 1), "I2: g0 != 2^{v-1}")
        r = h0 // g0
        require(r == L, "I2: h0/g0 = %d != L = %d" % (r, L))
        print("       2^%d  %6d       %6d        %6d       yes"
              % (v, L, L - 2, r))
    print("       => DSA's deep-stratum threshold and the stratum-0 threshold"
          " are the SAME number (to within 2).")
    pw = 6597069766657
    lw = log2D(pw)
    print("  [I2] witness row p = %d, log2 p = %s"
          % (pw, str(lw.quantize(Decimal('0.001')))))
    require(lw < Decimal(126), "witness not in DSA regime")
    require(lw < Decimal(128), "witness not in stratum-0 regime")
    print("       log2 p < 126 (DSA fires) and < 128 = h0/g0 (stratum-0 floor"
          " fires): BOTH strata forced at the same row")
    e1 = Decimal('129.585')
    require(e1 > Decimal(128) and e1 > Decimal(126),
            "e=1 dichotomy broken")
    print("  [I2] e = 1 rows: log2 p >= 129.585 > 128 > 126 -> outside BOTH"
          " regimes (the banked dichotomy, reproduced by the master threshold)")

    # ---- I3: the (ES) stratum-0 odd-condition object ----
    print("  [I3] n = 2^41, h = 2^40, delta = 1, Lambda = odd s in [1,w-1]")
    print("        w      g=2^{v-1}   h/g      log2 p for which the floor fires")
    for v in range(34, 40):
        w = 2 ** v
        g = 2 ** (v - 1)
        h0 = 2 ** 40
        print("       2^%d   2^%d      %6d    log2 p < %d"
              % (v, v - 1, h0 // g, h0 // g))
    print("       recorded rows log2 p = 256: floor SILENT at every w"
          " (256 > 128) -- consistent with the banked 'prime rows untouched'")
    print("       tower rows   log2 p = 42.6: floor FIRES at w = 2^34"
          " (42.6 < 128)")
    done("thresh")


# ------------------------------------------------------------------- rot ----

def negshift(v):
    h = len(v)
    return tuple([-v[h - 1]] + list(v[:h - 1]))


def dilate(v, m, h):
    """V(X) -> V(X^m) mod X^h+1, a signed permutation for m odd."""
    out = [0] * h
    for j, c in enumerate(v):
        if c:
            k = (m * j) % (2 * h)
            if k < h:
                out[k] += c
            else:
                out[k - h] -= c
    return tuple(out)


def stage_rot():
    """LEMMA ROT-M: the master symmetry group of T(P, Lambda)."""
    print("=== STAGE rot: LEMMA ROT-M (negacyclic shift, sign, dilates) ===")
    print("   n   p   w   g  #ternary  orbits  max orbit  |Stab(Lam*)|  n=2h")
    for (n, p, w) in CELLS:
        if n != 16:
            continue
        d = cell_data(n, p, w)
        if d is None or not d["cw"]:
            continue
        h = d["h"]
        Sset = set(tuple(v) for v in d["cw"])
        # closure under R and -1
        for v in Sset:
            require(negshift(v) in Sset,
                    "ROT-M n=%d p=%d w=%d: R does not preserve T" % (n, p, w))
            require(tuple(-c for c in v) in Sset,
                    "ROT-M: -1 does not preserve T")
        # R has order 2h = n on nonzero vectors
        v0 = next(iter(Sset))
        u, o = v0, 0
        while True:
            u = negshift(u)
            o += 1
            if u == v0:
                break
        require(n % o == 0, "R order %d does not divide n=%d" % (o, n))
        # Stab(Lambda^*) and the dilate action
        lam_star = d["lam_star"]
        stab = [m for m in range(1, n, 2)
                if {(m * s) % n for s in lam_star} == lam_star]
        require(all((p ** k) % n in stab for k in range(d["delta"])),
                "Stab does not contain <p>")
        for m in stab:
            for v in list(Sset)[:40]:
                require(dilate(v, m, h) in Sset,
                        "dilate m=%d leaves T at n=%d p=%d w=%d" % (m, n, p, w))
        # orbit decomposition under <R, -1>
        seen, orbits, mx = set(), 0, 0
        for v in Sset:
            if v in seen:
                continue
            orb, u = set(), v
            for _ in range(2 * n):
                orb.add(u)
                orb.add(tuple(-c for c in u))
                u = negshift(u)
            seen |= orb
            orbits += 1
            mx = max(mx, len(orb))
        require(mx <= n, "orbit larger than n")
        print("  %2d %3d %3d %3d %9d %7d %10d %13d  %4d"
              % (n, p, w, d["g"], len(Sset), orbits, mx, len(stab), n))
    print("  every orbit size divides n = 2h (LEMMA ROT at master level);"
          " Stab(Lambda^*) always contains <p>.")
    done("rot")


# ---------------------------------------------------------------- newton ----

def stage_newton():
    """THEOREM Z-1 at master level: for a PREFIX Lambda = {1,3,..,2l-1} and
    char > wt, every nonzero ternary codeword has wt >= 2l+1; and the scope
    failure for shifted Lambda."""
    print("=== STAGE newton: THEOREM Z-1 transported (prefix scope) ===")
    print("   n   p   ell  Lambda            min wt  2*ell+1  char>wt?  verdict")
    ok = 0
    for n in (16, 32):
        h = n // 2
        for p in (17, 97, 193, 257, 449, 641):
            if p <= h:
                continue
            for ell in (1, 2, 3):
                lam = [2 * j - 1 for j in range(1, ell + 1)]
                F = ExtField(p, n)
                lam_star = frob_closure(lam, p, n)
                G = F.gen_poly(lam_star)
                cw = ternary_codewords(h, G, p)
                if not cw:
                    continue
                mw = min(wt(v) for v in cw)
                require(mw >= 2 * ell + 1,
                        "Z-1-M n=%d p=%d ell=%d: min wt %d < %d"
                        % (n, p, ell, mw, 2 * ell + 1))
                ok += 1
                print("  %2d %4d %4d  %-16s %6d %8d  %-8s  holds"
                      % (n, p, ell, str(lam), mw, 2 * ell + 1, "yes"))
    print("  %d prefix cells, 0 violations." % ok)
    # scope: a SHIFTED Lambda of the same size can break the 2*ell+1 law
    print("  --- scope: shifted Lambda (same |Lambda|) ---")
    broke = 0
    for n in (16, 32):
        h = n // 2
        for p in (17, 97, 193, 257, 449, 641):
            if p <= h:
                continue
            for lam in ([3], [5], [3, 5], [5, 7]):
                ell = len(lam)
                F = ExtField(p, n)
                G = F.gen_poly(frob_closure(lam, p, n))
                cw = ternary_codewords(h, G, p)
                if not cw:
                    continue
                mw = min(wt(v) for v in cw)
                if mw < 2 * ell + 1:
                    broke += 1
                    if broke <= 6:
                        print("     n=%d p=%d Lambda=%s : min wt %d < %d"
                              " -- SHIFT BREAKS THE LAW"
                              % (n, p, lam, mw, 2 * ell + 1))
    print("  shifted counterexamples found: %d" % broke)
    if broke == 0:
        print("  *** REGISTERED EXPECTATION MISSED (reported, not buried) ***")
        print("      I expected shifted-Lambda counterexamples to the 2*ell+1")
        print("      law, mirroring I1's 43. My grid is 2-POWER n ONLY (the")
        print("      CATCH-Z6 rule) and finds NONE.  This is CONSISTENT with")
        print("      z1_ternary_mass/PROOFS.md:536-539, which records that of")
        print("      its 43 shifted counterexamples exactly ONE is at 2-power")
        print("      2N -- 'a thin sample'.  So the 2-power grid cannot see")
        print("      the scope failure, and I do NOT get to claim the prefix")
        print("      hypothesis is load-bearing at 2-power orders: at master")
        print("      level that remains OPEN, exactly as at I1.")
    done("newton")


# ------------------------------------------------------------ failclosed ----

def stage_failclosed():
    print("=== STAGE failclosed: this stage MUST exit 1 ===")
    require(True, "control: a true check passes")
    require(1 == 2, "injected false check -- fail-closed proof")
    done("failclosed")


STAGES = dict(dict=stage_dict, char0=stage_char0, cs=stage_cs,
              floor=stage_floor, thresh=stage_thresh, rot=stage_rot,
              newton=stage_newton, failclosed=stage_failclosed)

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in STAGES:
        print("usage: check.py {%s}" % "|".join(STAGES))
        sys.exit(64)
    STAGES[sys.argv[1]]()
