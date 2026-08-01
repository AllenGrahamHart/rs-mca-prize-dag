#!/usr/bin/env python3
"""Verify all eight branches of the zero-loop 433 cell-13 classifier."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / (
    "experiments/prize_resolution/rate_half_kb_zero_loop_433_cell1314_router.py"
)


EXPECTED = {
    (1, 1, "minus"): (
        (1061119412, 2122238824, 583634928, 407713360),
        (1069587021, 8467609, 1547071499, 1756416433),
    ),
    (1, 1, "plus"): (
        (8467609, 1069587021, 583634928, 407713360),
        (2122238824, 1061119412, 1547071499, 1756416433),
    ),
    (1, -1, "minus"): (),
    (1, -1, "plus"): (),
    (-1, 1, "minus"): (),
    (-1, 1, "plus"): (),
    (-1, -1, "minus"): (
        (1069587021, 8467609, 583634928, 365822393),
        (1061119412, 2122238824, 1547071499, 1731460684),
    ),
    (-1, -1, "plus"): (
        (2122238824, 1061119412, 583634928, 365822393),
        (8467609, 1069587021, 1547071499, 1731460684),
    ),
}


def main():
    specification = importlib.util.spec_from_file_location("router", SCRIPT)
    router = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(router)
    total = 0
    for key, expected in EXPECTED.items():
        epsilon_1, epsilon_2, branch = key
        route = router.compile_branch(13, epsilon_1, epsilon_2, branch)
        packets, candidates = router.reconstruct(
            13, epsilon_1, epsilon_2, branch, route
        )
        router.audit_route(route)
        if packets != expected:
            raise RuntimeError(f"{key} packets {packets}")
        if route["kind"] == "finite" and (
            route["residual"].degree(), route["root_gcd"].degree()
        ) != (2, 2):
            raise RuntimeError(f"{key} residual")
        if route["kind"] == "guarded_empty" and candidates:
            raise RuntimeError(f"{key} obstruction candidates")
        total += len(packets)
    if total != 8:
        raise RuntimeError("cell-13 total")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_BC_SINGLETON_CELL13_PASS "
        "branches=8 packets=8 opposite_rows=empty"
    )


if __name__ == "__main__":
    main()
