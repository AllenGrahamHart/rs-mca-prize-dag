#!/usr/bin/env python3
"""Factor a uniform pilot of exact weight-six recursive norm gcds on Modal."""

from __future__ import annotations

import json

import modal


app = modal.App("rs-mca-dli-wcl-weight6-recursive-factor-pilot")
image = modal.Image.debian_slim().pip_install("python-flint").apt_install("pari-gp")


@app.function(image=image, cpu=4, memory=8192, timeout=1200)
def pilot(sample_count: int = 512) -> dict[str, object]:
    import hashlib
    import itertools
    import math
    import subprocess
    import sys
    import time
    from collections import defaultdict

    from flint import fmpz_poly

    sys.set_int_max_str_digits(0)
    order = 1024
    degree = order // 2
    half = order // 2
    units = tuple(range(1, order, 2))
    available = tuple(value for value in range(1, order) if value != half)
    legal_pairs = {
        pair
        for pair in itertools.combinations(available, 2)
        if (pair[1] - pair[0]) % order != half
    }

    unseen = set(legal_pairs)
    pair_representative: dict[tuple[int, int], tuple[int, int]] = {}
    canonicalizers: dict[tuple[int, int], tuple[int, ...]] = {}
    representatives = []
    while unseen:
        seed = min(unseen)
        images: dict[tuple[int, int], list[int]] = defaultdict(list)
        for unit in units:
            image_pair = tuple(
                sorted((unit * seed[0] % order, unit * seed[1] % order))
            )
            images[image_pair].append(unit)
        representative = min(images)
        representative_units = images[representative]
        representatives.append(representative)
        for pair, seed_to_pair_units in images.items():
            inverse = pow(seed_to_pair_units[0], -1, order)
            pair_representative[pair] = representative
            canonicalizers[pair] = tuple(
                sorted(unit * inverse % order for unit in representative_units)
            )
        unseen.difference_update(images)

    def canonical_key(a: int, b: int, product: int) -> tuple[int, int, int]:
        presentations = (
            ((a, b), product),
            ((-a % order, b - a), product - 3 * a),
            ((-b % order, a - b), product - 3 * b),
        )
        keys = []
        for raw_pair, raw_product in presentations:
            pair = tuple(sorted(value % order for value in raw_pair))
            representative = pair_representative[pair]
            keys.extend(
                (representative[0], representative[1], unit * raw_product % order)
                for unit in canonicalizers[pair]
            )
        return min(keys)

    key_set = {
        canonical_key(a, b, product)
        for a, b in representatives
        for product in range(order)
    }
    keys = sorted(key_set)
    if len(keys) != 404_740:
        raise AssertionError("candidate count")
    sample_indices = sorted(
        {(index * (len(keys) - 1)) // (sample_count - 1) for index in range(sample_count)}
    )
    sample = [keys[index] for index in sample_indices]

    modulus = fmpz_poly([1] + [0] * (degree - 1) + [1])

    def reduce(value: fmpz_poly) -> fmpz_poly:
        return value % modulus

    def multiply(left: fmpz_poly, right: fmpz_poly) -> fmpz_poly:
        return reduce(left * right)

    def monomial(exponent: int) -> fmpz_poly:
        exponent %= order
        coefficients = [0] * degree
        if exponent >= degree:
            coefficients[exponent - degree] = -1
        else:
            coefficients[exponent] = 1
        return fmpz_poly(coefficients)

    def recursive_norm(value: fmpz_poly) -> int:
        width = degree
        current = value
        while width > 1:
            next_width = width // 2
            even = fmpz_poly(
                [int(current[2 * index]) for index in range(next_width)]
            )
            odd = fmpz_poly(
                [int(current[2 * index + 1]) for index in range(next_width)]
            )
            paired = even * even - fmpz_poly([0, 1]) * odd * odd
            coefficients = [int(paired[index]) for index in range(width)]
            for index in range(next_width, width):
                coefficients[index - next_width] -= coefficients[index]
            current = fmpz_poly(coefficients[:next_width])
            width = next_width
        return abs(int(current[0]))

    def saturated_gcd(exponents: tuple[int, int, int]) -> int:
        one = fmpz_poly([1])
        x_value = monomial(exponents[0])
        y_value = monomial(exponents[1])
        d_value = monomial(exponents[2])
        xy_value = multiply(x_value, y_value)
        u_value = one + x_value + y_value
        a_value = x_value + y_value + xy_value
        w_value = reduce(multiply(u_value, a_value) - xy_value - d_value)
        u_squared = multiply(u_value, u_value)
        sigma = -u_squared
        theta = multiply(u_value, w_value)
        product_value = multiply(multiply(u_squared, u_value), d_value)
        u_power = u_value
        power = 1
        while power < order:
            old_sigma, old_theta, old_product = sigma, theta, product_value
            sigma = reduce(old_sigma * old_sigma - 2 * old_theta)
            theta = reduce(old_theta * old_theta - 2 * old_product * old_sigma)
            product_value = reduce(old_product * old_product)
            u_power = reduce(u_power * u_power)
            power *= 2
        first = reduce(sigma - 3 * u_power)
        second = reduce(theta - 3 * multiply(u_power, u_power))
        common = math.gcd(recursive_norm(first), recursive_norm(second))
        u_norm = recursive_norm(u_value)
        while common:
            removable = math.gcd(common, u_norm)
            if removable == 1:
                break
            common //= removable
        return common

    norm_started = time.monotonic()
    gcds = [saturated_gcd(key) for key in sample]
    norm_seconds = time.monotonic() - norm_started
    distinct = sorted({value for value in gcds if value > 1})

    factor_started = time.monotonic()
    values = ",".join(str(value) for value in distinct)
    program = (
        f"v=[{values}];"
        "for(i=1,#v,f=factor(v[i]);print(\"BEGIN:\",i);"
        "for(j=1,matsize(f)[1],print(f[j,1],\":\",f[j,2])));quit()\n"
    )
    completed = subprocess.run(
        ["gp", "-q", "-s", "4294967296"],
        input=program,
        text=True,
        capture_output=True,
        timeout=1100,
        check=True,
    )
    factor_seconds = time.monotonic() - factor_started

    factors_by_index: dict[int, list[tuple[int, int]]] = defaultdict(list)
    current = 0
    for line in completed.stdout.splitlines():
        if line.startswith("BEGIN:"):
            current = int(line.split(":", 1)[1])
            continue
        if current and ":" in line:
            prime_text, exponent_text = line.split(":", 1)
            factors_by_index[current].append((int(prime_text), int(exponent_text)))

    prime_set = set()
    max_v2 = 0
    max_prime_bits = 0
    factor_digest = hashlib.sha256()
    for index, value in enumerate(distinct, 1):
        factors = factors_by_index[index]
        product = math.prod(prime**exponent for prime, exponent in factors)
        if product != value:
            raise AssertionError((index, "incomplete factorization"))
        for prime, exponent in factors:
            prime_set.add(prime)
            valuation = (prime - 1 & -(prime - 1)).bit_length() - 1
            max_v2 = max(max_v2, valuation)
            max_prime_bits = max(max_prime_bits, prime.bit_length())
            factor_digest.update(f"{index},{prime},{exponent}\n".encode())

    return {
        "schema": "dli-wcl-ell2-weight6-recursive-factor-pilot-v1",
        "candidate_orbits": len(keys),
        "sample_count": len(sample),
        "nonunit_gcds": sum(value > 1 for value in gcds),
        "distinct_nonunit_gcds": len(distinct),
        "distinct_primes": len(prime_set),
        "max_gcd_bits": max((value.bit_length() for value in gcds), default=0),
        "max_prime_bits": max_prime_bits,
        "max_v2_prime_minus_1": max_v2,
        "norm_seconds": round(norm_seconds, 6),
        "factor_seconds": round(factor_seconds, 6),
        "factor_digest": factor_digest.hexdigest(),
        "status": "COMPLETE",
    }


@app.local_entrypoint()
def main(sample_count: int = 512) -> None:
    print(json.dumps(pilot.remote(sample_count), sort_keys=True))
