#!/usr/bin/env python3
"""Independent audit of the R-L2 witness theorem node.

This is the COORDINATOR'S from-scratch verifier of the round-35 q = 97
witness (written at round 35 with no pilot code, banked in the session
scratchpad, cleaned and pinned here). Second code path relative to
verify.py: its own polynomial/gcd/rank routines, the E1/E2
B-parametrization identities checked as polynomial equations, the pencil
blocks checked entrywise, and the 36x32 nullity + deg<=1-kernel
certification assembled independently. All witness data comes from
certificate.json.

Run: tools/ramguard tiny -- python3 \
  background/nodes/rate_half_l2_stratum_nonempty_at_m_two/verify_audit.py
(RAMGUARD_TIMEOUT 60s)
"""

import json
from pathlib import Path

cert = json.loads(Path(__file__).with_name("certificate.json").read_text())
q = cert["q"]
Q0, Q1, Q2 = cert["Q0"], cert["Q1"], cert["Q2"]
y0, y1 = cert["y0"], cert["y1"]
f, g, h, k = cert["f"], cert["g"], cert["h"], cert["k"]


def pmul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % q
    return c


def psub(a, b):
    n = max(len(a), len(b))
    return [((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % q
            for i in range(n)]


def degp(p):
    d = -1
    for i, x in enumerate(p):
        if x % q:
            d = i
    return d


def pgcd(a, b):
    def pmodp(a_, b_):
        a_ = [x % q for x in a_]
        db = degp(b_)
        inv = pow(b_[db], q - 2, q)
        while degp(a_) >= db:
            da = degp(a_)
            fac = a_[da] * inv % q
            for i in range(db + 1):
                a_[da - db + i] = (a_[da - db + i] - fac * b_[i]) % q
        return a_
    a, b = [x % q for x in a], [x % q for x in b]
    while degp(b) >= 0:
        a, b = b, pmodp(a, b)
    return a


def rank(M):
    M = [row[:] for row in M]
    r = 0
    rows, cols = len(M), len(M[0])
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] % q:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], q - 2, q)
        M[r] = [x * inv % q for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] % q:
                fac = M[i][c]
                M[i] = [(M[i][j] - fac * M[r][j]) % q for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


# E1/E2: the round-35 B-parametrization relations
E1 = psub(psub(pmul(Q2, f), pmul(Q1, g)), pmul(Q0, h))
E2 = psub(psub(pmul(Q1, f), pmul(Q0, g)), pmul(Q2, k))
assert not any(x % q for x in E1), "E1 fails"
assert not any(x % q for x in E2), "E2 fails"

# degrees and s = 0
assert degp(Q0) == degp(Q1) == degp(Q2) == 7
assert degp(pgcd(pgcd(Q0, Q1), Q2)) == 0

# the pencil blocks M(Z) Q_Z = 0, entrywise
hank = lambda y: [[y[a + b] % q for b in range(8)] for a in range(9)]
M0, M1 = hank(y0), hank(y1)
mv = lambda M, v: [sum(M[i][j] * v[j] for j in range(8)) % q for i in range(9)]
B0 = mv(M0, Q0)
B1 = [(x + y) % q for x, y in zip(mv(M0, Q1), mv(M1, Q0))]
B2 = [(x + y) % q for x, y in zip(mv(M0, Q2), mv(M1, Q1))]
B3 = mv(M1, Q2)
for blk in (B0, B1, B2, B3):
    assert all(x % q == 0 for x in blk), "pencil block nonzero"

# generic rank, single drop, infinity
drops, maxr = [], 0
for z in range(q):
    Mz = [[(M0[i][j] + z * M1[i][j]) % q for j in range(8)] for i in range(9)]
    rz = rank(Mz)
    maxr = max(maxr, rz)
    if rz < 7:
        drops.append((z, rz))
assert maxr == cert["generic_rank"] == 7
assert drops == [(cert["drop_z"], cert["drop_rank"])] == [(10, 6)]
assert rank(M1) == 7, "drop at infinity"

# nullity of the 36x32 system in (y0, y1)
rows = []
for coeffs in ((Q0, None), (Q1, Q0), (Q2, Q1), (None, Q2)):
    a_, b_ = coeffs
    for a in range(9):
        row = [0] * 32
        for b in range(8):
            if a_ is not None:
                row[a + b] = (row[a + b] + a_[b]) % q
            if b_ is not None:
                row[16 + a + b] = (row[16 + a + b] + b_[b]) % q
        rows.append(row)
assert 32 - rank(rows) == cert["nullity_36x32"] == 1

# e = 2 exactly: no kernel vector of parameter degree <= 1
rows2 = []
for A_, B_ in ((M0, None), (M1, M0), (None, M1)):
    for a in range(9):
        row = [0] * 16
        for b in range(8):
            if A_ is not None:
                row[b] = (row[b] + A_[a][b]) % q
            if B_ is not None:
                row[8 + b] = (row[8 + b] + B_[a][b]) % q
        rows2.append(row)
assert 16 - rank(rows2) == 0, "deg<=1 kernel exists: e < 2"

print(
    "RATE_HALF_L2_STRATUM_NONEMPTY_AT_M_TWO_AUDIT_PASS "
    "q=97 witness: E1/E2 hold, degs (7,7,7), s=0, blocks zero, generic "
    "rank 7, single drop z=10->6, inf full, nullity(36x32)=1, "
    "no deg<=1 kernel => e=m=2 exactly"
)
