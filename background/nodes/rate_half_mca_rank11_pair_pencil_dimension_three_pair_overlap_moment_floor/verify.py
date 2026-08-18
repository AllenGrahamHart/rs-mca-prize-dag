#!/usr/bin/env python3
"""Verify the dimension-three pair-overlap moment floor."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "eef820acd53814309a2862a5328f8cf1aa3132b001109ed5dc0cdbc45a485aed"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def moment_gap(k_prime: int, q: int, n0: int, s0: int) -> tuple[int, int]:
    n_prime = n0 + k_prime
    incidence = q * (s0 + k_prime)
    average, remainder = divmod(incidence, n_prime)
    minimum = average * incidence - comb(average + 1, 2) * n_prime
    capacity = comb(q, 2) * (k_prime - 1)
    return capacity - minimum, average


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-dimension-three-pair-overlap-moment-floor-v1",
        "schema",
    )
    q = data.get("selected_pair_cores")
    n0 = data.get("residual_length_offset")
    s0 = data.get("residual_core_offset")
    require((q, n0, s0, data.get("pair_overlap_offset"),
             data.get("scalar_dimension")) == (520, 1048576, 67470, 1, 3),
            "input pins")
    intervals = data.get("average_floor_intervals")
    require(intervals == [[3, 1167, 33], [1168, 3331, 34],
                          [3332, 4835, 35]], "interval pins")
    previous = 2
    for start, stop, average in intervals:
        require(start == previous + 1 and stop >= start, "interval partition")
        for k_prime in range(start, stop + 1):
            gap, actual_average = moment_gap(k_prime, q, n0, s0)
            require(actual_average == average, f"average {k_prime}")
            require(gap < 0, f"excluded row {k_prime}")
        previous = stop

    last = data.get("last_excluded_residual_dimension")
    first = data.get("first_feasible_residual_dimension")
    require((last, first) == (4835, 4836), "adjacent rows")
    last_gap, _ = moment_gap(last, q, n0, s0)
    first_gap, _ = moment_gap(first, q, n0, s0)
    require(last_gap == -data.get("last_excluded_deficit") == -2110,
            "last deficit")
    require(first_gap == data.get("first_feasible_slack") == 115260,
            "first slack")

    kmax = data.get("residual_dimension_ceiling")
    require(kmax == 595763, "dimension ceiling")
    require(data.get("common_core_floor") == n0 - kmax == 452813, "core floor")
    require(data.get("common_core_ceiling") == n0 - first == 1043740,
            "core ceiling")
    payment_max = data.get("shared_payment_residual_ceiling")
    require(payment_max == 4922, "payment threshold")
    require(data.get("shared_payment_overlap_row_count") ==
            payment_max - first + 1 == 87, "payment overlap count")
    require("does not transport" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    parent = "rate_half_mca_rank11_pair_pencil_dimension_three_rich_plane_recurrence_sharpening"
    require(nodes.get(parent, {}).get("status") == "PROVED", "dependency")
    return {"last": last, "first": first, "deficit": -last_gap,
            "slack": first_gap, "rows": payment_max - first + 1}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("selected_pair_cores", 519),
        lambda item: item.__setitem__("pair_overlap_offset", 0),
        lambda item: item.__setitem__("average_floor_intervals",
                                      [[3, 1167, 33], [1168, 3331, 34], [3332, 4834, 35]]),
        lambda item: item.__setitem__("last_excluded_residual_dimension", 4834),
        lambda item: item.__setitem__("last_excluded_deficit", 2109),
        lambda item: item.__setitem__("first_feasible_residual_dimension", 4835),
        lambda item: item.__setitem__("first_feasible_slack", 115259),
        lambda item: item.__setitem__("common_core_ceiling", 1043739),
        lambda item: item.__setitem__("shared_payment_overlap_row_count", 86),
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
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256,
            "contract hash")
    data = json.loads(CONTRACT.read_text())
    checked = validate(data)
    if args.tamper_selftest:
        print(f"RANK11_D3_PAIR_MOMENT_TAMPER_PASS mutations={tamper_selftest(data)}/9")
        return
    print(
        "RANK11_D3_PAIR_MOMENT_PASS "
        f"last={checked['last']} deficit={checked['deficit']} "
        f"first={checked['first']} slack={checked['slack']} "
        f"payment_rows={checked['rows']}"
    )


if __name__ == "__main__":
    main()
