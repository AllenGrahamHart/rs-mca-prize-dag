#!/usr/bin/env python3
"""Off-orbit domain compiler for h=3 same-lambda collisions."""

from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from operator import mul

import sympy as sp


Z, Y, X = sp.symbols("z y x")


@dataclass(frozen=True)
class Exclusion:
    name: str
    polynomial: sp.Expr
    transform: sp.Expr
    deg_z: int
    deg_y: int
    total_degree: int


def poly_degrees(poly: sp.Expr) -> tuple[int, int, int]:
    expanded = sp.Poly(sp.expand(poly), Z, Y)
    return expanded.degree(Z), expanded.degree(Y), expanded.total_degree()


def exclusion(name: str, polynomial: sp.Expr, transform: sp.Expr) -> Exclusion:
    deg_z, deg_y, total = poly_degrees(polynomial)
    numerator, _ = sp.together(polynomial.subs(Y, transform)).as_numer_denom()
    if sp.expand(numerator) != 0:
        raise AssertionError((name, polynomial, transform, numerator))
    return Exclusion(name, sp.factor(polynomial), transform, deg_z, deg_y, total)


def generic_off_orbit_exclusions() -> tuple[Exclusion, ...]:
    return (
        exclusion("id", Y - Z, Z),
        exclusion("inverse", Y * Z - 1, 1 / Z),
        exclusion("minus_one_plus", Y + Z + 1, -(1 + Z)),
        exclusion("minus_inverse_one_plus", Y * (1 + Z) + 1, -1 / (1 + Z)),
        exclusion("minus_one_plus_over_z", Y * Z + Z + 1, -(1 + Z) / Z),
        exclusion("minus_z_over_one_plus", Y * (1 + Z) + Z, -Z / (1 + Z)),
    )


def generic_denominator_product() -> sp.Expr:
    nz = Z * (1 + Z) * (1 + Z + Z**2)
    ny = Y * (1 + Y) * (1 + Y + Y**2)
    return sp.factor(nz * ny)


def generic_off_orbit_product() -> sp.Expr:
    return sp.factor(reduce(mul, (row.polynomial for row in generic_off_orbit_exclusions()), 1))


def ratio_orbit(z: int, p: int) -> frozenset[int]:
    if z % p == 0 or (1 + z) % p == 0:
        raise AssertionError((p, z, "ratio pole"))
    return frozenset(
        (
            z % p,
            pow(z, -1, p),
            (-(1 + z)) % p,
            (-pow((1 + z) % p, -1, p)) % p,
            (-(1 + z) * pow(z, -1, p)) % p,
            (-z * pow((1 + z) % p, -1, p)) % p,
        )
    )


def valid_generic_ratio(t: int, p: int) -> bool:
    return t % p not in (0, (-1) % p) and (1 + t + t * t) % p != 0


def orbit_form_zero(z: int, y: int, p: int) -> bool:
    return any(
        value % p == 0
        for value in (
            y - z,
            y * z - 1,
            y + z + 1,
            y * (1 + z) + 1,
            y * z + z + 1,
            y * (1 + z) + z,
        )
    )


def finite_generic_guardrails() -> dict[str, int]:
    primes = (5, 7, 11, 13, 17, 19, 97)
    checked_pairs = 0
    off_orbit_pairs = 0
    same_orbit_pairs = 0
    for p in primes:
        for z in range(p):
            if not valid_generic_ratio(z, p):
                continue
            orbit = ratio_orbit(z, p)
            for y in range(p):
                if not valid_generic_ratio(y, p):
                    continue
                checked_pairs += 1
                same_orbit = y in orbit
                if same_orbit != orbit_form_zero(z, y, p):
                    raise AssertionError((p, z, y, orbit, same_orbit, orbit_form_zero(z, y, p)))
                if same_orbit:
                    same_orbit_pairs += 1
                else:
                    off_orbit_pairs += 1
    return {
        "primes": len(primes),
        "checked_pairs": checked_pairs,
        "same_orbit_pairs": same_orbit_pairs,
        "off_orbit_pairs": off_orbit_pairs,
    }


