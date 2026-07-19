#!/usr/bin/env python3
"""Light schema check for DLI reduced-phase manifests."""

from __future__ import annotations


def verifies_polar_obstruction(p: int, reduced_pole_order: int) -> bool:
    return p > 1 and reduced_pole_order > 0 and reduced_pole_order % p != 0


def verify_manifest(universe: set[str], manifest: dict[str, dict], budget: int, p: int) -> None:
    assert set(manifest) == universe
    total = 0
    for key, row in manifest.items():
        assert row["tuple_id"] == key
        assert row["local_expansion"]
        assert verifies_polar_obstruction(p, row["reduced_pole_order"])
        assert 0 <= row["true_reduced_polar_degree"] <= row["majorant"]
        total += row["majorant"]
    assert total < budget


def main() -> None:
    universe = {"tau0", "tau1", "tau2"}
    manifest = {
        "tau0": {
            "tuple_id": "tau0",
            "local_expansion": "u^-3 + O(1)",
            "reduced_pole_order": 3,
            "true_reduced_polar_degree": 3,
            "majorant": 3,
        },
        "tau1": {
            "tuple_id": "tau1",
            "local_expansion": "u^-2 + O(1)",
            "reduced_pole_order": 2,
            "true_reduced_polar_degree": 2,
            "majorant": 3,
        },
        "tau2": {
            "tuple_id": "tau2",
            "local_expansion": "u^-1 + O(1)",
            "reduced_pole_order": 1,
            "true_reduced_polar_degree": 1,
            "majorant": 1,
        },
    }
    verify_manifest(universe, manifest, budget=8, p=5)
    print("PASS: DLI reduced-phase manifest schema supplies pole and majorant data")


if __name__ == "__main__":
    main()
