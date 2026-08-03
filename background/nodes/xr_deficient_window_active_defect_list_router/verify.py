#!/usr/bin/env python3
"""Exact fixtures for the active-defect list router."""


def ev(poly, x, q):
    out = 0
    for c in reversed(poly):
        out = (out * x + c) % q
    return out


q = 17
H = [pow(3, i, q) for i in range(16)]
assert len(set(H)) == 16
P = [1, 1]
Q = [0, 1]
tau = [2, 3, 1]
D = set(H[:4])
z_blocks = {H[0]: 0, H[1]: 0, H[2]: None, H[3]: None}

# Outside D, choose w=tau only at the unique H-root of P. On D choose two
# two-point projective direction blocks, both with nonzero primitive residual.
minus_one = q - 1
assert minus_one in H and minus_one not in D
E0 = {}
E1 = {}
w = {}
for x in H:
    px, qx, tx = ev(P, x, q), ev(Q, x, q), ev(tau, x, q)
    if x not in D:
        wx = tx if x == minus_one else (tx + 1) % q
        w[x] = wx
        E0[x] = qx * wx % q
        E1[x] = -px * wx % q
    elif z_blocks[x] == 0:
        # Parameter errors (0,1): finite slope zero.
        E0[x] = qx * tx % q
        E1[x] = (1 - px * tx) % q
    else:
        # Parameter errors (1,0): projective infinite slope.
        E0[x] = (1 + qx * tx) % q
        E1[x] = -px * tx % q

rho = {x: (ev(P, x, q) * E0[x] + ev(Q, x, q) * E1[x]) % q
       for x in H}
assert {x for x in H if rho[x]} == D

Et = {x: (E0[x] - ev(Q, x, q) * ev(tau, x, q)) % q for x in H}
Ft = {x: (E1[x] + ev(P, x, q) * ev(tau, x, q)) % q for x in H}
assert all((ev(P, x, q) * Et[x] + ev(Q, x, q) * Ft[x]) % q == rho[x]
           for x in H)
assert all(Et[x] == ev(Q, x, q) * (w[x] - ev(tau, x, q)) % q
           for x in H if x not in D)
assert all(Ft[x] == -ev(P, x, q) * (w[x] - ev(tau, x, q)) % q
           for x in H if x not in D)
assert not any(Et[x] == Ft[x] == 0 for x in D)

# lambda=[1:0] and [0:1]. Their outside roots are absent or already core;
# their active-defect blocks are the planted disjoint two-point blocks.
finite_block = {x for x in D if Et[x] == 0}
infinite_block = {x for x in D if Ft[x] == 0}
assert finite_block == set(H[:2])
assert infinite_block == set(H[2:4])
assert finite_block.isdisjoint(infinite_block)
roots_Q = {x for x in H if x not in D and ev(Q, x, q) == 0}
roots_P = {x for x in H if x not in D and ev(P, x, q) == 0}
core = {x for x in H if x not in D and ev(tau, x, q) == w[x]}
assert not roots_Q
assert roots_P == {minus_one} <= core

# Exact complementary budget and official endpoint arithmetic.
partition_checks = 0
for n in range(2, 65):
    for e in range(n + 1):
        residual = 17 * n * n - 25 * (n - e)
        assert residual >= 0
        assert 25 * (n - e) + residual == 17 * n * n
        partition_checks += 1

rows = (
    (2**41, 2**39, 2**33 + 1),
    (2**41, 2**38, 2**33 + 1),
    (2**41, 2**37, 2**32 + 1),
)
depth_checks = 0
for _n, k, h in rows:
    for d in (h - 2, (3 * h + 3) // 4):
        m = h - d
        ell = max(1, min(m, 3 * d - 2 * h - 1))
        emax = d - ell - 1
        assert k - ell > emax
        if emax >= 2 * m:
            assert 2 <= emax // m
        depth_checks += 1

print("XR_DEFICIENT_WINDOW_ACTIVE_DEFECT_LIST_ROUTER_PASS "
      f"checks={23 + partition_checks + depth_checks}")
