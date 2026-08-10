#!/usr/bin/env python3
"""Finite-field replay of marked-row elimination and source combination."""


def inv(a, p):
    return pow(a % p, p - 2, p)


def main():
    p = 1009
    profiles = 0
    moment_checks = 0
    for m in range(2, 32):
        rho = 4 * m - 1
        assert rho + 2 == 4 * m + 1
        n = 2 * m + 4
        points = list(range(1, n + 1))
        x0 = points[0]

        sigma_prime = {}
        for x in points:
            value = 1
            for y in points:
                if y != x:
                    value = value * (x - y) % p
            sigma_prime[x] = value

        omega0 = {x: inv(sigma_prime[x], p) for x in points}
        omega1 = {x: x * omega0[x] % p for x in points}

        # Both source weights annihilate all moments through degree 2m+1.
        for omega in (omega0, omega1):
            for degree in range(2 * m + 2):
                assert sum(omega[x] * pow(x, degree, p) for x in points) % p == 0
                moment_checks += 1

        # The marked combination annihilates every Veronese tensor entry.
        for omega in (omega0, omega1):
            for degree in range(2 * m + 1):
                total = sum(
                    (x - x0) * omega[x] * pow(x, degree, p)
                    for x in points
                    if x != x0
                )
                assert total % p == 0
                moment_checks += 1

        # Choose a projective source combination avoiding every zero.
        forbidden = {
            (-omega0[x] * inv(omega1[x], p)) % p
            for x in points
            if x != x0 and omega1[x] != 0
        }
        parameter = next(t for t in range(p) if t not in forbidden)
        for x in points[1:]:
            coefficient = (x - x0) * (omega0[x] + parameter * omega1[x])
            assert coefficient % p != 0
        profiles += 1

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_MARKED_ROW_SPLIT_VERONESE_DEPENDENCY_PASS "
        f"profiles={profiles} moment_checks={moment_checks}"
    )


if __name__ == "__main__":
    main()
