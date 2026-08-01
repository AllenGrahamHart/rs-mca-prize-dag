#!/usr/bin/env python3
"""All loop-placement determinant cuts for positive three-loop packets."""

import importlib.util
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
KERNEL_SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_three_loop_common_kernel.py"
)


def load_kernel():
    specification = importlib.util.spec_from_file_location("common_kernel", KERNEL_SCRIPT)
    common_kernel = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(common_kernel)
    return common_kernel


def role_orbits(profile):
    """Quotient branch interchange acts on the three loop slots."""
    if profile == "442":
        assignments = {("H", "H", "L"), ("H", "L", "H"), ("L", "H", "H")}
    elif profile == "433":
        assignments = {("H", "L", "L"), ("L", "H", "L"), ("L", "L", "H")}
    else:
        raise ValueError(profile)
    unseen = set(assignments)
    orbits = []
    while unseen:
        representative = min(unseen)
        swapped = (representative[1], representative[0], representative[2])
        orbit = {representative, swapped}
        unseen -= orbit
        orbits.append(tuple(sorted(orbit)))
    return tuple(sorted(orbits))


def placement_cases():
    kernel = load_kernel()
    x, y, b, c = sp.symbols("x y b c")
    source_guard = x * y * (x - 1) * (x + 1) * (x - y) * (x + y) * (y - 1) * (y + 1)

    residual_442_root_low = (
        (y - x) * (b**2 - c**2)
        + b * x * y * (x + y) * (c**2 - 1)
    )
    residual_442_root_high = (
        (y - x) * (b**2 - c**2)
        + x
        * y
        * (
            x * (c - 1) * (b**2 + c)
            + y * (c + 1) * (b**2 - c)
        )
    )
    residual_433_root_low = (
        (y - x) * (b**2 - c**2)
        + (c - 1)
        * x
        * y
        * (b * (c + 1) * x - (b**2 + c) * y)
    )
    residual_433_root_high = (
        (b - c) * ((b + c) * y - (b * c + 1) * x)
        + x
        * y
        * (c - 1)
        * ((b**2 + c) * x - b * (c + 1) * y)
    )

    return {
        "442_root_low": (
            kernel.common_matrix(1, b, c, ((x, b, 1 + b), (y, -b, 1 - b))),
            -source_guard * (b - 1) * (b + 1),
            residual_442_root_low,
        ),
        "442_root_high": (
            kernel.common_matrix(1, b, c, ((x, c, 1 + c), (y, -c, 1 - c))),
            -source_guard * (c - 1) * (c + 1),
            residual_442_root_high,
        ),
        "433_root_low": (
            kernel.common_matrix(1, b, c, ((x, b, 1 + b), (y, c, 1 + c))),
            source_guard * (b + 1) * (c + 1),
            residual_433_root_low,
        ),
        "433_root_high": (
            kernel.common_matrix(1, b, c, ((x, c, 1 + c), (y, b * c, b + c))),
            source_guard * (b + c) * (c + 1),
            residual_433_root_high,
        ),
    }


def verify():
    orbit_counts = {profile: len(role_orbits(profile)) for profile in ("442", "433")}
    if orbit_counts != {"442": 2, "433": 2}:
        raise RuntimeError(f"placement orbits {orbit_counts}")

    cases = placement_cases()
    expected = {
        "442_root_low",
        "442_root_high",
        "433_root_low",
        "433_root_high",
    }
    if set(cases) != expected:
        raise RuntimeError("placement coverage")
    for name, (matrix, guards, residual) in cases.items():
        if sp.expand(matrix.det() - guards * residual) != 0:
            raise RuntimeError(f"{name} determinant")
        if sp.total_degree(residual) != 6:
            raise RuntimeError(f"{name} residual degree")
    return orbit_counts, cases


def main():
    orbit_counts, cases = verify()
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_PLACEMENT_ATLAS_PASS "
        f"orbits={sum(orbit_counts.values())} profiles={len(orbit_counts)} "
        f"cuts={len(cases)} residual_degrees="
        f"{','.join(str(sp.total_degree(case[2])) for case in cases.values())}"
    )


if __name__ == "__main__":
    main()
