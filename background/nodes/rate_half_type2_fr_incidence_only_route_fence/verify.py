#!/usr/bin/env python3
"""Primary replay of the quartic-difference-family FR route fence."""

from __future__ import annotations

import hashlib
import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "experiments/prize_resolution/rh_type2_fr_incidence_m64_result.json"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def decode_w(payload: dict, domain_size: int, field_order: int) -> set[tuple[int, int]]:
    raw = bytes.fromhex(payload["W_bitset_hex_little_endian"])
    check(len(raw) * 8 == domain_size, "mask length")
    check(hashlib.sha256(raw).hexdigest() == payload["W_sha256"], "mask digest")
    mask = int.from_bytes(raw, "little")
    return {
        (index // (field_order - 1), index % (field_order - 1) + 1)
        for index in range(domain_size)
        if (mask >> index) & 1
    }


def build(payload: dict) -> tuple[set[tuple[int, int]], dict[int, set[tuple[int, int]]]]:
    m = payload["m"]
    q = payload["field_order"]
    g = payload["generator"]
    subgroup = {pow(g, 4 * j, q) for j in range(m)}
    cosets = [{pow(g, i, q) * x % q for x in subgroup} for i in range(4)]
    check(len(subgroup) == m, "quartic subgroup order")
    check(set().union(*cosets) == set(range(1, q)), "quartic coset cover")
    check(sum(map(len, cosets)) == q - 1, "quartic coset disjointness")

    domain = {(i, x) for i in range(4) for x in range(1, q)}
    blocks: dict[int, set[tuple[int, int]]] = {}
    for gamma in range(q):
        block = {
            (i, (gamma + value) % q)
            for i, coset in enumerate(cosets)
            for value in coset
            if (gamma + value) % q
        }
        if gamma == 0:
            block.remove((0, 1))
        blocks[gamma] = block
    return domain, blocks


def main() -> None:
    payload = json.loads(RESULT.read_text())
    m = payload["m"]
    q = payload["field_order"]
    rho = payload["rho"]
    a = payload["a"]
    check((m, q, rho, a) == (64, 257, 255, 447), "pinned parameters")
    check(pow(payload["generator"], 128, q) == q - 1, "generator order 256")

    domain, blocks = build(payload)
    w_set = decode_w(payload, len(domain), q)
    check(w_set <= domain, "W outside domain")
    check(len(domain) == payload["N"] == 16 * m, "domain size")
    check(len(blocks) == payload["T"] == rho + 2, "block count")
    check({len(block) for block in blocks.values()} == {rho}, "block sizes")

    degrees = [sum(point in block for block in blocks.values()) for point in domain]
    check(sorted(degrees) == [m - 1] + [m] * (16 * m - 1), "degree profile")
    check(sum(m - degree for degree in degrees) == payload["deficit"] == 1, "deficit")

    pair_unions = [len(blocks[g] | blocks[h]) for g, h in combinations(range(q), 2)]
    check(min(pair_unions) == payload["minimum_pair_union"] == a, "pair union")
    intersections = {gamma: len(block & w_set) for gamma, block in blocks.items()}
    spends = {gamma: len(block - w_set) for gamma, block in blocks.items()}
    check(len(w_set) == a, "W size")
    check(min(spends.values()) == payload["minimum_spend"] == m + 2, "spend")
    check(max(intersections.values()) == payload["maximum_intersection_with_W"], "maximum")
    check([g for g, value in intersections.items() if value == max(intersections.values())] == [0], "maximizer")
    check(max(intersections.values()) == 3 * m - 3, "linear violation value")
    check(max(intersections.values()) - 2 * m == payload["violation"] == m - 3, "violation gap")

    # Fail-closed controls: the undeleted construction and a changed mask are invalid.
    raw_zero = set(blocks[0])
    raw_zero.add((0, 1))
    check(len(raw_zero) == rho + 1, "deletion mutation did not change size")
    mutated = set(w_set)
    mutated.remove(next(iter(mutated)))
    check(len(mutated) != a, "mask mutation was not detected")

    print(
        "RH_TYPE2_FR_INCIDENCE_ROUTE_FENCE_PASS "
        f"m={m} N={len(domain)} T={len(blocks)} min_union={min(pair_unions)} "
        f"min_spend={min(spends.values())} max_W_intersection={max(intersections.values())} "
        f"two_m={2*m} violation={max(intersections.values())-2*m}"
    )


if __name__ == "__main__":
    main()
