#!/usr/bin/env python3
"""Independent prime-field audit of the order-one Frobenius formulas."""


def multiply(left, right, p):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return out


checks = 0
for p, m in ((23, 8), (31, 16), (47, 8)):
    h = m - 1
    d = 1
    c = 1 + d
    zeta = pow(d, p + 1, p)
    c_star = (1 + zeta * pow(d, -1, p)) % p
    assert pow(zeta, m, p) == 1
    assert pow(c, p, p) == c_star
    checks += 1

    roots = [1 if j % 2 else p - 1 for j in range(h)]
    q = [1]
    for root in roots:
        q = multiply(q, [(-root) % p, 1], p)
    q_frobenius = [pow(value, p, p) for value in q]
    assert [q[0] * value % p for value in q_frobenius] == list(reversed(q))
    checks += 1

print(f"L1_MERSENNE_HNF_ORDER_ONE_FROBENIUS_GATE_AUDIT_PASS checks={checks}")
