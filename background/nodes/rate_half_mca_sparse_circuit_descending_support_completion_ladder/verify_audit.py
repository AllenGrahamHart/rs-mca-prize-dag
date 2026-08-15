#!/usr/bin/env python3
"""Independent audit of the descending-support completion partition."""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def independent_label(values: tuple[int, ...], q: int) -> tuple[int, int] | None:
    for source, maximum in zip((5, 4, 3, 2), values):
        for defect in range(10 - source):
            if maximum == q - defect:
                return source, defect
        require(maximum <= q - (10 - source), "stage partition")
    return None


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    require(p["source_order"] == [5, 4, 3, 2], "order")
    counts: dict[str, int] = {}
    assignments = 0
    for q in (8, 9, 11):
        for values in product(range(q + 1), repeat=4):
            leaf = independent_label(values, q)
            name = "all_fallback" if leaf is None else f"c{leaf[0]}_defect_{leaf[1]}"
            counts[name] = counts.get(name, 0) + 1
            assignments += 1
    require(len(counts) == p["total_leaf_count"] == 27, "leaf census")

    target_checks = 0
    for source in p["source_order"]:
        for defect in p["terminal_defects"][str(source)]:
            valid = []
            for target in range(2, 10):
                left = source + (defect + 1) * target - defect - 1
                carrier_without_q = source - 1 + defect * (target - 1)
                require((left <= 10) == (carrier_without_q + target <= 10), "union")
                if left <= 10:
                    valid.append(target)
                target_checks += 1
            require(valid, "each terminal controls a target")
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_DESCENDING_SUPPORT_COMPLETION_LADDER_AUDIT_PASS "
        f"assignments={assignments} leaves={len(counts)} target_checks={target_checks}"
    )


if __name__ == "__main__":
    main()
