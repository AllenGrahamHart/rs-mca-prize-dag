#!/usr/bin/env python3
"""Independent audit of the (PAR) parametrization node.

Second code path, deliberately different from verify.py:
  - (DET) and both syzygies (SYZ) are PROVED SYMBOLICALLY over
    Z[f,g,h,k,z] with a tiny multivariate polynomial engine (f,g,h,k as
    abstract commuting variables) -- a characteristic-free identity proof,
    not a sampled check;
  - the banked q = 97 witness is recertified with the coordinator's OWN
    elimination code (the round-38 certification path): Q_0,Q_1,Q_2 are
    derived from (f,g,h,k,L) by exact division per (PAR), the 36x32
    syndrome system is solved for (y_0,y_1), and nullity/generic rank/
    single-drop/infinity/deg<=1-kernel are certified from scratch.

Run: tools/ramguard tiny -- python3 \
  background/nodes/rate_half_l2_stratum_rational_parametrization/verify_audit.py
(RAMGUARD_TIMEOUT 60s)
"""

import json
from pathlib import Path

cert = json.loads(Path(__file__).with_name("certificate.json").read_text())

# ---------------- symbolic engine over Z[f,g,h,k,z]: dict monomial -> int
# monomial = (ef, eg, eh, ek, ez)
def mono_mul(a, b):
    return tuple(x + y for x, y in zip(a, b))


def pmul(P, Q):
    out = {}
    for ma, ca in P.items():
        for mb, cb in Q.items():
            m = mono_mul(ma, mb)
            out[m] = out.get(m, 0) + ca * cb
    return {m: c for m, c in out.items() if c}


def padd(*Ps):
    out = {}
    for P in Ps:
        for m, c in P.items():
            out[m] = out.get(m, 0) + c
    return {m: c for m, c in out.items() if c}


def pneg(P):
    return {m: -c for m, c in P.items()}


F = {(1, 0, 0, 0, 0): 1}
G = {(0, 1, 0, 0, 0): 1}
H = {(0, 0, 1, 0, 0): 1}
K = {(0, 0, 0, 1, 0): 1}
Z = {(0, 0, 0, 0, 1): 1}

A = padd(pmul(F, F), pneg(pmul(K, G)))          # f^2 - kg
Bt = padd(pmul(F, G), pmul(H, K))               # fg + hk
C = padd(pmul(G, G), pmul(H, F))                # g^2 + hf

# (DET): det([[f,k],[g,f]] + z[[g,f],[-h,g]]) = A + z*Bt + z^2*C
m11 = padd(F, pmul(Z, G))
m12 = padd(K, pmul(Z, F))
m21 = padd(G, pmul(Z, pneg(H)))
m22 = padd(F, pmul(Z, G))
det = padd(pmul(m11, m22), pneg(pmul(m12, m21)))
rhs = padd(A, pmul(Z, Bt), pmul(Z, pmul(Z, C)))
assert det == rhs, "(DET) fails symbolically"

# (SYZ): f*C = g*Bt + h*A   and   f*Bt = g*A + k*C
assert pmul(F, C) == padd(pmul(G, Bt), pmul(H, A)), "(SYZ) 1 fails"
assert pmul(F, Bt) == padd(pmul(G, A), pmul(K, C)), "(SYZ) 2 fails"

# ---------------- witness recertification (coordinator code path)
q = cert["q"]


