#!/usr/bin/env python3
"""Exact small checks for the binary-quartic harmonic norm gate."""

from itertools import combinations, permutations, product


def poly_mul(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return out


def poly_add(*terms):
    size = max(map(len, terms))
    out = [0] * size
    for term in terms:
        for i, value in enumerate(term):
            out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(term, scalar):
    return [scalar * value for value in term]


def invariant_from_roots(roots, p):
    s1 = sum(roots) % p
    s2 = sum(roots[i] * roots[j] for i, j in combinations(range(4), 2)) % p
    s3 = sum(
        roots[i] * roots[j] * roots[k]
        for i, j, k in combinations(range(4), 3)
    ) % p
    s4 = roots[0] * roots[1] * roots[2] * roots[3] % p
    return (
        72 * s2 * s4
        + 9 * s1 * s2 * s3
        - 27 * s3 * s3
        - 27 * s1 * s1 * s4
        - 2 * s2 * s2 * s2
    ) % p


def cross_ratio(roots, p):
    a, b, c, d = roots
    numerator = (a - c) * (b - d) % p
    denominator = (a - d) * (b - c) % p
    return numerator * pow(denominator, -1, p) % p


def is_harmonic(roots, p):
    return cross_ratio(roots, p) in {-1 % p, 2 % p, pow(2, -1, p)}


def sign_product(roots, p):
    answer = 1
    for signs in product((1, -1), repeat=3):
        signed = [roots[0]] + [signs[i - 1] * roots[i] % p for i in range(1, 4)]
        answer = answer * invariant_from_roots(signed, p) % p
    return answer


PAIRINGS = (
    ((0, 1), (2, 3)),
    ((0, 2), (1, 3)),
    ((0, 3), (1, 2)),
)


def pairing_form(roots, pairing, p):
    (i, j), (k, ell) = pairing
    return (
        2 * (roots[i] * roots[j] + roots[k] * roots[ell])
        - (roots[i] + roots[j]) * (roots[k] + roots[ell])
    ) % p


def pairing_sign_product(roots, pairing, p):
    answer = 1
    for signs in product((1, -1), repeat=3):
        signed = [roots[0]] + [signs[i - 1] * roots[i] % p for i in range(1, 4)]
        answer = answer * pairing_form(signed, pairing, p) % p
    return answer


def pairing_norm_formula(x, y, z, t, p):
    q = x * y % p
    pair_sum = (x + y) % p
    delta = (z - t) % p
    c0 = (4 * q + pair_sum * delta - 4 * z * t) % p
    d0 = (pair_sum * (t * t + q) - 4 * t * q) % p
    d1 = 2 * (t * t + q - pair_sum * t) % p
    k0 = (c0 * c0 + 4 * delta * delta * q - 16 * z * d0) % p
    k1 = (4 * c0 * delta - 16 * z * d1) % p
    return (k0 * k0 - q * k1 * k1) % p


def support_formula(roots, p):
    squares = [root * root % p for root in roots]
    answer = 1
    for (i, j), (k, ell) in PAIRINGS:
        answer = answer * pairing_norm_formula(
            squares[i], squares[j], squares[k], squares[ell], p
        ) % p
    return answer


class RadicalAlgebra:
    def __init__(self, squares, p):
        self.squares = [value % p for value in squares]
        self.p = p

    def add(self, left, right):
        out = dict(left)
        for mask, value in right.items():
            out[mask] = (out.get(mask, 0) + value) % self.p
            if out[mask] == 0:
                del out[mask]
        return out

    def scale(self, value, scalar):
        return {
            mask: coefficient * scalar % self.p
            for mask, coefficient in value.items()
            if coefficient * scalar % self.p
        }

    def mul(self, left, right):
        out = {}
        for lmask, lvalue in left.items():
            for rmask, rvalue in right.items():
                overlap = lmask & rmask
                coefficient = lvalue * rvalue
                for i, square in enumerate(self.squares):
                    if overlap & (1 << i):
                        coefficient *= square
                mask = lmask ^ rmask
                out[mask] = (out.get(mask, 0) + coefficient) % self.p
        return {mask: value for mask, value in out.items() if value}

    def conjugate(self, value, index):
        bit = 1 << index
        return {
            mask: (-coefficient if mask & bit else coefficient) % self.p
            for mask, coefficient in value.items()
        }

    def norm(self, value, index):
        return self.mul(value, self.conjugate(value, index))


def algebra_invariant(algebra):
    roots = [{1 << i: 1} for i in range(4)]
    one = {0: 1}
    zero = {}
    s1 = zero
    s2 = zero
    s3 = zero
    for root in roots:
        s1 = algebra.add(s1, root)
    for indices in combinations(range(4), 2):
        s2 = algebra.add(s2, algebra.mul(roots[indices[0]], roots[indices[1]]))
    for indices in combinations(range(4), 3):
        term = one
        for index in indices:
            term = algebra.mul(term, roots[index])
        s3 = algebra.add(s3, term)
    s4 = one
    for root in roots:
        s4 = algebra.mul(s4, root)

    terms = [
        algebra.scale(algebra.mul(s2, s4), 72),
        algebra.scale(algebra.mul(algebra.mul(s1, s2), s3), 9),
        algebra.scale(algebra.mul(s3, s3), -27),
        algebra.scale(algebra.mul(algebra.mul(s1, s1), s4), -27),
        algebra.scale(algebra.mul(algebra.mul(s2, s2), s2), -2),
    ]
    answer = zero
    for term in terms:
        answer = algebra.add(answer, term)
    return answer


def check_normalized_identity():
    # For XY(X-Y)(X-lambda Y): (a,b,c,d,e)=(0,1,-1-lambda,lambda,0).
    c = [-1, -1]
    d = [0, 1]
    direct = poly_add(poly_scale(poly_mul(c, d), 9), poly_scale(poly_mul(poly_mul(c, c), c), -2))
    factored = poly_mul(poly_mul([1, 1], [-1, 2]), [-2, 1])
    assert direct == factored == [2, -3, -3, 2]


def check_cross_ratio_equivalence():
    p = 11
    for roots in combinations(range(p), 4):
        assert (invariant_from_roots(roots, p) == 0) == is_harmonic(roots, p)
        pairing_product = 1
        for pairing in PAIRINGS:
            pairing_product = pairing_product * pairing_form(roots, pairing, p) % p
        assert invariant_from_roots(roots, p) == -pairing_product % p


def check_norm_and_invariance():
    p = 97
    roots = [1, 2, 3, 4]
    squares = [root * root % p for root in roots]
    direct = sign_product(roots, p)
    assert direct != 0

    algebra = RadicalAlgebra(squares, p)
    normed = algebra_invariant(algebra)
    for index in (1, 2, 3):
        normed = algebra.norm(normed, index)
    assert normed == {0: direct}

    for index in range(4):
        changed = roots[:]
        changed[index] = -changed[index] % p
        assert sign_product(changed, p) == direct
    for order in permutations(range(4)):
        assert sign_product([roots[i] for i in order], p) == direct

    assert support_formula(roots, p) == direct
    squares = [root * root % p for root in roots]
    for (i, j), (k, ell) in PAIRINGS:
        expected = pairing_sign_product(roots, ((i, j), (k, ell)), p)
        assert pairing_norm_formula(
            squares[i], squares[j], squares[k], squares[ell], p
        ) == expected

    scale = 5
    scaled = [scale * root % p for root in roots]
    assert sign_product(scaled, p) == direct * pow(scale, 48, p) % p

    harmonic = [1, 27, 12, 75]
    assert len({root * root % p for root in harmonic}) == 4
    assert invariant_from_roots(harmonic, p) == 0
    assert sign_product(harmonic, p) == 0
    assert support_formula(harmonic, p) == 0


def check_mutation_caught():
    # Changing the cubic coefficient destroys the normalized factorization.
    c = [-1, -1]
    d = [0, 1]
    mutated = poly_add(poly_scale(poly_mul(c, d), 9), poly_scale(poly_mul(poly_mul(c, c), c), -3))
    target = poly_mul(poly_mul([1, 1], [-1, 2]), [-2, 1])
    assert mutated != target


def main():
    check_normalized_identity()
    check_cross_ratio_equivalence()
    check_norm_and_invariance()
    check_mutation_caught()
    print("PASS binary-quartic harmonic norm gate")


if __name__ == "__main__":
    main()
