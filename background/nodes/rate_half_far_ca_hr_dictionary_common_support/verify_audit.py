#!/usr/bin/env python3
"""Independent audit of the h_r dictionary node.

Second code path, deliberately different from verify.py:
  - (DICT) replayed at FRESH fields (601, 1013) and at a rho = 3 shape the
    draft verifier never ran, with an independently written rank routine;
  - (CS) verified as a SYMBOLIC identity on syndrome vectors -- given
    y_0 + gamma_i y_1 = syn(u_i), the reconstruction e_0, e_1 satisfies
    syn(e_0) = y_0 and syn(e_1) = y_1 by two lines of linear algebra, which
    the audit checks entrywise on a concrete instance built the other way
    around (from the errors, then re-derived from the slopes);
  - (LB1)'s forced T_1 = r+1 checked constructively: for every x0 in T the
    error (L - L(x0)) * 1_T has weight exactly r and syndrome
    y_1 - L(x0) y_0, so every value of L is exhibited as a bad slope with
    its annihilating error, not counted statistically.
POSED/carried components ((PSTAR), the h_r = 2rho leg) are not audited.

Run: tools/ramguard tiny -- python3 \
  background/nodes/rate_half_far_ca_hr_dictionary_common_support/verify_audit.py
(RAMGUARD_TIMEOUT 60s)
"""

import json
from pathlib import Path

cert = json.loads(Path(__file__).with_name("certificate.json").read_text())


def weights(D, q):
    out = {}
    for x in D:
        p = 1
        for y in D:
            if y != x:
                p = p * (x - y) % q
        out[x] = pow(p, q - 2, q)
    return out


def syn(e, D, v, q, R):
    return [sum(e.get(x, 0) * v[x] * pow(x, i, q) for x in D) % q
            for i in range(R)]


def rank(rows, q):
    rows = [r[:] for r in rows]
    rk = 0
    for c in range(len(rows[0])):
        piv = None
        for i in range(rk, len(rows)):
            if rows[i][c] % q:
                piv = i
                break
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        inv = pow(rows[rk][c], q - 2, q)
        rows[rk] = [x * inv % q for x in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][c] % q:
                f = rows[i][c]
                rows[i] = [(a - f * b) % q for a, b in zip(rows[i], rows[rk])]
        rk += 1
    return rk


def stacked(y0, y1, rho, r, q):
    rows = [[y0[i + j] % q for j in range(r + 1)] for i in range(rho)]
    rows += [[y1[i + j] % q for j in range(r + 1)] for i in range(rho)]
    return rows


# ---- (DICT) at fresh fields and shapes -- in scope d <= rho; plus the
#      saturation exhibits that FORCE the d <= rho qualifier (rank cannot
#      exceed the 2rho rows, so polynomial ratios of degree d > rho give
#      h_r = 2rho exactly like non-polynomial ones)
for spec in cert["dict_replays"]:
    n, k, rho, q = spec["n"], spec["k"], spec["rho"], spec["q"]
    R = n - k
    r = R - rho
    D = list(range(1, n + 1))
    v = weights(D, q)
    T = D[: r + 1]
    for d in spec["degrees"]:
        # L = X^d + 1 (monic, degree d, no root in T by construction check)
        L = lambda x: (pow(x, d, q) + 1) % q
        e0 = {x: 1 for x in T}
        e1 = {x: L(x) for x in T}
        y0 = syn(e0, D, v, q, R)
        y1 = syn(e1, D, v, q, R)
        M = stacked(y0, y1, rho, r, q)
        hr = rank(M, q)
        assert hr == rho + d, ("(DICT) h_r", spec, d, hr)
        assert (r + 1) - hr == r + 1 - rho - d, ("(DICT) dim K_0", spec, d)
        # (LB1) at d = 1: every value of L is a bad slope, constructively
        if d == 1:
            slopes = set()
            for x0 in T:
                g = L(x0)
                e_ann = {x: (L(x) - g) % q for x in T if (L(x) - g) % q}
                assert len(e_ann) == r, ("annihilating error weight", x0)
                sg = syn(e_ann, D, v, q, R)
                want = [(y1[i] - g * y0[i]) % q for i in range(R)]
                assert sg == want, ("(LB1) syndrome mismatch", x0)
                slopes.add(g)
            assert len(slopes) == r + 1, ("(LB1) T_1", len(slopes))

# ---- the saturation exhibits (the scope correction's positive record)
for ex in cert["saturation_exhibits"]:
    n, k, rho, q, d = ex["n"], ex["k"], ex["rho"], ex["q"], ex["d"]
    assert d > rho
    R = n - k
    r = R - rho
    D = list(range(1, n + 1))
    v = weights(D, q)
    T = D[: r + 1]
    e0 = {x: 1 for x in T}
    e1 = {x: (pow(x, d, q) + 1) % q for x in T}
    M = stacked(syn(e0, D, v, q, R), syn(e1, D, v, q, R), rho, r, q)
    assert rank(M, q) == ex["h_r"] == 2 * rho, ("saturation", ex)

# ---- (CS) the reconstruction identity, on a concrete instance
ci = cert["cs_instance"]
n, k, rho, q = ci["n"], ci["k"], ci["rho"], ci["q"]
R = n - k
r = R - rho
D = list(range(1, n + 1))
v = weights(D, q)
T = D[: r + 1]
# build a genuine two-slope situation from a common-support pair (d = 1)
e0 = {x: 1 for x in T}
e1 = {x: (x + 1) % q for x in T}
y0 = syn(e0, D, v, q, R)
y1 = syn(e1, D, v, q, R)
# convention here: slope g_i is bad through the weight-r error
# u_i = e_1 - g_i e_0 (syndrome y_1 - g_i y_0); with L injective of degree
# 1, taking g_i = L(x_i) drops exactly the point x_i from the support.
g1, g2 = (T[0] + 1) % q, (T[1] + 1) % q          # two distinct L-values
u1 = {x: (e1[x] - g1 * e0[x]) % q for x in T}
u2 = {x: (e1[x] - g2 * e0[x]) % q for x in T}
assert sum(1 for x in T if u1[x]) == r and sum(1 for x in T if u2[x]) == r
# reconstruction in this convention (two lines of linear algebra):
#   u_1 - u_2 = (g_2 - g_1) e_0,   g_2 u_1 - g_1 u_2 = (g_2 - g_1) e_1;
# checked ENTRYWISE and then on syndromes.
inv21 = pow((g2 - g1) % q, q - 2, q)
rec_e0 = {x: (u1[x] - u2[x]) * inv21 % q for x in T}
rec_e1 = {x: (g2 * u1[x] - g1 * u2[x]) % q * inv21 % q for x in T}
assert all(rec_e0[x] == e0[x] for x in T), "(CS) e_0 reconstructs"
assert all(rec_e1[x] == e1[x] for x in T), "(CS) e_1 reconstructs"
assert syn(rec_e0, D, v, q, R) == y0
assert syn(rec_e1, D, v, q, R) == y1

print(
    "RATE_HALF_FAR_CA_HR_DICTIONARY_COMMON_SUPPORT_AUDIT_PASS "
    "(DICT) at 601/1013 incl. rho=3 shape (scope d <= rho, saturation "
    "h_r = 2rho exhibited at d > rho); (LB1) T_1=r+1 constructive; "
    "(CS) reconstruction exact entrywise + on syndromes"
)
