#!/usr/bin/env python3
"""Verify the affine-plane cap 218 sharpening."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "80a52ccc002ea76bbf30ea7b4013b492ca519cf680deac74d1b0bf6d1c649762"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-pair-pencil-affine-plane-cap-218-sharpening-v1",
        "schema",
    )
    n, m, K = data.get("n"), data.get("m"), data.get("K")
    q, s = data.get("selected_types"), data.get("pair_core_size")
    line, t = data.get("affine_line_cap"), data.get("excluded_plane_occupancy")
    require((n, m, K, q, s, line, t) == (2097152, 1116048, 1048576, 520, m - 2, 15, 219), "pins")

    c = ceil_div(t * s - line * n, t - line)
    require(data.get("plane_core_floor") == c == 1043906, "plane core")
    kmax = K - c
    require(data.get("plane_shortened_K_ceiling") == kmax == 4670, "shortened K")
    lines = (t * ((t - 1) // (line - 1))) // line
    require(data.get("full_line_count_ceiling") == lines == 219, "line packing")
    margin = 96085 - 14 * kmax
    require(data.get("contradiction_margin_floor") == margin == 30705, "margin")
    plane = t - 1
    require(data.get("affine_plane_cap") == plane == 218, "plane cap")

    core = ceil_div(q * s - plane * n, q - plane)
    require(data.get("dimension_three_core_floor") == core == 407831, "dimension-three core")
    n1, K1, m1, s1 = n - core, K - core, m - core, s - core
    require(data.get("dimension_three_shortened_n") == n1 == 1689321, "n1")
    require(data.get("dimension_three_shortened_K") == K1 == 640745, "K1")
    require(data.get("dimension_three_shortened_m") == m1 == 708217, "m1")
    require(data.get("dimension_three_shortened_pair_core") == s1 == 708215, "s1")
    slack = plane * n1 - q * s1
    require(data.get("dimension_three_incidence_slack") == slack == 178, "slack")
    heavy = plane + 1
    require(data.get("dimension_four_heavy_type_floor") == heavy == 219, "heavy")
    record_floor = data.get("selected_type_record_floor")
    require(record_floor == 29, "record floor")
    records = heavy * record_floor
    require(data.get("dimension_four_heavy_record_floor") == records == 6351, "records")
    require("not paid" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_pair_pencil_dimension_four_heavy_affine_three_router",
        "rate_half_mca_rank11_pair_pencil_affine_line_cap_direction_router",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"plane": plane, "core": core, "slack": slack, "records": records}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("affine_line_cap", 16),
        lambda item: item.__setitem__("excluded_plane_occupancy", 218),
        lambda item: item.__setitem__("plane_core_floor", 1043905),
        lambda item: item.__setitem__("full_line_count_ceiling", 220),
        lambda item: item.__setitem__("contradiction_margin_floor", 30704),
        lambda item: item.__setitem__("affine_plane_cap", 219),
        lambda item: item.__setitem__("dimension_three_core_floor", 407830),
        lambda item: item.__setitem__("dimension_four_heavy_record_floor", 6350),
    )
    caught = 0
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutations")
    return caught


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    checked = validate(data)
    if args.tamper_selftest:
        print(f"PAIR_PENCIL_PLANE218_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "PAIR_PENCIL_PLANE218_PASS "
        f"plane={checked['plane']} core={checked['core']} "
        f"slack={checked['slack']} records={checked['records']}"
    )


if __name__ == "__main__":
    main()
