#!/usr/bin/env python3
"""Exact quotient-norm controls for both distance-three dihedral branches."""

from __future__ import annotations


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    size = max(len(left), len(right))
    out = [0] * size
    for index in range(size):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(poly: list[int], scalar: int, prime: int) -> list[int]:
    return [scalar * coefficient % prime for coefficient in poly]


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return out


def locator(roots: list[int], prime: int) -> list[int]:
    out = [1]
    for root in roots:
        out = multiply(out, [(-root) % prime, 1], prime)
    return out


def evaluate(poly: list[int], point: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % prime
    return value


def product(values: list[int], prime: int) -> int:
    out = 1
    for value in values:
        out = out * value % prime
    return out


def inverse(value: int, prime: int) -> int:
    require(value % prime != 0, "attempted to invert zero")
    return pow(value, prime - 2, prime)


def divide_linear(poly: list[int], root: int, prime: int) -> list[int]:
    require(len(poly) > 1, "cannot divide a constant polynomial")
    quotient = [0] * (len(poly) - 1)
    quotient[-1] = poly[-1]
    for index in range(len(poly) - 3, -1, -1):
        quotient[index] = (poly[index + 1] + root * quotient[index + 1]) % prime
    remainder = (poly[0] + root * quotient[0]) % prime
    require(remainder == 0, "linear division has nonzero remainder")
    return quotient


def splits_over(poly: list[int], roots: list[int], prime: int) -> bool:
    remainder = poly[:]
    for root in roots:
        while len(remainder) > 1 and evaluate(remainder, root, prime) == 0:
            remainder = divide_linear(remainder, root, prime)
    return len(remainder) == 1


def dickson(order: int, parameter: int, prime: int) -> list[int]:
    if order == 0:
        return [2]
    previous_previous = [2]
    previous = [0, 1]
    for _ in range(2, order + 1):
        current = add([0] + previous, scale(previous_previous, -parameter, prime), prime)
        previous_previous, previous = previous, current
    return previous


class Fixture:
    def __init__(self, branch: str, constant_exponent: int = 0) -> None:
        self.prime = 97
        self.n = 24
        self.e = 2
        self.generator = pow(5, 4, self.prime)
        self.subgroup = sorted(
            {pow(self.generator, index, self.prime) for index in range(self.n)}
        )
        require(len(self.subgroup) == self.n, "toy subgroup has wrong order")

        if branch == "antipodal":
            self.c = -1 % self.prime
            involution = lambda value: -value % self.prime
        elif branch == "constant_product":
            self.c = pow(self.generator, constant_exponent, self.prime)
            involution = lambda value: self.c * inverse(value, self.prime) % self.prime
        else:
            raise ValueError(branch)

        self.branch = branch
        self.involution = involution
        orbits = sorted(
            {
                tuple(sorted((value, involution(value))))
                for value in self.subgroup
                if value != involution(value)
            }
        )
        self.pairs = orbits[: self.e]
        exceptional = {value for pair in self.pairs for value in pair}
        boundary = [value for value in self.subgroup if value not in exceptional][:5]
        self.s, self.x_zero = boundary[:2]
        self.triple = boundary[2:]
        self.a_poly = locator(sorted(exceptional), self.prime)
        self.b_poly = locator(self.triple, self.prime)
        self.internal = [6, 10]
        self.lambdas = [2, 3]

        if branch == "antipodal":
            self.orbit_roots = [left * left % self.prime for left, _ in self.pairs]
        else:
            self.orbit_roots = [
                (left + right) % self.prime for left, right in self.pairs
            ]
        self.e_poly = locator(self.orbit_roots, self.prime)

    def phi(self, parameter: int) -> int:
        numerator = product(
            [(parameter - point) % self.prime for point in self.internal], self.prime
        )
        denominator = product([(-point) % self.prime for point in self.internal], self.prime)
        return numerator * inverse(denominator, self.prime) % self.prime

    def lagrange(self, index: int, parameter: int) -> int:
        numerator = product(
            [
                (parameter - point) % self.prime
                for j, point in enumerate(self.internal)
                if j != index
            ],
            self.prime,
        )
        denominator = product(
            [
                (self.internal[index] - point) % self.prime
                for j, point in enumerate(self.internal)
                if j != index
            ],
            self.prime,
        )
        return numerator * inverse(denominator, self.prime) % self.prime

    def orbit_sum(self, parameter: int, orbit_point: int) -> int:
        total = 0
        for index, root in enumerate(self.orbit_roots):
            quotient = locator(
                [value for value in self.orbit_roots if value != root], self.prime
            )
            coefficient = self.lambdas[index] * inverse(self.internal[index], self.prime)
            coefficient = coefficient * self.lagrange(index, parameter) % self.prime
            total = (total + coefficient * evaluate(quotient, orbit_point, self.prime)) % self.prime
        return total

    def orbit_sum_poly(self, parameter: int) -> list[int]:
        total = [0]
        for index, root in enumerate(self.orbit_roots):
            quotient = locator(
                [value for value in self.orbit_roots if value != root], self.prime
            )
            coefficient = self.lambdas[index] * inverse(self.internal[index], self.prime)
            coefficient = coefficient * self.lagrange(index, parameter) % self.prime
            total = add(total, scale(quotient, coefficient, self.prime), self.prime)
        return total

    def q(self, parameter: int, point: int) -> int:
        total = self.phi(parameter) * evaluate(self.a_poly, point, self.prime)
        correction = 0
        for index, pair in enumerate(self.pairs):
            quotient = locator(
                [value for j, other in enumerate(self.pairs) if j != index for value in other],
                self.prime,
            )
            coefficient = self.lambdas[index] * inverse(self.internal[index], self.prime)
            coefficient = coefficient * self.lagrange(index, parameter) % self.prime
            correction = (correction + coefficient * evaluate(quotient, point, self.prime)) % self.prime
        total += parameter * evaluate(self.b_poly, point, self.prime) * correction
        return total % self.prime

    def q_poly(self, parameter: int) -> list[int]:
        correction = [0]
        for index, _ in enumerate(self.pairs):
            quotient = locator(
                [value for j, other in enumerate(self.pairs) if j != index for value in other],
                self.prime,
            )
            coefficient = self.lambdas[index] * inverse(self.internal[index], self.prime)
            coefficient = coefficient * self.lagrange(index, parameter) % self.prime
            correction = add(correction, scale(quotient, coefficient, self.prime), self.prime)
        return add(
            scale(self.a_poly, self.phi(parameter), self.prime),
            scale(multiply(self.b_poly, correction, self.prime), parameter, self.prime),
            self.prime,
        )

    def antipodal_norm(self, parameter: int, orbit_point: int) -> int:
        sigma_1 = -self.b_poly[2] % self.prime
        sigma_2 = self.b_poly[1]
        sigma_3 = -self.b_poly[0] % self.prime
        e_value = evaluate(self.e_poly, orbit_point, self.prime)
        h_value = self.orbit_sum(parameter, orbit_point)
        even = (
            self.phi(parameter) * e_value
            - parameter * (sigma_1 * orbit_point + sigma_3) * h_value
        ) % self.prime
        odd = parameter * (orbit_point + sigma_2) * h_value % self.prime
        return (even * even - orbit_point * odd * odd) % self.prime

    def antipodal_norm_poly(self, parameter: int) -> list[int]:
        sigma_1 = -self.b_poly[2] % self.prime
        sigma_2 = self.b_poly[1]
        sigma_3 = -self.b_poly[0] % self.prime
        h_poly = self.orbit_sum_poly(parameter)
        even = add(
            scale(self.e_poly, self.phi(parameter), self.prime),
            scale(
                multiply([sigma_3, sigma_1], h_poly, self.prime),
                -parameter,
                self.prime,
            ),
            self.prime,
        )
        odd = scale(
            multiply([sigma_2, 1], h_poly, self.prime), parameter, self.prime
        )
        return add(
            multiply(even, even, self.prime),
            scale([0] + multiply(odd, odd, self.prime), -1, self.prime),
            self.prime,
        )

    def product_norm(self, parameter: int, orbit_point: int) -> int:
        sigma_1 = -self.b_poly[2] % self.prime
        sigma_2 = self.b_poly[1]
        sigma_3 = -self.b_poly[0] % self.prime
        e_value = evaluate(self.e_poly, orbit_point, self.prime)
        h_value = self.orbit_sum(parameter, orbit_point)
        mixed = (
            self.c * orbit_point * orbit_point
            - 2 * self.c * self.c
            - (sigma_1 * self.c + sigma_3) * orbit_point
            + 2 * sigma_2 * self.c
        ) % self.prime
        b_norm = product(
            [
                (self.c + point * point - point * orbit_point) % self.prime
                for point in self.triple
            ],
            self.prime,
        )
        inside = self.c * self.phi(parameter) ** 2 * e_value**2
        inside += self.phi(parameter) * parameter * e_value * h_value * mixed
        inside += parameter**2 * h_value**2 * b_norm
        return pow(self.c, self.e - 1, self.prime) * inside % self.prime

    def product_norm_poly(self, parameter: int) -> list[int]:
        sigma_1 = -self.b_poly[2] % self.prime
        sigma_2 = self.b_poly[1]
        sigma_3 = -self.b_poly[0] % self.prime
        h_poly = self.orbit_sum_poly(parameter)
        mixed = [
            (-2 * self.c * self.c + 2 * sigma_2 * self.c) % self.prime,
            (-(sigma_1 * self.c + sigma_3)) % self.prime,
            self.c,
        ]
        b_norm = [1]
        for point in self.triple:
            b_norm = multiply(
                b_norm,
                [(self.c + point * point) % self.prime, (-point) % self.prime],
                self.prime,
            )
        inside = scale(
            multiply(self.e_poly, self.e_poly, self.prime),
            self.c * self.phi(parameter) ** 2,
            self.prime,
        )
        inside = add(
            inside,
            scale(
                multiply(multiply(self.e_poly, h_poly, self.prime), mixed, self.prime),
                self.phi(parameter) * parameter,
                self.prime,
            ),
            self.prime,
        )
        inside = add(
            inside,
            scale(
                multiply(multiply(h_poly, h_poly, self.prime), b_norm, self.prime),
                parameter * parameter,
                self.prime,
            ),
            self.prime,
        )
        return scale(inside, pow(self.c, self.e - 1, self.prime), self.prime)


def check_antipodal() -> None:
    fixture = Fixture("antipodal")
    quotient_roots = sorted({value * value % fixture.prime for value in fixture.subgroup})
    quotient_locator = locator(quotient_roots, fixture.prime)
    expected = [(-1) % fixture.prime] + [0] * (fixture.n // 2 - 1) + [1]
    require(quotient_locator == expected, "antipodal quotient is not the half subgroup")

    split_parameters = 0
    for parameter in range(fixture.prime):
        direct = product(
            [fixture.q(parameter, point) for point in fixture.subgroup], fixture.prime
        )
        descended = product(
            [fixture.antipodal_norm(parameter, point) for point in quotient_roots],
            fixture.prime,
        )
        require(direct == descended, "antipodal norm descent failed")
        q_poly = fixture.q_poly(parameter)
        v_poly = fixture.antipodal_norm_poly(parameter)
        require(
            all(
                fixture.q(parameter, point) == evaluate(q_poly, point, fixture.prime)
                for point in fixture.subgroup
            ),
            "antipodal Q polynomial mismatch",
        )
        if len(q_poly) == 2 * fixture.e + 2 and q_poly[0] != 0:
            q_split = splits_over(q_poly, fixture.subgroup, fixture.prime)
            v_split = splits_over(v_poly, quotient_roots, fixture.prime)
            require(q_split == v_split, "antipodal split-slope equivalence failed")
            split_parameters += int(q_split)
    require(split_parameters >= fixture.e, "antipodal fixture lost its internal split slopes")


def check_constant_product(constant_exponent: int, expected_fixed: int) -> None:
    fixture = Fixture("constant_product", constant_exponent)
    fixed = [point for point in fixture.subgroup if fixture.involution(point) == point]
    require(len(fixed) == expected_fixed, "wrong fixed-point count")
    nonfixed_orbits = sorted(
        {
            tuple(sorted((point, fixture.involution(point))))
            for point in fixture.subgroup
            if fixture.involution(point) != point
        }
    )
    quotient_roots = [(left + right) % fixture.prime for left, right in nonfixed_orbits]
    omega = locator(quotient_roots, fixture.prime)
    fixed_locator = locator([2 * point % fixture.prime for point in fixed], fixture.prime)
    dickson_minus_two = add(
        dickson(fixture.n, fixture.c, fixture.prime), [-2 % fixture.prime], fixture.prime
    )
    recovered = multiply(fixed_locator, multiply(omega, omega, fixture.prime), fixture.prime)
    require(dickson_minus_two == recovered, "Dickson quotient-locator identity failed")

    all_quotient_roots = quotient_roots + [2 * point % fixture.prime for point in fixed]
    split_parameters = 0
    for parameter in range(fixture.prime):
        direct = product(
            [fixture.q(parameter, point) for point in fixture.subgroup], fixture.prime
        )
        fixed_product = product(
            [fixture.q(parameter, point) for point in fixed], fixture.prime
        )
        descended = fixed_product * product(
            [fixture.product_norm(parameter, point) for point in quotient_roots],
            fixture.prime,
        ) % fixture.prime
        require(direct == descended, "constant-product norm descent failed")
        q_poly = fixture.q_poly(parameter)
        v_poly = fixture.product_norm_poly(parameter)
        require(
            all(
                fixture.q(parameter, point) == evaluate(q_poly, point, fixture.prime)
                for point in fixture.subgroup
            ),
            "constant-product Q polynomial mismatch",
        )
        if len(q_poly) == 2 * fixture.e + 2 and q_poly[0] != 0:
            q_split = splits_over(q_poly, fixture.subgroup, fixture.prime)
            v_split = splits_over(v_poly, all_quotient_roots, fixture.prime)
            require(q_split == v_split, "constant-product split-slope equivalence failed")
            split_parameters += int(q_split)
    require(
        split_parameters >= fixture.e,
        "constant-product fixture lost its internal split slopes",
    )


def main() -> None:
    check_antipodal()
    check_constant_product(constant_exponent=3, expected_fixed=0)
    check_constant_product(constant_exponent=2, expected_fixed=2)
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_DISTANCE_THREE_"
        "DIHEDRAL_SUBGROUP_NORM_DESCENT_PASS branches=3 parameters=97"
    )


if __name__ == "__main__":
    main()
