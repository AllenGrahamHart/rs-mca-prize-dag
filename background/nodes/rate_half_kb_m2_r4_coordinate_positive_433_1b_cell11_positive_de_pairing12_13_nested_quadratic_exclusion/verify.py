#!/usr/bin/env python3
"""Verify the cell-11 positive-DE pairing-12/13 packet."""

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
    "rate_half_kb_positive_433_1b_cell11_positive_de_pairing12_"
    "template_adapter_modal.py"
)
RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell11_positive_de_pairing12_"
    "template_adapter_result.json"
)
TEMPLATE = EXP / (
    "rate_half_kb_positive_433_1b_cell4_positive_de_pairing12_"
    "nested_quadratic_modal.py"
)
TOWER = EXP / "rate_half_kb_positive_433_1b_cell11_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
ROOT_SCRIPT = EXP / (
    "rate_half_kb_positive_433_1b_cell11_positive_de_pairing12_"
    "frobenius_roots_modal.py"
)
ROOT_RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell11_positive_de_pairing12_"
    "frobenius_roots_result.json"
)
PINNED = {
    SCRIPT: "de01f5cb386a0d4724d2afd94aaef359878d727dde9d1a64fa4a7b3d68fe2738",
    RESULT: "1917f5485206843967bea1eb2f673332ff16d73204110bf2ab2c0dc1b3d97bf1",
    TEMPLATE: "6fe230daa08afdd875015dbcba465e6b9781281831b8adcbb2d5dc160969d7b8",
    ROOT_SCRIPT: "cb6a7a7034f4c634ef2c8f09dd45feeb507d6f5143a9328e0d0bb08d8778b339",
    ROOT_RESULT: "5b046fa1c195c2f10cad3e15ac71c025554f009b5a12eb5bec14d67a7b246b74",
}
P = 2130706433
MATCHING = ((0, 5), (1, 2), (3, 4))


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
        == "rate-half-kb-positive-433-1b-cell11-positive-de-pairing12-adapter-v1"
        and payload["field"] == P
        and payload["source_template_sha256"] == digest(TEMPLATE)
        and payload["source_tower_sha256"] == digest(TOWER)
        and payload["source_kernel_sha256"] == digest(KERNEL),
        "packet custody",
    )
    expected_rows = set(itertools.product(
        itertools.product((-1, 1), repeat=2),
        itertools.product((-1, 1), repeat=2),
    ))
    seen = set()
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), tuple(row["sigma"]))
        require(key in expected_rows and key not in seen, "Cartesian row cover")
        seen.add(key)
        expected = (
            8,
            13 if row["epsilon"][1] == -1 else 12,
            10,
            2,
        )
        require(
            row["status"] == "COMPLETE" and row["excluded"]
            and row["xi_index"] == 0 and row["pairing_index"] == 12
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
    require(seen == expected_rows and len(payload["rows"]) == 16,
            "16-row cover")
    totals = tuple(
        sum(row[key] for row in payload["rows"])
        for key in ("target_root_count", "candidate_root_count",
                    "source_point_count", "route_point_count",
                    "uf_candidate_count", "colored_solution_count")
    )
    require(totals == (128, 200, 160, 160, 32, 0), "exact totals")
    finite = collections.Counter(
        item["status"] for row in payload["rows"] for item in row["finite_rows"]
    )
    boundary = collections.Counter(
        item["stage"] for row in payload["rows"] for item in row["boundary_rows"]
    )
    require(
        finite == {"CHECKED": 96, "MISSING_IMPOSSIBLE": 32,
                   "TARGET_PRODUCT_BOUNDARY": 32}
        and boundary == {"R_GUARD": 80, "T_GUARD": 32,
                         "CELL11_B_LEADING": 16,
                         "CELL11_C_LEADING": 16},
        "terminal partitions",
    )
    endings = collections.Counter(item["status"] for item in uf_rows(payload))
    require(endings == {"MISSING_RELATION_NONZERO": 224,
                        "COLORED_PAIR_NONZERO": 32}, "256 final uf rows")
    require(
        orbit((0, 12)) == {(0, 12), (0, 13), (1, 12), (1, 13)},
        "exact generic orbit",
    )
    manifest = json.loads((NODE / "node.json").read_text())
    require(manifest["node"]["id"] == NODE.name
            and manifest["node"]["status"] == "PROVED", "node manifest")
    print("PASS cell-11 positive-DE pairing 12/13: rows=16 candidates=200 uf=256")


if __name__ == "__main__":
    main()
