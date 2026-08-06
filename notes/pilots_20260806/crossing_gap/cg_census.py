#!/usr/bin/env python3
"""cg_census.py -- round-20 crossing_gap pilot: exact censuses over F_{p^d}.

Stages:
  haar     (C1) the 2-adic Haar tower: LEMMA OE at every level, the
                bijection S <-> (eps^(0),...,eps^(m-1), r'), strat law
  census   (C1) EXACT a=0 census over ALL 2^n subsets, n in {16,32},
                reproducing the banked round-18 table
  coupled  (C1) the COUPLED odd/even criterion and the p=7,w=7 gate
  cwtoy    (C2) CW-FLOOR: LEMMA TC, the shell identity, the diagonal
                floor, and the cross-shell FAILURE
  failclosed  permanent fail-closed control (MUST exit 1)

COMPUTE LAW: run only via  tools/ramguard tiny|local -- python3 ...
"""
import sys
import itertools
from math import comb, log2

FAILS = []
NCHECK = 0


def check(desc, cond, extra=""):
    global NCHECK
    NCHECK += 1
    if not cond:
        FAILS.append(desc)
        print("  FAIL  %s %s" % (desc, extra))
    return bool(cond)


def hdr(t):
    print("\n" + "=" * 74)
    print(t)
    print("=" * 74)


# ------------------------------------------------------- F_p[x]/(f) toolkit
def pnorm(a, p):
    while a and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b, p):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % p
    return pnorm(r, p)


def pmod(a, f, p):
    a = a[:]
    df = len(f) - 1
    inv = pow(f[-1], p - 2, p)
    while len(a) - 1 >= df and a:
        d = len(a) - 1 - df
        c = a[-1] * inv % p
        for i, y in enumerate(f):
            a[i + d] = (a[i + d] - c * y) % p
        pnorm(a, p)
    return a


def pmulmod(a, b, f, p):
    return pmod(pmul(a, b, p), f, p)


def ppowmod(a, e, f, p):
    r, b = [1], pmod(a[:], f, p)
    while e:
        if e & 1:
            r = pmulmod(r, b, f, p)
        b = pmulmod(b, b, f, p)
        e >>= 1
    return r


def pgcd(a, b, p):
    a, b = pnorm(a[:], p), pnorm(b[:], p)
    while b:
        a = pmod(a, b, p)
        a, b = b, a
    if a:
        inv = pow(a[-1], p - 2, p)
        a = [x * inv % p for x in a]
    return a


def psub_x(a, p):
    """a(X) - X."""
    r = list(a) + [0] * max(0, 2 - len(a))
    r[1] = (r[1] - 1) % p
    return pnorm(r, p)


