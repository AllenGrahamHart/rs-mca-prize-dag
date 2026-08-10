#!/usr/bin/env python3
"""Profile Schur coefficient-block ranks on random bad m=2 patterns."""

from __future__ import annotations

import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "rh_bivariate_m2_badpattern_modal.py"
RESULT = HERE / "rh_bivariate_m2_schur_profile_result.json"
REMOTE_SOURCE = "/root/rh_bivariate_m2_badpattern_modal.py"

APP = modal.App("rate-half-bivariate-m2-schur-profile")
IMAGE = modal.Image.debian_slim().add_local_file(SOURCE, REMOTE_SOURCE, copy=True)


def load_source():
    import importlib.util

    try:
        remote_exists = Path(REMOTE_SOURCE).is_file()
    except OSError:
        remote_exists = False
    source_path = REMOTE_SOURCE if remote_exists else str(SOURCE)
    spec = importlib.util.spec_from_file_location("rh_m2_search_source", source_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load search source")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def lagrange_weight(points, pivot, value, prime):
    numerator = 1
    denominator = 1
    for point in points:
        if point == pivot:
            continue
        numerator = numerator * (value - point) % prime
        denominator = denominator * (pivot - point) % prime
    return numerator * pow(denominator, prime - 2, prime) % prime


def coefficient_block_ranks(source, matrix, blocks, support):
    size = 4 * source.M + 1
    pivot_points = list(support[:size])
    residual_blocks = blocks[size:]
    normalized = {}
    for point_index, (column, indices, _) in enumerate(blocks):
        highest = indices[-1]
        leading = matrix[source.M + 1][highest]
        if not leading:
            raise RuntimeError("zero highest-clone leading coefficient")
        normalized[column] = [
            matrix[degree][highest] * pow(leading, source.P - 2, source.P)
            % source.P
            for degree in range(source.M + 1)
        ]

    block_ranks = []
    matrices = []
    for degree in range(source.M + 1):
        rows = []
        for moment in range(size):
            row = []
            for column, _, _ in residual_blocks:
                defect = (
                    pow(source.DOMAIN[column], moment, source.P)
                    * normalized[column][degree]
                    - sum(
                        lagrange_weight(
                            [source.DOMAIN[pivot] for pivot in pivot_points],
                            source.DOMAIN[pivot],
                            source.DOMAIN[column],
                            source.P,
                        )
                        * pow(source.DOMAIN[pivot], moment, source.P)
                        * normalized[pivot][degree]
                        for pivot in pivot_points
                    )
                ) % source.P
                row.append(defect)
            rows.append(row)
        matrices.append(rows)
        block_ranks.append(source.matrix_rank(rows))

    pair_ranks = {}
    for first in range(source.M + 1):
        for second in range(first + 1, source.M + 1):
            pair_ranks[f"{first}{second}"] = source.matrix_rank(
                matrices[first] + matrices[second]
            )
    stacked_rank = source.matrix_rank([row for matrix in matrices for row in matrix])
    top_rows = [moment * (source.M + 2) + source.M + 1 for moment in range(size)]
    top_matrix = [matrix[row] for row in top_rows]
    full_block_ranks = []
    for degree in range(source.M + 1):
        degree_rows = [
            moment * (source.M + 2) + degree for moment in range(size)
        ]
        full_block_ranks.append(
            source.matrix_rank(top_matrix + [matrix[row] for row in degree_rows])
            - size
        )
    full_pair_ranks = {}
    for first in range(source.M + 1):
        for second in range(first + 1, source.M + 1):
            selected_rows = [
                moment * (source.M + 2) + degree
                for degree in (first, second)
                for moment in range(size)
            ]
            full_pair_ranks[f"{first}{second}"] = (
                source.matrix_rank(top_matrix + [matrix[row] for row in selected_rows])
                - size
            )
    return (
        tuple(block_ranks),
        pair_ranks,
        stacked_rank,
        tuple(full_block_ranks),
        full_pair_ranks,
    )


def profile_core(seed: int, seconds: float, trial_cap: int):
    import random
    import time

    source = load_source()
    rng = random.Random(seed)
    started = time.monotonic()
    counters = {
        "attempted": 0,
        "regular_incidence": 0,
        "bad_pairs": 0,
        "saturated_w": 0,
        "deficient_w": 0,
        "full_matrix_rank": 0,
        "any_single_full_saturated": 0,
        "j0_full_saturated": 0,
        "j1_full_saturated": 0,
        "j2_full_saturated": 0,
        "any_pair_full_saturated": 0,
        "all_blocks_full_saturated": 0,
        "any_single_full_deficient": 0,
        "j0_full_deficient": 0,
        "j1_full_deficient": 0,
        "j2_full_deficient": 0,
        "any_pair_full_deficient": 0,
    }
    histograms = {
        "saturated_block_ranks": {},
        "deficient_block_ranks": {},
        "saturated_pair_full_sets": {},
        "saturated_full_schur_block_ranks": {},
        "deficient_full_schur_block_ranks": {},
        "deficient_pair_full_sets": {},
    }
    exceptions = []

    def bump(histogram, key):
        histogram[key] = histogram.get(key, 0) + 1

    while counters["attempted"] < trial_cap and time.monotonic() - started < seconds:
        counters["attempted"] += 1
        generated = source.random_incidence(rng)
        if generated is None:
            continue
        root_sets, owners, deficient = generated
        counters["regular_incidence"] += 1
        intersections = {
            (first, second): len(root_sets[first] & root_sets[second])
            for first in source.SLOPES
            for second in source.SLOPES
            if first < second
        }
        maximum = max(intersections.values())
        a_star = 2 * source.RHO - maximum
        if not (11 <= a_star <= 13):
            continue
        pairs = [pair for pair, value in intersections.items() if value == maximum]
        rng.shuffle(pairs)
        for first, second in pairs[:4]:
            support_set = root_sets[first] | root_sets[second]
            need_x = source.RHO - (
                (source.N - len(support_set)) * source.M
                // (len(source.SLOPES) - 2)
                + 1
            )
            worst_x = max(
                len(root_sets[slope] & support_set)
                for slope in source.SLOPES
                if slope not in (first, second)
            )
            if worst_x <= need_x:
                continue
            counters["bad_pairs"] += 1
            matrix, blocks, support, _ = source.build_matrix(
                owners,
                deficient,
                first,
                second,
                rng,
            )
            matrix_rank = source.matrix_rank(matrix)
            if matrix_rank == len(matrix[0]):
                counters["full_matrix_rank"] += 1
            (
                block_ranks,
                pair_ranks,
                stacked_rank,
                full_block_ranks,
                full_pair_ranks,
            ) = coefficient_block_ranks(
                source,
                matrix,
                blocks,
                support,
            )
            top_width = len(support) - (4 * source.M + 1)
            residual_width = len(matrix[0]) - (4 * source.M + 1)
            saturated = deficient not in support
            histogram = histograms[
                "saturated_block_ranks" if saturated else "deficient_block_ranks"
            ]
            bump(histogram, ",".join(str(value) for value in block_ranks))
            full_histogram = histograms[
                "saturated_full_schur_block_ranks"
                if saturated
                else "deficient_full_schur_block_ranks"
            ]
            bump(full_histogram, ",".join(str(value) for value in full_block_ranks))
            if not saturated:
                counters["deficient_w"] += 1
                full_degrees = [
                    degree
                    for degree, value in enumerate(full_block_ranks)
                    if value == residual_width
                ]
                full_pairs = [
                    key for key, value in full_pair_ranks.items()
                    if value == residual_width
                ]
                bump(
                    histograms["deficient_pair_full_sets"],
                    ",".join(full_pairs) or "none",
                )
                if full_degrees:
                    counters["any_single_full_deficient"] += 1
                for degree in full_degrees:
                    counters[f"j{degree}_full_deficient"] += 1
                if full_pairs:
                    counters["any_pair_full_deficient"] += 1
                if not full_degrees and len(exceptions) < 8:
                    exceptions.append(
                        {
                            "seed": seed,
                            "deficient": deficient,
                            "pair": [first, second],
                            "support": list(support),
                            "a_star": a_star,
                            "need_x": need_x,
                            "worst_x": worst_x,
                            "block_ranks": list(block_ranks),
                            "full_block_ranks": list(full_block_ranks),
                            "full_pair_ranks": full_pair_ranks,
                            "residual_width": residual_width,
                        }
                    )
                continue

            counters["saturated_w"] += 1
            full_degrees = [
                degree for degree, value in enumerate(block_ranks) if value == top_width
            ]
            full_pairs = [key for key, value in pair_ranks.items() if value == top_width]
            bump(histograms["saturated_pair_full_sets"], ",".join(full_pairs) or "none")
            if full_degrees:
                counters["any_single_full_saturated"] += 1
            for degree in full_degrees:
                counters[f"j{degree}_full_saturated"] += 1
            if full_pairs:
                counters["any_pair_full_saturated"] += 1
            if stacked_rank == top_width:
                counters["all_blocks_full_saturated"] += 1
            if not full_degrees and len(exceptions) < 8:
                exceptions.append(
                    {
                        "seed": seed,
                        "deficient": deficient,
                        "pair": [first, second],
                        "support": list(support),
                        "a_star": a_star,
                        "need_x": need_x,
                        "worst_x": worst_x,
                        "block_ranks": list(block_ranks),
                        "pair_ranks": pair_ranks,
                        "stacked_rank": stacked_rank,
                    }
                )

    return {
        "seed": seed,
        "elapsed": time.monotonic() - started,
        "counters": counters,
        "histograms": histograms,
        "exceptions": exceptions,
    }


@APP.function(image=IMAGE, cpu=1.0, memory=256, timeout=60, max_containers=32)
def profile_seed(seed: int, seconds: float, trial_cap: int):
    return profile_core(seed, seconds, trial_cap)


@APP.local_entrypoint()
def main(tasks: int = 16, seconds: float = 30.0, trial_cap: int = 100000) -> None:
    rows = []

    def checkpoint(complete: bool, error: str | None = None):
        counter_keys = (
            "attempted",
            "regular_incidence",
            "bad_pairs",
            "saturated_w",
            "deficient_w",
            "full_matrix_rank",
            "any_single_full_saturated",
            "j0_full_saturated",
            "j1_full_saturated",
            "j2_full_saturated",
            "any_pair_full_saturated",
            "all_blocks_full_saturated",
            "any_single_full_deficient",
            "j0_full_deficient",
            "j1_full_deficient",
            "j2_full_deficient",
            "any_pair_full_deficient",
        )
        totals = {
            key: sum(int(row["counters"][key]) for row in rows)
            for key in counter_keys
        }
        histograms = {}
        for histogram_name in (
            "saturated_block_ranks",
            "deficient_block_ranks",
            "saturated_pair_full_sets",
            "saturated_full_schur_block_ranks",
            "deficient_full_schur_block_ranks",
            "deficient_pair_full_sets",
        ):
            merged = {}
            for row in rows:
                for key, value in row["histograms"][histogram_name].items():
                    merged[key] = merged.get(key, 0) + int(value)
            histograms[histogram_name] = dict(sorted(merged.items()))
        packet = {
            "schema": "rate-half-bivariate-m2-schur-profile-v1",
            "complete": complete,
            "error": error,
            "parameters": {
                "field": 97,
                "m": 2,
                "tasks": tasks,
                "seconds_per_task": seconds,
                "trial_cap_per_task": trial_cap,
                "pivot_rule": "first 9 sorted support points",
            },
            "completed_tasks": len(rows),
            "totals": totals,
            "histograms": histograms,
            "exceptions": [item for row in rows for item in row["exceptions"]],
            "rows": sorted(rows, key=lambda row: int(row["seed"])),
        }
        RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
        return packet

    checkpoint(False)
    try:
        for row in profile_seed.map(
            range(tasks),
            [seconds] * tasks,
            [trial_cap] * tasks,
        ):
            rows.append(row)
            checkpoint(False)
    except BaseException as error:
        packet = checkpoint(False, f"{type(error).__name__}: {error}")
        print("RATE_HALF_BIVARIATE_M2_SCHUR_PROFILE_INCOMPLETE " + json.dumps(packet["totals"], sort_keys=True))
        raise
    packet = checkpoint(len(rows) == tasks)
    print("RATE_HALF_BIVARIATE_M2_SCHUR_PROFILE " + json.dumps(packet["totals"], sort_keys=True))
    print("RATE_HALF_BIVARIATE_M2_SCHUR_PROFILE_HIST " + json.dumps(packet["histograms"], sort_keys=True))
    print(f"RATE_HALF_BIVARIATE_M2_SCHUR_PROFILE_COMPLETE {packet['complete']}")
    print(f"RATE_HALF_BIVARIATE_M2_SCHUR_PROFILE_RESULT {RESULT}")
