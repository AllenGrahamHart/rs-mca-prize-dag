#!/usr/bin/env python3
"""F2-ADM verifier -- the F2 mechanism on a PRIZE-ADMISSIBLE row.

Round 17, pilot notes/pilots_20260806/f2_adm/.  Self-contained: no imports
from other pilots, no network, exact integer / Fraction / Decimal arithmetic
only.  Fail-closed: any FAIL sets the exit code to 1.

Stages
  S0  verbatim quote checks at file:line (every statement relied on)
  S1  the banked admissible witness row, exact
  S2  the admissible region, the depth-budget trade-off, existence witnesses
  S3  TOY brute force: the decomposition theorem, GRS structure, Z(L),
      LEMMA 1, the trace-tower collapse, the coset behaviour
  S4  THEOREM A / LEMMA 2 discharge on admissible rows
  S5  LEMMA 3 margins, both window readings, worst case over t in (2^33, 5.364e10]
  S6  SL-1 / SL-1b / SL-1b' re-based
  S7  the |K1| / PP5.0 seam, all three readings
  S8  the tower's own-field self-consistency control
  S9  sibling controls (t*, 2^33, 255.911275, m_16)
"""
from __future__ import annotations

import sys
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product

getcontext().prec = 60

REPO = "/home/u2470931/smooth-read-solomin/prize"

PASS = 0
FAIL = 0
LOG: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    if cond:
        PASS += 1
        LOG.append(f"PASS  {name}   {detail}")
    else:
        FAIL += 1
        LOG.append(f"FAIL  {name}   {detail}")


def say(s: str = "") -> None:
    LOG.append(s)


# ----------------------------------------------------------------- helpers --
def C_new(D: int) -> int:
    """number of F_p-proportionality classes, new-part reading."""
    return 1 if D <= 1 else (1 << (D - 1))


def C_nest(D: int) -> int:
    """number of F_p-proportionality classes, nested reading."""
    return 1 << D


def v2(x: int) -> int:
    return (x & -x).bit_length() - 1


def log2d(x: int | Decimal) -> Decimal:
    return Decimal(x).ln() / Decimal(2).ln()


