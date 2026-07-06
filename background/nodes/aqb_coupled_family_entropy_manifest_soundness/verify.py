#!/usr/bin/env python3
"""Light schema check for coupled AQB family/entropy manifests."""

from __future__ import annotations

SIGMA_STAR = 8_592_912_738
THRESHOLD = 429_645_547


def certified_net(ledger: dict) -> int:
    positives = [ledger["shared_entropy_lower"]]
    costs = [
        ledger["charged_box_upper"],
        ledger["overlap_upper"],
        ledger["multiplicity_upper"],
        ledger["quotient_fiber_upper"],
    ]
    return sum(positives) - sum(costs)


def verify_manifest(manifest: dict) -> None:
    assert manifest["sigma_star"] == SIGMA_STAR
    assert manifest["c"] == 2

    shared = manifest["shared"]
    assert shared["quotient_cell"]
    assert shared["fiber_data"]
    assert shared["reusable_box_charge"] is True

    members = manifest["members"]
    assert members
    member_ids = []
    for member in members:
        member_ids.append(member["id"])
        assert member["sigma_star"] == SIGMA_STAR
        assert member["c"] == 2
        assert member["quotient_cell"] == shared["quotient_cell"]
        assert member["transfer_witness"]
    assert len(set(member_ids)) == len(member_ids)

    ledger = manifest["ledger"]
    assert ledger["member_ids"] == member_ids
    assert ledger["quotient_cell"] == shared["quotient_cell"]
    assert certified_net(ledger) >= THRESHOLD


def main() -> None:
    toy = {
        "sigma_star": SIGMA_STAR,
        "c": 2,
        "shared": {
            "quotient_cell": "Q0",
            "fiber_data": {"fiber_rank": 40},
            "reusable_box_charge": True,
        },
        "members": [
            {
                "id": "w0",
                "sigma_star": SIGMA_STAR,
                "c": 2,
                "quotient_cell": "Q0",
                "transfer_witness": "L0",
            },
            {
                "id": "w1",
                "sigma_star": SIGMA_STAR,
                "c": 2,
                "quotient_cell": "Q0",
                "transfer_witness": "L1",
            },
        ],
        "ledger": {
            "member_ids": ["w0", "w1"],
            "quotient_cell": "Q0",
            "shared_entropy_lower": THRESHOLD + 1000,
            "charged_box_upper": 300,
            "overlap_upper": 200,
            "multiplicity_upper": 100,
            "quotient_fiber_upper": 50,
        },
    }
    verify_manifest(toy)
    print("PASS: coupled AQB family/entropy manifest schema is coherent")


if __name__ == "__main__":
    main()
