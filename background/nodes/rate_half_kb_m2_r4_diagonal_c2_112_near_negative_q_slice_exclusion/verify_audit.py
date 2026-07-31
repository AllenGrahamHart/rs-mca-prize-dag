#!/usr/bin/env python3
"""Independent standard-library reconstruction of the near constant gate."""

from fractions import Fraction as F
import importlib.util
from pathlib import Path

from verify_runner import HELPERS, check_hashes


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_source():
    spec = importlib.util.spec_from_file_location(
        "aligned_negative_audit_source", HELPERS["audit_source"]
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("audit source import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def near_mismatch(source, template, c, d, w, xi):
    aligned = source.mismatch(template, c, d, w)
    aligned_crossing = source.multiply([-1 / c, F(1)], [-1 / d, F(1)])
    aligned_target = source.monic(
        source.multiply(aligned_crossing, aligned_crossing)
    )
    observed = source.add(aligned, aligned_target)
    near_crossing = source.multiply([-1 / xi, F(1)], [-1 / d, F(1)])
    near_target = source.monic(source.multiply(near_crossing, near_crossing))
    return source.add(observed, source.scale(near_target, -1))


def main():
    check_hashes()
    source = load_source()
    fixtures = ((F(3), F(7), F(5)), (F(4), F(6), F(9)))
    checks = 0
    for c, d, w in fixtures:
        p = c * d - 2 * c - 2 * d + 1
        q = 2 * c * d - c - d + 2
        b = -q / p
        for xi in (F(2), F(1, 2), b):
            fixed = near_mismatch(
                source, "fixed-moving", c, d, w, xi
            )
            moving = near_mismatch(
                source, "moving-moving", c, d, w, xi
            )
            require(fixed == moving, "template q-slice equality")
            require(fixed[0] == 1 - 1 / (xi * xi * d * d),
                    "near constant mismatch")
            checks += 1
    print(
        "KB_C2_112_NEAR_NEGATIVE_AUDIT_PASS "
        f"exact_fixtures={checks} templates=2 xi_orbits=3"
    )


if __name__ == "__main__":
    main()
