#!/usr/bin/env python3
"""Screen cofactor-1028 E=4 types by their exact cubic conjugate moment."""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb
from pathlib import Path


B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
COFACTOR = 1028
EXPECTED_DISTRIBUTION = {
    -36: 1,
    -30: 1,
    -24: 13,
    -18: 38,
    -12: 478,
    -6: 704,
    0: 5860,
    6: 755,
    12: 477,
    18: 45,
    24: 13,
}
EXPECTED_DIGEST = "401203ca53dbd51a859b702767576b50aca05c73216194120a60eff251d1d442"


def autocorrelation_multiplicity(lags: tuple[int, ...]) -> int:
    exponents = tuple(value for lag in lags for value in (lag, 128 - lag))
    return next(
        (
            derivative
            for derivative in range(16)
            if sum(comb(exponent, derivative) for exponent in exponents) % 2
        ),
        16,
    )


def cubic_index(lags: tuple[int, ...], signs: tuple[int, ...]) -> int:
    oriented = tuple(
        (orientation * lag, sign)
        for lag, sign in zip(lags, signs)
        for orientation in (-1, 1)
    )
    index = 0
    for first_value, first_sign in oriented:
        for second_value, second_sign in oriented:
            for third_value, third_sign in oriented:
                total = first_value + second_value + third_value
                weight = first_sign * second_sign * third_sign
                if total == 0:
                    index += weight
                elif abs(total) == 128:
                    index -= weight
    return index


def cubic_index_by_relations(
    lags: tuple[int, ...], signs: tuple[int, ...]
) -> int:
    sign_by_lag = dict(zip(lags, signs))
    index = 0
    for first, second, third in combinations(lags, 3):
        sign_product = sign_by_lag[first] * sign_by_lag[second] * sign_by_lag[third]
        if first + second == third:
            index += 12 * sign_product
        if first + second + third == 128:
            index -= 12 * sign_product
    for source in lags:
        for target in lags:
            if source == target:
                continue
            if 2 * source == target:
                index += 6 * sign_by_lag[target]
            if 2 * source + target == 128:
                index -= 6 * sign_by_lag[target]
    return index


def census() -> dict[str, object]:
    root = 3
    if pow(root, 128, 257) != 256 or pow(root, 256, 257) != 1:
        raise RuntimeError("primitive-root check failed")
    traces = [0] + [
        (pow(root, lag, 257) + pow(pow(root, lag, 257), -1, 257)) % 257
        for lag in range(1, 64)
    ]
    distribution = Counter()
    high_rows = []
    ledger_rows = []
    multiplicity_four_sets = 0
    for lags in combinations(range(1, 64), 4):
        if autocorrelation_multiplicity(lags) != 4:
            continue
        multiplicity_four_sets += 1
        for signs in product((-1, 1), repeat=4):
            if (18 + sum(sign * traces[lag] for sign, lag in zip(signs, lags))) % 257:
                continue
            index = cubic_index(lags, signs)
            if index != cubic_index_by_relations(lags, signs):
                raise RuntimeError("cubic relation formula drift")
            distribution[index] += 1
            row = lags + signs + (index,)
            ledger_rows.append(",".join(map(str, row)))
            if index > 32:
                high_rows.append({"lags": lags, "signs": signs, "cubic_index": index})

    ledger = "\n".join(ledger_rows)
    return {
        "schema": "e1-m1028-e4-third-moment-screen-v1",
        "multiplicity_four_lag_sets": multiplicity_four_sets,
        "types": len(ledger_rows),
        "distribution": dict(sorted(distribution.items())),
        "maximum_cubic_index": max(distribution),
        "high_types": high_rows,
        "high_count": len(high_rows),
        "ledger_digest": sha256(ledger.encode("ascii")).hexdigest(),
    }


def main(
    output: str = "experiments/prize_resolution/e1_m1028_e4_third_moment_screen_result.json",
) -> None:
    payload = census()
    Path(output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    if payload["types"] != 8385:
        raise RuntimeError(f"compatible type census drift: {payload['types']}")
    if payload["multiplicity_four_lag_sets"] != 134720:
        raise RuntimeError("multiplicity-four lag census drift")
    if payload["distribution"] != EXPECTED_DISTRIBUTION:
        raise RuntimeError("cubic-index distribution drift")
    if payload["maximum_cubic_index"] != 24 or payload["high_count"]:
        raise RuntimeError("cubic-index cap drift")
    if payload["ledger_digest"] != EXPECTED_DIGEST:
        raise RuntimeError("compatible type ledger digest drift")
    print(
        "E1_M1028_E4_THIRD_MOMENT_SCREEN_DONE "
        f"types={payload['types']} maximum_K={payload['maximum_cubic_index']} "
        f"high_count={payload['high_count']} digest={payload['ledger_digest']}"
    )


if __name__ == "__main__":
    main()
