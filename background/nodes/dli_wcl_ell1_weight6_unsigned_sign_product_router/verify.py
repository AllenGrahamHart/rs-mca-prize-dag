#!/usr/bin/env python3
"""Verify the WCL weight-six unsigned sign-product router."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BURNSIDE = ROOT / "experiments/prize_resolution/dli_wcl_ell1_weight6_unsigned_burnside_result.json"
BURNSIDE_SOURCE = ROOT / "experiments/prize_resolution/dli_wcl_ell1_weight6_unsigned_burnside_modal.py"
FORMULA = ROOT / "experiments/prize_resolution/dli_wcl_ell1_weight6_psi6_formula_result.json"
FORMULA_SOURCE = ROOT / "experiments/prize_resolution/dli_wcl_ell1_weight6_psi6_formula_modal.py"

HASHES = {
    BURNSIDE: "ac03b26f0627e20e96081c135c1a26ea10b2226a9adb1689bf9f74928fc8aab9",
    BURNSIDE_SOURCE: "eb3a06197ad0a7377b36a8c5677c0ec2ae1561ce214853771a9a7c2b36ca8560",
    FORMULA: "f74cf2c2775821182a9f9086a43c64c91772c28f6bd9eb8467cabe8c142d9292",
    FORMULA_SOURCE: "252d3345e3ff46281b4f74707e52a4f71819b26ea77673b45097199680669b3a",
}

ORDER = 256
WEIGHT = 6
GROUP_ORDER = 32_768
FIXED = [197_438_898_176, 184_310_267_904]
ORBITS = [6_025_357, 5_624_703]


class Reject(ValueError):
    pass


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def integer(value: object) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise Reject("integer")
    return value


def validate_burnside(data: object) -> None:
    keys = {
        "compression_ratio", "fixed_sums_by_product_parity", "group_order",
        "orbit_count", "orbits_by_product_parity", "order", "schema",
        "seconds", "signed_affine_galois_classes", "status",
        "transformation_digest", "transformations", "weight",
    }
    if not isinstance(data, dict) or set(data) != keys:
        raise Reject("Burnside schema")
    if (
        data["schema"] != "dli-wcl-ell1-weight6-unsigned-burnside-v1"
        or data["status"] != "COMPLETE"
        or integer(data["order"]) != ORDER
        or integer(data["weight"]) != WEIGHT
        or integer(data["group_order"]) != GROUP_ORDER
        or integer(data["transformations"]) != GROUP_ORDER
        or data["fixed_sums_by_product_parity"] != FIXED
        or data["orbits_by_product_parity"] != ORBITS
        or integer(data["orbit_count"]) != sum(ORBITS)
        or integer(data["signed_affine_galois_classes"]) != 185_569_028
        or data["transformation_digest"] != "a8b91835001476adc37630576d8ac9ba331836279bdbfeb3de04de1969c48f95"
        or not isinstance(data["seconds"], (int, float))
        or abs(data["compression_ratio"] - 185_569_028 / sum(ORBITS)) > 1e-15
    ):
        raise Reject("Burnside payload")


def validate_formula_fence(data: object) -> None:
    expected = [
        ("eliminate_r6", 16),
        ("eliminate_r5", 58),
        ("eliminate_r4", 294),
        ("eliminate_r3", 2079),
    ]
    if not isinstance(data, dict) or set(data) != {"schema", "stage_lines", "status"}:
        raise Reject("formula fence schema")
    if data["schema"] != "dli-wcl-ell1-weight6-psi6-formula-v1" or data["status"] != "TIMEOUT":
        raise Reject("formula fence header")
    rows = []
    for line in data["stage_lines"]:
        if not isinstance(line, str) or not line.startswith("STAGE "):
            raise Reject("formula stage")
        row = json.loads(line[6:])
        rows.append((row.get("stage"), row.get("terms")))
    if rows != expected:
        raise Reject("formula stage ledger")


def burnside_digest() -> tuple[list[int], str]:
    totals = [0, 0]
    ledger = hashlib.sha256()
    for multiplier in range(1, ORDER, 2):
        for shift in range(ORDER):
            seen = [False] * ORDER
            cycles = []
            for start in range(ORDER):
                if seen[start]:
                    continue
                cycle = []
                point = start
                while not seen[point]:
                    seen[point] = True
                    cycle.append(point)
                    point = (multiplier * point + shift) % ORDER
                if point != start:
                    raise Reject("cycle")
                cycles.append(cycle)
            dp = [[0, 0] for _ in range(WEIGHT + 1)]
            dp[0][0] = 1
            for cycle in cycles:
                length = len(cycle)
                if length > WEIGHT:
                    continue
                parity = sum(cycle) & 1
                for size in range(WEIGHT - length, -1, -1):
                    for old in range(2):
                        dp[size + length][old ^ parity] += dp[size][old]
            even, odd = dp[WEIGHT]
            totals[0] += even
            totals[1] += odd
            ledger.update(f"{multiplier}:{shift}:{even}:{odd}\n".encode())
    return totals, ledger.hexdigest()


def psi(roots: tuple[int, ...], modulus: int | None = None) -> int:
    value = 1
    for mask in range(32):
        factor = roots[0]
        for index in range(1, 6):
            factor += (-1 if (mask >> (index - 1)) & 1 else 1) * roots[index]
        value *= factor
        if modulus is not None:
            value %= modulus
    return value


def algebra_controls() -> None:
    roots = (1, 2, 4, 8, 16, 32)
    baseline = psi(roots)
    if baseline == 0:
        raise Reject("baseline")
    for index in range(6):
        changed = list(roots)
        changed[index] *= -1
        if psi(tuple(changed)) != baseline:
            raise Reject("square-root invariance")
    for order in ((1, 0, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0), (2, 5, 0, 4, 1, 3)):
        if psi(tuple(roots[index] for index in order)) != baseline:
            raise Reject("symmetry")
    if psi(tuple(3 * root for root in roots)) != 3**32 * baseline:
        raise Reject("homogeneity")

    p, omega = 97, 28
    exponents = (0, 1, 2, 3, 4, 8)
    signs = (1, -1, 1, 1, 1, 1)
    relation = tuple(
        sign * pow(omega, exponent, p) % p
        for exponent, sign in zip(exponents, signs)
    )
    if sum(relation) % p or len({root * root % p for root in relation}) != 6:
        raise Reject("positive control fixture")
    if psi(relation, p) != 0:
        raise Reject("positive control")

    for exponent_sum in range(256):
        target = exponent_sum & 1
        solutions = [
            shift for shift in range(256)
            if (exponent_sum + WEIGHT * shift) % 256 == target
        ]
        if len(solutions) != 2 or (solutions[1] - solutions[0]) % 256 != 128:
            raise Reject("sector normalization")


def main() -> None:
    for path, expected in HASHES.items():
        if digest(path) != expected:
            raise Reject(f"hash {path.name}")
    burnside = json.loads(BURNSIDE.read_text())
    formula = json.loads(FORMULA.read_text())
    validate_burnside(burnside)
    validate_formula_fence(formula)

    controls = []
    for mutate in (
        lambda item: item.__setitem__("orbit_count", item["orbit_count"] - 1),
        lambda item: item["orbits_by_product_parity"].__setitem__(0, ORBITS[0] - 1),
        lambda item: item.__setitem__("transformation_digest", "0" * 64),
    ):
        altered = copy.deepcopy(burnside)
        mutate(altered)
        try:
            validate_burnside(altered)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("Burnside mutation control")

    totals, ledger = burnside_digest()
    if totals != FIXED or ledger != burnside["transformation_digest"]:
        raise Reject("exact Burnside replay")
    algebra_controls()
    print(
        "DLI_WCL_ELL1_WEIGHT6_UNSIGNED_ROUTER_PASS "
        f"orbits={sum(ORBITS)} sectors={ORBITS} transformations={GROUP_ORDER} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
