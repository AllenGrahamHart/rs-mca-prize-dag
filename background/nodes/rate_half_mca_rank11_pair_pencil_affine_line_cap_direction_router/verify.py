#!/usr/bin/env python3
"""Verify the pair-pencil affine-line cap and direction router."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "a2f83ea90cb88bfd0d170fec234a3f9b9d505133db50831a935097214211287e"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def choose2(value: int) -> int:
    return value * (value - 1) // 2


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-pair-pencil-affine-line-cap-direction-router-v1",
        "schema",
    )
    n, m, K = data.get("n"), data.get("m"), data.get("K")
    s = data.get("pair_core_size")
    q = data.get("selected_type_floor")
    dim = data.get("scalar_dimension_cap")
    require((n, m, K) == (2097152, 1116048, 1048576), "official row")
    require((s, q, dim) == (m - 2, 520, 4), "input pins")
    line_cap = (n - (K - 1)) // (s - (K - 1))
    require(data.get("affine_line_cap") == line_cap == 15, "line cap")
    blocks, remainder = divmod(q, line_cap)
    require((data.get("full_line_blocks"), data.get("line_remainder")) == (blocks, remainder), "partition")
    pair_cap = blocks * choose2(line_cap) + choose2(remainder)
    require(data.get("pairs_per_projective_direction_cap") == pair_cap == 3615, "pair cap")
    directions = math.ceil(choose2(q) / pair_cap)
    require(data.get("projective_direction_floor") == directions == 38, "directions")
    roots = 2 * s - n
    require(data.get("direction_root_floor") == roots == 134940, "roots")
    require(data.get("dimension_outputs") == [2, 3, 4], "dimension outputs")
    require("not asserted" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    dependency = "rate_half_mca_rank11_pair_pencil_coprime_direction_normal_form"
    require(nodes.get(dependency, {}).get("status") == "PROVED", "dependency")
    return {"line": line_cap, "pairs": pair_cap, "directions": directions, "roots": roots}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("n", 2097151),
        lambda item: item.__setitem__("pair_core_size", 1116045),
        lambda item: item.__setitem__("selected_type_floor", 519),
        lambda item: item.__setitem__("affine_line_cap", 16),
        lambda item: item.__setitem__("full_line_blocks", 35),
        lambda item: item.__setitem__("pairs_per_projective_direction_cap", 3614),
        lambda item: item.__setitem__("projective_direction_floor", 37),
        lambda item: item.__setitem__("dimension_outputs", [1, 2, 3, 4]),
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
        print(f"PAIR_PENCIL_AFFINE_LINE_CAP_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "PAIR_PENCIL_AFFINE_LINE_CAP_PASS "
        f"line={checked['line']} pairs={checked['pairs']} "
        f"directions={checked['directions']} roots={checked['roots']}"
    )


if __name__ == "__main__":
    main()
