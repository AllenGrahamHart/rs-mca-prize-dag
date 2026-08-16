#!/usr/bin/env python3
"""Complete K'=83 carrier frontier with raw-safe threshold pruning."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import tarfile
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


ROUTER = load_module(
    "k83_threshold_router",
    ROOT
    / "experiments/prize_resolution/rate_half_mca_rank11_k83_stratified56_lane_probe.py",
)
PROBE = ROUTER.PROBE
K71 = ROUTER.K71
KPRIME = 83
Q = KPRIME - 10
M = 67472 + KPRIME
N_CODE = 1048576 + KPRIME


def safe_ceiling() -> int:
    old = K71.LEDGER.row(KPRIME)
    return (
        K71.LEDGER.RECORD_FLOOR * 55 * comb(M, 11)
        - 55 * comb(N_CODE, 11)
        - 55 * int(old["kernel"])
        - int(old["marks"])
        - 1
    ) // K71.LEDGER.RECORD_FLOOR


CEILING = safe_ceiling()


class LaneAudit:
    def __init__(self, lane: str, high: list[tuple[str, tuple[int, ...]]]):
        self.lane = lane
        self.high = high
        self.units = 0
        self.raw_rows = 0
        self.raw_safe_units = 0
        self.expanded_units = 0
        self.geometry_rows = 0
        self.maximum = (-1, "")

    def keep(self, value: int, label: str) -> None:
        self.maximum = max(self.maximum, (value, label))

    def progress(self) -> None:
        if self.units % 1000 == 0:
            print(json.dumps({
                "event": "PROGRESS",
                "lane": self.lane,
                "units": self.units,
                "raw_safe_units": self.raw_safe_units,
                "expanded_units": self.expanded_units,
                "current_maximum": self.maximum[0],
            }, sort_keys=True), flush=True)

    def plain(self, local: tuple[int, ...], prefix: str) -> None:
        self.units += 1
        for high_name, high_vector in self.high:
            caps = K71.combine(local, high_vector)
            self.keep(K71.premium(caps), f"{prefix}/{high_name}/plain")
            self.raw_rows += 1
        self.progress()

    def geometric(self, local: tuple[int, ...], prefix: str, cases: dict) -> None:
        self.units += 1
        raw = (-1, "")
        for high_name, high_vector in self.high:
            caps = K71.combine(local, high_vector)
            raw = max(raw, (K71.premium(caps), high_name))
            self.raw_rows += 1
        if raw[0] <= CEILING:
            self.raw_safe_units += 1
            self.keep(raw[0], f"{prefix}/{raw[1]}/raw-safe")
            self.progress()
            return

        self.expanded_units += 1
        for (candidate, adjacent), case in (
            ROUTER.charged_case_rows_all_adjacent(
                KPRIME, local, cases
            ).items()
        ):
            for high_name, high_vector in self.high:
                caps = K71.combine(candidate, high_vector)
                self.keep(
                    ROUTER.priced_all_adjacent(
                        KPRIME, caps, adjacent
                    ),
                    f"{prefix}/{high_name}/{case}",
                )
                self.geometry_rows += 1
        self.progress()

    def profiled(
        self,
        local: tuple[int, ...],
        prefix: str,
        adjacent: tuple[tuple[int, int], ...],
    ) -> None:
        self.units += 1
        for high_name, high_vector in self.high:
            caps = K71.combine(local, high_vector)
            self.keep(
                ROUTER.priced_all_adjacent(
                    KPRIME, caps, adjacent
                ),
                f"{prefix}/{high_name}/profiled",
            )
            self.raw_rows += 1
            self.geometry_rows += 1
        self.progress()

    def result(self) -> dict[str, object]:
        return {
            "event": "LANE",
            "lane": self.lane,
            "units": self.units,
            "raw_rows": self.raw_rows,
            "raw_safe_units": self.raw_safe_units,
            "expanded_units": self.expanded_units,
            "geometry_rows": self.geometry_rows,
            "maximum": self.maximum[0],
            "margin": CEILING - self.maximum[0],
            "active_branch": self.maximum[1],
            "complete": True,
        }


def replay_lane(lane: str) -> dict[str, object]:
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(Q, M)
    _, front23, steps, carrier32, _ = PROBE.position23_group(KPRIME, baseline)
    exact45, _, front45 = K71.exact45_rows(KPRIME, baseline)
    _, high = K71.PARENT.high_group(KPRIME, baseline)
    audit = LaneAudit(lane, high)

    if lane == "ordinary":
        profiles = {}
        plain = {}
        single = []
        infinity = 10**500
        for s2 in range(Q + 1):
            for s3 in range(Q + 1):
                left_vector = K71.base23_vector(KPRIME, baseline, s2, s3)
                m2, m3 = Q - s2, Q - s3
                if m2 > 0 and m3 > 0 and m3 <= m2:
                    if s2 + s3 < Q:
                        continue
                    b2, b3 = m2 + 1, m3 + 2
                    for name, union, dimension in (
                        ("T23", b2 + b3, 7),
                        ("A23", b2 + b3 - 1, 8),
                    ):
                        candidate = K71.charged_vector(
                            KPRIME, left_vector, union, dimension
                        )
                        adjacent = dict(
                            ROUTER.all_adjacent_caps(
                                KPRIME, [(union, dimension)]
                            )
                        )
                        profile = candidate + tuple(
                            adjacent.get(edge, infinity)
                            for edge in range(4, 9)
                        )
                        profiles[profile] = (
                            f"s2={s2}/s3={s3}/{name}"
                        )
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

        for left_name, profile in K71.maximal_vectors(profiles):
            left_vector = profile[:len(K71.SUPPORTS)]
            adjacent = tuple(
                (edge, profile[len(K71.SUPPORTS) + edge - 4])
                for edge in range(4, 9)
                if profile[len(K71.SUPPORTS) + edge - 4] < infinity
            )
            for middle_name, middle_vector in front45:
                audit.profiled(
                    K71.combine(left_vector, middle_vector),
                    f"{left_name}/{middle_name}/ordinary",
                    adjacent,
                )
        for left_name, left_vector in K71.maximal_vectors(plain):
            for middle_name, middle_vector in front45:
                audit.plain(
                    K71.combine(left_vector, middle_vector),
                    f"{left_name}/{middle_name}/ordinary",
                )
        for s2, s3, left_vector, cases in single:
            for middle_name, middle_vector in front45:
                audit.geometric(
                    K71.combine(left_vector, middle_vector),
                    f"s2={s2}/s3={s3}/{middle_name}/ordinary-single",
                    cases,
                )
        return audit.result()

    if lane == "carrier32":
        rows = carrier32
    else:
        offset = int(lane.removeprefix("offset"))
        rows = []
        for m2 in range(1, Q - offset + 1):
            m3 = m2 + offset
            s2, s3 = Q - m2, Q - m3
            rows.append(
                (s2, s3, K71.base23_vector(KPRIME, baseline, s2, s3))
            )

    for s2, s3, left_vector in rows:
        m2, m3 = Q - s2, Q - s3
        offset = m3 - m2
        for s4, s5, middle_vector in exact45:
            m4, m5 = Q - s4, Q - s5
            cases = PROBE.mixed_cases(m2, offset, m4, m5)
            audit.geometric(
                K71.combine(left_vector, middle_vector),
                f"s2={s2}/s3={s3}/s4={s4}/s5={s5}/{lane}",
                cases,
            )
    return audit.result()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "lanes",
        help="comma-separated ordinary,carrier32,offset1,...,offset72",
    )
    args = parser.parse_args()
    selected = args.lanes.split(",")
    allowed = {"ordinary", "carrier32"} | {
        f"offset{value}" for value in range(1, 73)
    }
    assert selected and set(selected) <= allowed and len(selected) == len(set(selected))
    print(json.dumps({"event": "START", "ceiling": CEILING, "lanes": selected}), flush=True)
    results = []
    for lane in selected:
        result = replay_lane(lane)
        results.append(result)
        print(json.dumps(result, sort_keys=True), flush=True)
    maximum = max((row["maximum"], row["active_branch"]) for row in results)
    conclusion = {
        "event": "PASS" if maximum[0] <= CEILING else "FAIL",
        "maximum": maximum[0],
        "margin": CEILING - maximum[0],
        "active_branch": maximum[1],
        "complete_lanes": len(results),
    }
    print(json.dumps(conclusion, sort_keys=True), flush=True)
    raise SystemExit(0 if conclusion["event"] == "PASS" else 1)


if __name__ == "__main__":
    main()
