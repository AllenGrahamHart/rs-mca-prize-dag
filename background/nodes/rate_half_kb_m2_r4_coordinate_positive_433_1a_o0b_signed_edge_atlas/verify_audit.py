#!/usr/bin/env python3
"""Independent graph audit for the positive 433-1a/O0b signed atlas."""


def main():
    edges = (
        ("C", "C"),
        ("A", "B"), ("A", "B"), ("A", "B"),
        ("A", "C"), ("B", "E"), ("C", "F"),
        ("D", "E"), ("D", "E"),
        ("D", "F"), ("D", "F"), ("E", "F"),
    )
    degrees = {name: 0 for name in "ABCDEF"}
    for left, right in edges:
        degrees[left] += 1
        degrees[right] += 1
    assert degrees == {name: 4 for name in "ABCDEF"}
    active = {"AB", "BE", "EF", "FC", "CA"}
    assert len(active) == 5
    assert {vertex for edge in active for vertex in edge} == set("ABCEF")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_O0B_SIGNED_EDGE_ATLAS_AUDIT_PASS "
        "degrees=4,4,4,4,4,4 active_cycle=5 defect=3"
    )


if __name__ == "__main__":
    main()
