#!/usr/bin/env python3
"""Verify the cell-5 parallel-DE pairing-4/7/9/10 packet."""

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
    "rate_half_kb_positive_433_1b_cell5_de_pairing4_"
    "template_adapter_modal.py"
)
RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell5_de_pairing4_"
    "template_adapter_result.json"
)
TEMPLATE = EXP / (
    "rate_half_kb_positive_433_1b_cell4_de_pairing4_"
    "nested_quadratic_modal.py"
)
TOWER = EXP / "rate_half_kb_positive_433_1b_cell5_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell5_compact_kernel_result.json"
ROOT_SCRIPT = EXP / (
    "rate_half_kb_positive_433_1b_cell5_de_pairing4_"
    "frobenius_roots_modal.py"
)
ROOT_RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell5_de_pairing4_"
    "frobenius_roots_result.json"
)
PINNED = {
    SCRIPT: "1e53212a5bb99c0bbc42f7230f570544cbea4890ee3fc747a466e0567c846f11",
    RESULT: "3052812d26f144ab9fdd2a4a42d7521d982b51dff3695fd512954e48b435bb04",
    TEMPLATE: "86a51dc9a451980ff2f916fc7c249c7ab35c20a4a6a92d928577534df90c87c3",
    ROOT_SCRIPT: "39146a6b71ab18e39e92e7597de858d423d543a215169491c4b64d67aea2e532",
    ROOT_RESULT: "9fee2d13e3a79a7dd2404e1ce27c9414ad2cd143bdfe446f584e4d00fa056442",
}
P = 2130706433
MATCHING = ((0, 2), (1, 4), (3, 5))


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
        == "rate-half-kb-positive-433-1b-cell5-de-pairing4-adapter-v1"
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
    row_census = {0: (14, 20, 32, 8), 2: (9, 15, 20, 3)}
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), tuple(row["sigma"]), row["xi_index"])
        require(key in expected_rows and key not in seen, "Cartesian row cover")
        seen.add(key)
        expected = row_census[row["xi_index"]]
        require(
            row["status"] == "COMPLETE" and row["excluded"]
            and row["pairing_index"] == 4
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
    require(totals == (368, 560, 832, 832, 176, 0), "exact totals")
    finite = collections.Counter(
        item["status"] for row in payload["rows"] for item in row["finite_rows"]
    )
    boundary = collections.Counter(
        item["stage"] for row in payload["rows"] for item in row["boundary_rows"]
    )
    require(
        finite == {"CHECKED": 704, "MISSING_IMPOSSIBLE": 64,
                   "TARGET_PRODUCT_BOUNDARY": 64}
        and boundary == {"R_GUARD": 160, "T_GUARD": 128},
        "terminal partitions",
    )
    endings = collections.Counter(item["status"] for item in uf_rows(payload))
    require(endings == {"MISSING_RELATION_NONZERO": 1376,
                        "COLORED_PAIR_NONZERO": 128,
                        "TARGET_BOUNDARY": 48}, "1552 final uf rows")
    require(
        orbit((0, 4)) == {(0, 4), (0, 7), (1, 4), (1, 7)}
        and orbit((2, 4)) == {(2, 4), (2, 7), (2, 9), (2, 10)},
        "two exact generic orbits",
    )
    manifest = json.loads((NODE / "node.json").read_text())
    require(manifest["node"]["id"] == NODE.name
            and manifest["node"]["status"] == "PROVED", "node manifest")
    print("PASS cell-5 parallel-DE pairing 4/7/9/10: rows=32 candidates=560 uf=1552")


if __name__ == "__main__":
    main()
