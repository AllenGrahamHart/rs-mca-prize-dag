#!/usr/bin/env python3
"""Finite exact audit of the primitive shift-pair dyadic norm router."""

from itertools import combinations


class PrimeField:
    def __init__(self, p):
        self.p = p
        self.zero = 0
        self.one = 1

    def add(self, a, b):
        return (a + b) % self.p

    def neg(self, a):
        return (-a) % self.p

    def mul(self, a, b):
        return (a * b) % self.p

    def pow(self, a, exponent):
        return pow(a, exponent, self.p)

    def const(self, value):
        return value % self.p


class F9:
    """F_3[x]/(x^2+1), represented as a+bx."""

    p = 3
    zero = (0, 0)
    one = (1, 0)

    def add(self, left, right):
        return ((left[0] + right[0]) % 3, (left[1] + right[1]) % 3)

    def neg(self, value):
        return ((-value[0]) % 3, (-value[1]) % 3)

    def mul(self, left, right):
        a, b = left
        c, d = right
        return ((a * c - b * d) % 3, (a * d + b * c) % 3)

    def pow(self, value, exponent):
        result = self.one
        while exponent:
            if exponent & 1:
                result = self.mul(result, value)
            value = self.mul(value, value)
            exponent >>= 1
        return result

    def const(self, value):
        return (value % 3, 0)


def poly_mul_linear(field, coeffs, root):
    result = [field.zero] * (len(coeffs) + 1)
    for index, coeff in enumerate(coeffs):
        result[index] = field.add(result[index], field.mul(field.neg(root), coeff))
        result[index + 1] = field.add(result[index + 1], coeff)
    return result


def locator_prefix(field, roots, t):
    coeffs = [field.one]
    for root in roots:
        coeffs = poly_mul_linear(field, coeffs, root)
    degree = len(roots)
    return tuple(coeffs[degree - index] for index in range(1, t + 1))


def determinant_bareiss(matrix):
    work = [row[:] for row in matrix]
    size = len(work)
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if work[pivot_index][pivot_index] == 0:
            swap = next(
                (row for row in range(pivot_index + 1, size)
                 if work[row][pivot_index] != 0),
                None,
            )
            assert swap is not None
            work[pivot_index], work[swap] = work[swap], work[pivot_index]
            sign *= -1
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                assert numerator % previous == 0
                work[row][column] = numerator // previous
        previous = pivot
    return sign * work[-1][-1]


def cyclotomic_norm(coeffs):
    """Norm in Z[x]/(x^h+1), using the multiplication matrix."""
    h = len(coeffs)
    matrix = [[0] * h for _ in range(h)]
    for column in range(h):
        for index, coeff in enumerate(coeffs):
            degree = index + column
            if degree >= h:
                degree -= h
                coeff = -coeff
            matrix[degree][column] += coeff
    return abs(determinant_bareiss(matrix))


def multiplicative_order(value, modulus):
    residue = value % modulus
    product = residue
    order = 1
    while product != 1:
        product = product * residue % modulus
        order += 1
        assert order <= modulus
    return order


def orbit_count(p, n, frequencies):
    seen_orbits = set()
    for frequency in frequencies:
        residue = frequency % n
        orbit = []
        current = residue
        while current not in orbit:
            orbit.append(current)
            current = current * p % n
        seen_orbits.add(tuple(sorted(orbit)))
    return len(seen_orbits)


def fold(c, j):
    n = len(c) >> j
    h = n // 2
    buckets = [sum(c[index] for index in range(residue, len(c), n))
               for residue in range(n)]
    return [buckets[residue] - buckets[residue + h] for residue in range(h)]


def evaluate_integer_poly(field, coeffs, point):
    result = field.zero
    power = field.one
    for coeff in coeffs:
        result = field.add(result, field.mul(field.const(coeff), power))
        power = field.mul(power, point)
    return result


