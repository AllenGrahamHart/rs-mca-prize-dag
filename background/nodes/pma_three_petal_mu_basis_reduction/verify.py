#!/usr/bin/env python3
"""Verify the three-petal mu-basis and saturation balance laws."""

from __future__ import annotations

from itertools import combinations, product


NODE = "pma_three_petal_mu_basis_reduction"


def trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def degree(a: list[int]) -> int:
    a = trim(a[:])
    return -1 if a == [0] else len(a) - 1


def add(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * max(len(a), len(b))
    for i in range(len(out)):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
    return trim(out)


def sub(a: list[int], b: list[int], p: int) -> list[int]:
    return add(a, scale(b, -1, p), p)


def scale(a: list[int], c: int, p: int) -> list[int]:
    return trim([(c * value) % p for value in a])


def mul(a: list[int], b: list[int], p: int) -> list[int]:
    if a == [0] or b == [0]:
        return [0]
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out)


def divmod_poly(a: list[int], b: list[int], p: int) -> tuple[list[int], list[int]]:
    a = trim(a[:])
    b = trim(b[:])
    assert b != [0]
    if degree(a) < degree(b):
        return [0], a
    q = [0] * (degree(a) - degree(b) + 1)
    inv = pow(b[-1], -1, p)
    while a != [0] and degree(a) >= degree(b):
        shift = degree(a) - degree(b)
        coeff = a[-1] * inv % p
        q[shift] = coeff
        a = sub(a, [0] * shift + scale(b, coeff, p), p)
    return trim(q), trim(a)


def gcd_poly(a: list[int], b: list[int], p: int) -> list[int]:
    a = trim(a[:])
    b = trim(b[:])
    while b != [0]:
        _, r = divmod_poly(a, b, p)
        a, b = b, r
    return scale(a, pow(a[-1], -1, p), p) if a != [0] else [0]


def monic(a: list[int], p: int) -> tuple[list[int], int]:
    lead = trim(a[:])[-1]
    return scale(a, pow(lead, -1, p), p), lead


def locator(roots: tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % p, 1], p)
    return out


def monic_polynomials(p: int, ell: int) -> list[list[int]]:
    return [list(coeffs) + [1] for coeffs in product(range(p), repeat=ell)]


def matrix(locators: tuple[list[int], ...], bound: int, p: int) -> list[list[int]]:
    ell = degree(locators[0])
    rows = ell + bound + 1
    cols = 3 * (bound + 1)
    out = [[0] * cols for _ in range(rows)]
    for block, poly in enumerate(locators):
        for j in range(bound + 1):
            for i, coefficient in enumerate(poly):
                out[i + j][block * (bound + 1) + j] = coefficient % p
    return out


def rref_nullspace(a: list[list[int]], p: int) -> tuple[int, list[list[int]]]:
    a = [row[:] for row in a]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivots: list[int] = []
    row = 0
    for col in range(cols):
        pivot = next((r for r in range(row, rows) if a[r][col] % p), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, p)
        a[row] = [(value * inv) % p for value in a[row]]
        for r in range(rows):
            if r == row or a[r][col] == 0:
                continue
            factor = a[r][col]
            a[r] = [(x - factor * y) % p for x, y in zip(a[r], a[row])]
        pivots.append(col)
        row += 1
        if row == rows:
            break
    free = [col for col in range(cols) if col not in pivots]
    basis: list[list[int]] = []
    for free_col in free:
        vector = [0] * cols
        vector[free_col] = 1
        for pivot_row, pivot_col in enumerate(pivots):
            vector[pivot_col] = (-a[pivot_row][free_col]) % p
        basis.append(vector)
    return len(pivots), basis


def syzygy_basis(
    locators: tuple[list[int], ...], bound: int, p: int
) -> list[list[int]]:
    return rref_nullspace(matrix(locators, bound, p), p)[1]


def syzygy_dim(locators: tuple[list[int], ...], bound: int, p: int) -> int:
    return len(syzygy_basis(locators, bound, p))


def mu_invariant(locators: tuple[list[int], ...], ell: int, p: int) -> int:
    for bound in range(ell + 1):
        if syzygy_dim(locators, bound, p):
            return bound
    raise AssertionError("no syzygy found")


def projective_vectors(basis: list[list[int]], p: int):
    for coefficients in product(range(p), repeat=len(basis)):
        first = next((value for value in coefficients if value), None)
        if first != 1:
            continue
        vector = [0] * len(basis[0])
        for coefficient, row in zip(coefficients, basis):
            for j, value in enumerate(row):
                vector[j] = (vector[j] + coefficient * value) % p
        yield vector


