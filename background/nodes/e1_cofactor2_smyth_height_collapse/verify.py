#!/usr/bin/env python3
"""Certify the entropy and Smyth margins for the E1 cofactor-2 collapse."""

from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
PARENT_PATH = (
    ROOT / "background/nodes/e1_high_cofactor_schinzel_height_collapse/verify.py"
)
EXPECTED_PARENT_SHA256 = (
    "ef12337e19256b03bed7ce6e0fbd51d4e0ae5da4471e3ba722bfb4ff761fe491"
)
EXPECTED_CERTIFICATE_DIGEST = (
    "ee3e59acdfed6536189c3ff18476a7c657e279729e0c906ef627c4224c245cb8"
)


def load_parent():
    digest = sha256(PARENT_PATH.read_bytes()).hexdigest()
    if digest != EXPECTED_PARENT_SHA256:
        raise RuntimeError(f"parent verifier hash drift: {digest}")
    spec = importlib.util.spec_from_file_location("e1_c2_parent", PARENT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load parent verifier")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


PARENT = load_parent()
Interval = PARENT.Interval
ONE = PARENT.ONE
ORDER = 64
D_LIMIT = Decimal("7.539")
P_LIMIT = Decimal("12.2")
BISECTION_STEPS = 84
CERTIFICATE_SCALE = Decimal(10) ** 20


def entropy_certificate() -> tuple[Decimal, int, str, int, int]:
    minimum_barrier: Decimal | None = None
    minimum_index = -1
    certificate_rows: list[str] = []
    active = 0
    skipped = 0

    for positive_count in range(1, ORDER):
        negative_count = ORDER - positive_count
        maximum_positive_log = PARENT.log_any_positive(
            Interval.point(ORDER) / Interval.point(positive_count)
        ).times_int(positive_count)
        if maximum_positive_log.hi < P_LIMIT:
            skipped += 1
            certificate_rows.append(f"{positive_count}:skip")
            continue

        active += 1
        lower_excess = Decimal(0)
        upper_excess = Decimal(negative_count)
        for _ in range(BISECTION_STEPS):
            midpoint = PARENT.PARENT.down_div(
                PARENT.PARENT.down_add(lower_excess, upper_excess), Decimal(2)
            )
            positive_average = ONE + (
                Interval.point(midpoint) / Interval.point(positive_count)
            )
            candidate = PARENT.log_any_positive(positive_average).times_int(
                positive_count
            )
            if candidate.hi < P_LIMIT:
                lower_excess = midpoint
            else:
                upper_excess = midpoint

        positive_average = ONE + (
            Interval.point(lower_excess) / Interval.point(positive_count)
        )
        negative_average = ONE - (
            Interval.point(lower_excess) / Interval.point(negative_count)
        )
        positive_log = PARENT.log_any_positive(positive_average)
        negative_log = PARENT.log_any_positive(negative_average)
        positive_total = positive_log.times_int(positive_count)
        if not positive_total.hi < P_LIMIT:
            raise RuntimeError(f"invalid lower bracket at {positive_count}")

        barrier = -positive_total - negative_log.times_int(negative_count)
        if not barrier.lo > D_LIMIT:
            raise RuntimeError(
                f"entropy barrier failed at {positive_count}: {barrier.lo}"
            )
        if minimum_barrier is None or barrier.lo < minimum_barrier:
            minimum_barrier = barrier.lo
            minimum_index = positive_count

        scaled = PARENT.PARENT.floor_decimal(
            PARENT.PARENT.down_mul(lower_excess, CERTIFICATE_SCALE)
        )
        certificate_rows.append(
            f"{positive_count}:{scaled}:"
            f"{PARENT.PARENT.floor_decimal(PARENT.PARENT.down_mul(barrier.lo, CERTIFICATE_SCALE))}"
        )

    if minimum_barrier is None:
        raise RuntimeError("empty entropy certificate")
    digest = sha256("\n".join(certificate_rows).encode("ascii")).hexdigest()
    return minimum_barrier, minimum_index, digest, active, skipped


def smyth_polynomial(value: Fraction) -> Fraction:
    return value**4 - value**3 - 3 * value**2 + value + 1


def check_smyth_polynomial() -> None:
    q = Fraction
    if not smyth_polynomial(q(209, 100)) < 0 < smyth_polynomial(q(3)):
        raise RuntimeError("positive beta_2 root bracket failed")
    if not smyth_polynomial(q(-2)) > 0 > smyth_polynomial(q(-133, 100)):
        raise RuntimeError("negative beta_2 root bracket failed")
    if not q(209, 100) * q(133, 100) > q(129, 100) ** 4:
        raise RuntimeError("beta_2 Mahler lower bound failed")


def main() -> None:
    log_eighteen = PARENT.log_any_positive(Interval.point(18))
    deficit = log_eighteen.times_int(64) - PARENT.PARENT.LOG_TWO.times_int(256)
    if not deficit.hi < D_LIMIT:
        raise RuntimeError(f"cofactor-2 deficit failed: {deficit}")

    minimum, index, digest, active, skipped = entropy_certificate()
    print(f"certificate_digest={digest}")
    if digest != EXPECTED_CERTIFICATE_DIGEST:
        raise RuntimeError(f"certificate digest drift: {digest}")

    check_smyth_polynomial()
    pair_upper = Decimal(2) * (D_LIMIT + Decimal(2) * P_LIMIT)
    smyth_lower = PARENT.log_any_positive(
        Interval.point(Decimal("1.29"))
    ).times_int(256)
    if not pair_upper < smyth_lower.lo:
        raise RuntimeError(f"Smyth separation failed: {pair_upper}, {smyth_lower.lo}")

    print("E1_COFACTOR2_SMYTH_HEIGHT_COLLAPSE_PASS checks=72")
    print(f"cofactor2_D_upper={deficit.hi}")
    print(
        f"entropy_minimum_barrier={minimum} positive_count={index} "
        f"active={active} skipped={skipped}"
    )
    print(f"pair_log_l1_upper={pair_upper}")
    print(f"smyth_log_l1_lower={smyth_lower.lo}")
    print("collapsed_cofactor=2 maximum_orbits=1")


if __name__ == "__main__":
    main()