def check_pair(field, zeta, p_set, q_set, t):
    n_total = 8
    e = len(p_set)
    c = [int(index in p_set) - int(index in q_set) for index in range(n_total)]
    levels = 0
    max_orbits = 0
    for j in range(t.bit_length()):
        n = n_total >> j
        if (1 << j) > t or n < 4:
            continue
        beta = fold(c, j)
        frequencies = list(range(1, t // (1 << j) + 1, 2))
        xi = field.pow(zeta, 1 << j)
        for frequency in frequencies:
            point = field.pow(xi, frequency)
            assert evaluate_integer_poly(field, beta, point) == field.zero

        energy = sum(value * value for value in beta)
        assert energy <= (1 << (j + 2)) * e
        if any(beta):
            norm = cyclotomic_norm(beta)
            f = multiplicative_order(field.p, n)
            orbit_number = orbit_count(field.p, n, frequencies)
            max_orbits = max(max_orbits, orbit_number)
            divisor = field.p ** (f * orbit_number)
            assert norm > 0 and norm % divisor == 0
            assert norm * norm <= energy ** (n // 2)
        levels += 1

    antipodal = all(c[index] == c[index + 4] for index in range(4))
    beta_zero = not any(fold(c, 0))
    assert beta_zero == antipodal
    if not antipodal:
        assert cyclotomic_norm(fold(c, 0)) > 0
    return levels, antipodal, max_orbits


def audit_field(field, zeta):
    assert field.pow(zeta, 8) == field.one
    assert field.pow(zeta, 4) != field.one
    roots = [field.pow(zeta, index) for index in range(8)]
    collisions = 0
    primitive = 0
    folded = 0
    levels = 0
    max_orbits = 0
    universe = set(range(8))
    for e in (2, 3, 4):
        for p_tuple in combinations(range(8), e):
            p_set = set(p_tuple)
            for q_tuple in combinations(sorted(universe - p_set), e):
                q_set = set(q_tuple)
                for t in range(1, min(3, e - 1) + 1):
                    p_prefix = locator_prefix(field, [roots[a] for a in p_tuple], t)
                    q_prefix = locator_prefix(field, [roots[a] for a in q_tuple], t)
                    if p_prefix != q_prefix:
                        continue
                    checked, is_folded, pair_orbits = check_pair(
                        field, zeta, p_set, q_set, t
                    )
                    levels += checked
                    max_orbits = max(max_orbits, pair_orbits)
                    collisions += 1
                    folded += int(is_folded)
                    primitive += int(not is_folded)
    assert collisions and primitive and folded and levels
    return collisions, primitive, folded, levels, max_orbits


def main():
    split = PrimeField(17)
    split_zeta = 9  # Order 8 modulo 17.
    split_counts = audit_field(split, split_zeta)
    extension = F9()
    extension_zeta = (1, 1)
    extension_counts = audit_field(extension, extension_zeta)

    # Frequencies 1 and 3 are distinct split-prime orbits modulo 17, but one
    # degree-two Frobenius orbit modulo 3.  Explicit vanishing polynomials
    # audit the corresponding p^2 norm divisor in both descriptions.
    assert orbit_count(17, 8, [1, 3]) == 2
    split_beta = [135, -24, 1, 0]
    for frequency in (1, 3):
        assert evaluate_integer_poly(
            split, split_beta, split.pow(split_zeta, frequency)
        ) == split.zero
    assert cyclotomic_norm(split_beta) % (17**2) == 0

    assert orbit_count(3, 8, [1, 3]) == 1
    extension_beta = [2, 1, 1, 0]
    for frequency in (1, 3):
        assert evaluate_integer_poly(
            extension, extension_beta, extension.pow(extension_zeta, frequency)
        ) == extension.zero
    assert cyclotomic_norm(extension_beta) % (3**2) == 0
    print(
        "X4_PRIMITIVE_SHIFTPAIR_DYADIC_NORM_ROUTER_PASS "
        f"split={split_counts} extension={extension_counts}"
    )


if __name__ == "__main__":
    main()
