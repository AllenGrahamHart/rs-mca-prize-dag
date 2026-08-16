#!/usr/bin/env python3
"""Independent K'=83 threshold-frontier implementation."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import re
import tarfile
from functools import lru_cache
from math import comb
from pathlib import Path


ARCHIVES = list(Path(".").glob("*.tar.gz"))
ROOT = Path("repo") if ARCHIVES else Path(__file__).resolve().parents[2]
if ARCHIVES:
    for archive_path in ARCHIVES:
        with tarfile.open(archive_path, "r:gz") as archive:
            archive.extractall(ROOT, filter="data")


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PROBE = load_module(
    "k83_threshold_audit_probe",
    ROOT
    / "experiments/prize_resolution/rate_half_mca_rank11_k72_two_step_probe.py",
)
K71 = PROBE.K71
KPRIME, Q, M, N_CODE = 83, 73, 67555, 1048659
OLD_ROW = K71.LEDGER.row(KPRIME)
CEILING = (
    K71.LEDGER.RECORD_FLOOR * 55 * comb(M, 11)
    - 55 * comb(N_CODE, 11)
    - 55 * int(OLD_ROW["kernel"])
    - int(OLD_ROW["marks"])
    - 1
) // K71.LEDGER.RECORD_FLOOR


@lru_cache(maxsize=None)
def adjacent_pair(union: int, dimension: int, support: int) -> int:
    residual, outside = KPRIME - union - dimension, M - union
    assert dimension >= support + 1 and residual >= 0
    weight = (
        K71.LEDGER.DEFICITS[support]
        * comb(M - support, 11 - support)
    )
    weight_next = (
        K71.LEDGER.DEFICITS[support + 1]
        * comb(M - support - 1, 10 - support)
    )
    pieces = []
    for inside in range(support - 1):
        low = (
            comb(union, inside)
            * residual
            * comb(outside, support - 1 - inside)
            // (support - inside)
        )
        adjacent_rhs = (
            comb(union, inside)
            * residual
            * comb(outside, support - inside)
        )
        loss = outside - residual - support + 1 + inside
        slope = (support + 1 - inside) * weight - loss * weight_next
        pieces.append(
            (
                weight_next * adjacent_rhs
                + max(slope, 0) * low
            )
            // (support + 1 - inside)
        )
    pieces.append(
        weight
        * (
            comb(union, support - 1) * residual
            + comb(union, support)
        )
    )
    pieces.append(
        weight_next
        * (
            comb(union, support - 1) * residual * outside // 2
            + comb(union, support) * residual
            + comb(union, support + 1)
        )
    )
    return sum(pieces)


def charge_options(local: tuple[int, ...], cases: dict):
    for name, charges in reversed(tuple(cases.items())):
        candidate = local
        adjacent = {}
        for union, dimension in charges:
            candidate = K71.combine(
                candidate,
                PROBE.fixed_union_cap(KPRIME, union, dimension),
            )
            if KPRIME - union - dimension < 0:
                continue
            for support in range(4, min(dimension, 9)):
                value = adjacent_pair(union, dimension, support)
                if support == 4:
                    value = min(
                        value,
                        PROBE.joint45_weighted_cap(
                            KPRIME, union, dimension
                        ),
                    )
                adjacent[support] = min(
                    adjacent.get(support, value), value
                )
        yield name, candidate, tuple(sorted(adjacent.items()))


def price(caps: tuple[int, ...], adjacent: tuple[tuple[int, int], ...]) -> int:
    base = K71.premium(caps)
    edges = dict(adjacent)
    values = [base]
    for width in range(1, len(edges) + 1):
        for selected in itertools.combinations(sorted(edges), width):
            covered = set()
            for edge in selected:
                covered.update((edge, edge + 1))
            if len(covered) != 2 * len(selected):
                continue
            old = sum(
                K71.LEDGER.DEFICITS[support] * caps[support - 2]
                for support in covered
            )
            values.append(base - old + sum(edges[edge] for edge in selected))
    return min(values)


def lane_audit(lane: str) -> dict[str, object]:
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(Q, M)
    _, front23, steps, carrier32, _ = PROBE.position23_group(KPRIME, baseline)
    exact45, _, front45 = K71.exact45_rows(KPRIME, baseline)
    _, high = K71.PARENT.high_group(KPRIME, baseline)
    high = list(reversed(high))
    maximum = (-1, "")
    units = raw_rows = raw_safe = expanded = geometry_rows = 0

    def keep(value: int, label: str) -> None:
        nonlocal maximum
        maximum = max(maximum, (value, label))

    def evaluate(local: tuple[int, ...], prefix: str, cases: dict | None) -> None:
        nonlocal units, raw_rows, raw_safe, expanded, geometry_rows
        units += 1
        raw_max = (-1, "")
        for high_name, high_vector in high:
            raw_max = max(
                raw_max,
                (K71.premium(K71.combine(local, high_vector)), high_name),
            )
            raw_rows += 1
        if cases is None or raw_max[0] <= CEILING:
            if cases is not None:
                raw_safe += 1
            keep(raw_max[0], f"{prefix}/{raw_max[1]}/raw")
            if units % 1000 == 0:
                print(json.dumps({
                    "event": "AUDIT_PROGRESS",
                    "lane": lane,
                    "units": units,
                    "raw_safe_units": raw_safe,
                    "expanded_units": expanded,
                    "current_maximum": maximum[0],
                }, sort_keys=True), flush=True)
            return
        expanded += 1
        for case, candidate, adjacent in charge_options(local, cases):
            for high_name, high_vector in high:
                keep(
                    price(K71.combine(candidate, high_vector), adjacent),
                    f"{prefix}/{high_name}/{case}",
                )
                geometry_rows += 1
        if units % 1000 == 0:
            print(json.dumps({
                "event": "AUDIT_PROGRESS",
                "lane": lane,
                "units": units,
                "raw_safe_units": raw_safe,
                "expanded_units": expanded,
                "current_maximum": maximum[0],
                }, sort_keys=True), flush=True)

    def evaluate_profile(
        local: tuple[int, ...],
        prefix: str,
        adjacent: tuple[tuple[int, int], ...],
    ) -> None:
        nonlocal units, raw_rows, geometry_rows
        units += 1
        for high_name, high_vector in high:
            keep(
                price(K71.combine(local, high_vector), adjacent),
                f"{prefix}/{high_name}/profiled",
            )
            raw_rows += 1
            geometry_rows += 1
        if units % 1000 == 0:
            print(json.dumps({
                "event": "AUDIT_PROGRESS",
                "lane": lane,
                "units": units,
                "raw_safe_units": raw_safe,
                "expanded_units": expanded,
                "current_maximum": maximum[0],
            }, sort_keys=True), flush=True)

    if lane == "ordinary":
        profiles = {}
        plain = {}
        single = []
        infinity = 10**500
        for s2 in reversed(range(Q + 1)):
            for s3 in reversed(range(Q + 1)):
                left_vector = K71.base23_vector(KPRIME, baseline, s2, s3)
                m2, m3 = Q - s2, Q - s3
                if m2 > 0 and m3 > 0 and m3 <= m2:
                    if s2 + s3 < Q:
                        continue
                    b2, b3 = m2 + 1, m3 + 2
                    for name, union, dimension in (
                        ("A23", b2 + b3 - 1, 8),
                        ("T23", b2 + b3, 7),
                    ):
                        candidate = K71.charged_vector(
                            KPRIME, left_vector, union, dimension
                        )
                        adjacent = {}
                        for support in range(4, min(dimension, 9)):
                            value = adjacent_pair(union, dimension, support)
                            if support == 4:
                                value = min(
                                    value,
                                    PROBE.joint45_weighted_cap(
                                        KPRIME, union, dimension
                                    ),
                                )
                            adjacent[support] = value
                        profile = candidate + tuple(
                            adjacent.get(edge, infinity)
                            for edge in range(4, 9)
                        )
                        profiles[profile] = f"s2={s2}/s3={s3}/{name}"
                elif m2 == 0 and m3 > 0:
                    single.append(
                        (s2, s3, left_vector, {"C3": [(m3 + 2, 8)]})
                    )
                elif m3 == 0 and m2 > 0:
                    single.append(
                        (s2, s3, left_vector, {"C2": [(m2 + 1, 9)]})
                    )
                elif m2 == 0 and m3 == 0:
                    plain[left_vector] = f"s2={s2}/s3={s3}/empty"

        for left_name, profile in reversed(K71.maximal_vectors(profiles)):
            left_vector = profile[:len(K71.SUPPORTS)]
            adjacent = tuple(
                (edge, profile[len(K71.SUPPORTS) + edge - 4])
                for edge in range(4, 9)
                if profile[len(K71.SUPPORTS) + edge - 4] < infinity
            )
            for middle_name, middle_vector in reversed(front45):
                evaluate_profile(
                    K71.combine(left_vector, middle_vector),
                    f"{left_name}/{middle_name}/ordinary",
                    adjacent,
                )
        for left_name, left_vector in reversed(K71.maximal_vectors(plain)):
            for middle_name, middle_vector in reversed(front45):
                evaluate(
                    K71.combine(left_vector, middle_vector),
                    f"{left_name}/{middle_name}/ordinary",
                    None,
                )
        for s2, s3, left_vector, cases in reversed(single):
            for middle_name, middle_vector in reversed(front45):
                evaluate(
                    K71.combine(left_vector, middle_vector),
                    f"s2={s2}/s3={s3}/{middle_name}/ordinary-single",
                    cases,
                )
    else:
        if lane == "carrier32":
            rows = carrier32
        else:
            offset = int(lane[6:])
            rows = []
            for m2 in range(1, Q - offset + 1):
                m3 = m2 + offset
                s2, s3 = Q - m2, Q - m3
                rows.append(
                    (
                        s2,
                        s3,
                        K71.base23_vector(
                            KPRIME, baseline, s2, s3
                        ),
                    )
                )
        for s2, s3, left_vector in reversed(rows):
            m2, m3 = Q - s2, Q - s3
            for s4, s5, middle_vector in reversed(exact45):
                evaluate(
                    K71.combine(left_vector, middle_vector),
                    f"s2={s2}/s3={s3}/s4={s4}/s5={s5}/{lane}",
                    PROBE.mixed_cases(m2, m3 - m2, Q - s4, Q - s5),
                )

    return {
        "event": "AUDIT_LANE",
        "lane": lane,
        "units": units,
        "raw_rows": raw_rows,
        "raw_safe_units": raw_safe,
        "expanded_units": expanded,
        "geometry_rows": geometry_rows,
        "maximum": maximum[0],
        "margin": CEILING - maximum[0],
        "active_branch": maximum[1],
        "complete": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("lanes")
    args = parser.parse_args()
    selected = args.lanes.split(",")
    allowed = {"ordinary", "carrier32"} | {
        f"offset{value}" for value in range(1, 73)
    }
    assert selected and set(selected) <= allowed and len(selected) == len(set(selected))
    print(json.dumps({"event": "AUDIT_START", "ceiling": CEILING, "lanes": selected}), flush=True)
    rows = []
    for lane in selected:
        row = lane_audit(lane)
        rows.append(row)
        print(json.dumps(row, sort_keys=True), flush=True)
    maximum = max((row["maximum"], row["active_branch"]) for row in rows)
    event = "AUDIT_PASS" if maximum[0] <= CEILING else "AUDIT_FAIL"
    print(json.dumps({
        "event": event,
        "maximum": maximum[0],
        "margin": CEILING - maximum[0],
        "active_branch": maximum[1],
        "complete_lanes": len(rows),
    }, sort_keys=True), flush=True)
    raise SystemExit(0 if event == "AUDIT_PASS" else 1)


if __name__ == "__main__":
    main()
