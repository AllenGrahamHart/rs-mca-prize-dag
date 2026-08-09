#!/usr/bin/env python3
"""Verify the cell-5 positive-DE pairing-12/13 packet."""

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
    "rate_half_kb_positive_433_1b_cell5_positive_de_pairing12_"
    "template_adapter_modal.py"
)
RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell5_positive_de_pairing12_"
    "template_adapter_result.json"
)
TEMPLATE = EXP / (
    "rate_half_kb_positive_433_1b_cell4_positive_de_pairing12_"
    "nested_quadratic_modal.py"
)
TOWER = EXP / "rate_half_kb_positive_433_1b_cell5_four_basis_tower_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell5_compact_kernel_result.json"
ROOT_SCRIPT = EXP / (
    "rate_half_kb_positive_433_1b_cell5_positive_de_pairing12_"
    "frobenius_roots_modal.py"
)
ROOT_RESULT = EXP / (
    "rate_half_kb_positive_433_1b_cell5_positive_de_pairing12_"
    "frobenius_roots_result.json"
)
AUDIT_REPLAY = EXP / (
    "rate_half_kb_positive_433_1b_cell5_positive_de_pairing12_audit_replay.json"
)
PINNED = {
    SCRIPT: "556ec39c43db9d803da7485d0c5291e6adb97856c5c6f1c4b41ae15d5b097d67",
    RESULT: "16d8f89e73c15b62dd2221118acabf6920fe3967d9e5132325c55add8e1e1761",
    TEMPLATE: "6fe230daa08afdd875015dbcba465e6b9781281831b8adcbb2d5dc160969d7b8",
    ROOT_SCRIPT: "fb819db43fa3ca473dfdce427f61f7db5b8b732e1dca32dc1fc3f453f4b8f545",
    ROOT_RESULT: "8361e6c2e0eb2f0912e3fba40a4245573e1b917011e8e40a9c3585da473cbd9f",
    AUDIT_REPLAY: "5411a15a6c6424f3a76ff7d76faaf3905c98487dc738a1c4129c96bb8f60a93d",
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
        == "rate-half-kb-positive-433-1b-cell5-positive-de-pairing12-adapter-v1"
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
        require(
            row["status"] == "COMPLETE" and row["excluded"]
            and row["xi_index"] == 0 and row["pairing_index"] == 12
            and tuple(map(tuple, row["matching"])) == MATCHING
            and (row["p_u_degree"], row["p_f_degree"],
                 row["uf_eliminant_degree"], row["remainder_degree"])
            == (2, 2, 8, 1)
            and (row["target_root_count"], row["candidate_root_count"],
                 row["source_point_count"], row["uf_candidate_count"])
            == (13, 19, 36, 6)
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
    require(totals == (208, 304, 576, 576, 96, 0), "exact totals")
    finite = collections.Counter(
        item["status"] for row in payload["rows"] for item in row["finite_rows"]
    )
    boundary = collections.Counter(
        item["stage"] for row in payload["rows"] for item in row["boundary_rows"]
    )
    require(
        finite == {"CHECKED": 512, "MISSING_IMPOSSIBLE": 32,
                   "TARGET_PRODUCT_BOUNDARY": 32}
        and boundary == {"R_GUARD": 80, "T_GUARD": 64},
        "terminal partitions",
    )
    endings = collections.Counter(item["status"] for item in uf_rows(payload))
    require(endings == {"MISSING_RELATION_NONZERO": 960,
                        "COLORED_PAIR_NONZERO": 96}, "1056 final uf rows")
    require(
        orbit((0, 12)) == {(0, 12), (0, 13), (1, 12), (1, 13)},
        "exact generic orbit",
    )
    replay = json.loads(AUDIT_REPLAY.read_text())
    require(replay["complete"] and replay["counts"] == {
        "FAIL": 0, "HASH_MISMATCH": 0, "PASS": 1,
        "REMOTE_ERROR": 0, "TIMEOUT": 0,
    } and len(replay["results"]) == 1
        and replay["results"][0]["status"] == "PASS"
        and replay["results"][0]["sha256"]
        == digest(NODE / "verify_audit.py"), "Modal audit receipt")
    manifest = json.loads((NODE / "node.json").read_text())
    require(manifest["node"]["id"] == NODE.name
            and manifest["node"]["status"] == "PROVED", "node manifest")
    print("PASS cell-5 positive-DE pairing 12/13: rows=16 candidates=304 uf=1056")


if __name__ == "__main__":
    main()
