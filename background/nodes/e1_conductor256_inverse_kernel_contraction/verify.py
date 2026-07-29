#!/usr/bin/env python3
"""Certify the conductor-256 inverse log-convolution contraction."""

from __future__ import annotations

from decimal import Decimal
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
PARENT_PATH = (
    ROOT
    / "background/nodes/e1_conductor256_character_eigenvalue_preflight/verify.py"
)
EXPECTED_PARENT_SHA256 = (
    "66db2b81c14c1d3c6459b92727a74b895ece03286f7691e704be47e1e58c6cba"
)
EXPECTED_KERNEL_DIGEST = (
    "cea9045128e02103e878ef6a4694840fa97aa5a00cfd524da46f0b26347febbe"
)


def load_parent():
    digest = sha256(PARENT_PATH.read_bytes()).hexdigest()
    if digest != EXPECTED_PARENT_SHA256:
        raise RuntimeError(f"parent verifier hash drift: {digest}")
    spec = importlib.util.spec_from_file_location("e1_cep_parent", PARENT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load parent verifier")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


PARENT = load_parent()
Interval = PARENT.Interval
ComplexInterval = PARENT.ComplexInterval
ORDER = PARENT.ORDER
SCALE = PARENT.SCALE


def square_interval(value: Interval) -> Interval:
    maximum = max(value.lo.copy_abs(), value.hi.copy_abs())
    if value.lo <= 0 <= value.hi:
        minimum = Decimal(0)
    else:
        minimum = min(value.lo.copy_abs(), value.hi.copy_abs())
    return Interval(
        PARENT.down_mul(minimum, minimum),
        PARENT.up_mul(maximum, maximum),
    )


def complex_multiply(left: ComplexInterval, right: ComplexInterval) -> ComplexInterval:
    return ComplexInterval(
        left.real * right.real - left.imag * right.imag,
        left.real * right.imag + left.imag * right.real,
    )


def complex_inverse(value: ComplexInterval) -> ComplexInterval:
    denominator = square_interval(value.real) + square_interval(value.imag)
    if denominator.lo <= 0:
        raise RuntimeError("inverse rectangle meets zero")
    return ComplexInterval(value.real / denominator, -value.imag / denominator)


def kernel_intervals() -> list[ComplexInterval]:
    pi, kappas, _magnitudes = PARENT.spectrum()
    roots = PARENT.root_table(pi)
    inverses = [None] + [complex_inverse(kappas[j]) for j in range(1, ORDER)]
    kernel: list[ComplexInterval] = []
    for index in range(ORDER):
        total = PARENT.COMPLEX_ZERO
        for frequency in range(1, ORDER):
            root = roots[(frequency * index) % ORDER].conjugate()
            total = total + complex_multiply(inverses[frequency], root)
        kernel.append(
            ComplexInterval(
                total.real / Interval.point(ORDER),
                total.imag / Interval.point(ORDER),
            )
        )
    return kernel


def main() -> None:
    kernel = kernel_intervals()
    for index, value in enumerate(kernel):
        if not (value.imag.lo <= 0 <= value.imag.hi):
            raise RuntimeError(f"kernel entry {index} is not certified real")
        if value.real.width() >= Decimal("1e-68"):
            raise RuntimeError(f"kernel entry {index} interval too wide")

    global_lower = min(value.real.lo for value in kernel)
    global_upper = max(value.real.hi for value in kernel)
    radius_upper = PARENT.up_div(
        PARENT.up_sub(global_upper, global_lower), Decimal(2)
    )

    l1_upper = Decimal(0)
    brackets: list[str] = []
    for index, value in enumerate(kernel):
        absolute_upper = max(value.real.lo.copy_abs(), value.real.hi.copy_abs())
        l1_upper = PARENT.up_add(l1_upper, absolute_upper)
        lower_scaled = PARENT.floor_decimal(PARENT.down_mul(value.real.lo, SCALE))
        upper_scaled = PARENT.ceil_decimal(PARENT.up_mul(value.real.hi, SCALE))
        brackets.append(f"{index}:{lower_scaled}:{upper_scaled}")

    digest = sha256("\n".join(brackets).encode("ascii")).hexdigest()
    print(f"kernel_digest={digest}")
    if digest != EXPECTED_KERNEL_DIGEST:
        raise RuntimeError(f"kernel digest drift: {digest}")

    if not global_lower > Decimal("-0.057805"):
        raise RuntimeError(f"kernel lower headline failed: {global_lower}")
    if not global_upper < Decimal("0.031594"):
        raise RuntimeError(f"kernel upper headline failed: {global_upper}")
    if not radius_upper < Decimal("0.044700"):
        raise RuntimeError(f"kernel radius headline failed: {radius_upper}")
    if not l1_upper < Decimal("0.802"):
        raise RuntimeError(f"kernel L1 headline failed: {l1_upper}")

    radius_product = PARENT.up_mul(radius_upper, Decimal("77.202"))
    l1_product = PARENT.up_mul(l1_upper, Decimal("77.202"))
    if not radius_product < Decimal("3.451"):
        raise RuntimeError(f"coordinate contraction failed: {radius_product}")
    if not l1_product < Decimal("61.92"):
        raise RuntimeError(f"L1 contraction failed: {l1_product}")

    print("E1_CONDUCTOR256_INVERSE_KERNEL_CONTRACTION_PASS checks=75")
    print(f"kernel_lower={global_lower} kernel_upper={global_upper}")
    print(f"kernel_half_range_upper={radius_upper}")
    print(f"kernel_l1_upper={l1_upper}")
    print(f"coordinate_product_upper={radius_product}")
    print(f"exponent_l1_product_upper={l1_product}")
    print("coordinate_bound=3 exponent_l1_bound=60")


if __name__ == "__main__":
    main()
