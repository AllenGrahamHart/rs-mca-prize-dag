#!/usr/bin/env python3
"""Small exact check for AQB entropy-ledger monotonicity."""

from __future__ import annotations

THRESHOLD = 429_645_547


def certified_net(positive_lower_bounds, cost_upper_bounds) -> int:
    return sum(positive_lower_bounds) - sum(cost_upper_bounds)


def accepts(ledger) -> bool:
    required = {
        "shared_entropy_lower",
        "charged_box_upper",
        "overlap_upper",
        "multiplicity_upper",
        "quotient_fiber_upper",
    }
    if set(ledger) != required:
        return False
    positives = [ledger["shared_entropy_lower"]]
    costs = [
        ledger["charged_box_upper"],
        ledger["overlap_upper"],
        ledger["multiplicity_upper"],
        ledger["quotient_fiber_upper"],
    ]
    return certified_net(positives, costs) >= THRESHOLD


def main() -> None:
    good = {
        "shared_entropy_lower": THRESHOLD + 1000,
        "charged_box_upper": 300,
        "overlap_upper": 200,
        "multiplicity_upper": 100,
        "quotient_fiber_upper": 50,
    }
    assert accepts(good)

    weak = dict(good)
    weak["shared_entropy_lower"] = THRESHOLD + 649
    assert not accepts(weak)

    missing = dict(good)
    missing.pop("overlap_upper")
    assert not accepts(missing)

    print("PASS: AQB entropy ledger soundness")


if __name__ == "__main__":
    main()
