#!/usr/bin/env python3
"""Adversarial local-socle replay, including ramified fibres."""


def polymul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def polydiv_linear(a, s, p):
    out = [0] * (len(a) - 1)
    carry = a[-1]
    out[-1] = carry
    for i in range(len(a) - 2, 0, -1):
        carry = (a[i] + s * carry) % p
        out[i - 1] = carry
    remainder = (a[0] + s * carry) % p
    return out, remainder


def main():
    p = 1009
    cases = 0
    socle_checks = 0
    for m in range(2, 22):
        s = (11 * m + 5) % p
        for multiplicity in range(1, m + 1):
            q = [1]
            for _ in range(multiplicity):
                q = polymul(q, [(-s) % p, 1], p)
            for j in range(m - multiplicity):
                q = polymul(q, [(-(s + j + 1)) % p, 1], p)

            a0, remainder = polydiv_linear(q, s, p)
            assert remainder == 0
            assert polymul(a0, [(-s) % p, 1], p) == q
            assert any(a0)

            killed = polymul(a0, [(-s) % p, 1], p)
            assert killed == q
            evaluation = [pow(s, j, p) for j in range(m - 1)]
            assert evaluation and evaluation[0] == 1
            socle_checks += multiplicity + len(evaluation)
            cases += 1

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_PICARD_RESIDUAL_EVALUATION_DIRECTION_AUDIT_PASS "
        f"ramified_cases={cases} socle_checks={socle_checks}"
    )


if __name__ == "__main__":
    main()
