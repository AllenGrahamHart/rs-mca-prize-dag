#!/usr/bin/env python3
"""Independent audit of the projective-image degree router."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "7db36df8a696c4ad7a415b2c9e0933e395d6fe44845ee0c3bc2f2116dc6b0c03"


def ceiling(a: int, b: int) -> int:
    return (a + b - 1) // b


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    check(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256,
          "contract hash")
    data = json.loads(CONTRACT.read_text())
    conic = []
    higher = []
    gcd_rows = []
    for kprime in range(4960, 4983):
        full = 2953 * kprime - 13661092
        deficit = 14709668 - 2952 * kprime
        gcd_roots = deficit // 218
        primitive_roots = kprime - 2609 - gcd_roots
        conic.append(ceiling(full, (kprime - 1) // 2))
        higher.append(ceiling(full, (kprime - 1) // 3))
        gcd_rows.append((deficit, gcd_roots, primitive_roots,
                         ceiling(primitive_roots, 2)))
    check((conic[0], conic[-1]) == (398, 422), "conic rows")
    check((higher[0], higher[-1]) == (597, 633), "higher rows")
    check(min(conic) == data["conic_normal_floor_first_row"], "conic min")
    check(max(conic) == data["conic_normal_floor_last_row"], "conic max")
    check(min(higher) == data["higher_image_normal_floor_first_row"], "higher min")
    check(max(higher) == data["higher_image_normal_floor_last_row"], "higher max")
    check(gcd_rows[0] == (67748, 310, 2041, 1021), "gcd first")
    check(gcd_rows[-1] == (2804, 12, 2361, 1181), "gcd last")
    check(data["common_gcd_domain_root_ceiling_first_row"] == 310, "gcd root first")
    check(data["common_gcd_domain_root_ceiling_last_row"] == 12, "gcd root last")
    check(data["primitive_direction_root_floor_first_row"] == 2041, "primitive first")
    check(data["primitive_direction_root_floor_last_row"] == 2361, "primitive last")
    check(min(row[3] for row in gcd_rows) == data["conic_map_degree_floor"] == 1021,
          "conic map floor")
    check((4982 - 1) // 2 == data["conic_map_degree_ceiling"] == 2490,
          "conic map ceiling")
    check((4982 - 1) // 3 == data["higher_image_map_degree_ceiling"] == 1660,
          "higher map ceiling")

    proof = " ".join((HERE / "proof.md").read_text().split())
    audit = " ".join((HERE / "audit.md").read_text().lower().split())
    check("d=e deg O_C(1)=ec." in proof, "degree identity")
    check("[f_0:f_1:f_2]=[A^2:AB:B^2]." in proof, "conic form")
    check("inseparable" in audit, "inseparable audit")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    check(nodes["rate_half_mca_rank11_pair_pencil_dimension_three_population_endpoint_direction_saturation"]["status"] == "PROVED",
          "dependency")
    print("RANK11_D3_IMAGE_DEGREE_AUDIT_PASS rows=23 conic=398..422 higher=597..633")


if __name__ == "__main__":
    main()
