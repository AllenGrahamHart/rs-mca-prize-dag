#!/usr/bin/env python3
"""Verifier for f2_antipodal_descent_lemma.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers, deterministic, no third-party imports, no file reads.

The banked first-descent window model is RE-IMPLEMENTED FROM SCRATCH here
(provenance for the conventions, in comments only:
 notes/pilots_20260802/f2_carry_reachability/f2model.py  -- Fp2, pair_reps,
     residues, half_flag
 notes/pilots_20260802/f2_slice_coefficients/slicecore.py -- sigma_of, Delta_of
 notes/pilots_20260802/f2_deployed_windows/tower.py:22-43 -- the lemma).

  A  LTE at the official KoalaBear prime p = 2^31-2^24+1 (e = 24),
     rungs j = 0..16, by TWO independent routes
  B  LTE at 8 further primes with e = 2..8
  C  clause (iii) at rung 1: every y of order exactly 2^{e+1} in F_{p^2}
     has y^p = -y and Tr(y) = 0                       (positive control)
  D  clause (ii) at rung 1: mu_{2^{e+1}} ^ F_p = mu_{2^e}
  E  Corollary B EXHAUSTIVELY over every frequency c in F_{p^2}^*:
     all Delta_i even on the rung-1 window, 0 violations
  F  Corollary C: R_p = 1 and flat = 0 EXACTLY (integer arithmetic)
  G  Corollary D: sub-window inheritance
  H  NON-VACUITY: the full-group window at the same primes has odd
     Delta_i, so the k = p mode is alive there -- the law is a property
     of the rung subgroups, not of the model
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

FAILURES = []


def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    if not ok:
        FAILURES.append(label)


# --------------------------------------------------------------- 2-adics --

def v2(x: int) -> int:
    assert x != 0
    n = 0
    while x % 2 == 0:
        x //= 2
        n += 1
    return n


# ------------------------------------------------------------ F_{p^2} ----

def nonresidue(p: int) -> int:
    """least quadratic non-residue mod p (f2model.nonresidue)."""
    for a in range(2, p):
        if pow(a, (p - 1) // 2, p) == p - 1:
            return a
    raise AssertionError("no non-residue")


class Fp2:
    """F_{p^2} = F_p(w), w^2 = N0; elements are pairs (a, b) = a + b w."""

    def __init__(self, p: int):
        self.p = p
        self.N0 = nonresidue(p)

    def mul(self, x, y):
        p, N = self.p, self.N0
        a1, b1 = x
        a2, b2 = y
        return ((a1 * a2 + N * b1 * b2) % p, (a1 * b2 + a2 * b1) % p)

    def pw(self, x, e):
        r, b = (1, 0), x
        while e:
            if e & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            e >>= 1
        return r

    def trace(self, x):
        return (2 * x[0]) % self.p

    def neg(self, x):
        return ((-x[0]) % self.p, (-x[1]) % self.p)

    def order(self, x):
        o = self.p * self.p - 1
        for q in factor(o):
            while o % q == 0 and self.pw(x, o // q) == (1, 0):
                o //= q
        return o

    def generator(self):
        tgt = self.p * self.p - 1
        prs = factor(tgt)
        for a in range(self.p):
            for b in range(self.p):
                if (a, b) == (0, 0):
                    continue
                if all(self.pw((a, b), tgt // q) != (1, 0) for q in prs):
                    return (a, b)
        raise AssertionError("no generator")

    def subgroup(self, n: int):
        tgt = self.p * self.p - 1
        assert tgt % n == 0
        g = self.pw(self.generator(), tgt // n)
        out, cur = [], (1, 0)
        for _ in range(n):
            out.append(cur)
            cur = self.mul(cur, g)
        assert cur == (1, 0)
        return out


def factor(m: int):
    out, d = set(), 2
    while d * d <= m:
        if m % d == 0:
            out.add(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        out.add(m)
    return sorted(out)


# ------------------------------------------------ the window model -------
#
# pair_reps convention (f2model.pair_reps): one representative per genuine
# conjugate pair = the member whose w-component lies in [1, (p-1)/2].
# residues(c, y) = (Tr(c y), Tr(c y^p)) as least residues in [0, p).
# half_flag(p, s) = 1 iff 2s > p.   sigma = s + p*half_flag  (mod 2p).
# Delta = sigma^+ - sigma^-  (mod 2p).

def pair_reps(F: Fp2, mu):
    half = (F.p - 1) // 2
    return [y for y in mu if 1 <= y[1] <= half]


def residues(F: Fp2, c, y):
    p, N = F.p, F.N0
    ac, bc = c
    ay, by = y
    return ((2 * (ac * ay + N * bc * by)) % p,
            (2 * (ac * ay - N * bc * by)) % p)


def deltas(F: Fp2, c, reps):
    p = F.p
    two_p = 2 * p
    out = []
    for y in reps:
        sp, sm = residues(F, c, y)
        gp = (sp + p * (1 if 2 * sp > p else 0)) % two_p
        gm = (sm + p * (1 if 2 * sm > p else 0)) % two_p
        out.append((gp - gm) % two_p)
    return out


# ------------------------------------------------------------- checks ----

KOALABEAR = (1 << 31) - (1 << 24) + 1          # 2130706433, p-1 = 2^24 * 127
# 8 further primes p == 1 (mod 4) with the recorded e = v_2(p-1)
PRIMES_E = [13, 17, 29, 41, 97, 193, 257, 641]


def stage_A():
    p = KOALABEAR
    ok_prime = all(p % d for d in range(2, 50000)) and p > 2
    e = v2(p - 1)
    check("A0: the official KoalaBear prime p = 2^31-2^24+1 = 2130706433 "
          "is PRIME (trial division to 5e4; 46160^2 > p, so the screen is "
          "a complete proof) and v_2(p-1) = e = 24, p-1 = 2^24 * 127",
          ok_prime and e == 24 and (p - 1) == (1 << 24) * 127
          and 50000 * 50000 > p,
          f"p={p} e={e}")
    # route 1: exact big integers, j = 0..6
    bad1 = []
    for j in range(0, 7):
        q = pow(p, 1 << j)
        if v2(q - 1) != e + j:
            bad1.append((j, v2(q - 1)))
    check("A1: LTE at KoalaBear by EXACT big integers, rungs j = 0..6: "
          "v_2(p^{2^j} - 1) = 24 + j", not bad1, f"bad={bad1}")
    # route 2: modulo 2^64 (valid because e+j <= 40 < 64), j = 0..16
    bad2 = []
    M = 1 << 64
    for j in range(0, 17):
        q = pow(p, 1 << j, M)
        d = (q - 1) % M
        val = 64 if d == 0 else v2(d)
        if val != e + j:
            bad2.append((j, val))
    check("A2: LTE at KoalaBear by the 2^64-modular route, ALL 16 official "
          "rungs j = 0..16: v_2(p^{2^j} - 1) = 24 + j (valid since "
          "e+j <= 40 < 64)", not bad2, f"bad={bad2}")
    # the two routes agree where they overlap
    agree = all(v2(pow(p, 1 << j) - 1) == v2((pow(p, 1 << j, M) - 1) % M)
                for j in range(0, 7))
    check("A3: the exact and modular routes agree on their overlap "
          "(j = 0..6)", agree)


def stage_B():
    bad = []
    rows = []
    for p in PRIMES_E:
        e = v2(p - 1)
        if e < 2:
            bad.append((p, "e < 2"))
            continue
        rows.append((p, e))
        for j in range(0, 7):
            if v2(pow(p, 1 << j) - 1) != e + j:
                bad.append((p, j))
    check("B: LTE v_2(p^{2^j}-1) = v_2(p-1) + j at 8 further primes "
          "(e = 2..8), rungs j = 0..6", not bad and len(rows) == 8,
          f"(p,e) = {rows}")


def stage_C_D():
    bad_c, bad_d, tot = [], [], 0
    for p in (13, 17, 29, 41, 97):
        e = v2(p - 1)
        F = Fp2(p)
        n1 = 1 << (e + 1)
        assert (p * p - 1) % n1 == 0
        mu = F.subgroup(n1)
        genuine = [y for y in mu if F.order(y) == n1]
        # (iii): y^{q_0} = y^p = -y and Tr(y) = 0
        for y in genuine:
            tot += 1
            if F.pw(y, p) != F.neg(y):
                bad_c.append((p, y, "y^p != -y"))
            if F.trace(y) != 0:
                bad_c.append((p, y, "Tr != 0"))
        if len(genuine) != (1 << e):
            bad_c.append((p, "count", len(genuine)))
        # (ii): mu_{n_1} ^ F_p = mu_{2^e}  (x in F_p  <=>  x^p == x)
        in_fp = [y for y in mu if F.pw(y, p) == y]
        n0 = 1 << e
        ok = (len(in_fp) == n0 and
              all(F.pw(y, n0) == (1, 0) for y in in_fp))
        if not ok:
            bad_d.append((p, len(in_fp), n0))
    check("C: clause (iii) at rung 1 -- every element of order exactly "
          "2^{e+1} in F_{p^2} satisfies y^p = -y and Tr(y) = 0 "
          "(and there are exactly 2^e of them)", not bad_c,
          f"{tot} genuine elements over p = 13,17,29,41,97; bad={bad_c[:3]}")
    check("D: clause (ii) at rung 1 -- mu_{2^{e+1}} ^ F_p = mu_{2^e} "
          "exactly", not bad_d, f"bad={bad_d}")


def stage_E_F_G():
    bad_e, bad_f, bad_g = [], [], []
    freqs_total = 0
    rows = []
    for p in (13, 17, 29, 41):
        e = v2(p - 1)
        F = Fp2(p)
        n1 = 1 << (e + 1)
        mu = F.subgroup(n1)
        reps = pair_reps(F, mu)
        m = len(reps)
        # m = (n_ord - gcd(n_ord, p-1))/2 = (2^{e+1} - 2^e)/2 = 2^{e-1}
        if m != (1 << (e - 1)):
            bad_e.append((p, "m", m, 1 << (e - 1)))
        rows.append((p, e, m))
        # E: EVERY frequency c in F_{p^2}^*
        for ac in range(p):
            for bc in range(p):
                if (ac, bc) == (0, 0):
                    continue
                freqs_total += 1
                ds = deltas(F, (ac, bc), reps)
                if any(x % 2 for x in ds):
                    bad_e.append((p, (ac, bc), "odd Delta"))
                    continue
                # F: R_p = (1/m) sum (-1)^{Delta} = 1  EXACTLY (integers)
                num = sum(1 if x % 2 == 0 else -1 for x in ds)
                if num != m:
                    bad_f.append((p, (ac, bc), num, m))
        # G: sub-window inheritance -- every non-empty subset keeps it
        c0 = (1, 1)
        ds = deltas(F, c0, reps)
        seed = 12345
        for _ in range(40):
            seed = (6364136223846793005 * seed + 1442695040888963407) % (1 << 64)
            mask = (seed >> 5) % (1 << m)
            if mask == 0:
                continue
            sub = [ds[i] for i in range(m) if (mask >> i) & 1]
            if any(x % 2 for x in sub):
                bad_g.append((p, mask, "odd in sub-window"))
            if sum(1 if x % 2 == 0 else -1 for x in sub) != len(sub):
                bad_g.append((p, mask, "R_p != 1 on sub-window"))
    check("E: Corollary B -- on the rung-1 deployed window EVERY Delta_i "
          "is EVEN, at EVERY frequency c in F_{p^2}^* (exhaustive)",
          not bad_e, f"{freqs_total} frequencies over (p,e,m) = {rows}; "
                     f"bad={bad_e[:3]}")
    check("F: Corollary C -- R_p = (1/m) sum_i (-1)^{Delta_i} = 1 EXACTLY "
          "at every one of those frequencies, so flat = 0 exactly "
          "(integer arithmetic, no floats)", not bad_f, f"bad={bad_f[:3]}")
    check("G: Corollary D -- 160 random non-empty SUB-windows all inherit "
          "all-Delta-even and R_p = 1 (selection cannot repair it)",
          not bad_g, f"bad={bad_g[:3]}")


def stage_H():
    """NON-VACUITY: the law is about the rung subgroups, not the model."""
    rows, bad = [], []
    for p in (13, 17, 29, 41):
        F = Fp2(p)
        n_ord = p * p - 1
        mu = F.subgroup(n_ord)
        reps = pair_reps(F, mu)
        m = len(reps)
        if m != p * (p - 1) // 2:
            bad.append((p, "m", m))
        ds = deltas(F, (1, 1), reps)
        odd = sum(1 for x in ds if x % 2)
        num = sum(1 if x % 2 == 0 else -1 for x in ds)
        rows.append((p, m, odd, num))
        if odd == 0:
            bad.append((p, "no odd Delta at the full group"))
        if abs(num) >= m:
            bad.append((p, "|R_p| = 1 at the full group"))
    check("H: NON-VACUITY -- at the SAME primes the FULL-group window "
          "(n_ord = p^2-1, c = (1,1)) has odd Delta_i and |R_p| < 1, so "
          "the mode k = p is alive there; the degeneracy is a property of "
          "the rung subgroups, not of the model",
          not bad, f"(p, m, #odd, m*R_p) = {rows}")


def main():
    stage_A()
    stage_B()
    stage_C_D()
    stage_E_F_G()
    stage_H()
    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("F2_ANTIPODAL_DESCENT_LEMMA_ALL_PASS")


if __name__ == "__main__":
    main()
