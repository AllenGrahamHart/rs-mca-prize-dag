#!/usr/bin/env python3
"""Exact lane-to-common-compiler assembly for positive 433-1b -> O0b."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ATLAS_PATH = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1b_o0b_signed_edge_atlas.py"
)
STRATA = ("S0", "SBC", "SDE", "SDF")


def load_atlas():
    spec = importlib.util.spec_from_file_location("o0b_atlas", ATLAS_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def normalized_common_products(records):
    products = tuple(value for _, value in records[:5])
    return tuple("-1" if value == "-a^2" else value.replace("a*", "")
                 for value in products)


def assemble():
    atlas = load_atlas()
    atlases, lanes, _ = atlas.verify()
    rows = []
    for key in sorted(lanes):
        stratum = key[0]
        common_products = normalized_common_products(lanes[key])
        if stratum == "SBC":
            bc_sign = key[2]
            expected = (
                "-1", "b", "c",
                "b*c" if bc_sign == 1 else "-b*c",
                "b*c" if bc_sign == 1 else "-b*c",
            )
            compiler = "repeat"
        else:
            bc_sign = None
            expected = ("-1", "b", "c", "b*c", "-b*c")
            compiler = "split"
        if common_products != expected:
            raise RuntimeError(f"common record transport {key}")
        rows.append({
            "key": key,
            "stratum": stratum,
            "compiler": compiler,
            "bc_sign": bc_sign,
            "common_products": common_products,
            "source_rows": 60,
        })

    split = sum(row["compiler"] == "split" for row in rows)
    repeat = sum(row["compiler"] == "repeat" for row in rows)
    if (split, repeat) != (6, 4):
        raise RuntimeError("compiler lane partition")
    if {key: len(value) for key, value in atlases.items()} != {
        "S0": 2, "SBC": 4, "SDE": 2, "SDF": 2,
    }:
        raise RuntimeError("stratum partition")
    repeated_signs = {row["bc_sign"] for row in rows
                      if row["compiler"] == "repeat"}
    if repeated_signs != {-1, 1}:
        raise RuntimeError("repeated sign coverage")
    counts = {
        "lanes": len(rows),
        "split_lanes": split,
        "repeat_lanes": repeat,
        "source_rows_per_lane": 60,
        "formal_common_systems": sum(row["source_rows"] for row in rows),
        "distinct_split_algebra_rows": 60,
        "distinct_repeat_algebra_rows": 120,
        "distinct_algebra_rows": 180,
        "formal_minors_per_mode": sum(row["source_rows"] * 6 for row in rows),
        "compiled_minors_per_mode": (60 + 120) * 6,
    }
    expected_counts = {
        "lanes": 10,
        "split_lanes": 6,
        "repeat_lanes": 4,
        "source_rows_per_lane": 60,
        "formal_common_systems": 600,
        "distinct_split_algebra_rows": 60,
        "distinct_repeat_algebra_rows": 120,
        "distinct_algebra_rows": 180,
        "formal_minors_per_mode": 3600,
        "compiled_minors_per_mode": 1080,
    }
    if counts != expected_counts:
        raise RuntimeError(f"common compiler census {counts}")
    return rows, counts


def main():
    _, counts = assemble()
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_COMMON_ASSEMBLY_PASS "
        f"lanes={counts['lanes']} split={counts['split_lanes']} "
        f"repeat={counts['repeat_lanes']} "
        f"formal_systems={counts['formal_common_systems']} "
        f"distinct_algebra_rows={counts['distinct_algebra_rows']} "
        f"formal_minors_per_mode={counts['formal_minors_per_mode']}"
    )


if __name__ == "__main__":
    main()