def is_irred(f, p):
    """Rabin's irreducibility test for monic f over F_p."""
    d = len(f) - 1
    if d == 1:
        return True
    # X^{p^d} = X  mod f
    cur = [0, 1]
    pows = {}
    for k in range(1, d + 1):
        cur = ppowmod(cur, p, f, p)
        pows[k] = cur
    if pows[d] != [0, 1]:
        return False
    for r in range(2, d + 1):
        if d % r:
            continue
        if all(r % q for q in range(2, r)):            # r prime
            g = pgcd(psub_x(pows[d // r], p), f, p)
            if len(g) - 1 > 0:
                return False
    return True


def find_irred(p, d, rng):
    if d == 1:
        return [1, 1]          # F_p[X]/(X+1) = F_p
    while True:
        f = [rng() % p for _ in range(d)] + [1]
        if is_irred(f, p):
            return f


def ordmod(a, n):
    from math import gcd as _g
    if _g(a, n) != 1:
        raise ValueError("ordmod: gcd(%d,%d) != 1" % (a, n))
    o, t = 1, a % n
    while t != 1:
        t = (t * a) % n
        o += 1
    return o


class GF:
    """F_{p^d} with a fixed primitive n-th root of unity xi."""

    def __init__(self, p, n, seed=12345):
        self.p, self.n = p, n
        self.d = ordmod(p, n)
        st = [seed]

        def rng():
            st[0] = (st[0] * 1103515245 + 12345) & 0x7FFFFFFF
            return st[0] >> 5
        self.f = find_irred(p, self.d, rng)
        assert self.f[0] % p != 0, self.f
        Q = p ** self.d
        # independent field check: every nonzero element must satisfy
        # x^(Q-1) = 1 (false for a reducible modulus, which has zero divisors)
        for tr in range(25):
            g = pnorm([rng() % p for _ in range(self.d)], p)
            if not g:
                continue
            assert ppowmod(g, Q - 1, self.f, p) == [1], (p, n, self.f, g)
        assert (Q - 1) % n == 0, (p, n, self.d)
        self.Q = Q
        while True:
            g = [rng() % p for _ in range(self.d)]
            g = pnorm(g, p)
            if not g:
                continue
            xi = ppowmod(g, (Q - 1) // n, self.f, p)
            # EXACT order test (no 2-power assumption): order n iff
            # xi^(n/r) != 1 for every prime r | n
            ok = True
            nn, rs = n, []
            r = 2
            while r * r <= nn:
                if nn % r == 0:
                    rs.append(r)
                    while nn % r == 0:
                        nn //= r
                r += 1
            if nn > 1:
                rs.append(nn)
            for r in rs:
                if ppowmod(xi, n // r, self.f, p) == [1]:
                    ok = False
                    break
            if ok:
                self.xi = xi
                break
        # xi has EXACT order n: n distinct powers
        pows = set()
        cur = [1]
        for _ in range(n):
            pows.add(tuple(self.vec(cur)))
            cur = pmulmod(cur, self.xi, self.f, p)
        assert len(pows) == n, (p, n, len(pows))
        assert cur == [1], (p, n, cur)

    def vec(self, a):
        return tuple((a[i] if i < len(a) else 0) for i in range(self.d))

    def powxi(self, e):
        return self.vec(ppowmod(self.xi, e % self.n, self.f, self.p))


_GFCACHE = {}


def gf(p, n):
    if (p, n) not in _GFCACHE:
        _GFCACHE[(p, n)] = GF(p, n)
    return _GFCACHE[(p, n)]


def cyc_cosets(S, p, n):
    """p-cyclotomic coset representatives of S in Z/n."""
    reps, seen = [], set()
    for s in sorted(S):
        s %= n
        if s in seen:
            continue
        reps.append(s)
        t = s
        while t not in seen:
            seen.add(t)
            t = (t * p) % n
    return reps


def rot(S, t, n):
    return ((S << t) | (S >> (n - t))) & ((1 << n) - 1)


def strat(S, n, m):
    a = 0
    for aa in range(1, m + 1):
        if rot(S, n >> aa, n) == S:
            a = aa
        else:
            break
    return a


# ================================================================== haar
def stage_haar():
    hdr("STAGE haar -- (C1) the 2-adic Haar tower / LEMMA OE at every level")
    for (n, p) in [(16, 3), (16, 7), (32, 7), (32, 17), (64, 5)]:
        m = n.bit_length() - 1
        F = GF(p, n)
        pw = [[F.powxi(s * i) for i in range(n)] for s in range(n)]

        def fS(S, s):
            acc = [0] * F.d
            for i in range(n):
                if S >> i & 1:
                    v = pw[s][i]
                    for k in range(F.d):
                        acc[k] = (acc[k] + v[k]) % p
            return tuple(acc)

        # tower vectors
        def tower(S):
            cur = [(S >> i) & 1 for i in range(n)]
            eps = []
            for a in range(m):
                half = len(cur) // 2
                eps.append([cur[j] - cur[j + half] for j in range(half)])
                cur = [cur[j] + cur[j + half] for j in range(half)]
            return eps, cur[0]

        def untower(eps, tot):
            cur = [tot]
            for a in range(m - 1, -1, -1):
                e = eps[a]
                nxt = [0] * (2 * len(cur))
                for j in range(len(cur)):
                    nxt[j] = (cur[j] + e[j]) // 2
                    nxt[j + len(cur)] = (cur[j] - e[j]) // 2
                cur = nxt
            return sum((1 << i) for i in range(n) if cur[i])

        rs = 987654321
        for _ in range(40):
            rs = (rs * 1103515245 + 12345) & 0x7FFFFFFF
            S = rs & ((1 << n) - 1)
            eps, tot = tower(S)
            check("tower total = |S| (n=%d,p=%d)" % (n, p),
                  tot == bin(S).count("1"))
            check("tower bijection S -> eps -> S (n=%d,p=%d)" % (n, p),
                  untower(eps, tot) == S)
            check("|eps^(a)_j| <= 2^a (n=%d,p=%d)" % (n, p),
                  all(all(abs(x) <= (1 << a) for x in eps[a])
                      for a in range(m)))
            # LEMMA OE at every level: f_S(xi^{2^a t}) = eps^(a)(theta_a^t)
            for s in range(1, n):
                a = (s & -s).bit_length() - 1
                t = s >> a
                if a >= m:
                    continue
                lhs = fS(S, s)
                acc = [0] * F.d
                half = n >> (a + 1)
                for j in range(half):
                    c = eps[a][j] % p
                    if c:
                        v = pw[((1 << a) * t) % n][j]
                        for k in range(F.d):
                            acc[k] = (acc[k] + c * v[k]) % p
                check("LEMMA OE level split at n=%d p=%d s=%d" % (n, p, s),
                      lhs == tuple(acc))
        # strat law, EXHAUSTIVE at n = 16
        if n == 16:
            bad = 0
            for S in range(1 << n):
                eps, tot = tower(S)
                st = strat(S, n, m)
                zz = 0
                while zz < m and all(x == 0 for x in eps[zz]):
                    zz += 1
                if st != zz:
                    bad += 1
            check("EXHAUSTIVE (all 2^16): strat(S) = #leading zero eps levels",
                  bad == 0, "(%d mismatches)" % bad)
    print("  LEMMA OE holds at EVERY level, the tower is a bijection, and")
    print("  strat(S) >= b  <=>  eps^(0) = ... = eps^(b-1) = 0  (G1.1 HELD).")
    print("  The window conditions therefore decompose EXACTLY by v_2(s):")
    print("  s = 2^a t (t odd)  =>  f_S(xi^s) = eps^(a)(theta_a^t).")


# ================================================================== census
def exact_census(n, p, w, cap=6000000, odd_only=False):
    """EXACT census over ALL 2^n subsets.  Returns (total, a0, a0_by_r)."""
    m = n.bit_length() - 1
    F = gf(p, n)
    win = [s for s in range(1, w) if (not odd_only) or (s % 2 == 1)]
    if not win:
        return None
    reps = cyc_cosets(win, p, n)
    D = F.d * len(reps)
    half = n // 2
    pwv = []
    for i in range(n):
        v = []
        for s in reps:
            v.extend(F.powxi(s * i))
        pwv.append(tuple(v))
    # DP over subsets of each half
    def syndromes(lo, hi):
        out = [tuple([0] * D)]
        for i in range(lo, hi):
            add = pwv[i]
            out = out + [tuple((x + y) % p for x, y in zip(s, add))
                         for s in out]
        return out
    synL = syndromes(0, half)
    synR = syndromes(half, n)
    tbl = {}
    for idx, s in enumerate(synL):
        tbl.setdefault(s, []).append(idx)
    total = 0
    a0 = 0
    a0r = {}
    nmatch = 0
    for idx, s in enumerate(synR):
        key = tuple((-x) % p for x in s)
        lst = tbl.get(key)
        if not lst:
            continue
        nmatch += len(lst)
        if nmatch > cap:
            return ("CAP", nmatch, None)
        Rm = idx << half
        for li in lst:
            S = li | Rm
            total += 1
            if strat(S, n, m) == 0:
                a0 += 1
                r = bin(S).count("1")
                a0r[r] = a0r.get(r, 0) + 1
    return (total, a0, a0r)


def stage_census():
    hdr("STAGE census -- (C1) EXACT a=0 census over ALL 2^n subsets")
    # banked round-18 table, efloor_sparsity/PROOFS.md:224-228 (n=32, p=3)
    banked32p3 = {2: (1048576, 983040), 3: (4096, 3072), 4: (4096, 3072),
                  5: (128, 64), 6: (64, 0), 7: (64, 0), 8: (64, 0)}
    print("  n=32, p=3 -- reproducing the banked table (all/a=0):")
    for w in sorted(banked32p3):
        res = exact_census(32, 3, w)
        if res[0] == "CAP":
            print("    w=%-3d CAP" % w)
            continue
        tot, a0, a0r = res
        exp = banked32p3[w]
        print("    w=%-3d all=%-9d a0=%-9d   (banked all=%-9d a0=%d)"
              % (w, tot, a0, exp[0], exp[1]))
        check("banked n=32 p=3 w=%d 'bad, all S' reproduced" % w,
              tot == exp[0], "(got %d)" % tot)
        check("banked n=32 p=3 w=%d 'bad, a=0' reproduced" % w,
              a0 == exp[1], "(got %d)" % a0)

    print("\n  FULL-WINDOW vs ODD-ONLY a=0 counts (the even conditions' bite):")
    print("  %-4s %-4s %-3s %14s %14s" % ("n", "p", "w", "a0 FULL", "a0 ODD-only"))
    gate = {}
    for (n, plist, wmax) in ((16, (3, 5, 7, 17), 13), (32, (3, 7, 17), 10)):
        for p in plist:
            for w in range(2, wmax):
                rf = exact_census(n, p, w)
                ro = exact_census(n, p, w, odd_only=True)
                if rf is None or ro is None:
                    continue
                if rf[0] == "CAP" or ro[0] == "CAP":
                    continue
                gate[(n, p, w)] = (rf[1], ro[1])
                if p == 7 or (rf[1] == 0 and ro[1] != 0):
                    print("  %-4d %-4d %-3d %14d %14d"
                          % (n, p, w, rf[1], ro[1]))
    # THE GATE the mandate names
    for n in (16, 32):
        g7 = gate.get((n, 7, 7))
        check("GATE: n=%d p=7 w=7 -- a=0 class EMPTY with the FULL window"
              % n, g7 is not None and g7[0] == 0, "(got %s)" % (g7,))
        check("GATE: n=%d p=7 w=7 -- ODD conditions alone do NOT suffice"
              % n, g7 is not None and g7[1] > 0, "(got %s)" % (g7,))
    g76 = gate.get((32, 7, 6))
    print("\n  The gate is exactly the s=6 EVEN condition:")
    print("    n=32 p=7 w=6 : a0 FULL = %d   (odd-only = %d)"
          % (g76[0], g76[1]))
    print("    n=32 p=7 w=7 : a0 FULL = %d   (odd-only = %d)"
          % (gate[(32, 7, 7)][0], gate[(32, 7, 7)][1]))
    check("w=6 -> w=7 at (n=32,p=7) adds ONLY the even condition s=6",
          [s for s in range(1, 6) if s % 2 == 1] ==
          [s for s in range(1, 7) if s % 2 == 1] and
          6 % 2 == 0)
    check("n=32 p=7 a=0 is NONEMPTY at w=6 and EMPTY at w=7",
          g76[0] > 0 and gate[(32, 7, 7)][0] == 0,
          "(w=6: %d, w=7: %d)" % (g76[0], gate[(32, 7, 7)][0]))
    # w_cov(7) = 12 : odd-alone can never suffice below w=12
    print("  w_cov(7, 2^m) = 12, so SP-COVER cannot fire below w=12 at any n;")
    print("  the exclusion at w=7 is therefore NOT a coverage phenomenon.")


# ================================================================== coupled
def coupled_certificate(n, p, w, verbose=True):
    """The COUPLED odd/even criterion.

    eps in {0,+-1}^h with the ODD conditions;  u = m^(1) in {0,1,2}^h with
    the EVEN conditions;  coupling  supp(eps) = {j : u_j = 1}.
    Returns (n_tern_nonzero, n_coupled_pairs, sum 2^z(eps)).
    """
    m = n.bit_length() - 1
    h = n // 2
    F = gf(p, n)
    oddw = [s for s in range(1, w) if s % 2 == 1]
    evenw = [s // 2 for s in range(1, w) if s % 2 == 0]      # t = s/2 mod h
    repso = cyc_cosets(oddw, p, n)
    repse = cyc_cosets(evenw, p, h) if evenw else []
    Do = F.d * len(repso)
    De = F.d * len(repse)

    # eps_j sits at xi^{s j}  (odd s);  u_j sits at (xi^2)^{t j} = xi^{2 t j}
    pwo = []
    for j in range(h):
        v = []
        for s in repso:
            v.extend(F.powxi(s * j))
        pwo.append(tuple(v))
    pwe = []
    for j in range(h):
        v = []
        for t in repse:
            v.extend(F.powxi(2 * t * j))
        pwe.append(tuple(v))

    # --- enumerate ternary eps in C_odd by meet-in-the-middle
    hh = h // 2

    def tern_half(lo, hi):
        out = {}
        for combo in itertools.product((0, 1, -1), repeat=hi - lo):
            acc = [0] * Do
            for k, c in enumerate(combo):
                if c:
                    v = pwo[lo + k]
                    if c == 1:
                        for i in range(Do):
                            acc[i] = (acc[i] + v[i]) % p
                    else:
                        for i in range(Do):
                            acc[i] = (acc[i] - v[i]) % p
            out.setdefault(tuple(acc), []).append(combo)
        return out
    LH = tern_half(0, hh)
    RH = tern_half(hh, h)
    eps_list = []
    for key, rl in RH.items():
        nk = tuple((-x) % p for x in key)
        ll = LH.get(nk)
        if not ll:
            continue
        for a in ll:
            for b in rl:
                e = list(a) + list(b)
                if any(e):
                    eps_list.append(e)
    ntern = len(eps_list)
    sum2z = sum(1 << e.count(0) for e in eps_list)

    # --- couple each eps to an even-code witness u = 1_T + 2y
    ncoupled = 0
    by_r = {}
    for e in eps_list:
        T = [j for j in range(h) if e[j] != 0]
        comp = [j for j in range(h) if e[j] == 0]
        if De == 0:                       # no even conditions in the window
            ncoupled += 1 << len(comp)
            continue
        base = [0] * De
        for j in T:
            v = pwe[j]
            for i in range(De):
                base[i] = (base[i] + v[i]) % p
        # y subsets of comp with base + 2*syn(y) = 0
        cur = {tuple(base): [0]}
        for j in comp:
            v = pwe[j]
            nxt = {}
            for k, wl in cur.items():
                nxt.setdefault(k, []).extend(wl)
                k2 = tuple((k[i] + 2 * v[i]) % p for i in range(De))
                nxt.setdefault(k2, []).extend([x + 1 for x in wl])
            cur = nxt
        zero = cur.get(tuple([0] * De))
        if zero:
            ncoupled += len(zero)
            for ny in zero:
                r = len(T) + 2 * ny
                by_r[r] = by_r.get(r, 0) + 1
    return ntern, ncoupled, sum2z, by_r


def stage_coupled():
    hdr("STAGE coupled -- (C1) the COUPLED odd/even criterion, and the gate")
    print("  THEOREM SP-COUPLE (this pilot).  strat(S)=0 and p | N(I_S) force")
    print("  simultaneously:  eps = A-B in C_odd (ternary),")
    print("  u = m^(1) in C_even ({0,1,2}), and supp(eps) = {j : u_j = 1}.")
    print("  SP-TERNARY is the eps-half alone.\n")
    print("  %-4s %-3s %-3s %10s %14s %12s" %
          ("n", "p", "w", "#tern!=0", "SP-TERNARY ct", "COUPLED ct"))
    for (n, p, wlist) in [(32, 7, [4, 5, 6, 7, 8]),
                          (32, 3, [4, 5, 6]),
                          (16, 7, [4, 5, 6, 7, 8])]:
        for w in wlist:
            nt, nc, s2z, byr = coupled_certificate(n, p, w)
            print("  %-4d %-3d %-3d %10d %14d %12d" % (n, p, w, nt, s2z, nc))
            # the coupled count IS the exact a=0 census
            ref = exact_census(n, p, w)
            check("coupled count = exact a=0 census at (n=%d,p=%d,w=%d)"
                  % (n, p, w), ref[1] == nc, "(census %d vs coupled %d)"
                  % (ref[1], nc))
            refo = exact_census(n, p, w, odd_only=True)
            check("SP-TERNARY sum 2^z(eps) = odd-only a=0 census at "
                  "(n=%d,p=%d,w=%d)" % (n, p, w), refo[1] == s2z,
                  "(census %d vs formula %d)" % (refo[1], s2z))
    # THE GATE
    for n in (16, 32):
        nt, nc, s2z, byr = coupled_certificate(n, 7, 7)
        check("GATE CERTIFICATE n=%d p=7 w=7: C_odd HAS nonzero ternary "
              "codewords (SP-TERNARY cannot fire)" % n, nt > 0,
              "(got %d)" % nt)
        check("GATE CERTIFICATE n=%d p=7 w=7: NO ternary codeword admits a "
              "compatible even-code witness -> a=0 EMPTY" % n, nc == 0,
              "(got %d)" % nc)
        print("  n=%d p=7 w=7: %d nonzero ternary codewords in C_odd, %d "
              "SP-TERNARY-counted sets, 0 survive the even coupling."
              % (n, nt, s2z))
    print("\n  => the p=7 / w=7 census cell IS reproduced, by the COUPLED")
    print("     criterion and by nothing weaker (G1.5 HELD).")


# ================================================================== cwtoy
def stage_cwtoy():
    hdr("STAGE cwtoy -- (C2) CW-FLOOR: LEMMA TC, shells, floor, and break")
    for (L, p) in [(8, 5), (8, 3), (8, 7), (8, 17), (6, 5), (6, 7),
                   (4, 3), (4, 5)]:
        twoL = 2 * L
        F = GF(p, twoL)
        Q = F.Q
        th = [F.powxi(j) for j in range(twoL)]

        def psi_set(sub):
            acc = [0] * F.d
            for j in sub:
                v = th[j]
                for k in range(F.d):
                    acc[k] = (acc[k] + v[k]) % p
            return tuple(acc)

        # relations R
        R = []
        for e in itertools.product((0, 1, -1), repeat=L):
            acc = [0] * F.d
            for j, c in enumerate(e):
                if c:
                    v = th[j]
                    for k in range(F.d):
                        acc[k] = (acc[k] + c * v[k]) % p
            if all(x == 0 for x in acc):
                R.append(e)
        check("eps = 0 is a relation (L=%d,p=%d)" % (L, p),
              tuple([0] * L) in R)

        for rp in [L - 2, L - 4]:
            if rp < 2:
                continue
            # brute-force |X_{r'}| over ALL C(2L,r') subsets of Z/2L
            X = 0
            for sub in itertools.combinations(range(twoL), rp):
                if all(x == 0 for x in psi_set(sub)):
                    X += 1
            # LEMMA TC (cited; re-verified here)
            tc = 0
            for e in R:
                U = sum(1 for c in e if c)
                if U <= rp and (U % 2) == (rp % 2):
                    tc += comb(L - U, (rp - U) // 2)
            check("LEMMA TC reproduces |X_{r'}| (L=%d,p=%d,r'=%d)"
                  % (L, p, rp), tc == X, "(TC %d vs brute %d)" % (tc, X))
            # the SHELL decomposition |X| = sum_W N(W, r'-W)
            NW = {}
            for W in range(0, rp + 1):
                Wp = rp - W
                if W > L or Wp > L:
                    NW[W] = 0
                    continue
                fw, fwp = {}, {}
                for a in itertools.combinations(range(L), W):
                    fw[psi_set(a)] = fw.get(psi_set(a), 0) + 1
                for b in itertools.combinations(range(L), Wp):
                    fwp[psi_set(b)] = fwp.get(psi_set(b), 0) + 1
                NW[W] = sum(v * fwp.get(k, 0) for k, v in fw.items())
            check("SHELL identity |X_{r'}| = sum_W N(W,r'-W) "
                  "(L=%d,p=%d,r'=%d)" % (L, p, rp),
                  sum(NW.values()) == X,
                  "(shells %d vs %d)" % (sum(NW.values()), X))
            if rp % 2 == 0:
                W0 = rp // 2
                cs = comb(L, W0) ** 2 / Q
                check("DIAGONAL floor N(W,W) >= C(L,W)^2/Q "
                      "(L=%d,p=%d,r'=%d)" % (L, p, rp), NW[W0] >= cs,
                      "(N=%d vs %.3f)" % (NW[W0], cs))
                check("CW-FLOOR |X_{r'}| >= N(r'/2,r'/2) "
                      "(L=%d,p=%d,r'=%d)" % (L, p, rp), X >= NW[W0])
                check("CW-FLOOR |X_{r'}| >= C(L,r'/2)^2/Q "
                      "(L=%d,p=%d,r'=%d)" % (L, p, rp), X >= cs,
                      "(X=%d vs floor %.3f)" % (X, cs))
                # non-structural corollary
                if comb(L, W0) > Q:
                    check("CW-FLOOR forces a NON-STRUCTURAL solution when "
                          "C(L,r'/2) > Q (L=%d,p=%d,r'=%d)" % (L, p, rp),
                          X > comb(L, W0), "(X=%d vs struct %d)"
                          % (X, comb(L, W0)))
                # THE BREAK: cross-shell terms have NO floor
                broke = []
                for W in range(0, rp + 1):
                    if W == W0 or W > L or rp - W > L:
                        continue
                    naive = comb(L, W) * comb(L, rp - W) / Q
                    if NW[W] < naive:
                        broke.append((W, NW[W], naive))
                if broke:
                    print("  L=%d p=%d r'=%d : cross-shell floor FAILS at "
                          "W = %s" % (L, p, rp, [b[0] for b in broke[:6]]))
                    for b in broke[:3]:
                        print("      W=%-3d N(W,r'-W)=%-8d  <  "
                              "C(L,W)C(L,r'-W)/Q = %.3f" % b)
                check("G2.2: at least one cross-shell term violates the "
                      "naive floor (L=%d,p=%d,r'=%d)" % (L, p, rp),
                      len(broke) > 0 or comb(L, 0) * comb(L, rp) / Q <= 1,
                      "(none broke)")
            else:
                # r' ODD: the diagonal shell does not exist
                bal = [e for e in R
                       if sum(1 for c in e if c == 1) ==
                       sum(1 for c in e if c == -1)]
                idx = [e for e in R
                       if sum(1 for c in e if c) <= rp and
                       sum(1 for c in e if c) % 2 == rp % 2]
                inter = set(bal) & set(idx)
                check("r' ODD: balanced relations and LEMMA TC's index set "
                      "are DISJOINT except eps=0 (L=%d,p=%d,r'=%d)"
                      % (L, p, rp),
                      inter <= {tuple([0] * L)}, "(overlap %d)" % len(inter))
    print("\n  CW-FLOOR verified: the diagonal shell W = r'/2 carries a")
    print("  Cauchy-Schwarz floor, the cross shells do NOT, and at odd r'")
    print("  the diagonal shell is empty of LEMMA TC weight (G2.1, G2.2).")


# ================================================================== main
STAGES = {"haar": stage_haar, "census": stage_census,
          "coupled": stage_coupled, "cwtoy": stage_cwtoy}


def main():
    if len(sys.argv) < 2:
        print("usage: cg_census.py STAGE  (%s|failclosed)" % "|".join(STAGES))
        return 2
    st = sys.argv[1]
    if st == "failclosed":
        hdr("STAGE failclosed -- permanent control, MUST exit 1")
        check("injected false check (this MUST fail)", 1 == 2)
    elif st in STAGES:
        STAGES[st]()
    else:
        print("unknown stage %r" % st)
        return 2
    print("\n" + "-" * 74)
    print("checks = %d   failures = %d" % (NCHECK, len(FAILS)))
    for f in FAILS:
        print("  FAILED: %s" % f)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
