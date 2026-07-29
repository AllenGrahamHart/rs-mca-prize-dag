#!/usr/bin/env python3
"""Audit the inverse kernel by direct time-domain convolution."""

from __future__ import annotations

from decimal import Decimal
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
PRIMARY_PATH = (
    ROOT / "background/nodes/e1_conductor256_inverse_kernel_contraction/verify.py"
)
EXPECTED_PRIMARY_SHA256 = (
    "8455922b1542c0f5db733e2f0bc8b48c6c88b181b681f49aee0d139be6df9c30"
)


def load_primary():
    digest = sha256(PRIMARY_PATH.read_bytes()).hexdigest()
    if digest != EXPECTED_PRIMARY_SHA256:
        raise RuntimeError(f"primary verifier hash drift: {digest}")
    spec = importlib.util.spec_from_file_location("e1_ikc_primary", PRIMARY_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load primary verifier")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    primary = load_primary()
    parent = primary.PARENT
    pi, _kappas, _magnitudes = parent.spectrum()
    representatives = [parent.canonical(pow(5, index, 256)) for index in range(64)]
    logs = []
    for representative in representatives:
        angle = pi.times_int(representative) / parent.Interval.point(256)
        logs.append(parent.log_positive(parent.sine_monotone(angle)).times_int(2))

    kernel = primary.kernel_intervals()
    maximum_width = Decimal(0)
    for displacement in range(64):
        total = parent.ZERO
        for index in range(64):
            total = total + kernel[(displacement + index) % 64].real * logs[index]
        expected = Decimal(63) / Decimal(64) if displacement == 0 else -Decimal(1) / Decimal(64)
        if not (total.lo <= expected <= total.hi):
            raise RuntimeError(
                f"inverse convolution mismatch at {displacement}: {total}, {expected}"
            )
        maximum_width = max(maximum_width, total.width())

    if maximum_width >= Decimal("1e-66"):
        raise RuntimeError(f"audit intervals too wide: {maximum_width}")
    print(
        "E1_CONDUCTOR256_INVERSE_KERNEL_CONTRACTION_AUDIT_PASS "
        f"identities=64 maximum_width={maximum_width}"
    )


if __name__ == "__main__":
    main()
