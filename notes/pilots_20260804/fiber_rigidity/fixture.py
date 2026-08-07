#!/usr/bin/env python3
"""Exact boundary fixture for the proposed XR fiber-rigidity mechanism.

The quick path reconstructs the active-defect primitive-Pade data.  The full
path streams the complete k-subset pencil atlas, retaining only the current
agreement maximum and lexicographically first support at each slope.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import sys
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ALGEBRA = ROOT / "notes/pilots_20260803/sl2_unstructured"
sys.path.insert(0, str(ALGEBRA))

from algebra import evalpoly, interpolate, inv, locator, pmul, rank, root_of_unity  # noqa: E402


QFIELD = 193
N = 64
K = 4
DEPTH = 13
H_EXCESS = 18
AGREEMENT = K + H_EXCESS
ELL = 2
BLOCK_SIZE = H_EXCESS - DEPTH
RPRIME = N - K - DEPTH
INF = "inf"
DEFAULT_OUTPUT = HERE / "fixture.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def trim(coefficients: list[int]) -> list[int]:
    out = list(coefficients)
    while out and out[-1] == 0:
        out.pop()
    return out or [0]


def polynomial_digest(coefficients: list[int]) -> str:
    encoded = json.dumps(trim(coefficients), separators=(",", ":"))
    return hashlib.sha256(encoded.encode("ascii")).hexdigest()


def toeplitz(word: list[int]) -> list[list[int]]:
    return [
        [word[(row - column) % N] for column in range(RPRIME + 1)]
        for row in range(N - DEPTH, N)
    ]


def update_maximum(
    maxima: dict[object, int],
    selected: dict[object, tuple[int, ...]],
    slope: object,
    support: tuple[int, ...],
) -> bool:
    agreement = len(support)
    old = maxima.get(slope, -1)
    if agreement > old:
        maxima[slope] = agreement
        selected[slope] = support
        return agreement > AGREEMENT
    if agreement == old and support < selected[slope]:
        selected[slope] = support
    return False


def support_profile(
    u_values: list[int], v_values: list[int], f: list[int], g: list[int], H: list[int]
) -> tuple[tuple[int, ...], dict[object, tuple[int, ...]]]:
    core = []
    extras: dict[object, list[int]] = {}
    for index, x_value in enumerate(H):
        first = (u_values[index] - evalpoly(f, x_value, QFIELD)) % QFIELD
        second = (v_values[index] - evalpoly(g, x_value, QFIELD)) % QFIELD
        if first == 0 and second == 0:
            core.append(index)
        elif second == 0:
            extras.setdefault(INF, []).append(index)
        else:
            slope = (-first * inv(second, QFIELD)) % QFIELD
            extras.setdefault(slope, []).append(index)
    return tuple(core), {key: tuple(value) for key, value in extras.items()}


def initialize_zero_pair(
    u_values: list[int], v_values: list[int], H: list[int]
) -> tuple[dict[object, int], dict[object, tuple[int, ...]], tuple[int, ...]]:
    core, extras = support_profile(u_values, v_values, [0], [0], H)
    maxima: dict[object, int] = {}
    selected: dict[object, tuple[int, ...]] = {}
    for slope in [*range(QFIELD), INF]:
        support = tuple(sorted((*core, *extras.get(slope, ()))))
        update_maximum(maxima, selected, slope, support)
    return maxima, selected, core


def exhaustive_pencil_scan(
    u_values: list[int], v_values: list[int], H: list[int]
) -> dict:
    maxima, selected, planted_core = initialize_zero_pair(u_values, v_values, H)
    require(len(planted_core) == K + DEPTH, "planted core size before scan")

    subsets = 0
    canonical_pairs = 0
    high_core_pairs = 0
    for subset in combinations(range(N), K):
        subsets += 1
        points = [H[index] for index in subset]
        f = interpolate(
            [(points[j], u_values[subset[j]]) for j in range(K)], QFIELD
        )
        g = interpolate(
            [(points[j], v_values[subset[j]]) for j in range(K)], QFIELD
        )
        core, extras = support_profile(u_values, v_values, f, g, H)

        # Every pair appears once for each k-subset of its joint core.  Only
        # its lexicographically first k-subset performs the atlas update.
        if core[:K] != subset:
            continue
        canonical_pairs += 1
        base = len(core)
        if base >= len(planted_core):
            high_core_pairs += 1
            for slope in [*range(QFIELD), INF]:
                support = tuple(sorted((*core, *extras.get(slope, ()))))
                if update_maximum(maxima, selected, slope, support):
                    return {
                        "complete": False,
                        "reason": "over_agreement",
                        "slope": slope,
                        "agreement": len(support),
                        "subsets": subsets,
                        "canonical_pairs": canonical_pairs,
                        "high_core_pairs": high_core_pairs,
                    }
        else:
            for slope, extra in extras.items():
                support = tuple(sorted((*core, *extra)))
                if update_maximum(maxima, selected, slope, support):
                    return {
                        "complete": False,
                        "reason": "over_agreement",
                        "slope": slope,
                        "agreement": len(support),
                        "subsets": subsets,
                        "canonical_pairs": canonical_pairs,
                        "high_core_pairs": high_core_pairs,
                    }

        if subsets % 100000 == 0:
            print(
                "scan_progress "
                f"subsets={subsets} canonical_pairs={canonical_pairs} "
                f"max={max(maxima.values())}",
                flush=True,
            )

    live = sorted(
        (slope for slope, value in maxima.items() if value == AGREEMENT),
        key=lambda value: (value == INF, value if value != INF else 0),
    )
    return {
        "complete": True,
        "subsets": subsets,
        "expected_subsets": 635376,
        "canonical_pairs": canonical_pairs,
        "high_core_pairs": high_core_pairs,
        "maximum": max(maxima.values()),
        "live_slopes": live,
        "maxima": {str(key): value for key, value in maxima.items()},
        "selected": {str(key): list(value) for key, value in selected.items()},
    }


def choose_ray_parameters(H: list[int], D: tuple[int, ...]) -> tuple[int, int]:
    image = {
        (evalpoly([1, 0, 1], x_value, QFIELD) * inv(x_value, QFIELD)) % QFIELD
        for x_value in H
    }
    allowed = []
    for value in range(1, QFIELD):
        # Error ray (1,value) has finite pencil slope z=-1/value.  The
        # corresponding L=Q-zP has an H-root iff -value lies in phi(H).
        if (-value) % QFIELD in image:
            continue
        if all(
            (
                evalpoly([1, 0, 1], H[index], QFIELD)
                + value * H[index]
            )
            % QFIELD
            != 0
            for index in D
        ):
            allowed.append(value)
    require(len(allowed) >= 2, "two root-free ray parameters")
    return allowed[0], allowed[1]


def build_fixture(seed: int) -> dict:
    require(BLOCK_SIZE == 2 * ELL + 1, "tuple-incidence boundary")
    generator = root_of_unity(N, QFIELD)
    H = [pow(generator, index, QFIELD) for index in range(N)]
    require(len(set(H)) == N, "smooth domain cardinality")

    fibers = ((1, 63), (2, 62), (3, 61), (4, 60), (5, 59))
    D = tuple(index for pair in fibers for index in pair)
    block_plus = (1, 63, 2, 3, 4)
    block_minus = tuple(sorted(set(D) - set(block_plus)))
    require(len(block_plus) == len(block_minus) == BLOCK_SIZE, "block sizes")

    phi_values = [
        (evalpoly([1, 0, 1], H[index], QFIELD) * inv(H[index], QFIELD))
        % QFIELD
        for index in D
    ]
    fiber_partition: dict[int, list[int]] = {}
    for index, value in zip(D, phi_values):
        fiber_partition.setdefault(value, []).append(index)
    require(
        sorted(len(value) for value in fiber_partition.values()) == [2] * 5,
        "five complete inverse-pair fibers",
    )

    ray_plus, ray_minus = choose_ray_parameters(H, D)
    slope_plus = (-inv(ray_plus, QFIELD)) % QFIELD
    slope_minus = (-inv(ray_minus, QFIELD)) % QFIELD
    require(slope_plus != slope_minus, "distinct planted slopes")

    available = [index for index in range(N) if index not in D]
    core = tuple(available[: K + DEPTH])
    random_source = random.Random(seed)
    w_values = [0] * N
    for index in available:
        if index in core:
            continue
        w_values[index] = random_source.randrange(1, QFIELD)

    u_values = [0] * N
    v_values = [0] * N
    for index, x_value in enumerate(H):
        if index in block_plus:
            u_values[index] = 1
            v_values[index] = ray_plus
        elif index in block_minus:
            u_values[index] = 1
            v_values[index] = ray_minus
        else:
            p_value = evalpoly([1, 0, 1], x_value, QFIELD)
            q_value = x_value
            u_values[index] = q_value * w_values[index] % QFIELD
            v_values[index] = -p_value * w_values[index] % QFIELD

    u_polynomial = interpolate(list(zip(H, u_values)), QFIELD)
    v_polynomial = interpolate(list(zip(H, v_values)), QFIELD)
    require(
        all(evalpoly(u_polynomial, x, QFIELD) == y for x, y in zip(H, u_values)),
        "u interpolation",
    )
    require(
        all(evalpoly(v_polynomial, x, QFIELD) == y for x, y in zip(H, v_values)),
        "v interpolation",
    )

    P = [1, 0, 1]
    Q = [0, 1]
    Z_D = locator([H[index] for index in D], QFIELD)
    A = pmul(Z_D, P, QFIELD)
    B = pmul(Z_D, Q, QFIELD)
    require(len(A) == DEPTH and len(B) <= DEPTH, "syzygy component degrees")

    first_rows = toeplitz(u_polynomial)
    second_rows = toeplitz(v_polynomial)
    stacked_rank = rank(first_rows + second_rows, QFIELD)
    expected_rank = 2 * DEPTH - 1
    relation_first = list(reversed(A + [0] * (DEPTH - len(A))))
    relation_second = list(reversed(B + [0] * (DEPTH - len(B))))
    relation = [
        sum(
            relation_first[row] * first_rows[row][column]
            + relation_second[row] * second_rows[row][column]
            for row in range(DEPTH)
        )
        % QFIELD
        for column in range(RPRIME + 1)
    ]
    require(not any(relation), "displayed left-kernel relation")
    require(stacked_rank == expected_rank, "one-dimensional left kernel")

    residual = [
        (
            evalpoly(P, x_value, QFIELD) * u_values[index]
            + evalpoly(Q, x_value, QFIELD) * v_values[index]
        )
        % QFIELD
        for index, x_value in enumerate(H)
    ]
    residual_support = tuple(index for index, value in enumerate(residual) if value)
    require(residual_support == tuple(sorted(D)), "active residual support")

    actual_core = tuple(
        index
        for index, (first, second) in enumerate(zip(u_values, v_values))
        if first == 0 and second == 0
    )
    require(actual_core == core, "exact planted joint core")

    zero_maxima, zero_selected, _ = initialize_zero_pair(u_values, v_values, H)
    expected_plus = tuple(sorted((*core, *block_plus)))
    expected_minus = tuple(sorted((*core, *block_minus)))
    require(zero_selected[slope_plus] == expected_plus, "zero-pair plus support")
    require(zero_selected[slope_minus] == expected_minus, "zero-pair minus support")
    require(zero_maxima[slope_plus] == AGREEMENT, "zero-pair plus agreement")
    require(zero_maxima[slope_minus] == AGREEMENT, "zero-pair minus agreement")

    profiles = {}
    for label, block in (("plus", block_plus), ("minus", block_minus)):
        counts = []
        for points in fiber_partition.values():
            count = len(set(points) & set(block))
            if count:
                counts.append(count)
        counts.sort(reverse=True)
        require(counts == [2, 1, 1, 1], f"{label} split-fiber profile")
        profiles[label] = counts

    # BE at tau=0 in the finite chart w_z=u+zv.
    for slope, block in ((slope_plus, block_plus), (slope_minus, block_minus)):
        for index in block:
            x_value = H[index]
            denominator = (
                evalpoly(Q, x_value, QFIELD)
                - slope * evalpoly(P, x_value, QFIELD)
            ) % QFIELD
            numerator = (u_values[index] + slope * v_values[index]) % QFIELD
            require(denominator != 0 and numerator == 0, "block equation BE")

    return {
        "schema": "xr-fiber-rigidity-boundary-fixture-v1",
        "seed": seed,
        "row": {
            "q": QFIELD,
            "n": N,
            "k": K,
            "d": DEPTH,
            "h": H_EXCESS,
            "A": AGREEMENT,
            "ell": ELL,
            "r": BLOCK_SIZE,
            "rprime": RPRIME,
            "sigma": DEPTH - ELL - 1 - 2 * BLOCK_SIZE,
        },
        "domain": H,
        "P": P,
        "Q": Q,
        "Z_D": Z_D,
        "syzygy": {
            "A": A,
            "B": B,
            "stacked_rank": stacked_rank,
            "left_nullity": 2 * DEPTH - stacked_rank,
            "relation_zero": not any(relation),
        },
        "received": {
            "u_values": u_values,
            "v_values": v_values,
            "u_polynomial": trim(u_polynomial),
            "v_polynomial": trim(v_polynomial),
            "u_digest": polynomial_digest(u_polynomial),
            "v_digest": polynomial_digest(v_polynomial),
        },
        "active_defect": {
            "D": list(D),
            "residual_values": [residual[index] for index in D],
            "support_exact": residual_support == tuple(sorted(D)),
        },
        "core": list(core),
        "fiber_partition": {
            str(key): value for key, value in sorted(fiber_partition.items())
        },
        "blocks": {
            "plus": list(block_plus),
            "minus": list(block_minus),
            "profiles": profiles,
        },
        "rays": {
            "error_plus": ray_plus,
            "error_minus": ray_minus,
            "slope_plus": slope_plus,
            "slope_minus": slope_minus,
            "support_plus": list(expected_plus),
            "support_minus": list(expected_minus),
        },
        "quick_checks": {
            "primitive_kernel": True,
            "maximal_core": True,
            "active_locality": True,
            "block_equation": True,
            "fiber_rigidity_holds": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260806)
    parser.add_argument("--max-seeds", type=int, default=1)
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()

    rejected = []
    for offset in range(arguments.max_seeds):
        seed = arguments.seed + offset
        fixture = build_fixture(seed)
        if arguments.quick:
            print(
                "XR_FIBER_RIGIDITY_QUICK_PASS "
                f"seed={seed} rank={fixture['syzygy']['stacked_rank']} "
                "profiles=2,1,1,1/2,1,1,1",
                flush=True,
            )
            return

        scan = exhaustive_pencil_scan(
            fixture["received"]["u_values"],
            fixture["received"]["v_values"],
            fixture["domain"],
        )
        if not scan["complete"]:
            rejected.append({"seed": seed, **scan})
            print(
                "seed_rejected "
                f"seed={seed} reason={scan['reason']} "
                f"agreement={scan.get('agreement')}",
                flush=True,
            )
            continue

        plus = str(fixture["rays"]["slope_plus"])
        minus = str(fixture["rays"]["slope_minus"])
        require(scan["maximum"] == AGREEMENT, "global tangent ceiling")
        require(
            scan["selected"][plus] == fixture["rays"]["support_plus"],
            "plus first-match support",
        )
        require(
            scan["selected"][minus] == fixture["rays"]["support_minus"],
            "minus first-match support",
        )
        selected_supports = {
            slope: set(support) for slope, support in scan["selected"].items()
        }
        planted_core = set(fixture["core"])
        containing = sorted(
            slope
            for slope, support in selected_supports.items()
            if planted_core <= support and len(support) == AGREEMENT
        )
        require(containing == sorted((plus, minus)), "exact selected L_P=2")

        fixture["scan"] = scan
        fixture["scan"]["rejected_seeds"] = rejected
        fixture["scan"]["selected_slopes_containing_core"] = containing
        fixture["verdict"] = "COUNTEREXAMPLE_TO_FIELD_INDEPENDENT_FR"
        encoded = json.dumps(fixture, sort_keys=True, indent=1) + "\n"
        arguments.output.write_text(encoded, encoding="ascii")
        print(
            "XR_FIBER_RIGIDITY_BOUNDARY_COUNTEREXAMPLE_PASS "
            f"seed={seed} subsets={scan['subsets']} "
            f"canonical_pairs={scan['canonical_pairs']} live={len(scan['live_slopes'])} "
            "Lp=2 profiles=2,1,1,1/2,1,1,1",
            flush=True,
        )
        return

    raise RuntimeError(
        f"no passing seed in bounded range; rejected={json.dumps(rejected)}"
    )


if __name__ == "__main__":
    main()
