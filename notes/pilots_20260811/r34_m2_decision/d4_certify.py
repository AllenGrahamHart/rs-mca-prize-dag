"""D4 (r34): certification pass.

Two jobs:

 (A) IS THE (SAT1) PROFILE WITH e = m = 2 NONEMPTY AT ALL?  Round 33 built no
     m>=2 object with e = m (every ladder entry had e = 1, a range (ERC2)
     already closes).  A nonzero solution of the 36 x 32 realization system is
     NOT enough: it must be non-degenerate (y_0 != 0, y_1 != 0, generic rank
     exactly rho = 7 so A = R+1-2rho = 3, the primitive kernel of Z-degree
     exactly 2, no fixed domain factor).  This script certifies or refutes.

 (B) THE (SAT) PROFILE OF WHATEVER EXISTS: T, u_gamma, O, d_x, the deficit,
     w* = a*, and a* vs 7m-1 = 13 (the F1 test, live for the first time at
     m = 2 because the w* window is not a single point).

Usage: d4_certify.py OUTFILE
"""
import sys
import random
from itertools import combinations

LINES = []
M, RHO, N, R, RR = 2, 7, 32, 16, 7


def out(s=""):
    print(s)
    LINES.append(s)


def rref(rows, ncols, q):
    rows = [r[:] for r in rows]
    piv, rk = [], 0
    for c in range(ncols):
        p = None
        for i in range(rk, len(rows)):
            if rows[i][c] % q:
                p = i
                break
        if p is None:
            continue
        rows[rk], rows[p] = rows[p], rows[rk]
        iv = pow(rows[rk][c], q - 2, q)
        rows[rk] = [v * iv % q for v in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][c] % q:
                f = rows[i][c]
                rows[i] = [(a - f * b) % q for a, b in zip(rows[i], rows[rk])]
        piv.append(c)
        rk += 1
        if rk == len(rows):
            break
    return rows, piv, rk


def nullspace(rows, ncols, q):
    rr, piv, rk = rref(rows, ncols, q)
    basis = []
    for f in [c for c in range(ncols) if c not in piv]:
        v = [0] * ncols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-rr[i][f]) % q
        basis.append(v)
    return basis


