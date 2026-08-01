#!/usr/bin/env python3
"""Verify all eight branches of the zero-loop 433 cell-12 classifier."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / (
    "experiments/prize_resolution/rate_half_kb_zero_loop_433_cell12_router.py"
)


EXPECTED = {
    (1, 1, "cy"): (
        (1361855312, 1859271856, 1587494773, 1299348518),
        (1859271856, 1361855312, 1608564875, 823002076),
    ),
    (1, 1, "cdivy"): (
        (271434577, 768851121, 1587494773, 1299348518),
        (768851121, 271434577, 1608564875, 823002076),
    ),
    (1, -1, "cy"): (
        (33423358, 1056997377, 1056997377, 8355839),
        (1073709056, 2097283075, 2097283075, 16711678),
    ),
    (1, -1, "cdivy"): (
        (1056997377, 33423358, 1056997377, 8355839),
        (2097283075, 1073709056, 2097283075, 16711678),
    ),
    (-1, 1, "cy"): (
        (1056997377, 33423358, 33423358, 2113994753),
        (2097283075, 1073709056, 1073709056, 2122350593),
    ),
    (-1, 1, "cdivy"): (
        (33423358, 1056997377, 33423358, 2113994753),
        (1073709056, 2097283075, 1073709056, 2122350593),
    ),
    (-1, -1, "cy"): (
        (271434577, 768851121, 1608564875, 263421243),
        (768851121, 271434577, 1587494773, 1875641030),
    ),
    (-1, -1, "cdivy"): (
        (1361855312, 1859271856, 1608564875, 263421243),
        (1859271856, 1361855312, 1587494773, 1875641030),
    ),
}


def main():
    specification = importlib.util.spec_from_file_location("router", SCRIPT)
    router = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(router)
    total = 0
    for key, expected in EXPECTED.items():
        epsilon_1, epsilon_2, branch = key
        route = router.compile_branch(epsilon_1, epsilon_2, branch)
        packets, candidates = router.reconstruct(
            epsilon_1, epsilon_2, branch, route
        )
        router.audit_lost(route)
        if packets != expected:
            raise RuntimeError(f"{key} packets {packets}")
        if route["eliminant"].degree() not in (12, 16):
            raise RuntimeError(f"{key} eliminant")
        if route["root_gcd"].degree() not in (5, 6):
            raise RuntimeError(f"{key} root gcd")
        if len(candidates) < len(packets):
            raise RuntimeError(f"{key} candidates")
        total += len(packets)
    if total != 16:
        raise RuntimeError("cell-12 total")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_BC_SINGLETON_CELL12_PASS "
        "branches=8 packets=16"
    )


if __name__ == "__main__":
    main()
