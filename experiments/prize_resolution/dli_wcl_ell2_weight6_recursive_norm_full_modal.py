#!/usr/bin/env python3
"""Exhaust the weight-six router norm obstruction in sharded Modal workers."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


OUTPUT = Path(__file__).with_name(
    "dli_wcl_ell2_weight6_recursive_norm_full_result.json"
)
ORDER = 1024
EXPECTED_CANDIDATES = 404_740
BATCH_SIZE = 128
VOLUME_PATH = "/certificate/weight6_candidates.bin"
METADATA_PATH = "/certificate/weight6_candidates_metadata.json"

app = modal.App("rs-mca-dli-wcl-weight6-recursive-norm-full")
volume = modal.Volume.from_name(
    "rs-mca-dli-wcl-weight6-recursive-norm-v1", create_if_missing=True
)
generator_image = modal.Image.debian_slim()
worker_image = (
    modal.Image.debian_slim().pip_install("python-flint").apt_install("pari-gp")
)


@app.function(
    image=generator_image,
    cpu=2,
    memory=4096,
    timeout=300,
    volumes={"/certificate": volume},
)
def generate_candidates() -> dict[str, object]:
    import hashlib
    import itertools
    import json
    import struct
    from collections import Counter, defaultdict

    order = ORDER
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
    pair_orbit_histogram: Counter[int] = Counter()
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
        pair_orbit_histogram[len(images)] += 1
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

    multiplicities: Counter[tuple[int, int, int]] = Counter()
    for a, b in representatives:
        for product in range(order):
            multiplicities[canonical_key(a, b, product)] += 1
    candidates = sorted(multiplicities)
    if len(candidates) != EXPECTED_CANDIDATES:
        raise AssertionError("candidate count")

    digest = hashlib.sha256()
    with open(VOLUME_PATH, "wb") as handle:
        for candidate in candidates:
            packed = struct.pack("<HHH", *candidate)
            handle.write(packed)
            digest.update(f"{candidate[0]},{candidate[1]},{candidate[2]}\n".encode())

    metadata = {
        "schema": "dli-wcl-ell2-weight6-candidate-file-v1",
        "order": order,
        "legal_pairs": len(legal_pairs),
        "pair_orbits": len(representatives),
        "pair_orbit_size_histogram": dict(sorted(pair_orbit_histogram.items())),
        "router_presentations": len(representatives) * order,
        "candidate_orbits": len(candidates),
        "presentation_multiplicity_histogram": dict(
            sorted(Counter(multiplicities.values()).items())
        ),
        "representative_digest": digest.hexdigest(),
        "binary_sha256": hashlib.sha256(Path(VOLUME_PATH).read_bytes()).hexdigest(),
        "status": "COMPLETE",
    }
    Path(METADATA_PATH).write_text(json.dumps(metadata, sort_keys=True) + "\n")
    volume.commit()
    return metadata


@app.function(
    image=worker_image,
    cpu=2,
    memory=4096,
    timeout=900,
    max_containers=500,
    volumes={"/certificate": volume},
)
def process_batch(bounds: tuple[int, int]) -> dict[str, object]:
    import hashlib
    import math
    import struct
    import subprocess
    import sys
    import time
    from collections import defaultdict

    from flint import fmpz_poly

    sys.set_int_max_str_digits(0)
    started = time.monotonic()
    start, end = bounds
    if not 0 <= start < end <= EXPECTED_CANDIDATES:
        raise AssertionError("batch bounds")
    with open(VOLUME_PATH, "rb") as handle:
        handle.seek(6 * start)
        payload = handle.read(6 * (end - start))
    candidates = [row for row in struct.iter_unpack("<HHH", payload)]
    if len(candidates) != end - start:
        raise AssertionError("candidate read")

    order = ORDER
    degree = order // 2
    modulus = fmpz_poly([1] + [0] * (degree - 1) + [1])

    def reduce(value: fmpz_poly) -> fmpz_poly:
        return value % modulus

    def multiply(left: fmpz_poly, right: fmpz_poly) -> fmpz_poly:
        return reduce(left * right)

    def monomial(exponent: int) -> fmpz_poly:
        coefficients = [0] * degree
        exponent %= order
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

    def obstruction(candidate: tuple[int, int, int]) -> tuple[int, bool, bool]:
        one = fmpz_poly([1])
        x_value = monomial(candidate[0])
        y_value = monomial(candidate[1])
        d_value = monomial(candidate[2])
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
        first_zero = first == 0
        second_zero = second == 0
        first_norm = 0 if first_zero else recursive_norm(first)
        second_norm = 0 if second_zero else recursive_norm(second)
        common = math.gcd(first_norm, second_norm)
        u_norm = recursive_norm(u_value)
        if u_norm == 0:
            raise AssertionError("char-zero weight-three branch")
        while common:
            removable = math.gcd(common, u_norm)
            if removable == 1:
                break
            common //= removable
        return common, first_zero, second_zero

    obstruction_rows = []
    structural_zero_cases = []
    for candidate in candidates:
        common, first_zero, second_zero = obstruction(candidate)
        obstruction_rows.append((candidate, common))
        if first_zero or second_zero:
            structural_zero_cases.append(
                {
                    "candidate": list(candidate),
                    "first_zero": first_zero,
                    "second_zero": second_zero,
                }
            )

    distinct = sorted({common for _, common in obstruction_rows if common > 1})
    factors_by_value: dict[int, list[tuple[int, int]]] = {}
    if distinct:
        values = ",".join(str(value) for value in distinct)
        program = (
            f"v=[{values}];"
            "for(i=1,#v,f=factor(v[i]);print(\"BEGIN:\",i);"
            "for(j=1,matsize(f)[1],print(f[j,1],\":\",f[j,2])));quit()\n"
        )
        completed = subprocess.run(
            ["gp", "-q", "-s", "2147483648"],
            input=program,
            text=True,
            capture_output=True,
            timeout=300,
            check=True,
        )
        by_index: dict[int, list[tuple[int, int]]] = defaultdict(list)
        current = 0
        for line in completed.stdout.splitlines():
            if line.startswith("BEGIN:"):
                current = int(line.split(":", 1)[1])
            elif current and ":" in line:
                prime_text, exponent_text = line.split(":", 1)
                by_index[current].append((int(prime_text), int(exponent_text)))
        for index, value in enumerate(distinct, 1):
            factors = by_index[index]
            if math.prod(prime**exponent for prime, exponent in factors) != value:
                raise AssertionError("incomplete factorization")
            factors_by_value[value] = factors

    candidate_digest = hashlib.sha256()
    factor_digest = hashlib.sha256()
    prime_set = set()
    max_v2 = -1
    max_v2_cases = []
    high_gate_cases = []
    for candidate, common in obstruction_rows:
        candidate_digest.update(
            f"{candidate[0]},{candidate[1]},{candidate[2]}\n".encode()
        )
        factors = factors_by_value.get(common, [])
        factor_text = ",".join(f"{prime}^{exponent}" for prime, exponent in factors)
        factor_digest.update(
            f"{candidate[0]},{candidate[1]},{candidate[2]}:{common}:{factor_text}\n".encode()
        )
        for prime, exponent in factors:
            prime_set.add(prime)
            valuation = (prime - 1 & -(prime - 1)).bit_length() - 1
            case = {
                "candidate": list(candidate),
                "prime": str(prime),
                "exponent": exponent,
                "v2_prime_minus_1": valuation,
            }
            if valuation > max_v2:
                max_v2 = valuation
                max_v2_cases = [case]
            elif valuation == max_v2 and len(max_v2_cases) < 3:
                max_v2_cases.append(case)
            if valuation >= 41:
                high_gate_cases.append(case)

    return {
        "schema": "dli-wcl-ell2-weight6-recursive-norm-batch-v1",
        "start": start,
        "end": end,
        "rows": len(candidates),
        "candidate_digest": candidate_digest.hexdigest(),
        "factor_digest": factor_digest.hexdigest(),
        "nonunit_gcds": sum(common > 1 for _, common in obstruction_rows),
        "distinct_nonunit_gcds": len(distinct),
        "max_gcd_bits": max((common.bit_length() for _, common in obstruction_rows), default=0),
        "distinct_primes": [str(prime) for prime in sorted(prime_set)],
        "max_v2_prime_minus_1": max_v2,
        "max_v2_cases": max_v2_cases,
        "structural_zero_cases": structural_zero_cases,
        "high_gate_cases": high_gate_cases,
        "seconds": round(time.monotonic() - started, 6),
        "status": "COMPLETE",
    }


@app.local_entrypoint()
def main(limit: int = 0) -> None:
    metadata = generate_candidates.remote()
    row_count = EXPECTED_CANDIDATES if limit <= 0 else min(limit, EXPECTED_CANDIDATES)
    bounds = [
        (start, min(start + BATCH_SIZE, row_count))
        for start in range(0, row_count, BATCH_SIZE)
    ]
    remote_rows = list(process_batch.map(bounds, return_exceptions=True))
    batches = []
    errors = []
    for bound, row in zip(bounds, remote_rows):
        if isinstance(row, BaseException):
            errors.append({"bounds": list(bound), "error": repr(row)})
        else:
            batches.append(row)

    batches.sort(key=lambda row: int(row["start"]))
    covered = sum(int(row["rows"]) for row in batches)
    source_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    aggregate_candidate_digest = hashlib.sha256(
        "\n".join(str(row["candidate_digest"]) for row in batches).encode()
    ).hexdigest()
    aggregate_factor_digest = hashlib.sha256(
        "\n".join(str(row["factor_digest"]) for row in batches).encode()
    ).hexdigest()
    result = {
        "schema": "dli-wcl-ell2-weight6-recursive-norm-full-v1",
        "scope": "complete" if row_count == EXPECTED_CANDIDATES else "prefix test",
        "status": (
            "COMPLETE"
            if not errors and covered == row_count
            else "INCOMPLETE"
        ),
        "source_sha256": source_sha256,
        "candidate_metadata": metadata,
        "requested_rows": row_count,
        "covered_rows": covered,
        "batch_size": BATCH_SIZE,
        "batches": batches,
        "errors": errors,
        "aggregate_candidate_digest": aggregate_candidate_digest,
        "aggregate_factor_digest": aggregate_factor_digest,
        "nonunit_gcds": sum(int(row["nonunit_gcds"]) for row in batches),
        "distinct_primes": sorted(
            {
                prime
                for row in batches
                for prime in row["distinct_primes"]
            },
            key=int,
        ),
        "max_gcd_bits": max((int(row["max_gcd_bits"]) for row in batches), default=0),
        "max_v2_prime_minus_1": max(
            (int(row["max_v2_prime_minus_1"]) for row in batches), default=-1
        ),
        "structural_zero_cases": [
            case for row in batches for case in row["structural_zero_cases"]
        ],
        "high_gate_cases": [
            case for row in batches for case in row["high_gate_cases"]
        ],
        "max_batch_seconds": max(
            (float(row["seconds"]) for row in batches), default=0.0
        ),
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_ELL2_WEIGHT6_RECURSIVE_NORM_FULL "
        + json.dumps(
            {
                "scope": result["scope"],
                "status": result["status"],
                "covered_rows": covered,
                "batches": len(batches),
                "errors": len(errors),
                "nonunit_gcds": result["nonunit_gcds"],
                "distinct_primes": len(result["distinct_primes"]),
                "max_gcd_bits": result["max_gcd_bits"],
                "max_v2_prime_minus_1": result["max_v2_prime_minus_1"],
                "structural_zero_cases": len(result["structural_zero_cases"]),
                "high_gate_cases": len(result["high_gate_cases"]),
                "max_batch_seconds": result["max_batch_seconds"],
            },
            sort_keys=True,
        )
    )
