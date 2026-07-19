#!/usr/bin/env python3
"""Lightweight schema check for AQB averaged-family certificates."""

from __future__ import annotations

SIGMA_STAR = 8_592_912_738


def verify_certificate(cert: dict) -> None:
    assert cert["sigma_star"] == SIGMA_STAR
    assert cert["c"] == 2
    members = cert["members"]
    assert isinstance(members, list)
    assert members

    shared = cert["shared"]
    assert shared["quotient_cell"]
    assert shared["fiber_data"]
    assert shared["reusable_box_charge"] is True

    seen = set()
    for member in members:
        ident = member["id"]
        assert ident not in seen
        seen.add(ident)
        assert member["c"] == 2
        assert member["sigma_star"] == SIGMA_STAR
        assert member["quotient_cell"] == shared["quotient_cell"]
        assert member["transfer_witness"]


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
                "c": 2,
                "sigma_star": SIGMA_STAR,
                "quotient_cell": "Q0",
                "transfer_witness": "L0",
            },
            {
                "id": "w1",
                "c": 2,
                "sigma_star": SIGMA_STAR,
                "quotient_cell": "Q0",
                "transfer_witness": "L1",
            },
        ],
    }
    verify_certificate(toy)
    print("PASS: AQB averaged-family certificate schema is coherent")


if __name__ == "__main__":
    main()
