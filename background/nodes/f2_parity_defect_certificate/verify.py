#!/usr/bin/env python3
"""Verifier for f2_parity_defect_certificate.

PROFILE: tiny.   Run:  tools/ramguard tiny -- python3 verify.py
Pure python integers, deterministic, no third-party imports, no file reads.
Every CHECK is exact integer / exact cyclotomic-integer arithmetic; the one
float line is printed as a DIAGNOSTIC and is not a check.

The banked first-descent window model and the exact ring Z[zeta_p] are
RE-IMPLEMENTED FROM SCRATCH (provenance, in comments only:
 f2_carry_reachability/f2model.py, f2_slice_coefficients/slicecore.py,
 f2_deployed_windows/deployed.py:37-56 + :126-147, census.py:65-75,
 f2_deployed_windows/verify.py:300-321 (A8)).

  A  the grouping identity (ID) R_k = (1/m) sum_d c_d omega^{k x_d} for
     EVERY odd k, checked exactly in Z[zeta_p] against a direct evaluation
  B  non-vacuity of (DEF) at the full group: 2D < m, i.e. D/m < 1/2
  C  the autocorrelation formula A(t) = (-1)^t (p - 2t), 0 <= t <= M
  D  the support of (c_d) is a HALF-SYSTEM of F_p^*
  E  THEOREM 2 exhaustively: D = ((p-1)/2)^2 at EVERY frequency with
     a_c b_c != 0, p = 11,13,19,23,31,41  (incl. the pilot's own A8 row)
  F  THEOREM 3: the ONLY exceptions are a_c = 0 and b_c = 0, and D = m there
  G  the multiplicity law  [1,2,...,p-1]                   (MEASURED label)
  H  Corollary 4: rung-1 deployed windows have D = m and R_p = 1 exactly
  I  D is invariant under the GLOBAL orientation reversal, and partial
     flips DO change it (so D is not label-free)
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

FAILURES = []


def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    if not ok:
        FAILURES.append(label)


# ------------------------------------------------------------ Z[zeta_p] --
# integer vectors of length p modulo sum_i zeta^i = 0; canonical: c[p-1] = 0.

def zcanon(v, p):
    t = v[p - 1]
    if t:
        return [x - t for x in v]
    return v


def zadd(a, b, p):
    return zcanon([x + y for x, y in zip(a, b)], p)


def omega_pow_vec(p, e):
    """omega^e as a Z[zeta_p] vector, omega = zeta_{2p} = -zeta_p^{(p+1)/2}."""
    e %= 2 * p
    sign = -1 if (e & 1) else 1
    idx = (e * ((p + 1) // 2)) % p
    v = [0] * p
    v[idx] = sign
    return zcanon(v, p)


# ------------------------------------------------------------ F_{p^2} ----

def nonresidue(p):
    for a in range(2, p):
        if pow(a, (p - 1) // 2, p) == p - 1:
            return a
    raise AssertionError


def full_group_reps(p):
    """pair reps of mu_{p^2-1}: w-component in [1,(p-1)/2]."""
    return [(a, b) for a in range(p) for b in range(1, (p - 1) // 2 + 1)]


def rung1_reps(p, N0):
    """pair reps of mu_{2^{e+1}} (the deployed rung-1 window)."""
    e = 0
    t = p - 1
    while t % 2 == 0:
        t //= 2
        e += 1
    n1 = 1 << (e + 1)
    # elements of mu_{n1} in F_{p^2}: build via a generator of F_{p^2}^*
    tgt = p * p - 1
    assert tgt % n1 == 0

    def mul(x, y):
        return ((x[0] * y[0] + N0 * x[1] * y[1]) % p,
                (x[0] * y[1] + x[1] * y[0]) % p)

    def pw(x, k):
        r, b = (1, 0), x
        while k:
            if k & 1:
                r = mul(r, b)
            b = mul(b, b)
            k >>= 1
        return r

    def factor(mm):
        out, d = set(), 2
        while d * d <= mm:
            if mm % d == 0:
                out.add(d)
                while mm % d == 0:
                    mm //= d
            d += 1
        if mm > 1:
            out.add(mm)
        return sorted(out)

    prs = factor(tgt)
    gen = None
    for a in range(p):
        for b in range(p):
            if (a, b) == (0, 0):
                continue
            if all(pw((a, b), tgt // q) != (1, 0) for q in prs):
                gen = (a, b)
                break
        if gen:
            break
    g = pw(gen, tgt // n1)
    mu, cur = [], (1, 0)
    for _ in range(n1):
        mu.append(cur)
        cur = mul(cur, g)
    half = (p - 1) // 2
    return [y for y in mu if 1 <= y[1] <= half], e


def deltas(p, N0, c, reps):
    ac, bc = c
    two_p = 2 * p
    out = []
    for (ay, by) in reps:
        sp = (2 * (ac * ay + N0 * bc * by)) % p
        sm = (2 * (ac * ay - N0 * bc * by)) % p
        gp = (sp + p * (1 if 2 * sp > p else 0)) % two_p
        gm = (sm + p * (1 if 2 * sm > p else 0)) % two_p
        out.append((gp - gm) % two_p)
    return out


def parity_classes(p, ds):
    """c_d (exact ints) and the even representative x_d (deployed.py:126-135)."""
    cd = [0] * p
    for x in ds:
        x %= 2 * p
        cd[x % p] += 1 if x % 2 == 0 else -1
    xd = [(d if d % 2 == 0 else d + p) for d in range(p)]
    return cd, xd


def defect(p, ds):
    cd, _ = parity_classes(p, ds)
    return sum(abs(v) for v in cd)


def kappa(p, x):
    M = (p - 1) // 2
    x %= p
    return -1 if ((x if x <= M else x - p) % 2) else 1


# --------------------------------------------------------------- checks --

def stage_A_B():
    bad_id, bad_nv, wins = [], [], []
    for p in (11, 13, 19):
        N0 = nonresidue(p)
        cases = [("full", full_group_reps(p))]
        r1, e = rung1_reps(p, N0)
        cases.append((f"rung1(e={e})", r1))
        for name, reps in cases:
            m = len(reps)
            for c in ((1, 1), (2, 3), (1, 0), (0, 1)):
                if c[0] % p == 0 and c[1] % p == 0:
                    continue
                ds = deltas(p, N0, c, reps)
                cd, xd = parity_classes(p, ds)
                # (ID) at every ODD k, exactly in Z[zeta_p]
                for k in range(1, 2 * p, 2):
                    lhs = [0] * p
                    for x in ds:
                        lhs = zadd(lhs, omega_pow_vec(p, k * x), p)
                    rhs = [0] * p
                    for d in range(p):
                        if cd[d]:
                            w = omega_pow_vec(p, k * xd[d])
                            rhs = zadd(rhs, [cd[d] * t for t in w], p)
                    if lhs != rhs:
                        bad_id.append((p, name, c, k))
                wins.append((p, name, c, m, sum(abs(v) for v in cd)))
        # B: non-vacuity at the full group with a_c b_c != 0
        reps = full_group_reps(p)
        m = len(reps)
        for c in ((1, 1), (2, 3)):
            D = defect(p, deltas(p, N0, c, reps))
            if not (2 * D < m):
                bad_nv.append((p, c, D, m))
    check("A: the grouping identity (ID) R_k = (1/m) sum_d c_d omega^{k x_d} "
          "holds for EVERY odd k, verified EXACTLY in Z[zeta_p] (integer "
          "vectors, no floats) -- hence (DEF) and (FLAT) by the triangle "
          "inequality", not bad_id,
          f"{len(wins)} (p, window, c) cases x p odd modes each; "
          f"bad={bad_id[:3]}")
    check("B: (DEF) is NON-VACUOUS at the full group: 2D < m, i.e. "
          "D/m < 1/2 (exact integers)", not bad_nv, f"bad={bad_nv}")


def stage_C_D():
    bad_c, bad_d, rows = [], [], []
    for p in (11, 13, 19, 23, 31, 41, 43, 53):
        M = (p - 1) // 2
        A = [sum(kappa(p, a) * kappa(p, (a + t) % p) for a in range(p))
             for t in range(p)]
        for t in range(0, M + 1):
            if A[t] != (-1) ** t * (p - 2 * t):
                bad_c.append((p, t, A[t]))
        for t in range(1, p):
            if A[t] != A[(-t) % p]:
                bad_c.append((p, t, "not even"))
        rows.append((p, A[0], A[1], A[M]))
        # D: the support is a half-system, at every admissible frequency
        N0 = nonresidue(p)
        if p <= 23:
            reps = full_group_reps(p)
            for ac in range(1, p):
                for bc in range(1, p):
                    cd, _ = parity_classes(p, deltas(p, N0, (ac, bc), reps))
                    supp = [d for d in range(p) if cd[d] != 0]
                    if len(supp) != M:
                        bad_d.append((p, (ac, bc), "size"))
                    elif any(((-d) % p) in set(supp) for d in supp):
                        bad_d.append((p, (ac, bc), "not a half-system"))
    check("C: A(t) = sum_a kappa(a)kappa(a+t) = (-1)^t (p - 2t) for "
          "0 <= t <= (p-1)/2, and A is even in t (8 primes)",
          not bad_c, f"(p, A(0), A(1), A(M)) = {rows}")
    check("D: the support of (c_d) at the full group is a HALF-SYSTEM of "
          "F_p^* (size (p-1)/2, no pair {d,-d} both present), at EVERY "
          "frequency with a_c b_c != 0", not bad_d,
          f"p = 11,13,19,23 exhaustive; bad={bad_d[:3]}")


def stage_E_F_G():
    bad_e, bad_f, bad_g, rows = [], [], [], []
    pilot_rows = []
    for p in (11, 13, 19, 23, 31, 41):
        N0 = nonresidue(p)
        reps = full_group_reps(p)
        m = len(reps)
        M = (p - 1) // 2
        target = M * M
        if m != p * (p - 1) // 2:
            bad_e.append((p, "m"))
        n_ok = n_exc_a = n_exc_b = n_other = 0
        mult_ok = mult_tot = 0
        for ac in range(p):
            for bc in range(p):
                if (ac, bc) == (0, 0):
                    continue
                ds = deltas(p, N0, (ac, bc), reps)
                D = defect(p, ds)
                if ac != 0 and bc != 0:
                    if D == target:
                        n_ok += 1
                    else:
                        bad_e.append((p, (ac, bc), D, target))
                    # G: multiplicity law (MEASURED)
                    if p <= 23:
                        cnt = [0] * (2 * p)
                        for x in ds:
                            cnt[x] += 1
                        mult_tot += 1
                        if sorted(v for v in cnt if v > 0) == list(range(1, p)):
                            mult_ok += 1
                else:
                    if D != m:
                        bad_f.append((p, (ac, bc), D, m))
                    if ac == 0:
                        n_exc_a += 1
                    elif bc == 0:
                        n_exc_b += 1
                    else:
                        n_other += 1
                if (ac, bc) in ((1, 1), (2, 3)):
                    pilot_rows.append((p, (ac, bc), D, target, m))
        if n_exc_a != p - 1 or n_exc_b != p - 1 or n_other != 0:
            bad_f.append((p, "exception count", n_exc_a, n_exc_b, n_other))
        rows.append((p, m, target, n_ok))
        if p <= 23:
            bad_g.append((p, mult_ok, mult_tot))
    check("E: THEOREM 2 -- D = ((p-1)/2)^2 EXACTLY at EVERY frequency of "
          "the full group with a_c != 0 and b_c != 0 (exhaustive sweep, "
          "p = 11,13,19,23,31,41)", not bad_e,
          f"(p, m, D, #frequencies) = {rows}")
    pilot_ok = all(D == tgt for (_, _, D, tgt, _) in pilot_rows)
    check("E2: the pilot's own A8 row reproduced -- m = p(p-1)/2 and "
          "D = ((p-1)/2)^2 at c = (1,1) and (2,3), p = 11..41 "
          "(f2_deployed_windows/verify.py:300-321)", pilot_ok,
          f"{len(pilot_rows)} (p,c) rows")
    check("F: THEOREM 3 -- the ONLY frequencies where D != ((p-1)/2)^2 are "
          "the two lines a_c = 0 and b_c = 0, exactly p-1 each, and there "
          "D = m (certificate vacuous)", not bad_f, f"bad={bad_f[:3]}")
    print("NOTE (MEASURED, not a claim of the node): multiplicity law "
          "[1..p-1] holds at (p, ok/total) = "
          + str([(p, f"{a}/{b}") for (p, a, b) in bad_g]))


def stage_H_I():
    bad_h, bad_i, rows, flipped = [], [], [], []
    for p in (13, 17, 29, 41):
        N0 = nonresidue(p)
        r1, e = rung1_reps(p, N0)
        m = len(r1)
        if m != (1 << (e - 1)):
            bad_h.append((p, "m", m))
        for ac in range(p):
            for bc in range(p):
                if (ac, bc) == (0, 0):
                    continue
                ds = deltas(p, N0, (ac, bc), r1)
                if any(x % 2 for x in ds):
                    bad_h.append((p, (ac, bc), "odd Delta at rung 1"))
                    continue
                if defect(p, ds) != m:
                    bad_h.append((p, (ac, bc), "D != m"))
                if sum(1 if x % 2 == 0 else -1 for x in ds) != m:
                    bad_h.append((p, (ac, bc), "R_p != 1"))
        rows.append((p, e, m))
    # I: global flip preserves D; partial flips need not
    for p in (11, 13, 19):
        N0 = nonresidue(p)
        reps = full_group_reps(p)
        ds = deltas(p, N0, (1, 1), reps)
        D0 = defect(p, ds)
        Dg = defect(p, [(-x) % (2 * p) for x in ds])
        if D0 != Dg:
            bad_i.append((p, "global flip changed D", D0, Dg))
        seed = 987654321
        changed = 0
        for _ in range(30):
            seed = (6364136223846793005 * seed + 1442695040888963407) % (1 << 64)
            sub = [(-x) % (2 * p) if ((seed >> (i % 60)) & 1) else x
                   for i, x in enumerate(ds)]
            if defect(p, sub) != D0:
                changed += 1
        flipped.append((p, D0, changed))
    check("H: Corollary 4 -- on rung-1 DEPLOYED windows every Delta is even, "
          "so D = m and (FLAT) is vacuous; the true value R_p = 1 "
          "(flat = 0) is attained, so the certificate is tight-but-empty "
          "there", not bad_h, f"(p, e, m) = {rows}")
    check("I: D is invariant under the GLOBAL orientation reversal (proved), "
          "and PARTIAL flips DO change it -- so D must be quoted with its "
          "labelling", not bad_i and all(ch > 0 for (_, _, ch) in flipped),
          f"(p, D, #partial-flips-that-changed-D of 30) = {flipped}")


def main():
    stage_A_B()
    stage_C_D()
    stage_E_F_G()
    stage_H_I()
    if FAILURES:
        print("FAILED CHECKS:", FAILURES)
        sys.exit(1)
    print("F2_PARITY_DEFECT_CERTIFICATE_ALL_PASS")


if __name__ == "__main__":
    main()