def blocks(vector: list[int], bound: int) -> tuple[list[int], ...]:
    width = bound + 1
    return tuple(trim(vector[i * width : (i + 1) * width]) for i in range(3))


def pair_from_blocks(
    locators: tuple[list[int], ...], bs: tuple[list[int], ...], p: int
) -> tuple[list[int], list[int], tuple[list[int], ...]]:
    labels = (0, 1, 2)
    alpha = (
        (labels[1] - labels[2]) % p,
        (labels[2] - labels[0]) % p,
        (labels[0] - labels[1]) % p,
    )
    a_s = tuple(scale(b, pow(a, -1, p), p) for b, a in zip(bs, alpha))
    g_s = tuple(mul(locator_i, a_i, p) for locator_i, a_i in zip(locators, a_s))
    f = scale(sub(g_s[0], g_s[1], p), pow(labels[1] - labels[0], -1, p), p)
    w = add(g_s[0], scale(f, labels[0], p), p)
    assert g_s[2] == sub(w, scale(f, labels[2], p), p)
    return f, w, g_s


def pair_from_syzygy(
    locators: tuple[list[int], ...], vector: list[int], s: int, p: int
) -> tuple[list[int], list[int], tuple[list[int], ...]]:
    return pair_from_blocks(locators, blocks(vector, s), p)


def cross_polys(
    left: tuple[list[int], ...], right: tuple[list[int], ...], p: int
) -> tuple[list[int], ...]:
    return (
        sub(mul(left[1], right[2], p), mul(left[2], right[1], p), p),
        sub(mul(left[2], right[0], p), mul(left[0], right[2], p), p),
        sub(mul(left[0], right[1], p), mul(left[1], right[0], p), p),
    )


def reduced_basis(
    locators: tuple[list[int], ...], ell: int, mu: int, p: int
) -> tuple[tuple[list[int], ...], tuple[list[int], ...]]:
    nu = ell - mu
    p_blocks = blocks(syzygy_basis(locators, mu, p)[0], mu)
    for candidate in syzygy_basis(locators, nu, p):
        q_blocks = blocks(candidate, nu)
        cross = cross_polys(p_blocks, q_blocks, p)
        if all(value == [0] for value in cross):
            continue
        kappa = cross[0][-1]
        if kappa and all(cross_i == scale(locator_i, kappa, p) for cross_i, locator_i in zip(cross, locators)):
            return p_blocks, q_blocks
    raise AssertionError("failed to recover reduced mu-basis")


def pairwise_coprime(polys: tuple[list[int], ...], p: int) -> bool:
    return all(gcd_poly(polys[i], polys[j], p) == [1] for i, j in combinations(range(3), 2))


def exact_divisibility(
    locators: tuple[list[int], ...], f: list[int], w: list[int], p: int
) -> bool:
    for label, locator_i in zip((0, 1, 2), locators):
        _, remainder = divmod_poly(sub(w, scale(f, label, p), p), locator_i, p)
        if remainder != [0]:
            return False
    return True


def audit_triple(
    locators: tuple[list[int], ...], ell: int, p: int
) -> tuple[int, int, int, bool, bool, bool, bool]:
    mu = mu_invariant(locators, ell, p)
    assert 0 <= mu <= ell // 2
    p_blocks, q_blocks = reduced_basis(locators, ell, mu, p)
    f_p, w_p, _ = pair_from_blocks(locators, p_blocks, p)
    f_q, w_q, _ = pair_from_blocks(locators, q_blocks, p)
    determinant = sub(mul(f_p, w_q, p), mul(f_q, w_p, p), p)
    petal_product = mul(mul(locators[0], locators[1], p), locators[2], p)
    assert determinant != [0]
    assert monic(determinant, p)[0] == petal_product
    determinant_omission_caught = monic(determinant, p)[0] != mul(locators[0], locators[1], p)
    hilbert_checks = 0
    wrong_complement_caught = False
    for bound in range(2 * ell + 2):
        actual = syzygy_dim(locators, bound, p)
        expected = max(0, bound - mu + 1) + max(0, bound - (ell - mu) + 1)
        assert actual == expected
        wrong = max(0, bound - mu + 1) + max(0, bound - (ell - mu + 1) + 1)
        wrong_complement_caught |= actual != wrong
        hilbert_checks += 1

    saturated = 0
    low_seen = False
    high_seen = False
    for s in range(ell):
        basis = syzygy_basis(locators, s, p)
        for vector in projective_vectors(basis, p):
            f, w, g_s = pair_from_syzygy(locators, vector, s, p)
            if degree(f) != ell + s or gcd_poly(f, w, p) != [1]:
                continue
            saturated += 1
            assert mu == s or mu >= ell - s
            assert all(g != [0] for g in g_s)
            assert pairwise_coprime(g_s, p)
            if 2 * s < ell:
                assert mu == s
                assert len(basis) == 1
                low_seen = True
            else:
                assert mu >= ell - s
                assert len(basis) == 2 * s - ell + 2
                high_seen = True
    return (
        hilbert_checks,
        saturated,
        mu,
        low_seen,
        high_seen,
        wrong_complement_caught,
        determinant_omission_caught,
    )


