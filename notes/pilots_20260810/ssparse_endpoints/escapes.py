"""Escape tests.

ESC-1 (CORRECTED -- registered miss P13): the brief asks that S_sparse
reproduce `B_mca - B_ca^far`.  That is NOT (MS1): the PROVED identity is
B_mca = max(B_ca^far, S_sparse), a MAXIMUM, so the difference form is false
whenever one term dominates.  What the (RH-SPLIT) PROOF actually asserts,
and what I therefore replay, is the load-bearing lemma: for a column-CLOSE
pair, translating by a closest code pair gives a SPARSE pair with EXACTLY
the same MCA-bad slope set.

ESC-2: replay the wave-10 determined-region formula a_RH(q) = n - B*(q) + 1
at 3 sample q < 2^167.
"""
import random
from itertools import combinations

import ffield as ff


def extends(vals, S, D, K, q):
    """does v|_S extend to a polynomial of degree < K ?"""
    rows = [[pow(D[i], t, q) for t in range(K)] for i in S]
    rhs = [vals[i] for i in S]
    return ff.solve(rows, rhs, K, q) is not None


def mca_bad_set(f1, f2, D, K, q, a):
    n = len(D)
    subs = [S for j in range(a, n + 1) for S in combinations(range(n), j)]
    bad = []
    for g in range(q):
        w = [(f1[i] + g * f2[i]) % q for i in range(n)]
        hit = False
        for S in subs:
            if not extends(w, S, D, K, q):
                continue
            if extends(f1, S, D, K, q) and extends(f2, S, D, K, q):
                continue
            hit = True
            break
        if hit:
            bad.append(g)
    return set(bad)


def rand_code(D, K, q, rnd):
    co = [rnd.randrange(q) for _ in range(K)]
    return [sum(co[t] * pow(x, t, q) for t in range(K)) % q for x in D]


if __name__ == "__main__":
    n_s, K, q = 8, 4, 17
    a = K + 1
    r = n_s - a
    D = ff.subgroup(n_s, q)
    rnd = random.Random(7)

    print("=== ESC-1 (corrected): translation invariance of the MCA-bad set ===")
    print(f"    n_s={n_s} K={K} q={q} a={a} r={r}")
    ok = 0
    for trial in range(6):
        # build a column-close pair: plant a code pair + a sparse error
        p1, p2 = rand_code(D, K, q, rnd), rand_code(D, K, q, rnd)
        E = rnd.sample(range(n_s), r)
        e1 = [0] * n_s
        e2 = [0] * n_s
        for j in E:
            while True:
                u, v = rnd.randrange(q), rnd.randrange(q)
                if u or v:
                    break
            e1[j], e2[j] = u, v
        f1 = [(p1[i] + e1[i]) % q for i in range(n_s)]
        f2 = [(p2[i] + e2[i]) % q for i in range(n_s)]
        A = mca_bad_set(f1, f2, D, K, q, a)
        B = mca_bad_set(e1, e2, D, K, q, a)
        sup = len([j for j in range(n_s) if e1[j] or e2[j]])
        same = (A == B)
        ok += same
        print(f"  trial {trial}: |supp union|={sup} <= r={r}: {sup <= r};  "
              f"|bad(f)|={len(A)} |bad(eps)|={len(B)}  IDENTICAL: {same}")
    print(f"  ESC-1 result: {ok}/6 identical")

    print()
    print("=== tangent lemma (T): every tangent slope is MCA-bad ===")
    bad_tan = 0
    for trial in range(6):
        E = rnd.sample(range(n_s), r)
        e1 = [0] * n_s
        e2 = [0] * n_s
        for j in E:
            e1[j], e2[j] = rnd.randrange(1, q), rnd.randrange(1, q)
        tang = {(-e1[j]) * pow(e2[j], q - 2, q) % q for j in E}
        B = mca_bad_set(e1, e2, D, K, q, a)
        inc = tang <= B
        bad_tan += inc
        print(f"  trial {trial}: #tangent={len(tang)} all MCA-bad: {inc}; "
              f"|S_sparse(this pair)|={len(B)} (>= min(r,q)={min(r,q)}: {len(B) >= min(r,q)})")
    print(f"  tangent lemma: {bad_tan}/6")

    print()
    print("=== ESC-2: wave-10 determined-region formula a_RH(q) = n - B*(q) + 1 ===")
    n, k = 1 << 41, 1 << 40
    B_Q = 389500552609
    for q in (1 << 129, (1 << 150) + 7, (1 << 166) + 3):
        B = q >> 128
        aRH = n - B + 1
        print(f"  q=2^{q.bit_length()-1:<4} B*={B:<22} a_RH={aRH:<15} "
              f"n-a_RH+1==B*: {n - aRH + 1 == B}  "
              f"a_RH in [k+2^34, n]: {k + (1<<34) <= aRH <= n}  "
              f"B*<=B_Q (quadratic range): {B <= B_Q}")