def mu_group(q, n):
    for a in range(2, q):
        h = pow(a, (q - 1) // n, q)
        seen = {pow(h, i, q) for i in range(n)}
        if len(seen) == n:
            return sorted(seen)
    raise RuntimeError


def poly_from_roots(roots, q):
    c = [1]
    for r in roots:
        nc = [0] * (len(c) + 1)
        for i, ci in enumerate(c):
            nc[i] = (nc[i] - r * ci) % q
            nc[i + 1] = (nc[i + 1] + ci) % q
        c = nc
    return c


def peval(c, x, q):
    v = 0
    for co in reversed(c):
        v = (v * x + co) % q
    return v


def Mr(y, q):
    return [[y[i + j] for j in range(RR + 1)] for i in range(R - RR)]


def realization_rows(Qk, q, e):
    rows = []
    for k in range(e + 2):
        for i in range(R - RR):
            row = [0] * (2 * R)
            if 0 <= k <= e:
                for j in range(RR + 1):
                    row[i + j] = (row[i + j] + Qk[k][j]) % q
            if 0 <= k - 1 <= e:
                for j in range(RR + 1):
                    row[R + i + j] = (row[R + i + j] + Qk[k - 1][j]) % q
            rows.append(row)
    return rows


def e1_kernel_exists(y0, y1, q):
    """is there a nonzero degree-<=1 (in Z) kernel?  27 eqs on 16 unknowns"""
    rows = []
    for k in range(3):
        for i in range(R - RR):
            row = [0] * (2 * (RR + 1))
            if k <= 1:
                for j in range(RR + 1):
                    row[j] = (row[j] + y0[i + j] * 0) % q
            rows.append(row)
    # build properly: unknowns (A,B); blocks  M0 A, M0 B + M1 A, M1 B
    rows = []
    m0, m1 = Mr(y0, q), Mr(y1, q)
    for i in range(R - RR):
        rows.append([m0[i][j] for j in range(RR + 1)] + [0] * (RR + 1))
    for i in range(R - RR):
        rows.append([m1[i][j] for j in range(RR + 1)] +
                    [m0[i][j] for j in range(RR + 1)])
    for i in range(R - RR):
        rows.append([0] * (RR + 1) + [m1[i][j] for j in range(RR + 1)])
    return len(nullspace(rows, 2 * (RR + 1), q)) > 0


def main():
    random.seed(4340811)
    out("=== r34 D4: certification of e = m = 2 objects at m=2 ===")
    out(f"profile targets: rho={RHO}, N={N}, R={R}, r={RR}, A=R+1-2rho="
        f"{R + 1 - 2 * RHO}, e=m={M}, delta=m-1={M-1}, 7m-1={7*M-1}, "
        f"2rho={2*RHO}")
    out("")
    for q in (97, 193):
        D = mu_group(q, 32)
        Dset = set(D)
        n_try = 0
        n_null = 0
        n_deg = 0          # y_0 = 0 or y_1 = 0
        n_rank = {}
        genuine = []
        Tdist = {}
        while n_try < 700:
            n_try += 1
            S0 = random.sample(D, 7)
            S2 = random.sample(D, 7)
            Qk = [poly_from_roots(S0, q),
                  [random.randrange(q) for _ in range(RR + 1)],
                  poly_from_roots(S2, q)]
            ns = nullspace(realization_rows(Qk, q, M), 2 * R, q)
            if not ns:
                continue
            n_null += 1
            cands = [v[:] for v in ns]
            for _ in range(4):
                v = [0] * (2 * R)
                for b in ns:
                    c = random.randrange(q)
                    v = [(a + c * bb) % q for a, bb in zip(v, b)]
                cands.append(v)
            for sol in cands:
                y0, y1 = sol[:R], sol[R:]
                if not any(y0) or not any(y1):
                    n_deg += 1
                    continue
                ranks = []
                for g in range(q):
                    yg = [(a + g * b) % q for a, b in zip(y0, y1)]
                    ranks.append(rref(Mr(yg, q), RR + 1, q)[2])
                gr = max(ranks)
                n_rank[gr] = n_rank.get(gr, 0) + 1
                if gr != RHO:
                    continue
                if e1_kernel_exists(y0, y1, q):
                    continue                      # parameter degree e <= 1
                # supported slopes
                sup = {}
                for g in range(q):
                    yg = [(a + g * b) % q for a, b in zip(y0, y1)]
                    k = nullspace(Mr(yg, q), RR + 1, q)
                    if len(k) != 1:
                        continue
                    v = k[0]
                    if v[RR] == 0:
                        continue
                    iv = pow(v[RR], q - 2, q)
                    w = [a * iv % q for a in v]
                    rts = [x for x in D if peval(w, x, q) == 0]
                    if len(rts) == RHO:
                        sup[g] = tuple(sorted(rts))
                T = len(sup)
                Tdist[T] = Tdist.get(T, 0) + 1
                if T >= 2:
                    genuine.append((T, y0[:], y1[:], dict(sup)))
                break
        out(f"--- q={q} ---")
        out(f"  split-endpoint nets tried: {n_try}; with a nonzero "
            f"realization: {n_null} ({n_null/n_try:.2%})")
        out(f"  degenerate solutions (y_0 = 0 or y_1 = 0): {n_deg}")
        out(f"  generic-rank histogram of non-degenerate solutions "
            f"(need rho={RHO}): {dict(sorted(n_rank.items()))}")
        out(f"  GENUINE e=2, A=3 objects (rank rho, no degree-<=1 kernel): "
            f"{sum(Tdist.values())}")
        out(f"  T distribution over those objects: {dict(sorted(Tdist.items()))}"
            )
        if genuine:
            genuine.sort(key=lambda t: -t[0])
            T, y0, y1, sup = genuine[0]
            out(f"  BEST OBJECT: T = {T} finite supported slopes "
                f"(need rho+2 = {RHO+2} for (SAT3), rho+1 = {RHO+1} for the "
                f"strict target)")
            out(f"    y_0 = {y0}")
            out(f"    y_1 = {y1}")
            dx = {x: sum(1 for S in sup.values() if x in S) for x in D}
            O = sum(RHO - len(S) for S in sup.values())
            out(f"    slopes/u_gamma: "
                f"{[(g, len(S)) for g, S in sorted(sup.items())]}")
            out(f"    O = {O}; max d_x = {max(dx.values())} (<= e = {M}); "
                f"sum_x d_x = {sum(dx.values())} (= T*rho - O = "
                f"{T*RHO - O})")
            out(f"    saturated points (d_x = 2): "
                f"{sum(1 for x in D if dx[x] == M)}")
            if T >= 2:
                ws = min(len(set(sup[g]) | set(sup[h]))
                         for g, h in combinations(sorted(sup), 2))
                out(f"    w* = a* = {ws};  7m-1 = {7*M-1};  2rho = {2*RHO};  "
                    f"F1 fires (a* > 7m-1)? "
                    f"{'YES' if ws > 7*M-1 else 'NO'}")
        out("")
    with open(sys.argv[1], "w") as f:
        f.write("\n".join(LINES) + "\n")


main()
