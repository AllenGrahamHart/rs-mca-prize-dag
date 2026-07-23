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

    y_zero = 1
    remaining_roots = [p - 1 if j % 2 else 1 for j in range(h - 1)]
    q_tilde = [1]
    for root in remaining_roots:
        q_tilde = multiply(q_tilde, [(-root) % p, 1], p)
    q_tilde_frobenius = [pow(value, p, p) for value in q_tilde]
    assert [q_tilde[0] * value % p for value in q_tilde_frobenius] == \
        list(reversed(q_tilde))
    checks += 1

    roots = [y_zero] + remaining_roots
    q = [1]
    for root in roots:
        q = multiply(q, [(-root) % p, 1], p)
    q_frobenius = [pow(value, p, p) for value in q]
    assert [q[0] * value % p for value in q_frobenius] == list(reversed(q))
    checks += 1

print(f"L1_MERSENNE_HNF_ORDER_ONE_FROBENIUS_GATE_AUDIT_PASS checks={checks}")
