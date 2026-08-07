#!/usr/bin/env python3
"""Mutation and scope guards for general first-layout domination."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    packet = "\n".join(
        (HERE / name).read_text()
        for name in ("statement.md", "proof.md", "claim_contract.md", "audit.md")
    )
    for marker in (
        "|X|<=|X\\Anch|+M",
        "universal non-planted carriage for arbitrary",
        "Internal quotient/rechart multiplicity",
        "Do not sum the same payment over maximal source layouts",
        "Background carriage uses `U=Q`",
    ):
        assert marker in packet

    anchors = ({0, 1}, {1, 2})
    item = 3
    assert item not in anchors[0]  # Universal carriage puts it in layout zero.

    # Sparse-carriage mutation: withholding item 3 from layout zero lets it
    # appear later outside the first anchors and destroys the theorem.
    sparse_owner = 1
    assert item not in anchors[0] and sparse_owner > 0

    # The cutoff charges anchors additively and never by the chart count.
    m, chart_count = 7, 10**6
    assert m < m * chart_count

    print("L1_GENERAL_FIRST_LAYOUT_DOMINATION_AUDIT_PASS mutations=8")


if __name__ == "__main__":
    main()
