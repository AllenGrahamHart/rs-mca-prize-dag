#!/usr/bin/env python3
"""Independent audit of the negation-closure excess fence.

Second code path, deliberately different from verify.py:
  - the covering law (CNT) is checked by ENUMERATION (itertools filter),
    never by math.comb;
  - the weights v_x are computed as 1/P'(x) with P = prod(X - y) built as a
    polynomial and formally differentiated, not as pairwise products;
  - the pencil conditions are evaluated DIRECTLY as functionals
    F_i = sum_x e(x) v_x x^i sigma(x) with sigma evaluated pointwise from
    its roots -- no syndrome vector and no Hankel matrix anywhere;
  - the rho = 2 cells are replayed at FRESH fields (1009, 2003), which the
    field-independence claim licenses; the H3 distinct-slope sub-count 329
    and the H4 zero-count are re-checked at the original field 65537: the
    former because birthday collisions contaminate slope counts at small q,
    the latter because the rho >= 3 kill is GENERIC in q, not
    field-uniform -- this audit FOUND the accidental covering solution
    A = {6,9,11,12,13} at q = 1009 (certificate.json
    generic_qualifier_exhibit), confirming the ~165/q accident rate;
  - the razor kill uses the ceil expression ((rho-1)//M)+1 and finds the
    minimal M by doubling, not by scanning a precomputed list.

Run: tools/ramguard tiny -- python3 \
  background/nodes/rate_half_far_ca_negation_closure_excess_fence/verify_audit.py
(RAMGUARD_TIMEOUT 60s)
"""

import json
from itertools import combinations
from pathlib import Path

cert = json.loads(Path(__file__).with_name("certificate.json").read_text())
CELLS = {c["tag"]: c for c in cert["cells"]}


def shape(cell):
    n, k, rho = cell["n"], cell["k"], cell["rho"]
    R = n - k
    r = R - rho
    m = n // 2
    off = m - (r + 1)
    return n, k, rho, R, r, m, off


# ---- (CNT) by pure enumeration, all six cells
for tag, cell in CELLS.items():
    n, k, rho, R, r, m, off = shape(cell)
    missed = set(range(r + 2, m + 1))
    assert len(missed) == off, tag
    count = sum(
        1 for A in combinations(range(1, m + 1), r // 2) if missed <= set(A)
    )
    assert count == cell["covering"], (tag, count, cell["covering"])


# ---- direct functional replays
def poly_mul(p, q_, mod):
    out = [0] * (len(p) + len(q_) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q_):
                out[i + j] = (out[i + j] + a * b) % mod
    return out


def replay(cell, q):
    n, k, rho, R, r, m, off = shape(cell)
    D = [i % q for i in range(1, m + 1)] + [(-i) % q for i in range(1, m + 1)]
    assert len(set(D)) == n, "domain degenerate at q=%d" % q
    # v_x = 1/P'(x), P = prod (X - y)
    P = [1]
    for y in D:
        P = poly_mul(P, [(-y) % q, 1], q)
    dP = [(i * c) % q for i, c in enumerate(P)][1:]
    ev = lambda p, x: sum(c * pow(x, i, q) for i, c in enumerate(p)) % q
    v = {x: pow(ev(dP, x), q - 2, q) for x in D}
    T = [i % q for i in range(1, r + 2)]
    missed = list(range(r + 2, m + 1))
    weights0 = {x: v[x] % q for x in T}
    weights1 = {x: (x * x % q) * v[x] % q for x in T}

    def functional(weights, i, roots):
        tot = 0
        for x, w in weights.items():
            sig = 1
            for s in roots:
                sig = sig * (x - s) % q
        # sigma has roots A u (-A); pointwise product above covers them all
            tot = (tot + w * pow(x, i, q) * sig) % q
        return tot

    covering = bad = 0
    slopes = set()
    for A in combinations(range(1, m + 1), r // 2):
        roots = [i % q for i in A] + [(-i) % q for i in A]
        F0 = [functional(weights0, i, roots) for i in range(rho)]
        F1 = [functional(weights1, i, roots) for i in range(rho)]
        if set(missed) <= set(A):
            covering += 1
            assert not any(F0[i] or F1[i] for i in range(1, rho, 2)), (
                "odd functional survives on covering locator", cell["tag"], q)
        if all(x == 0 for x in F1):
            continue
        j0 = next(i for i in range(rho) if F1[i])
        g = (-F0[j0]) * pow(F1[j0], q - 2, q) % q
        if all((F0[i] + g * F1[i]) % q == 0 for i in range(rho)):
            bad += 1
            slopes.add(g)
    return covering, bad, len(slopes)


for spec in cert["audit_replays"]:
    cell = CELLS[spec["tag"]]
    covering, bad, nslopes = replay(cell, spec["q"])
    assert covering == cell["covering"], (spec, covering)
    assert bad == cell["bad"], (spec, bad)
    if spec["q"] == 65537:
        assert nslopes == cell["distinct_slopes"], (spec, nslopes)

# ---- the razor kill, ceil-free
rz = cert["razor"]
rho = rz["rho"]
assert rho == 2 ** 34
assert ((rho - 1) // 2) + 1 == 2 ** 33
assert ((rho - 1) // 2) + 1 - 1 == rz["surplus_at_M2"] == 8589934591
M = 1
while ((rho - 1) // M) + 1 > 1:
    M *= 2
assert M == rho, "ceil(rho/M) = 1 first holds at M = rho"
# shape fence: razor row and both rho=2 exhibits at r > R/2
assert 2 * rz["r"] > rz["R"]
for tag in ("H1", "H3"):
    n, k, rho_, R, r, m, off = shape(CELLS[tag])
    assert 2 * r > R, tag

print(
    "RATE_HALF_FAR_CA_NEGATION_CLOSURE_EXCESS_FENCE_AUDIT_PASS "
    "(CNT) by enumeration on 6 cells; direct-functional replays H1@1009,"
    "H1@2003,H3@65537(329 slopes),H4@65537(0 bad); razor surplus 2^33-1; "
    "generic-qualifier exhibit at H4@1009 recorded in certificate.json"
)
