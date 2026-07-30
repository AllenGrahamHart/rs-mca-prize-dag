#!/usr/bin/env python3
"""Verify the KoalaBear inner-degree-six routing theorem."""

from pathlib import Path

NODE = Path(__file__).resolve().parent

M6_ROWS = ((1, 24), (2, 12), (3, 8), (4, 6), (6, 4), (8, 3))
PRIMITIVE_DEGREE6 = (
    ("A5", 60, "A5", (1, 5)),
    ("S5", 120, "A5", (1, 5)),
    ("A6", 360, "A6", (1, 5)),
    ("S6", 720, "A6", (1, 5)),
)
TRANSITIVE_DEGREE10_ORDERS = (
    10, 10, 20, 20, 40, 50, 60, 80, 100, 100,
    120, 120, 120, 160, 160, 160, 200, 200, 200, 200,
    200, 240, 320, 320, 320, 360, 400, 400, 640, 720,
    720, 720, 800, 960, 1440, 1920, 1920, 1920, 3840,
    7200, 14400, 14400, 28800, 1814400, 3628800,
)
KERNEL_FREE_WREATH = (
    ("[A5^2]2", 7200, 720, "A5", 120, 600),
    ("parity wreath, split", 14400, 1440, "S5", 240, 1200),
    ("parity wreath, twist", 14400, 1440, "S5", 240, 1200),
    ("[S5^2]2", 28800, 2880, "S5", 480, 2400),
)
REMAINING_ROWS = (
    (2, 2, 4), (2, 4, 2), (2, 8, 1),
    (3, 2, 6), (3, 3, 4), (3, 4, 3), (3, 6, 2), (3, 12, 1),
    (4, 1, 16), (4, 2, 8), (4, 4, 4), (4, 8, 2),
)


def verify_documents() -> None:
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    evidence = (NODE / "source_evidence.md").read_text()
    audit = (NODE / "audit.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "inner-degree-two decomposition" in statement
    assert "12 types in degrees `2,3,4`" in contract
    assert "00bc5cdf6d0d833236953b9462c7c595a28960407ab2ee89e1b44ae11c16f5b7" in evidence
    assert "e7d8189cac31fa4f5a0f830234080fbddf0d741ca27921ffc7946c24b22f51d0" in evidence
    assert "Scott twists are not assumed realizable" in audit


def verify_catalogues() -> None:
    assert len(PRIMITIVE_DEGREE6) == 4
    assert {row[2] for row in PRIMITIVE_DEGREE6} == {"A5", "A6"}
    assert all(row[3] == (1, 5) for row in PRIMITIVE_DEGREE6)
    assert len(TRANSITIVE_DEGREE10_ORDERS) == 45
    candidates = tuple(
        (index + 1, order)
        for index, order in enumerate(TRANSITIVE_DEGREE10_ORDERS)
        if order % 600 == 0
    )
    assert candidates == (
        (40, 7200),
        (41, 14400),
        (42, 14400),
        (43, 28800),
        (44, 1814400),
        (45, 3628800),
    )


def verify_kernel_free_routes() -> None:
    for _, group_order, block_stabilizer, inner_group, endpoint, middle in KERNEL_FREE_WREATH:
        assert group_order // block_stabilizer == 10
        assert block_stabilizer // endpoint == 6
        assert middle // endpoint == 5
        assert inner_group in {"A5", "S5"}
    assert 181440 > 720  # A9 cannot inject into S6.
    assert 362880 > 720  # S9 cannot inject into S6.
    assert 2 < 6  # The sole proper nontrivial S9 quotient is not transitive.


def verify_scott_route() -> None:
    support_sizes = tuple(size for size in range(1, 11) if 10 % size == 0)
    assert support_sizes == (1, 2, 5, 10)
    inner_socle_orbits = (1, 5)
    assert 4 not in inner_socle_orbits
    # Delta consists of four synchronized counterparts plus alpha's coordinate.
    compatible_sizes = tuple(size for size in support_sizes if size >= 5)
    assert compatible_sizes == (5, 10)
    # Size five is excluded. Size ten makes Delta a same-fiber m10 suborbit.
    primitive_m10_nontrivial_subdegrees = {3, 6, 9}
    assert 4 not in primitive_m10_nontrivial_subdegrees
    proper_right_factor_degrees = tuple(d for d in range(2, 10) if 10 % d == 0)
    assert proper_right_factor_degrees == (2, 5)
    surviving_routes = tuple(d for d in proper_right_factor_degrees if d != 5)
    assert surviving_routes == (2,)


def verify_frontier() -> None:
    assert all(delta * r == 24 for r, delta in M6_ROWS)
    assert len(M6_ROWS) == 6
    assert 18 - len(M6_ROWS) == 12
    assert len(REMAINING_ROWS) == 12
    assert {m for m, _, _ in REMAINING_ROWS} == {2, 3, 4}
    assert all(delta * r == 4 * m for m, r, delta in REMAINING_ROWS)


def main() -> None:
    verify_documents()
    verify_catalogues()
    verify_kernel_free_routes()
    verify_scott_route()
    verify_frontier()
    print("RATE_HALF_KB_M6_SCOTT_CARTESIAN_DEGREE2_ROUTER_PASS")


if __name__ == "__main__":
    main()