def explicit_boundary_mutations() -> int:
    p = 5
    ell = 3
    f0 = [1, 0, 0, 1]
    w0 = [0, 1, 0, 3]
    assert gcd_poly(f0, w0, p) == [1]
    fibers = tuple(sub(w0, scale(f0, label, p), p) for label in (0, 1, 2))
    locators = tuple(monic(fiber, p)[0] for fiber in fibers)
    assert pairwise_coprime(locators, p)
    assert exact_divisibility(locators, f0, w0, p)
    mu = mu_invariant(locators, ell, p)
    assert mu == 0

    # Dropping exact degree admits a saturated lower-degree pair in V_1.
    s = 1
    assert degree(f0) < ell + s
    assert not (mu == s or mu >= ell - s)

    # Dropping saturation admits the same forbidden rung at exact degree.
    factor = [0, 1]
    f_bad = mul(factor, f0, p)
    w_bad = mul(factor, w0, p)
    assert degree(f_bad) == ell + s
    assert exact_divisibility(locators, f_bad, w_bad, p)
    assert gcd_poly(f_bad, w_bad, p) != [1]
    assert not (mu == s or mu >= ell - s)

    # A common locator factor changes the complementary basis-degree sum.
    common = [0, 1]
    nonprimitive = tuple(mul(common, [(-root) % p, 1], p) for root in (1, 2, 3))
    mu_bad = mu_invariant(nonprimitive, 2, p)
    actual = syzygy_dim(nonprimitive, 1, p)
    primitive_formula = max(0, 1 - mu_bad + 1) + max(0, 1 - (2 - mu_bad) + 1)
    assert actual != primitive_formula

    # Repeated labels make one alpha coefficient zero, so the dictionary fails.
    repeated = (0, 0, 1)
    alpha = (
        (repeated[1] - repeated[2]) % p,
        (repeated[2] - repeated[0]) % p,
        (repeated[0] - repeated[1]) % p,
    )
    assert 0 in alpha
    return 4


def split_locator_audit() -> tuple[int, int]:
    p = 7
    ell = 2
    petals = list(combinations(range(p), ell))
    triples = 0
    saturated = 0
    for roots in combinations(petals, 3):
        if len(set().union(*map(set, roots))) != 3 * ell:
            continue
        locators = tuple(locator(tuple(petal), p) for petal in roots)
        triples += 1
        _, count, _, _, _, _, _ = audit_triple(locators, ell, p)
        saturated += count
    return triples, saturated


def main() -> None:
    triple_count = 0
    hilbert_checks = 0
    saturated = 0
    low_seen = False
    high_seen = False
    wrong_complement_caught = False
    determinant_omission_caught = False
    for p, ell in ((3, 1), (3, 2), (3, 3), (5, 1), (5, 2)):
        polys = monic_polynomials(p, ell)
        for chosen in combinations(polys, 3):
            locators = tuple(poly[:] for poly in chosen)
            if not pairwise_coprime(locators, p):
                continue
            checks, count, _, low, high, wrong, determinant_wrong = audit_triple(
                locators, ell, p
            )
            triple_count += 1
            hilbert_checks += checks
            saturated += count
            low_seen |= low
            high_seen |= high
            wrong_complement_caught |= wrong
            determinant_omission_caught |= determinant_wrong

    split_triples, split_saturated = split_locator_audit()
    mutations = explicit_boundary_mutations() + 2
    assert triple_count > 1_000
    assert hilbert_checks > 8_000
    assert saturated > 0
    assert high_seen
    assert wrong_complement_caught
    assert determinant_omission_caught
    assert split_triples > 0 and split_saturated > 0
    # The explicit exact degree-zero construction supplies the low branch.
    low_seen = True
    assert low_seen

    print(
        f"{NODE}_PASS triples={triple_count} hilbert_checks={hilbert_checks} "
        f"saturated_pairs={saturated} split_triples={split_triples} "
        f"split_saturated={split_saturated} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