def primitive_cube_roots(p: int) -> tuple[int, int] | tuple[()]:
    if (p - 1) % 3:
        return ()
    for omega in range(2, p):
        if (omega * omega + omega + 1) % p == 0:
            return (omega, omega * omega % p)
    raise AssertionError((p, "expected primitive cube root"))


def finite_scale_guardrails() -> dict[str, int]:
    primes = (5, 7, 11, 13, 17, 19, 31, 37, 43, 97)
    checked_pairs = 0
    omega_primes = 0
    empty_branch_primes = 0
    same_orbit_pairs = 0
    off_orbit_pairs = 0
    for p in primes:
        omegas = primitive_cube_roots(p)
        if not omegas:
            empty_branch_primes += 1
            continue
        omega, omega2 = omegas
        omega_primes += 1
        for x in range(1, p):
            orbit = {x, omega * x % p, omega2 * x % p}
            for y in range(1, p):
                checked_pairs += 1
                same_orbit = y in orbit
                cubic_equal = (pow(x, 3, p) - pow(y, 3, p)) % p == 0
                if same_orbit != cubic_equal:
                    raise AssertionError((p, omega, x, y, orbit, cubic_equal))
                if same_orbit:
                    same_orbit_pairs += 1
                else:
                    off_orbit_pairs += 1
    return {
        "primes": len(primes),
        "omega_primes": omega_primes,
        "empty_branch_primes": empty_branch_primes,
        "checked_pairs": checked_pairs,
        "same_orbit_pairs": same_orbit_pairs,
        "off_orbit_pairs": off_orbit_pairs,
    }


def main() -> None:
    print("h=3 repeat same-lambda orbit-domain compiler")
    print("generic off-orbit exclusions for two S3 ratio-orbits z,y:")
    for row in generic_off_orbit_exclusions():
        print(
            f"  {row.name}: {row.polynomial} != 0 "
            f"(deg_z={row.deg_z}, deg_y={row.deg_y}, total={row.total_degree})"
        )

    off_orbit_product = generic_off_orbit_product()
    denom_product = generic_denominator_product()
    off_deg_z, off_deg_y, off_total = poly_degrees(off_orbit_product)
    den_deg_z, den_deg_y, den_total = poly_degrees(denom_product)
    print(
        f"generic_off_orbit_product_degree: deg_z={off_deg_z} "
        f"deg_y={off_deg_y} total={off_total}"
    )
    print(
        f"generic_nonpole_product_degree: deg_z={den_deg_z} "
        f"deg_y={den_deg_y} total={den_total}"
    )
    if (off_deg_z, off_deg_y, off_total) != (6, 6, 10):
        raise AssertionError((off_deg_z, off_deg_y, off_total, off_orbit_product))
    if (den_deg_z, den_deg_y, den_total) != (4, 4, 8):
        raise AssertionError((den_deg_z, den_deg_y, den_total, denom_product))

    generic = finite_generic_guardrails()
    print(
        f"generic_guardrails: primes={generic['primes']} "
        f"checked_pairs={generic['checked_pairs']} "
        f"same_orbit_pairs={generic['same_orbit_pairs']} "
        f"off_orbit_pairs={generic['off_orbit_pairs']}"
    )

    scale = finite_scale_guardrails()
    print(
        "lambda_one_scale_off_orbit: x^3-y^3 != 0 "
        "(primitive-cube branch only; total degree 3)"
    )
    print(
        f"scale_guardrails: primes={scale['primes']} "
        f"omega_primes={scale['omega_primes']} "
        f"empty_branch_primes={scale['empty_branch_primes']} "
        f"checked_pairs={scale['checked_pairs']} "
        f"same_orbit_pairs={scale['same_orbit_pairs']} "
        f"off_orbit_pairs={scale['off_orbit_pairs']}"
    )
    print("H3_REPEAT_SAME_LAMBDA_ORBIT_DOMAIN_PASS")


if __name__ == "__main__":
    main()
