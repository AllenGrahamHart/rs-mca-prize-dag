#!/usr/bin/env python3
"""Certify the entropy-height collapse for E1 cofactors 4, 8, and 16."""

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
EXPECTED_CERTIFICATE_DIGEST = (
    "0404fc4ac941d2a48453fac4d316b47f4c2538b7f3db47d0b6a5ea356c6f9e2f"
)


def load_parent():
    digest = sha256(PARENT_PATH.read_bytes()).hexdigest()
    if digest != EXPECTED_PARENT_SHA256:
        raise RuntimeError(f"parent verifier hash drift: {digest}")
    spec = importlib.util.spec_from_file_location("e1_shc_parent", PARENT_PATH)
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
D_LIMIT = Decimal("6.845")
P_LIMIT = Decimal("11.9")
BISECTION_STEPS = 84
CERTIFICATE_SCALE = Decimal(10) ** 20


def log_any_positive(value: Interval) -> Interval:
    if value.hi <= 1:
        return PARENT.log_positive(value)
    if value.lo >= 1:
        return -PARENT.log_positive(ONE / value)
    raise RuntimeError("log interval crosses one")


def entropy_certificate() -> tuple[Decimal, int, str, int, int]:
    minimum_barrier: Decimal | None = None
    minimum_index = -1
    certificate_rows: list[str] = []
    active = 0
    skipped = 0

    for positive_count in range(1, ORDER):
        negative_count = ORDER - positive_count
        maximum_positive_log = log_any_positive(
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
            midpoint = PARENT.down_div(
                PARENT.down_add(lower_excess, upper_excess), Decimal(2)
            )
            positive_average = ONE + (
                Interval.point(midpoint) / Interval.point(positive_count)
            )
            candidate = log_any_positive(positive_average).times_int(positive_count)
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
        positive_log = log_any_positive(positive_average)
        negative_log = log_any_positive(negative_average)
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

        scaled = PARENT.floor_decimal(
            PARENT.down_mul(lower_excess, CERTIFICATE_SCALE)
        )
        certificate_rows.append(
            f"{positive_count}:{scaled}:"
            f"{PARENT.floor_decimal(PARENT.down_mul(barrier.lo, CERTIFICATE_SCALE))}"
        )

    if minimum_barrier is None:
        raise RuntimeError("empty entropy certificate")
    digest = sha256("\n".join(certificate_rows).encode("ascii")).hexdigest()
    return minimum_barrier, minimum_index, digest, active, skipped


def main() -> None:
    log_nine_sixteenths = PARENT.log_positive(
        Interval.point(Decimal(9) / Decimal(16))
    )
    log_eighteen = log_nine_sixteenths + PARENT.LOG_TWO.times_int(5)
    high_cofactor_deficit = (
        log_eighteen.times_int(64) - PARENT.LOG_TWO.times_int(257)
    )
    if not high_cofactor_deficit.hi < D_LIMIT:
        raise RuntimeError(f"cofactor deficit failed: {high_cofactor_deficit}")

    minimum_barrier, minimum_index, digest, active, skipped = entropy_certificate()
    print(f"certificate_digest={digest}")
    if digest != EXPECTED_CERTIFICATE_DIGEST:
        raise RuntimeError(f"certificate digest drift: {digest}")

    sqrt_five = Interval(PARENT.down_sqrt(Decimal(5)), PARENT.up_sqrt(Decimal(5)))
    phi = (ONE + sqrt_five) / Interval.point(2)
    schinzel_lower = log_any_positive(phi).times_int(128)
    pair_upper = Decimal(2) * (D_LIMIT + Decimal(2) * P_LIMIT)
    if not pair_upper < schinzel_lower.lo:
        raise RuntimeError(
            f"Schinzel separation failed: {pair_upper}, {schinzel_lower.lo}"
        )

    print("E1_HIGH_COFACTOR_SCHINZEL_HEIGHT_COLLAPSE_PASS checks=72")
    print(f"high_cofactor_D_upper={high_cofactor_deficit.hi}")
    print(
        f"entropy_minimum_barrier={minimum_barrier} "
        f"positive_count={minimum_index} active={active} skipped={skipped}"
    )
    print(f"pair_log_l1_upper={pair_upper}")
    print(f"schinzel_log_l1_lower={schinzel_lower.lo}")
    print("collapsed_cofactors=4,8,16 maximum_orbits=3 open_cofactor=2")


if __name__ == "__main__":
    main()
