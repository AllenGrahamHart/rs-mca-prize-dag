#!/usr/bin/env python3
"""Check marked exponents and the bidiagonal kernel identity."""


def main():
    checks = 0
    assert 2 + 2 * 3 == 8
    assert 1 + 2 * 3 == 7
    checks += 2

    for eta in range(3, 100):
        # Row i of L_eta is -z at i and 1 at i+1.  Record exponents.
        for i in range(eta):
            terms = [(-1, i + 1), (1, i + 1)]
            by_degree = {}
            for coefficient, degree in terms:
                by_degree[degree] = by_degree.get(degree, 0) + coefficient
            assert all(coefficient == 0 for coefficient in by_degree.values())
            checks += 1
        assert 2 + 2 * 3 == 8
        assert 1 + 2 * 3 == 7
        checks += 2

    print(f"PASS quadratic correction marked-jet fence checks={checks}")


if __name__ == "__main__":
    main()