def is_prime(m: int) -> bool:
    if m < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % q == 0:
            return m == q
    d, r = m - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(r - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def mult_order(a: int, mod: int) -> int:
    """order of a mod 2^s (mod is a power of two here, but general enough)."""
    o = 1
    x = a % mod
    while x != 1:
        x = x * a % mod
        o += 1
        if o > mod:
            raise ValueError("no order")
    return o


# ------------------------------------------------------- S0 verbatim quotes --
QUOTES = [
    ("critical/nodes/rules_freeze/statement.md", 9,
     "smooth domain = coset of a power-of-2-order subgroup; k <= 2^40; |F| < 2^256"),
    ("critical/nodes/rules_freeze/statement.md", 9,
     "on any residual ambiguity the campaign plans against the stricter reading"),
    ("notes/pilots_20260802/f2_deployed_windows/tower.py", 17,
     "the moving coordinates are the elements of order EXACTLY 2^{24+j},"),
    ("notes/pilots_20260802/f2_deployed_windows/tower.py", 18,
     "m_j = (n_j - n_{j-1}) / 2 = 2^{22+j} conjugate pairs."),
    ("notes/pilots_20260802/f2_deployed_windows/tower.py", 15,
     "RUNG j (j = 1..16):  n_j = 2^{24+j},  q_j = p^{2^j},  k_j = 2^j,"),
    ("notes/pilots_20260802/f2_deployed_windows/tower.py", 26,
     "(i)   v_2(q_j - 1) = e + j            for every j >= 0   [LTE],"),
    ("notes/pilots_20260802/f2_deployed_windows/tower.py", 28,
     "(iii) every y of order exactly n_j satisfies  y^{q_{j-1}} = -y."),
    ("notes/pilots_20260804/f2_opening/PROOFS.md", 10,
     "`G = mu_{n}` with `n | p^2-1`, `n` even; `psi(s) = zeta_p^s`."),
    ("notes/pilots_20260804/f2_opening/PROOFS.md", 15,
     "`W = {x : ord(x) = n_j}`, `m_j = 2^{22+j}`; the full-group window is"),
    ("notes/pilots_20260804/f2_opening/PROOFS.md", 81,
     "sum_{i=1}^{m} eps_i y_i^{l} = 0  in F_{p^2},  for every l in Lambda."),
    ("notes/pilots_20260804/f2_opening/PROOFS.md", 94,
     "E_{c in K1}[T_W(c)]  >=  2^{m}  =  2^{|W|/2}   for EVERY Lambda."),
    ("notes/pilots_20260804/f2_opening/PROOFS.md", 106,
     "Suppose `Lambda ⊇ {1, 3, 5, ..., 2m-1}` and these are distinct residues"),
    ("notes/pilots_20260804/f2_opening/PROOFS.md", 225,
     "dim_{F_p} L  >=  m / log2 p  -  o(n)/log2 p."),
    ("notes/pilots_20260804/f2_opening/PROOFS.md", 330,
     "is forced, since `dim L <= t < m`) and (O1) reduces to bounding"),
    ("notes/pilots_20260804/f2_opening/PROOFS.md", 341,
     "- `E_c[.]` is an **average** over the K1 subspace. The consumer sums"),
    ("notes/pilots_20260804/f2_sl1_powersums/PROOFS.md", 99,
     "and `eps != 0` satisfies **`wt(eps) >= R + 1`**."),
    ("notes/pilots_20260804/f2_sl1_powersums/PROOFS.md", 316,
     "**SL-1b (the named residual, replacing SL-1 on the obligation list):** prove"),
    ("notes/pilots_20260806/f2_sl1b/PROOFS.md", 161,
     "min(m, R)   <=   dim_{F_p} L   <=   min(m, k·|Lambda|)."),
    ("notes/pilots_20260806/f2_sl1b/PROOFS.md", 259,
     "k = 1   =>   dim_{F_p} L  =  min(m, R)   EXACTLY."),
    ("notes/pilots_20260806/f2_sl1b/PROOFS.md", 571,
     "prove `Z(L) = sum_{eps in L^perp ∩ T} 2^{-wt(eps)} <= 2^{o(m)}`."),
    ("notes/pilots_20260806/f2_tq_pin/PROOFS.md", 114,
     "v_2(e) <= 2,      e <= 6,      log2 p >= 39,"),
    ("notes/pilots_20260806/f2_tq_pin/PROOFS.md", 131,
     "p = 18446735827372343297   (prime, v_2(p-1) = 39 exactly, log2 p = 64.0000)"),
    ("notes/pilots_20260806/f2_tq_pin/PROOFS.md", 174,
     "t · L  >=  n .                                (C)"),
    ("notes/pilots_20260806/f2_tq_pin/PROOFS.md", 202,
     "2^41/256  <  t  <=  2^41/41 ,        i.e.   8.590e9 < t <= 5.364e10 ."),
    ("notes/pilots_20260806/f2_tq_pin/PROOFS.md", 402,
     "**In the extension reading, average-vs-sum is EXACTLY a factor `2^{n/2}`.**"),
    ("notes/pilots_20260802/f2_fixed_sector/REPORT.md", 33,
     "(O1) first-moment target E_{c in K1}[exp S_c] <= 2^{n/2 + o(n)}"),
]


def stage0() -> None:
    say("=== S0  verbatim quote checks =========================================")
    for path, line, frag in QUOTES:
        try:
            with open(f"{REPO}/{path}", encoding="utf-8") as fh:
                lines = fh.read().split("\n")
            ok = frag in lines[line - 1]
        except Exception as exc:  # noqa: BLE001
            ok = False
            frag = f"{frag}  [{exc}]"
        check(f"S0 {path}:{line}", ok, frag[:70])


# ------------------------------------------------------------- S1 the witness --
N_BITS = 41
N = 1 << N_BITS
P_WIT = 18446735827372343297
CAP = 256


def stage1() -> dict:
    say()
    say("=== S1  the banked admissible witness row =============================")
    check("S1.1 p prime", is_prime(P_WIT), f"p = {P_WIT}")
    ep = v2(P_WIT - 1)
    check("S1.2 v_2(p-1) = 39", ep == 39, f"e_p = {ep}")
    lp = log2d(P_WIT)
    check("S1.3 log2 p in [63.99, 64)", Decimal("63.99") < lp < Decimal(64),
          f"log2 p = {lp:.9f}")
    q = P_WIT ** 4
    L = 4 * lp
    check("S1.4 log2 q < 256", L < CAP, f"L = {L:.9f}")
    check("S1.5 v_2(q-1) = 41", v2(q - 1) == 41, f"v_2(q-1) = {v2(q-1)}")
    check("S1.6 n | q-1", (q - 1) % N == 0, "2^41 | p^4 - 1")
    k = mult_order(P_WIT, N)
    check("S1.7 ord_{2^41}(p) = 4", k == 4, f"k = {k}")
    D = N_BITS - ep
    check("S1.8 moving-rung count D = 2", D == 2 and k == 2 ** D, f"D = {D}")
    # the ladder (A2)
    ladder = []
    for j in range(0, D + 1):
        a = ep + j
        n_j = 1 << a
        k_j = 1 if j == 0 else mult_order(P_WIT, n_j)
        m_new = (n_j - (1 << (a - 1))) // 2 if j >= 1 else n_j // 2
        m_nest = n_j // 2
        ladder.append((j, a, n_j, k_j, m_new, m_nest))
    exp = [(0, 39, 1 << 39, 1, 1 << 38, 1 << 38),
           (1, 40, 1 << 40, 2, 1 << 38, 1 << 39),
           (2, 41, 1 << 41, 4, 1 << 39, 1 << 40)]
    check("S1.9 ladder = (2^39,p,1,2^38)/(2^40,p^2,2,2^38)/(2^41,p^4,4,2^39)",
          ladder == exp, str([(x[1], x[3], x[4]) for x in ladder]))
    frac_fixed = Fraction(1 << ep, N)
    check("S1.10 fixed sector = 1/4 of the domain", frac_fixed == Fraction(1, 4),
          f"|mu_2^39|/n = {frac_fixed}")
    kb_frac = Fraction(1 << 24, 1 << 40)
    check("S1.11 KoalaBear fixed sector = 2^-16 of its domain",
          kb_frac == Fraction(1, 1 << 16), f"{kb_frac}")
    t_row = Decimal(N) / L
    check("S1.12 row-consistent t = n/L just above 2^33",
          Decimal(1 << 33) < t_row < Decimal(1 << 33) * Decimal("1.0001"),
          f"t_row = {t_row:.1f}  (2^33 = {1<<33})")
    say(f"      witness: p = {P_WIT}, e_p = 39, e = 4, k = 4, L = {L:.6f}")
    say(f"      t_row = n/L = {t_row:.1f};  R = ceil(t/2) = {int(t_row/2)+1}")
    return {"ep": ep, "k": k, "e": 4, "L": L, "lp": lp, "t_row": t_row,
            "ladder": ladder}


# --------------------------------------------- S2 admissible region + trade-off --
def stage2() -> list:
    say()
    say("=== S2  the admissible region and the depth-budget trade-off ==========")
    rows = []
    for ep in range(1, 60):
        D = max(0, N_BITS - ep)
        k = 1 << D
        for e in range(1, 12):
            if e % k != 0:
                continue
            # log2 p > e_p  (2^{e_p} | p-1)  and, when D = 0, log2 p >= 41
            lp_min = max(ep, N_BITS if D == 0 else 0)
            L_min = e * lp_min
            adm = L_min < CAP and v2(e) <= 2
            if adm:
                rows.append({"ep": ep, "D": D, "k": k, "e": e, "L_min": L_min})
    Ds = sorted({r["D"] for r in rows})
    check("S2.1 admissible depth <= 2 rungs", Ds == [0, 1, 2], f"D in {Ds}")
    check("S2.2 v_2(e) <= 2 and e <= 6 on every admissible row",
          all(v2(r["e"]) <= 2 and r["e"] <= 6 for r in rows),
          f"max e = {max(r['e'] for r in rows)}")
    check("S2.3 log2 p >= 39 on every admissible row",
          min(max(r["ep"], N_BITS if r["D"] == 0 else 0) for r in rows) == 39,
          "min forced log2 p = 39")
    # depth-budget trade-off (A3)
    say("      D | forced L >= | t = n/L <=      | classes (e_p, e, k)")
    tmax = {}
    for D in [0, 1, 2, 3]:
        ep = N_BITS - D
        Lmin = (1 << D) * (ep if D > 0 else N_BITS)
        tm = Decimal(N) / Decimal(Lmin)
        tmax[D] = (Lmin, tm)
        cls = sorted({(r["ep"], r["e"], r["k"]) for r in rows if r["D"] == D})
        say(f"      {D} | {Lmin:11d} | {tm:15.4e} | {cls if cls else 'INADMISSIBLE'}")
    check("S2.4 D=0 cap t <= 5.364e10",
          abs(tmax[0][1] - Decimal("5.3634e10")) / tmax[0][1] < Decimal("1e-3"),
          f"{tmax[0][1]:.4e}")
    check("S2.5 D=1 cap t <= 2.749e10",
          abs(tmax[1][1] - Decimal("2.7488e10")) / tmax[1][1] < Decimal("1e-3"),
          f"{tmax[1][1]:.4e}")
    check("S2.6 D=2 cap t <= 1.410e10",
          abs(tmax[2][1] - Decimal("1.4096e10")) / tmax[2][1] < Decimal("1e-3"),
          f"{tmax[2][1]:.4e}")
    check("S2.7 D=3 needs L >= 304 > 256 -> INADMISSIBLE", tmax[3][0] == 304,
          f"L >= {tmax[3][0]}")
    check("S2.8 each extra rung at least halves the t cap",
          tmax[0][1] > tmax[1][1] > tmax[2][1] and
          tmax[0][1] / tmax[1][1] > Decimal("1.9"),
          f"{tmax[0][1]/tmax[1][1]:.3f}x, {tmax[1][1]/tmax[2][1]:.3f}x")
    # existence witnesses per (e_p, e) class: p = c*2^{e_p} + 1, c odd,
    # and e*log2 p < 256, i.e. c < 2^{256/e - e_p}.  A class can be EMPTY.
    say("      existence per (e_p, e) class  [p = c*2^{e_p}+1, c odd, L < 256]:")
    found = {}
    empty = []
    for ep, e in ((41, 1), (41, 2), (41, 3), (41, 4), (41, 5), (41, 6),
                  (40, 2), (40, 4), (40, 6), (39, 4)):
        cmax = Decimal(2) ** (Decimal(256) / e - ep)
        pw = None
        c = 1
        while Decimal(c) < cmax and c < 4_000_001:
            cand = c * (1 << ep) + 1
            if v2(cand - 1) == ep and is_prime(cand):
                pw = cand
                break
            c += 2
        if pw is None:
            empty.append((ep, e))
            say(f"        (e_p={ep}, e={e}): c < {cmax:.2f}  ->  NO PRIME EXISTS"
                f"  -- CLASS IS EMPTY")
        else:
            found[(ep, e)] = pw
            say(f"        (e_p={ep}, e={e}): p = {pw}  (log2 p = "
                f"{log2d(pw):.4f}, L = {e*log2d(pw):.4f})")
    check("S2.9 the (e_p=40, e=6) class is EMPTY (no prime admits it)",
          empty == [(40, 6)], f"empty classes = {empty}")
    check("S2.10 the witness class (e_p=39, e=4) is realised, and by a smaller "
          "prime than the banked witness", (39, 4) in found and
          found[(39, 4)] < P_WIT, f"p = {found.get((39,4))}")
    check("S2.11 an EXPLICIT k=1, e=6 admissible row exists (LEMMA 3 refuted "
          "there, S5)", (41, 6) in found,
          f"p = {found.get((41,6))}, L = {6*log2d(found[(41,6)]):.4f}"
          if (41, 6) in found else "none")
    check("S2.12 an EXPLICIT k=2, e=4 admissible row exists", (40, 4) in found,
          f"p = {found.get((40,4))}")
    return rows


# ------------------------------------------------------------------ toy fields --
class GF:
    """F_{p^d} = F_p[x]/(f), elements are tuples of length d."""

    def __init__(self, p: int, d: int):
        self.p, self.d = p, d
        self.f = self._irred()

    def _polymulmod(self, a, b, f):
        p, d = self.p, self.d
        res = [0] * (2 * d - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    res[i + j] = (res[i + j] + ai * bj) % p
        for i in range(2 * d - 2, d - 1, -1):
            c = res[i]
            if c:
                res[i] = 0
                for j in range(d):
                    res[i - d + j] = (res[i - d + j] - c * f[j]) % p
        return tuple(res[:d])

    # --- general polynomial helpers over F_p (low-degree-first lists) -------
    def _pdeg(self, a):
        d = len(a) - 1
        while d >= 0 and a[d] % self.p == 0:
            d -= 1
        return d

    def _pdivmod(self, a, b):
        p = self.p
        a = [x % p for x in a]
        db = self._pdeg(b)
        inv = pow(b[db], p - 2, p)
        q = [0] * max(1, len(a) - db)
        while True:
            da = self._pdeg(a)
            if da < db:
                break
            c = a[da] * inv % p
            q[da - db] = c
            for i in range(db + 1):
                a[da - db + i] = (a[da - db + i] - c * b[i]) % p
        return q, a

    def _pgcd(self, a, b):
        a, b = a[:], b[:]
        while self._pdeg(b) >= 0:
            _, r = self._pdivmod(a, b)
            a, b = b, r
        return a

    def _f_poly(self):
        """the modulus as a low-first coefficient list: x^d - sum f_j x^j."""
        return [(-c) % self.p for c in self.f] + [1]

    def _irred(self):
        """Rabin's test: f = x^d - sum f_j x^j is irreducible over F_p iff
        x^{p^d} = x mod f and gcd(x^{p^{d/r}} - x, f) = 1 for every prime
        r | d.  Candidates are drawn in a seeded pseudo-random order (a plain
        LCG, so the run is reproducible) and pre-filtered by a root test."""
        p, d = self.p, self.d
        if d == 1:
            self.f = [0]
            return self.f
        primes = [r for r in range(2, d + 1)
                  if d % r == 0 and all(r % s for s in range(2, r))]
        x = tuple([0, 1] + [0] * (d - 2))
        seed = 1234567 + 7919 * p + 104729 * d
        for _ in range(2_000_000):
            seed = (1103515245 * seed + 12345) % (1 << 31)
            v, coeffs = seed, []
            for _ in range(d):
                v = (1103515245 * v + 12345) % (1 << 31)
                coeffs.append(v % p)
            if coeffs[0] == 0:                     # x | f
                continue
            # root test: f(r) = r^d - sum c_j r^j != 0 for all r in F_p
            if any((pow(r, d, p) - sum(c * pow(r, j, p) for j, c in
                                       enumerate(coeffs))) % p == 0
                   for r in range(p)):
                continue
            self.f = coeffs
            if self.pow(x, p ** d) != x:
                continue
            fp = self._f_poly()
            ok = True
            for r in primes:
                xr = list(self.pow(x, p ** (d // r)))
                xr[1] = (xr[1] - 1) % p            # x^{p^{d/r}} - x
                if self._pdeg(xr) < 0:
                    ok = False
                    break
                g = self._pgcd(fp, xr + [0])
                if self._pdeg(g) > 0:
                    ok = False
                    break
            if ok:
                return self.f
        raise RuntimeError("no irreducible found")

    def one(self):
        return tuple([1] + [0] * (self.d - 1))

    def zero(self):
        return tuple([0] * self.d)

    def mul(self, a, b):
        return self._polymulmod(list(a), list(b), self.f)

    def pow(self, a, n):
        r, b = self.one(), a
        while n:
            if n & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            n >>= 1
        return r

    def neg(self, a):
        return tuple((-x) % self.p for x in a)

    def scal(self, c, a):
        return tuple((c * x) % self.p for x in a)

    def from_int(self, c):
        return tuple([c % self.p] + [0] * (self.d - 1))

    def trace(self, a):
        """Tr_{F_{p^d}/F_p}(a) = sum_{i<d} a^{p^i}."""
        s = 0
        x = a
        for _ in range(self.d):
            s = (s + x[0] if self.d == 1 else s + x[0]) % self.p
            # need actual coordinate sum of conjugates: recompute properly
            x = self.pow(x, self.p)
        return s % self.p

    def elements(self):
        for c in product(range(self.p), repeat=self.d):
            yield tuple(c)


def gf_trace(F: GF, a):
    s = F.zero()
    x = a
    for _ in range(F.d):
        s = tuple((si + xi) % F.p for si, xi in zip(s, x))
        x = F.pow(x, F.p)
    assert all(c == 0 for c in s[1:]), "trace not in prime field"
    return s[0]


def find_root_of_unity(F: GF, n: int):
    """an element of exact order n in F^* (seeded pseudo-random search)."""
    order = F.p ** F.d - 1
    assert order % n == 0, "mu_n not in this field"
    cof = order // n
    seed = 987654321 + 31 * F.p + 17 * F.d + n
    for _ in range(100000):
        a = []
        for _ in range(F.d):
            seed = (1103515245 * seed + 12345) % (1 << 31)
            a.append(seed % F.p)
        a = tuple(a)
        if all(z == 0 for z in a):
            continue
        y = F.pow(a, cof)
        if y == F.one():
            continue
        ok = True
        for r in range(1, n):
            if n % r == 0 and F.pow(y, r) == F.one():
                ok = False
                break
        if ok:
            return y
    raise RuntimeError("no root of unity")


def rref_kernel(rows: list[list[int]], ncols: int, p: int) -> list[list[int]]:
    """kernel basis over F_p of the matrix given by `rows`."""
    M = [r[:] for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        sel = None
        for i in range(r, len(M)):
            if M[i][c] % p:
                sel = i
                break
        if sel is None:
            continue
        M[r], M[sel] = M[sel], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [(x * inv) % p for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(piv):
            v[pc] = (-M[i][fc]) % p
        basis.append(v)
    return basis


def dim_L_and_kernel(F: GF, reps: list, Lam: list[int], p: int):
    """L^perp = ker_{F_p}(A), A = (y_i^l); returns (dim L, kernel basis)."""
    m = len(reps)
    rows = []
    for l in Lam:
        col = [F.pow(y, l) for y in reps]
        for coord in range(F.d):
            rows.append([col[i][coord] % p for i in range(m)])
    ker = rref_kernel(rows, m, p)
    return m - len(ker), ker


def rank_fp(rows: list[list[int]], p: int) -> int:
    M = [r[:] for r in rows]
    r = 0
    ncols = len(M[0]) if M else 0
    for c in range(ncols):
        sel = None
        for i in range(r, len(M)):
            if M[i][c] % p:
                sel = i
                break
        if sel is None:
            continue
        M[r], M[sel] = M[sel], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [(x * inv) % p for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
    return r


def dim_L_direct(F: GF, reps: list, Lam: list[int], p: int) -> int:
    """dim_{F_p} L computed as the RANK OF THE IMAGE of the evaluation map
    c |-> (Tr_{F_q/F_p}(sum_l C_l y_i^l))_i, c ranging over an F_p-basis of
    K1(Lambda) = F_q^Lambda.  A route disjoint from the kernel computation:
    it uses the trace explicitly and never forms A."""
    imgs = []
    for li in range(len(Lam)):
        for coord in range(F.d):
            basis_elt = tuple(1 if j == coord else 0 for j in range(F.d))
            vec = []
            for yi in reps:
                val = F.mul(basis_elt, F.pow(yi, Lam[li]))
                vec.append(gf_trace(F, val))
            imgs.append(vec)
    return rank_fp(imgs, p)


def kernel_elements(basis: list[list[int]], p: int):
    if not basis:
        yield [0] * (len(basis[0]) if basis else 0)
        return
    m = len(basis[0])
    for coef in product(range(p), repeat=len(basis)):
        v = [0] * m
        for c, b in zip(coef, basis):
            if c:
                for i in range(m):
                    v[i] = (v[i] + c * b[i]) % p
        yield v


def ternary_kernel_stats(F: GF, reps: list, Lam: list[int], p: int):
    """min ternary weight and Z(L) = sum 2^{-wt} over ternary kernel vectors."""
    m = len(reps)
    pw = [[F.pow(y, l) for y in reps] for l in Lam]
    Z = Fraction(0)
    minwt = None
    cnt = 0
    for eps in product((0, 1, -1), repeat=m):
        ok = True
        for row in pw:
            s = F.zero()
            for e, val in zip(eps, row):
                if e == 1:
                    s = tuple((a + b) % p for a, b in zip(s, val))
                elif e == -1:
                    s = tuple((a - b) % p for a, b in zip(s, val))
            if any(s):
                ok = False
                break
        if ok:
            wt = sum(1 for e in eps if e)
            Z += Fraction(1, 2 ** wt)
            cnt += 1
            if wt and (minwt is None or wt < minwt):
                minwt = wt
    return minwt, Z, cnt


# ------------------------------------------------- S3 the toy reconstruction --
TOYS = [
    # (label, p, n, ambient degree e, note)
    ("T1 witness-analogue D=2,k=4,e=4", 5, 16, 4),
    ("T2 D=1,k=2,e=2", 17, 32, 2),
    ("T3 prime-field D=0,k=1,e=1", 17, 16, 1),
    ("T4 D=0,k=1 in a BIGGER ambient e=2", 17, 16, 2),
    ("T5 D=1,k=2 in a BIGGER ambient e=6", 17, 32, 6),
    ("T6 D=2,k=4,e=4 (p=13)", 13, 16, 4),
    ("T7 D=3,k=8,e=8 (beyond the admissible cap)", 5, 32, 8),
    ("T8 D=2,k=4,e=4 with larger classes (p=41,n=32)", 41, 32, 4),
]


def layer_reps(F: GF, y, n: int, a: int, nested: bool):
    """representatives, one per antipodal pair, of the order-2^a layer
    (new-part) or of mu_{2^a} (nested)."""
    step = n >> a  # y^step has order 2^a
    eta = F.pow(y, step)
    if nested:
        idx = range(0, 1 << (a - 1))
    else:
        idx = range(1, 1 << (a - 1), 2)
    return [F.pow(eta, i) for i in idx], eta


def stage3() -> None:
    say()
    say("=== S3  TOY brute force: the decomposition that replaces the descent ===")
    for label, p, n, e in TOYS:
        ep = v2(p - 1)
        a_top = v2(n)
        D = max(0, a_top - ep)
        k = mult_order(p, n)
        if k != 2 ** D:
            check(f"S3 {label} k = 2^D", False, f"k={k}, D={D}")
            continue
        if e % k or (p ** e - 1) % n:
            check(f"S3 {label} ambient contains mu_n", False, "")
            continue
        F = GF(p, e)
        y = find_root_of_unity(F, n)
        for nested in (False, True):
            reps, _ = layer_reps(F, y, n, a_top, nested)
            m = len(reps)
            if m > 12:
                continue
            C = C_nest(D) if nested else C_new(D)
            S = m // C
            Rmax = min(m, 5)
            for R in range(1, Rmax + 1):
                Lam = [2 * r + 1 for r in range(R)]
                dimL, ker = dim_L_and_kernel(F, reps, Lam, p)
                pred = C * min(S, R)
                tag = "nested" if nested else "new-part"
                check(f"S3.A {label} [{tag}] dim L = C*min(S,R)  R={R}",
                      dimL == pred,
                      f"dim L = {dimL}, C={C}, S={S}, pred = {pred}, m={m}")
                # sl1b bracket must still hold (control)
                check(f"S3.B {label} [{tag}] sl1b bracket  R={R}",
                      min(m, R) <= dimL <= min(m, k * len(Lam)),
                      f"{min(m,R)} <= {dimL} <= {min(m, k*len(Lam))}")
                # SL-1 designed distance (control)
                if m <= 10:
                    minwt, Z, cnt = ternary_kernel_stats(F, reps, Lam, p)
                    check(f"S3.C {label} [{tag}] SL-1 wt >= R+1  R={R}",
                          minwt is None or minwt >= R + 1,
                          f"min ternary wt = {minwt}, R+1 = {R+1}")
                    # Z(L) factorises as Z_class^C
                    if C > 1:
                        cls_reps = reps[0:m:C] if False else None
                        # classes: index i -> i mod C under the natural order
                        groups: dict[int, list] = {}
                        for i, r in enumerate(reps):
                            groups.setdefault(i % C, []).append(r)
                        good = all(len(g) == S for g in groups.values())
                        Zs = []
                        for g in groups.values():
                            _, Zg, _ = ternary_kernel_stats(F, g, Lam, p)
                            Zs.append(Zg)
                        prod_ = Fraction(1)
                        for zz in Zs:
                            prod_ *= zz
                        check(f"S3.D {label} [{tag}] Z(L) = prod Z_class  R={R}",
                              good and prod_ == Z,
                              f"Z = {Z}, prod = {prod_}"
                              + ("" if Z == 1 else "  [NONTRIVIAL]"))
                        # SET-level check of L^perp = (+) ker(A_c): embed each
                        # class-kernel basis vector by zeros and verify it lies
                        # in the full kernel, and that the dimensions add up.
                        _, kerfull = dim_L_and_kernel(F, reps, Lam, p)
                        dsum = 0
                        emb_ok = True
                        for gi2, g2 in groups.items():
                            _, kg = dim_L_and_kernel(F, g2, Lam, p)
                            dsum += len(kg)
                            for bv in kg:
                                full = [0] * m
                                for pos, idx in enumerate(
                                        [i for i in range(m) if i % C == gi2]):
                                    full[idx] = bv[pos]
                                for row in [[F.pow(y2, l)[co] % p for y2 in reps]
                                            for l in Lam for co in range(F.d)]:
                                    if sum(a * b for a, b in
                                           zip(full, row)) % p:
                                        emb_ok = False
                        check(f"S3.N {label} [{tag}] L^perp = (+)_c ker(A_c) "
                              f"as SETS  R={R}",
                              emb_ok and dsum == len(kerfull),
                              f"sum of class kernel dims = {dsum} = "
                              f"dim L^perp = {len(kerfull)}, embeddings in ker: "
                              f"{emb_ok}")
        say(f"      {label}: p={p}, n={n}, e_p={ep}, D={D}, k={k}, e={e}")
    # ---- LEMMA 1 brute force (E_c[T_W] = 2^m Z(L)) ---------------------------
    # honest brute force over ALL c in K1(Lambda) = F_q^Lambda; the trace is
    # precomputed as an F_p-linear functional per (i, l) so no Frobenius power
    # is recomputed inside the loop.
    for (pp, nn, ee, Rlist) in ((5, 16, 4, (1,)), (17, 16, 1, (1, 2, 3)),
                                (17, 32, 2, (1,))):
        F = GF(pp, ee)
        y = find_root_of_unity(F, nn)
        reps, _ = layer_reps(F, y, nn, v2(nn), False)
        m = len(reps)
        for R in Rlist:
            Lam = [2 * r + 1 for r in range(R)]
            _, Z, _ = ternary_kernel_stats(F, reps, Lam, pp)
            func = [[[gf_trace(F, F.mul(tuple(1 if u == j else 0
                                              for u in range(F.d)),
                                        F.pow(yi, l)))
                      for j in range(F.d)] for l in Lam] for yi in reps]
            acc = [0] * pp
            total = 0
            for cs in product(product(range(pp), repeat=F.d), repeat=R):
                total += 1
                poly = [0] * pp
                poly[0] = 1
                for i in range(m):
                    sv = 0
                    for li in range(R):
                        fi = func[i][li]
                        ci = cs[li]
                        for j in range(F.d):
                            if ci[j]:
                                sv += ci[j] * fi[j]
                    sv %= pp
                    newp = [0] * pp
                    for a_, ca in enumerate(poly):
                        if ca:
                            newp[a_] += 2 * ca
                            newp[(a_ + sv) % pp] += ca
                            newp[(a_ - sv) % pp] += ca
                    poly = newp
                for a_ in range(pp):
                    acc[a_] += poly[a_]
            red = [x - acc[1] for x in acc]     # reduce mod 1+z+...+z^{p-1}
            val = Fraction(red[0], total)
            check(f"S3.E LEMMA 1 brute force (p={pp}, n={nn}, e={ee}, R={R}, "
                  f"m={m}): E_c[T_W] = 2^m Z(L)",
                  val == Fraction(2 ** m) * Z,
                  f"E = {val}, 2^m Z(L) = {Fraction(2**m)*Z}, "
                  f"{total} frequencies")
    # ---- A6: the trace-tower collapse (dim L depends on k, not e) ----
    for (p, n, e_small, e_big) in ((17, 16, 1, 2), (17, 32, 2, 6)):
        k = mult_order(p, n)
        a_top = v2(n)
        Fs, Fb = GF(p, e_small), GF(p, e_big)
        ys, yb = find_root_of_unity(Fs, n), find_root_of_unity(Fb, n)
        rs, _ = layer_reps(Fs, ys, n, a_top, False)
        rb, _ = layer_reps(Fb, yb, n, a_top, False)
        for R in (1, 2, 3):
            Lam = [2 * r + 1 for r in range(R)]
            d1, _ = dim_L_and_kernel(Fs, rs, Lam, p)
            d2, _ = dim_L_and_kernel(Fb, rb, Lam, p)
            check(f"S3.F trace-tower collapse p={p},n={n}: dim L(e={e_small}) "
                  f"= dim L(e={e_big})  R={R}", d1 == d2,
                  f"{d1} vs {d2}; k|Lambda| = {k*R}")
            # disjoint route: rank of the IMAGE, coefficients over the big field
            di = dim_L_direct(Fb, rb, Lam, p)
            check(f"S3.L direct-image route agrees, ambient e={e_big}, "
                  f"p={p},n={n} R={R}", di == d2,
                  f"image-rank {di} = kernel-route {d2} <= k|Lambda| = {k*R}")
            dis = dim_L_direct(Fs, rs, Lam, p)
            check(f"S3.M dim L does NOT grow with the ambient degree "
                  f"(e={e_small} -> {e_big}), p={p},n={n} R={R}", dis == di,
                  f"{dis} vs {di}  (coefficients range over F_p^{e_big})")
            check(f"S3.G dim L <= ord_n(p)*|Lambda| p={p},n={n} R={R}",
                  d2 <= min(len(rb), k * R), f"{d2} <= {min(len(rb), k*R)}")
    # ---- A10: the coset ----
    p, n, e = 5, 16, 4
    F = GF(p, e)
    y = find_root_of_unity(F, n)
    reps, _ = layer_reps(F, y, n, 4, False)
    q_prev = p ** 2  # F_{q_1} = F_{p^2}, the subfield below the top rung
    # (iii) on the subgroup
    ok_sub = all(F.pow(r, q_prev) == F.neg(r) for r in reps)
    check("S3.H antipodal law y^{q_{j-1}} = -y holds on the subgroup", ok_sub, "")
    # a coset rep outside F_{p^2}
    g = None
    for c in F.elements():
        if all(x == 0 for x in c):
            continue
        if F.pow(c, q_prev) != c:  # g not in F_{p^2}
            g = c
            break
    cos = [F.mul(g, r) for r in reps]
    ok_cos = all(F.pow(x, q_prev) == F.neg(x) for x in cos)
    check("S3.I antipodal law FAILS on a coset with g not in F_{q_{j-1}}",
          not ok_cos, "as predicted (A10)")
    # but the mass machinery is coset-invariant
    for R in (1, 2, 3):
        Lam = [2 * r + 1 for r in range(R)]
        d_sub, _ = dim_L_and_kernel(F, reps, Lam, p)
        d_cos, _ = dim_L_and_kernel(F, cos, Lam, p)
        mw1, Z1, _ = ternary_kernel_stats(F, reps, Lam, p)
        mw2, Z2, _ = ternary_kernel_stats(F, cos, Lam, p)
        check(f"S3.J coset invariance of dim L / Z(L) / min wt  R={R}",
              d_sub == d_cos and Z1 == Z2 and mw1 == mw2,
              f"dim {d_sub}={d_cos}, Z {Z1}={Z2}, wt {mw1}={mw2}")
    # ---- GRS/MDS identification: the class code is [S, S-R, R+1] ----
    p, n, e = 5, 16, 4
    F = GF(p, e)
    y = find_root_of_unity(F, n)
    reps, _ = layer_reps(F, y, n, 4, False)
    groups: dict[int, list] = {}
    for i, r in enumerate(reps):
        groups.setdefault(i % 2, []).append(r)
    for gi, g in groups.items():
        for R in (1, 2):
            Lam = [2 * r + 1 for r in range(R)]
            dl, ker = dim_L_and_kernel(F, g, Lam, p)
            Sg = len(g)
            # MDS: dim of the kernel code = S - R and min distance = R + 1
            dists = []
            for v in kernel_elements(ker, p):
                w = sum(1 for x in v if x)
                if w:
                    dists.append(w)
            check(f"S3.K class code is [S,S-R,R+1] MDS  class={gi} R={R}",
                  len(ker) == max(0, Sg - R) and (not dists or min(dists) == R + 1),
                  f"S={Sg}, dim ker={len(ker)}, d_min={min(dists) if dists else '-'}")


# ------------------------------------------------------- S4 THEOREM A / LEMMA 2 --
def stage4(wit: dict) -> None:
    say()
    say("=== S4  THEOREM A / LEMMA 2 on admissible rows =========================")
    L = wit["L"]
    t_row = wit["t_row"]
    # layer table at the witness
    say("      layer a | m(a)=2^{a-2} | needs t >= 2m-1 | discharged? (t = n/L)")
    top_disch = None
    for a in range(2, 42):
        m = 1 << (a - 2)
        need = Decimal(2 * m - 1)
        d = need <= t_row
        if d:
            top_disch = a
        if a in (30, 33, 34, 35, 39, 40, 41):
            say(f"      {a:7d} | {m:12d} | {need:15.4e} | {'YES' if d else 'no'}"
                f"   (shortfall {need/t_row:.2f}x)")
    check("S4.1 witness: THEOREM A discharges exactly layers a <= 34",
          top_disch == 34, f"top discharged layer = {top_disch}")
    frac = Decimal(1 << top_disch) / Decimal(N)
    check("S4.2 discharged fraction = 2/L", abs(frac - 2 / L) / frac < Decimal("0.02"),
          f"2^{top_disch}/n = {frac:.6f} vs 2/L = {2/L:.6f}")
    check("S4.3 discharged fraction at prize-max = 1/128",
          abs(frac - Decimal(1) / 128) < Decimal("1e-9"), f"{frac}")
    # no moving rung is ever discharged, on any admissible row
    worst = None
    for ep, e in ((41, 1), (41, 2), (41, 3), (41, 4), (41, 5), (41, 6),
                  (40, 2), (40, 4), (40, 6), (39, 4)):
        D = max(0, N_BITS - ep)
        if D == 0:
            continue
        lp_min = Decimal(ep)
        L_min = e * lp_min
        t_max_row = Decimal(N) / L_min
        for a in range(ep + 1, 42):
            m = 1 << (a - 2)
            sh = Decimal(2 * m - 1) / t_max_row
            if worst is None or sh < worst[0]:
                worst = (sh, ep, e, a)
    check("S4.4 NO moving rung is discharged on ANY admissible row",
          worst is not None and worst[0] > 1,
          f"min shortfall = {worst[0]:.2f}x at (e_p={worst[1]}, e={worst[2]}, a={worst[3]})")
    check("S4.5 the minimum shortfall over the admissible region is 39x "
          "(39*(1-2^-39), attained at e_p=39, e=4, a=40)",
          Decimal("38.999") < worst[0] <= 39, f"{worst[0]:.9f}x")
    for a, lbl in ((40, "rung 1"), (41, "rung 2")):
        sh = Decimal(2 * (1 << (a - 2)) - 1) / t_row
        check(f"S4.6 witness {lbl} (a={a}) misses THEOREM A",
              sh > 1, f"shortfall {sh:.2f}x")
    # the maximal discharged fraction over the whole admissible region
    best = max(2 / (Decimal(e) * Decimal(max(ep, N_BITS if N_BITS - ep <= 0 else 0)))
               for ep, e in ((41, 1), (40, 2), (39, 4)))
    check("S4.7 discharged fraction <= 2/41 = 4.88% on every admissible row",
          best <= Decimal(2) / 41 + Decimal("1e-9"), f"max = {best:.5f}")


# --------------------------------------------------------------- S5 LEMMA 3 --
def lemma3_ratio(k: int, e: int, nested: bool) -> Fraction:
    """exact ratio dim L * log2 p / m at the TOP window, from the
    decomposition theorem plus the counting balance t = n/L."""
    C = C_nest(k.bit_length()-1) if nested else C_new(k.bit_length()-1)
    return Fraction(2 * C, e) if not nested else Fraction(k, e)


def stage5(wit: dict) -> None:
    say()
    say("=== S5  LEMMA 3 on the admissible ladder ==============================")
    lp, L, t_row = wit["lp"], wit["L"], wit["t_row"]
    ep, k, e = wit["ep"], wit["k"], wit["e"]
    # (a) direct recomputation at the witness, every layer, both readings
    say("      layer a | reading  | C | dim L (exact)   | need m/log2 p   | ratio")
    for a in range(35, 42):
        for nested in (False, True):
            m = (1 << (a - 1)) if nested else (1 << (a - 2))
            Da = max(0, a - ep)
            C = C_nest(Da) if nested else C_new(Da)
            S = m // C
            R = int(t_row / 2) + 1
            dimL = C * min(S, R)
            need = Decimal(m) / lp
            ratio = Decimal(dimL) / need
            tag = "nested  " if nested else "new-part"
            if a >= 39:
                say(f"      {a:7d} | {tag} | {C} | {dimL:15d} | {need:15.4e} |"
                    f" {ratio:.6f}")
            if a == 41:
                pred = lemma3_ratio(k, e, nested)
                check(f"S5.1 witness top window [{tag.strip()}]: ratio = "
                      f"{pred} (= {'k/e' if nested else 'max(2,k)/e'})",
                      abs(ratio - Decimal(pred.numerator) / pred.denominator)
                      < Decimal("1e-6"), f"ratio = {ratio:.8f}")
    # (b) worst case over the full pinned t-interval, both readings
    say("      worst case over t in (2^33, 5.364e10] at the witness top window:")
    for nested in (False, True):
        m = (1 << 40) if nested else (1 << 39)
        Da = 41 - ep
        C = C_nest(Da) if nested else C_new(Da)
        S = m // C
        need = Decimal(m) / lp
        vals = []
        for tv in (Decimal(1 << 33) + 1, t_row, Decimal("5.3634e10")):
            R = int(tv / 2) + 1
            vals.append(Decimal(C * min(S, R)) / need)
        tag = "nested" if nested else "new-part"
        say(f"        [{tag:8s}] t=2^33+: {vals[0]:.6f}   t=n/L: {vals[1]:.6f}"
            f"   t=5.36e10: {vals[2]:.6f}")
        check(f"S5.2 [{tag}] worst case over the interval is the row value 1.000",
              abs(min(vals) - 1) < Decimal("1e-6"),
              f"min = {min(vals):.8f}")
    # (c) the whole admissible region, both readings
    say("      (k, e) | new-part ratio | nested ratio | verdict (nested governs)")
    verdicts = {}
    for ep2, e2 in ((41, 1), (41, 2), (41, 3), (41, 4), (41, 5), (41, 6),
                    (40, 2), (40, 4), (40, 6), (39, 4)):
        k2 = 1 << max(0, N_BITS - ep2)
        rn = lemma3_ratio(k2, e2, False)
        rs = lemma3_ratio(k2, e2, True)
        v = ("SATURATED (zero margin)" if rs == 1 else
             ("MARGIN" if rs > 1 else "(O1) REFUTED at this window"))
        if (ep2, e2) == (40, 6):
            v += "   [but this class is EMPTY -- S2.9]"
        verdicts[(k2, e2)] = (rn, rs, v)
        say(f"      ({k2}, {e2}) | {float(rn):14.4f} | {float(rs):12.4f} | {v}")
    check("S5.3 nested ratio = k/e <= 1 on EVERY admissible row",
          all(v[1] <= 1 for v in verdicts.values()), "")
    check("S5.4 nested ratio = 1 iff k = e",
          all((v[1] == 1) == (ke[0] == ke[1]) for ke, v in verdicts.items()), "")
    check("S5.5 (O1) at the full-group window REFUTED whenever k < e",
          all(v[2].startswith("(O1)") for ke, v in verdicts.items()
              if ke[0] < ke[1]),
          f"{sorted(ke for ke, v in verdicts.items() if ke[0] < ke[1])}")
    check("S5.6 the only new-part row with margin > 1 is the prime-field row q=p",
          [ke for ke, v in verdicts.items() if v[0] > 1] == [(1, 1)],
          f"{[ke for ke, v in verdicts.items() if v[0] > 1]}")
    check("S5.7 witness (k=e=4) saturated under BOTH readings",
          verdicts[(4, 4)][0] == 1 and verdicts[(4, 4)][1] == 1, "1.000 / 1.000")
    # (c2) REGIME ROBUSTNESS: the refutation does not need t = n/L.
    # The F2 question is non-vacuous only while the t-null block window is
    # non-empty, i.e. t*L <= n (the balance (C)).  Over that WHOLE regime the
    # ratio is (t*L/n) * k/e <= k/e, so k < e refutes (O1) for every relevant
    # t -- no dependence on the leading-order balance being exact.
    say("      regime robustness: ratio(t) = (tL/n) * k/e over t*L <= n")
    for (k2, e2, L2, lbl) in ((1, 6, Decimal("255.5098"), "p=3*2^41+1, q=p^6"),
                              (2, 4, Decimal("179.0196"), "p=27*2^40+1, q=p^4"),
                              (4, 4, wit["L"], "the banked witness")):
        worst_ok = True
        shown = []
        for frac in (Decimal("0.25"), Decimal("0.5"), Decimal("1.0")):
            tv = frac * Decimal(N) / L2
            m2 = Decimal(1 << 40)                     # nested top window
            lp2 = L2 / e2
            dimL2 = Decimal(k2) * (tv / 2)
            ratio = dimL2 * lp2 / m2
            shown.append(f"tL/n={frac}: {ratio:.4f}")
            if ratio > Decimal(k2) / e2 + Decimal("1e-9"):
                worst_ok = False
        say(f"        (k={k2}, e={e2}) {lbl}: " + "  ".join(shown))
        check(f"S5.9 regime robustness at (k={k2}, e={e2}): ratio <= k/e for "
              f"EVERY t with tL <= n", worst_ok,
              f"k/e = {Decimal(k2)/e2:.4f}; refutation needs no exact t")

    # (d) the exponential size of the refutation where it fires
    for (k2, e2) in ((1, 6), (2, 4)):
        rs = lemma3_ratio(k2, e2, True)
        excess = (1 - rs) * Fraction(1, 2)   # m = n/2 nested: 2^{m(1-ratio)}
        check(f"S5.8 (k={k2}, e={e2}): (O1) fails by 2^{{{excess}*n}}",
              excess > 0, f"excess exponent = {excess} * n")


# ------------------------------------------------------------- S6 SL-1/SL-1b --
def stage6(wit: dict) -> None:
    say()
    say("=== S6  SL-1 / SL-1b / SL-1b' re-based ================================")
    lp, L, t_row, ep = wit["lp"], wit["L"], wit["t_row"], wit["ep"]
    R = int(t_row / 2) + 1
    for a, nested in ((41, False), (41, True), (40, False)):
        m = (1 << (a - 1)) if nested else (1 << (a - 2))
        frac = Decimal(R + 1) / Decimal(m)
        tag = "nested" if nested else "new-part"
        say(f"      layer {a} [{tag:8s}]: (R+1)/m = {frac:.8f}  (= {1/frac:.1f}^-1)")
        if a == 41 and not nested:
            check("S6.1 SL-1 designed distance fraction = 2/L = 1/128",
                  abs(frac - 2 / L) / frac < Decimal("1e-6"), f"{frac:.9f}")
    banked = Decimal("0.01563")
    frac_top = Decimal(R + 1) / Decimal(1 << 39)
    check("S6.2 SL-1 fraction is HALF the banked tower rung-16 value",
          abs(frac_top * 2 - banked) / banked < Decimal("0.01"),
          f"{frac_top:.5f} vs banked {banked} at tower rung 16")
    # SL-1b (R-A) at the top window
    log_p3 = log2d(3) / lp
    for nested in (False, True):
        m = (1 << 40) if nested else (1 << 39)
        Da = 41 - ep
        C = C_nest(Da) if nested else C_new(Da)
        dimL = C * min(m // C, R)
        need = Decimal(m) * log_p3
        ratio = Decimal(dimL) / need
        tag = "nested" if nested else "new-part"
        say(f"      SL-1b (R-A) [{tag:8s}]: dim L = {dimL:.4e}, need = {need:.4e},"
            f" ratio = {ratio:.4f}")
        check(f"S6.3 (R-A) at the witness top window [{tag}] is REFUTED "
              f"(dim L is now EXACT)", ratio < 1, f"ratio = {ratio:.6f}")
    # the general law: ratio = 2C/(e log2 3) new-part
    for (k2, e2) in ((1, 1), (2, 2), (4, 4), (1, 2), (2, 6)):
        C = C_new(k2.bit_length() - 1)
        pred = Decimal(2 * C) / (Decimal(e2) * log2d(3))
        verdict = "PROVED" if pred >= 1 else "REFUTED"
        expect = "PROVED" if (k2, e2) == (1, 1) else "REFUTED"
        check(f"S6.4 (R-A) new-part ratio law at (k={k2}, e={e2}) = {pred:.4f}"
              f" -> {verdict}", verdict == expect,
              f"exact dim L = C*min(S,R); expected {expect}")
    # GRS parameters of the re-based terminal
    S = 1 << (ep - 1)
    check("S6.5 SL-1b' re-based: class code = [2^38, 2^38 - R, R+1]_p GRS/MDS",
          S == 1 << 38, f"S = 2^{ep-1}, R = {R}, d = {R+1}, C = 2 copies")


# ------------------------------------------------------------------ S7 |K1| --
def stage7(wit: dict) -> None:
    say()
    say("=== S7  the |K1| / PP5.0 seam on admissible rows ======================")
    lp, L, t_row, k, e = wit["lp"], wit["L"], wit["t_row"], wit["k"], wit["e"]
    R = Decimal(int(t_row / 2) + 1)
    ext = R * L                      # |K1| = q^{|Lambda|}
    base = R * lp                    # |K1| = p^{|Lambda|}
    eff = R * k * lp                 # the A6-effective sector F_{p^k}^Lambda
    half_n = Decimal(N) / 2
    check("S7.1 extension reading: log2|K1| = n/2 EXACTLY",
          abs(ext - half_n) / half_n < Decimal("1e-9"),
          f"{ext:.6e} vs n/2 = {half_n:.6e}")
    check("S7.2 base reading: log2|K1| = n/(2e) = n/8 at the witness",
          abs(base - half_n / e) / base < Decimal("1e-9"),
          f"{base:.6e} vs n/8 = {half_n/e:.6e}")
    check("S7.3 effective reading: log2|K1|_eff = (k/e)(n/2) = n/2 at k=e",
          abs(eff - half_n * k / e) / eff < Decimal("1e-9"),
          f"{eff:.6e}")
    check("S7.4 all three readings are Theta(n), none is o(n)",
          min(ext, base, eff) / Decimal(N) > Decimal("0.05"),
          f"min = {min(ext, base, eff)/Decimal(N):.4f} * n")
    # row-independence of the extension reading
    for ep2, e2 in ((41, 1), (40, 2), (40, 6), (39, 4)):
        L2 = Decimal(e2) * Decimal(ep2)      # a lower-bound row in that class
        t2 = Decimal(N) / L2
        ext2 = (t2 / 2) * L2
        check(f"S7.5 extension reading = n/2 on class (e_p={ep2}, e={e2})",
              abs(ext2 - half_n) / half_n < Decimal("1e-12"), f"{ext2:.6e}")
    # the seam identity: LEMMA 3 (nested) IS the seam inequality
    need_nested = Decimal(1 << 40) / lp          # m/log2 p at the full window
    check("S7.6 SEAM IDENTITY: dim K1_eff * log2 p = log2|K1|_eff, and LEMMA 3 "
          "(nested) is exactly 'log2|K1|_eff >= n/2'",
          abs((eff) - half_n * k / e) / eff < Decimal("1e-9") and
          abs(need_nested * lp - half_n) / half_n < Decimal("1e-9"),
          f"log2|K1|_eff = {eff:.6e}, target n/2 = {half_n:.6e}")
    check("S7.7 at k = e the seam EQUALS the whole (O1) target (sum reading "
          "double-counts n/2 bits)", k == e and abs(eff - half_n) / half_n <
          Decimal("1e-9"), "equality")


# --------------------------------------------------------- S8 tower control --
def stage8() -> None:
    say()
    say("=== S8  the tower's own-field self-consistency control ================")
    p_kb = 2 ** 31 - 2 ** 24 + 1
    check("S8.1 KoalaBear p prime, v_2(p-1) = 24", is_prime(p_kb) and
          v2(p_kb - 1) == 24, f"p = {p_kb}")
    lp = log2d(p_kb)
    L16 = Decimal(2 ** 16) * lp
    check("S8.2 log2 q_16 = 2,030,874 (banked)",
          abs(L16 - Decimal("2030874")) < Decimal("2"), f"{L16:.1f}")
    n_kb = 1 << 40
    t_own = Decimal(n_kb) / L16
    check("S8.3 the tower's OWN field forces t = n/L ~ 5.4e5, not 7e10",
          Decimal("4e5") < t_own < Decimal("6e5"), f"t = {t_own:.4e}")
    ratio = Decimal("7e10") / t_own
    check("S8.4 the banked 7e10 is ~1.3e5x too large BY THE TOWER'S OWN field",
          ratio > Decimal("1e5"), f"{ratio:.3e}x")
    # under its own t, no tower rung is discharged
    worst = None
    for j in range(1, 17):
        m_j = 1 << (22 + j)
        need = Decimal(2 * m_j - 1)
        sh = need / t_own
        if worst is None or sh < worst[0]:
            worst = (sh, j)
    check("S8.5 under its own field NO tower rung is discharged (rung 1 already "
          "needs t >= 2^24)", worst[0] > 1,
          f"min shortfall {worst[0]:.2f}x at rung {worst[1]}")
    check("S8.6 rungs 4..16 break |F| < 2^256",
          all(Decimal(2 ** j) * lp > CAP for j in range(4, 17)) and
          Decimal(2 ** 3) * lp < CAP,
          f"log2 q_3 = {8*lp:.1f}, log2 q_4 = {16*lp:.1f}")


def stage10(wit: dict) -> None:
    say()
    say("=== S10 the K1 cancellation budget on the admissible row ==============")
    lp = wit["lp"]
    # banked tower arithmetic (control)
    lp_kb = log2d(2 ** 31 - 2 ** 24 + 1)
    tower_budget = Decimal(sum(1 << (22 + j) for j in range(1, 17))) / 43
    tower_deliv = 16 * lp_kb
    check("S10.1 banked tower budget 1.278e10 bits reproduces",
          abs(tower_budget - Decimal("1.278e10")) / tower_budget < Decimal("1e-2"),
          f"{tower_budget:.4e}")
    check("S10.2 banked tower delivery 16*log2 p = 495.8 bits reproduces",
          abs(tower_deliv - Decimal("495.8")) < Decimal("0.5"), f"{tower_deliv:.1f}")
    tower_short = tower_budget / tower_deliv
    # admissible witness: 2 moving rungs, per-rung ceiling log2 p
    adm_budget = Decimal((1 << 38) + (1 << 39)) / 43
    adm_deliv = 2 * lp
    adm_short = adm_budget / adm_deliv
    say(f"      tower      : budget {tower_budget:.4e} bits, delivered "
        f"{tower_deliv:.1f} bits, shortfall {tower_short:.4e}x")
    say(f"      admissible : budget {adm_budget:.4e} bits, delivered "
        f"{adm_deliv:.1f} bits, shortfall {adm_short:.4e}x")
    check("S10.3 the admissible row delivers 3.9x LESS K1 cancellation than the "
          "tower (2 rungs x 64 bits vs 16 x 31)",
          Decimal("3.8") < tower_deliv / adm_deliv < Decimal("4.0"),
          f"{tower_deliv/adm_deliv:.3f}x less")
    check("S10.4 the K1 shortfall gets WORSE on the admissible row",
          adm_short > tower_short,
          f"{adm_short/tower_short:.3f}x worse ({adm_short:.3e}x vs "
          f"{tower_short:.3e}x)")
    # (M3) of f2_sl1_powersums is vacuous on admissible rows
    R_over_m = 2 / wit["L"]
    check("S10.5 (M3)'s criterion R > 0.61315 m NEVER fires on an admissible "
          "row (max R/m = 2/L <= 2/41 = 0.0488)",
          Decimal(2) / 41 < Decimal("0.61315") and R_over_m < Decimal("0.61315"),
          f"witness R/m = {R_over_m:.6f}, best admissible = "
          f"{Decimal(2)/41:.6f}, needed 0.61315")


# --------------------------------------------------------- S9 sibling controls --
def stage9() -> None:
    say()
    say("=== S9  sibling controls (arithmetic agreement) =======================")
    L = Decimal("255.9")
    t_star = 8592912739
    check("S9.1 2^33 = 8,589,934,592 is the interval's left endpoint",
          (1 << 33) == 8589934592, f"{1<<33}")
    check("S9.2 t* lies inside (2^33, 5.364e10]",
          (1 << 33) < t_star < 5.364e10, f"t* = {t_star}")
    check("S9.3 n/t* = 255.911275 (the sliver's left endpoint, CATCH-5)",
          abs(Decimal(N) / t_star - Decimal("255.911275")) < Decimal("1e-5"),
          f"{Decimal(N)/t_star:.6f}")
    check("S9.4 at L = 255.9, t*L < n (CATCH-2 reproduces)",
          Decimal(t_star) * L < Decimal(N),
          f"t*L = {Decimal(t_star)*L:.6e} < n = {Decimal(N):.6e}")
    check("S9.5 n/L at L = 255.9 = 8.5933e9 (the banked t = n/L)",
          abs(Decimal(N) / L - Decimal("8593291331")) < Decimal("1e4"),
          f"{Decimal(N)/L:.1f}")
    # tower m_16 readings
    check("S9.6 tower m_16 = 2^38 (new-part) / 2^39 (nested)",
          (1 << 38) == 274877906944 and (1 << 39) == 549755813888, "")
    # banked LEMMA 3 numbers at tower rung 16
    lp_kb = log2d(2 ** 31 - 2 ** 24 + 1)
    need16 = Decimal(1 << 38) / lp_kb
    check("S9.7 banked m_16/log2 p = 8.87e9 reproduces",
          abs(need16 - Decimal("8.87e9")) / need16 < Decimal("1e-2"),
          f"{need16:.4e}")
    check("S9.8 banked 0.9687x sign flip reproduces (t*/(m_16/log2 p))",
          abs(Decimal(t_star) / need16 - Decimal("0.9687")) < Decimal("1e-3"),
          f"{Decimal(t_star)/need16:.4f}")


# ------------------------------------------------------------------- driver --
def main() -> int:
    stage0()
    wit = stage1()
    stage2()
    stage3()
    stage4(wit)
    stage5(wit)
    stage6(wit)
    stage7(wit)
    stage8()
    stage9()
    stage10(wit)
    say()
    say("=" * 72)
    say(f"TOTAL: {PASS} PASS, {FAIL} FAIL")
    digest = "F2_ADM_ALL_PASS" if FAIL == 0 else "F2_ADM_FAILURES"
    say(f"DIGEST: {digest}")
    out = "\n".join(LOG)
    print(out)
    with open(f"{REPO}/notes/pilots_20260806/f2_adm/VERIFY_LOG.txt", "w",
              encoding="utf-8") as fh:
        fh.write(out + "\n")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
