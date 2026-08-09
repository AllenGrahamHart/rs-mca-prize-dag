#!/usr/bin/env python3
"""Verify the cell-12 parallel-DE pairing-5/8/12/13 packet."""

import ast
import collections
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
SCRIPT = EXP / (
    "rate_half_kb_positive_433_1b_cell12_de_pairing5_"
    "template_adapter_modal.py"
)
RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell12_de_pairing5_"
    "template_adapter_result.json"
)
TEMPLATE = EXP / (
    "rate_half_kb_positive_433_1b_cell4_de_pairing5_"
    "nested_quadratic_modal.py"
)
TOWER = EXP / "rate_half_kb_positive_433_1b_cell12_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
ROOT_SCRIPT = EXP / (
    "rate_half_kb_positive_433_1b_cell12_de_pairing5_"
    "frobenius_roots_modal.py"
)
ROOT_RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell12_de_pairing5_"
    "frobenius_roots_result.json"
)
PINNED = {
    SCRIPT: "6661e0c1a8ca1a407300cf17b73d1ca863b59fb04b1d753f34eef8c7bc379ff8",
    RESULT: "2131dd306d2e3d85535d41f83973900ccdced33d3d289f1d465a94ab723b8c1a",
    TEMPLATE: "047d9b65d0d6ccdfef71113c782b383be88fbdc9ba0e15492a543a890b299969",
    ROOT_SCRIPT: "7d3884a4a42da3f7e290fa1d403e9c9a3ae512849ea88c1d859868092c7c4b91",
    ROOT_RESULT: "f0b074891e2f9ded97dff3ad9f8052ec9db5b96331a23bcb81863dbedbd75f25",
}
P = 2130706433
MATCHING = ((0, 2), (1, 5), (3, 4))


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


def uf_rows(payload):
    for row in payload["rows"]:
        for finite in row["finite_rows"]:
            yield from finite.get("uf_rows", [])


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
        payload["schema"]
        == "rate-half-kb-positive-433-1b-cell12-de-pairing5-adapter-v1"
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
    row_census = {0: (15, 22, 36, 4), 2: (13, 20, 32, 9)}
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), tuple(row["sigma"]), row["xi_index"])
        require(key in expected_rows and key not in seen, "Cartesian row cover")
        seen.add(key)
        expected = row_census[row["xi_index"]]
        require(
            row["status"] == "COMPLETE" and row["excluded"]
            and row["pairing_index"] == 5
            and tuple(map(tuple, row["matching"])) == MATCHING
            and (row["p_u_degree"], row["p_f_degree"],
                 row["uf_eliminant_degree"], row["remainder_degree"])
            == (2, 2, 8, 1)
            and (row["target_root_count"], row["candidate_root_count"],
                 row["source_point_count"], row["uf_candidate_count"])
            == expected
            and row["route_point_count"] == row["source_point_count"]
            and row["colored_solution_count"] == 0
            and not row["colored_solutions"]
            and not row["witnesses"] and not row["unresolved"],
            "complete row terminal",
        )
    require(seen == expected_rows and len(payload["rows"]) == 32,
            "32-row cover")
    totals = tuple(
        sum(row[key] for row in payload["rows"])
        for key in ("target_root_count", "candidate_root_count",
                    "source_point_count", "route_point_count",
                    "uf_candidate_count", "colored_solution_count")
    )
    require(totals == (448, 672, 1088, 1088, 208, 0), "exact totals")
    finite = collections.Counter(
        item["status"] for row in payload["rows"] for item in row["finite_rows"]
    )
    boundary = collections.Counter(
        item["stage"] for row in payload["rows"] for item in row["boundary_rows"]
    )
    require(
        finite == {"CHECKED": 896, "MISSING_IMPOSSIBLE": 96,
                   "TARGET_PRODUCT_BOUNDARY": 96}
        and boundary == {"R_GUARD": 160, "T_GUARD": 128,
                         "CELL12_B_LEADING": 32},
        "terminal partitions",
    )
    endings = collections.Counter(item["status"] for item in uf_rows(payload))
    require(endings == {"MISSING_RELATION_NONZERO": 1472,
                        "COLORED_PAIR_NONZERO": 160,
                        "TARGET_BOUNDARY": 48}, "1680 final uf rows")
    require(
        orbit((0, 5)) == {(0, 5), (0, 8), (1, 5), (1, 8)}
        and orbit((2, 5)) == {(2, 5), (2, 8), (2, 12), (2, 13)},
        "two exact generic orbits",
    )
    manifest = json.loads((NODE / "node.json").read_text())
    require(manifest["node"]["id"] == NODE.name
            and manifest["node"]["status"] == "PROVED", "node manifest")
    print("PASS cell-12 parallel-DE pairing 5/8/12/13: rows=32 candidates=672 uf=1680")


if __name__ == "__main__":
    main()
