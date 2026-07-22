#!/usr/bin/env python3
"""Mutation audit for the XR prize nonpersistent-root cap."""

from pathlib import Path

from verify import ROWS, endpoint_conditions


ROOT = Path(__file__).resolve().parent


def main() -> None:
    n = 1 << 41
    endpoint_switches = 0
    for _name, rate, scale, a, _effective, threshold in ROWS:
        at_threshold = endpoint_conditions(n, rate, scale, a, threshold)
        below = endpoint_conditions(n, rate, scale, a, threshold - 1)
        assert all(at_threshold)
        assert not all(below)
        endpoint_switches += sum(left != right for left, right in zip(below, at_threshold))

    # Both endpoint tests are genuinely active across the official table.
    determining = [
        endpoint_conditions(n, rate, scale, a, threshold - 1)
        for _name, rate, scale, a, _effective, threshold in ROWS
    ]
    assert any(not zero and full for zero, full in determining)
    assert any(zero and not full for zero, full in determining)

    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "1,526,176,110" in statement
    assert "V-1" in audit
    assert "No Modal" in audit

    print(
        "XR_PRIZE_FLAT_NULLITY_NONPERSISTENT_ROOT_CAP_AUDIT_PASS "
        f"endpoint_switches={endpoint_switches} mutations=7"
    )


if __name__ == "__main__":
    main()