def pm(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % q
    return out


def psub(a, b):
    n = max(len(a), len(b))
    return [((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % q
            for i in range(n)]


def pdiv_linear(a, L):
    # divide by L = [c0, c1] (c1 != 0), assert exact
    a = a[:]
    c0, c1 = L[0] % q, L[1] % q
    inv1 = pow(c1, q - 2, q)
    quo = [0] * (len(a) - 1)
    for i in range(len(a) - 1, 0, -1):
        t = a[i] * inv1 % q
        quo[i - 1] = t
        a[i] = 0
        a[i - 1] = (a[i - 1] - t * c0) % q
    assert a[0] % q == 0, "division by L not exact"
    return [x % q for x in quo]


f, g, h, k, L = cert["f"], cert["g"], cert["h"], cert["k"], cert["L"]
Aq = psub(pm(f, f), pm(k, g))
Btq = [(x + y) % q for x, y in
       zip(pm(f, g) + [0] * 9, pm(h, k) + [0] * 9)][: len(pm(f, g))]
Cq = [(x + y) % q for x, y in
      zip(pm(g, g) + [0] * 9, pm(h, f) + [0] * 9)][: len(pm(g, g))]
Q0 = pdiv_linear(Aq, L)
Q1 = pdiv_linear(Btq, L)
Q2 = pdiv_linear(Cq, L)
for Q in (Q0, Q1, Q2):
    assert len(Q) == 8, "deg Q != 7 slot"

# roots
for x in cert["S0"]:
    assert sum(c * pow(x, i, q) for i, c in enumerate(Q0)) % q == 0
for x in cert["S2"]:
    assert sum(c * pow(x, i, q) for i, c in enumerate(Q2)) % q == 0
assert not set(cert["S0"]) & set(cert["S2"])
assert all(pow(x, 32, q) == 1 for x in cert["S0"] + cert["S2"])

# the 36x32 syndrome system and the pencil certification


def rank_and_kernel(rows, mod):
    M = [r[:] for r in rows]
    rr, cols = len(M), len(M[0])
    piv = []
    r_ = 0
    for c in range(cols):
        p = None
        for i in range(r_, rr):
            if M[i][c] % mod:
                p = i
                break
        if p is None:
            continue
        M[r_], M[p] = M[p], M[r_]
        inv = pow(M[r_][c], mod - 2, mod)
        M[r_] = [x * inv % mod for x in M[r_]]
        for i in range(rr):
            if i != r_ and M[i][c] % mod:
                fct = M[i][c]
                M[i] = [(M[i][j] - fct * M[r_][j]) % mod for j in range(cols)]
        piv.append(c)
        r_ += 1
    free = [c for c in range(cols) if c not in piv]
    kernel = []
    for fc in free:
        v = [0] * cols
        v[fc] = 1
        for ri, pc in enumerate(piv):
            v[pc] = (-M[ri][fc]) % mod
        kernel.append(v)
    return r_, kernel


rows = []
for (a_, b_) in ((Q0, None), (Q1, Q0), (Q2, Q1), (None, Q2)):
    for i in range(9):
        row = [0] * 32
        if a_ is not None:
            for j in range(8):
                row[i + j] = (row[i + j] + a_[j]) % q
        if b_ is not None:
            for j in range(8):
                row[16 + i + j] = (row[16 + i + j] + b_[j]) % q
        rows.append(row)
r36, ker = rank_and_kernel(rows, q)
assert 32 - r36 == cert["nullity_36x32"] == 1
y = ker[0]
H0 = [[y[i + j] % q for j in range(8)] for i in range(9)]
H1 = [[y[16 + i + j] % q for j in range(8)] for i in range(9)]
drops = []
mx = 0
for z in range(q):
    Mz = [[(H0[i][j] + z * H1[i][j]) % q for j in range(8)] for i in range(9)]
    rz, _ = rank_and_kernel(Mz, q)
    mx = max(mx, rz)
    if rz < 7:
        drops.append((z, rz))
assert mx == cert["generic_rank"] == 7
assert drops == [(cert["drop_z"], cert["drop_rank"])] == [(89, 6)]
rinf, _ = rank_and_kernel(H1, q)
assert rinf == 7, "rank drop at infinity"
# no kernel vector of parameter degree <= 1  =>  e = 2 exactly
rows2 = []
for (A_, B_) in ((H0, None), (H1, H0), (None, H1)):
    for i in range(9):
        row = [0] * 16
        if A_ is not None:
            for j in range(8):
                row[j] = (row[j] + A_[i][j]) % q
        if B_ is not None:
            for j in range(8):
                row[8 + j] = (row[8 + j] + B_[i][j]) % q
        rows2.append(row)
r27, _ = rank_and_kernel(rows2, q)
assert 16 - r27 == 0, "a deg<=1 kernel exists: e < 2"

print(
    "RATE_HALF_L2_STRATUM_RATIONAL_PARAMETRIZATION_AUDIT_PASS "
    "(DET)+(SYZ) proved symbolically over Z; witness q=97 recertified "
    "e=m=2 (nullity 1, generic rank 7, single drop z=89->6, inf full, "
    "no deg<=1 kernel) via exact division per (PAR)"
)
