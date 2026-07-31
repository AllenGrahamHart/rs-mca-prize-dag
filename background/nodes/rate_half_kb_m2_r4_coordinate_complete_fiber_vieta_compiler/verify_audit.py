#!/usr/bin/env python3
"""Independent audit of the complete-fiber product separator."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
CERT = ROOT / "background/nodes/rate_half_kb_m2_r4_coordinate_vieta_profile_only_f29_route_cut/certificate.json"


def determinant(matrix: list[list[int]], prime: int) -> int:
    if len(matrix) == 1:
        return matrix[0][0] % prime
    total = 0
    for column, value in enumerate(matrix[0]):
        minor = [row[:column] + row[column + 1:] for row in matrix[1:]]
        total += (-1 if column % 2 else 1) * value * determinant(minor, prime)
    return total % prime


def row(kappa: int, edge: list[int], prime: int) -> list[int]:
    product = edge[0] * edge[1] % prime
    powers = (1, kappa % prime, kappa * kappa % prime)
    return [(-product * value) % prime for value in powers] + list(powers)


def main() -> None:
    certificate = json.loads(CERT.read_text())
    prime = certificate["field"]
    records = list(zip(
        certificate["K"],
        [orbit[0] for orbit in certificate["k_orbits"]],
    ))
    records.append((certificate["xi"], certificate["eta_orbit"][0]))
    matrix = [row(kappa, edge, prime) for kappa, edge in records]
    value = determinant(matrix, prime)
    if value != 10:
        raise RuntimeError(f"unexpected separator determinant {value}")

    mutated = [entry[:] for entry in matrix]
    mutated[-1][0] = (mutated[-1][0] + 1) % prime
    if determinant(mutated, prime) == value:
        raise RuntimeError("mutation was not detected")

    statement = (NODE / "statement.md").read_text()
    audit = (NODE / "audit.md").read_text()
    if "not a characteristic" not in audit or "separate discovery equations" not in statement:
        raise RuntimeError("scope guard missing")
    if "An antipodal edge" not in audit or "seven-skeleton census" not in audit:
        raise RuntimeError("negative scope guard missing")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_COMPLETE_FIBER_VIETA_AUDIT_PASS "
        f"determinant={value} mutation=detected negative_scope=guarded"
    )


if __name__ == "__main__":
    main()
