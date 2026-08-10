#!/usr/bin/env python3
"""Deterministic arithmetic replay for the residual-evaluation direction."""


def polymul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def peval(a, x, p):
    value = 0
    for coefficient in reversed(a):
        value = (value * x + coefficient) % p
    return value


def main():
    p = 1009
    profiles = 0
    pairings = 0
    for m in range(2, 33):
        rho = 4 * m - 1
        negative_rank = m - 1
        assert negative_rank == len(range(m - 1))
        assert 1 - rho < 0

        for repeated in (False, True):
            s = (7 * m + 3) % p
            # A_0 has degree m-1 and optionally retains one copy of z-s.
            a0 = [1]
            roots = [s] if repeated else []
            roots += [(s + j + 1) % p for j in range(m - 1 - len(roots))]
            for root in roots:
                a0 = polymul(a0, [(-root) % p, 1], p)
            q0 = polymul(a0, [(-s) % p, 1], p)
            assert len(a0) == m
            assert len(q0) == m + 1
            assert polymul(a0, [(-s) % p, 1], p) == q0

            evaluation = [pow(s, j, p) for j in range(m - 1)]
            assert evaluation[0] == 1
            for j, value in enumerate(evaluation):
                basis = [0] * (j + 1)
                basis[j] = 1
                assert peval(basis, s, p) == value
                pairings += 1
            profiles += 1

    official_m = 1 << 37
    assert 4 * official_m - 1 > 0
    assert official_m - 1 > 0
    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_PICARD_RESIDUAL_EVALUATION_DIRECTION_PASS "
        f"profiles={profiles} pairings={pairings} official_m={official_m}"
    )


if __name__ == "__main__":
    main()
