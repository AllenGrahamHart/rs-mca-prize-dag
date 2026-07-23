#!/usr/bin/env python3
"""Independent coefficient audit of Frobenius inversion reciprocity."""


def multiply_polynomials(left, right, p):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return out


checks = 0
for p, h in ((23, 7), (31, 15), (47, 7)):
    # Repeated roots are intentional: the proof claims a multiset identity.
    roots = [1 if j % 3 else p - 1 for j in range(h)]
    q = [1]
    for root in roots:
        q = multiply_polynomials(q, [(-root) % p, 1], p)

    frobenius_roots = [pow(root, p, p) for root in roots]
    inverse_roots = [pow(root, p - 2, p) for root in roots]
    assert frobenius_roots == inverse_roots

    q_frobenius = [pow(value, p, p) for value in q]
    constant = q[0]
    assert [constant * value % p for value in q_frobenius] == list(reversed(q))
    checks += 1

    for j in range(h + 1):
        assert constant * q_frobenius[h - j] % p == q[j]
    checks += 1

print(f"L1_MERSENNE_HNF_FROBENIUS_RECIPROCAL_GATE_AUDIT_PASS checks={checks}")
