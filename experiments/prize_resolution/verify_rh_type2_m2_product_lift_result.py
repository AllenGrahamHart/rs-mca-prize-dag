#!/usr/bin/env python3
"""Check the persisted aggregate for the bounded m=2 product-lift sweep."""

from __future__ import annotations

import json
from pathlib import Path


RESULT = Path(__file__).with_name("rh_type2_m2_product_lift_result.json")


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(RESULT.read_text())
    check((data["m"], data["domain_order"], data["rho"], data["supported_slopes"]) == (2, 32, 7, 9), "parameter tuple")
    check(data["field_order"] == 97 and (data["field_order"] - 1) % data["domain_order"] == 0, "field/domain")

    missing = {(0, 1), (0, 2), (3, 4), (5, 6), (7, 8)}
    edges = {(i, j) for i in range(9) for j in range(i + 1, 9)} - missing
    degrees = [sum(vertex in edge for edge in edges) for vertex in range(9)]
    degrees[0] += 1  # singleton supported root
    check(len(edges) == 31, "double-root row count")
    check(degrees == [7] * 9, "supported-slope degrees")
    check(2 * len(edges) + 1 == 9 * 7, "incidence total")

    worker_trials = data["worker_trials"]
    total = sum(worker_trials)
    check(len(worker_trials) == data["workers"] == 8, "worker count")
    check(total == data["total_trials"] == 599897, "trial total")
    check(data["rank_histogram"] == {"32": total}, "rank histogram")
    check(data["positive_nullity"] == 0, "positive-nullity mismatch")
    check(data["coordinate_live"] == 0, "coordinate-live mismatch")
    check(data["full_support_product_lifts"] == 0, "product survivor mismatch")
    check(data["hankel_compatible_lifts"] == 0, "Hankel survivor mismatch")
    check("ap-dPpY3BMeJ2K3jWxK879KVv" in data["run_url"], "run id")

    print(
        "RH_TYPE2_M2_PRODUCT_LIFT_RESULT_PASS "
        f"trials={total} rank32={data['rank_histogram']['32']} "
        f"product_lifts=0 hankel_lifts=0"
    )


if __name__ == "__main__":
    main()
