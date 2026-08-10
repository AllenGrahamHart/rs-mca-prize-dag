#!/usr/bin/env python3
"""Verify the cell-11 parallel-DE pairing-3/6 packet."""

import ast
import collections
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_de_pairing3_template_adapter_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_de_pairing3_template_adapter_result.json"
TEMPLATE = EXP / "rate_half_kb_positive_433_1b_cell4_de_pairing3_nested_quadratic_modal.py"
TOWER = EXP / "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
ROOT_SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell11_de_pairing3_independent_roots_modal.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_de_pairing3_independent_roots_result.json"
PINNED = {
    SCRIPT: "dd4cf944fdb3ca216a8414a2c17ba43107920bdf763a848bd1b23f55eb57e962",
    RESULT: "6c1319f7113f5dd60798cc09e71f5af31e73c30ddf86829c12294c12872e9965",
    TEMPLATE: "9e3b21a458b5405051fca1ad7cabd9f6b07b09bf1e44bed358e80f4254d69d5c",
    ROOT_SCRIPT: "0e22b424869d374d715863e7357110cb5bed8d572fde2f644caec62146e5356d",
    ROOT_RESULT: "47079f4527e61e385274c419b8bd798840933c8b1ba1fee7f152adc9878611da",
}
P = 2130706433
MATCHING = ((0, 2), (1, 3), (4, 5))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    for index in range(1, len(values)):
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((values[0], values[index]),) + tail


def orbit(seed):
    matchings = tuple(pairings(range(6)))
    lookup = {
        tuple(sorted(tuple(sorted(edge)) for edge in matching)): index
        for index, matching in enumerate(matchings)
    }
    permutations = ((1, 0, 2, 3, 4, 5, 6), (0, 1, 2, 4, 3, 5, 6))

    def act(label, permutation):
        xi, pairing = label
        old = tuple(index for index in range(7) if index != xi)
        new_xi = permutation[xi]
        new = tuple(index for index in range(7) if index != new_xi)
        compact = {value: index for index, value in enumerate(new)}
        image = tuple(sorted(
            tuple(sorted((compact[permutation[old[left]]],
                          compact[permutation[old[right]]])))
            for left, right in matchings[pairing]
        ))
        return new_xi, lookup[image]

    output = {seed}
    queue = [seed]
    while queue:
        label = queue.pop()
        for permutation in permutations:
            image = act(label, permutation)
            if image not in output:
                output.add(image)
                queue.append(image)
    return output


def f_rows(payload):
    for row in payload["rows"]:
        for finite in row["finite_rows"]:
            for uv_row in finite.get("uv_rows", []):
                yield from uv_row.get("f_rows", [])


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"hash drift: {path.name}")
    source = SCRIPT.read_text()
    ast.parse(source)
    require(
        "function.decorator_list = []" in source
        and 'node.name == "evaluate_case"' in source
        and 'compile(module, REMOTE_TEMPLATE, "exec")' in source,
        "AST adapter boundary",
    )
    payload = json.loads(RESULT.read_text())
    require(
        payload["schema"] == "rate-half-kb-positive-433-1b-cell11-de-pairing3-adapter-v1"
        and payload["field"] == P
        and payload["source_template_sha256"] == digest(TEMPLATE)
        and payload["source_tower_sha256"] == digest(TOWER)
        and payload["source_kernel_sha256"] == digest(KERNEL),
        "packet custody",
    )
    expected_rows = set(itertools.product(
        itertools.product((-1, 1), repeat=2),
        itertools.product((-1, 1), repeat=2),
        (0, 2),
    ))
    seen = set()
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), tuple(row["sigma"]), row["xi_index"])
        require(key in expected_rows and key not in seen, "Cartesian row cover")
        seen.add(key)
        special = row["xi_index"] == 2 and row["sigma"][1] == -1
        expected = (
            9 if special else 5,
            (10 if row["epsilon"][1] == -1 else 9) + (4 if special else 0),
            16 if special else 4,
            16 if special else 0,
        )
        require(
            row["status"] == "COMPLETE" and row["excluded"]
            and row["pairing_index"] == 3
            and tuple(map(tuple, row["matching"])) == MATCHING
            and (row["p_u_degree"], row["p_v_degree"],
                 row["nested_quartic_degree"], row["remainder_degree"])
                == (2, 2, 4, 1)
            and (row["target_root_count"], row["candidate_root_count"],
                 row["source_point_count"], row["uv_candidate_count"])
                == expected
            and row["route_point_count"] == row["source_point_count"]
            and row["colored_solution_count"] == 0
            and not row["colored_solutions"] and not row["witnesses"]
            and not row["unresolved"],
            "complete row terminal",
        )
    require(seen == expected_rows and len(payload["rows"]) == 32, "32-row cover")
    totals = tuple(sum(row[key] for row in payload["rows"]) for key in (
        "target_root_count", "candidate_root_count", "source_point_count",
        "route_point_count", "uv_candidate_count", "colored_solution_count",
    ))
    require(totals == (192, 336, 224, 224, 128, 0), "exact totals")
    finite = collections.Counter(
        item["status"] for row in payload["rows"] for item in row["finite_rows"]
    )
    boundary = collections.Counter(
        item["stage"] for row in payload["rows"] for item in row["boundary_rows"]
    )
    require(finite == {"CHECKED": 96, "MISSING_IMPOSSIBLE": 64,
                       "TARGET_PRODUCT_BOUNDARY": 64}
            and boundary == {"R_GUARD": 160, "T_GUARD": 64,
                             "CELL11_B_LEADING": 32,
                             "CELL11_C_LEADING": 32},
            "terminal partitions")
    endings = collections.Counter(item["status"] for item in f_rows(payload))
    require(endings == {"COLORED_PAIR_NONZERO": 256}, "256 final f rows")
    require(orbit((0, 3)) == {(0, 3), (0, 6), (1, 3), (1, 6)}
            and orbit((2, 3)) == {(2, 3), (2, 6)},
            "two exact generic orbits")
    manifest = json.loads((NODE / "node.json").read_text())
    require(manifest["node"]["id"] == NODE.name
            and manifest["node"]["status"] == "PROVED", "node manifest")
    print("PASS cell-11 parallel-DE pairing 3/6: rows=32 candidates=336 f=256")


if __name__ == "__main__":
    main()
