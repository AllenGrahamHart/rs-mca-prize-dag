#!/usr/bin/env python3
"""Verify the profile-(4,4) official energy-at-most-four exclusion."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_profile44_official_energy_le4_exclusion"
PARENTS = {
    "e1_profile44_local_norm_route_fence",
    "e1_low_square_mass_weighted_kernel_dictionary",
}
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "unsafe_crossing_family_instantiation",
}
B_PRIZE = 317494674775468773183020924238786383963
EXPECTED_COUNTS = {
    "1": 126,
    "2": 7_812,
    "3": 317_688,
    "4": 9_530_766,
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def correlations(state: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    values = [0] * 64
    for index, (left, left_value) in enumerate(state):
        for right, right_value in state[index + 1 :]:
            delta = right - left
            if delta < 64:
                values[delta] += left_value * right_value
            elif delta > 64:
                values[128 - delta] -= left_value * right_value
    return tuple(values)


def validate(packet: dict[str, object], contract: dict[str, object]) -> None:
    row = packet["row"]
    assert int(row["p_lower"]) == B_PRIZE << 128
    assert int(row["p_upper"]) == ((B_PRIZE + 1) << 128) - 1
    assert row["cofactor_count"] == 1133
    assert row["cofactor_maximum"] == 1_704_448

    assert packet["energy_1_2"]["spectra"] == {
        "1": EXPECTED_COUNTS["1"],
        "2": EXPECTED_COUNTS["2"],
    }
    assert sum(packet["energy_1_2"]["valuation_counts"].values()) == 7_938
    assert packet["energy_1_2"]["viable"] == []
    assert packet["energy_3"]["shards"] == 16
    assert packet["energy_3"]["spectra"] == EXPECTED_COUNTS["3"]
    assert sum(packet["energy_3"]["valuation_counts"].values()) == EXPECTED_COUNTS["3"]
    assert packet["energy_3"]["viable"] == []
    assert packet["energy_4"]["shards"] == 128
    assert packet["energy_4"]["spectra"] == EXPECTED_COUNTS["4"]
    assert packet["energy_4"]["integer_multiple_interval_hits"] == 0
    assert packet["energy_4"]["viable"] == []

    for source in contract["sources"]:
        path = ROOT / source["path"]
        assert sha256(path) == source["sha256"]
    assert len(contract["sources"]) == 6


def main() -> None:
    node_dir = ROOT / "background/nodes" / NODE
    packet = json.loads((node_dir / "modal_certificate.json").read_text())
    contract = json.loads((node_dir / "source_contract.json").read_text())
    validate(packet, contract)

    assert EXPECTED_COUNTS == {
        "1": 63 * 2,
        "2": comb(63, 2) * 2**2,
        "3": comb(63, 3) * 2**3,
        "4": 63 * 2 + comb(63, 4) * 2**4,
    }

    witness = tuple(tuple(row) for row in packet["falsification"]["energy_two_witness"])
    corr = correlations(witness)
    assert sum(value * value for value in corr) == 2
    assert [(index, value) for index, value in enumerate(corr) if value] == [(60, 1), (62, 1)]
    assert sum(abs(value) == 1 for _, value in witness) == 4
    assert sum(abs(value) == 2 for _, value in witness) == 4

    for script_name, needles in {
        "profile44_abstract_energy12_norm_census_modal.py": (
            "assert len(rows) == 126 + 7812", "is_prime", "viable"
        ),
        "profile44_abstract_energy3_norm_census_modal.py": (
            "combinations(range(1, 64), 3)", "cofactor_map.get", "viable"
        ),
        "profile44_abstract_energy4_norm_census_modal.py": (
            "combinations(range(1, 64), 4)", "maximum_cofactor - minimum_cofactor <= 1",
            "interval_hits",
        ),
    }.items():
        text = (node_dir / "notes" / script_name).read_text()
        assert all(needle in text for needle in needles)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all((parent, NODE, "req") in edges for parent in PARENTS)
    assert all((NODE, target, "ev") in edges for target in TARGETS)

    controls = 0
    mutation = json.loads(json.dumps(packet))
    mutation["energy_4"]["spectra"] -= 1
    try:
        validate(mutation, contract)
    except AssertionError:
        controls += 1
    mutation = json.loads(json.dumps(packet))
    mutation["energy_3"]["viable"] = [{}]
    try:
        validate(mutation, contract)
    except AssertionError:
        controls += 1
    mutation_contract = json.loads(json.dumps(contract))
    mutation_contract["sources"][0]["sha256"] = "0" * 64
    try:
        validate(packet, mutation_contract)
    except AssertionError:
        controls += 1
    assert controls == 3

    print(
        "E1_PROFILE44_OFFICIAL_ENERGY_LE4_EXCLUSION_PASS "
        "spectra=9856392 energy_floor=5 controls=3/3"
    )


if __name__ == "__main__":
    main()
