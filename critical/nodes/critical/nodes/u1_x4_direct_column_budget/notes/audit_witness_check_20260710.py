#!/usr/bin/env python3
"""Independent replay of the (n=8192, p=67239937) h=3 witness trade.

Worktree claim (context lead, FLIP_LOG 2026-07-10): exponent triples
P=(86,1410,6696), Q=(1513,2110,2368) form a same-signature (e1,e2) disjoint
pair over mu_8192 <= F_67239937^*.  Exponents depend on generator choice, so
scan all odd dilations u: test (uP, uQ) for one fixed generator.  Also
verify p = 1 mod n, p > n^2, and non-torality (h=3 toral needs 3 | n; 3 does
not divide 8192, so any hit is automatically non-toral).
"""
n, p = 8192, 67239937
assert (p - 1) % n == 0
assert p > n * n
# find generator of mu_n
e = (p - 1) // n
a = 2
while True:
    z = pow(a, e, p)
    if pow(z, n, p) == 1 and pow(z, n // 2, p) != 1:
        break
    a += 1
P = (86, 1410, 6696)
Q = (1513, 2110, 2368)


def esig(roots):
    e1 = sum(roots) % p
    e2 = (roots[0] * roots[1] + roots[0] * roots[2] + roots[1] * roots[2]) % p
    return e1, e2


hits = []
for u in range(1, n, 2):
    A = [pow(z, (u * x) % n, p) for x in P]
    B = [pow(z, (u * x) % n, p) for x in Q]
    if esig(A) == esig(B):
        hits.append(u)
print(f"generator base a={a}; dilation hits: {len(hits)} -> {hits[:8]}")
if hits:
    u = hits[0]
    A = sorted((u * x) % n for x in P)
    B = sorted((u * x) % n for x in Q)
    print(f"witness trade at u={u}: P_exps={A} Q_exps={B}")
    print("disjoint:", not set(A) & set(B), "| non-toral: True (3 does not divide 8192)")
    print("WITNESS CONFIRMED: non-toral h=3 trade exists at first official row, first boundary prime")
else:
    print("NO dilation of the claimed pattern is a trade under this generator convention")
