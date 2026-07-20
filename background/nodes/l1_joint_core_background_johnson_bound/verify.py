#!/usr/bin/env python3
"""Verify the joint core/background Johnson bound and exact boundaries."""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(name: str, relative: str):
    path = ROOT / relative / "verify.py"
    spec = spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


V17 = load("l1_joint_f17", "l1_background_overlap_singleton_payment")
V23 = load("l1_joint_f23", "l1_cross_quotient_split_descent_obstruction")


def f17_sharp_fixture() -> tuple[int, int, int]:
    p_0 = V17.check_pair(V17.D0, V17.F0, V17.W0)
    p_1 = V17.check_pair(V17.D1, V17.F1, V17.W1)
    assert p_0 != p_1

    delta = V17.sub(V17.mul(V17.W0, V17.F1), V17.mul(V17.W1, V17.F0))
    common_defect = set(V17.D0) & set(V17.D1)
    common_background = set(V17.BACKGROUND)
    assert not common_defect
    assert all(
        V17.evaluate(delta, point) == 0
        for point in V17.SUPPORT + V17.BACKGROUND
    )

    n_core = len(V17.CORE)
    d = len(V17.D0)
    h = len(V17.SUPPORT)
    b = len(V17.BACKGROUND)
    s = h - d
    u = V17.ELL - s
    r = 2 * d - h
    assert len(common_defect) + len(common_background) <= r
    joint = b * d * d + n_core * u * u - n_core * b * r
    numerator = n_core * b * V17.ELL
    assert (joint, numerator // joint) == (4, 2)
    return 2, joint, r


def f23_zero_fixture() -> tuple[int, int, int]:
    V23.check_pair(V23.D0, V23.F0, V23.W0)
    V23.check_pair(V23.D1, V23.F1, V23.W1)
    delta = V23.sub(V23.mul(V23.W0, V23.F1), V23.mul(V23.W1, V23.F0))
    common_defect = set(V23.D0) & set(V23.D1)
    common_background = set(V23.BACKGROUND)
    assert not common_defect
    assert all(
        V23.evaluate(delta, point) == 0
        for point in V23.SUPPORT + V23.BACKGROUND
    )

    n_core = len(V23.CORE)
    d = len(V23.D0)
    h = len(V23.SUPPORT)
    b = len(V23.BACKGROUND)
    s = h - d
    u = V23.ELL - s
    r = 2 * d - h
    assert len(common_defect) + len(common_background) <= r
    joint = b * d * d + n_core * u * u - n_core * b * r
    assert joint == 0
    return 2, joint, r


def arithmetic_audit() -> tuple[int, int, int]:
    positive = 0
    zero = 0
    tail = 0
    for n_core in range(2, 31):
        for ell in range(1, 11):
            for b in range(ell):
                for a in range(n_core + 1):
                    for c in range(a + 1):
                        s = a - c
                        u = ell - s
                        if not (0 <= u <= b) or s == 0:
                            continue
                        d = n_core - a
                        h = n_core - c
                        r = 2 * d - h
                        joint = b * d * d + n_core * u * u - n_core * b * r
                        transformed = (
                            b * a * a + n_core * u * u - n_core * b * c
                        )
                        assert joint == transformed
                        if r < 0:
                            continue
                        if joint > 0:
                            assert d + u - r == ell
                            assert n_core * b * ell >= joint
                            positive += 1
                        elif joint == 0:
                            zero += 1
                        else:
                            assert b > 0
                            assert a * a <= n_core * c
                            assert u * u <= b * c
                            tail += 1
    return positive, zero, tail


def main() -> None:
    sharp_count, sharp_joint, sharp_r = f17_sharp_fixture()
    zero_count, zero_joint, zero_r = f23_zero_fixture()
    positive, zero, tail = arithmetic_audit()
    assert positive > 0 and zero > 0 and tail > 0
    print(
        "L1_JOINT_CORE_BACKGROUND_JOHNSON_PASS "
        f"sharp={sharp_count} joint={sharp_joint} r={sharp_r} "
        f"boundary={zero_count} zero_joint={zero_joint} zero_r={zero_r} "
        f"positive={positive} zero={zero} tail={tail}"
    )


if __name__ == "__main__":
    main()
